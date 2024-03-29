"""
 * @author nhphung
"""
from pprint import pprint

from AST import *
from Visitor import *
from StaticError import *


class D96Utils:
    @staticmethod
    def isOpForNumber(op):
        return str(op) in ["+", "-", "*", "/", ">", "<", ">=", "<=", "==", "!="]

    @staticmethod
    def isIntOrFloat(t):
        if isinstance(t, IntType) or isinstance(t, FloatType):
            return True
        return False

    @staticmethod
    def mergeNumberType(leftType, rightType):
        return FloatType() if FloatType in [leftType, rightType] else IntType()

    @staticmethod
    def checkTypeMatch(ast, lhsType, rhsType, isConstant=False):
        # print("From checkTypeMatch")
        if isinstance(lhsType, IntType) and isinstance(rhsType, IntType) \
                or isinstance(lhsType, ArrayType) and isinstance(rhsType, ArrayType) \
                or isinstance(lhsType, FloatType) and isinstance(rhsType, FloatType) \
                or isinstance(lhsType, StringType) and isinstance(rhsType, StringType) \
                or isinstance(lhsType, BoolType) and isinstance(rhsType, BoolType):
            return True
        else:
            if isConstant:
                raise TypeMismatchInConstant(ast)
            else:
                raise TypeMismatchInStatement(ast)


"""
Print output for checking
"""


class Scope:
    def __init__(self, enclosingScope=None):
        """
        It is the nearest parent scope
        """
        self.enclosingScope = enclosingScope
        """
        All symbols defined in this scope; can include classes, functions,
        variables, or anything else that is a Symbol impl. It does NOT
        include non-Symbol-based things like LocalScope.
        """
        self.symbols = {}
        """
        All directly contained scopes, typically LocalScopes within a
        LocalScope or a LocalScope within a FunctionSymbol. This does not
        include SymbolWithScope objects.
        """
        self.nestedScopeNotSymbols = []
        self.inLoop = False

    def __str__(self):
        return str(self.symbols.keys())

    """
    Get symbol if name defined in this specific scope
    """

    def getSymbol(self, name):
        return self.symbols.get(name)

    def getSymbols(self):
        return [s for s in self.symbols.values()]

    def getSymbolNames(self):
        return self.symbols.keys()

    def getNumOfSymbols(self):
        return len(self.symbols)

    """
    Add a nested local scope to this scope; it's like define() but
    for non SymbolWithScope objects. E.g., a FunctionSymbol will
    add a LocalScope for its block via this method.
    :return void
    """

    def nest(self, scope):
        if isinstance(scope, SymbolWithScope):
            raise Exception(f"Add SymbolWithScope Instance {scope.name} via define()")
        self.nestedScopeNotSymbols.append(scope)

    def getNestedScopedSymbols(self):
        scopes = []
        for s in self.getSymbols():
            if isinstance(s, Scope):
                scopes.append(s)
        return scopes

    """
    Return a list of scopes nested within this scope
    :return List[Scope]
    """

    def getNestedScopes(self):
        allScopes = [self.getSymbols(), self.nestedScopeNotSymbols]
        return allScopes

    def getOuterMostEnclosingScope(self):
        s = self
        while s.enclosingScope is not None:
            s = s.enclosingScope
        return s

    def getEnclosingPathToRoot(self):
        scopeList = []
        s = self
        while s is not None:
            scopeList.append(s)
            s = s.enclosingScope
        return scopeList

    @staticmethod
    def getNewLocalScope(enclosingScope):
        newScope = LocalScope()
        newScope.enclosingScope = enclosingScope
        return newScope

    """
    Define a Symbol in this scope
    """

    def define(self, symbol):
        # print("----From define----")
        # print("symbol:", symbol)
        kind = None
        symbolName = symbol.name
        if isinstance(symbol, ClassSymbol):
            kind = Class()
        elif isinstance(symbol, MethodSymbol):
            kind = Method()
        elif isinstance(symbol, AttributeSymbol):
            kind = Attribute()
        elif isinstance(symbol, VariableSymbol):
            kind = Variable()
        elif isinstance(symbol, ConstSymbol):
            kind = Constant()
        elif isinstance(symbol, ParameterSymbol):
            kind = Parameter()

        if self.symbols.__contains__(symbolName):
            raise Redeclared(kind, symbolName)
        symbol.scope = self
        self.symbols[symbolName] = symbol

    """
    Look up name in this scope or recursively in parent scope if not here
    """

    def resolve(self, name):
        # print("resolve:", name)
        s = self.symbols.get(name)
        if s is not None: return s
        # If not here, resolve in parent scope
        parent = self.enclosingScope
        if parent is not None:
            return parent.resolve(name)
        else:
            return None


class GlobalScope(Scope):
    name = "global"

    def __init__(self):
        super().__init__()


class LocalScope(Scope):
    name = "local"

    def __init__(self):
        super().__init__()


class MType:
    """
    partype -> param type   ->  List<Type>
    rettype -> return type  ->  Type
    """

    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType([' + ','.join([str(i) for i in self.partype]) + '],' + str(self.rettype) + ')'


class Symbol:
    """
    :param name:    string
    :param mtype:   MType | IntType | BoolType | FloatType | StringType | ArrayType
    :param value:   dynamic
    :param kind:    Class | Method | SpecialMethod | Attribute | Parameter | Constant | Variable | Identifier
    """

    def __init__(self, name, d96Type=None, scope=None, kind=None):
        self.name = name
        self.d96Type = d96Type
        self.scope = scope
        self.kind = kind

    # def __str__(self):
    #     return 'Symbol(' + self.name + ',' + str(self.d96Type) + ',' + str(self.scope) + ',' + str(self.kind) + ')'


class SymbolWithScope(Scope, Symbol):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def getQualifiedName(self):
        return f"{self.enclosingScope.getName()}'.'{self.name}"


class MemberSymbol(Symbol):
    pass


class MethodSymbol(SymbolWithScope, MemberSymbol):
    def __init__(self, name):
        super().__init__(name)


class VariableSymbol(Symbol):
    def __init__(self, name):
        super().__init__(name)


class ConstSymbol(Symbol):
    def __init__(self, name):
        super().__init__(name)


class ParameterSymbol(Symbol):
    def __init__(self, name):
        super().__init__(name)


class AttributeSymbol(Symbol):
    def __init__(self, name, isConstant):
        super().__init__(name)
        self.isConstant = isConstant


class ClassSymbol(SymbolWithScope, MemberSymbol):
    def __init__(self, name, superClassName):
        super().__init__(name)
        self.superClassName = superClassName

    def getSuperClassScope(self):
        if self.superClassName is not None:
            if self.enclosingScope is not None:
                superClass = self.enclosingScope.resolve(self.superClassName)
                if isinstance(superClass, ClassSymbol):
                    return superClass
        return None

    def getSuperClassScopes(self):
        superClassScope = self.getSuperClassScope()
        if superClassScope is not None: return [superClassScope]

    def resolve(self, name):
        s = self.resolveMember(name)
        if s is not None: return s
        # If not here, go to parent scope
        parent = self.enclosingScope
        if parent is not None: return parent.resolve(name)
        return None  # If not found

    """
    Look for a member with this name in this scope or any super class.
    Return null if no member found.
    """

    def resolveMember(self, name):
        s = self.symbols.get(name)
        if isinstance(s, MemberSymbol): return s

        # Traverse super class
        superClassScopes = self.getSuperClassScopes()
        if superClassScopes is not None:
            for ele in superClassScopes:
                s = ele.resolveMember(self.name)
                if isinstance(s, MemberSymbol): return s
        return None

    """
    Look for a field with this name in this scope or any super class.
    Return null if no field found.
    """

    # def resolveField(self, name):
    #     s = self.resolveMember(name)
    #     if isinstance(s, FieldSymbol): return s
    #     return None

    def resolveMethod(self, name):
        s = self.resolveMember(name)
        if isinstance(s, MethodSymbol): return s

    """
    Return the set of all methods defined within this class
    """

    def getAllDefinedMethods(self):
        methods = set()
        for ele in self.getSymbols():
            if isinstance(ele, MemberSymbol):
                methods.add(ele)
        return methods


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.globalScope = GlobalScope()

    def check(self):
        return self.visit(self.ast, self.globalScope)

    def visitProgram(self, ast, presentScope):
        TAG = "----visitProgram----"
        # print(TAG)
        # print("Program presentScope before: ")
        # p#print(presentScope.symbols)
        # If Program class is not present, raise NoEntryPoint
        hasProgramClass = False
        for ele in ast.decl:
            if ele.classname.name == "Program":
                hasProgramClass = True
                break
        if hasProgramClass:
            for ele in ast.decl:  # ele is ClassDecl
                classSymbol = ClassSymbol(name=ele.classname.name,
                                          superClassName=ele.parentname.name if ele.parentname is not None else None)
                presentScope.define(classSymbol)
                newScope = Scope.getNewLocalScope(enclosingScope=presentScope)
                classSymbol.scope = newScope
                self.visit(ele, newScope)
        else:
            raise NoEntryPoint()

        # print(TAG)
        # print("Program presentScope after: ")
        # p#print(presentScope.symbols)
        return []

    def visitClassDecl(self, ast, presentScope):
        TAG = "----visitClassDecl----"
        # print(TAG, ast.classname.name)
        # print("ast:")
        # p#print(ast)
        # print("Class presentScope before: ")
        # p#print(presentScope.symbols)
        # Check super class exist
        if ast.parentname is not None:
            if presentScope.enclosingScope.symbols.get(ast.parentname.name) is None:
                raise Undeclared(k=Class(), n=ast.parentname.name)
        # Check Program class condition
        if ast.classname.name == "Program":
            hasMain = False
            # Visit body
            for ele in ast.memlist:
                # Visit attribute
                if isinstance(ele, AttributeDecl):
                    decl = ele.decl
                    if isinstance(decl, ConstDecl):
                        constType = decl.constType
                        value = decl.value
                        valueType = self.visit(value, presentScope)
                        if D96Utils.checkTypeMatch(ast=decl, lhsType=constType, rhsType=valueType, isConstant=True):
                            attributeSymbol = AttributeSymbol(name=decl.constant.name, isConstant=True)
                            attributeSymbol.d96Type = valueType
                            presentScope.define(attributeSymbol)
                    elif isinstance(decl, VarDecl):
                        varType = decl.varType
                        varInit = decl.varInit
                        if varInit is not None:
                            varInitType = self.visit(varInit, presentScope)
                            D96Utils.checkTypeMatch(ast=ele, lhsType=varType, rhsType=varInitType)
                        else:
                            varInitType = None
                        attributeSymbol = AttributeSymbol(name=decl.variable.name, isConstant=False)
                        attributeSymbol.d96Type = varInitType
                        presentScope.define(attributeSymbol)
                # Visit method
                elif isinstance(ele, MethodDecl):
                    # TODO lack condition about return void
                    if ele.name.name == "main" and len(ele.param) == 0:
                        hasMain = True
                        mainMethodSymbol = MethodSymbol(name="main")
                        newScope = Scope.getNewLocalScope(enclosingScope=presentScope)
                        presentScope.define(mainMethodSymbol)
                        self.visit(ele, newScope)
                    elif ele.name.name != "main":
                        methodSymbol = MethodSymbol(name=ele.name.name)
                        presentScope.define(methodSymbol)
                        newScope = Scope.getNewLocalScope(enclosingScope=presentScope)
                        methodSymbol.scope = newScope
                        self.visit(ele, newScope)
            if not hasMain:
                raise NoEntryPoint()
        else:  # Other class
            # Visit body
            for ele in ast.memlist:
                # Visit attribute
                if isinstance(ele, AttributeDecl):
                    decl = ele.decl
                    if isinstance(decl, ConstDecl):
                        constType = decl.constType
                        value = decl.value
                        valueType = self.visit(value, presentScope)
                        if D96Utils.checkTypeMatch(ast=decl, lhsType=constType, rhsType=valueType, isConstant=True):
                            attributeSymbol = AttributeSymbol(name=decl.constant.name, isConstant=True)
                            attributeSymbol.d96Type = valueType
                            presentScope.define(attributeSymbol)
                    elif isinstance(decl, VarDecl):
                        varType = decl.varType
                        varInit = decl.varInit
                        if varInit is not None:
                            varInitType = self.visit(varInit, presentScope)
                            D96Utils.checkTypeMatch(ast=ele, lhsType=varType, rhsType=varInitType)
                        else:
                            varInitType = None
                        # if D96Utils.checkTypeMatch(ast=decl, lhsType=varType, rhsType=varInitType):
                        attributeSymbol = AttributeSymbol(name=decl.variable.name, isConstant=False)
                        attributeSymbol.d96Type = varInitType
                        presentScope.define(attributeSymbol)
                # Visit method
                elif isinstance(ele, MethodDecl):
                    methodSymbol = MethodSymbol(name=ele.name.name)
                    presentScope.define(methodSymbol)
                    newScope = Scope.getNewLocalScope(enclosingScope=presentScope)
                    methodSymbol.scope = newScope
                    self.visit(ele, newScope)

        # print("Class presentScope after: ")
        # p#print(presentScope.symbols)
        return []

    def visitMethodDecl(self, ast, presentScope):
        TAG = "----visitMethodDecl----"
        # print(TAG, ast.name.name)
        # print("ast:")
        # p#print(ast)
        # print("Method presentScope before: ")
        # p#print(presentScope.symbols)

        for ele in ast.param:
            paramSymbol = ParameterSymbol(name=ele.variable.name)
            presentScope.define(paramSymbol)

        # print("presentScope after param loop: ")
        # p#print(presentScope.symbols)

        for ele in ast.body.inst:
            # symbol = None
            if isinstance(ele, VarDecl):
                varType = ele.varType
                varInit = ele.varInit
                # print("varType:", varType)
                # print("varInit:", varInit)
                if varInit is not None:
                    varInitType = self.visit(varInit, presentScope)
                    D96Utils.checkTypeMatch(ast=ele, lhsType=varType, rhsType=varInitType)
                else:
                    varInitType = None

                varSymbol = VariableSymbol(name=ele.variable.name)
                varSymbol.d96Type = varInitType
                presentScope.define(varSymbol)
            elif isinstance(ele, ConstDecl):
                # constType = ele.constType
                value = ele.value
                if value is None:
                    raise IllegalConstantExpression(None)

                constType = ele.constType
                # value = ele.value
                valueType = self.visit(value, presentScope)
                if D96Utils.checkTypeMatch(ast=ele, lhsType=constType, rhsType=valueType, isConstant=True):
                    attributeSymbol = ConstSymbol(name=ele.constant.name)
                    attributeSymbol.d96Type = valueType
                    presentScope.define(attributeSymbol)

            elif isinstance(ele, Block):
                newScope = Scope.getNewLocalScope(enclosingScope=presentScope)
                self.visit(ele, newScope)
            elif isinstance(ele, Assign):
                self.visit(ele, presentScope)
            elif isinstance(ele, If) or isinstance(ele, For):
                newScope = Scope.getNewLocalScope(enclosingScope=presentScope)
                self.visit(ele, newScope)
            elif isinstance(ele, Break):
                raise MustInLoop(ele)
            elif isinstance(ele, Return):
                self.visit(ele, presentScope)
            else:
                self.visit(ele, presentScope)

        # print("Method presentScope after: ")
        # p#print(presentScope.symbols)

        return []

    def visitAssign(self, ast: Assign, presentScope):
        # print("Hello")
        lhs = ast.lhs
        if isinstance(lhs, Id):
            s = presentScope.resolve(lhs.name)
            # print("s: ", s)
            if s is None:
                raise Undeclared(Identifier(), n=lhs.name)
            if isinstance(s, AttributeSymbol):
                if s.isConstant:
                    raise CannotAssignToConstant(ast)
                else:
                    self.visit(ast, presentScope)
            elif isinstance(s, ConstSymbol):
                raise CannotAssignToConstant(ast)
            else:
                self.visit(ast, presentScope)
        return []

    def visitVarDecl(self, ast, presentScope):
        TAG = "----visitVarDecl----"
        # print(TAG)
        # print("ast:")
        # p#print(ast)

        if presentScope.resolve(ast.variable.name) is not None:
            raise Redeclared(Variable(), n=ast.variable.name)

        varInit = ast.varInit
        # print("ast.varInit: ", varInit)
        if varInit is not None:
            self.visit(varInit, presentScope)

        return []

    def visitConstDecl(self, ast, presentScope):
        TAG = "----visitConstDecl----"
        # print(TAG)
        # print("ast:")
        # p#print(ast)

        if presentScope.resolve(ast.constant.name) is not None:
            raise Redeclared(Variable(), n=ast.constant.name)

        value = ast.value
        # print("ast.varInit: ", value)
        if value is not None:
            self.visit(value, presentScope)

        return []

    def visitId(self, ast, presentScope):
        # print("----visitId----")
        # print("ast: ", ast)
        idSymbol = presentScope.resolve(ast.name)
        # print("idSymbol: ", idSymbol)
        if idSymbol is None:
            raise Undeclared(Identifier(), ast.name)
        return idSymbol.d96Type

    def visitBinaryOp(self, ast, presentScope):
        # print("----visitBinaryOp----")
        leftType = self.visit(ast.left, presentScope)
        rightType = self.visit(ast.right, presentScope)
        # print("leftType:", leftType)
        # print("rightType:", rightType)
        op = ast.op
        # print("op: ", op)

        if D96Utils.isOpForNumber(op):
            if D96Utils.isIntOrFloat(leftType) is False or D96Utils.isIntOrFloat(rightType) is False:
                raise TypeMismatchInExpression(ast)
            if str(op) == '%':
                if FloatType in [leftType, rightType]:
                    raise TypeMismatchInExpression(ast)
                return IntType()
            if op in ['+', '-', '*', '/']: return D96Utils.mergeNumberType(leftType, rightType)
            return BoolType()  # For op like =, <,>, <=,...
        if not isinstance(leftType, BoolType) and not isinstance(rightType, BoolType):
            raise TypeMismatchInExpression(ast)

        return BoolType()

    def visitFieldAccess(self, ast, presentScope):
        # print("----visitFieldAccess----")
        # print("ast: ", ast)
        # Get scope of field obj
        objSymbol = presentScope.resolve(ast.obj.name)
        if objSymbol is None:
            raise Undeclared(Class(), ast.obj.name)
        else:
            fieldSymbol = objSymbol.scope.resolve(ast.fieldname.name)
            if not isinstance(fieldSymbol, AttributeSymbol):
                raise Undeclared(k=Attribute(), n=ast.fieldname.name)
            # print("d96Type:", fieldSymbol.d96Type)
            return fieldSymbol.d96Type

    def visitCallExpr(self, ast, presentScope):
        # print("----visitCallExpr----")
        # print("ast:", ast)
        objSymbol = presentScope.resolve(ast.obj.name)
        if objSymbol is None:
            raise Undeclared(Class(), ast.obj.name)
        else:
            symbol = objSymbol.scope.resolve(ast.method.name)
            # print("methodSymbol:", symbol)
            if not isinstance(symbol, MethodSymbol):
                raise Undeclared(k=Method(), n=ast.method.name)

    def visitIf(self, ast: If, presentScope):
        # print("----visitIf----")
        # print("ast:", ast)
        conditionType = self.visit(ast.expr, presentScope)
        # print("conditionType:", conditionType)
        if type(conditionType) is not BoolType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.thenStmt, LocalScope())
        self.visit(ast.elseStmt, LocalScope())

        # print("thenStmt:", thenStmt)
        # print("elseStmt:", elseStmt)

    def visitBlock(self, ast: Block, presentScope):
        return [self.visit(x, presentScope) for x in ast.inst]

    def visitFor(self, ast : For, presentScope):
        scalarVarSymbol = presentScope.resolve(ast.id.name)
        if scalarVarSymbol is None:
            return Undeclared(Variable(), ast.id.name)
        expr1Type = self.visit(ast.expr1, presentScope)
        expr2Type = self.visit(ast.expr2, presentScope)
        if not isinstance(expr1Type, IntType) or isinstance(expr2Type, IntType):
            raise TypeMismatchInStatement(ast)

        return []

    def visitCallStmt(self, ast, presentScope):
        objSymbol = presentScope.resolve(ast.obj.name)
        if objSymbol is None:
            raise Undeclared(Class(), ast.obj.name)
        else:
            symbol = objSymbol.scope.resolve(ast.method.name)
            # print("methodSymbol:", symbol)
            if not isinstance(symbol, MethodSymbol):
                raise Undeclared(k=Method(), n=ast.method.name)

    def visitUnaryOp(self, ast : UnaryOp, presentScope):
        op = str(ast.op)
        expType = self.visit(ast.body, presentScope)
        if (op == '-' and not D96Utils.isIntOrFloat(expType)) or (op == '!' and type(expType) is not BoolType):
            raise TypeMismatchInExpression(ast)
        return expType

    def visitIntLiteral(self, ast, presentScope):
        return IntType()

    def visitFloatLiteral(self, ast, presentScope):
        return FloatType()

    def visitStringLiteral(self, ast, presentScope):
        return StringType()

    def visitBooleanLiteral(self, ast, presentScope):
        return BoolType()
