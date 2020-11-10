from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from dataclasses import dataclass
from functools import reduce


class Raiser:
    def __init__(self, e: Exception):
        raise e

@dataclass
class Symbol:
    name: str
    kind: Kind

class StaticChecker(BaseVisitor, Utils):
    # Global Environment
    globalEnv = [
        #Built-in Functions
        Symbol("print", Function()),
        Symbol("printLn", Function()),
        Symbol("printStrLn", Function()),
        Symbol("read", Function()),
    ]
    
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.globalEnv)

    """ Program """

    def visitDecl(self, ast: Decl, param: List[Symbol]):
        declParam = (
            (param, Variable()) if isinstance(ast, VarDecl) else
            param
        )
        return self.visit(ast, declParam)
    # check duplicate name
    def checkIfDuplicate(self, symbol, listSym):
        dupSyms = [sym for sym in listSym if symbol.name == sym.name]
        # if not duplicate return new symbol has symbol is checked
        if not dupSyms:
            return listSym + [symbol]
        # raise exception
        else:
            raise Redeclared(symbol.kind, symbol.name)
    """ Program """
    def visitProgram(self, ast: Program, param: List[Symbol]):
        # Check No Entry Point 
        entry = any([decl for decl in ast.decl if isinstance(decl, FuncDecl) and decl.name.name == "main"])
        if not entry:
            raise NoEntryPoint()
        # Check Redeclared
        # Visit each decl and return list symbol
        globalSym = reduce(lambda acc, ele: self.visitDecl(ele, acc), ast.decl, param)
    
    """ Declaration """
            
    def visitVarDecl(self, ast: VarDecl, param: Tuple[List[Symbol], Kind]):
        # get list symbol, kind from tuple param
        listSym, kind = param
        # create new symbol with kind
        newSym = Symbol(ast.variable.name, kind)
        # check symbol
        return self.checkIfDuplicate(newSym, listSym)

    def visitFuncDecl(self, ast: FuncDecl, param: List[Symbol]):
        # check no entry point
        
        # new symbol with kind function
        newSym = Symbol(ast.name.name, Function())
        # return list symbol with kind param
        listParamSym = reduce (
            lambda acc, ele: self.visit(ele, (acc, Parameter())),
            ast.param, []
        )
        varList, stmtList = ast.body
        # tra ve list symbol moi co gia tri ban dau la list symbol param
        reduce(
            lambda acc, ele: self.visit(ele, (acc, Variable())),
            varList, listParamSym
        )
        return self.checkIfDuplicate(newSym, param)

    def visitBinaryOp(self, ast: BinaryOp, param):
        return None

    def visitUnaryOp(self, ast: UnaryOp, param):
        return None

    def visitCallExpr(self, ast: CallExpr, param):
        return None

    def visitId(self, ast: Id, param):
        return None

    def visitArrayCell(self, ast: ArrayCell, param):
        return None

    def visitAssign(self, ast: Assign, param):
        return None

    def visitIf(self, ast: If, param):
        return None

    def visitFor(self, ast: For, param):
        return None

    def visitContinue(self, ast: Continue, param):
        return None

    def visitBreak(self, ast: Break, param):
        return None

    def visitReturn(self, ast: Return, param):
        return None

    def visitDowhile(self, ast: Dowhile, param):
        return None

    def visitWhile(self, ast: While, param):
        return None

    def visitCallStmt(self, ast: CallStmt, param):
        return None

    def visitIntLiteral(self, ast: IntLiteral, param):
        return IntLiteral()

    def visitFloatLiteral(self, ast: FloatLiteral, param):
        return FloatLiteral()

    def visitBooleanLiteral(self, ast: BooleanLiteral, param):
        return None

    def visitStringLiteral(self, ast: StringLiteral, param):
        return None

    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        return None
