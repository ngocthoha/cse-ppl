from antlr4 import *
import unittest
import subprocess
import sys
import os
sys.path.append('./test/')

# Make sure that ANTLR_JAR is set to antlr-4.8-complete.jar
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET = '../target/main/bkit/parser' if os.name == 'posix' else os.path.normpath(
    '../target/')
locpath = ['./main/bkit/parser/', './main/bkit/astgen/', './main/bkit/utils/']
locpath = locpath + ['./main/bkit/ast/']
for p in locpath:
    if not p in sys.path:
        sys.path.append(p)


def main(argv):
    global ANTLR_JAR, TARGET
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        subprocess.run(["java", "-jar", ANTLR_JAR, "-o", "../target",
                        "-no-listener", "-visitor", "main/bkit/parser/BKIT.g4"])
    elif argv[0] == 'clean':
        subprocess.run(["rm", "-rf", "../target/main"])
    elif argv[0] == 'test':

        # Injector setup start
        from CodeInjector import CodeInjector
        injector = CodeInjector()
        injector.setup()
        # Injector setup end

        if os.path.isdir(TARGET) and not TARGET in sys.path:
            sys.path.append(TARGET)
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'LexerSuite':
            from LexerSuite import LexerSuite
            suite = unittest.makeSuite(LexerSuite)
            test(suite)
        elif argv[1] == 'ParserSuite':
            from ParserSuite import ParserSuite
            suite = unittest.makeSuite(ParserSuite)
            test(suite)
        elif argv[1] == 'ASTGenSuite':
            from ASTGenSuite import ASTGenSuite
            suite = unittest.makeSuite(ASTGenSuite)
            test(suite)
        else:
            printUsage()

        # Injector inject start
        injector.inject()
        # Injector inject end

    else:
        printUsage()


def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())


def printUsage():
    print("python3 run.py gen")
    print("python3 run.py test LexerSuite")
    print("python3 run.py test ParserSuite")
    print("python3 run.py test ASTGenSuite")


if __name__ == "__main__":
    main(sys.argv[1:])
