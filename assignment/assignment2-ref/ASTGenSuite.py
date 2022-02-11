# Lu Anh Khoa - 1852112
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x=0xF;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(0xF))])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))


    def test_ast_1(self):
        input = """Var:a=3,b=4.,c="gg";"""
        expect = Program([VarDecl(Id("a"),[],IntLiteral(3)),VarDecl(Id("b"),[],FloatLiteral(4.0)),VarDecl(Id("c"),[],StringLiteral('gg'))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))


    def test_ast_2(self):
        input = """Var: a=True,b=False;"""
        expect = Program([VarDecl(Id('a'),[],BooleanLiteral(True)),VarDecl(Id('b'),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))


    def test_ast_3(self):
        input = """Var: a[2]={1,2};"""
        expect = Program([VarDecl(Id('a'),[2],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))


    def test_ast_4(self):
        input = """Var: a[4][5][6], b[2][2] = {{3,4},{6,7}};"""
        expect = Program([VarDecl(Id('a'),[4,5,6],None),VarDecl(Id('b'),[2,2],ArrayLiteral([ArrayLiteral([IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(6),IntLiteral(7)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))


    def test_ast_5(self):
        input = """Var: a,b,c;
        Var: a,b,c,d;
        """
        expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))


    def test_ast_6(self):
        input = """
        Function: main
        Body:
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))


    def test_ast_7(self):
        input = """
        Function: main
        Parameter: a
        Body:
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))


    def test_ast_8(self):
        input = """
        Function: main
        Parameter: a[3], b[4][5]
        Body:
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[3],None),VarDecl(Id('b'),[4,5],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))


    def test_ast_9(self):
        input = """
        Var: a=3;
        Function: main
        Body:
            Var: p,q;
        EndBody.
        """
        expect = Program([VarDecl(Id('a'),[],IntLiteral(3)),FuncDecl(Id('main'),[],([VarDecl(Id('p'),[],None),VarDecl(Id('q'),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))


    def test_ast_10(self):
        input = """
        Function: main
        Body:
            a = 10;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('a'),IntLiteral(10))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))


    def test_ast_11(self):
        input = """
        Function: main
        Body:
            a = b;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('a'),Id('b'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))


    def test_ast_12(self):
        input = """
        Function: main
        Body:
            If a Then Var:b; b = a; EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[If([(Id('a'),[VarDecl(Id('b'),[],None)],[Assign(Id('b'),Id('a'))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))


    def test_ast_13(self):
        input = """
        Function: main
        Body:
            If a==3 Then Var:b; b = a; EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('==',Id('a'),IntLiteral(3)),[VarDecl(Id('b'),[],None)],[Assign(Id('b'),Id('a'))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))


    def test_ast_14(self):
        input = """
        Function: main
        Body:
            If a==3 Then 
                Var:b; 
            ElseIf a==4 Then
                c = -4;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('==',Id('a'),IntLiteral(3)),[VarDecl(Id('b'),[],None)],[]),(BinaryOp('==',Id('a'),IntLiteral(4)),[],[Assign(Id('c'),UnaryOp('-',IntLiteral(4)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))


    def test_ast_15(self):
        input = """
        Function: main
        Body:
            If a==3 Then 
                Var:b; 
                a = 5;
            Else
                a = 6;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('==',Id('a'),IntLiteral(3)),[VarDecl(Id('b'),[],None)],[Assign(Id('a'),IntLiteral(5))])],([],[Assign(Id('a'),IntLiteral(6))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))


    def test_ast_16(self):
        input = """
        Function: main
        Body:
            If a == True Then 
                Var:b; 
                a = 5;
            ElseIf a == 4 Then
                a = 6;
            Else
                b = -1;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('==',Id('a'),BooleanLiteral(True)),[VarDecl(Id('b'),[],None)],[Assign(Id('a'),IntLiteral(5))]),(BinaryOp('==',Id('a'),IntLiteral(4)),[],[Assign(Id('a'),IntLiteral(6))])],([],[Assign(Id('b'),UnaryOp('-',IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))


    def test_ast_17(self):
        input = """
        Function: main
        Body:
            For(i=1,i<10,1) Do
                a = a + 1;
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))


    def test_ast_18(self):
        input = """
        Function: main
        Body:
            For(i=1,i<10,1) Do
                Var: j;
                For(j=1,j<10,1) Do
                    a = a + 1;
                EndFor.
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),IntLiteral(1),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([VarDecl(Id('j'),[],None)],[For(Id('j'),IntLiteral(1),BinaryOp('<',Id('j'),IntLiteral(10)),IntLiteral(1),([],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))


    def test_ast_19(self):
        input = """
        Function: main
        Body:
            While a <. False Do
                b = b\\2;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[While(BinaryOp('<.',Id('a'),BooleanLiteral(False)),([],[Assign(Id('b'),BinaryOp('\\',Id('b'),IntLiteral(2)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))


    def test_ast_20(self):
        input = """
        Function: main
        Body:
            Do 
                Var: c = "45";
                b = b\\2; 
            While a <. False EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Dowhile(([VarDecl(Id('c'),[],StringLiteral('45'))],[Assign(Id('b'),BinaryOp('\\',Id('b'),IntLiteral(2)))]),BinaryOp('<.',Id('a'),BooleanLiteral(False)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))


    def test_ast_21(self):
        input = """
        Function: main
        Body:
            Break;
            Continue;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Break(),Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))


    def test_ast_22(self):
        input = """
        Function: main
        Body:
            foo();
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))


    def test_ast_23(self):
        input = """
        Function: main
        Body:
            foo(2,3e-4,"rt",True);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[IntLiteral(2),FloatLiteral(0.0003),StringLiteral('rt'),BooleanLiteral(True)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))


    def test_ast_24(self):
        input = """
        Function: main
        Body:
            foo(foo());
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[CallExpr(Id('foo'),[])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))


    def test_ast_25(self):
        input = """
        Function: main
        Body:
            Return;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))


    def test_ast_26(self):
        input = """
        Function: main
        Body:
            Return a+6;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('+',Id('a'),IntLiteral(6)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))


    def test_ast_27(self):
        input = """
        Var: a = {{2},{2},{4,5,6,7}}; 
        """
        expect = Program([VarDecl(Id('a'),[],ArrayLiteral([ArrayLiteral([IntLiteral(2)]),ArrayLiteral([IntLiteral(2)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))


    def test_ast_28(self):
        input = """
        Function: main
        Body:
            Return a < b;
            Return a <= b;
            Return a <. b;
            Return a <=. b;
            Return a > b;
            Return a >= b;
            Return a >. b;
            Return a >=. b;
            Return a == b;
            Return a != b;
            Return a =/= b;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('<',Id('a'),Id('b'))),Return(BinaryOp('<=',Id('a'),Id('b'))),Return(BinaryOp('<.',Id('a'),Id('b'))),Return(BinaryOp('<=.',Id('a'),Id('b'))),Return(BinaryOp('>',Id('a'),Id('b'))),Return(BinaryOp('>=',Id('a'),Id('b'))),Return(BinaryOp('>.',Id('a'),Id('b'))),Return(BinaryOp('>=.',Id('a'),Id('b'))),Return(BinaryOp('==',Id('a'),Id('b'))),Return(BinaryOp('!=',Id('a'),Id('b'))),Return(BinaryOp('=/=',Id('a'),Id('b')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))


    def test_ast_29(self):
        input = """
        Function: main
        Body:
            Return a&&b < c||d;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('<',BinaryOp('&&',Id('a'),Id('b')),BinaryOp('||',Id('c'),Id('d'))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))


    def test_ast_30(self):
        input = """
        Function: main
        Body:
            Return 1 + 2*4 + 5;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('+',BinaryOp('+',IntLiteral(1),BinaryOp('*',IntLiteral(2),IntLiteral(4))),IntLiteral(5)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))


    def test_ast_31(self):
        input = """
        Function: main
        Body:
            Return a&& b+c ||d;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('||',BinaryOp('&&',Id('a'),BinaryOp('+',Id('b'),Id('c'))),Id('d')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))


    def test_ast_32(self):
        input = """
        Function: main
        Body:
            Return a<b+c;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('<',Id('a'),BinaryOp('+',Id('b'),Id('c'))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))


    def test_ast_33(self):
        input = """
        Function: main
        Body:
            Return 5*a > b+5*0&&67;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('>',BinaryOp('*',IntLiteral(5),Id('a')),BinaryOp('&&',BinaryOp('+',Id('b'),BinaryOp('*',IntLiteral(5),IntLiteral(0))),IntLiteral(67))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))


    def test_ast_34(self):
        input = """
        Function: main
        Body:
            Return !a+t%e;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('+',UnaryOp('!',Id('a')),BinaryOp('%',Id('t'),Id('e'))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))


    def test_ast_35(self):
        input = """
        Function: main
        Body:
            Return !!!!e;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(UnaryOp('!',UnaryOp('!',UnaryOp('!',UnaryOp('!',Id('e'))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))


    def test_ast_36(self):
        input = """
        Function: main
        Body:
            Return -----a;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',UnaryOp('-',Id('a')))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))


    def test_ast_37(self):
        input = """
        Function: main
        Body:
            Return !-a;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(UnaryOp('!',UnaryOp('-',Id('a'))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))


    def test_ast_38(self):
        input = """
        Function: main
        Body:
            Return -(!a);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(UnaryOp('-',UnaryOp('!',Id('a'))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))


    def test_ast_39(self):
        input = """
        Function: main
        Body:
            Return a[3];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(Id('a'),[IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))


    def test_ast_40(self):
        input = """
        Function: main
        Body:
            Return a[3][0][-4];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(Id('a'),[IntLiteral(3),IntLiteral(0),UnaryOp('-',IntLiteral(4))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))


    def test_ast_41(self):
        input = """
        Function: main
        Body:
            Return a[3+3*8%90];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(3),BinaryOp('%',BinaryOp('*',IntLiteral(3),IntLiteral(8)),IntLiteral(90)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))


    def test_ast_42(self):
        input = """
        Function: main
        Body:
            Return a[a[a[2]]];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(Id('a'),[ArrayCell(Id('a'),[ArrayCell(Id('a'),[IntLiteral(2)])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))


    def test_ast_43(self):
        input = """
        Function: main
        Parameter: a[2][4], b[2]
        Body:
            Return a[x][y] == b[4];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('a'),[2,4],None),VarDecl(Id('b'),[2],None)],([],[Return(BinaryOp('==',ArrayCell(Id('a'),[Id('x'),Id('y')]),ArrayCell(Id('b'),[IntLiteral(4)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))


    def test_ast_44(self):
        input = """
        Function: main
        Body:
            Return foo()[1][3];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(1),IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))


    def test_ast_45(self):
        input = """
        Function: main
        Body:
            Return foo(a[1],foo(4,90));
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(CallExpr(Id('foo'),[ArrayCell(Id('a'),[IntLiteral(1)]),CallExpr(Id('foo'),[IntLiteral(4),IntLiteral(90)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))


    def test_ast_46(self):
        input = """
        Function: main
        Body:
            Return 6 + !a[foo()][-a && 6];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('+',IntLiteral(6),UnaryOp('!',ArrayCell(Id('a'),[CallExpr(Id('foo'),[]),BinaryOp('&&',UnaryOp('-',Id('a')),IntLiteral(6))]))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))


    def test_ast_47(self):
        input = """
        Function: main
        Body:
            Return (a+b)*c;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('*',BinaryOp('+',Id('a'),Id('b')),Id('c')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))


    def test_ast_48(self):
        input = """
        Function: main
        Body:
            Return a - -b;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('-',Id('a'),UnaryOp('-',Id('b'))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))


    def test_ast_49(self):
        input = """
        Function: main
        Body:
            Return ((1+2)*(3+4)%(a&&b) > 7) + 56 ;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('+',BinaryOp('>',BinaryOp('%',BinaryOp('*',BinaryOp('+',IntLiteral(1),IntLiteral(2)),BinaryOp('+',IntLiteral(3),IntLiteral(4))),BinaryOp('&&',Id('a'),Id('b'))),IntLiteral(7)),IntLiteral(56)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))


    def test_ast_50(self):
        input = """
        Function: main
        Body:
            Return (((((4+5))))) * 7;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('*',BinaryOp('+',IntLiteral(4),IntLiteral(5)),IntLiteral(7)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))


    def test_ast_51(self):
        input = """
        Function: main
        Body:
            Return {2,4,5,6}[2];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(ArrayLiteral([IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6)]),[IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))


    def test_ast_52(self):
        input = """
        Function: main
        Body:
        EndBody.

        Function: main2
        Body:
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[])),FuncDecl(Id('main2'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))


    def test_ast_53(self):
        input = """
        Var: a,b,c;
        Var: t=6,t=8,t=9;

        Function: main
        Body:
        EndBody.

        Function: main
        Body:
        EndBody.

        Function: main
        Parameter: x
        Body:
        EndBody.
        """
        expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('t'),[],IntLiteral(6)),VarDecl(Id('t'),[],IntLiteral(8)),VarDecl(Id('t'),[],IntLiteral(9)),FuncDecl(Id('main'),[],([],[])),FuncDecl(Id('main'),[],([],[])),FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))


    def test_ast_54(self):
        input = """
        Function: main
        Body:
            a =foo(a[1+2][a*func()])[a < b];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('a'),ArrayCell(CallExpr(Id('foo'),[ArrayCell(Id('a'),[BinaryOp('+',IntLiteral(1),IntLiteral(2)),BinaryOp('*',Id('a'),CallExpr(Id('func'),[]))])]),[BinaryOp('<',Id('a'),Id('b'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))


    def test_ast_55(self):
        input = """
        Function: main
        Body:
            foo()[3] = a;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(3)]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))


    def test_ast_56(self):
        input = """
        Function: main
        Body:
            foo()[a<b] = 0;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(CallExpr(Id('foo'),[]),[BinaryOp('<',Id('a'),Id('b'))]),IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))


    def test_ast_57(self):
        input = """
        Function: main
        Body:
            foo()[a<b] = foo()[a<b];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(CallExpr(Id('foo'),[]),[BinaryOp('<',Id('a'),Id('b'))]),ArrayCell(CallExpr(Id('foo'),[]),[BinaryOp('<',Id('a'),Id('b'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))


    def test_ast_58(self):
        input = """
        Function: main
        Body:
            (a+b)[3] = 4;
        EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(BinaryOp('+',Id('a'),Id('b')),[IntLiteral(3)]),IntLiteral(4))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))


    def test_ast_59(self):
        input = """
        Function: fibo
        Parameter: x
        Body:
            If (x == 1) || (x == 0) Then 
                Return 1;
            Else
                Return fibo(x-1) + fibo(x-2);
            EndIf.
        EndBody.

        Function: main
        Body:
            fibo(3);
        EndBody.
        """
        expect = Program([FuncDecl(Id('fibo'),[VarDecl(Id('x'),[],None)],([],[If([(BinaryOp('||',BinaryOp('==',Id('x'),IntLiteral(1)),BinaryOp('==',Id('x'),IntLiteral(0))),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp('+',CallExpr(Id('fibo'),[BinaryOp('-',Id('x'),IntLiteral(1))]),CallExpr(Id('fibo'),[BinaryOp('-',Id('x'),IntLiteral(2))])))]))])),FuncDecl(Id('main'),[],([],[CallStmt(Id('fibo'),[IntLiteral(3)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))


    def test_ast_60(self):
        input = """
        Function: main
        Body:
            b = (x == 0) || (x == 1);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('b'),BinaryOp('||',BinaryOp('==',Id('x'),IntLiteral(0)),BinaryOp('==',Id('x'),IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))


    def test_ast_61(self):
        input = """
        Function: main
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([VarDecl(Id('i'),[],IntLiteral(0))],[While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp('+.',Id('b'),FloatLiteral(1.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))


    def test_ast_62(self):
        input = """
        Function: main
        Body:
            While i < 21 Do
                Var: a;
                While j < 5 Do
                    Var: a;
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[While(BinaryOp('<',Id('i'),IntLiteral(21)),([VarDecl(Id('a'),[],None)],[While(BinaryOp('<',Id('j'),IntLiteral(5)),([VarDecl(Id('a'),[],None)],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))


    def test_ast_63(self):
        input = """
        Function: main
        Body:
            While i < 21 Do
                Var: a;
                For(a=1,a<6,8) Do
                    Var: b,c;
                    If b != c Then
                        b = 1;
                    Else
                        v = -7;
                    EndIf.
                EndFor.
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[While(BinaryOp('<',Id('i'),IntLiteral(21)),([VarDecl(Id('a'),[],None)],[For(Id('a'),IntLiteral(1),BinaryOp('<',Id('a'),IntLiteral(6)),IntLiteral(8),([VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],[If([(BinaryOp('!=',Id('b'),Id('c')),[],[Assign(Id('b'),IntLiteral(1))])],([],[Assign(Id('v'),UnaryOp('-',IntLiteral(7)))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))


    def test_ast_64(self):
        input = """
        Function: a
        Parameter: x, y
        Body:
            Var: x, y;
            Var: a=True, b, c = "o";
            b = -8;
            b = 5 % (b * 2);
            Return 0;
        EndBody.
        """
        expect = Program([FuncDecl(Id('a'),[VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None)],([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('a'),[],BooleanLiteral(True)),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],StringLiteral('o'))],[Assign(Id('b'),UnaryOp('-',IntLiteral(8))),Assign(Id('b'),BinaryOp('%',IntLiteral(5),BinaryOp('*',Id('b'),IntLiteral(2)))),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))


    def test_ast_65(self):
        input = """
        Var: a, b, c;
        Var: d = 5;
        Function: main
        Body:
            Var: x;
        EndBody.

        Function: main2
        Body:
        EndBody.

        Function: main3
        Body:
        EndBody.
        """
        expect = Program([VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],IntLiteral(5)),FuncDecl(Id('main'),[],([VarDecl(Id('x'),[],None)],[])),FuncDecl(Id('main2'),[],([],[])),FuncDecl(Id('main3'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))


    def test_ast_66(self):
        input = """
        Function: main
        Body:
            foo(!r, 5+6, 7&&6%4==1);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[UnaryOp('!',Id('r')),BinaryOp('+',IntLiteral(5),IntLiteral(6)),BinaryOp('==',BinaryOp('&&',IntLiteral(7),BinaryOp('%',IntLiteral(6),IntLiteral(4))),IntLiteral(1))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))


    def test_ast_67(self):
        input = """
        Function: main
        Body:
            (1+2)[1] = 1;
            foo(a,b,c);
            foo();
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(BinaryOp('+',IntLiteral(1),IntLiteral(2)),[IntLiteral(1)]),IntLiteral(1)),CallStmt(Id('foo'),[Id('a'),Id('b'),Id('c')]),CallStmt(Id('foo'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))


    def test_ast_68(self):
        input = """
        Function: main
        Body:
            a = ** comment goes here **  6*6;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('a'),BinaryOp('*',IntLiteral(6),IntLiteral(6)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))


    def test_ast_69(self):
        input = """
        Function: main
        Body:
            While a == 69 Do
                Var: c;
                c = -1;
                Do 
                    a[1] = 34;
                    c =  - 1 + c * 2;
                While c =/= 6. EndDo. 
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[While(BinaryOp('==',Id('a'),IntLiteral(69)),([VarDecl(Id('c'),[],None)],[Assign(Id('c'),UnaryOp('-',IntLiteral(1))),Dowhile(([],[Assign(ArrayCell(Id('a'),[IntLiteral(1)]),IntLiteral(34)),Assign(Id('c'),BinaryOp('+',UnaryOp('-',IntLiteral(1)),BinaryOp('*',Id('c'),IntLiteral(2))))]),BinaryOp('=/=',Id('c'),FloatLiteral(6.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))


    def test_ast_70(self):
        input = """
        Function: main
        Body:
            For (i = foo()[1], i < foo(2,{1,2,3},4), {{3}}) Do
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(1)]),BinaryOp('<',Id('i'),CallExpr(Id('foo'),[IntLiteral(2),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),IntLiteral(4)])),ArrayLiteral([ArrayLiteral([IntLiteral(3)])]),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))


    def test_ast_71(self):
        input = """
        Function: main
        Body:
            a = 4*.0.6;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('a'),BinaryOp('*.',IntLiteral(4),FloatLiteral(0.6)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))


    def test_ast_72(self):
        input = """
        Function: main
        Body:
            a = !a * !e % !!(-5);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('a'),BinaryOp('%',BinaryOp('*',UnaryOp('!',Id('a')),UnaryOp('!',Id('e'))),UnaryOp('!',UnaryOp('!',UnaryOp('-',IntLiteral(5))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))


    def test_ast_73(self):
        input = """
        Function: main
        Body:
            If (a == 1) && a == 5 Then
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[If([(BinaryOp('==',BinaryOp('&&',BinaryOp('==',Id('a'),IntLiteral(1)),Id('a')),IntLiteral(5)),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))


    def test_ast_74(self):
        input = """
        Function: main
        Body:
            b = -.-.--5;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('b'),UnaryOp('-.',UnaryOp('-.',UnaryOp('-',UnaryOp('-',IntLiteral(5))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))


    def test_ast_75(self):
        input = """
        Function: main
        Body:
            Return (foo(foo(), (foo)));
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(CallExpr(Id('foo'),[CallExpr(Id('foo'),[]),Id('foo')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))


    def test_ast_76(self):
        input = """
        Function: main
        Body:
            Return True % "234";
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('%',BooleanLiteral(True),StringLiteral('234')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))


    def test_ast_77(self):
        input = """
        Function: main
        Body:
            Return {1,2,3}[x];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),[Id('x')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))


    def test_ast_78(self):
        input = """
        Function: main
        Body:
            Return (((1==2) == 3) == 4) == ((5 == 6) == 7);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(BinaryOp('==',BinaryOp('==',BinaryOp('==',BinaryOp('==',IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),BinaryOp('==',BinaryOp('==',IntLiteral(5),IntLiteral(6)),IntLiteral(7))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))


    def test_ast_79(self):
        input = """
        Function: main
        Body:
            Return !y[4][foo()];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(UnaryOp('!',ArrayCell(Id('y'),[IntLiteral(4),CallExpr(Id('foo'),[])])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))


    def test_ast_80(self):
        input = """
        Function: main
        Body:
            Return (!y)[4][foo()];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(UnaryOp('!',Id('y')),[IntLiteral(4),CallExpr(Id('foo'),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))


    def test_ast_81(self):
        input = """
        Function: main
        Body:
            Return func(!y)[4][foo()];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Return(ArrayCell(CallExpr(Id('func'),[UnaryOp('!',Id('y'))]),[IntLiteral(4),CallExpr(Id('foo'),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))


    def test_ast_82(self):
        input = """
        Function: main
        Body:
            x = "dfd\\rfsd";
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('x'),StringLiteral('dfd\\rfsd'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))


    def test_ast_83(self):
        input = """
        Function: main
        Body:
            If (e)[4] Then 
            ElseIf (e)[a][b][c] Then
            Else 
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[If([(ArrayCell(Id('e'),[IntLiteral(4)]),[],[]),(ArrayCell(Id('e'),[Id('a'),Id('b'),Id('c')]),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))


    def test_ast_84(self):
        input = """
        Function: main
        Body:
            a[4][3][5] = b[4];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral(4),IntLiteral(3),IntLiteral(5)]),ArrayCell(Id('b'),[IntLiteral(4)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))


    def test_ast_85(self):
        input = """
        Function: main
        Body:
            5[4][3][2] = b[4];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(IntLiteral(5),[IntLiteral(4),IntLiteral(3),IntLiteral(2)]),ArrayCell(Id('b'),[IntLiteral(4)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))


    def test_ast_86(self):
        input = """
        Function: main
        Body:
            (1<x)[z][s] = 1;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(BinaryOp('<',IntLiteral(1),Id('x')),[Id('z'),Id('s')]),IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))


    def test_ast_87(self):
        input = """
        Var: x = 0xFF;
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(255))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))


    def test_ast_88(self):
        input = """
        Var: x = 0o77;
        """
        expect = Program([VarDecl(Id('x'),[],IntLiteral(63))])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))


    def test_ast_89(self):
        input = """
        Var: a[0x1][0o7][56] = {"True", True}, literal, array;
        """
        expect = Program([VarDecl(Id('a'),[1,7,56],ArrayLiteral([StringLiteral('True'),BooleanLiteral(True)])),VarDecl(Id('literal'),[],None),VarDecl(Id('array'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))


    def test_ast_empty_prog(self):
        input = """"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))


    def test_ast_91(self):
        input = """
        Function: main
        Body:
            a = a;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('a'),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))


    def test_ast_92(self):
        input = """
        Function: main
        Body:
            For(i = i == 0, f%4, c) Do
                e[2][3][4] = t[6][7][8];
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[For(Id('i'),BinaryOp('==',Id('i'),IntLiteral(0)),BinaryOp('%',Id('f'),IntLiteral(4)),Id('c'),([],[Assign(ArrayCell(Id('e'),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayCell(Id('t'),[IntLiteral(6),IntLiteral(7),IntLiteral(8)]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))


    def test_ast_93(self):
        input = """
        Function: main
        Body:
            Var: i;
            For(i=0,i<10,1) Do
            Var: i;
            For(i=0,i<10,1) Do
            Var: i;
            For(i=0,i<10,1) Do
        
            EndFor.
            EndFor.
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([VarDecl(Id('i'),[],None)],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([VarDecl(Id('i'),[],None)],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([VarDecl(Id('i'),[],None)],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(1),([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))


    def test_ast_94(self):
        input = """
        Function: main
        Body:
            a = !w[2];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('a'),UnaryOp('!',ArrayCell(Id('w'),[IntLiteral(2)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))


    def test_ast_95(self):
        input = """
        Function: main
        Body:
            (!w[2])[3] = a;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(UnaryOp('!',ArrayCell(Id('w'),[IntLiteral(2)])),[IntLiteral(3)]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))


    def test_ast_96(self):
        input = """
        Function: main
        Body:
            ((--w[2])[3][8])[7][9] = a;
        EndBody.
        """
        # expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(ArrayCell(UnaryOp("-",UnaryOp("-",ArrayCell(Id("w"),[IntLiteral(2)]))),[IntLiteral(3),IntLiteral(8)]),[IntLiteral(7),IntLiteral(9)]),Id("a"))]))])
        # expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(ArrayCell(ArrayCell(UnaryOp(-,UnaryOp(-,ArrayCell(Id(w),[IntLiteral(2)]))),[IntLiteral(3),IntLiteral(8)]),[IntLiteral(7)]),[IntLiteral(9)]),Id(a))]))])
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(ArrayCell(ArrayCell(UnaryOp('-',UnaryOp('-',ArrayCell(Id('w'),[IntLiteral(2)]))),[IntLiteral(3),IntLiteral(8)]),[IntLiteral(7),IntLiteral(9)]),Id('a'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))


    def test_ast_97(self):
        input = """
        Function: main
        Body:
            v = "True"[0] == "T";
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('v'),BinaryOp('==',ArrayCell(StringLiteral('True'),[IntLiteral(0)]),StringLiteral('T')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))


    def test_ast_98(self):
        input = """
        Function: main
        Body:
            While True Do
            While False Do
            While "True" Do
            
            EndWhile.
            EndWhile.
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[While(BooleanLiteral(True),([],[While(BooleanLiteral(False),([],[While(StringLiteral('True'),([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))


    def test_ast_99(self):
        input = """
        Function: main
        Body:
            r = !(r+5%4) * -7;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'),[],([],[Assign(Id('r'),BinaryOp('*',UnaryOp('!',BinaryOp('+',Id('r'),BinaryOp('%',IntLiteral(5),IntLiteral(4)))),UnaryOp('-',IntLiteral(7))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))



 
   