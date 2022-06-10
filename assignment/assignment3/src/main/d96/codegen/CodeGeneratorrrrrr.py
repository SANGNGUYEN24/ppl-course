'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from ast import Param
from email import message
from hashlib import new
from lib2to3.pygram import Symbols
from pydoc import resolve

from numpy import isin
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce

from initial.src.main.d96.checker.AST import Instance


# class Scope: pass
# class ScopedSymbol(Symbol, Scope): pass

# class Symbol:
#     def __init__(self, name:str, typ = None) -> None:
#         self.name = name 
#         self.typ = typ


# class AttributeSymbol(Symbol):
#     def __init__(self, name: str, type: Type, kind: SIKind, cv: Kind) -> None:
#         self.name = name
#         self.type = type        # IntType, FloatType
#         self.kind = kind        # Static or Instance
#         self.cv = cv            # Constant or variable

#     def __str__(self) -> str:
#         return "AttributeSymbol(" + str(self.name) + "," + str(self.type) + "," + str(self.kind) + "," + str(self.cv)+ ")"

# # Refer to thing in method
# class VariableSymbol(Symbol):
#     def __init__(self, name: str, type: Type, cv: Kind) -> None:
#         self.name = name
#         self.type = type        # IntType, FloatType ...
#         self.cv = cv          # Constant or variable or parameter

#     def __str__(self) -> str:
#         return "VariableSymbol(" + str(self.name) + "," + str(self.type) + "," + str(self.cv) + ")"

# class MethodSymbol(ScopedSymbol):
#     def __init__(self, name: str, kind: SIKind, blockScope: Scope=None) -> None:
#         self.name = name
#         self.kind = kind
#         self.symbols = []               # Store only the parameters
#         self.blockScope = blockScope    # Use storing statement scope //// LATE INIT
#         self.type = None

#     def addSymbol(self, symbol: Symbol):
#         self.symbols.append(symbol)

#     def __str__(self) -> str:
#         return "MethodSymbol(" + str(self.name) + "," + str(self.kind) + "," + str(len(self.symbols)) + ")"

# class ClassSymbol(ScopedSymbol, Type):
#     def __init__(self, name: str, type: Type, superClass: ClassSymbol=None, classScope: Scope = None) -> None:
#         self.name = name
#         self.type = type
#         self.symbols = []
#         self.superClass = superClass
#         self.classScope = classScope

#     def allSymbols(self):
#         super = self.superClass
#         sym = self.symbols
#         while super is not None:
#             names = [i.name for i in sym]
#             for i in super.symbols:
#                 # Dont need the previous declaration
#                 if i.name not in names:
#                     sym.append(i)
#             super = super.superClass
#         return sym

#     def __str__(self) -> str:
#         return "ClassSymbol(" + str(self.name) + "," + str(self.type) + "," + str(len(self.symbols)) + "," + (self.superClass.name if self.superClass else "") + ")"

# class GlobalScope(Scope):
#     def __init__(self) -> None:
#         self.symbols = []
#         self.symbols.append(Symbol("Int"))
#         self.symbols.append(Symbol("Float"))
#         self.symbols.append(Symbol("Boolean"))
#         self.symbols.append(Symbol("String"))
#         self.symbols.append(Symbol("Void"))

#     def __str__(self) -> str:
#         return "GlobalScope(Global," + ','.join(str(i.name) for i in self.symbols) + ")"

# class BlockScope(Scope):
#     def __init__(self) -> None:
#         self.symbols = []               # Store variable declaration in this scope Ex: For scope
#         self.blockScope = []            # Reference if block scope have if statement or for statement
#         self.upperScope = None          # Referenec to upperScope

#     def addBlock(self, block: Scope):
#         self.blockScope.append(block)

#     def getToMethod(self):
#         upper = self
#         while upper.upperScope is not None:
#             upper = upper.upperScope
#         return upper

#     def lookUpperPlease(self) -> List[Symbol]:
#         sym = self.symbols
#         upper = self.upperScope
#         while upper is not None:
#             names = [i.name for i in sym]
#             for i in upper.symbols:
#                 # Dont need the previous declaration cause messing with type
#                 if i.name not in names:
#                     sym.append(i)
#             upper = upper.upperScope
#         return sym

#     def trigger(self) -> None:
#         if self.blockScope != []:
#             for i in self.blockScope:
#                 i.upperScope = self

#     def lookClass(self):
#         upper = self.upperScope
#         while upper.upperScope is not None:
#             upper = upper.upperScope
#         return upper.insideClass


#     def __str__(self) -> str:
#         return "BlockScope(Block," + ','.join(str(i.name) for i in self.symbols) + (",Upper" if self.upperScope else "") + ")"


class Scope:
    def __init__(self, parent, name, class_parent=None):
        self.parent = parent
        self.symbols = []
        self.name = name
        self.class_parent = class_parent

    def __str__(self):
        return ""


class Symbol:
    def __init__(self, name: str, typ: Type, value, scope: Scope = None):
        self.name = name
        self.typ = typ
        self.value = value
        self.scope = scope


def Flatten(scope: Scope):
    syms = []
    cur = scope
    while (cur.parent):
        syms.append([cur.symbols.copy(), cur])
        cur = cur.parent


class CodeGenerator(Utils):
    def __init__(self):
        self.globalScope = Scope(None, "Global", None)
        self.globalScope.symbols.append(Symbol("Int", IntType()))
        self.globalScope.symbols.append(Symbol("Float", FloatType()))
        self.globalScope.symbols.append(Symbol("Boolean", BoolType()))
        self.globalScope.symbols.append(Symbol("String", StringType()))
        self.globalScope.symbols.append(Symbol("Void", VoidType()))

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

    def accept(self, v, param):
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


def resolveSym(scope: Scope, name: str):
    cur = scope
    while (cur.parent):
        for sym in cur.symbols:
            if (sym.name == name):
                return sym
        cur = cur.parent
    return None


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        # astTree: AST
        # env: List[Symbol]
        # dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast: Program, c):
        # ast: Program
        # c: Any
        curScope = self.env
        for i in ast.decl:
            i.accept(self, curScope)
        self.emit.emitEPILOG()
        # generate default constructor
        # self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list(), list())), c, Frame("<init>", VoidType))
        return c

    def visitClassDecl(self, ast: ClassDecl, c: GlobalScope):
        cName = ast.classname.name;
        Parent_class = ast.parentname;
        if cName == "Program":
            self.emit.printout(self.emit.emitPROLOG(cName, ""))
        else:
            parent = ""
            parent_sym = None;
            if Parent_class is not None:
                parent, _ = ast.parentname.name
                parent_sym = resolveId(c, parent)  ## Need to implement
            self.emit.printout(self.emit.emitPROLOG(cName, parent))
        curScope = Scope(c, cName, parent_sym)
        c.symbols.append(Symbol(cName, None, None, curScope))

        for mem in ast.memlist:
            mem.accept(self, curScope)
        return c

    def visitAttributeDecl(self, ast: AttributeDecl, c: Scope):
        attr_name, attr_typ, isFinal, rhs = ast.decl.accept(self, c)
        if type(ast.kind) is Instance:
            c.symbols.append(Symbol(attr_name, attr_typ, CName(c.name)))
            self.emit.printout(self.emit.emitATTRIBUTE(attr_name, attr_typ, isFinal, False))
            if (rhs[0]):
                self.emit.printout(rhs[0])
                self.emit.printout(self.emit.emitPUTFIELD(attr_name, attr_typ, None))

        else:
            c.symbols.append(Symbol(attr_name, attr_typ, CName(c.name)))
            self.emit.printout(self.emit.emitATTRIBUTE(attr_name, attr_typ, isFinal, True))
            if (rhs[0]):
                self.emit.printout(rhs[0])
                self.emit.printout(self.emit.emitPUTSTATIC(attr_name, attr_typ, None))
        return c

    def visitMethodDecl(self, ast: MethodDecl, c: Scope):
        Method_name = ast.name.name
        paraTyp = []
        for par in ast.param:
            paraTyp.append(par.varType.accept(self, self.env))
        retyp = resolveId(c, "Void")
        for stmt in ast.body.inst:
            if (isinstance(stmt, Return)):
                _, retyp = stmt.expr.accept(self, Access(None, c, False, False))  ## Note
                break
        method_typ = MType(paraTyp, retyp)
        CurrScope = Scope(c, Method_name)
        Method_sym = Symbol(Method_name, method_typ, CName(c.name), CurrScope)
        c.symbols.append(Method_sym)
        # Pre_syms = Flatten(c) ## Need to ilement
        message = SubBody(Frame(Method_name, retyp), CurrScope)
        IsStatic = True
        if (isinstance(ast.kind, Instance)):
            IsStatic = False
            message.frame.getNewIndex()

        self.emit.printout(self.emit.emitMETHOD(Method_name, method_typ, IsStatic))
        message.frame.enterScope(True)
        for param in ast.param:
            param_name, param_typ, isFinal, _ = param.accept(self, message)
            CurrScope.symbols.append(Symbol(param_name, param_typ, Index(message.frame.getCurrIndex())))
            self.emit.printout(
                self.emit.emitVAR(message.frame.getCurrIndex(), param_name, param_typ, message.frame.getStartLabel(),
                                  message.frame.getEndLabel(), isFinal, message.frame))
            message.frame.getNewIndex()
        self.emit.printout(self.emit.emitLABEL(message.frame.getStartLabel(), message.frame))
        for stmt in ast.body.inst:
            stmt.accept(self, message)
        self.emit.printout(self.emit.emitLABEL(message.frame.getEndLabel(), message.frame))
        self.emit.printout(self.emit.emitENDMETHOD(message.frame))
        message.frame.exitScope()
        return c

    def visitVarDecl(self, ast: VarDecl, c):  ## c can be Scope or Access
        if (isinstance(c, Scope)):  ## Declare the attribute => c is Scope
            var_name = ast.variable.name
            varTyp = ast.varType.accept(self, Access(None, c, False, False))
            if (ast.varInit):
                varInit = ast.varInit.accept(self, Access(None, c, False, False))  ## VarInit: [code, typ]
            else:
                varInit = [None, None]  ## VarInit: [code, typ]

            return var_name, varTyp, False, varInit
        else:  ## Declare the variable => c is Subody => in a method
            frame = c.frame
            access = Access(frame, c.sym)
            var_name = ast.variable.name
            varTyp = ast.varType.accept(self, None)
            access.sym.symbols.append(Symbol(var_name, varTyp, frame.getCurrIndex()))
            self.emit.printout(
                self.emit.emitVAR(frame.getCurrIndex(), var_name, varTyp, frame.getStartLabel(), frame.getEndLabel(),
                                  False, frame))
            if (ast.varInit):
                varInit = ast.varInit(self, access)
                self.emit.printout(varInit[0])
                self.emit.printout(self.emit.emitWRITEVAR(var_name, varTyp, frame.getCurrIndex(), frame))
            frame.getNewIndex()

    def visitConstDecl(self, ast: ConstDecl, c):
        if (isinstance(c, Scope)):  ## Declare the attribute => c is Scope
            var_name = ast.constant.name
            varTyp = ast.constType.accept(self, Access(None, c, False, False))
            if (ast.value):
                varInit = ast.value.accept(self, c)  ## VarInit: [code, typ]
            else:
                varInit = [None, None]  ## VarInit: [code, typ]

            return var_name, varTyp, False, varInit
        else:  ## Declare the variable => c is Subody => in a method
            frame = c.frame
            access = Access(frame, c.sym)
            var_name = ast.constant.name
            varTyp = ast.constType.accept(self, None)
            access.sym.symbols.append(Symbol(var_name, varTyp, frame.getCurrIndex()))
            self.emit.printout(
                self.emit.emitVAR(frame.getCurrIndex(), var_name, varTyp, frame.getStartLabel(), frame.getEndLabel(),
                                  False, frame))
            if (ast.varInit):
                varInit = ast.value(self, access)
                self.emit.printout(varInit[0])
                self.emit.printout(self.emit.emitWRITEVAR(var_name, varTyp, frame.getCurrIndex(), frame))
            frame.getNewIndex()
            return None

    def visitBlock(self, ast: Block, c: SubBody):  ## c is a Subody
        frame = c.frame
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        CurrScope = Scope(c.sym, "BlockScope")
        message = SubBody(frame, CurrScope)
        for stmt in ast.inst:
            stmt.accept(self, message)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        return None

    def visitBinaryOp(self, ast: BinaryOp, c):
        pass

    def visitUnaryOp(self, ast: UnaryOp, c: Access):
        exprCode, exprType = self.visit(ast.body, c)
        if ast.op == '-':
            return exprCode + self.emit.emitNEGOP(exprType, c.frame), exprType
        else:
            return exprCode + self.emit.emitNOT(exprType, c.frame), exprType

    def visitCallExpr(self, ast: CallExpr, c):
        obj_code, obj_typ = ast.obj.accept(self, Access(c.frame, c.sym, False, True))
        self.emit.printout(obj_code)
        obj_sym = resolveSym(c.sym, obj_typ.name)
        method_sym = resolveSym(obj_sym.scope, ast.method.name)
        ParamTypes = method_sym.typ.partype
        Param_code = ""

        for idx, param in enumerate(ast.param):
            pCode, pType = param.accept(self, Access(c.frame, c.sym, False, True))
            if (type(ParamTypes[idx]) is FloatType and type(pType) is IntType):
                pCode = pCode + self.emit.emitI2F(c.frame)
            Param_code += pCode

        if (method_sym.name[0] == "$"):
            invoke_code = self.emit.emitINVOKESTATIC(obj_typ.name + "/" + method_sym.name, method_sym.typ, c.frame)
        else:
            invoke_code = self.emit.emitINVOKEVIRTUAL(obj_typ.name + "/" + method_sym.name, method_sym.typ, c.frame)
        return obj_code + Param_code + invoke_code, method_sym.typ.rettype

    def visitCallStmt(self, ast: CallStmt, c: SubBody):
        obj_code, obj_typ = ast.obj.accept(self, Access(c.frame, c.sym, False, True))
        self.emit.printout(obj_code)
        obj_sym = resolveSym(c.sym, obj_typ.name)
        method_sym = resolveSym(obj_sym.scope, ast.method.name)
        ParamTypes = method_sym.typ.partype
        Param_code = ""

        for idx, param in enumerate(ast.param):
            pCode, pType = param.accept(self, Access(c.frame, c.sym, False, True))
            if (type(ParamTypes[idx]) is FloatType and type(pType) is IntType):
                pCode = pCode + self.emit.emitI2F(c.frame)
            Param_code += pCode

        if (method_sym.name[0] == "$"):
            invoke_code = self.emit.emitINVOKESTATIC(obj_typ.name + "/" + method_sym.name, method_sym.typ, c.frame)
        else:
            invoke_code = self.emit.emitINVOKEVIRTUAL(obj_typ.name + "/" + method_sym.name, method_sym.typ, c.frame)
        self.emit.printout(obj_code + Param_code + invoke_code)
        return None

    def visitNewExpr(self, ast: NewExpr, c: Access):
        newcode = self.emit.emitNEW(ast.classname.name, c.frame)
        class_sym = resolveSym(self.env, ast.classname.name)
        method_init_sym = resolveSym(class_sym.scope, "<init>")
        ParamTypes = method_init_sym.typ.partype
        retyp = method_init_sym.typ.rettype
        Param_code = ""

        for idx, param in enumerate(ast.param):
            pCode, pType = param.accept(self, c)
            if (type(ParamTypes[idx]) is FloatType and type(pType) is IntType):
                pCode = pCode + self.emit.emitI2F(c.frame)
            Param_code += pCode
        return newcode + Param_code + self.emit.emitINVOKESPECIAL(c.frame, ast.classname.name + '/' + "<init>",
                                                                  method_init_sym.typ)

    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        pass

    def visitNullLiteral(self, ast: NullLiteral, c):
        pass

    def visitSelfLiteral(self, ast: SelfLiteral, c):
        pass

    def visitId(self, ast: Id, o: Access):

        # Return (name, type, index)
        frame, symbols = o.frame, o.sym
        isLeft = o.isLeft
        isFirst = o.isFirst

        # if isLeft and o.checkArrayType: return False, None

        sym = self.lookup(ast.name.lower(), symbols, lambda x: x.name.lower())

        # recover status of stack in frame. # FIXME: FOR WHAT?
        if not isFirst and isLeft:
            frame.push()  # because a = 2; emitWRITEVAR will pop() -> need to push first
        elif not isFirst and not isLeft:
            frame.pop()  # a.call(), x = a, load value of a onto stack (push) =>  nees to pop? Why isFirst = False?
        isArrayType = type(sym.mtype) is ArrayType
        emitType = StupidUtils.retrieveType(sym.mtype)
        if sym.value is None:  # not index -> global var - static field # NOTE: WHY is None but bot String?
            if isLeft and not isArrayType:
                retCode = self.emit.emitPUTSTATIC(self.className + "/" + sym.name, emitType, frame)
            else:
                retCode = self.emit.emitGETSTATIC(self.className + "/" + sym.name, emitType, frame)
        else:
            if isLeft and not isArrayType:
                retCode = self.emit.emitWRITEVAR(sym.name, emitType, sym.value.value, frame)
            else:
                retCode = self.emit.emitREADVAR(sym.name, emitType, sym.value.value, frame)

        return retCode, sym.mtype

    def visitArrayCell(self, ast: ArrayCell, c):
        pass

    def visitFieldAccess(self, ast: FieldAccess, c):
        pass

    def visitIf(self, ast: If, o: SubBody):
        frame, nenv = o.frame, o.sym

        ifCode, _ = self.visit(ast.expr, Access(frame, nenv, False, True))
        self.emit.printout(ifCode)

        labelThen, labelEnd = frame.getNewLabel(), frame.getNewLabel()
        self.emit.printout(self.emit.emitIFTRUE(labelThen, frame))
        # False -> Do Else stmt
        ast.elseStmt.accept(self, o)
        self.emit.printout(self.emit.emitGOTO(labelEnd, frame))  # go to end
        # Then stmt
        self.emit.printout(self.emit.emitLABEL(labelThen, frame))
        ast.thenStmt.accept(self, o)
        self.emit.printout(self.emit.emitLABEL(labelEnd, frame))
        return None

    def visitFor(self, ast: For, o: SubBody):  # TODO: Protected var in forloop stmt
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
        # TODO: WHat is isFirst? I guess isFirst = True-> initialzation
        lhsWriteCode, _ = self.visit(ast.id, Access(frame, nenv, True, True))  # Write code
        lhsReadCode, _ = self.visit(ast.id, Access(frame, nenv, False, False))  # Read code

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
        if ast.expr3:
            self.emit.printout(e3Code)
        else:
            self.emit.printout(self.emit.emitPUSHICONST(1, frame))
        self.emit.printout(self.emit.emitADDOP('+', IntType(), frame))
        self.emit.printout(lhsWriteCode)  # NOTE: Why? pop() -> pop (lhs + e3) above from stack and store it in

        # goto LabelCont
        if not hasReturnStmt: self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))  # loop

        # LabelBreak:
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitBreak(self, ast: Break, o: SubBody):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))

    def visitContinue(self, ast: Continue, o: SubBody):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    # TODO: change checkArrayType in Access to isArrayType, MOITOIDAY
    def visitAssign(self, ast: Assign, o: SubBody):
        frame, nenv = o.frame, o.sym
        # stack: ..., arrayref, index, value -> ...
        isArray, _ = self.visit(ast.lhs, Access(frame, nenv, True, True, isArrayType=True))
        # simulate to push 2 slot for arrayref and index, visit exp first
        if isArray: [frame.push() for _ in range(0, 2)]

        # Visit lhs: Id or ArrayCell or static attribute or instance attribute
        exprCode, expType = self.visit(ast.exp, Access(frame, nenv, False, True))
        lhsCode, lhsType = self.visit(ast.lhs, Access(frame, nenv, True, True))

        if type(lhsType) is FloatType and type(expType) is IntType:  # Coerce int -> float
            exprCode = exprCode + self.emit.emitI2F(frame)

        if not isArray:
            self.emit.printout(exprCode + lhsCode)
        else:
            self.emit.printout(lhsCode[0] + exprCode + lhsCode[1])
            # recover stack status
            [frame.pop() for _ in range(0, 2)]

    def visitReturn(self, ast: Return, o: SubBody):
        frame, nenv = o.frame, o.sym
        if ast.expr:
            exprCode, exprType = self.visit(ast.expr, Access(frame, nenv, False, True))
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
