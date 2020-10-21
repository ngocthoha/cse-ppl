from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):

    # program: vardecls EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))
    
    # vardecls: vardecl vardecls | vardecl ;
    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        firstVarDecl = self.visit(ctx.vardecl())
        recursive = self.visit(ctx.vardecls()) if ctx.vardecls() else []
        return [firstVarDecl] + recursive

    # vardecl: mctype ids ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        return VarDecl(self.visit(ctx.mctype()), self.visit(ctx.ids()))

  	# mctype: INTTYPE | FLOATTYPE ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    # ids: ID (COMMA ID)* ;
    def visitIds(self,ctx:MCParser.IdsContext):
        return [id.getText() for id in ctx.ID()]