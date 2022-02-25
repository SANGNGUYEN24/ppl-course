# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classDeclaration.
    def visitClassDeclaration(self, ctx:D96Parser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#normalClassDecl.
    def visitNormalClassDecl(self, ctx:D96Parser.NormalClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#programClassDecl.
    def visitProgramClassDecl(self, ctx:D96Parser.ProgramClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#programClassMemDecl.
    def visitProgramClassMemDecl(self, ctx:D96Parser.ProgramClassMemDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mainMethodDecl.
    def visitMainMethodDecl(self, ctx:D96Parser.MainMethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:D96Parser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:D96Parser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameterList.
    def visitParameterList(self, ctx:D96Parser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter.
    def visitParameter(self, ctx:D96Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#d96Type.
    def visitD96Type(self, ctx:D96Parser.D96TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attributeDeclaration.
    def visitAttributeDeclaration(self, ctx:D96Parser.AttributeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifierList.
    def visitIdentifierList(self, ctx:D96Parser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mixedIdentifier.
    def visitMixedIdentifier(self, ctx:D96Parser.MixedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expressionList.
    def visitExpressionList(self, ctx:D96Parser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elementExpression.
    def visitElementExpression(self, ctx:D96Parser.ElementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexOperator.
    def visitIndexOperator(self, ctx:D96Parser.IndexOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relationalOperator.
    def visitRelationalOperator(self, ctx:D96Parser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relationalExpr.
    def visitRelationalExpr(self, ctx:D96Parser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#andOrExpr.
    def visitAndOrExpr(self, ctx:D96Parser.AndOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#addSubExpr.
    def visitAddSubExpr(self, ctx:D96Parser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mulAddMolExpr.
    def visitMulAddMolExpr(self, ctx:D96Parser.MulAddMolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#notExpr.
    def visitNotExpr(self, ctx:D96Parser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#signExpr.
    def visitSignExpr(self, ctx:D96Parser.SignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexOperatorExpr.
    def visitIndexOperatorExpr(self, ctx:D96Parser.IndexOperatorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instanceAccess.
    def visitInstanceAccess(self, ctx:D96Parser.InstanceAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#staticAccess.
    def visitStaticAccess(self, ctx:D96Parser.StaticAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#objectCreation.
    def visitObjectCreation(self, ctx:D96Parser.ObjectCreationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#atomExpr.
    def visitAtomExpr(self, ctx:D96Parser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varValStatement.
    def visitVarValStatement(self, ctx:D96Parser.VarValStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varValValueList.
    def visitVarValValueList(self, ctx:D96Parser.VarValValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignStatement.
    def visitAssignStatement(self, ctx:D96Parser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifStatement.
    def visitIfStatement(self, ctx:D96Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifPart.
    def visitIfPart(self, ctx:D96Parser.IfPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseIfPart.
    def visitElseIfPart(self, ctx:D96Parser.ElseIfPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elsePart.
    def visitElsePart(self, ctx:D96Parser.ElsePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forInStatement.
    def visitForInStatement(self, ctx:D96Parser.ForInStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#loopPart.
    def visitLoopPart(self, ctx:D96Parser.LoopPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#breakStatement.
    def visitBreakStatement(self, ctx:D96Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continueStatement.
    def visitContinueStatement(self, ctx:D96Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#returnStatement.
    def visitReturnStatement(self, ctx:D96Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memberAccessInstance.
    def visitMemberAccessInstance(self, ctx:D96Parser.MemberAccessInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memberAccessStatic.
    def visitMemberAccessStatic(self, ctx:D96Parser.MemberAccessStaticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodInvocationStatement.
    def visitMethodInvocationStatement(self, ctx:D96Parser.MethodInvocationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blockStatement.
    def visitBlockStatement(self, ctx:D96Parser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexedArray.
    def visitIndexedArray(self, ctx:D96Parser.IndexedArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multiDimentionalArray.
    def visitMultiDimentionalArray(self, ctx:D96Parser.MultiDimentionalArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayType.
    def visitArrayType(self, ctx:D96Parser.ArrayTypeContext):
        return self.visitChildren(ctx)



del D96Parser