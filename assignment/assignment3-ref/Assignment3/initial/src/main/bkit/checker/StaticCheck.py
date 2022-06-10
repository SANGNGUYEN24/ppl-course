
"""
 * @author nhphung
"""
# Trieu Minh Sang - 1852717
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

    def __init__(self, d, e):
        self.dimen = d
        self.eletype = e

@dataclass
class MType(Type):
    intype:List[Type]
    restype:Type

    def __init__(self, i, o):
        self.intype = i
        self.restype = o

@dataclass
class Symbol:
    name: str
    mtype:Type
    ktype:Kind

    def __init__(self, n, m, k):
        self.name = n
        self.mtype = m
        self.ktype = k

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType()),Function()),
Symbol("float_to_int",MType([IntType()],FloatType()),Function()),
Symbol("float_of_int",MType([IntType()],FloatType()),Function()),
Symbol("int_of_string",MType([StringType()],IntType()),Function()),
Symbol("string_of_int",MType([IntType()],StringType()),Function()),
Symbol("float_of_string",MType([StringType()],FloatType()),Function()),
Symbol("string_of_float",MType([FloatType()],StringType()),Function()),
Symbol("bool_of_string",MType([StringType()],BoolType()),Function()),
Symbol("string_of_bool",MType([BoolType()],StringType()),Function()),
Symbol("read",MType([],StringType()),Function()),
Symbol("printLn",MType([],VoidType()),Function()),
Symbol("print",MType([StringType()],VoidType()),Function()),
Symbol("printStrLn",MType([StringType()],VoidType()),Function())]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        l = [self.global_envi]
        l = reduce(lambda a,b: b.accept(self, [0,a]), ast.decl, l)
        for i in l[0]:
            if i.name == "main" and isinstance(i.mtype,MType):
                l = reduce(lambda a,b: b.accept(self, [1,a]), ast.decl, l)
                return None
        raise NoEntryPoint()

    def visitVarDecl(self, ast, c):
        if c[0] == 1:
            return c[1] # Pass for second check

        name = ast.variable.name
        if c[0] == 0: # For Variable
            for i in c[1][0]:
                if i.name == name:
                    raise Redeclared(Variable(),name)

            mt = Unknown()
            if ast.varInit != None:
                mt = ast.varInit.accept(self,[0,c])[1] 
            else:
                if len(ast.varDimen) > 0:
                    mt = ArrayType(ast.varDimen,Unknown())
            c[1][0].append(Symbol(name,mt,Variable()))
            return c[1]

        if c[0] == 2: # For Parameter
            
            pos = len(c[1][0])
            mt = Unknown()
            for i in c[1][0]:
                if i.name == name:
                    raise Redeclared(Parameter(),name)
            for i in c[1][len(c[1]) - 1]:
                if c[2] == i.name and isinstance(i.mtype,MType):
                    mt = i.mtype.intype[pos]
            c[1][0].append(Symbol(name,mt,Parameter()))
            return c[1]
            
        elif c[0] == 3: # For Parameter type
            mt = Unknown()
            if len(ast.varDimen) > 0:
                mt = ArrayType(ast.varDimen,Unknown())
            c[1].append(mt)
            return c[1]  
    
    def visitFuncDecl(self, ast, c):
        name = ast.name.name
        if c[0] == 0:
            for i in c[1][0]:
                if i.name == name:
                    raise Redeclared(Function(),name)
            params = reduce(lambda a,b: b.accept(self, [3,a]), ast.param, [])
            f = Symbol(name,MType(params,Unknown()),Function())
            c[1][0].append(f)
            return c[1]
        elif c[0] == 1:
            local_scope = reduce(lambda a,b: b.accept(self, [2,a,name]), ast.param, [[]] + c[1])
            local_scope = reduce(lambda a,b: b.accept(self, [0,a]), ast.body[0], local_scope)
            for i in ast.body[1]:
                local_scope = i.accept(self,[local_scope,name])
            return c[1]
 
    def visitBinaryOp(self, ast, c):
        l = ast.left.accept(self,[0,c[1],c[2]])
        lhs = l[1]
        o = l[0]
        if lhs == None:
            return [o,None]
        if isinstance(ast.left,Id):
            lhs = o[l[1][0]][l[1][1]].mtype
        elif isinstance(ast.left,CallExpr):
            lhs = o[l[1][0]][l[1][1]].mtype.restype
        else:
            lhs = l[1]
        
        r = ast.right.accept(self,[0,l[0],c[2]])
        o = r[0]
        rhs = r[1]
        if rhs == None:
            return [o,None]
        if isinstance(ast.right,Id):
            rhs = o[r[1][0]][r[1][1]].mtype
        elif isinstance(ast.right,CallExpr):
            rhs = o[r[1][0]][r[1][1]].mtype.restype
        else:
            rhs = r[1]

        if ast.op in ['&&','||']:
            if isinstance(lhs,Unknown):
                lhs = BoolType()
                if isinstance(ast.left,Id):
                    o[l[1][0]][l[1][1]].mtype = lhs
                    if isinstance(o[l[1][0]][l[1][1]].ktype,Parameter):
                        for i in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][i].name == c[2]:
                                o[len(o) - 1][i].mtype.intype[l[1][1]] = lhs
                elif isinstance(ast.left,CallExpr):
                    o[l[1][0]][l[1][1]].mtype.restype = lhs
            if isinstance(rhs,Unknown):
                rhs = BoolType()
                if isinstance(ast.right,Id):
                    o[r[1][0]][r[1][1]].mtype = rhs
                    if isinstance(o[r[1][0]][r[1][1]].ktype,Parameter):
                        for i in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][i].name == c[2]:
                                o[len(o) - 1][i].mtype.intype[r[1][1]] = rhs
                elif isinstance(ast.right,CallExpr):
                    o[r[1][0]][r[1][1]].mtype.restype = rhs
            if not(isinstance(lhs,BoolType)) or not(isinstance(rhs,BoolType)):
                raise TypeMismatchInExpression(ast)
            return [o,BoolType()]

        elif ast.op in ['+','-','*','\\','%','==','!=','<','>','>=','<=']:
            if isinstance(lhs,Unknown):
                lhs = IntType()
                if isinstance(ast.left,Id):
                    o[l[1][0]][l[1][1]].mtype = lhs
                    if isinstance(o[l[1][0]][l[1][1]].ktype,Parameter):
                        for i in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][i].name == c[2]:
                                o[len(o) - 1][i].mtype.intype[l[1][1]] = lhs
                elif isinstance(ast.left,CallExpr):
                    o[l[1][0]][l[1][1]].mtype.restype = lhs
            if isinstance(rhs,Unknown):
                rhs = IntType()
                if isinstance(ast.right,Id):
                    o[r[1][0]][r[1][1]].mtype = rhs
                    if isinstance(o[r[1][0]][r[1][1]].ktype,Parameter):
                        for i in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][i].name == c[2]:
                                o[len(o) - 1][i].mtype.intype[r[1][1]] = rhs
                elif isinstance(ast.right,CallExpr):
                    o[r[1][0]][r[1][1]].mtype.restype = IntType()
            if not(isinstance(lhs,IntType)) or not(isinstance(rhs,IntType)):
                raise TypeMismatchInExpression(ast)
            if ast.op in ['+','-','*','\\','%']:
                return [o,IntType()]
            else:
                return [o,BoolType()]

        elif ast.op in ['+.','-.','*.','\\.','=/=','<.','>.','>=.','<=.']:
            if isinstance(lhs,Unknown):
                lhs = FloatType()
                if isinstance(ast.left,Id):
                    o[l[1][0]][l[1][1]].mtype = lhs
                    if isinstance(ast.left,Id):
                        o[l[1][0]][l[1][1]].mtype = IntType()
                    if isinstance(o[l[1][0]][l[1][1]].ktype,Parameter):
                        for i in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][i].name == c[2]:
                                o[len(o) - 1][i].mtype.intype[l[1][1]] = lhs
                elif isinstance(ast.left,CallExpr):
                    o[l[1][0]][l[1][1]].mtype.restype = lhs
            if isinstance(rhs,Unknown):
                rhs = FloatType()
                if isinstance(ast.right,Id):
                    o[r[1][0]][r[1][1]].mtype = rhs
                    if isinstance(o[r[1][0]][r[1][1]].ktype,Parameter):
                        for i in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][i].name == c[2]:
                                o[len(o) - 1][i].mtype.intype[r[1][1]] = rhs
                elif isinstance(ast.right,CallExpr):
                    o[r[1][0]][r[1][1]].mtype.restype = rhs
            if not(isinstance(lhs,FloatType)) or not(isinstance(rhs,FloatType)):
                raise TypeMismatchInExpression(ast)
            if ast.op in ['+.','-.','*.','\\.']:
                return [o,FloatType()]
            else:
                return [o,BoolType()]
    
    def visitUnaryOp(self, ast, c):
        ot = ast.body.accept(self,[0,c[1],c[2]])
        o = ot[0]

        t = ot[1]
        if t == None:
            return [o,None]
        if isinstance(ast.body,Id):
            t = o[ot[1][0]][ot[1][1]].mtype
        elif isinstance(ast.body,CallExpr):
            t = o[ot[1][0]][ot[1][1]].mtype.restype
        else:
            t = ot[1]
            
        if ast.op in ['!']:
            if isinstance(t,Unknown):
                t = BoolType()
                if isinstance(ast.body,Id):
                    o[ot[1][0]][ot[1][1]].mtype = t
                    if isinstance(o[ot[1][0]][ot[1][1]].ktype,Parameter):
                        for i in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][i].name == c[2]:
                                o[len(o) - 1][i].mtype.intype[ot[1][1]] = t
                elif isinstance(ast.body,CallExpr):
                    o[ot[1][0]][ot[1][1]].mtype.restype = t
            if not(isinstance(t,BoolType)):
                raise TypeMismatchInExpression(ast)
            return [o,BoolType()]

        elif ast.op in ['-']:
            if isinstance(t,Unknown):
                t = IntType()
                if isinstance(ast.body,Id):
                    o[ot[1][0]][ot[1][1]].mtype = t
                    if isinstance(o[ot[1][0]][ot[1][1]].ktype,Parameter):
                        for i in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][i].name == c[2]:
                                o[len(o) - 1][i].mtype.intype[ot[1][1]] = t
                elif isinstance(ast.body,CallExpr):
                    o[ot[1][0]][ot[1][1]].mtype.restype = t
            if not(isinstance(t,IntType)):
                raise TypeMismatchInExpression(ast)
            return [o,IntType()]

        elif ast.op in ['-.']:
            if isinstance(t,Unknown):
                t = FloatType()
                if isinstance(ast.body,Id):
                    o[ot[1][0]][ot[1][1]].mtype = t
                    if isinstance(o[ot[1][0]][ot[1][1]].ktype,Parameter):
                        for i in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][i].name == c[2]:
                                o[len(o) - 1][i].mtype.intype[ot[1][1]] = t
                elif isinstance(ast.body,CallExpr):
                    o[ot[1][0]][ot[1][1]].mtype.restype = t
            if not(isinstance(t,FloatType)):
                raise TypeMismatchInExpression(ast)
            return [o,FloatType()]
    
    def visitCallExpr(self, ast, c):
        ot = ast.method.accept(self,[1,c[1]])
        o = ot[0]
        e = Unknown()
        
        if ot[1] != None:
            e = o[ot[1][0]][ot[1][1]]
            if len(e.mtype.intype) != len(ast.param):
                raise TypeMismatchInExpression(ast)
            
            for i in range(len(e.mtype.intype)):
                p = ast.param[i].accept(self,[0,o,c[2]])
                o = p[0]
                t = p[1]
                if (t == None):
                    return [o,None]
                if isinstance(ast.param[i],Id):
                    t = o[p[1][0]][p[1][1]].mtype
                elif isinstance(ast.param[i],CallExpr):
                    t = o[p[1][0]][p[1][1]].mtype.restype

                if isinstance(e.mtype.intype[i],Unknown) and isinstance(t,Unknown):
                    return [o,None]
                elif isinstance(e.mtype.intype[i],Unknown):
                    o[ot[1][0]][ot[1][1]].mtype.intype[i] = t
                    e = o[ot[1][0]][ot[1][1]]
                    if o[ot[1][0]][ot[1][1]].name == c[2]:
                        o[len(o) - 2][i].mtype = t
                elif isinstance(t,Unknown):
                    if isinstance(ast.param[i],Id):
                        o[p[1][0]][p[1][1]].mtype = e.mtype.intype[i]
                    elif isinstance(ast.param[i],CallExpr):
                        o[p[1][0]][p[1][1]].mtype.restype = e.mtype.intype[i]
                    t = e.mtype.intype[i]
                    if isinstance(o[p[1][0]][p[1][1]].ktype,Parameter):
                        for j in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][j].name == c[2]:
                                o[len(o) - 1][j].mtype.intype[p[1][1]] = e.mtype.intype[i]
                if type(e.mtype.intype[i]) != type(t):
                    raise TypeMismatchInExpression(ast)
            return [o,(ot[1][0],ot[1][1])]
        else:
            raise Undeclared(Function(),ast.method.name)
            
    def visitId(self, ast, c):
        if c[0] == 0: # Find Variable
            for i in range(len(c[1])):
                for j in range(len(c[1][i])):
                    if c[1][i][j].name == ast.name:
                        if not(isinstance(c[1][i][j].mtype,MType)):
                            return [c[1],(i,j)]
                        else:
                            raise Undeclared(Identifier(),ast.name)
            raise Undeclared(Identifier(),ast.name)
        if c[0] == 1: # Find Function
            for i in range(len(c[1])):
                for j in range(len(c[1][i])):
                    if c[1][i][j].name == ast.name:
                        if isinstance(c[1][i][j].mtype,MType):
                            return [c[1],(i,j)]
                        else:
                            raise Undeclared(Function(),ast.name)
            raise Undeclared(Function(),ast.name)
    
    def visitArrayCell(self, ast, c):
        if c[0] == 0:
            arr = ast.arr.accept(self,[0,c[1]])
            o = arr[0]
            t_arr = arr[1]
            if t_arr == None:
                return [o,None]
            if isinstance(ast.arr,Id):
                t_arr = o[arr[1][0]][arr[1][1]].mtype
            elif isinstance(ast.arr,CallExpr):
                t_arr = o[arr[1][0]][arr[1][1]].mtype.restype
            if not(isinstance(t_arr,ArrayType)):
                raise TypeMismatchInExpression(ast)

            if len(t_arr.dimen) != len(ast.idx):
                raise TypeMismatchInExpression(ast)
            for i in ast.idx:
                expr = i.accept(self,[0,o,c[2]])
                o = expr[0]
                t = expr[1]
                if t == None:
                    return [o,None]
                if isinstance(i,Id):
                    t = o[expr[1][0]][expr[1][1]].mtype
                elif isinstance(i,CallExpr):
                    t = o[expr[1][0]][expr[1][1]].mtype.restype
                if isinstance(t,Unknown):
                    return [o,None]
                if not(isinstance(t,IntType)):
                    raise TypeMismatchInExpression(ast)
            if isinstance(ast.arr,Id):
                return [o,(arr[1][0],arr[1][1])]
            elif isinstance(ast.arr,CallExpr):
                return [o,(arr[1][0],arr[1][1])]
    
    def visitAssign(self, ast, c):
        l = ast.lhs.accept(self,[0,c[0],c[1]])
        o = l[0]
        lhs = Unknown()
        if l[1] == None:
            raise TypeCannotBeInferred(ast)
        if isinstance(ast.lhs,Id):
            lhs = o[l[1][0]][l[1][1]].mtype
        elif isinstance(ast.lhs,ArrayCell):
            if isinstance(ast.lhs.arr,Id):
                lhs = o[l[1][0]][l[1][1]].mtype.eletype
            elif isinstance(ast.lhs.arr,CallExpr):
                lhs = o[l[1][0]][l[1][1]].mtype.restype.eletype


        r = ast.rhs.accept(self,[0,o,c[1]])
        o = r[0]
        rhs = r[1]
        if rhs == None:
            raise TypeCannotBeInferred(ast)
        if isinstance(ast.rhs,Id):
            rhs = o[r[1][0]][r[1][1]].mtype
        elif isinstance(ast.rhs,CallExpr):
            rhs = o[r[1][0]][r[1][1]].mtype.restype
        else:
            rhs = r[1]

        if isinstance(lhs,Unknown) and isinstance(rhs,Unknown):
            raise TypeCannotBeInferred(ast)
        elif isinstance(lhs,Unknown):
            o[l[1][0]][l[1][1]].mtype = rhs
            if isinstance(o[l[1][0]][l[1][1]].ktype,Parameter):
                for i in range(len(o[len(o) - 1])):
                    if o[len(o) - 1][i].name == c[1]:
                        o[len(o) - 1][i].mtype.intype[l[1][1]] = rhs
            if isinstance(rhs,ArrayType):
                raise TypeMismatchInStatement(ast)
            lhs = rhs
        elif isinstance(rhs,Unknown):
            if isinstance(ast.rhs,CallExpr):
                o[r[1][0]][r[1][1]].mtype.restype = lhs
            else:
                o[r[1][0]][r[1][1]].mtype = lhs
                if isinstance(o[r[1][0]][r[1][1]].ktype,Parameter):
                    for i in range(len(o[len(o) - 1])):
                        if o[len(o) - 1][i].name == c[1]:
                            o[len(o) - 1][i].mtype.intype[r[1][1]] = lhs
            if isinstance(lhs,ArrayType):
                raise TypeMismatchInStatement(ast)
            rhs = lhs
        if isinstance(lhs,ArrayType) and isinstance(rhs,ArrayType):
            if len(o[l[1][0]][l[1][1]].mtype.dimen) != len(o[r[1][0]][r[1][1]].mtype.dimen):
                raise TypeMismatchInStatement(ast)
            if isinstance(o[l[1][0]][l[1][1]].mtype.eletype,Unknown) and isinstance(o[r[1][0]][r[1][1]].mtype.eletype,Unknown):
                raise TypeCannotBeInferred(ast)
            elif isinstance(o[l[1][0]][l[1][1]].mtype.eletype,Unknown):
                o[l[1][0]][l[1][1]] = rhs
                if isinstance(o[l[1][0]][l[1][1]].ktype,Parameter):
                    for i in range(len(o[len(o) - 1])):
                        if o[len(o) - 1][i].name == c[1]:
                            o[len(o) - 1][i].mtype.intype[l[1][1]] = rhs
                
            elif isinstance(o[r[1][0]][r[1][1]].mtype.eletype,Unknown):
                o[r[1][0]][r[1][1]] = lhs
            if type(o[l[1][0]][l[1][1]].mtype.eletype) != type(o[r[1][0]][r[1][1]].mtype.eletype):
                raise TypeMismatchInStatement(ast)

        if type(lhs) != type(rhs):
            raise TypeMismatchInStatement(ast)

        return o
    
    def visitIf(self, ast, c):
        for i in ast.ifthenStmt:
            expr = i[0].accept(self,[0,c[0],c[1]])
            o = expr[0]
            t = expr[1]
            if t == None:
                raise TypeCannotBeInferred(ast)
            if isinstance(i[0],Id):
                t = o[expr[1][0]][expr[1][1]].mtype
            elif isinstance(i[0],CallExpr):
                t = o[expr[1][0]][expr[1][1]].mtype.restype
            
            if isinstance(t,Unknown):
                t = BoolType()
                if isinstance(i[0],Id):
                    o[expr[1][0]][expr[1][1]].mtype = t
                    if isinstance(o[expr[1][0]][expr[1][1]].ktype,Parameter):
                        for j in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][j].name == c[1]:
                                o[len(o) - 1][j].mtype.intype[expr[1][1]] = t
                elif isinstance(i[0],CallExpr):
                    o[expr[1][0]][expr[1][1]].mtype.restype = t
            if not(isinstance(t,BoolType)):
                raise TypeMismatchInStatement(ast)

            new_scope = reduce(lambda a,b: b.accept(self, [0,a]), i[1], [[]])
            for j in i[2]:
                new_scope = j.accept(self,[new_scope + o,c[1]])
            
            
        new_scope = reduce(lambda a,b: b.accept(self, [0,a]),ast.elseStmt[0],[[]])
        for j in ast.elseStmt[1]:
            new_scope = j.accept(self,[new_scope + o,c[1]])
        
        return o
   
    def visitFor(self, ast, c):
        ot = ast.idx1.accept(self,[0,c[0]])
        o = ot[0]
        if isinstance(o[ot[1][0]][ot[1][1]].mtype,Unknown):
            t = IntType()
            o[ot[1][0]][ot[1][1]].mtype = t
            if isinstance(o[ot[1][0]][ot[1][1]].ktype,Parameter):
                for j in range(len(o[len(o) - 1])):
                    if o[len(o) - 1][j].name == c[1]:
                        o[len(o) - 1][j].mtype.intype[ot[1][1]] = t
        if not(isinstance(o[ot[1][0]][ot[1][1]].mtype,IntType)):
            raise TypeMismatchInStatement(ast)
        

        expr1 = ast.expr1.accept(self,[0,o,c[1]])
        o = expr1[0]
        e1 = expr1[1]
        if e1 == None:
            raise TypeCannotBeInferred(ast)
        if isinstance(ast.expr1,Id):
            e1 = o[expr1[1][0]][expr1[1][1]].mtype
        elif isinstance(ast.expr1,CallExpr):
            e1 = o[expr1[1][0]][expr1[1][1]].mtype.restype
        if isinstance(e1,Unknown):
            e1 = IntType()
            if isinstance(ast.expr1,Id):
                o[expr1[1][0]][expr1[1][1]].mtype = e1
                if isinstance(o[expr1[1][0]][expr1[1][1]].ktype,Parameter):
                    for j in range(len(o[len(o) - 1])):
                        if o[len(o) - 1][j].name == c[1]:
                            o[len(o) - 1][j].mtype.intype[expr1[1][1]] = e1
            elif isinstance(ast.expr1,CallExpr):
                o[expr1[1][0]][expr1[1][1]].mtype.restype = e1
        if not(isinstance(e1,IntType)):
            raise TypeMismatchInStatement(ast)


        expr2 = ast.expr2.accept(self,[0,o,c[1]])
        o = expr2[0]
        e2 = expr2[1]
        if e2 == None:
            raise TypeCannotBeInferred(ast)
        if isinstance(ast.expr2,Id):
            e2 = o[expr2[1][0]][expr2[1][1]].mtype
        elif isinstance(ast.expr2,CallExpr):
            e2 = o[expr2[1][0]][expr2[1][1]].mtype.restype
        if isinstance(e2,Unknown):
            e2 = BoolType()
            if isinstance(ast.expr2,Id):
                o[expr2[1][0]][expr2[1][1]].mtype = e2
                if isinstance(o[expr2[1][0]][expr2[1][1]].ktype,Parameter):
                    for j in range(len(o[len(o) - 1])):
                        if o[len(o) - 1][j].name == c[1]:
                            o[len(o) - 1][j].mtype.intype[expr2[1][1]] = e2
            elif isinstance(ast.expr2,CallExpr):
                o[expr2[1][0]][expr2[1][1]].mtype.restype = e2
        if not(isinstance(e2,BoolType)):
            raise TypeMismatchInStatement(ast)

        expr3 = ast.expr3.accept(self,[0,o,c[1]])
        o = expr3[0]
        e3 = expr3[1]
        if e3 == None:
            raise TypeCannotBeInferred(ast)
        if isinstance(ast.expr3,Id):
            e3 = o[expr3[1][0]][expr3[1][1]].mtype
        elif isinstance(ast.expr3,CallExpr):
            e3 = o[expr3[1][0]][expr3[1][1]].mtype.restype
        if isinstance(e3,Unknown):
            e3 = IntType()
            if isinstance(ast.expr3,Id):
                o[expr3[1][0]][expr3[1][1]].mtype = e3
                if isinstance(o[expr3[1][0]][expr3[1][1]].ktype,Parameter):
                    for j in range(len(o[len(o) - 1])):
                        if o[len(o) - 1][j].name == c[1]:
                            o[len(o) - 1][j].mtype.intype[expr3[1][1]] = e3
            elif isinstance(ast.expr3,CallExpr):
                o[expr3[1][0]][expr3[1][1]].mtype.restype = e3
        if not(isinstance(e3,IntType)):
            raise TypeMismatchInStatement(ast)

        new_scope = reduce(lambda a,b: b.accept(self, [0,a]),ast.loop[0],[[]])
        for j in ast.loop[1]:
            new_scope = j.accept(self,[new_scope + o,c[1]])
        
        return o
    
    def visitContinue(self, ast, c):
        pass
    
    def visitBreak(self, ast, c):
        pass
    
    def visitReturn(self, ast, c):
        res = VoidType()
        o = c[0]
        if ast.expr != None:
            expr = ast.expr.accept(self,[0,c[0],c[1]])
            o = expr[0]
            if isinstance(ast.expr,Id):
                res = o[expr[1][0]][expr[1][1]].mtype
                if isinstance(res,Unknown):
                    for i in range(len(o[len(o) - 1])):
                        if o[len(o) - 1][i].name == c[1]:
                            if isinstance(o[len(o) - 1][i].mtype.restype,Unknown):
                                raise TypeCannotBeInferred(ast)
                            else:
                                o[expr[1][0]][expr[1][1]].mtype = o[len(o) - 1][i].mtype.restype
                                res = o[len(o) - 1][i].mtype.restype
                elif isinstance(res,ArrayType):
                    ele = o[expr[1][0]][expr[1][1]].mtype.eletype
                    if isinstance(ele,Unknown):
                        for i in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][i].name == c[1]:
                                if isinstance(o[len(o) - 1][i].mtype.restype,Unknown):
                                    raise TypeCannotBeInferred(ast)
                                elif isinstance(o[len(o) - 1][i].mtype.restype,ArrayType):
                                    if isinstance(o[len(o) - 1][i].mtype.restype.eletype,Unknown):
                                        raise TypeCannotBeInferred(ast)
                                    else:
                                        o[expr[1][0]][expr[1][1]].mtype.eletype = o[len(o) - 1][i].mtype.restype.eletype
                                        ele = o[len(o) - 1][i].mtype.restype.eletype
                                else:
                                    raise TypeCannotBeInferred(ast)                
            elif isinstance(ast.expr,CallExpr):
                if expr[1] == None:
                    raise TypeCannotBeInferred(ast)
                res = o[expr[1][0]][expr[1][1]].mtype.restype
                if isinstance(res,Unknown):
                    if isinstance(res,Unknown):
                        for i in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][i].name == c[1]:
                                if isinstance(o[len(o) - 1][i].mtype.restype,Unknown):
                                    raise TypeCannotBeInferred(ast)
                                else:
                                    o[expr[1][0]][expr[1][1]].mtype.restype = o[len(o) - 1][i].mtype.restype
                                    res = o[len(o) - 1][i].mtype.restype
            elif isinstance(ast.expr,Expr):
                if expr[1] == None or isinstance(expr[1],Unknown):
                    raise TypeCannotBeInferred(ast)
                res = expr[1]
        for i in range(len(o[len(o) - 1])):
            if o[len(o) - 1][i].name == c[1]:
                if isinstance(o[len(o) - 1][i].mtype.restype,Unknown):
                    o[len(o) - 1][i].mtype.restype = res
                
                if type(o[len(o) - 1][i].mtype.restype) != type(res):
                    raise TypeMismatchInStatement(ast)
        return o
    
    def visitDowhile(self, ast, c):
        o = c[0]
        new_scope = reduce(lambda a,b: b.accept(self, [0,a]),ast.sl[0],[[]])
        for j in ast.sl[1]:
            new_scope = j.accept(self,[new_scope + o,c[1]])

        ot = ast.exp.accept(self,[0,o,c[1]])
        o = ot[0]

        t = ot[1]
        if t == None:
            raise TypeCannotBeInferred(ast)
        if isinstance(ast.exp,Id):
            t = o[ot[1][0]][ot[1][1]].mtype
        elif isinstance(ast.exp,CallExpr):
            t = o[ot[1][0]][ot[1][1]].mtype.restype
        if isinstance(t,Unknown):
            t = BoolType()
            if isinstance(ast.exp,Id):
                o[ot[1][0]][ot[1][1]].mtype = t
                if isinstance(o[ot[1][0]][ot[1][1]].ktype,Parameter):
                    for j in range(len(o[len(o) - 1])):
                        if o[len(o) - 1][j].name == c[1]:
                            o[len(o) - 1][j].mtype.intype[ot[1][1]] = t
            elif isinstance(ast.exp,CallExpr):
                o[ot[1][0]][ot[1][1]].mtype.restype = t
        if not(isinstance(t,BoolType)):
            raise TypeMismatchInStatement(ast)

    def visitWhile(self, ast, c):
        ot = ast.exp.accept(self,[0,c[0],c[1]])
        o = ot[0]

        t = ot[1]
        if t == None:
            raise TypeCannotBeInferred(ast)
        if isinstance(ast.exp,Id):
            t = o[ot[1][0]][ot[1][1]].mtype
        elif isinstance(ast.exp,CallExpr):
            t = o[ot[1][0]][ot[1][1]].mtype.restype
        if isinstance(t,Unknown):
            t = BoolType()
            if isinstance(ast.exp,Id):
                o[ot[1][0]][ot[1][1]].mtype = t
                if isinstance(o[ot[1][0]][ot[1][1]].ktype,Parameter):
                    for j in range(len(o[len(o) - 1])):
                        if o[len(o) - 1][j].name == c[1]:
                            o[len(o) - 1][j].mtype.intype[ot[1][1]] = t
            elif isinstance(ast.exp,CallExpr):
                o[ot[1][0]][ot[1][1]].mtype.restype = t
        if not(isinstance(t,BoolType)):
            raise TypeMismatchInStatement(ast)

        new_scope = reduce(lambda a,b: b.accept(self, [0,a]),ast.sl[0],[[]])
        for j in ast.sl[1]:
            new_scope = j.accept(self,[new_scope + o,c[1]])
        
        return o

    def visitCallStmt(self, ast, c):
        ot = ast.method.accept(self,[1,c[0]])
        o = ot[0]
        e = Unknown()
        if ot[1] != None:
            e = o[ot[1][0]][ot[1][1]]
            if isinstance(e.mtype.restype,Unknown):
                o[ot[1][0]][ot[1][1]].mtype.restype = VoidType()
                e = o[ot[1][0]][ot[1][1]]
            if not(isinstance(e.mtype.restype,VoidType)):
                raise TypeMismatchInStatement(ast)
            if len(e.mtype.intype) != len(ast.param):
                raise TypeMismatchInStatement(ast)
            
            for i in range(len(e.mtype.intype)):
                p = ast.param[i].accept(self,[0,o,c[1]])
                o = p[0]
                t = Unknown()
                if isinstance(ast.param[i],Id):
                    t = o[p[1][0]][p[1][1]].mtype
                elif isinstance(ast.param[i],CallExpr):
                    t = o[p[1][0]][p[1][1]].mtype.restype
                else:
                    t = p[1]
                if (t == None):
                    raise TypeCannotBeInferred(ast)
                if isinstance(e.mtype.intype[i],Unknown) and isinstance(t,Unknown):
                    raise TypeCannotBeInferred(ast)
                elif isinstance(e.mtype.intype[i],Unknown):
                    o[ot[1][0]][ot[1][1]].mtype.intype[i] = t
                    if o[ot[1][0]][ot[1][1]].name == c[1]:
                        o[len(o) - 2][i].mtype = t
                elif isinstance(t,Unknown):
                    o[p[1][0]][p[1][1]].mtype = e.mtype.intype[i]
                    t = e.mtype.intype[i]
                    if isinstance(o[p[1][0]][p[1][1]].ktype,Parameter):
                        for j in range(len(o[len(o) - 1])):
                            if o[len(o) - 1][j].name == c[1]:
                                o[len(o) - 1][j].mtype.intype[p[1][1]] = e.mtype.intype[i]
                    t = e.mtype.intype[i]
                if type(e.mtype.intype[i]) != type(t):
                    raise TypeMismatchInStatement(ast)
            return o
        # else:
        #     raise Undeclared(Function(),ast.method.name)
    
    def visitIntLiteral(self, ast, c):
        if c[0] == 0:
            return [c[1],IntType()]

    def visitFloatLiteral(self, ast, c):
        if c[0] == 0:
            return [c[1],FloatType()]
    
    def visitBooleanLiteral(self, ast, c):
        if c[0] == 0:
            return [c[1],BoolType()]
    
    def visitStringLiteral(self, ast, c):
        if c[0] == 0:
            return [c[1],StringType()]

    def visitArrayLiteral(self, ast, c):
        if c[0] == 0:
            dim = []
            dim.append(len(ast.value))
            
            if isinstance(ast.value[0],ArrayLiteral):
                dim = ast.value[0].accept(self,[1,dim])
                return [c[1],ArrayType(dim[0],dim[1])]
            else:
                t = ast.value[0].accept(self,[0,c[1]])[1]
                return [c[1],ArrayType(dim,t)]

        elif c[0] == 1:
            dim = c[1]
            dim.append(len(ast.value))
            if isinstance(ast.value[0],ArrayLiteral):
                dim = ast.value[0].accept(self,[1,dim])
                return dim
            else:
                t = ast.value[0].accept(self,[0,c[1]])
                return [dim,t[1]]




        
