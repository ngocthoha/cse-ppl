from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce

def stoi(x):
    if '0o' in x or '0O' in x: return int(x, 8)
    elif '0x' in x or '0X' in x: return int(x, 16)
    else: return int(x)

class ASTGeneration(BKITVisitor):
    # //===== PARSER STRUCTURE =====//
    #program  :variableStatement* funcDeclaration* EOF;
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        VarDecl = reduce(lambda x, y: x + self.visit(y), ctx.variableStatement(), [])
        FunDecl = list(map(lambda x: self.visit(x), ctx.funcDeclaration()))
        return Program( VarDecl + FunDecl)

    # variableStatement: VAR COLON varList SEMI;
    def visitVariableStatement(self, ctx:BKITParser.VariableStatementContext):
        return self.visit(ctx.varList())

    # varList: varDeclaration (COMMA varDeclaration)*;
    def visitVarList(self, ctx:BKITParser.VarListContext):
        return [self.visit(x) for x in ctx.varDeclaration()]

    # varDeclaration: Identifier (LSB IntegerConstant RSB)* (ASSIGN literals)?;
    def visitVarDeclaration(self, ctx:BKITParser.VarDeclarationContext):
        return VarDecl(
            Id(ctx.Identifier().getText()),
            [stoi(x.getText()) for x in ctx.IntegerConstant()] if ctx.IntegerConstant() else [],
            self.visit(ctx.literals()) if ctx.ASSIGN() else None
        )
    # funcDeclaration: FUNCTION COLON Identifier (PARAMETER COLON paraList)? funcBody;
    def visitFuncDeclaration(self, ctx:BKITParser.FuncDeclarationContext):
        return FuncDecl(
            Id(ctx.Identifier().getText()),
            self.visit(ctx.paraList()) if ctx.paraList() else [],
            self.visit(ctx.funcBody())
        )
    # paraList: parameters (COMMA parameters)*;
    def visitParaList(self, ctx:BKITParser.ParaListContext):
        return reduce(lambda x, y: x + self.visit(y), ctx.parameters(), [])
    
    # parameters: Identifier (LSB IntegerConstant RSB)*;
    def visitParameters(self, ctx:BKITParser.ParametersContext):
        return [VarDecl(
            Id(ctx.Identifier().getText()),
            [stoi(x.getText()) for x in ctx.IntegerConstant()] if ctx.IntegerConstant() else [],
            None
        )]


    # funcBody: BODY COLON statementList ENDBODY DOT;
    def visitFuncBody(self, ctx:BKITParser.FuncBodyContext):
        return self.visit(ctx.statementList())
    # //===== STATEMENTS =====//
    # variableStatement* statement*
    def visitStatementList(self, ctx:BKITParser.StatementListContext):
        VarList = reduce(lambda x, y: x + self.visit(y), ctx.variableStatement(), [])
        StaList = reduce(lambda x, y: x + self.visit(y), ctx.statement(), [])
        return (VarList, StaList)

    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:BKITParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignDeclaration.
    def visitAssignDeclaration(self, ctx:BKITParser.AssignDeclarationContext):
        return self.visitChildren(ctx)


    # IF expression THEN statementList (ELSEIF expression THEN statementList)* (ELSE statementList)? ENDIF DOT
    def visitIfStatement(self, ctx:BKITParser.IfStatementContext):
        return [If(
            [
                (
                    self.visit(ctx.expression(0)),
                    [self.visitVariableStatement(ctx.v)],
                    []
                )
            ],
            (
                [],
                []
            )
        )]


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


    # functionCall SEMI
    def visitCallStatement(self, ctx:BKITParser.CallStatementContext):
        return self.visit(ctx.functionCall())

    # Identifier LB argumentList? RB
    def visitFunctionCall(self, ctx:BKITParser.FunctionCallContext):
        return [CallStmt(
            Id(ctx.Identifier().getText()),
            [] if ctx.argumentList() else []
        )]

    # argumentList COMMA expression | expression
    def visitArgumentList(self, ctx:BKITParser.ArgumentListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKITParser#returnStatement.
    def visitReturnStatement(self, ctx:BKITParser.ReturnStatementContext):
        return self.visitChildren(ctx)

    # //===== EXPRESSIONS =====//
    # logicalOrAndExpression relationalOperator logicalOrAndExpression | logicalOrAndExpression 
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        if ctx.relationalOperator():
            op = self.visit(ctx.relationalOperator())
            left = self.visit(ctx.logicalOrAndExpression(0))
            right = self.visit(ctx.logicalOrAndExpression(1))
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.logicalOrAndExpression(0))

    # Visit a parse tree produced by BKITParser#relationalOperator.
    def visitRelationalOperator(self, ctx:BKITParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # logicalOrAndExpression logicalOrAndOperator additiveExpression | additiveExpression
    def visitLogicalOrAndExpression(self, ctx:BKITParser.LogicalOrAndExpressionContext):
        if ctx.logicalOrAndOperator():
            op = self.visit(ctx.logicalOrAndOperator())
            left = self.visit(ctx.logicalOrAndExpression())
            right = self.visit(ctx.additiveExpression(0))
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.additiveExpression())


    # logicalOrAndOperator.
    def visitLogicalOrAndOperator(self, ctx:BKITParser.LogicalOrAndOperatorContext):
        return self.visitChildren(ctx)


    # additiveExpression additiveOperator multiplicativeExpression | multiplicativeExpression
    def visitAdditiveExpression(self, ctx:BKITParser.AdditiveExpressionContext):
        if ctx.additiveOperator():
            op = self.visit(ctx.additiveOperator())
            left = self.visit(ctx.additiveExpression())
            right = self.visit(ctx.multiplicativeExpression(0))
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.multiplicativeExpression())

    # Visit a parse tree produced by BKITParser#additiveOperator.
    def visitAdditiveOperator(self, ctx:BKITParser.AdditiveOperatorContext):
        return self.visitChildren(ctx)


    # multiplicativeExpression multiplicativeOperator logicalNotExpression | logicalNotExpression
    def visitMultiplicativeExpression(self, ctx:BKITParser.MultiplicativeExpressionContext):
        if ctx.multiplicativeOperator():
            op = self.visit(ctx.multiplicativeOperator())
            left = self.visit(ctx.multiplicativeExpression())
            right = self.visit(ctx.logicalNotExpression())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.logicalNotExpression())
        

    # multiplicativeOperator.
    def visitMultiplicativeOperator(self, ctx:BKITParser.MultiplicativeOperatorContext):
        return self.visitChildren(ctx)


    # NOT logicalNotExpression | signExpression
    def visitLogicalNotExpression(self, ctx:BKITParser.LogicalNotExpressionContext):
        if ctx.NOT():
            return UnaryOp(self.visit(ctx.NOT()), self.visit(ctx.logicalNotExpression()))
        else:
            return self.visit(ctx.signExpression())

    # signOperator signExpression | indexExpression
    def visitSignExpression(self, ctx:BKITParser.SignExpressionContext):
        if ctx.signOperator():
            return UnaryOp(self.visit(ctx.signOperator(), self.visit(ctx.signExpression())))
        else:
            return self.visit(ctx.indexExpression())

    # SUB | SUBF
    def visitSignOperator(self, ctx:BKITParser.SignOperatorContext):
        return self.visitChildren(ctx)


    # indexExpression indexOperator | funcExpression
    def visitIndexExpression(self, ctx:BKITParser.IndexExpressionContext):
        if ctx.indexOperator():
            return UnaryOp(self.visit(ctx.indexOperator()), self.visit(ctx.indexExpression))
        else:
            return self.visit(ctx.funcExpression())


    # LSB expression RSB
    def visitIndexOperator(self, ctx:BKITParser.IndexOperatorContext):
        return self.visit(ctx.expression())


    # primaryExpression LSB expression RSB | primaryExpression
    def visitFuncExpression(self, ctx:BKITParser.FuncExpressionContext):
        if ctx.expression():
            return UnaryOp(self.visit(ctx.expression()), self.visit(ctx.primaryExpression(0)))
        else:
            return self.visit(ctx.primaryExpression())


    #primaryExpression.
    def visitPrimaryExpression(self, ctx:BKITParser.PrimaryExpressionContext):
        if ctx.expression(): return self.visit(ctx.expression())
        elif ctx.Identifier(): return Id(ctx.Identifier().getText())
        elif ctx.literals(): return self.visit(ctx.literals())
        else: return self.visit(ctx.functionCall())

    
    # Visit a parse tree produced by BKITParser#literals.
    def visitLiterals(self, ctx:BKITParser.LiteralsContext):
        if ctx.IntegerConstant():
            return IntLiteral(stoi(ctx.IntegerConstant().getText())) 
        elif ctx.FloatingConstant():
            return FloatLiteral(float(ctx.FloatingConstant().getText()))
        elif ctx.String():
            return StringLiteral(ctx.String().getText())
        elif ctx.boolean():
            return self.visitBoolean(ctx)
        else:
            return self.visit(ctx.array())

    # Visit a parse tree produced by BKITParser#boolean.
    def visitBoolean(self, ctx:BKITParser.BooleanContext):
        return BooleanLiteral(True if ctx.boolean().getText() == "True" else False)

    # LP literals (COMMA literals)* RP
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return ArrayLiteral([self.visit(x) for x in ctx.literals()])

    # Visit a parse tree produced by BKITParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:BKITParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)

    