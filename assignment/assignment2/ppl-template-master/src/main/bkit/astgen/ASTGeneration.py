from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce


class ASTGeneration(BKITVisitor):
    # //===== PARSER STRUCTURE =====//
    #program  :variableStatement* funcDeclaration* EOF;
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        varDecls = sum([self.visit(var) for var in ctx.variableStatement()], [])
        funcDecls = [self.visit(func) for func in ctx.funcDeclaration()]
        return Program(varDecls + funcDecls)

    # variableStatement: VAR COLON varList SEMI;
    def visitVariableStatement(self, ctx: BKITParser.VariableStatementContext):
        return self.visit(ctx.varList())

    # varList: varDeclaration (COMMA varDeclaration)*;
    def visitVarList(self, ctx: BKITParser.VarListContext):
        return [self.visit(x) for x in ctx.varDeclaration()]

    # varDeclaration: Identifier (LSB IntegerConstant RSB)* (ASSIGN literals)?;
    def visitVarDeclaration(self, ctx: BKITParser.VarDeclarationContext):
        ids = [self.stoi(x.getText()) for x in ctx.IntegerConstant()]
        return VarDecl(
            Id(ctx.Identifier().getText()), ids,
            self.visit(ctx.literals()) if ctx.ASSIGN() else None
        )

    # funcDeclaration: FUNCTION COLON Identifier (PARAMETER COLON paraList)? funcBody;
    def visitFuncDeclaration(self, ctx: BKITParser.FuncDeclarationContext):
        return FuncDecl(
            Id(ctx.Identifier().getText()),
            self.visit(ctx.paraList()) if ctx.paraList() else [],
            self.visit(ctx.funcBody())
        )

    # paraList: parameters (COMMA parameters)*;
    def visitParaList(self, ctx: BKITParser.ParaListContext):
        return [self.visit(param) for param in ctx.parameters()]

    # parameters: Identifier (LSB IntegerConstant RSB)*;
    def visitParameters(self, ctx: BKITParser.ParametersContext):
        return VarDecl(
            Id(ctx.Identifier().getText()),
            [self.stoi(x.getText()) for x in ctx.IntegerConstant()
             ] if ctx.IntegerConstant() else [],
            None
        )

    # funcBody: BODY COLON statementList ENDBODY DOT;
    def visitFuncBody(self, ctx: BKITParser.FuncBodyContext):
        return self.visit(ctx.statementList())

    # //===== STATEMENTS =====//
    # variableStatement* statement*
    def visitStatementList(self, ctx: BKITParser.StatementListContext):
        varList = sum([self.visit(var) for var in ctx.variableStatement()], [])
        staList = [self.visit(sta) for sta in ctx.statement()]
        return (varList, staList)

    # statement.
    def visitStatement(self, ctx: BKITParser.StatementContext):
        return self.visitChildren(ctx)

    # assignDeclaration ASSIGN expression SEMI;
    def visitAssignmentStatement(self, ctx: BKITParser.AssignmentStatementContext):
        lhs = self.visit(ctx.assignDeclaration())
        rhs = self.visit(ctx.expression())
        return Assign(lhs, rhs)

    # (Identifier | functionCall) indexOperator*;
    def visitAssignDeclaration(self, ctx: BKITParser.AssignDeclarationContext):
        idFunc, expFunc = self.visit(ctx.functionCall()) if ctx.functionCall() else (None, [])
        lhs = Id(ctx.Identifier().getText()) if ctx.Identifier() else CallExpr(idFunc, expFunc)
        return (
            lhs if not ctx.indexOperator() else
            ArrayCell(
                lhs, [self.visit(x) for x in ctx.indexOperator()]
            )
        )

    # IF expression THEN statementList elseIfStatement* (ELSE statementList)? ENDIF DOT
    def visitIfStatement(self, ctx: BKITParser.IfStatementContext):
        ifExpr = self.visit(ctx.expression())
        elseStmt = self.visit(ctx.statementList(1)) if ctx.ELSE() else ([], [])
        varList, staList = self.visit(ctx.statementList(0))
        ifStmt = (ifExpr, varList, staList)
        elseIfStmt = [self.visit(sta) for sta in ctx.elseIfStatement()]
        ifThen = [ifStmt] + elseIfStmt
        return If(ifThen, elseStmt)

    # elseIfStatement
    def visitElseIfStatement(self, ctx: BKITParser.ElseIfStatementContext):
        ifExpr = self.visit(ctx.expression())
        varlist, stalist = self.visit(ctx.statementList())
        return (ifExpr, varlist, stalist)

    # iterationStatement.
    def visitIterationStatement(self, ctx: BKITParser.IterationStatementContext):
        return self.visitChildren(ctx)

    # FOR LB forCondition RB DO statementList ENDFOR DOT
    def visitForStatement(self, ctx: BKITParser.ForStatementContext):
        id1, expr1, expr2, expr3 = self.visit(ctx.forCondition())
        listDecls = self.visit(ctx.statementList())
        return For(id1, expr1, expr2, expr3, listDecls)

    # forDeclaration COMMA conditionExpr? COMMA updateExpr?
    def visitForCondition(self, ctx: BKITParser.ForConditionContext):
        ids, expr = self.visit(ctx.forDeclaration())
        return (
            ids,
            expr,
            self.visit(ctx.conditionExpr()) if ctx.conditionExpr() else None,
            self.visit(ctx.updateExpr()) if ctx.updateExpr() else None
        )

    # Identifier ASSIGN expression;
    def visitForDeclaration(self, ctx: BKITParser.ForDeclarationContext):
        return (
            Id(ctx.Identifier().getText()),
            self.visit(ctx.expression())
        )

    # conditionExpr: expression;
    def visitConditionExpr(self, ctx: BKITParser.ConditionExprContext):
        return self.visitChildren(ctx)

    # updateExpr: expression;
    def visitUpdateExpr(self, ctx: BKITParser.UpdateExprContext):
        return self.visitChildren(ctx)

    # WHILE expression DO statementList ENDWHILE DOT
    def visitWhileStatement(self, ctx: BKITParser.WhileStatementContext):
        expr = self.visit(ctx.expression())
        staList = self.visit(ctx.statementList())
        return While(expr, staList)

    # DO statementList WHILE expression ENDDO DOT
    def visitDoWhileStatement(self, ctx: BKITParser.DoWhileStatementContext):
        staList = self.visit(ctx.statementList())
        expr = self.visit(ctx.expression())
        return Dowhile(staList, expr)

    # jumpStatement.
    def visitJumpStatement(self, ctx: BKITParser.JumpStatementContext):
        return self.visitChildren(ctx)

    # breakStatement.
    def visitBreakStatement(self, ctx: BKITParser.BreakStatementContext):
        return Break()

    # Visit a parse tree produced by BKITParser#continueStatement.
    def visitContinueStatement(self, ctx: BKITParser.ContinueStatementContext):
        return Continue()

    # functionCall SEMI
    def visitCallStatement(self, ctx: BKITParser.CallStatementContext):
        idList, expList = self.visit(ctx.functionCall())
        return CallStmt(idList, expList)

    # Identifier LB argumentList? RB
    def visitFunctionCall(self, ctx: BKITParser.FunctionCallContext):
        return (
            Id(ctx.Identifier().getText()),
            self.visit(ctx.argumentList()) if ctx.argumentList() else []
        )

    # argumentList COMMA expression | expression
    def visitArgumentList(self, ctx: BKITParser.ArgumentListContext):
        return (
            [self.visit(ctx.expression())] if not ctx.COMMA() else
            self.visit(ctx.argumentList()) + [self.visit(ctx.expression())]
        )

    # RETURN expression? SEMI
    def visitReturnStatement(self, ctx: BKITParser.ReturnStatementContext):
        return Return(self.visit(ctx.expression())) if ctx.expression() else Return(None)

    # //===== EXPRESSIONS =====//
    # logicalOrAndExpression relationalOperator logicalOrAndExpression | logicalOrAndExpression
    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        left = self.visit(ctx.logicalOrAndExpression(0))
        opt = self.visit(ctx.relationalOperator()) if ctx.relationalOperator() else None
        return (
            left if not opt else
            BinaryOp(opt, left, self.visit(ctx.logicalOrAndExpression(1)))
        )

    # Visit a parse tree produced by BKITParser#relationalOperator.
    def visitRelationalOperator(self, ctx: BKITParser.RelationalOperatorContext):
        return ctx.getChild(0).getText()

    # logicalOrAndExpression logicalOrAndOperator additiveExpression | additiveExpression
    def visitLogicalOrAndExpression(self, ctx: BKITParser.LogicalOrAndExpressionContext):
        right = self.visit(ctx.additiveExpression())
        opt = self.visit(ctx.logicalOrAndOperator()) if ctx.logicalOrAndOperator() else None
        return (
            right if not opt else
            BinaryOp(opt, self.visit(ctx.logicalOrAndExpression()), right)
        )

    # logicalOrAndOperator.
    def visitLogicalOrAndOperator(self, ctx: BKITParser.LogicalOrAndOperatorContext):
        return ctx.getChild(0).getText()

    # additiveExpression additiveOperator multiplicativeExpression | multiplicativeExpression
    def visitAdditiveExpression(self, ctx: BKITParser.AdditiveExpressionContext):
        right = self.visit(ctx.multiplicativeExpression())
        opt = self.visit(ctx.additiveOperator()) if ctx.additiveOperator() else None
        return (
            right if not opt else
            BinaryOp(opt, self.visit(ctx.additiveExpression()), right)
        )

    # additiveOperator.
    def visitAdditiveOperator(self, ctx: BKITParser.AdditiveOperatorContext):
        return ctx.getChild(0).getText()

    # multiplicativeExpression multiplicativeOperator logicalNotExpression | logicalNotExpression
    def visitMultiplicativeExpression(self, ctx: BKITParser.MultiplicativeExpressionContext):
        right = self.visit(ctx.logicalNotExpression())
        opt = self.visit(ctx.multiplicativeOperator()) if ctx.multiplicativeOperator() else None
        return (
            right if not opt else
            BinaryOp(opt, self.visit(ctx.multiplicativeExpression()), right)
        )

    # multiplicativeOperator.
    def visitMultiplicativeOperator(self, ctx: BKITParser.MultiplicativeOperatorContext):
        return ctx.getChild(0).getText()

    # NOT logicalNotExpression | signExpression
    def visitLogicalNotExpression(self, ctx: BKITParser.LogicalNotExpressionContext):
        return (
            UnaryOp(ctx.NOT().getText(), self.visit(ctx.logicalNotExpression())) if ctx.NOT() else
            self.visit(ctx.signExpression())
        )

    # signOperator signExpression | indexExpression
    def visitSignExpression(self, ctx: BKITParser.SignExpressionContext):
        return (
            UnaryOp(self.visit(ctx.signOperator()), self.visit(ctx.signExpression())) if ctx.signOperator() else
            self.visit(ctx.indexExpression())
        )

    # SUB | SUBF
    def visitSignOperator(self, ctx: BKITParser.SignOperatorContext):
        return ctx.getChild(0).getText()

    # indexExpression indexOperator+ | primaryExpression
    def visitIndexExpression(self, ctx: BKITParser.IndexExpressionContext):
        optList = reduce(lambda x, y: x + [self.visit(y)], ctx.indexOperator(), [])
        return (
            ArrayCell(self.visit(ctx.indexExpression()), optList) if ctx.indexOperator() else
            self.visit(ctx.primaryExpression())
        )

    # LSB expression RSB
    def visitIndexOperator(self, ctx: BKITParser.IndexOperatorContext):
        return self.visit(ctx.expression())

    # primaryExpression.
    def visitPrimaryExpression(self, ctx: BKITParser.PrimaryExpressionContext):
        return (
            self.visit(ctx.expression()) if ctx.expression() else
            Id(ctx.Identifier().getText()) if ctx.Identifier() else
            self.visit(ctx.literals()) if ctx.literals() else
            self.visit(ctx.callExpr())
        )

    # callExpr
    def visitCallExpr(self, ctx: BKITParser.CallExprContext):
        return CallExpr(
            Id(ctx.Identifier().getText()),
            self.visit(ctx.argumentList()) if ctx.argumentList() else []
        )

    # Visit a parse tree produced by BKITParser#literals.
    def visitLiterals(self, ctx: BKITParser.LiteralsContext):
        return (
            IntLiteral(self.stoi(ctx.IntegerConstant().getText())) if ctx.IntegerConstant() else
            FloatLiteral(float(ctx.FloatingConstant().getText())) if ctx.FloatingConstant() else
            StringLiteral(ctx.String().getText()) if ctx.String() else
            self.visitBoolean(ctx) if ctx.boolean() else
            self.visit(ctx.array())
        )

    # boolean.
    def visitBoolean(self, ctx: BKITParser.BooleanContext):
        return BooleanLiteral(True if ctx.boolean().getText() == "True" else False)

    # LP literals (COMMA literals)* RP
    def visitArray(self, ctx: BKITParser.ArrayContext):
        return ArrayLiteral([self.visit(x) for x in ctx.literals()])

    # Visit a parse tree produced by BKITParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx: BKITParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)

    def stoi(self, num: str):
        return (
            int(num, 8) if '0o' in num or '0O' in num else
            int(num, 16) if '0x' in num or '0X' in num else
            int(num)
        )
