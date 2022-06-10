'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC


class Scope:
    def __init__(self, enclosingScope=None):
        self.name = None
        self.enclosingScope = enclosingScope
        self.symbols = {}
        self.nestedScopeNotSymbols = []
        self.inLoop = False

    @staticmethod
    def resolve(self, name: str):
        # print("resolve:", name)
        s = self.symbols.get(name)
        if s is not None: return s
        # If not here, resolve in parent scope
        parent = self.enclosingScope
        if parent is not None:
            return parent.resolve(name)
        else:
            return None


class Symbol:
    def __init__(self, name: str, typee: Type, value, scope: Scope = None):
        self.name = name
        self.typee = typee
        self.value = value
        self.scope = scope


class CodeGenerator(Utils):
    def __init__(self):
        self.globalScope = Scope(None)

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String
        gc = CodeGenVisitor(ast, self.globalScope, dir_)
        gc.visit(ast, None)


class ArrayPointerType(Type):
    def __init__(self, ctype):
        # cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def visit(self, v, param):
        return None


class SubBody():
    def __init__(self, frame, sym):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, curscope, isLeft, isFirst: False):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.sym = None
        self.frame = frame
        self.curscope = curscope
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        # value: Int

        self.value = value


class CName(Val):
    def __init__(self, value):
        # value: String

        self.value = value


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, path):
        # astTree: AST
        # env: List[Symbol]
        # dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = path
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast: Program, c):
        # ast: Program
        # c: Any
        currentScope = self.env
        for ele in ast.decl:
            self.visit(currentScope, ele)
        self.emit.emitEPILOG()
        return c

    def visitClassDecl(self, ast: ClassDecl, presentScope):
        global parentSym
        className = ast.classname.name
        parentClass = ast.parentname
        if className == "Program":
            self.emit.printout(self.emit.emitPROLOG(className, ""))
        else:
            parentName = str()
            parentSym = None
            if parentClass is not None:
                parentName, parentType = ast.parentname.name
                parentSym = resolve(c, parentName)
            self.emit.printout(self.emit.emitPROLOG(className, parentName))
        currentScope = Scope()
        c.symbols.append(Symbol(className, None, None, currentScope))

        for member in ast.memlist:
            member.visit(self, currentScope)
        return c

    def visitAttributeDecl(self, ast: AttributeDecl, c: Scope):
        attrName, attrType, isFinal, rhs = ast.decl.visit(self, c)
        if type(ast.kind) is Instance:
            c.symbols[attrName] = Symbol(attrName, attrType, CName(c.name))
            self.emit.printout(self.emit.emitATTRIBUTE(
                attrName, attrType, isFinal, False))
            if rhs[0]:
                self.emit.printout(rhs[0])
                self.emit.printout(self.emit.emitPUTFIELD(
                    attrName, attrType, None))
        else:
            c.symbols[attrName] = Symbol(attrName, attrType, CName(c.name))
            self.emit.printout(self.emit.emitATTRIBUTE(
                attrName, attrType, isFinal, True))
            if rhs[0]:
                self.emit.printout(rhs[0])
                self.emit.printout(self.emit.emitPUTSTATIC(
                    attrName, attrType, None))
        return c

    def visitMethodDecl(self, ast: MethodDecl, c: Scope):
        methodName = ast.name.name
        paramType = []
        for par in ast.param:
            paramType.append(par.varType.visit(self, self.env))
        returnType = None
        for stmt in ast.body.inst:
            if isinstance(stmt, Return):
                _, returnType = stmt.expr.visit(
                    self, Access(None, c, False, False))  # Note
                break
        methodType = MType(paramType, returnType)
        currScope = Scope(c)
        methodSym = Symbol(methodName, methodType, CName(c.name), currScope)
        c.symbols[methodName] = methodSym
        # Pre_syms = Flatten(c) ## Need to ilement
        message = SubBody(Frame(methodName, returnType), currScope)
        isStatic = True
        if isinstance(ast.kind, Instance):
            isStatic = False
            message.frame.getNewIndex()

        self.emit.printout(self.emit.emitMETHOD(
            methodName, methodType, isStatic))
        message.frame.enterScope(True)
        for param in ast.param:
            paramName, paramType, isFinal, _ = param.visit(self, message)
            currScope.symbols[paramName] = Symbol(paramName, paramType, Index(message.frame.getCurrIndex()))
            self.emit.printout(self.emit.emitVAR(message.frame.getCurrIndex(), paramName, paramType,
                                                 message.frame.getStartLabel(), message.frame.getEndLabel(), isFinal))
            message.frame.getNewIndex()
        self.emit.printout(self.emit.emitLABEL(
            message.frame.getStartLabel(), message.frame))
        for stmt in ast.body.inst:
            stmt.visit(self, message)
        self.emit.printout(self.emit.emitLABEL(
            message.frame.getEndLabel(), message.frame))
        self.emit.printout(self.emit.emitENDMETHOD(message.frame))
        message.frame.exitScope()
        return c

    def visitVarDecl(self, ast: VarDecl, c):
        if isinstance(c, Scope):
            varName = ast.variable.name
            varType = ast.varType.visit(self, Access(None, c, False, False))
            varInit = ast.varInit.visit(self, Access(None, c, False, False)) if ast.varInit else [None, None]
            return varName, varType, False, varInit
        else:
            frame = c.frame
            access = Access(frame, c.sym, isLeft=True, isFirst=True)
            varName = ast.variable.name
            varType = ast.varType.visit(self, None)
            access.sym.symbols[varName] = Symbol(varName, varType, frame.getCurrIndex())
            self.emit.printout(self.emit.emitVAR(frame.getCurrIndex(
            ), varName, varType, frame.getStartLabel(), frame.getEndLabel(), False))
            if ast.varInit:
                varInit = ast.varInit(self, access)
                self.emit.printout(varInit[0])
                self.emit.printout(self.emit.emitWRITEVAR(
                    varName, varType, frame.getCurrIndex(), frame))
            frame.getNewIndex()

    def visitConstDecl(self, ast: ConstDecl, c):
        if isinstance(c, Scope):
            varName = ast.constant.name
            varType = ast.constType.visit(self, Access(None, c, False, False))
            varInit = ast.value.visit(self, c) if ast.value else varInit = [None, None]
            return varName, varType, False, varInit
        else:
            frame = c.frame
            access = Access(frame, c.sym, isLeft=None, isFirst=None)
            varName = ast.constant.name
            varType = ast.constType.visit(self, None)
            access.sym.symbols[varName] = Symbol(varName, varType, frame.getCurrIndex())
            self.emit.printout(self.emit.emitVAR(frame.getCurrIndex(
            ), varName, varType, frame.getStartLabel(), frame.getEndLabel(), False))
            if ast.varInit:
                varInit = ast.value(self, access)
                self.emit.printout(varInit[0])
                self.emit.printout(self.emit.emitWRITEVAR(
                    varName, varType, frame.getCurrIndex(), frame))
            frame.getNewIndex()
            return None

    def visitBlock(self, ast: Block, c: SubBody):  # c is a Subody
        frame = c.frame
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        currScope = Scope(c.sym)
        message = SubBody(frame, currScope)
        for stmt in ast.inst:
            stmt.visit(self, message)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        return None

    def visitUnaryOp(self, ast: UnaryOp, c: Access):
        exprCode, exprType = self.visit(ast.body, c)
        if ast.op == '-':
            return exprCode + self.emit.emitNEGOP(exprType, c.frame), exprType
        else:
            return exprCode + self.emit.emitNOT(exprType, c.frame), exprType

    def visitCallExpr(self, ast: CallExpr, c):
        objCode, objType = ast.obj.visit(
            self, Access(c.frame, c.sym, False, True))
        self.emit.printout(objCode)
        objSym = c.resolve(c.sym, objType.name)
        methodSym = c.resolve(objSym.scope, ast.method.name)
        paramType = methodSym.typee.partype
        paramCode = ""

        for idx, param in enumerate(ast.param):
            pCode, pType = param.visit(
                self, Access(c.frame, c.sym, False, True))
            if type(paramType[idx]) is FloatType and type(pType) is IntType:
                pCode = pCode + self.emit.emitI2F(c.frame)
            paramCode += pCode

        if methodSym.name[0] == "$":
            invokeCode = self.emit.emitINVOKESTATIC(
                objType.name + "/" + methodSym.name, methodSym.typee, c.frame)
        else:
            invokeCode = self.emit.emitINVOKEVIRTUAL(
                objType.name + "/" + methodSym.name, methodSym.typee, c.frame)
        return objCode + paramCode + invokeCode, methodSym.typee.rettype

    def visitCallStmt(self, ast: CallStmt, c: SubBody):
        objCode, objType = ast.obj.visit(
            self, Access(c.frame, c.sym, False, True))
        self.emit.printout(objCode)
        objSym = c.resolve(c.sym, objType.name)
        methodSym = c.resolve(objSym.scope, ast.method.name)
        paramType = methodSym.typee.partype
        paramCode = ""

        for idx, param in enumerate(ast.param):
            pCode, pType = param.visit(
                self, Access(c.frame, c.sym, False, True))
            if type(paramType[idx]) is FloatType and type(pType) is IntType:
                pCode = pCode + self.emit.emitI2F(c.frame)
            paramCode += pCode

        if methodSym.name[0] == "$":
            invokeCode = self.emit.emitINVOKESTATIC(
                objType.name + "/" + methodSym.name, methodSym.typee, c.frame)
        else:
            invokeCode = self.emit.emitINVOKEVIRTUAL(
                objType.name + "/" + methodSym.name, methodSym.typee, c.frame)
        self.emit.printout(objCode + paramCode + invokeCode)
        return None

    def visitNewExpr(self, ast: NewExpr, c: Access):
        newCode = self.emit.emitNEW(ast.classname.name, c.frame)
        classSym = resolve(self.env, ast.classname.name)
        initSym = resolve(classSym.scope, "<init>")
        paramType = initSym.typee.partype
        paramCode = ""

        for idx, param in enumerate(ast.param):
            pCode, pType = param.visit(self, c)
            if type(paramType[idx]) is FloatType and type(pType) is IntType:
                pCode = pCode + self.emit.emitI2F(c.frame)
            paramCode += pCode
        return newCode + paramCode + self.emit.emitINVOKESPECIAL(c.frame, ast.classname.name + '/' + "<init>",
                                                                 initSym.typee)

    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        pass

    def visitNullLiteral(self, ast: NullLiteral, c):
        pass

    def visitSelfLiteral(self, ast: SelfLiteral, c):
        pass

    def visitId(self, ast: Id, o: Access):
        frame, symbols = o.frame, o.sym
        isLeft = o.isLeft
        isFirst = o.isFirst
        sym = self.lookup(ast.name.lower(), symbols, lambda x: x.name.lower())

        if not isFirst and isLeft:
            frame.push()
        elif not isFirst and not isLeft:
            frame.pop()
        isArrayType = type(sym.mtype) is ArrayType
        emitType = symbols
        if sym.value is None:  # not index -> global var - static field # NOTE: WHY is None but bot String?
            if isLeft and not isArrayType:
                retCode = self.emit.emitPUTSTATIC(
                    self.className + "/" + sym.name, emitType, frame)
            else:
                retCode = self.emit.emitGETSTATIC(
                    self.className + "/" + sym.name, emitType, frame)
        else:
            if isLeft and not isArrayType:
                retCode = self.emit.emitWRITEVAR(
                    sym.name, emitType, sym.value.value, frame)
            else:
                retCode = self.emit.emitREADVAR(
                    sym.name, emitType, sym.value.value, frame)

        return retCode, sym.mtype

    def visitArrayCell(self, ast: ArrayCell, c):
        pass

    def visitFieldAccess(self, ast: FieldAccess, c):
        pass

    def visitIf(self, ast: If, o: SubBody):
        frame, nEnv = o.frame, o.sym

        ifCode, _ = self.visit(ast.expr, Access(frame, nEnv, False, True))
        self.emit.printout(ifCode)

        labelThen, labelEnd = frame.getNewLabel(), frame.getNewLabel()
        self.emit.printout(self.emit.emitIFTRUE(labelThen, frame))
        ast.elseStmt.visit(self, o)
        self.emit.printout(self.emit.emitGOTO(labelEnd, frame))
        self.emit.printout(self.emit.emitLABEL(labelThen, frame))
        ast.thenStmt.visit(self, o)
        self.emit.printout(self.emit.emitLABEL(labelEnd, frame))
        return None

    def visitFor(self, ast: For, o: SubBody):
        # id: Id
        # expr1: Expr
        # expr2: Expr
        # loop: Stmt
        # expr3: Expr = None
        frame, nEnv = o.frame, o.sym

        e1Code, _ = self.visit(ast.expr1, Access(frame, nEnv, False, True))
        e2Code, _ = self.visit(ast.expr2, Access(frame, nEnv, False, True))
        e3Code = None
        if ast.expr3:
            e3Code, _ = self.visit(ast.expr3, Access(frame, nEnv, False, True))
        lhsWriteCode, _ = self.visit(ast.id, Access(
            frame, nEnv, True, True))
        lhsReadCode, _ = self.visit(ast.id, Access(
            frame, nEnv, False, False))

        self.emit.printout(e1Code)
        self.emit.printout(lhsWriteCode)

        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(
            frame.getContinueLabel(), frame))

        self.emit.printout(lhsReadCode)
        self.emit.printout(e2Code)
        self.emit.printout(self.emit.emitIFICMPGT(
            frame.getBreakLabel(), frame))

        loopStmtList = [self.visit(x, o) for x in ast.loop]
        hasReturnStmt = True in loopStmtList

        self.emit.printout(lhsReadCode)
        if ast.expr3:
            self.emit.printout(e3Code)
        else:
            self.emit.printout(self.emit.emitPUSHICONST(1, frame))
        self.emit.printout(self.emit.emitADDOP('+', IntType(), frame))
        self.emit.printout(lhsWriteCode)

        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(
                frame.getContinueLabel(), frame))  # loop
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitBreak(self, ast: Break, o: SubBody):
        self.emit.printout(self.emit.emitGOTO(
            o.frame.getBreakLabel(), o.frame))

    def visitContinue(self, ast: Continue, o: SubBody):
        self.emit.printout(self.emit.emitGOTO(
            o.frame.getContinueLabel(), o.frame))

    def visitAssign(self, ast: Assign, o: SubBody):
        frame, nEnv = o.frame, o.sym
        isArray, _ = self.visit(ast.lhs, Access(
            frame, nEnv, True, True))

        exprCode, expType = self.visit(
            ast.exp, Access(frame, nEnv, False, True))
        lhsCode, lhsType = self.visit(ast.lhs, Access(frame, nEnv, True, True))

        if type(lhsType) is FloatType and type(expType) is IntType:  # Coerce int -> float
            exprCode = exprCode + self.emit.emitI2F(frame)

        if not isArray:
            self.emit.printout(exprCode + lhsCode)
        else:
            self.emit.printout(lhsCode[0] + exprCode + lhsCode[1])
            [frame.pop() for x in range(0, 2)]

    def visitReturn(self, ast: Return, o: SubBody):
        frame, nEnv = o.frame, o.sym
        if ast.expr:
            exprCode, exprType = self.visit(
                ast.expr, Access(frame, nEnv, False, True))
            self.emit.printout(exprCode)
        else:
            exprType = VoidType()
        self.emit.printout(self.emit.emitRETURN(exprType, frame))
        return None if type(exprType) == VoidType else exprType

    def visitIntLiteral(self, ast: IntLiteral, c: Access):
        return self.emit.emitPUSHICONST(str(ast.value), c.frame), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, c: Access):
        return self.emit.emitPUSHFCONST(str(ast.value), c.frame), FloatType()

    def visitStringLiteral(self, ast: StringLiteral, c: Access):
        frame = c.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, c: Access):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), c.frame), BoolType()
