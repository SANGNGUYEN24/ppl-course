'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from lib2to3.pygram import Symbols
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class Scope:
    def __init__(self, name: str = "", syms: List[Symbol] = [], outerScope : str = None):
       self.name = name
       self.syms = syms 
       self.outerScope = outerScope

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def scopeTable(self):
        return Scope("Global")
        # return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
        #             Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
        #             Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName))
        #             ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class StringType(Type):
    
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym, isGlobal):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal

class Access():
    def __init__(self, frame, sym, isLeft, isFirst, isArrayType=False):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean
        #checkArrayType: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
        self.isArrayType = isArrayType

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast: Program, o):
        #ast: Program
        #c: Any
        [self.visit(mem, o) for mem in ast.memlist]
        self.emit.emitEPILOG()
        return o
        
    # classname: Id
    # memlist: List[MemDecl]
    # parentname: Id = None  # None if there is no parent
    def visitClassDecl(self, ast:ClassDecl, o):
        pClass = ast.parentname if ast.parentname else "" # "" automatically java/land/Object
        self.emit.printout(self.emit.emitPROLOG(ast.classname, pClass))

        for decl in ast.decl:
            self.visit(decl, Scope(ast.classname, {}))
        self.genMETHOD(MethodDecl(Static(), Id("<init>"), list(), Block(list())), e, Frame("<init>", VoidType))
    
    # MOITOIDAY
    def visitMethodDecl(self, ast: MethodDecl, o: Scope):
        # find return type:
        partype = [i.varType for i in ast.param]
        returnTypes = [self.visit(stmt, o) for stmt in ast.body]
        if isinstance(stmt, Return):
        #TODO: Get returtntype in if stmt, for stmt
        retType = VoidType()
        for i in returnTypes:
            if i != None: 
                retType = i
                break
        frame = Frame(ast.name, retType)
        o.syms.append([Symbol(ast.name, MType(partype, retType))])

        isInit = type(retType) is VoidType
        isMain = ast.name.name == "main" and len(methodDecl.param) == 0 and type(methodDecl.returnType) is VoidType
        returnType = VoidType() if isInit else methodDecl.returnType
        methodName = "<init>" if isInit else methodDecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        # self.genMETHOD(ast, subctxt.sym, frame)
        # return SubBody(None, [Symbol(ast.name, MType(paramSyms, retType), CName(self.className))] + subctxt.sym)
    
    def visitVarDecl(self, ast: VarDecl, o):
        pass
        
    def genMETHOD(self, methodDecl: MethodDecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        # isInit = consdecl.returnType is None 
        isInit = methodDecl.returnType is None
        isMain = methodDecl.name.name == "main" and len(methodDecl.param) == 0 and type(methodDecl.returnType) is VoidType
        returnType = VoidType() if isInit else methodDecl.returnType
        methodName = "<init>" if isInit else methodDecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        body = methodDecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

############################## Stmts ##############################    
# param: o: Subody(frame, sym)

    def visitCallStmt(self, ast: CallStmt, o: SubBody):
        self.call(ast, o.frame, o.sym, _isStmt=True)

    def call(self, ast, frame, syms, _isStmt=False):
        # ast: CallStmt or CallExpr
        # NOTE:lower() -> Lowercase of String 
        sym = self.lookup(ast.method.name.lower(), syms, lambda x: x.name.lower())
        cname = sym.value.value
        methodType = sym.mtype

        paramTypes = methodType.partype
        paramsCode = ""
        for idx, param in enumerate(ast.param):
            pCode, pType = self.visit(param, Access(frame, syms, False, True))
            if type(paramTypes[idx]) is FloatType and type(pType) is IntType:
                pCode = pCode + self.emit.emitI2F(frame) #NOTE: WHY i2f. -> coerce ref param type and actual param type
            # if type(paramTypes[idx]) is ArrayType: pass
            paramsCode = paramsCode + pCode
        
        # if sym.name.lower() == "main": ctype = MType([ArrayPointerType(StringType())], VoidType())
        callCode = paramsCode + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, methodType, frame) 
        if _isStmt: self.emit.printout(callCode)
        else: return callCode, methodType.rettype
    
    def visitReturn(self, ast: Return, o: SubBody):
        frame, nenv = o.frame, o.sym
        if ast.expr:
            exprCode, exprType = self.visit(ast.expr, Access(frame, nenv, False, True))
            self.emit.printout(exprCode)
        else: exprType = VoidType()
        self.emit.printout(self.emit.emitRETURN(exprType, frame))
        return None if type(exprType) == VoidType else exprType

    def visitIf(self, ast: If, o: SubBody):
        frame, nenv = o.frame, o.sym
        
        ifCode, _ = self.visit(ast.expr, Access(frame, nenv, False, True))
        self.emit.printout(ifCode)

        labelThen, labelEnd = frame.getNewLabel(), frame.getNewLabel()
        self.emit.printout(self.emit.emitIFTRUE(labelThen, frame))
        # False -> Do Else stmt
        if isinstance(ast.elseStmt, list):
            elseStmtRetList = [self.visit(x, o) for x in ast.elseStmt]
        else: elseStmtRetList = self.visit(ast.elseStmt, o)
        if not any(elseStmtRetList):
            self.emit.printout(self.emit.emitGOTO(labelEnd, frame)) # go to end
        self.emit.printout(self.emit.emitGOTO(labelEnd, frame)) 
        # Then stmt
        self.emit.printout(self.emit.emitLABEL(labelThen, frame))
        thenStmtRetList = [self.visit(x, o) for x in ast.thenStmt]

        self.emit.printout(self.emit.emitLABEL(labelEnd, frame))
        retType = None
        for ret in elseStmtRetList + thenStmtRetList:
            if ret != None:
                retType = ret
                break
        return retType

    def visitFor(self, ast: For, o: SubBody): # Protected var in forloop stmt
        # id: Id
        # expr1: Expr
        # expr2: Expr 
        # loop: Stmt
        # expr3: Expr = None
        frame, nenv = o.frame, o.sym

        e1Code, _ = self.visit(ast.expr1, Access(frame, nenv, False, True))
        e2Code, _ = self.visit(ast.expr2, Access(frame, nenv, False, True))
        e3Code = None
        if ast.expr3: e3Code, _ = self.visit(ast.expr3, Access(frame, nenv, False, True))
        #TODO: WHat is isFirst? I guess isFirst = True-> initialzation
        lhsWriteCode, _ = self.visit(ast.id, Access(frame, nenv, True, True)) # Write code
        lhsReadCode, _ = self.visit(ast.id, Access(frame, nenv, False, False)) # Read code
        
        # Initialize scalar variable, assign expr1 to lhs
        self.emit.printout(e1Code)
        self.emit.printout(lhsWriteCode)

        frame.enterLoop()
        # labelCont:
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))

        # if lhs > e2
        self.emit.printout(lhsReadCode)
        self.emit.printout(e2Code)
        self.emit.printout(self.emit.emitIFICMPGT(frame.getBreakLabel(), frame))

        # Do loop stmts
        loopStmtList = [self.visit(x, o) for x in ast.loop]
        hasReturnStmt = True in loopStmtList

        # Increment scalar variable
        self.emit.printout(lhsReadCode)
        if ast.expr3: self.emit.printout(e3Code)
        else: self.emit.printout(self.emit.emitPUSHICONST(1, frame))
        self.emit.printout(self.emit.emitADDOP('+', IntType(), frame))
        self.emit.printout(lhsWriteCode) # NOTE: Why? pop() -> pop (lhs + e3) above from stack and store it in
        
        # goto LabelCont
        if not hasReturnStmt: self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame)) # loop
        
        # LabelBreak:
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitBreak(self, ast: Break, o: SubBody):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))

    def visitContinue(self, ast: Continue, o: SubBody):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    #TODO: change checkArrayType in Access to isArrayType, MOITOIDAY
    def visitAssign(self, ast: Assign, o: SubBody):
        frame, nenv = o.frame, o.sym
        # stack: ..., arrayref, index, value -> ...
        isArray, _ = self.visit(ast.lhs, Access(frame, nenv, True, True, isArrayType=True))
        # simulate to push 2 slot for arrayref and index, visit exp first
        if isArray: [frame.push() for _ in range(0,2)]

        # Visit lhs: Id or ArrayCell or static attribute or instance attribute
        exprCode, expType = self.visit(ast.exp, Access(frame, nenv, False, True))
        lhsCode, lhsType = self.visit(ast.lhs, Access(frame, nenv, True, True))

        if type(lhsType) is FloatType and type(expType) is IntType: # Coerce int -> float
            exprCode = exprCode + self.emit.emitI2F(frame)

        if not isArray: self.emit.printout(exprCode + lhsCode)
        else:
            self.emit.printout(lhsCode[0] + exprCode + lhsCode[1])
            # recover stack status
            [frame.pop() for _ in range(0,2)]

############################## Expr ##############################    
# Param: o: Access(frame, sym, isLeft, isFirst)
# Return: (code, type)

    def visitId(self, ast: Id, o: Access):
        # Return (name, type, index)
        frame, symbols = o.frame, o.sym
        isLeft = o.isLeft
        isFirst = o.isFirst

        if isLeft and o.checkArrayType: return False, None

        sym = self.lookup(ast.name.lower(), symbols, lambda x: x.name.lower())

        # recover status of stack in frame. # FIXME: FOR WHAT?
        if not isFirst and isLeft: frame.push() # because a = 2; emitWRITEVAR will pop() -> need to push first
        elif not isFirst and not isLeft: frame.pop() # a.call(), x = a, load value of a onto stack (push) =>  nees to pop? Why isFirst = False?
        isArrayType = type(sym.mtype) is ArrayType
        emitType = StupidUtils.retrieveType(sym.mtype)
        if sym.value is None: # not index -> global var - static field # NOTE: WHY is None but bot String?
            if isLeft and not isArrayType: retCode = self.emit.emitPUTSTATIC(self.className + "/" + sym.name, emitType, frame)
            else: retCode = self.emit.emitGETSTATIC(self.className + "/" + sym.name, emitType, frame)
        else:
            if isLeft and not isArrayType: retCode = self.emit.emitWRITEVAR(sym.name, emitType, sym.value.value, frame)
            else: retCode = self.emit.emitREADVAR(sym.name, emitType, sym.value.value, frame)

        return retCode, sym.mtype

    def visitArrayCell(self, ast: ArrayCell, o: Access):
        """
            1. store to array
            aload_ + iconst_
            expr # visitAssign will insert
            iastore

            2. load array
            aload_ + iconst_ + iaload
        """
        frame, symbols = o.frame, o.sym
        isLeft = o.isLeft

        if isLeft and o.checkArrayType: return True, None # FIXME: Why return  true, None (code, type) ????

        arrayCode, arrayType = self.visit(ast.arr, Access(frame, symbols, True, True))
        idxCode, _ = self.visit(ast.idx, Access(frame, symbols, False, True))

        if isLeft: # lhs: a[0] = 100 => aload_0 \n iconst_0 \n bipush 100 \n iastore
            return [arrayCode + idxCode, self.emit.emitASTORE(arrayType.eleType, frame)], arrayType.eleType
        # rhs: b = a[0] => aload_0 \n iconst_0 \n iaload istore_1
        return arrayCode + idxCode + self.emit.emitALOAD(arrayType.eleType, frame), arrayType.eleType

    def visitCallExpr(self, ast: CallExpr, o: Access):
        frame, symbols = o.frame, o.sym
        return self.call(ast, frame, symbols, _isStmt=False)

    def visitBinaryOp(self, ast: BinaryOp, o: Access):
        frame = o.frame
        op = ast.op
        lCode, lType = self.visit(ast.left, o)
        rCode, rType = self.visit(ast.right, o)

        if op in ['-', '+', '*', '/', '%']:        
            retType = FloatType() if FloatType in [type(x) for x in [lType, rType]] else IntType()
            if type(lType) is IntType and type(retType) == FloatType: lCode += self.emit.emitI2F(frame)
            if type(rType) is IntType and type(retType) == FloatType: rCode += self.emit.emitI2F(frame)
            if op in ['+', '-']:
                return lCode + rCode + self.emit.emitADDOP(op, retType, frame), retType
            if op in ['*', '/']:
                return lCode + rCode + self.emit.emitMULOP(op, retType, frame), retType
            if op == '%':
                return lCode + rCode + self.emit.emitMOD(frame), retType
        elif op in ['==', '!=', '<', '<=', '>', '>=']: 
            return lCode + rCode + self.emit.emitREOP(op, retType, frame), BoolType()
        elif op == '||': return lCode + rCode + self.emit.emitOROP(frame), retType
        elif op == '&&': return lCode + rCode + self.emit.emitANDOP(frame), retType
        #TODO: Compare 2 string? Concatenation 2 string
        elif op == '+.': 
            pass
        elif op == '==.':
            pass

    def visitUnaryOp(self, ast: UnaryOp, o: Access):
        frame = o.frame
        op = ast.op
        eleCode, eleType = self.visit(ast.body, o)
        if op == '!': return eleCode + self.emit.emitNOT(eleType, frame), eleType
        if op == '-': return eleCode + self.emit.emitNEGOP(eleType, frame), eleType


############################## Literal ##############################    

    def visitIntLiteral(self, ast: IntLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()

    def visitStringLiteral(self, ast: StringLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()