class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return self.visit(ctx.vardecls()) + 1

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) if ctx.vardecl() else 0

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        return self.visit(ctx.mptype()) + self.visit(ctx.ids()) + 1

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return 1

    def visitIds(self, ctx: MPParser.IdsContext):
        return 2 + self.visit(ctx.ids()) if ctx.ids() else 1
