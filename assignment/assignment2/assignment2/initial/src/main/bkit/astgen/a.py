from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce


class ASTGeneration(BKITVisitor):

    # //===== PARSER STRUCTURE =====//

    def visitProgram(self, ctx: BKITParser.ProgramContext):
        vars = reduce(lambda x, y: x + self.visit(y),
                      ctx.variableStatement(), [])
        funcs = list(map(lambda x: self.visit(x), ctx.funcDeclaration()))
        return Program(vars + funcs)

    def visitFuncDeclaration(self, ctx: BKITParser.FuncDeclarationContext):
        funcBody = self.visit(ctx.funcBody())
        return FuncDecl(Id("a"), [], funcBody)

    def visitParaList(self, ctx: BKITParser.ParaListContext):
        return self.visitChildren(ctx)

    def visitParameters(self, ctx: BKITParser.ParametersContext):
        return self.visitChildren(ctx)

    def visitFuncBody(self, ctx: BKITParser.FuncBodyContext):
        return self.visit(ctx.statementList())

    # //===== EXPRESSIONS =====//

    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        if ctx.relationalOperator():
            op = self.visit(ctx.relationalOperator())
            left = self.visit(ctx.logicalOrAndExpression(0))
            right = self.visit(ctx.logicalOrAndExpression(1))
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.logicalOrAndExpression())

    def visitLogicalOrAndExpression(self, ctx: BKITParser.LogicalOrAndExpressionContext):
        if ctx.logicalOrAndOperator():
            op = self.visit(ctx.logicalOrAndOperator())
            left = self.visit(ctx.logicalOrAndExpression(0))
            right = self.visit(ctx.additiveExpression(1))
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.logicalOrAndExpression())

    def visitAdditiveExpression(self, ctx: BKITParser.AdditiveExpressionContext):
        if ctx.relationalOperator():
            op = self.visit(ctx.additiveOperator())
            left = self.visit(ctx.additiveExpression(0))
            right = self.visit(ctx.additiveExpression(1))
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.logicalOrAndExpression())

    def visitMultiplicativeExpression(self, ctx: BKITParser.MultiplicativeExpressionContext):
        if ctx.relationalOperator():
            op = self.visit(ctx.relationalOperator())
            left = self.visit(ctx.logicalOrAndExpression(0))
            right = self.visit(ctx.logicalOrAndExpression(1))
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.logicalOrAndExpression())

    def visitLogicalNotExpression(self, ctx: BKITParser.LogicalNotExpressionContext):
        return self.visitChildren(ctx)

    def visitSignExpression(self, ctx: BKITParser.SignExpressionContext):
        return self.visitChildren(ctx)

    def visitIndexExpression(self, ctx: BKITParser.IndexExpressionContext):
        return self.visitChildren(ctx)

    def visitFuncExpression(self, ctx: BKITParser.FuncExpressionContext):
        return self.visitChildren(ctx)

    def visitPrimaryExpression(self, ctx: BKITParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)

    def visitAdditiveOperator(self, ctx: BKITParser.AdditiveOperatorContext):
        return ctx.getChild(0).getText()

    def visitMultiplicativeOperator(self, ctx: BKITParser.MultiplicativeOperatorContext):
        return ctx.getChild(0).getText()

    def visitLogicalOrAndOperator(self, ctx: BKITParser.LogicalOrAndOperatorContext):
        return ctx.getChild(0).getText()

    def visitLogicalNotOperator(self, ctx: BKITParser.LogicalNotOperatorContext):
        return ctx.getChild(0).getText()

    def visitRelationalOperator(self, ctx: BKITParser.RelationalOperatorContext):
        return ctx.getChild(0).getText()

    def visitSignOperator(self, ctx: BKITParser.SignOperatorContext):
        return ctx.getChild(0).getText()

    def visitAssignmentOperator(self, ctx: BKITParser.AssignmentOperatorContext):
        return ctx.getChild(0).getText()

    def visitIndexOperator(self, ctx: BKITParser.IndexOperatorContext):
        return self.visitChildren(ctx)

    def visitFunctionCall(self, ctx: BKITParser.FunctionCallContext):
        return self.visitChildren(ctx)

    def visitArgumentList(self, ctx: BKITParser.ArgumentListContext):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx: BKITParser.StatementContext):
        return self.visitChildren(ctx)

    # //===== STATEMENTS =====//

    def visitStatementList(self, ctx: BKITParser.StatementListContext):
        vars = reduce(lambda x, y: x + self.visit(y),
                      ctx.variableStatement(), [])
        stmts = list(map(lambda x: self.visit(x), ctx.statement()))
        return (vars, stmts)

    def visitExpressionStatement(self, ctx: BKITParser.ExpressionStatementContext):
        return self.visitChildren(ctx)

    def visitVariableStatement(self, ctx: BKITParser.VariableStatementContext):
        return [VarDecl(Id("a"), [], IntLiteral(1)), VarDecl(Id("b"), [1, 2], None)]

    def visitVarList(self, ctx: BKITParser.VarListContext):
        return self.visitChildren(ctx)

    def visitVarDeclaration(self, ctx: BKITParser.VarDeclarationContext):
        return self.visitChildren(ctx)

    def visitAssignmentStatement(self, ctx: BKITParser.AssignmentStatementContext):
        return self.visitChildren(ctx)

    def visitAssignDeclaration(self, ctx: BKITParser.AssignDeclarationContext):
        return self.visitChildren(ctx)

    def visitIfStatement(self, ctx: BKITParser.IfStatementContext):
        return self.visitChildren(ctx)

    def visitIterationStatement(self, ctx: BKITParser.IterationStatementContext):
        return self.visitChildren(ctx)

    def visitForStatement(self, ctx: BKITParser.ForStatementContext):
        return self.visitChildren(ctx)

    def visitForCondition(self, ctx: BKITParser.ForConditionContext):
        return self.visitChildren(ctx)

    def visitForDeclaration(self, ctx: BKITParser.ForDeclarationContext):
        return self.visitChildren(ctx)

    def visitConditionExpr(self, ctx: BKITParser.ConditionExprContext):
        return self.visitChildren(ctx)

    def visitUpdateExpr(self, ctx: BKITParser.UpdateExprContext):
        return self.visitChildren(ctx)

    def visitWhileStatement(self, ctx: BKITParser.WhileStatementContext):
        return self.visitChildren(ctx)

    def visitDoWhileStatement(self, ctx: BKITParser.DoWhileStatementContext):
        return self.visitChildren(ctx)

    def visitJumpStatement(self, ctx: BKITParser.JumpStatementContext):
        return self.visitChildren(ctx)

    def visitBreakStatement(self, ctx: BKITParser.BreakStatementContext):
        return Break()

    def visitContinueStatement(self, ctx: BKITParser.ContinueStatementContext):
        return self.visitChildren(ctx)

    def visitCallStatement(self, ctx: BKITParser.CallStatementContext):
        return self.visitChildren(ctx)

    def visitReturnStatement(self, ctx: BKITParser.ReturnStatementContext):
        return self.visitChildren(ctx)

    def visitLiterals(self, ctx: BKITParser.LiteralsContext):
        return (
            IntLiteral(int(ctx.IntegerConstant().getText())) if ctx.IntegerConstant() else
            FloatLiteral(float(ctx.FloatingConstant().getText())) if ctx.FloatingConstant() else
            StringLiteral(ctx.String().getText()) if ctx.String() else
            self.visitChildren(ctx)
        )

    def visitBoolean(self, ctx: BKITParser.BooleanContext):
        return BooleanLiteral(True if ctx.TRUE() else False)

    def visitArray(self, ctx: BKITParser.ArrayContext):
        return ArrayLiteral(list(map(lambda child: self.visit(child), ctx.literals())))
