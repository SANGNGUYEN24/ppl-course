# Generated from C:/development-area/ppl/ppl-course/assignment/assignment2/initial/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete listener for a parse tree produced by D96Parser.
class D96Listener(ParseTreeListener):

    # Enter a parse tree produced by D96Parser#program.
    def enterProgram(self, ctx:D96Parser.ProgramContext):
        pass

    # Exit a parse tree produced by D96Parser#program.
    def exitProgram(self, ctx:D96Parser.ProgramContext):
        pass


    # Enter a parse tree produced by D96Parser#classDeclaration.
    def enterClassDeclaration(self, ctx:D96Parser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by D96Parser#classDeclaration.
    def exitClassDeclaration(self, ctx:D96Parser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by D96Parser#normalClassDecl.
    def enterNormalClassDecl(self, ctx:D96Parser.NormalClassDeclContext):
        pass

    # Exit a parse tree produced by D96Parser#normalClassDecl.
    def exitNormalClassDecl(self, ctx:D96Parser.NormalClassDeclContext):
        pass


    # Enter a parse tree produced by D96Parser#programClassDecl.
    def enterProgramClassDecl(self, ctx:D96Parser.ProgramClassDeclContext):
        pass

    # Exit a parse tree produced by D96Parser#programClassDecl.
    def exitProgramClassDecl(self, ctx:D96Parser.ProgramClassDeclContext):
        pass


    # Enter a parse tree produced by D96Parser#programClassMemDecl.
    def enterProgramClassMemDecl(self, ctx:D96Parser.ProgramClassMemDeclContext):
        pass

    # Exit a parse tree produced by D96Parser#programClassMemDecl.
    def exitProgramClassMemDecl(self, ctx:D96Parser.ProgramClassMemDeclContext):
        pass


    # Enter a parse tree produced by D96Parser#mainMethodDecl.
    def enterMainMethodDecl(self, ctx:D96Parser.MainMethodDeclContext):
        pass

    # Exit a parse tree produced by D96Parser#mainMethodDecl.
    def exitMainMethodDecl(self, ctx:D96Parser.MainMethodDeclContext):
        pass


    # Enter a parse tree produced by D96Parser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:D96Parser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by D96Parser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:D96Parser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by D96Parser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:D96Parser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by D96Parser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:D96Parser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by D96Parser#constructor.
    def enterConstructor(self, ctx:D96Parser.ConstructorContext):
        pass

    # Exit a parse tree produced by D96Parser#constructor.
    def exitConstructor(self, ctx:D96Parser.ConstructorContext):
        pass


    # Enter a parse tree produced by D96Parser#destructor.
    def enterDestructor(self, ctx:D96Parser.DestructorContext):
        pass

    # Exit a parse tree produced by D96Parser#destructor.
    def exitDestructor(self, ctx:D96Parser.DestructorContext):
        pass


    # Enter a parse tree produced by D96Parser#parameterList.
    def enterParameterList(self, ctx:D96Parser.ParameterListContext):
        pass

    # Exit a parse tree produced by D96Parser#parameterList.
    def exitParameterList(self, ctx:D96Parser.ParameterListContext):
        pass


    # Enter a parse tree produced by D96Parser#parameter.
    def enterParameter(self, ctx:D96Parser.ParameterContext):
        pass

    # Exit a parse tree produced by D96Parser#parameter.
    def exitParameter(self, ctx:D96Parser.ParameterContext):
        pass


    # Enter a parse tree produced by D96Parser#d96Type.
    def enterD96Type(self, ctx:D96Parser.D96TypeContext):
        pass

    # Exit a parse tree produced by D96Parser#d96Type.
    def exitD96Type(self, ctx:D96Parser.D96TypeContext):
        pass


    # Enter a parse tree produced by D96Parser#attributeDeclaration.
    def enterAttributeDeclaration(self, ctx:D96Parser.AttributeDeclarationContext):
        pass

    # Exit a parse tree produced by D96Parser#attributeDeclaration.
    def exitAttributeDeclaration(self, ctx:D96Parser.AttributeDeclarationContext):
        pass


    # Enter a parse tree produced by D96Parser#identifierList.
    def enterIdentifierList(self, ctx:D96Parser.IdentifierListContext):
        pass

    # Exit a parse tree produced by D96Parser#identifierList.
    def exitIdentifierList(self, ctx:D96Parser.IdentifierListContext):
        pass


    # Enter a parse tree produced by D96Parser#mixedIdentifier.
    def enterMixedIdentifier(self, ctx:D96Parser.MixedIdentifierContext):
        pass

    # Exit a parse tree produced by D96Parser#mixedIdentifier.
    def exitMixedIdentifier(self, ctx:D96Parser.MixedIdentifierContext):
        pass


    # Enter a parse tree produced by D96Parser#expressionList.
    def enterExpressionList(self, ctx:D96Parser.ExpressionListContext):
        pass

    # Exit a parse tree produced by D96Parser#expressionList.
    def exitExpressionList(self, ctx:D96Parser.ExpressionListContext):
        pass


    # Enter a parse tree produced by D96Parser#relationalOperator.
    def enterRelationalOperator(self, ctx:D96Parser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by D96Parser#relationalOperator.
    def exitRelationalOperator(self, ctx:D96Parser.RelationalOperatorContext):
        pass


    # Enter a parse tree produced by D96Parser#expression.
    def enterExpression(self, ctx:D96Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by D96Parser#expression.
    def exitExpression(self, ctx:D96Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by D96Parser#relationalExpr.
    def enterRelationalExpr(self, ctx:D96Parser.RelationalExprContext):
        pass

    # Exit a parse tree produced by D96Parser#relationalExpr.
    def exitRelationalExpr(self, ctx:D96Parser.RelationalExprContext):
        pass


    # Enter a parse tree produced by D96Parser#andOrExpr.
    def enterAndOrExpr(self, ctx:D96Parser.AndOrExprContext):
        pass

    # Exit a parse tree produced by D96Parser#andOrExpr.
    def exitAndOrExpr(self, ctx:D96Parser.AndOrExprContext):
        pass


    # Enter a parse tree produced by D96Parser#addSubExpr.
    def enterAddSubExpr(self, ctx:D96Parser.AddSubExprContext):
        pass

    # Exit a parse tree produced by D96Parser#addSubExpr.
    def exitAddSubExpr(self, ctx:D96Parser.AddSubExprContext):
        pass


    # Enter a parse tree produced by D96Parser#mulAddMolExpr.
    def enterMulAddMolExpr(self, ctx:D96Parser.MulAddMolExprContext):
        pass

    # Exit a parse tree produced by D96Parser#mulAddMolExpr.
    def exitMulAddMolExpr(self, ctx:D96Parser.MulAddMolExprContext):
        pass


    # Enter a parse tree produced by D96Parser#notExpr.
    def enterNotExpr(self, ctx:D96Parser.NotExprContext):
        pass

    # Exit a parse tree produced by D96Parser#notExpr.
    def exitNotExpr(self, ctx:D96Parser.NotExprContext):
        pass


    # Enter a parse tree produced by D96Parser#signExpr.
    def enterSignExpr(self, ctx:D96Parser.SignExprContext):
        pass

    # Exit a parse tree produced by D96Parser#signExpr.
    def exitSignExpr(self, ctx:D96Parser.SignExprContext):
        pass


    # Enter a parse tree produced by D96Parser#elementExpr.
    def enterElementExpr(self, ctx:D96Parser.ElementExprContext):
        pass

    # Exit a parse tree produced by D96Parser#elementExpr.
    def exitElementExpr(self, ctx:D96Parser.ElementExprContext):
        pass


    # Enter a parse tree produced by D96Parser#instanceAccess.
    def enterInstanceAccess(self, ctx:D96Parser.InstanceAccessContext):
        pass

    # Exit a parse tree produced by D96Parser#instanceAccess.
    def exitInstanceAccess(self, ctx:D96Parser.InstanceAccessContext):
        pass


    # Enter a parse tree produced by D96Parser#staticAccess.
    def enterStaticAccess(self, ctx:D96Parser.StaticAccessContext):
        pass

    # Exit a parse tree produced by D96Parser#staticAccess.
    def exitStaticAccess(self, ctx:D96Parser.StaticAccessContext):
        pass


    # Enter a parse tree produced by D96Parser#objectCreation.
    def enterObjectCreation(self, ctx:D96Parser.ObjectCreationContext):
        pass

    # Exit a parse tree produced by D96Parser#objectCreation.
    def exitObjectCreation(self, ctx:D96Parser.ObjectCreationContext):
        pass


    # Enter a parse tree produced by D96Parser#atomExpr.
    def enterAtomExpr(self, ctx:D96Parser.AtomExprContext):
        pass

    # Exit a parse tree produced by D96Parser#atomExpr.
    def exitAtomExpr(self, ctx:D96Parser.AtomExprContext):
        pass


    # Enter a parse tree produced by D96Parser#varValStatement.
    def enterVarValStatement(self, ctx:D96Parser.VarValStatementContext):
        pass

    # Exit a parse tree produced by D96Parser#varValStatement.
    def exitVarValStatement(self, ctx:D96Parser.VarValStatementContext):
        pass


    # Enter a parse tree produced by D96Parser#lhs.
    def enterLhs(self, ctx:D96Parser.LhsContext):
        pass

    # Exit a parse tree produced by D96Parser#lhs.
    def exitLhs(self, ctx:D96Parser.LhsContext):
        pass


    # Enter a parse tree produced by D96Parser#assignStatement.
    def enterAssignStatement(self, ctx:D96Parser.AssignStatementContext):
        pass

    # Exit a parse tree produced by D96Parser#assignStatement.
    def exitAssignStatement(self, ctx:D96Parser.AssignStatementContext):
        pass


    # Enter a parse tree produced by D96Parser#ifStatement.
    def enterIfStatement(self, ctx:D96Parser.IfStatementContext):
        pass

    # Exit a parse tree produced by D96Parser#ifStatement.
    def exitIfStatement(self, ctx:D96Parser.IfStatementContext):
        pass


    # Enter a parse tree produced by D96Parser#elsePart.
    def enterElsePart(self, ctx:D96Parser.ElsePartContext):
        pass

    # Exit a parse tree produced by D96Parser#elsePart.
    def exitElsePart(self, ctx:D96Parser.ElsePartContext):
        pass


    # Enter a parse tree produced by D96Parser#forInStatement.
    def enterForInStatement(self, ctx:D96Parser.ForInStatementContext):
        pass

    # Exit a parse tree produced by D96Parser#forInStatement.
    def exitForInStatement(self, ctx:D96Parser.ForInStatementContext):
        pass


    # Enter a parse tree produced by D96Parser#breakStatement.
    def enterBreakStatement(self, ctx:D96Parser.BreakStatementContext):
        pass

    # Exit a parse tree produced by D96Parser#breakStatement.
    def exitBreakStatement(self, ctx:D96Parser.BreakStatementContext):
        pass


    # Enter a parse tree produced by D96Parser#continueStatement.
    def enterContinueStatement(self, ctx:D96Parser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by D96Parser#continueStatement.
    def exitContinueStatement(self, ctx:D96Parser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by D96Parser#returnStatement.
    def enterReturnStatement(self, ctx:D96Parser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by D96Parser#returnStatement.
    def exitReturnStatement(self, ctx:D96Parser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by D96Parser#methodInvocationStatement.
    def enterMethodInvocationStatement(self, ctx:D96Parser.MethodInvocationStatementContext):
        pass

    # Exit a parse tree produced by D96Parser#methodInvocationStatement.
    def exitMethodInvocationStatement(self, ctx:D96Parser.MethodInvocationStatementContext):
        pass


    # Enter a parse tree produced by D96Parser#blockStatement.
    def enterBlockStatement(self, ctx:D96Parser.BlockStatementContext):
        pass

    # Exit a parse tree produced by D96Parser#blockStatement.
    def exitBlockStatement(self, ctx:D96Parser.BlockStatementContext):
        pass


    # Enter a parse tree produced by D96Parser#statement.
    def enterStatement(self, ctx:D96Parser.StatementContext):
        pass

    # Exit a parse tree produced by D96Parser#statement.
    def exitStatement(self, ctx:D96Parser.StatementContext):
        pass


    # Enter a parse tree produced by D96Parser#ip.
    def enterIp(self, ctx:D96Parser.IpContext):
        pass

    # Exit a parse tree produced by D96Parser#ip.
    def exitIp(self, ctx:D96Parser.IpContext):
        pass


    # Enter a parse tree produced by D96Parser#literal.
    def enterLiteral(self, ctx:D96Parser.LiteralContext):
        pass

    # Exit a parse tree produced by D96Parser#literal.
    def exitLiteral(self, ctx:D96Parser.LiteralContext):
        pass


    # Enter a parse tree produced by D96Parser#indexedArray.
    def enterIndexedArray(self, ctx:D96Parser.IndexedArrayContext):
        pass

    # Exit a parse tree produced by D96Parser#indexedArray.
    def exitIndexedArray(self, ctx:D96Parser.IndexedArrayContext):
        pass


    # Enter a parse tree produced by D96Parser#arrayType.
    def enterArrayType(self, ctx:D96Parser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by D96Parser#arrayType.
    def exitArrayType(self, ctx:D96Parser.ArrayTypeContext):
        pass



del D96Parser