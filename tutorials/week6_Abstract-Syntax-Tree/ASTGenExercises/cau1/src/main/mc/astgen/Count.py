from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class Count(MCVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return self.visit(ctx.vardecls()) + 1

    # vardecls: vardecl vardecls | vardecl ;
    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        recur = self.visit(ctx.vardecls()) if ctx.vardecls() else 0;
        return self.visit(ctx.vardecl()) + recur
        
    # vardecl: mctype ids SEMI ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        return self.visit(ctx.mctype()) + self.visit(ctx.ids()) + 1

    # mctype: INTTYPE | FLOATTYPE | ARRAY LB INTLIT RB OF mctype ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        return self.visit(ctx.mctype()) + ctx.getChildCount() - 1 if ctx.ARRAY() else 1

    # ids: ID (COMMA ID)* ;
    def visitIds(self,ctx:MCParser.IdsContext):
        return 1 + len(ctx.COMMA()) * 2

