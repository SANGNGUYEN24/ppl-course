"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from StaticError import *


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
    def __init__(self, name, mtype, value=None, kind=None, isGlobal=False):
        """
        :param name:    string
        :param mtype:   MType | IntType | BoolType | FloatType | StringType | ArrayType
        :param value:   dynamic
        :param kind:    Class | Method | SpecialMethod | Attribute | Parameter | Constant | Variable | Identifier
        """
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.isGlobal = isGlobal

    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ',' + str(self.kind) + ')'

    def getKind(self):
        return self.kind if type(self.kind) is MType else Identifier()

    @staticmethod
    def getClassDeclSymbol(decl):
        return Symbol(name=decl.classname, mtype=ClassType, kind=Class)

    @staticmethod
    def setIsGlobal(self):
        self.isGlobal = True
        return self


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
        classSymbols = [Symbol.getClassDeclSymbol(x) for x in ast.decl]
        classNameList = [i.name for i in classSymbols]
        print("From visitProgram: ", classSymbols)
        for i in range(0, len(classSymbols)):
            if classSymbols[i].name in classNameList[i + 1:]:
                raise Redeclared(k=classSymbols[i].kind,
                                 n=str(classSymbols[i].name.name))
        return []

    def visitClassDecl(self, ast, c):
        print("From visitClassDecl: ", c)
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
