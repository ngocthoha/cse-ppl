class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(sum([self.visit(var) for var in ctx.vardecl()], []))

    def visitVardecl(self,ctx:MPParser.VardeclContext):
        typ = self.visit(ctx.mptype())
        return [VarDecl(id, typ) for id in self.visit(ctx.ids())]

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(id.getText()) for id in ctx.ID()]
