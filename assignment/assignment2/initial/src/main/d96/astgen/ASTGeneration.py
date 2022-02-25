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
        if ctx.expression(1):
            return [self.visit(x) for x in ctx.expression()]
        return ctx.expression()

    def visitElementExpression(self, ctx: D96Parser.ElementExpressionContext):
        return ArrayCell(
            self.visit(ctx.expression()),
            self.visit(ctx.indexOperator())
        )

    def visitIndexOperator(self, ctx: D96Parser.IndexOperatorContext):
        return [self.visit(x) for x in ctx.expression()]

    def visitExpression(self, ctx: D96Parser.ExpressionContext):
        if ctx.relationalExpr(0):
            if ctx.OP_STRING_CONCATENATION():
                operator = ctx.OP_STRING_CONCATENATION().getText()
            else:
                operator = ctx.OP_TWO_SAME_STRING().getText()

            return BinaryOp(
                operator,
                self.visit(ctx.relationalExpr(0)),
                self.visit(ctx.relationalExpr(1))
            )
        return self.visit(ctx.relationalExpr())

    def visitRelationalOperator(self, ctx: D96Parser.RelationalOperatorContext):
        if ctx.OP_IS_EQUAL_TO():
            operator = ctx.OP_IS_EQUAL_TO()
        elif ctx.OP_NOT_EQUAL_TO():
            operator = ctx.OP_NOT_EQUAL_TO()
        elif ctx.OP_LESS_THAN():
            operator = ctx.OP_LESS_THAN()
        elif ctx.OP_LESS_THAN_EQUAL():
            operator = ctx.OP_LESS_THAN_EQUAL()
        elif ctx.OP_GREATER_THAN():
            operator = ctx.OP_GREATER_THAN()
        else:
            operator = ctx.OP_GREATER_THAN_EQUAL()
        return operator.getText()

    def visitRelationalExpr(self, ctx: D96Parser.RelationalExprContext):
        if ctx.andOrExpr(0):
            operator = self.visit(ctx.relationalOperator())
            return BinaryOp(
                operator,
                self.visit(ctx.andOrExpr(0)),
                self.visit(ctx.andOrExpr(1))
            )
        return self.visit(ctx.andOrExpr())

    def visitAndOrExpr(self, ctx: D96Parser.AndOrExprContext):
        if ctx.addSubExpr():
            if ctx.OP_LOGICAL_AND():
                operator = ctx.OP_LOGICAL_AND().getText()
            else:
                operator = ctx.OP_LOGICAL_OR().getText()

            return BinaryOp(
                operator,
                self.visit(ctx.andOrExpr()),
                self.visit(ctx.addSubExpr())
            )
        return self.visit(ctx.addSubExpr())

    def visitAddSubExpr(self, ctx: D96Parser.AddSubExprContext):
        if ctx.addSubExpr():
            if ctx.OP_SUBTRACTION():
                operator = ctx.OP_SUBTRACTION().getText()
            else:
                operator = ctx.OP_ADDTION().getText()

            return BinaryOp(
                operator,
                self.visit(ctx.addSubExpr()),
                self.visit(ctx.mulAddMolExpr())
            )
        return self.visit(ctx.mulAddMolExpr())

    def visitMulAddMolExpr(self, ctx: D96Parser.MulAddMolExprContext):
        if ctx.mulAddMolExpr():
            if ctx.OP_MULTIPLICATION():
                operator = ctx.OP_MULTIPLICATION().getText()
            elif ctx.OP_MODULO():
                operator = ctx.OP_MODULO().getText()
            else:
                operator = ctx.OP_DIVISION().getText()

            return BinaryOp(
                operator,
                self.visit(ctx.mulAddMolExpr()),
                self.visit(ctx.notExpr())
            )
        return self.visit(ctx.notExpr())

    def visitNotExpr(self, ctx: D96Parser.NotExprContext):
        if ctx.signExpr():
            return self.visit(ctx.signExpr())
        return UnaryOp(
            ctx.OP_LOGICAL_NOT().getText(),
            self.visit(ctx.notExpr())
        )

    def visitSignExpr(self, ctx: D96Parser.SignExprContext):
        if ctx.indexOperatorExpr():
            return self.visit(ctx.indexOperatorExpr())
        operator = ctx.OP_SUBTRACTION().getText() if ctx.OP_SUBTRACTION() else ctx.OP_ADDTION().getText()
        return UnaryOp(
            operator,
            self.visit(ctx.signExpr())
        )

    def visitIndexOperatorExpr(self, ctx: D96Parser.IndexOperatorExprContext):
        if ctx.indexOperator():
            return ArrayCell(
                self.visit(ctx.instanceAccess()),
                self.visit(ctx.indexOperator())
            )
        return self.visit(ctx.instanceAccess())

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
        d96Type = self.visit(ctx.d96Type())
        if ctx.IDENTIFIER(1):
            identifierList = [self.visit(x) for x in ctx.IDENTIFIER()]
            print("identifierList", identifierList)
        else:
            identifierList = [self.visit(ctx.IDENTIFIER(0))]
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

    def visitLhs(self, ctx: D96Parser.LhsContext):
        if ctx.instanceAccess():
            if ctx.IDENTIFIER():
                return FieldAccess(
                    self.visit(ctx.instanceAccess()),
                    Id(ctx.IDENTIFIER().getText())
                )
            else:
                return FieldAccess(
                    self.visit(ctx.instanceAccess()),
                    Id(ctx.DOLAR_IDENTIFIER().getText())
                )
        if ctx.elementExpression():
            return self.visit(ctx.elementExpression())

        return Id(ctx.IDENTIFIER().getText())

    def visitAssignStatement(self, ctx: D96Parser.AssignStatementContext):
        return Assign(
            self.visit(ctx.lhs()),
            self.visit(ctx.expression())
        )

    def visitIfStatement(self, ctx: D96Parser.IfStatementContext):
        return If(
            self.visit(ctx.expression()),
            self.visit(ctx.blockStatement()),
            self.visit(ctx.blockStatement()) if ctx.K_ELSE() else None
        )

    def visitForInStatement(self, ctx: D96Parser.ForInStatementContext):
        return For(
            Id(ctx.IDENTIFIER().getText()),
            self.visit(ctx.expression(0)),
            self.visit(ctx.expression(1)),
            self.visit(ctx.blockStatement()),
            self.visit(ctx.expression(2)) if ctx.expression(2) else None
        )

    def visitBreakStatement(self, ctx: D96Parser.BreakStatementContext):
        return Break()

    def visitContinueStatement(self, ctx: D96Parser.ContinueStatementContext):
        return Continue()

    def visitReturnStatement(self, ctx: D96Parser.ReturnStatementContext):
        expression = self.visit(ctx.expression()) if ctx.expression() else None
        return Return(expression)

    def visitMethodInvocationStatement(self, ctx: D96Parser.MethodInvocationStatementContext):
        return self.visit(ctx.instanceAccess())

    def visitBlockStatement(self, ctx: D96Parser.BlockStatementContext):
        return [self.visit(child) for child in ctx.statement()]

    def visitStatement(self, ctx: D96Parser.StatementContext):
        if ctx.varValStatement():
            child = ctx.varValStatement()
        elif ctx.assignStatement():
            child = ctx.assignStatement()
        elif ctx.ifStatement():
            child = ctx.ifStatement()
        elif ctx.forInStatement():
            child = ctx.forInStatement()
        elif ctx.breakStatement():
            child = ctx.breakStatement()
        elif ctx.continueStatement():
            child = ctx.continueStatement()
        elif ctx.returnStatement():
            child = ctx.continueStatement()
        elif ctx.methodInvocationStatement():
            child = ctx.methodInvocationStatement()
        else:
            child = ctx.blockStatement()
        return self.visit(child)

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
        if ctx.INTEGER_LITERAL():
            destinations = ctx.INTEGER_LITERAL()
        elif ctx.INTEGER_LITERAL2():
            destinations = ctx.INTEGER_LITERAL2()
        elif ctx.FLOAT_LITERAL():
            destinations = ctx.FLOAT_LITERAL()
        elif ctx.BOOLEAN_LITERAL():
            destinations = ctx.BOOLEAN_LITERAL()
        elif ctx.STRING_LITERAL():
            destinations = ctx.STRING_LITERAL()
        else:
            destinations = ctx.indexedArray()

        return ArrayLiteral(
            [self.visit(child) for child in destinations]
        )

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
