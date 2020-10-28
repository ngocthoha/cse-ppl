class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return self.visit(ctx.vardecls())

    def visitVardecls(self, ctx: MPParser.VardeclsContext):

        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        return [] if not ctx.vardecl() else self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        typ = self.visit(ctx.mptype())
        return [VarDecl(id, typ) for id in self.visit(ctx.ids())]

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self, ctx: MPParser.IdsContext):

        return [Id(ctx.ID().getText())] + (self.visit(ctx.ids()) if ctx.ids() else [])
