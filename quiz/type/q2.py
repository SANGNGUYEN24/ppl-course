import enum

class Operator:
    numericOp = ['+', '-', '*', '/']  # Return int or float type
    boolOp = ['&&', '||']  # Get 2 bool return bool
    sameOperandTypeOp = ['>', '<', '==', '!=']  # Get 2 any same type return bool
    unaryNumOp = '-'
    unaryBoolOp = '!'

class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o):
        declared = [self.visit(x, None) for x in ctx.decl]
        self.visit(ctx.exp, declared)

    def visitVarDecl(self, ctx: VarDecl, o):
        return ctx.name, self.visit(ctx.typ, None)

    def visitIntType(self, ctx: IntType, o):
        return IntType()

    def visitFloatType(self, ctx: FloatType, o):
        return FloatType()

    def visitBoolType(self, ctx: BoolType, o):
        return BoolType()

    def visitBinOp(self, ctx: BinOp, o):
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)
        op = ctx.op
        if op in Operator.numericOp:
            if type(e1) in [IntType, FloatType] and type(e2) in [IntType, FloatType]:
                if op == '/':
                    return FloatType()
                elif type(e1) is IntType and type(e2) is IntType:
                    return IntType()
                else:
                    return FloatType()

            raise TypeMismatchInExpression(ctx)
        elif op in Operator.boolOp:
            if type(e1) is BoolType and type(e2) is BoolType:
                return BoolType()

            raise TypeMismatchInExpression(ctx)
        elif op in Operator.sameOperandTypeOp:
            if type(e1) == type(e2):
                return BoolType()

            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx: UnOp, o):
        e = self.visit(ctx.e, o)
        op = ctx.op
        if op == '-':
            if type(e) is IntType:
                return IntType()
            elif type(e) is FloatType:
                return FloatType()

            raise TypeMismatchInExpression(ctx)
        elif op == '!':
            if type(e) is BoolType:
                return BoolType()

            raise TypeMismatchInExpression(ctx)

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitBoolLit(self, ctx: Id, o):
        return BoolType()

    def visitId(self, ctx, o):
        for i in range(len(o)):
            if ctx.name == o[i][0]:
                return o[i][1]
        raise UndeclaredIdentifier(ctx.name)