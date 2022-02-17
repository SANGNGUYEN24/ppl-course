# TODO Import lai 3 lines nhu ban dau
# from D96Visitor import D96Visitor
# from D96Parser import D96Parser
# from AST import *

from initial.src.main.d96.utils.AST import *
from initial.target.D96Visitor import D96Visitor
from initial.target.D96Parser import D96Parser


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(list(map(lambda x: self.visit(x), ctx.classDeclaration())))

    def visitClassDeclaration(self, ctx: D96Parser.ClassDeclarationContext):
        superClass = Id(ctx.IDENTIFIER())

    def visitMemberDeclaration(self, ctx:D96Parser.MemberDeclarationContext):
        pass

    def visitMethodDeclaration(self, ctx: D96Parser.MethodDeclarationContext):
        pass

    def visitConstructor(self, ctx: D96Parser.ConstructorContext):
        pass

    def visitDestructor(self, ctx: D96Parser.DestructorContext):
        pass

    def visitParameterList(self, ctx: D96Parser.ParameterListContext):
        pass

    def visitParameter(self, ctx: D96Parser.ParameterContext):
        pass

    def visitD96Type(self, ctx: D96Parser.D96TypeContext):
        pass

    def visitAttributeDeclaration(self, ctx: D96Parser.AttributeDeclarationContext):
        pass

    def visitAttributeValueList(self, ctx: D96Parser.AttributeValueListContext):
        pass

    def visitIdentifierList(self, ctx: D96Parser.IdentifierListContext):
        pass

    def visitMixedIdentifierList(self, ctx: D96Parser.MixedIdentifierListContext):
        pass

    def visitExpressionList(self, ctx: D96Parser.ExpressionListContext):
        pass

    def visitElementExpression(self, ctx: D96Parser.ElementExpressionContext):
        pass

    def visitIndexOperator(self, ctx: D96Parser.IndexOperatorContext):
        pass

    def visitRelationalOperator(self, ctx: D96Parser.RelationalOperatorContext):
        pass

    def visitExpression(self, ctx: D96Parser.ExpressionContext):
        pass

    def visitRelationalExpr(self, ctx: D96Parser.RelationalExprContext):
        pass

    def visitAndOrExpr(self, ctx: D96Parser.AndOrExprContext):
        pass

    def visitAddSubExpr(self, ctx: D96Parser.AddSubExprContext):
        pass

    def visitMulAddMolExpr(self, ctx: D96Parser.MulAddMolExprContext):
        pass

    def visitNotExpr(self, ctx: D96Parser.NotExprContext):
        pass

    def visitSignExpr(self, ctx: D96Parser.SignExprContext):
        pass

    def visitIndexOperatorExpr(self, ctx: D96Parser.IndexOperatorExprContext):
        pass

    def visitInstanceAccess(self, ctx: D96Parser.InstanceAccessContext):
        pass

    def visitStaticAccess(self, ctx: D96Parser.StaticAccessContext):
        pass

    def visitObjectCreation(self, ctx: D96Parser.ObjectCreationContext):
        pass

    def visitAtomExpr(self, ctx: D96Parser.AtomExprContext):
        pass

    def visitVarValStatement(self, ctx: D96Parser.VarValStatementContext):
        pass

    def visitVarValValueList(self, ctx: D96Parser.VarValValueListContext):
        pass

    def visitLhs(self, ctx: D96Parser.LhsContext):
        pass

    def visitAssignStatement(self, ctx: D96Parser.AssignStatementContext):
        pass

    def visitIfStatement(self, ctx: D96Parser.IfStatementContext):
        pass

    def visitIfPart(self, ctx: D96Parser.IfPartContext):
        pass

    def visitElseIfPart(self, ctx: D96Parser.ElseIfPartContext):
        pass

    def visitElsePart(self, ctx: D96Parser.ElsePartContext):
        pass

    def visitForInStatement(self, ctx: D96Parser.ForInStatementContext):
        pass

    def visitLoopPart(self, ctx: D96Parser.LoopPartContext):
        pass

    def visitBreakStatement(self, ctx: D96Parser.BreakStatementContext):
        return Break()

    def visitContinueStatement(self, ctx: D96Parser.ContinueStatementContext):
        return Continue()

    def visitReturnStatement(self, ctx: D96Parser.ReturnStatementContext):
        if ctx.expression():
            return Return(ctx.expression().accept(self))
        else:
            return Return(None)

    def visitMemberAccessInstance(self, ctx: D96Parser.MemberAccessInstanceContext):
        pass

    def visitMemberAccessStatic(self, ctx: D96Parser.MemberAccessStaticContext):
        pass

    def visitMethodInvocationStatement(self, ctx: D96Parser.MethodInvocationStatementContext):
        pass

    def visitBlockStatement(self, ctx: D96Parser.BlockStatementContext):
        pass

    def visitStatement(self, ctx: D96Parser.StatementContext):
        pass

    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.INTEGER_LITERAL():
            if ctx.INTEGER_LITERAL().getText().isnumeric():
                return IntLiteral(int(ctx.INTEGER_LITERAL().getText()))
            else:
                return IntLiteral(int(ctx.INTEGER_LITERAL().getText(), 0))
        elif ctx.INTEGER_LITERAL2():
            if ctx.INTEGER_LITERAL2().getText().isnumeric():
                return IntLiteral(int(ctx.INTEGER_LITERAL2().getText()))
            else:
                return IntLiteral(int(ctx.INTEGER_LITERAL2().getText(), 0))
        elif ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        # TODO what is StringType
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.indexedArray():
            return ctx.indexedArray().accept(self)
        else:
            return ctx.multiDimentionalArray().accept(self)

    def visitIndexedArray(self, ctx: D96Parser.IndexedArrayContext):
        pass

    def visitMultiDimentionalArray(self, ctx: D96Parser.MultiDimentionalArrayContext):
        pass

    def visitPrimitiveType(self, ctx: D96Parser.PrimitiveTypeContext):
        pass

    def visitArrayType(self, ctx: D96Parser.ArrayTypeContext):
        pass
