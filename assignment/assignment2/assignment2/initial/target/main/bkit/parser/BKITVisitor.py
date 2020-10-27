# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variableStatement.
    def visitVariableStatement(self, ctx:BKITParser.VariableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varList.
    def visitVarList(self, ctx:BKITParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varDeclaration.
    def visitVarDeclaration(self, ctx:BKITParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcDeclaration.
    def visitFuncDeclaration(self, ctx:BKITParser.FuncDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paraList.
    def visitParaList(self, ctx:BKITParser.ParaListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameters.
    def visitParameters(self, ctx:BKITParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcBody.
    def visitFuncBody(self, ctx:BKITParser.FuncBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statementList.
    def visitStatementList(self, ctx:BKITParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:BKITParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignDeclaration.
    def visitAssignDeclaration(self, ctx:BKITParser.AssignDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifStatement.
    def visitIfStatement(self, ctx:BKITParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elseIfStatement.
    def visitElseIfStatement(self, ctx:BKITParser.ElseIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#iterationStatement.
    def visitIterationStatement(self, ctx:BKITParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forStatement.
    def visitForStatement(self, ctx:BKITParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forCondition.
    def visitForCondition(self, ctx:BKITParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forDeclaration.
    def visitForDeclaration(self, ctx:BKITParser.ForDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#conditionExpr.
    def visitConditionExpr(self, ctx:BKITParser.ConditionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#updateExpr.
    def visitUpdateExpr(self, ctx:BKITParser.UpdateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#whileStatement.
    def visitWhileStatement(self, ctx:BKITParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:BKITParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#jumpStatement.
    def visitJumpStatement(self, ctx:BKITParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#breakStatement.
    def visitBreakStatement(self, ctx:BKITParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continueStatement.
    def visitContinueStatement(self, ctx:BKITParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callStatement.
    def visitCallStatement(self, ctx:BKITParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#functionCall.
    def visitFunctionCall(self, ctx:BKITParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argumentList.
    def visitArgumentList(self, ctx:BKITParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#returnStatement.
    def visitReturnStatement(self, ctx:BKITParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relationalOperator.
    def visitRelationalOperator(self, ctx:BKITParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logicalOrAndExpression.
    def visitLogicalOrAndExpression(self, ctx:BKITParser.LogicalOrAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logicalOrAndOperator.
    def visitLogicalOrAndOperator(self, ctx:BKITParser.LogicalOrAndOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:BKITParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#additiveOperator.
    def visitAdditiveOperator(self, ctx:BKITParser.AdditiveOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:BKITParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiplicativeOperator.
    def visitMultiplicativeOperator(self, ctx:BKITParser.MultiplicativeOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logicalNotExpression.
    def visitLogicalNotExpression(self, ctx:BKITParser.LogicalNotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#signExpression.
    def visitSignExpression(self, ctx:BKITParser.SignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#signOperator.
    def visitSignOperator(self, ctx:BKITParser.SignOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#indexExpression.
    def visitIndexExpression(self, ctx:BKITParser.IndexExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#indexOperator.
    def visitIndexOperator(self, ctx:BKITParser.IndexOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcExpression.
    def visitFuncExpression(self, ctx:BKITParser.FuncExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:BKITParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literals.
    def visitLiterals(self, ctx:BKITParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#boolean.
    def visitBoolean(self, ctx:BKITParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array.
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:BKITParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)



del BKITParser