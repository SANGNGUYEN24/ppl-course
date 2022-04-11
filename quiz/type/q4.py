operatorRules = {
    '+': (int, int),
    '-': (int, int),
    '*': (int, int),
    '/': (int, int),
    '+.': (float, float),
    '-.': (float, float),
    '*.': (float, float),
    '/.': (float, float),
    '>': (int, bool),
    '=': (int, bool),
    '>.': (float, bool),
    '=.': (float, bool),
    '=b': (bool, bool),
    '>b': (bool, bool),
    '!': (bool, bool),
    '&&': (bool, bool),
    '||': (bool, bool),
    'i2f': (int, float),
    'floor': (float, int),
}


class Scope:
    def __init__(self):
        self.scope: Scope = None
        self.varType: dict[str, type] = {}

    def assignType(self, var, typ):
        current = self
        while current:
            if var in current.varType:
                current.varType[var] = typ
                return True
            current = current.scope
        return False

    def get(self, var: str, right=None):
        current = self
        while current:
            if var in current.varType:
                return current.varType[var]
            current = current.scope

        if right is not None:
            return right
        raise Exception("Not found ", var)


class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        scope = Scope()
        for dec in ctx.decl:
            self.visit(dec, scope)
        for stmt in ctx.stmts:
            self.visit(stmt, scope)

    def visitVarDecl(self, ctx: VarDecl, o):
        if ctx.name in o.varType:
            raise Redeclared(ctx)
        o.varType[ctx.name] = None

    def visitAssign(self, ctx: Assign, o):
        right = self.visit(ctx.rhs, o)  # visit RHS first
        left = self.visit(ctx.lhs, o)

        if right is None:
            if type(ctx.rhs) == Id:
                if left is not None:
                    o.assignType(ctx.rhs.name, left)
                    return
                raise TypeCannotBeInferred(ctx)
            raise TypeMismatchInStatement(ctx)

        if left is None:
            o.assignType(ctx.lhs.name, right)
            return

        if left != right:
            raise TypeMismatchInStatement(ctx)

    def visitBlock(self, ctx: Block, o):
        scope = Scope()
        scope.scope = o

        for dec in ctx.decl:
            self.visit(dec, scope)
        for stmt in ctx.stmts:
            self.visit(stmt, scope)

    def visitBinOp(self, ctx: BinOp, o):
        leftType = ctx.e1.accept(self, o)
        rightType = ctx.e2.accept(self, o)
        if ctx.op in operatorRules:
            _accept, _return = operatorRules[ctx.op]
            if leftType is None:
                leftType = _accept
                o.assignType(ctx.e1.name, _accept)
            if rightType is None:
                rightType = _accept
                o.assignType(ctx.e2.name, _accept)
            if leftType is _accept and rightType is _accept:
                return _return

        raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx: UnOp, o):
        ele = ctx.e.accept(self, o)
        if ctx.op in operatorRules:
            _accept, _return = operatorRules[ctx.op]

            if ele is None:
                o.assign(ctx.e.name, _accept)
                return _return

            if ele is _accept:
                return _return

        raise TypeMismatchInExpression(ctx)

    def visitIntLit(self, ctx: IntLit, o):
        return int

    def visitFloatLit(self, ctx, o):
        return float

    def visitBoolLit(self, ctx, o):
        return bool

    def visitId(self, ctx, o):
        t = o.get(ctx.name, "nil")
        if t != "nil":
            return t
        raise UndeclaredIdentifier(ctx.name)