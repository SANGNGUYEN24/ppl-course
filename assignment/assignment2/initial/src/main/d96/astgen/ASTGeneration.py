# TODO Import lai 3 lines nhu ban dau
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce


# from initial.src.main.d96.utils.AST import *
# from initial.target.D96Visitor import D96Visitor
# from initial.target.D96Parser import D96Parser


def flatten(lst):
    if not isinstance(lst, list):
        return [lst]

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return flatten(lst[0])

    head, tail = lst[0], lst[1:]
    return flatten(head) + flatten(tail)


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(list(map(lambda x: self.visit(x), ctx.classDeclaration())))

    def visitClassDeclaration(self, ctx: D96Parser.ClassDeclarationContext):
        superClass = Id(ctx.IDENTIFIER(1).getText()) if ctx.IDENTIFIER(1) else None
        memberDeclarationList = flatten([self.visit(x) for x in ctx.memberDeclaration()])
        return ClassDecl(
            Id(ctx.IDENTIFIER(0).getText()),
            memberDeclarationList,
            superClass
        )

    def visitMemberDeclaration(self, ctx: D96Parser.MemberDeclarationContext):
        if ctx.attributeDeclaration():
            return self.visit(ctx.attributeDeclaration())
        else:
            return self.visit(ctx.methodDeclaration())

    def visitMethodDeclaration(self, ctx: D96Parser.MethodDeclarationContext):
        if ctx.constructor():
            return self.visit(ctx.constructor())
        if ctx.destructor():
            return self.visit(ctx.destructor())

        param = self.visit(ctx.parameterList()) if ctx.parameterList() else []
        # TODO xem lai dieu kien cua statementList
        # Program([ClassDecl(Id(Adam),Id(Human),[MethodDecl(Id(main),Static,[],Block([None]))])])
        # Block([None]) expect Block([]) khi function main ko co gi
        statementList = [self.visit(ctx.blockStatement())] if ctx.blockStatement() else []
        # body = Block(statementList)
        body = Block([])

        # TODO Dieu kien chi main trong Program class moi la Static
        if ctx.IDENTIFIER():
            methodName = Id(ctx.IDENTIFIER().getText())
            kind = Static() if methodName == Id("main") else Instance()
            # param = []
        else:
            methodName = Id(ctx.DOLAR_IDENTIFIER().getText())
            kind = Static()

        return MethodDecl(kind, methodName, param, body)

    def visitConstructor(self, ctx: D96Parser.ConstructorContext):
        kind = Instance()
        methodName = Id("Constructor")
        param = self.visit(ctx.parameterList()) if ctx.parameterList() else []
        body = Block([])
        return MethodDecl(kind, methodName, param, body)

    def visitDestructor(self, ctx: D96Parser.DestructorContext):
        kind = Instance()
        methodName = Id("Destructor")
        param = []
        body = Block([])
        return MethodDecl(kind, methodName, param, body)

    def visitParameterList(self, ctx: D96Parser.ParameterListContext):
        if ctx.parameter(0):
            return self.visit(ctx.parameter(0))
        else:
            return list(map(lambda x: self.visit(x), ctx.parameter()))

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
        expression = self.visit(ctx.expression()) if ctx.expression() else None
        return Return(expression)

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
        if ctx.INTEGER_LITERAL2():
            return IntLiteral(int(ctx.INTEGER_LITERAL2().getText()))
        if ctx.INTEGER_LITERAL():
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText()))
        if ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        if ctx.BOOLEAN_LITERAL():
            return BooleanLiteral(ctx.BOOLEAN_LITERAL().getText() == "True")
        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        # TODO Xem lai phan Array
        if ctx.indexedArray():
            return ctx.indexedArray()
        if ctx.multiDimentionalArray():
            return ctx.multiDimentionalArray()

    def visitIndexedArray(self, ctx: D96Parser.IndexedArrayContext):
        pass

    def visitMultiDimentionalArray(self, ctx: D96Parser.MultiDimentionalArrayContext):
        pass

    def visitPrimitiveType(self, ctx: D96Parser.PrimitiveTypeContext):
        if ctx.K_BOOLEAN():
            return BoolType()
        if ctx.K_INT():
            return IntType()
        if ctx.K_FLOAT():
            return FloatType()
        if ctx.K_STRING():
            return StringType()

    def visitArrayType(self, ctx: D96Parser.ArrayTypeContext):
        pass
