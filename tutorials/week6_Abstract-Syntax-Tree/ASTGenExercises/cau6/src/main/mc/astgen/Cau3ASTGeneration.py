from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import reduce

class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return self.vist(ctx.exp())
    # exp: (term ASSIGN)* term;
    # 1 := 2 += 3
    # opts = [:=, +=] => [+=, :=]
    # oprs = [1,2,3] => [3,2,1]
    # zip(opts, oprs[1:]) = (+=, 2) (:=, 1)
    # Binary(+=, 2, 3)
    def visitExp(self, ctx: MPParser.ExpContext):
        operators = [opt.getText() for opt in ctx.ASSIGN()][::-1]
        operands = [self.visit(opr) for opr in ctx.term()][::-1]
        return reduce(
            lambda x, y: Binary(y[0], y[1], x),
            zip(operators, operands[1:]), operands[0]
        )

    def visitTerm(self, ctx: MPParser.TermContext):
        return (
            Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1))) if ctx.COMPARE() else
            self.visit(ctx.factor(0))
        )
    # factor: operand (ANDOR operand)* ;
    def visitFactor(self, ctx: MPParser.FactorContext):
        operators = [opt.getText() for opt in ctx.ANDOR()]
        operands = [self.visit(opr) for opr in ctx.operand()]
        return reduce(
            lambda x, y: Binary(y[0], x, y[1]),
            zip(operators, operands[1:]), operands[0]
        )

    def visitOperand(self, ctx: MPParser.OperandContext):
        return (
            Id(ctx.ID().getText()) if ctx.ID() else
            IntLiteral(int(ctx.INTLIT().getText())) if ctx.INTLIT() else
            BooleanLiteral(True if ctx.BOOLIT().getText() == "True" else False) if ctx.BOOLIT() else
            self.visit(ctx.exp())
        )
