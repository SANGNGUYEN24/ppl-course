# TODO Import lai 3 lines nhu ban dau
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce

# #
from initial.src.main.d96.utils.AST import *
from initial.target.D96Visitor import D96Visitor
from initial.target.D96Parser import D96Parser


def flatten(lst):
    if not isinstance(lst, list):
        return [lst]

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return flatten(lst[0])

    head, tail = lst[0], lst[1:]
    return flatten(head) + flatten(tail)


def convertStringToPrimitiveType(s):
    if s == "Int":
        return IntType()
    if s == "Boolean":
        return BoolType()
    if s == "Float":
        return FloatType()
    if s == "String":
        return StringType()


def text2int(text):
    if text[0] != '0':
        return int(text)
    elif text == '0':
        return 0
    elif text[1] in ['x', 'X']:
        return int(text, 16)
    elif text[1] in ['b', 'B']:
        return int(text, 2)
    return int(text[0] + 'o' + text[1:])


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classDeclaration()])

    def visitClassDeclaration(self, ctx: D96Parser.ClassDeclarationContext):
        if ctx.normalClassDecl():
            return self.visit(ctx.normalClassDecl())
        return self.visit(ctx.programClassDecl())

    def visitNormalClassDecl(self, ctx: D96Parser.NormalClassDeclContext):
        className = Id(ctx.K_MAIN().getText()) if ctx.K_MAIN() else Id(ctx.IDENTIFIER(0).getText())
        superClass = Id(ctx.IDENTIFIER(1).getText()) if ctx.IDENTIFIER(1) else None
        memberDeclarationList = flatten([self.visit(x) for x in ctx.memberDeclaration()])
        return ClassDecl(
            className,
            memberDeclarationList,
            superClass
        )

    def visitProgramClassDecl(self, ctx: D96Parser.ProgramClassDeclContext):
        className = Id(ctx.K_PROGRAM().getText())
        superClass = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else None
        memberDeclarationList = flatten([self.visit(x) for x in ctx.programClassMemDecl()])
        return ClassDecl(
            className,
            memberDeclarationList,
            superClass
        )

    def visitProgramClassMemDecl(self, ctx: D96Parser.ProgramClassMemDeclContext):
        if ctx.attributeDeclaration():
            return self.visit(ctx.attributeDeclaration())
        if ctx.mainMethodDecl():
            return self.visit(ctx.mainMethodDecl())
        return self.visit(ctx.methodDeclaration())

    def visitMainMethodDecl(self, ctx: D96Parser.MainMethodDeclContext):
        body = Block([])
        return MethodDecl(
            Static(),
            Id(ctx.K_MAIN().getText()),
            [],
            body
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

        # TODO xem lai dieu kien cua statementList
        # Program([ClassDecl(Id(Adam),Id(Human),[MethodDecl(Id(main),Static,[],Block([None]))])])
        # Block([None]) expect Block([]) khi function main ko co gi
        # statementList = [self.visit(ctx.blockStatement())] if ctx.blockStatement() else []
        # body = Block(statementList)
        param = self.visit(ctx.parameterList()) if ctx.parameterList() else []
        body = Block([])

        if ctx.K_MAIN():
            methodName = Id(ctx.K_MAIN().getText())
            kind = Instance()
        elif ctx.IDENTIFIER():
            methodName = Id(ctx.IDENTIFIER().getText())
            kind = Instance()
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
        return flatten([self.visit(x) for x in ctx.parameter()])

    def visitParameter(self, ctx: D96Parser.ParameterContext):
        variableList = self.visit(ctx.identifierList())
        varType = self.visit(ctx.d96Type())
        return [VarDecl(variable, varType) for variable in variableList]

    def visitD96Type(self, ctx: D96Parser.D96TypeContext):
        if ctx.PRIMITIVE_TYPE():
            return convertStringToPrimitiveType(ctx.PRIMITIVE_TYPE().getText())
        if ctx.IDENTIFIER():
            return ClassType(Id(ctx.IDENTIFIER().getText()))
        if ctx.arrayType():
            return self.visit(ctx.arrayType())

    def visitAttributeDeclaration(self, ctx: D96Parser.AttributeDeclarationContext):
        d96Type = self.visit(ctx.d96Type())
        if ctx.mixedIdentifier(1):
            identifierList = [self.visit(x) for x in ctx.mixedIdentifier()]
            print("identifierList", identifierList)
        else:
            identifierList = [self.visit(ctx.mixedIdentifier(0))]
            print("identifierList", identifierList)

        if ctx.expression(1):
            expressionList = [self.visit(x) for x in ctx.expression()]
        else:
            if ctx.expression(0):
                expressionList = [self.visit(ctx.expression(0))]
            else:
                expressionList = []

        print("expressionlist", expressionList)
        result = []
        isConstant = True if ctx.K_VAL() else False

        # No expression
        for i in range(len(identifierList)):
            identifier = identifierList[i]
            initialValue = expressionList[i] if len(expressionList) > 0 else None
            if "$" in identifier:
                kind = Static()
                if isConstant:
                    result += [
                        AttributeDecl(
                            kind,
                            ConstDecl(
                                Id(identifier),
                                d96Type,
                                initialValue
                            )
                        )
                    ]
                else:
                    result += [
                        AttributeDecl(
                            kind,
                            VarDecl(
                                Id(identifier),
                                d96Type,
                                initialValue
                            )
                        )
                    ]
            else:
                kind = Instance()
                if isConstant:
                    result += [
                        AttributeDecl(
                            kind,
                            ConstDecl(
                                Id(identifier),
                                d96Type,
                                initialValue
                            )
                        )
                    ]
                else:
                    result += [
                        AttributeDecl(
                            kind,
                            VarDecl(
                                Id(identifier),
                                d96Type,
                                initialValue
                            )
                        )
                    ]

        print("result", result)
        return result

    def visitIdentifierList(self, ctx: D96Parser.IdentifierListContext):
        return [Id(x.getText()) for x in ctx.IDENTIFIER()]

    def visitMixedIdentifier(self, ctx: D96Parser.MixedIdentifierContext):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        return ctx.DOLAR_IDENTIFIER().getText()

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

        return ArrayCell()

    def visitInstanceAccess(self, ctx: D96Parser.InstanceAccessContext):
        preExpression = self.visit(ctx.instanceAccess())
        accessField = Id(ctx.IDENTIFIER().getText())
        if ctx.staticAccess():
            return self.visit(ctx.staticAccess())
        else:
            if ctx.LEFT_PAREN():  # Access a function
                if ctx.expressionList():
                    expressionList = self.visit(ctx.expressionList())
                else:
                    expressionList = []
                return CallExpr(preExpression, accessField, expressionList)
            else:  # Access an attribute
                return FieldAccess(preExpression, accessField)

    def visitStaticAccess(self, ctx: D96Parser.StaticAccessContext):
        preExpression = self.visit(ctx.staticAccess())
        accessField = Id(ctx.DOLAR_IDENTIFIER().getText())
        if ctx.objectCreation():
            return self.visit(ctx.objectCreation())
        else:
            if ctx.LEFT_PAREN():  # Access a function
                if ctx.expressionList():
                    expressionList = self.visit(ctx.expressionList())
                else:
                    expressionList = []
                return CallExpr(preExpression, accessField, expressionList)
            else:  # Access an attribute
                return FieldAccess(preExpression, accessField)

    def visitObjectCreation(self, ctx: D96Parser.ObjectCreationContext):
        if ctx.atomExpr():
            return self.visit(ctx.atomExpr())
        return NewExpr(
            Id(ctx.IDENTIFIER().getText()),
            self.visit(ctx.expressionList()) if ctx.expressionList() else []
        )

    def visitAtomExpr(self, ctx: D96Parser.AtomExprContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.K_NULL():
            return NullLiteral()
        if ctx.K_SELF():
            return SelfLiteral()
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        return self.visit(ctx.expression())

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

    def visitArrayType(self, ctx: D96Parser.ArrayTypeContext):
        size = int(ctx.INTEGER_LITERAL2().getText())
        if ctx.PRIMITIVE_TYPE():
            eleType = convertStringToPrimitiveType(ctx.PRIMITIVE_TYPE().getText())
        elif ctx.arrayType():
            eleType = self.visit(ctx.arrayType())
        else:
            eleType = None
        return ArrayType(size, eleType)
