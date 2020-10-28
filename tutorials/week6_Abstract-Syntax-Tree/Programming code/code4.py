class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self, ctx: MPParser.ExpContext):
        left = self.visit(ctx.term())
        return (
            left if not ctx.exp() else
            Binary(ctx.ASSIGN().getText(), left, self.visit(ctx.exp()))
        )

    def visitTerm(self, ctx: MPParser.TermContext):
        left = self.visit(ctx.factor(0))
        return (
            left if not ctx.COMPARE() else
            Binary(ctx.COMPARE().getText(), left, self.visit(ctx.factor(1)))
        )

    def visitFactor(self, ctx: MPParser.FactorContext):
        right = self.visit(ctx.operand())
        return (
            right if not ctx.ANDOR() else
            Binary(ctx.ANDOR().getText(), self.visit(ctx.factor()), right)
        )

    def visitOperand(self, ctx: MPParser.OperandContext):
        def stob(value):
            return True if value == "True" else False

        return (
            Id(ctx.ID().getText()) if ctx.ID() else
            IntLiteral(int(ctx.INTLIT().getText())) if ctx.INTLIT() else
            BooleanLiteral(stob(ctx.BOOLIT().getText())) if ctx.BOOLIT() else
            self.visit(ctx.exp())
        )
