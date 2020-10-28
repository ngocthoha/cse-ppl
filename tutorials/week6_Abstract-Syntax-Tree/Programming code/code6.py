from functools import reduce


class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self, ctx: MPParser.ExpContext):
        opts = [opt.getText() for opt in ctx.ASSIGN()][::-1]
        oprs = [self.visit(opr) for opr in ctx.term()][::-1]
        return reduce(
            lambda acc, ele: Binary(ele[0], ele[1], acc),
            zip(opts, oprs[1:]), oprs[0]
        )

    def visitTerm(self, ctx: MPParser.TermContext):
        left = self.visit(ctx.factor(0))
        return (
            left if not ctx.COMPARE() else
            Binary(ctx.COMPARE().getText(), left, self.visit(ctx.factor(1)))
        )

    def visitFactor(self, ctx: MPParser.FactorContext):
        opts = [opt.getText() for opt in ctx.ANDOR()]
        oprs = [self.visit(opr) for opr in ctx.operand()]
        return reduce(
            lambda acc, ele: Binary(ele[0], acc, ele[1]),
            zip(opts, oprs[1:]), oprs[0]
        )

    def visitOperand(self, ctx: MPParser.OperandContext):
        return (
            Id(ctx.ID().getText()) if ctx.ID() else
            IntLiteral(int(ctx.INTLIT().getText())) if ctx.INTLIT() else
            BooleanLiteral(True if ctx.BOOLIT().getText() == "True" else False) if ctx.BOOLIT() else
            self.visit(ctx.exp())
        )
