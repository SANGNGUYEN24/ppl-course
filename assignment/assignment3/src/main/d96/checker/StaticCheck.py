"""
 * @author nhphung
"""
from pprint import pprint

from AST import *
from Visitor import *
from StaticError import *

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
        print(TAG)
        print("Program presentScope before: ")
        pprint(presentScope.symbols)
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
                self.visit(ele, newScope)
        else:
            raise NoEntryPoint()

        print(TAG)
        print("Program presentScope after: ")
        pprint(presentScope.symbols)

    def visitClassDecl(self, ast, presentScope):
        TAG = "----visitClassDecl----"
        print(TAG, ast.classname.name)
        print("ast:")
        pprint(ast)
        print("Class presentScope before: ")
        pprint(presentScope.symbols)
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
                    if isinstance(ele.decl, ConstDecl):
                        attributeSymbol = AttributeSymbol(name=ele.decl.constant.name, isConstant=True)
                        presentScope.define(attributeSymbol)
                    else:
                        attributeSymbol = AttributeSymbol(name=ele.decl.variable.name, isConstant=False)
                        presentScope.define(attributeSymbol)
                # Visit method
                elif isinstance(ele, MethodDecl):
                    # TODO lack condition about return void
                    if ele.name.name == "main" and len(ele.param) == 0:
                        hasMain = True
                        mainMethodSymbol = MethodSymbol(name="main")
                        presentScope.define(mainMethodSymbol)
                    elif ele.name.name != "main":
                        methodSymbol = MethodSymbol(name=ele.name.name)
                        presentScope.define(methodSymbol)
            if not hasMain:
                raise NoEntryPoint()
        else:  # Other class
            # Visit body
            for ele in ast.memlist:
                # Visit attribute
                if isinstance(ele, AttributeDecl):
                    decl = ele.decl
                    if isinstance(decl, ConstDecl):
                        value = decl.value
                        # If error exist in value, it is raised in self.visit
                        # TODO check type of the value
                        self.visit(value, presentScope)
                        attributeSymbol = AttributeSymbol(name=decl.constant.name, isConstant=True)
                        presentScope.define(attributeSymbol)
                    elif isinstance(decl, VarDecl):
                        varInit = decl.varInit
                        self.visit(varInit, presentScope)
                        attributeSymbol = AttributeSymbol(name=decl.variable.name, isConstant=False)
                        presentScope.define(attributeSymbol)
                # Visit method
                elif isinstance(ele, MethodDecl):
                    methodSymbol = MethodSymbol(name=ele.name.name)
                    presentScope.define(methodSymbol)
                    newScope = Scope.getNewLocalScope(enclosingScope=presentScope)
                    self.visit(ele, newScope)

        print("Class presentScope after: ")
        pprint(presentScope.symbols)

    def visitMethodDecl(self, ast, presentScope):
        TAG = "----visitMethodDecl----"
        print(TAG, ast.name.name)
        print("ast:")
        pprint(ast)
        print("Method presentScope before: ")
        pprint(presentScope.symbols)

        for ele in ast.param:
            paramSymbol = ParameterSymbol(name=ele.variable.name)
            presentScope.define(paramSymbol)

        print("presentScope after param loop: ")
        pprint(presentScope.symbols)

        for ele in ast.body.inst:
            # symbol = None
            if isinstance(ele, VarDecl):
                self.visit(ele, presentScope)
            elif isinstance(ele, ConstDecl):
                constType = ele.constType
                constValue = ele.value
                if constValue is None:
                    raise IllegalConstantExpression(None)
                if isinstance(constType, IntType) and isinstance(constValue, IntLiteral) \
                        or isinstance(constType, FloatType) and isinstance(constValue, FloatLiteral) \
                        or isinstance(constType, StringType) and isinstance(constValue, StringLiteral) \
                        or isinstance(constType, BoolType) and isinstance(constValue, BooleanLiteral):
                    presentScope.define(ConstSymbol(name=ele.constant.name))
                else:
                    raise TypeMismatchInConstant(constdecl=ele)
            elif isinstance(ele, Block):
                newScope = Scope.getNewLocalScope(enclosingScope=presentScope)
                self.visit(ele, newScope)
            elif isinstance(ele, Assign):
                # print("Enclosing Scope Symbols:")
                # pprint(presentScope.enclosingScope.symbols)
                if isinstance(ele.lhs, Id):
                    s = presentScope.resolve(ele.lhs.name)
                    if isinstance(s, AttributeSymbol):
                        if s.isConstant:
                            raise CannotAssignToConstant(ele)
                        else:
                            self.visit(ele, presentScope)
                    elif isinstance(s, ConstSymbol):
                        raise CannotAssignToConstant(ele)
                    else:
                        self.visit(ele, presentScope)

        print("Method presentScope after: ")
        pprint(presentScope.symbols)

        return []

    def visitAssign(self, ast, presentScope):
        return []

    def visitVarDecl(self, ast, presentScope):
        TAG = "----visitVarDecl----"
        print(TAG, ast.name)
        print("ast:")
        pprint(ast)

        varInit = ast.varInit
        print("ast.varInit: ", varInit)
        if isinstance(varInit, Id):
            self.visit(varInit, presentScope)

        varSymbol = VariableSymbol(name=ast.variable.name)
        presentScope.define(varSymbol)

    def visitId(self, ast, presentScope):
        idSymbol = presentScope.resolve(ast.name)
        if idSymbol is None:
            raise Undeclared(Identifier(), ast.name)
        return idSymbol

    def visitBinaryOp(self, ast, presentScope):
        pass

    def visitIntLiteral(self, ast, presentScope):
        return IntType()

    def visitFloatLiteral(self, ast, presentScope):
        return FloatType()

    def visitStringLiteral(self, ast, presentScope):
        return StringType()

    def visitBooleanLiteral(self, ast, presentScope):
        return BoolType()
