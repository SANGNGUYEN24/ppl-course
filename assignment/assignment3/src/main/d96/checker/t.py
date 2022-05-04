#c1
def visitId(self, ctx, o):
    for i in o.sym:
        if i.name == ctx.name:
            if o.isLeft == False:
                if isinstance(i.value.value, int):
                    return self.emit.emitREADVAR(i.name, i.mtype, i.value.value, o.frame), i.mtype
                return self.emit.emitGETSTATIC(i.value.value + '/' + i.name, i.mtype, o.frame), i.mtype
            else:
                if isinstance(i.value.value, int):
                    return self.emit.emitWRITEVAR(i.name, i.mtype, i.value.value, o.frame), i.mtype
                return self.emit.emitPUTSTATIC(i.value.value + '/' + i.name, i.mtype, o.frame), i.mtype
#c2
    def visitAssign(self,ctx,o):
        la = Access(o.frame,o.sym,True)
        ra = Access(o.frame,o.sym,False)
        rhs = ctx.rhs.accept(self,ra)
        lhs = ctx.lhs.accept(self,la)
        return self.emit.printout(rhs[0] + lhs[0])

# c3
def visitIf(self, ctx, o):
    ifExpCode, ifExpType = ctx.expr.accept(self, Access(o.frame, o.sym, False))

    if ctx.estmt:
        labelElse = o.frame.getNewLabel()
        labelExit = o.frame.getNewLabel()

        self.emit.printout(ifExpCode)
        self.emit.printout(
            self.emit.emitIFFALSE(labelElse, o.frame))
        ctx.tstmt.accept(self, o)
        self.emit.printout(self.emit.emitGOTO(labelExit, o.frame))
        self.emit.printout(self.emit.emitLABEL(labelElse, o.frame))
        ctx.estmt.accept(self, o)
        self.emit.printout(self.emit.emitLABEL(labelExit, o.frame))
    else:
        labelExit = o.frame.getNewLabel()

        self.emit.printout(ifExpCode)
        self.emit.printout(self.emit.emitIFFALSE(labelExit, o.frame))
        ctx.tstmt.accept(self, o)
        self.emit.printout(self.emit.emitLABEL(labelExit, o.frame))

    # c4
    def visitWhile(self, ctx, o):
        o.frame.enterLoop()

        exitLabel = o.frame.getBreakLabel()

        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame))

        ifExpCode, ifExpType = ctx.expr.accept(self, Access(o.frame, o.sym, False))
        self.emit.printout(ifExpCode)

        self.emit.printout(self.emit.emitIFFALSE(exitLabel, o.frame))

        ctx.stmt.accept(self, o)

        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

        self.emit.printout(self.emit.emitLABEL(exitLabel, o.frame))

        o.frame.exitLoop()


# c5
def visitFuncDecl(self, ctx, o):
    paraType = list(map(lambda x: x.typ, ctx.param))
    funcType = MType(paraType, ctx.returnType)

    self.emit.printout(self.emit.emitMETHOD(ctx.name, funcType, True))

    message = SubBody(Frame(ctx.name, ctx.returnType), o.sym.copy())
    message.frame.enterScope(True)

    paraSymbolList = list(map(lambda x: x.accept(self, message),
                              ctx.param))
    message.sym[:0] = paraSymbolList[::-1]

    varSymbolList = list(map(lambda x: x.accept(self, message), ctx.body[0]))
    message.sym[:0] = varSymbolList[::-1]

    self.emit.printout(self.emit.emitLABEL(message.frame.getStartLabel(),
                                           message.frame))

    list(map(lambda b: b.accept(self, message), ctx.body[1]))

    self.emit.printout(self.emit.emitLABEL(message.frame.getEndLabel(), message.frame))

    self.emit.printout(self.emit.emitENDMETHOD(message.frame))

    return Symbol(ctx.name, funcType, CName(self.className))


# c6
def visitBinExpr(self, ctx, o):
    op = ctx.op
    if op in ['+', '-', '+.', '-.']:
        if len(lex) > 1: lex = lex[0]  # remove dot if necessary
        lhsCode, lhsType = ctx.e1.accept(self, o)
        rhsCode, rhsType = ctx.e2.accept(self, o)
        return lhsCode + rhsCode + self.emit.emitADDOP(lex, lhsType, o.frame), lhsType
    elif op in ['', '\\', '.', '\\.']:
        if len(lex) > 1: lex = lex[0]  # remove dot if necessary
        lhsCode, lhsType = ctx.e1.accept(self, o)
        rhsCode, rhsType = ctx.e2.accept(self, o)
        return lhsCode + rhsCode + self.emit.emitMULOP(lex, lhsType, o.frame), lhsType
    elif op in ['%']:
        lhsCode, lhsType = ctx.e1.accept(self, o)
        rhsCode, rhsType = ctx.e2.accept(self, o)
        return lhsCode + rhsCode + self.emit.emitMOD(o.frame), lhsType
    elif op in ['>', '<', '==', '>=', '<=', '!=']:
        lhsCode, lhsType = ctx.e1.accept(self, o)
        rhsCode, rhsType = ctx.e2.accept(self, o)
        return lhsCode + rhsCode + self.emit.emitREOP(ctx.op, lhsType, o.frame), BoolType()
    elif op in ['>.', '<.', '>=.', '<=.', '=/=']:
        lhsCode, lhsType = ctx.e1.accept(self, o)
        rhsCode, rhsType = ctx.e2.accept(self, o)
        return lhsCode + rhsCode + self.emit.emitREFOP(ctx.op, lhsType, o.frame), BoolType()
    elif op in ['&&']:  # short-circuit evaluation
        labelF = o.frame.getNewLabel()
        labelO = o.frame.getNewLabel()

        lhsCode, lhsType = ctx.e1.accept(self, o)
        jCode = lhsCode  # put left expr boolean value on to stack
        jCode += self.emit.emitIFFALSE(labelF, o.frame)  # conclude false when left is false

        rhsCode, rhsType = ctx.e2.accept(self, o)
        jCode += rhsCode  # put right expr boolean value on to stack

        jCode += self.emit.emitIFFALSE(labelF, o.frame)

        jCode += self.emit.emitPUSHICONST(1, o.frame)
        o.frame.pop()
        jCode += self.emit.emitGOTO(labelO, o.frame)

        jCode += self.emit.emitLABEL(labelF, o.frame)
        jCode += self.emit.emitPUSHICONST(0, o.frame)
        jCode += self.emit.emitLABEL(labelO, o.frame)
        return jCode, BoolType()

    elif op in ['||']:  # short-circuit evaluation
        labelT = o.frame.getNewLabel()
        labelO = o.frame.getNewLabel()

        lhsCode, lhsType = ctx.e1.accept(self, o)
        jCode = lhsCode  # put left expr boolean value on to stack
        jCode += self.emit.emitIFTRUE(labelT, o.frame)  # conclude false when left is false

        rhsCode, rhsType = ctx.e2.accept(self, o)
        jCode += rhsCode  # put right expr boolean value on to stack

        jCode += self.emit.emitIFTRUE(labelT, o.frame)

        jCode += self.emit.emitPUSHICONST(0, o.frame)
        o.frame.pop()
        jCode += self.emit.emitGOTO(labelO, o.frame)

        jCode += self.emit.emitLABEL(labelT, o.frame)
        jCode += self.emit.emitPUSHICONST(1, o.frame)
        jCode += self.emit.emitLABEL(labelO, o.frame)
        return jCode, BoolType()
