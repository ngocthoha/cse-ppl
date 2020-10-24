from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import reduce

class ASTGeneration(MCVisitor):
    # program: vardecl+ EOF;
    def visitProgram(self, ctx: MCParser.ProgramContext):
        return Program(reduce(lambda x,y: x + self.visit(y), ctx.vardecl(), []))

    # vardecl: mctype manyvar ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        def getType(_type, _dimension):
            return ArrayType(_type, _dimension) if _dimension else _type
        type = self.visit(ctx.mctype())
        vars = self.visit(ctx.manyvar())
        return [VarDecl(getType(type, dimension), id) for id, dimension in vars]

        # return (
        #     list(map(
        #         lambda x, y:
        #             VarDecl(
        #                 ArrayType(self.visit(ctx.mctype()), x) if x else self.visit(ctx.mctype()), y
        #             ),
        #             self.visit(ctx.manyvar()),
        #             self.visit(ctx.manyvar())
        #         )
        #     )
                
        # )

    # mctype: INTTYPE | FLOATTYPE ;
    def visitMctype(self, ctx: MCParser.MctypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    # manyvar: var (COMMA var)* ;
    def visitManyvar(self, ctx: MCParser.ManyvarContext):
        return [self.visit(var) for var in ctx.var()]

    # var: ID (LSB INTLIT RSB)? ;
    def visitVar(self, ctx: MCParser.VarContext):
        return (
            ctx.ID().getText(),
            int(ctx.INTLIT().getText()) if ctx.INTLIT() else None
        )