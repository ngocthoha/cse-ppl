from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import reduce 

class ASTGeneration(MCVisitor):
	# exp: term COMPARE term | term ;
    def visitExp(self,ctx:MCParser.ExpContext):
        return (
            Binary(
                ctx.COMPARE().getText(), self.visit(ctx.term(0)), self.visit(ctx.term(1))
            ) if ctx.COMPARE() else
            self.visit(ctx.term(0))
        )

    # term: factor EXPONENT term | factor ;
    def visitTerm(self,ctx:MCParser.TermContext):
        return (
            Binary(
                ctx.EXPONENT().getText(), self.visit(ctx.factor()), self.visit(ctx.term())
            ) if ctx.EXPONENT() else
            self.visit(ctx.factor())
        )

    # factor: operand (ANDOR operand)* ; 
    def visitFactor(self,ctx:MCParser.FactorContext):
        listFactor = zip(ctx.ANDOR(), ctx.operand()[1:])
        return (
            reduce(
            lambda x,y: Binary(y[0].getText(), x, self.visit(y[1])),
            listFactor,
            self.visit(ctx.operand(0))
            )
        )
  
  	# operand: INTLIT | BOOLIT | LB exp RB ;
    def visitOperand(self,ctx:MCParser.OperandContext):
        return (
            IntLit(
                int(ctx.INTLIT().getText())
            ) if ctx.INTLIT() else
            BoolLit(
                True if (ctx.BOOLIT().getText() == "true") else False
            ) if ctx.BOOLIT() else
            self.visit(ctx.exp())
        )