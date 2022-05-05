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
    globalScope = GlobalScope()

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.globalScope)

    def visitProgram(self, ast, presentScope):
        TAG = "----visitProgram----"
        for ele in ast.decl:  # ele is ClassDecl
            classSymbol = ClassSymbol(name=ele.classname,
                                      superClassName=ele.parentname.name if ele.parentname is not None else None)
            presentScope.symbols[classSymbol.name.name] = classSymbol
            self.visit(ele, presentScope)
        pprint(presentScope.symbols)
        print(TAG)
        return []

    def visitClassDecl(self, ast, presentScope):
        TAG = "----visitClassDecl----"
        # Check super class exist
        if presentScope.symbols.get(ast.parentname.name) is None:
            raise Undeclared(k=Class(), n=ast.parentname.name)
        # Create a local scope in this class
        localScope = LocalScope()
        print(TAG, ast.classname.name)
        # localScope.symbols = {}
        # pprint(bigSymbolTable.symbols)


    def visitFuncDecl(self, ast, presentScope):
        return list(map(lambda x: self.visit(x, (c, True)), ast.body.stmt))

    def visitCallExpr(self, ast, presentScope):
        at = [self.visit(x, (c[0], False)) for x in ast.param]

        res = self.lookup(ast.method.name, presentScope[0], lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(), ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

    def visitIntLiteral(self, ast, presentScope):
        return IntType()
