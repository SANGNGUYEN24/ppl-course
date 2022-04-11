from typing import Dict, Tuple

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


class Func:
    def __init__(self, name: str, param: Dict[str, type]):
        self.name = name
        self.param = param

    def __str__(self):
        return "Func(" + self.name + "[" + ",".join((n + ":" + str(t)) for n, t in self.param.items()) + "])"


class Scope:
    def __init__(self, name=None):
        self.name: str = name
        self.outer: Scope = None
        self.env: Dict[str, type] = {}
        self.funcs: Dict[str, Func] = {}

    def assignType(self, n: str, t: type, ):
        current = self
        funcName = None
        while current:

            # check param in func first
            if funcName and funcName in current.funcs:
                func = current.funcs[funcName]
                if n in func.param:
                    func.param[n] = t
                    return True

            if n in current.env:
                current.env[n] = t
                return True

            funcName = current.name
            current = current.outer
        return False

    def getType(self, name: str, returnVal=None):
        current = self
        funcName = None
        while current:
            if name in current.env:
                return current.env[name]
            if funcName and funcName in current.funcs:
                func = current.funcs[funcName]
                if name in func.param:
                    return func.param[name]

            funcName = current.name
            current = current.outer

        if returnVal != None:
            return returnVal
        raise Exception("Not found ", name)

    def getFunc(self, n):
        current = self
        while current:
            if n in current.funcs:
                return current.funcs[n]
            current = current.outer
        return None

    def __str__(self):
        return "Scope(" + \
               "-N(" + str(self.name) + ")" + \
               "-O(" + str(self.outer) + ")" + \
               "-E(" + ",".join((n + ":" + (t.__name__ if t else str(None))) for n, t in self.env.items()) + ")" + \
               "-F(" + ",".join((n + ":" + str(f)) for n, f in self.funcs.items()) + "))"


class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        scope = Scope()
        is_param = False
        for dec in ctx.decl:
            self.visit(dec, (scope, is_param) if isinstance(dec, VarDecl) else scope)

        for stmt in ctx.stmts:
            self.visit(stmt, scope)

    def visitVarDecl(self, ctx: VarDecl, o: Tuple[Scope, bool]):
        scope, is_param = o
        if ctx.name in scope.env:
            raise Redeclared(ctx)
        if scope.name:  # this scope is Func
            f = scope.getFunc(scope.name)
            if f and (ctx.name in f.param):  # if exist
                raise Redeclared(ctx)
            if f and is_param:  # put the param into its func-decl
                f.param[ctx.name] = None
                return
        # normal vardecl
        scope.env[ctx.name] = None

    def visitAssign(self, ctx: Assign, o):
        r = self.visit(ctx.rhs, o)  # visit RHS first
        l = self.visit(ctx.lhs, o)

        if r is None:
            if type(ctx.rhs) == Id:
                if l is not None:
                    o.assignType(ctx.rhs.name, l)
                    return
                raise TypeCannotBeInferred(ctx)
            raise TypeMismatchInStatement(ctx)

        if l is None:
            o.assignType(ctx.lhs.name, r)
            return

        if l != r:
            raise TypeMismatchInStatement(ctx)

    def visitFuncDecl(self, ctx: FuncDecl, o: Scope):
        scope = Scope(ctx.name)  # create scope for local
        o.funcs[ctx.name] = Func(ctx.name, {})  # assign func-decl to the outer-scope

        if ctx.name in o.env:
            raise Redeclared(ctx)
        if o.name:  # this outer-scope is Func
            f = scope.getFunc(scope.name)
            if f and (ctx.name in f.param):  # if exist
                raise Redeclared(ctx)

        o.env[ctx.name] = Func

        scope.outer = o
        scope.env[ctx.name] = Func  # needed to check re-decl (if same name with this func)

        is_param = True
        for par in ctx.param:
            self.visit(par, (scope, is_param))

        is_param = False
        for dec in ctx.local:
            self.visit(dec, (scope, is_param) if isinstance(dec, VarDecl) else scope)

        for stmt in ctx.stmts:
            self.visit(stmt, scope)

    def visitCallStmt(self, ctx: CallStmt, o: Scope):
        func = o.getFunc(ctx.name)
        # check func-name
        if func is None:
            raise UndeclaredIdentifier(ctx.name)
        # check if num-param
        if len(func.param) != len(ctx.args):
            raise TypeMismatchInStatement(ctx)
        for _name, _type, _arg in zip(func.param.keys(), func.param.values(), ctx.args):
            _arg_type = self.visit(_arg, o)
            if _arg_type is None:
                if type(_arg) == Id:
                    if _type is not None:
                        o.assignType(_arg.name, _type)
                        continue
                raise TypeCannotBeInferred(ctx)

            if _type is None:
                func.param[_name] = _arg_type
                continue

            if _type != _arg_type:
                raise TypeMismatchInStatement(ctx)

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

    def visitId(self, ctx, o: Scope):
        t = o.getType(name=ctx.name, returnVal=False)
        if t != False:
            return t
        raise UndeclaredIdentifier(ctx.name)