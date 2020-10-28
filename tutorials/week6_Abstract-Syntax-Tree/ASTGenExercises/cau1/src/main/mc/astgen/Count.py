from functools import reduce
class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.vardecls())

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return (
            self.visit(ctx.vardecl()) +
            self.visit(ctx.vardecltail())
        )

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) if ctx.vardecl() else []


    def visitVardecl(self,ctx:MPParser.VardeclContext):
        typ = self.visit(ctx.mptype())
        listID = self.visit(ctx.ids())
        return [VarDecl(x, typ) for x in listID]

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return (
            IntType() if ctx.INTTYPE() else
            FloatType()
        )
    #ids: ID ',' ids | ID; 
    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(ctx.ID().getText())] if ctx.getChildCount() == 1 else [Id(ctx.ID().getText())] + self.visit(ctx.ids())