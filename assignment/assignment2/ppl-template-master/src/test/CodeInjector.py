from typing import *
import os
import sys
import tokenize
from token import *
import shutil
import abc

LEXER = 1
PARSER = 2


class Template:
    @staticmethod
    def lexer(id: int):
        return [
            "\n",
            "    def test_%d(self):\n" % id,
            "        input = r\"\"\"  \"\"\"\n",
            "        expect = r\"\"\"<EOF>\"\"\"\n",
            "        self.assertTrue(TestLexer.checkLexeme(input, expect, %d))\n" % id
        ]

    @staticmethod
    def parser(id: int):
        return [
            "\n",
            "    def test_%d(self):\n" % id,
            "        input = r\"\"\"\n\n",
            "\"\"\"\n",
            "        expect = r\"\"\"successful\"\"\"\n",
            "        self.assertTrue(TestParser.checkParser(input, expect, %d))\n" % id
        ]

    @staticmethod
    def astgen(id: int):
        return [
            "\n",
            "    def test_%d(self):\n" % id,
            "        input = r\"\"\"\n\n",
            "\"\"\"\n",
            "        expect = Program([])\n",
            "        self.assertTrue(TestAST.checkASTGen(input, expect, %d))\n" % id
        ]


class CodeInjector:

    __caseIds: List[int]
    targetPath: str
    target: int
    injector: Any
    templateEngine: Any
    fill: bool = False
    modeOn: bool = False

    def setup(self):
        magicString = os.environ.get('PPL_MAGIC_STRING')
        option = os.environ.get('PPL_OPTION')
        maxCount = os.environ.get('PPL_COUNT')

        # Select target and injector
        if magicString == "l3x3r5u173":
            start = 101
            self.target = LEXER
            self.targetPath = "./test/LexerSuite.py"
            self.injector = self.__stringExpectInjector
            self.templateEngine = Template.lexer
        elif magicString == "p4r53r5u173":
            start = 201
            self.target = PARSER
            self.targetPath = "./test/ParserSuite.py"
            self.injector = self.__stringExpectInjector
            self.templateEngine = Template.parser
        elif magicString == "45763n5u173":
            start = 301
            self.target = PARSER
            self.targetPath = "./test/ASTGenSuite.py"
            self.injector = self.__astInjector
            self.templateEngine = Template.astgen
            sys.path.remove('./main/bkit/ast/')
            sys.path.append('./test/astfake/')
        else:
            return

        if option == "f1ll":
            self.fill = True

        lines, tokens = self.__getTarget(self.targetPath)

        defTokenIndexs = []

        for i in range(len(tokens)):
            if tokens[i].type == NAME and tokens[i].string == "def":
                defTokenIndexs.append(i)

        count = 0
        for i in defTokenIndexs:
            id = start + count
            targetTokenId = self.__searchTokenId(id, tokens, i)
            self.__stringReplace("test_" + str(id), lines, tokens[i + 1])
            self.__stringReplace(str(id), lines, tokens[targetTokenId])
            count += 1

        if self.fill:
            try:
                maxCount = int(maxCount)
            except:
                maxCount = 100
            while count < (maxCount if maxCount <= 100 else 100):
                lines.extend(self.templateEngine(start + count))
                count += 1
        self.__caseIds = list(range(start, start + count))

        self.__backup(self.targetPath)
        self.__dump(self.targetPath, lines)
        self.modeOn = True

    def inject(self):
        if not self.modeOn:
            sys.exit(0)

        self.__backup(self.targetPath)
        tempPath = self.targetPath.replace(".py", ".temp.py")
        shutil.copyfile(self.targetPath, tempPath)

        # Inject code for each testcase
        for id in self.__caseIds:
            lines, tokens = self.__getTarget(tempPath)
            solution = self.__getSolution(id)
            self.injector(id, solution, lines, tokens)
            self.__dump(tempPath, lines)
        shutil.copyfile(tempPath, self.targetPath)

    def __getSolution(self, id: int):
        with open("./test/solutions/" + str(id) + ".txt") as f:
            return f.readline()

    def __getTarget(self, targetPath: str):
        with tokenize.open(targetPath) as f:
            tokens = list(tokenize.generate_tokens(f.readline))
            f.seek(0)
            lines = f.readlines()
        return (lines, tokens)

    def __dump(self, targetPath: str, lines):
        with open(targetPath, "w") as f:
            f.writelines(lines)

    def __backup(self, targetPath: str):
        backupPath = targetPath.replace(".py", ".bak.py")
        if not os.path.isfile(backupPath):
            shutil.copyfile(targetPath, backupPath)

    def __stringExpectInjector(self, id: int, solution: str, lines: List[str], tokens: List[tokenize.TokenInfo]):
        targetTokenId = self.__searchTokenId(id, tokens)

        token = tokens[targetTokenId]
        while token.type != STRING:
            targetTokenId = targetTokenId - 1
            token = tokens[targetTokenId]

        # Escape string
        if solution[0] == '"' or solution[-1] in ['\\', '"'] in solution:
            newSolution = '"' + \
                solution.replace('\\', '\\\\').replace('"', '\\"') + '"'
        else:
            newSolution = 'r"""' + solution + '"""'

        return self.__stringReplace(newSolution, lines, token)

    def __astInjector(self, id: int, solution: str, lines: List[str], tokens: List[tokenize.TokenInfo]):
        targetTokenId = self.__searchTokenId(id, tokens)

        # Find token "=" after "expect"
        i = targetTokenId
        token = tokens[i]
        while token.type != OP or token.string != "=":
            i = i - 1
            token = tokens[i]
        startToken = tokens[i + 1]

        # Find last token of ast
        i = targetTokenId
        token = tokens[i]
        while token.type != NAME or token.string != "self":
            i = i - 1
            token = tokens[i]
        i = i - 1
        token = tokens[i]
        while token.type == INDENT or token.type == NEWLINE:
            i = i - 1
            token = tokens[i]
        lastToken = tokens[i]

        startRow, endRow, startCol, endCol = startToken.start[0] - \
            1, lastToken.end[0] - 1, startToken.start[1], lastToken.end[1]
        newSolution = solution if solution else "Program([])"
        return self.__replace(newSolution, lines, startRow, endRow, startCol, endCol)

    """ Replace """

    def __stringReplace(self, value: str, lines: List[str], token: tokenize.TokenInfo):
        startRow, endRow, startCol, endCol = token.start[0] - \
            1, token.end[0] - 1, token.start[1], token.end[1]

        return self.__replace(value, lines, startRow, endRow, startCol, endCol)

    def __replace(self, value: str, lines: List[str], startRow, endRow, startCol, endCol):
        # Same row
        if startRow == endRow:
            line = lines[startRow]
            lines[startRow] = line[0:startCol] + value + line[endCol:]
        else:
            # To do
            line = lines[startRow]
            lines[startRow] = line[0:startCol] + value + "\n"
            lines[endRow] = lines[endRow][endCol + 1:]
            tempLines = list(lines)
            lines.clear()
            lines.extend(tempLines[0:startRow + 1])
            lines.extend(tempLines[endRow:])
        return lines

    def __searchTokenId(self, id: int, tokens: List[tokenize.TokenInfo], start=None):
        defTokenIndex = self.getDefTokens(tokens)
        if start is None:
            start = defTokenIndex[(id - 1) % 100]

        for i, token in enumerate(tokens):
            if i > start and token.type == NUMBER:
                assertToken = tokens[i - 10]
                if assertToken.type == NAME and assertToken.string == "assertTrue":
                    return i

    def getDefTokens(self, tokens):
        defTokenIndexs = []
        for i in range(len(tokens)):
            if tokens[i].type == NAME and tokens[i].string == "def":
                defTokenIndexs.append(i)
        return defTokenIndexs
