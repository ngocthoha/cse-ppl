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

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        self.visit(self.ast, None)

    """ Program """

    def visitDecl(self, ast: Decl, param: List[Symbol]):
        declParam = (
            (param, True) if type(ast) is VarDecl else
            param
        )
        return self.visit(ast, declParam)

    def visitProgram(self, ast: Program, param: List[Symbol]):
        reduce(lambda acc, ele: self.visitDecl(ele, acc), ast.decl, [])

    """ Declaration """

    def visitSym(self, symbol, listSym):
        dupSyms = [sym for sym in listSym if symbol.name == sym.name]
        if not dupSyms:
            return listSym + [symbol]
        else:
            raise Redeclared(symbol.kind, symbol.name)

    def visitVarDecl(self, ast: VarDecl, param: Tuple[List[Symbol], bool]):
        listSym, isVariable = param
        kind = Variable() if isVariable else Parameter()
        newSym = Symbol(ast.variable.name, kind)
        return self.visitSym(newSym, listSym)

    def visitFuncDecl(self, ast: FuncDecl, param):
        newSym = Symbol(ast.name.name, Function())
        return self.visitSym(newSym, param)

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
        return None

    def visitFloatLiteral(self, ast: FloatLiteral, param):
        return None

    def visitBooleanLiteral(self, ast: BooleanLiteral, param):
        return None

    def visitStringLiteral(self, ast: StringLiteral, param):
        return None

    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        return None
