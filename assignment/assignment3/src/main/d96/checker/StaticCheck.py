"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from StaticError import *


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

    """
    Define a Symbol in this scope
    """

    def define(self, symbol):
        if self.symbols.__contains__(symbol.name):
            raise Redeclared(symbol.kind, symbol.name)
        symbol.scope = self
        self.symbols[symbol.name] = symbol

    """
    Look up name in this scope or recursively in parent scope if not here
    """

    def resolve(self, name):
        s = self.symbols.get(name)
        if s is not None: return s
        # If not here, resolve in parent scope
        parent = self.enclosingScope
        if parent is not None: parent.resolve(name)
        return None


class GlobalScope(Scope):
    name = "global"

    def __init__(self, scope):
        super().__init__(scope)


class LocalScope(Scope):
    name = "local"

    def __init__(self, scope):
        super().__init__(scope)


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

    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ',' + str(self.kind) + ')'


class SymbolWithScope(Scope, Symbol):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def getQualifiedName(self):
        return f"{self.enclosingScope.getName()}'.'{self.name}"


class MemberSymbol(Symbol):
    pass


class MethodSymbol(MemberSymbol):
    def __init__(self, name):
        super().__init__(name)


class VariableSymbol(Symbol):
    def __init__(self, name):
        super().__init__(name)


class ParameterSymbol(VariableSymbol):
    def __init__(self, name):
        super().__init__(name)


class FieldSymbol(VariableSymbol, MemberSymbol):
    def __init__(self, name):
        super().__init__(name)


class ClassSymbol(SymbolWithScope, MemberSymbol):
    superClassName: str

    def __init__(self, name):
        super().__init__(name)

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

    def resolveField(self, name):
        s = self.resolveMember(name)
        if isinstance(s, FieldSymbol): return s
        return None

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
    global_envi = [
        # Symbol("getInt", MType([], IntType())),
        # Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        print("From visitProgram/ast.decl: ", ast.decl)
        classSymbols = [Symbol.getClassDeclSymbol(x) for x in ast.decl]
        classNameList = [i.name for i in classSymbols]
        print("From visitProgram/classSymbols ", classSymbols)
        for x in ast.decl:
            self.visit(x, c)

        # for i in range(0, len(classSymbols)):
        #     if classSymbols[i].name in classNameList[i + 1:]:
        #         raise Redeclared(k=classSymbols[i].kind,
        #                          n=str(classSymbols[i].name.name))
        return []

    def visitClassDecl(self, ast, c):
        print("From visitClassDecl/ast: ", ast)

        return 0

    def visitFuncDecl(self, ast, c):
        return list(map(lambda x: self.visit(x, (c, True)), ast.body.stmt))

    def visitCallExpr(self, ast, c):
        at = [self.visit(x, (c[0], False)) for x in ast.param]

        res = self.lookup(ast.method.name, c[0], lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(), ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

    def visitIntLiteral(self, ast, c):
        return IntType()
