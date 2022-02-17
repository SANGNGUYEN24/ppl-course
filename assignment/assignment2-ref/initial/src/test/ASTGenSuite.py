# Trieu Minh Sang - 1852717
import unittest
from TestUtils import TestAST
# from AST import *

from initial.src.main.bkit.utils.BKitAST import *


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        """Global Declaration - simple """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_2(self):
        """Global Declaration - multivariable"""
        input = """Var:x,y,z;"""
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_3(self):
        """Global Declaration - array declaration"""
        input = """Var:x[1][2][3][4][5];"""
        expect = Program([VarDecl(Id("x"), [1, 2, 3, 4, 5], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_4(self):
        """Global Declaration - declaration with initialization"""
        input = """Var:x=2,z[1][2]=True,z,a[2]="abc";"""
        expect = Program([VarDecl(Id("x"), [], IntLiteral(2)), VarDecl(Id("z"), [1, 2], BooleanLiteral(True)),
                          VarDecl(Id("z"), [], None), VarDecl(Id("a"), [2], StringLiteral("abc"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_5(self):
        """Global Declaration - declaration with initialization"""
        input = """
        Var: x = "This is a string", b = True, c = False;
        """
        expect = Program(
            [VarDecl(Id("x"), [], StringLiteral("This is a string")), VarDecl(Id("b"), [], BooleanLiteral(True)),
             VarDecl(Id("c"), [], BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_6(self):
        """Global Declaration - declaration with initialization"""
        input = """
        Var: x[1][2] = {1,2,3};
        Var: z[4][5] = {"a","b","c"};
        """
        expect = Program([VarDecl(Id("x"), [1, 2], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])),
                          VarDecl(Id("z"), [4, 5],
                                  ArrayLiteral([StringLiteral("a"), StringLiteral("b"), StringLiteral("c")]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_7(self):
        """Global Declaration - declaration with initialization"""
        input = """
        Var: i1 = 1, i2 = 0o12, i3 = 0XA17;
        Var: f1 = 12910100e+123, f2 = 100.0012E-12;
        """
        expect = Program([VarDecl(Id("i1"), [], IntLiteral(1)), VarDecl(Id("i2"), [], IntLiteral(0o12)),
                          VarDecl(Id("i3"), [], IntLiteral(0XA17)), VarDecl(Id("f1"), [], FloatLiteral(12910100e+123)),
                          VarDecl(Id("f2"), [], FloatLiteral(100.0012E-12))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_8(self):
        """Global Declaration - Advance"""
        input = """
        ** Var: n = 1, str = "This is not count"; **
        Var: tbool = True, fbool = False;
        Var: str = "This is a string";
        ** Oups, The end! **
        """
        expect = Program(
            [VarDecl(Id("tbool"), [], BooleanLiteral(True)), VarDecl(Id("fbool"), [], BooleanLiteral(False)),
             VarDecl(Id("str"), [], StringLiteral("This is a string"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_9(self):
        """Global Declaration - Advance"""
        input = """
        Var: z[4][5] = {};
        """
        expect = Program([VarDecl(Id("z"), [4, 5], ArrayLiteral([]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_10(self):
        """Global Declaration - Advance"""
        input = """
        Var: x[1][2] = {1,{1,2,{"A"},{True,False}},True};
        """
        expect = Program([VarDecl(Id("x"), [1, 2], ArrayLiteral([IntLiteral(1), ArrayLiteral(
            [IntLiteral(1), IntLiteral(2), ArrayLiteral([StringLiteral("A")]),
             ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)])]), BooleanLiteral(True)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_11(self):
        """Global Declaration - Advance"""
        input = """
        Var: y = {{{{{{}}}}}};
        """
        expect = Program([VarDecl(Id("y"), [], ArrayLiteral(
            [ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([])])])])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_12(self):
        """Global Declaration - Advance"""
        input = """

        """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_13(self):
        """Global Declaration - Advance"""
        input = """
        Var: a[4] = {  1, 2,     4,   7 };
        """
        expect = Program(
            [VarDecl(Id("a"), [4], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(4), IntLiteral(7)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_14(self):
        """Global Declaration - Advance"""
        input = """
        Var: a, c = "Check", d = {1,2,3};
        Var: e = {}, f[13] = True;
        """
        expect = Program([VarDecl(Id("a"), [], None), VarDecl(Id("c"), [], StringLiteral("Check")),
                          VarDecl(Id("d"), [], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])),
                          VarDecl(Id("e"), [], ArrayLiteral([])), VarDecl(Id("f"), [13], BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_15(self):
        """Global Declaration - Advance"""
        input = """
        Var: a[13] = {{**Comment**"a", 0o132},{},0XFAB,{13.92e-12,"float"},92.3E1};
        """
        expect = Program([VarDecl(Id("a"), [13], ArrayLiteral(
            [ArrayLiteral([StringLiteral("a"), IntLiteral(0o132)]), ArrayLiteral([]), IntLiteral(0XFAB),
             ArrayLiteral([FloatLiteral(13.92e-12), StringLiteral("float")]), FloatLiteral(92.3E1)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_16(self):
        """Function Declaration - Simple"""
        input = """
        Function: foo
        Body:

        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_17(self):
        """Function Declaration - Parameter"""
        input = """
        Function: p
        Parameter: x, y,a[10][2][3],b[1]
        Body:

        EndBody.
        """
        expect = Program([FuncDecl(Id("p"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None),
                                             VarDecl(Id("a"), [10, 2, 3], None), VarDecl(Id("b"), [1], None)],
                                   ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_18(self):
        """Function Declaration - VarDecl Statement"""
        input = """
        Function: vardecl
        Parameter: x, y
        Body:
            Var: x;
        EndBody.
        """
        expect = Program([FuncDecl(Id("vardecl"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)],
                                   ([VarDecl(Id("x"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_19(self):
        """Function Declaration - VarDecl Statement"""
        input = """
        Function: vardecl
        Parameter: x, y
        Body:
            Var: x, y;
            Var: a[1];
            Var: a[999];
        EndBody.
        """
        expect = Program([FuncDecl(Id("vardecl"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)], (
        [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("a"), [1], None),
         VarDecl(Id("a"), [999], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_20(self):
        """Function Declaration - VarDecl Statement"""
        input = """
        Function: vardecl
        Parameter: x, y
        Body:
            Var: x = 2, y[3][2] =4;
            Var: a[1];
            Var: b = "check";
        EndBody.
        """
        expect = Program([FuncDecl(Id("vardecl"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)], (
        [VarDecl(Id("x"), [], IntLiteral(2)), VarDecl(Id("y"), [3, 2], IntLiteral(4)), VarDecl(Id("a"), [1], None),
         VarDecl(Id("b"), [], StringLiteral("check"))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_21(self):
        """Function Declaration - VarDecl Statement"""
        input = """
        Function: vardecl
        Body:
            ** Var: n = 1, str = "This is not count"; **
            Var: tbool = True, fbool = False;
            Var: str = "This is a string";
            ** Oups, The end! **
        EndBody.
        """
        expect = Program([FuncDecl(Id("vardecl"), [], (
        [VarDecl(Id("tbool"), [], BooleanLiteral(True)), VarDecl(Id("fbool"), [], BooleanLiteral(False)),
         VarDecl(Id("str"), [], StringLiteral("This is a string"))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_22(self):
        """Function Declaration - VarDecl Statement"""
        input = """
        Function: vardecl
        Parameter: x,y,z,a[12]
        Body:
            Var: i1 = 1, i2 = 0o12, i3 = 0XA17;
            Var: f1 = 12910100e+123, f2 = 100.0012E-12;
        EndBody.
        """
        expect = Program([FuncDecl(Id("vardecl"),
                                   [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None),
                                    VarDecl(Id("a"), [12], None)], (
                                   [VarDecl(Id("i1"), [], IntLiteral(1)), VarDecl(Id("i2"), [], IntLiteral(0o12)),
                                    VarDecl(Id("i3"), [], IntLiteral(0XA17)),
                                    VarDecl(Id("f1"), [], FloatLiteral(12910100e+123)),
                                    VarDecl(Id("f2"), [], FloatLiteral(100.0012E-12))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_23(self):
        """Function Declaration - Assignment Statement"""
        input = """
        Function: assignment
        Body:
            x = 2;
        EndBody.
        """
        expect = Program([FuncDecl(Id("assignment"), [], ([], [Assign(Id("x"), IntLiteral(2))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_24(self):
        """Function Declaration - Assignment Statement"""
        input = """
        Function: expression
        Body:
            x = 2 + 3;
        EndBody.
        """
        expect = Program(
            [FuncDecl(Id("expression"), [], ([], [Assign(Id("x"), BinaryOp("+", IntLiteral(2), IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_25(self):
        """ Function Declaration - Expression """
        input = """
        Function: expression
        Body:
            x = (2 + 3 - 4 * 5) + 3;
        EndBody.
        """
        expect = Program([FuncDecl(Id("expression"), [], ([], [Assign(Id("x"), BinaryOp("+", BinaryOp("-", BinaryOp("+",
                                                                                                                    IntLiteral(
                                                                                                                        2),
                                                                                                                    IntLiteral(
                                                                                                                        3)),
                                                                                                      BinaryOp("*",
                                                                                                               IntLiteral(
                                                                                                                   4),
                                                                                                               IntLiteral(
                                                                                                                   5))),
                                                                                        IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_26(self):
        """ Function Declaration - Expression """
        input = """
        Function: expression
        Body:
            x = 1 + 2 + 3 + 4 + 5;
        EndBody.
        """
        expect = Program([FuncDecl(Id("expression"), [], ([], [Assign(Id("x"), BinaryOp("+", BinaryOp("+", BinaryOp("+",
                                                                                                                    BinaryOp(
                                                                                                                        "+",
                                                                                                                        IntLiteral(
                                                                                                                            1),
                                                                                                                        IntLiteral(
                                                                                                                            2)),
                                                                                                                    IntLiteral(
                                                                                                                        3)),
                                                                                                      IntLiteral(4)),
                                                                                        IntLiteral(5)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_27(self):
        """ Function Declaration - Expression """
        input = """
        Function: expression
        Body:
            x = ((-3 != (4 && False)) || True) >. -4.12E-32;
        EndBody.
        """
        expect = Program([FuncDecl(Id("expression"), [], ([], [Assign(Id("x"), BinaryOp(">.", BinaryOp("||",
                                                                                                       BinaryOp("!=",
                                                                                                                UnaryOp(
                                                                                                                    "-",
                                                                                                                    IntLiteral(
                                                                                                                        3)),
                                                                                                                BinaryOp(
                                                                                                                    "&&",
                                                                                                                    IntLiteral(
                                                                                                                        4),
                                                                                                                    BooleanLiteral(
                                                                                                                        False))),
                                                                                                       BooleanLiteral(
                                                                                                           True)),
                                                                                        UnaryOp("-", FloatLiteral(
                                                                                            4.12E-32))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_28(self):
        """ Function Declaration - Expression """
        input = """
        Function: expression
        Parameter: a,b
        Body:
            a[12] = -foo(1) + -((a || b) > 2) \\ 32 % arr[11];
        EndBody.
        """
        expect = Program([FuncDecl(Id("expression"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)], ([], [
            Assign(ArrayCell(Id("a"), [IntLiteral(12)]),
                   BinaryOp("+", UnaryOp("-", CallExpr(Id("foo"), [IntLiteral(1)])), BinaryOp("%", BinaryOp("\\",
                                                                                                            UnaryOp("-",
                                                                                                                    BinaryOp(
                                                                                                                        ">",
                                                                                                                        BinaryOp(
                                                                                                                            "||",
                                                                                                                            Id("a"),
                                                                                                                            Id("b")),
                                                                                                                        IntLiteral(
                                                                                                                            2))),
                                                                                                            IntLiteral(
                                                                                                                32)),
                                                                                              ArrayCell(Id("arr"), [
                                                                                                  IntLiteral(
                                                                                                      11)]))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_29(self):
        """ Function Declaration - Expression """
        input = """
        Function: expression
        Body:
            a = foo(foo() + foo({1,2,3}));
        EndBody.
        """
        expect = Program([FuncDecl(Id("expression"), [], ([], [Assign(Id("a"), CallExpr(Id("foo"), [
            BinaryOp("+", CallExpr(Id("foo"), []),
                     CallExpr(Id("foo"), [ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_30(self):
        """ Function Declaration - Expression """
        input = """
        Function: expression
        Body:
            a = foo(foo() && foo(1,2.33,"aa",True),foo(foo(foo(foo() + 2))));
        EndBody.
        """
        expect = Program([FuncDecl(Id("expression"), [], ([], [Assign(Id("a"), CallExpr(Id("foo"), [
            BinaryOp("&&", CallExpr(Id("foo"), []), CallExpr(Id("foo"),
                                                             [IntLiteral(1), FloatLiteral(2.33), StringLiteral("aa"),
                                                              BooleanLiteral(True)])), CallExpr(Id("foo"), [
                CallExpr(Id("foo"),
                         [CallExpr(Id("foo"), [BinaryOp("+", CallExpr(Id("foo"), []), IntLiteral(2))])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_31(self):
        """ Function Declaration - Simple If-Statement """
        input = """
        Function: if
        Body:
            If a == 2 Then
                a = 3;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("if"), [], (
        [], [If([(BinaryOp("==", Id("a"), IntLiteral(2)), [], [Assign(Id("a"), IntLiteral(3))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_32(self):
        """ Function Declaration - Simple If-Statement """
        input = """
        Function: if
        Body:
            If a == 2 Then
                If a == 3 Then
                    If a == 4 Then
                        Var: a;
                        a = 2;
                    EndIf.
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("if"), [], ([], [If([(BinaryOp("==", Id("a"), IntLiteral(2)), [], [If([(BinaryOp(
            "==", Id("a"), IntLiteral(3)), [], [If([(BinaryOp("==", Id("a"), IntLiteral(4)),
                                                     [VarDecl(Id("a"), [], None)], [Assign(Id("a"), IntLiteral(2))])],
                                                   ([], []))])], ([], []))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_33(self):
        """ Function Declaration - If-Statement + ElIf-Statement """
        input = """
        Function: if
        Body:
            If a == 2 Then
                Var: x=1,b;
                Var: y[1][2][3];
                a = 3;
                y = x + 3 \\ 2;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("if"), [], ([], [If([(BinaryOp("==", Id("a"), IntLiteral(2)),
                                                            [VarDecl(Id("x"), [], IntLiteral(1)),
                                                             VarDecl(Id("b"), [], None),
                                                             VarDecl(Id("y"), [1, 2, 3], None)],
                                                            [Assign(Id("a"), IntLiteral(3)), Assign(Id("y"),
                                                                                                    BinaryOp("+",
                                                                                                             Id("x"),
                                                                                                             BinaryOp(
                                                                                                                 "\\",
                                                                                                                 IntLiteral(
                                                                                                                     3),
                                                                                                                 IntLiteral(
                                                                                                                     2))))])],
                                                          ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_34(self):
        """ Function Declaration - If-Statement + ElIf-Statement """
        input = """
        Function: if_elseif
        Body:
            If a > 1 Then
                a = 1;
            ElseIf a == 1 Then
                a = 0;
            ElseIf a < 1 Then
                Var: b = True;
                a = -1;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("if_elseif"), [], ([], [
            If([(BinaryOp(">", Id("a"), IntLiteral(1)), [], [Assign(Id("a"), IntLiteral(1))]),
                (BinaryOp("==", Id("a"), IntLiteral(1)), [], [Assign(Id("a"), IntLiteral(0))]), (
                BinaryOp("<", Id("a"), IntLiteral(1)), [VarDecl(Id("b"), [], BooleanLiteral(True))],
                [Assign(Id("a"), UnaryOp("-", IntLiteral(1)))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_35(self):
        """ Function Declaration - If-Statement + ElIf-Statement """
        input = """
        Function: if_elseif
        Body:
            If (foo(2) \\ 2) * 3 >. 2.35E-12 Then
                a = 1;
            ElseIf a < 5 + 1 Then
                a = 2;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("if_elseif"), [], ([], [If([(BinaryOp(">.", BinaryOp("*", BinaryOp("\\", CallExpr(
            Id("foo"), [IntLiteral(2)]), IntLiteral(2)), IntLiteral(3)), FloatLiteral(2.35E-12)), [],
                                                                   [Assign(Id("a"), IntLiteral(1))]), (
                                                                  BinaryOp("<", Id("a"),
                                                                           BinaryOp("+", IntLiteral(5), IntLiteral(1))),
                                                                  [], [Assign(Id("a"), IntLiteral(2))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_36(self):
        """ Function Declaration - If-Statement + ElIf-Statement """
        input = """
        Function: if_elseif
        Body:
            If a > 1 Then
                a = 1;
            ElseIf a == 1 Then
                Var: x;
                If x == -1 Then
                    Var: y;
                    y = 2;
                EndIf.
            ElseIf a < 1 Then
                Var: y;
                If x < 1 Then
                    x = 2;
                ElseIf x > 1 Then
                    x = 3;
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("if_elseif"), [], ([], [
            If([(BinaryOp(">", Id("a"), IntLiteral(1)), [], [Assign(Id("a"), IntLiteral(1))]), (
            BinaryOp("==", Id("a"), IntLiteral(1)), [VarDecl(Id("x"), [], None)], [If([(BinaryOp("==", Id("x"),
                                                                                                 UnaryOp("-",
                                                                                                         IntLiteral(
                                                                                                             1))),
                                                                                        [VarDecl(Id("y"), [], None)], [
                                                                                            Assign(Id("y"),
                                                                                                   IntLiteral(2))])],
                                                                                      ([], []))]), (
                BinaryOp("<", Id("a"), IntLiteral(1)), [VarDecl(Id("y"), [], None)], [
                    If([(BinaryOp("<", Id("x"), IntLiteral(1)), [], [Assign(Id("x"), IntLiteral(2))]),
                        (BinaryOp(">", Id("x"), IntLiteral(1)), [], [Assign(Id("x"), IntLiteral(3))])], ([], []))])],
               ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_37(self):
        """ Function Declaration - If-Statement + ElIf-Statement + Else Statement """
        input = """
        Function: if_elseif_else
        Body:
            If a == 2 Then
                Var: x;
                a = 2;
            Else
                Var: y;
                a = 1;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("if_elseif_else"), [], ([], [If([(BinaryOp("==", Id("a"), IntLiteral(2)),
                                                                        [VarDecl(Id("x"), [], None)],
                                                                        [Assign(Id("a"), IntLiteral(2))])], (
                                                                      [VarDecl(Id("y"), [], None)],
                                                                      [Assign(Id("a"), IntLiteral(1))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_38(self):
        """ Function Declaration - If-Statement + ElIf-Statement + Else Statement """
        input = """
        Function: if_elseif_else
        Body:
            If a == 2 Then
                Var: a, b = 2;
                a = 3;
                b = 4;
            ElseIf a == 1 Then
                a = 2;
            ElseIf a < 1 Then
                a = 1;
            Else
                a = 3;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("if_elseif_else"), [], ([], [If([(BinaryOp("==", Id("a"), IntLiteral(2)),
                                                                        [VarDecl(Id("a"), [], None),
                                                                         VarDecl(Id("b"), [], IntLiteral(2))],
                                                                        [Assign(Id("a"), IntLiteral(3)),
                                                                         Assign(Id("b"), IntLiteral(4))]), (
                                                                       BinaryOp("==", Id("a"), IntLiteral(1)), [],
                                                                       [Assign(Id("a"), IntLiteral(2))]), (
                                                                       BinaryOp("<", Id("a"), IntLiteral(1)), [],
                                                                       [Assign(Id("a"), IntLiteral(1))])],
                                                                      ([], [Assign(Id("a"), IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_39(self):
        """ Function Declaration - If-Statement + ElIf-Statement + Else Statement """
        input = """
        Function: if_elseif_else
        Body:
            If a == 2 Then
                If a == 3 Then
                    If a == 4 Then
                        Var: a;
                        a = 2;
                    Else
                        a = 1;
                    EndIf.
                Else
                    a = 1;
                EndIf.
            Else
                a = 1;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("if_elseif_else"), [], ([], [If([(BinaryOp("==", Id("a"), IntLiteral(2)), [], [
            If([(BinaryOp("==", Id("a"), IntLiteral(3)), [], [If([(BinaryOp("==", Id("a"), IntLiteral(4)),
                                                                   [VarDecl(Id("a"), [], None)],
                                                                   [Assign(Id("a"), IntLiteral(2))])],
                                                                 ([], [Assign(Id("a"), IntLiteral(1))]))])],
               ([], [Assign(Id("a"), IntLiteral(1))]))])], ([], [Assign(Id("a"), IntLiteral(1))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_40(self):
        """ Function Declaration - If-Statement + ElIf-Statement + Else Statement """
        input = """
        Function: if_elseif_else
        Body:
            If a > 1 Then
                a = 1;
            ElseIf a == 1 Then
                Var: x;
                If x == -1 Then
                    Var: y;
                    y = 2;
                EndIf.
            ElseIf a < 1 Then
                Var: y;
                If x < 1 Then
                    x = 2;
                ElseIf x > 1 Then
                    x = 3;
                EndIf.
            Else
                Var: h;
                a = 2;
                If a > 2 Then
                    t = True;
                Else
                    t = False;
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("if_elseif_else"), [], ([], [
            If([(BinaryOp(">", Id("a"), IntLiteral(1)), [], [Assign(Id("a"), IntLiteral(1))]), (
            BinaryOp("==", Id("a"), IntLiteral(1)), [VarDecl(Id("x"), [], None)], [If([(BinaryOp("==", Id("x"),
                                                                                                 UnaryOp("-",
                                                                                                         IntLiteral(
                                                                                                             1))),
                                                                                        [VarDecl(Id("y"), [], None)], [
                                                                                            Assign(Id("y"),
                                                                                                   IntLiteral(2))])],
                                                                                      ([], []))]), (
                BinaryOp("<", Id("a"), IntLiteral(1)), [VarDecl(Id("y"), [], None)], [
                    If([(BinaryOp("<", Id("x"), IntLiteral(1)), [], [Assign(Id("x"), IntLiteral(2))]),
                        (BinaryOp(">", Id("x"), IntLiteral(1)), [], [Assign(Id("x"), IntLiteral(3))])], ([], []))])], (
               [VarDecl(Id("h"), [], None)], [Assign(Id("a"), IntLiteral(2)), If([(
                                                                                  BinaryOp(">", Id("a"), IntLiteral(2)),
                                                                                  [], [Assign(Id("t"),
                                                                                              BooleanLiteral(True))])],
                                                                                 ([], [Assign(Id("t"), BooleanLiteral(
                                                                                     False))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_41(self):
        """ Function Declaration - Simple For-Statement """
        input = """
        Function: for
        Body:
            For (a = 2, a < 3, a + 1) Do
                b = b + 1;
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id("for"), [], ([], [
            For(Id("a"), IntLiteral(2), BinaryOp("<", Id("a"), IntLiteral(3)), BinaryOp("+", Id("a"), IntLiteral(1)),
                ([], [Assign(Id("b"), BinaryOp("+", Id("b"), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_42(self):
        """ Function Declaration - Simple For-Statement """
        input = """
        Function: for
        Body:
            For (a = "string", foo(a[1]) \\ 4, a < b) Do
                Var: x = 2, y;
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id("for"), [], ([], [For(Id("a"), StringLiteral("string"), BinaryOp("\\", CallExpr(
            Id("foo"), [ArrayCell(Id("a"), [IntLiteral(1)])]), IntLiteral(4)), BinaryOp("<", Id("a"), Id("b")), (
                                                            [VarDecl(Id("x"), [], IntLiteral(2)),
                                                             VarDecl(Id("y"), [], None)], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_43(self):
        """ Function Declaration - Simple For-Statement """
        input = """
        Function: for
        Body:
            For (i = test()[999], t || foo1(True,{"a","b","c"},False), {{111}}) Do EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('for'), [], ([], [
            For(Id('i'), ArrayCell(CallExpr(Id('test'), []), [IntLiteral(999)]), BinaryOp('||', Id('t'),
                                                                                          CallExpr(Id('foo1'), [
                                                                                              BooleanLiteral(True),
                                                                                              ArrayLiteral(
                                                                                                  [StringLiteral("a"),
                                                                                                   StringLiteral("b"),
                                                                                                   StringLiteral("c")]),
                                                                                              BooleanLiteral(False)])),
                ArrayLiteral([ArrayLiteral([IntLiteral(111)])]), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_44(self):
        """ Function Declaration - Advance For-Statement """
        input = """
        Function: for
        Body:
            For (a = {1,{"a","b"},True}, a[1][2] \\ 4, a || b && c) Do
                Var: x = 2, y;
                a = a + 1;
                b = b - 2;
                Var: c;
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id("for"), [], ([], [For(Id("a"), ArrayLiteral(
            [IntLiteral(1), ArrayLiteral([StringLiteral("a"), StringLiteral("b")]), BooleanLiteral(True)]),
                                                            BinaryOp("\\",
                                                                     ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)]),
                                                                     IntLiteral(4)),
                                                            BinaryOp("&&", BinaryOp("||", Id("a"), Id("b")), Id("c")), (
                                                            [VarDecl(Id("x"), [], IntLiteral(2)),
                                                             VarDecl(Id("y"), [], None), VarDecl(Id("c"), [], None)],
                                                            [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))),
                                                             Assign(Id("b"),
                                                                    BinaryOp("-", Id("b"), IntLiteral(2)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_45(self):
        """ Function Declaration - Advance For-Statement """
        input = """
        Function: for
        Body:
            For(i=1,i<.999,32) Do
                Var: check;
                For(j=1,t +. 1,1) Do
                    e = x + 12;
                EndFor.
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('for'), [], ([], [
            For(Id('i'), IntLiteral(1), BinaryOp('<.', Id('i'), IntLiteral(999)), IntLiteral(32), (
            [VarDecl(Id('check'), [], None)], [
                For(Id('j'), IntLiteral(1), BinaryOp('+.', Id('t'), IntLiteral(1)), IntLiteral(1),
                    ([], [Assign(Id('e'), BinaryOp('+', Id('x'), IntLiteral(12)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_46(self):
        """ Function Declaration - Advance For-Statement """
        input = """
        Function: for
        Body:
            While a \\ 21 Do
                Var: b[13] = "a";
                For(a=1,a%6,2) Do
                    Var: x,y;
                    If x != y Then
                        t = 1;
                    Else
                        t = -7;
                    EndIf.
                EndFor.
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('for'), [], ([], [While(BinaryOp('\\', Id('a'), IntLiteral(21)), (
        [VarDecl(Id('b'), [13], StringLiteral("a"))], [
            For(Id('a'), IntLiteral(1), BinaryOp('%', Id('a'), IntLiteral(6)), IntLiteral(2), (
            [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None)], [
                If([(BinaryOp('!=', Id('x'), Id('y')), [], [Assign(Id('t'), IntLiteral(1))])],
                   ([], [Assign(Id('t'), UnaryOp('-', IntLiteral(7)))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_47(self):
        """ Function Declaration - Advance For-Statement """
        input = """
        Function: for
        Body:
            Var: a;
            For(a=1,a<1,1) Do
                Var: b;
                For(b=2,b<2,2) Do
                    Var: c;
                    For(c=3,c<3,3) Do
        
                    EndFor.
                EndFor.
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('for'), [], ([VarDecl(Id('a'), [], None)], [
            For(Id('a'), IntLiteral(1), BinaryOp('<', Id('a'), IntLiteral(1)), IntLiteral(1), (
            [VarDecl(Id('b'), [], None)], [
                For(Id('b'), IntLiteral(2), BinaryOp('<', Id('b'), IntLiteral(2)), IntLiteral(2), (
                [VarDecl(Id('c'), [], None)],
                [For(Id('c'), IntLiteral(3), BinaryOp('<', Id('c'), IntLiteral(3)), IntLiteral(3), ([], []))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_48(self):
        """ Function Declaration - Simple While-Statement """
        input = """
        Function: while
        Body:
            While t != False Do
                b = b + 1;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('while'), [], ([], [While(BinaryOp('!=', Id('t'), BooleanLiteral(False)), (
        [], [Assign(Id('b'), BinaryOp('+', Id('b'), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_49(self):
        """ Function Declaration - Simple While-Statement """
        input = """
        Function: while
        Body:
            While x == 2 Do

            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("while"), [], ([], [While(BinaryOp("==", Id("x"), IntLiteral(2)), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_50(self):
        """ Function Declaration - Simple While-Statement """
        input = """
        Function: while
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('while'), [], ([VarDecl(Id('i'), [], IntLiteral(0))], [
            While(BinaryOp('<', Id('i'), IntLiteral(5)),
                  ([], [Assign(ArrayCell(Id('a'), [Id('i')]), BinaryOp('+.', Id('b'), FloatLiteral(1.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_51(self):
        """ Function Declaration - Advance While-Statement """
        input = """
        Function: while
        Body:
            While i < 1 Do
                While j < 1 Do
                    Var: x,y,z;
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('while'), [], ([], [While(BinaryOp('<', Id('i'), IntLiteral(1)), ([], [
            While(BinaryOp('<', Id('j'), IntLiteral(1)),
                  ([VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('z'), [], None)], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_52(self):
        """ Function Declaration - Advance While-Statement """
        input = """
        Function: while
        Body:
            While t%21 Do
                Var: x[133] = 1;
                For(i=1,i>3,1) Do
                    Var: m[2],n;
                    If b != c Then
                        b = 1;
                    Else
                        v = -7;
                    EndIf.
                EndFor.
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id('while'), [], ([], [While(BinaryOp('%', Id('t'), IntLiteral(21)), (
        [VarDecl(Id('x'), [133], IntLiteral(1))], [
            For(Id('i'), IntLiteral(1), BinaryOp('>', Id('i'), IntLiteral(3)), IntLiteral(1), (
            [VarDecl(Id('m'), [2], None), VarDecl(Id('n'), [], None)], [
                If([(BinaryOp('!=', Id('b'), Id('c')), [], [Assign(Id('b'), IntLiteral(1))])],
                   ([], [Assign(Id('v'), UnaryOp('-', IntLiteral(7)))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_53(self):
        """ Function Declaration - Advance While-Statement """
        input = """
        Function: while
        Body:
            While a == 1 Do
                Var: x = 2;
                Return;
                Var: y[2] = 3;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("while"), [], ([], [While(BinaryOp("==", Id("a"), IntLiteral(1)), (
        [VarDecl(Id("x"), [], IntLiteral(2)), VarDecl(Id("y"), [2], IntLiteral(3))], [Return(None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_54(self):
        """ Function Declaration - Advance While-Statement """
        input = """
        Function: while
        Body:
            While (1) Do
                Return;
                Continue;
                Return;
                Continue;
                Break;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("while"), [], (
        [], [While(IntLiteral(1), ([], [Return(None), Continue(), Return(None), Continue(), Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_55(self):
        """ Function Declaration - Advance While-Statement """
        input = """
        Function: while
        Body:
            While 1 Do
                Var: x,y;
                Var: z;
                Var: a[1] = 2;
                Var: t[2][3];
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("while"), [], ([], [While(IntLiteral(1), (
        [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None),
         VarDecl(Id("a"), [1], IntLiteral(2)), VarDecl(Id("t"), [2, 3], None)], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_56(self):
        """ Function Declaration - Simple DoWhile-Statement """
        input = """
        Function: do_while
        Body:
            Do 
                Var: a;
                a = 1;
            While a != False EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id("do_while"), [], ([], [
            Dowhile(([VarDecl(Id("a"), [], None)], [Assign(Id("a"), IntLiteral(1))]),
                    BinaryOp("!=", Id("a"), BooleanLiteral(False)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_57(self):
        """ Function Declaration - Simple DoWhile-Statement """
        input = """
        Function: do_while
        Body:
            Do 
                Break;
                a = 1;
                Return(a);
            While a > 0 EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id("do_while"), [], ([], [
            Dowhile(([], [Break(), Assign(Id("a"), IntLiteral(1)), Return(Id("a"))]),
                    BinaryOp(">", Id("a"), IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_58(self):
        """ Function Declaration - Advance DoWhile-Statement """
        input = """
        Function: do_while
        Body:
            Do 
                Var: c = "45";
                b = b\\2; 
            While a <. False EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id('do_while'), [], ([], [Dowhile(
            ([VarDecl(Id('c'), [], StringLiteral('45'))], [Assign(Id('b'), BinaryOp('\\', Id('b'), IntLiteral(2)))]),
            BinaryOp('<.', Id('a'), BooleanLiteral(False)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_59(self):
        """ Function Declaration - Advance DoWhile-Statement """
        input = """
        Function: do_while
        Body:
            Do
                Return;
                Continue;
                Break;
                Return;
            While a == 2 EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id("do_while"), [], ([], [
            Dowhile(([], [Return(None), Continue(), Break(), Return(None)]),
                    BinaryOp("==", Id("a"), IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_60(self):
        """ Function Declaration - Other Statement """
        input = """
        Function: break
        Body:
            Break;
        EndBody.
        """
        expect = Program([FuncDecl(Id("break"), [], ([], [Break()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_61(self):
        """ Function Declaration - Other Statement """
        input = """
        Function: break
        Body:
            Break;
            Break;
            Break;
            Break;
            Break;
        EndBody.
        """
        expect = Program([FuncDecl(Id("break"), [], ([], [Break(), Break(), Break(), Break(), Break()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_62(self):
        """ Function Declaration - Other Statement """
        input = """
        Function: break
        Body:
            Var: x;
            While a > 1 Do
                Break;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("break"), [], (
        [VarDecl(Id("x"), [], None)], [While(BinaryOp(">", Id("a"), IntLiteral(1)), ([], [Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_63(self):
        """ Function Declaration - Other Statement """
        input = """
        Function: continue
        Body:
            Continue;
        EndBody.
        """
        expect = Program([FuncDecl(Id("continue"), [], ([], [Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_64(self):
        """ Function Declaration - Other Statement """
        input = """
        Function: break
        Body:
            Continue;
            Continue;
            Continue;
            Continue;
            Continue;
        EndBody.
        """
        expect = Program(
            [FuncDecl(Id("break"), [], ([], [Continue(), Continue(), Continue(), Continue(), Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_65(self):
        """ Function Declaration - Other Statement """
        input = """
        Function: break
        Body:
            Var: x;
            While a > 1 Do
                Continue;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("break"), [], (
        [VarDecl(Id("x"), [], None)], [While(BinaryOp(">", Id("a"), IntLiteral(1)), ([], [Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_66(self):
        """ Function Declaration - Other Statement """
        input = """
        Function: return
        Body:
            Return;
        EndBody.
        """
        expect = Program([FuncDecl(Id("return"), [], ([], [Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_67(self):
        """ Function Declaration - Other Statement """
        input = """
        Function: return
        Body:
            Return(True);
        EndBody.
        """
        expect = Program([FuncDecl(Id("return"), [], ([], [Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_68(self):
        """ Function Declaration - Other Statement """
        input = """
        Function: return
        Body:
            Return((2 + 3 - 4 * 5) + 3);
        EndBody.
        """
        expect = Program([FuncDecl(Id("return"), [], ([], [Return(BinaryOp("+", BinaryOp("-",
                                                                                         BinaryOp("+", IntLiteral(2),
                                                                                                  IntLiteral(3)),
                                                                                         BinaryOp("*", IntLiteral(4),
                                                                                                  IntLiteral(5))),
                                                                           IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_69(self):
        """ Function Declaration - Other Statement """
        input = """
        Function: return
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
        expect = Program([FuncDecl(Id('return'), [], ([], [Return(BinaryOp('<', Id('a'), Id('b'))),
                                                           Return(BinaryOp('<=', Id('a'), Id('b'))),
                                                           Return(BinaryOp('<.', Id('a'), Id('b'))),
                                                           Return(BinaryOp('<=.', Id('a'), Id('b'))),
                                                           Return(BinaryOp('>', Id('a'), Id('b'))),
                                                           Return(BinaryOp('>=', Id('a'), Id('b'))),
                                                           Return(BinaryOp('>.', Id('a'), Id('b'))),
                                                           Return(BinaryOp('>=.', Id('a'), Id('b'))),
                                                           Return(BinaryOp('==', Id('a'), Id('b'))),
                                                           Return(BinaryOp('!=', Id('a'), Id('b'))),
                                                           Return(BinaryOp('=/=', Id('a'), Id('b')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_70(self):
        """ Function Declaration - Other Statement """
        input = """
        Function: return
        Body:
            Return !!!!a;
        EndBody.
        """
        expect = Program([FuncDecl(Id('return'), [],
                                   ([], [Return(UnaryOp('!', UnaryOp('!', UnaryOp('!', UnaryOp('!', Id('a'))))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_71(self):
        """ Overall """
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
        expect = Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None),
                          VarDecl(Id('d'), [], IntLiteral(5)),
                          FuncDecl(Id('main'), [], ([VarDecl(Id('x'), [], None)], [])),
                          FuncDecl(Id('main2'), [], ([], [])), FuncDecl(Id('main3'), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_72(self):
        """ Overall """
        input = """
        Var: x,y;
        Function: overall
        Parameter: x,y
        Body:
            Return;
        EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None),
                          FuncDecl(Id("overall"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)],
                                   ([], [Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_73(self):
        """ Overall """
        input = """
        Var: x[1] = 2;
        Var: y;
        Function: overall
        Body:
            Var: x,y;
            Var: a[3] = 1;
        EndBody.
        """
        expect = Program([VarDecl(Id("x"), [1], IntLiteral(2)), VarDecl(Id("y"), [], None), FuncDecl(Id("overall"), [],
                                                                                                     ([VarDecl(Id("x"),
                                                                                                               [],
                                                                                                               None),
                                                                                                       VarDecl(Id("y"),
                                                                                                               [],
                                                                                                               None),
                                                                                                       VarDecl(Id("a"),
                                                                                                               [3],
                                                                                                               IntLiteral(
                                                                                                                   1))],
                                                                                                      []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_74(self):
        """ Overall """
        input = """
        Function: main
        Body:
            foo(!r, 5+6, 7&&6%4==1);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [], ([], [CallStmt(Id('foo'), [UnaryOp('!', Id('r')),
                                                                              BinaryOp('+', IntLiteral(5),
                                                                                       IntLiteral(6)), BinaryOp('==',
                                                                                                                BinaryOp(
                                                                                                                    '&&',
                                                                                                                    IntLiteral(
                                                                                                                        7),
                                                                                                                    BinaryOp(
                                                                                                                        '%',
                                                                                                                        IntLiteral(
                                                                                                                            6),
                                                                                                                        IntLiteral(
                                                                                                                            4))),
                                                                                                                IntLiteral(
                                                                                                                    1))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_75(self):
        """ Overall """
        input = """
        Function: main
        Body:
            b = -.-.--5;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [], (
        [], [Assign(Id('b'), UnaryOp('-.', UnaryOp('-.', UnaryOp('-', UnaryOp('-', IntLiteral(5))))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_76(self):
        """ Overall """
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
        expect = Program([FuncDecl(Id('a'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None)], (
        [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('a'), [], BooleanLiteral(True)),
         VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], StringLiteral('o'))],
        [Assign(Id('b'), UnaryOp('-', IntLiteral(8))),
         Assign(Id('b'), BinaryOp('%', IntLiteral(5), BinaryOp('*', Id('b'), IntLiteral(2)))),
         Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_77(self):
        """ Overall """
        input = """
        Var: x,y
        Function: overall
        Parameter: a,b
        Body:
            a = 1;
            Break;
            b = 2;
            Continue;
        EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None),
                          FuncDecl(Id("overall"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)], (
                          [], [Assign(Id("a"), IntLiteral(1)), Break(), Assign(Id("b"), IntLiteral(2)), Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_78(self):
        """ Overall """
        input = """
        Function: overall
        Body:
            Return;
            If a == 2 Then
                Continue;
                Return(a);
            EndIf.
            Return;
        EndBody.
        """
        expect = Program([FuncDecl(Id("overall"), [], ([], [Return(None), If([(BinaryOp("==", Id("a"), IntLiteral(2)),
                                                                               [], [Continue(), Return(Id("a"))])],
                                                                             ([], [])), Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_79(self):
        """ Overall """
        input = """
        Function: overall
        Body:
            For(i=1,i<10,1) Do
                Var: j;
                For(j=1,j<10,1) Do
                    a = a + 1;
                EndFor.
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('overall'), [], ([], [
            For(Id('i'), IntLiteral(1), BinaryOp('<', Id('i'), IntLiteral(10)), IntLiteral(1), (
            [VarDecl(Id('j'), [], None)], [
                For(Id('j'), IntLiteral(1), BinaryOp('<', Id('j'), IntLiteral(10)), IntLiteral(1),
                    ([], [Assign(Id('a'), BinaryOp('+', Id('a'), IntLiteral(1)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_80(self):
        """ Overall """
        input = """
        Function: overall
        Body:
            foo(2,3e-4,"rt",True);
        EndBody.
        """
        expect = Program([FuncDecl(Id('overall'), [], (
        [], [CallStmt(Id('foo'), [IntLiteral(2), FloatLiteral(0.0003), StringLiteral('rt'), BooleanLiteral(True)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_81(self):
        """ Overall """
        input = """
        Function: overall
        Body:
            (1+2)[1] = 1;
            foo(x);
            foo();
        EndBody.
        """
        expect = Program([FuncDecl(Id('overall'), [], ([], [
            Assign(ArrayCell(BinaryOp('+', IntLiteral(1), IntLiteral(2)), [IntLiteral(1)]), IntLiteral(1)),
            CallStmt(Id('foo'), [Id('x')]), CallStmt(Id('foo'), [])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_82(self):
        """ Overall """
        input = """
        **
        Function: overall
        Body:
            For(i=1,i<10,1) Do
                Var: j;
                For(j=1,j<10,1) Do
                    a = a + 1;
                EndFor.
            EndFor.
        EndBody.
        **
        """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_83(self):
        """ Overall """
        input = """
        Function: overall
        Body:
            t = ** Comment **  3\\2;
        EndBody.
        """
        expect = Program(
            [FuncDecl(Id('overall'), [], ([], [Assign(Id('t'), BinaryOp('\\', IntLiteral(3), IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_84(self):
        """ Overall """
        input = """
        Function: overall
        Body:
            Return (((100==102) == 200) == 202) == ((31 == 35) == 7);
        EndBody.
        """
        expect = Program([FuncDecl(Id('overall'), [], ([], [Return(BinaryOp('==', BinaryOp('==', BinaryOp('==',
                                                                                                          BinaryOp('==',
                                                                                                                   IntLiteral(
                                                                                                                       100),
                                                                                                                   IntLiteral(
                                                                                                                       102)),
                                                                                                          IntLiteral(
                                                                                                              200)),
                                                                                           IntLiteral(202)),
                                                                            BinaryOp('==',
                                                                                     BinaryOp('==', IntLiteral(31),
                                                                                              IntLiteral(35)),
                                                                                     IntLiteral(7))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_85(self):
        """ Overall """
        input = """
        Function: overall
        Body:
            If (a)[4] Then 
            ElseIf (a)[a][a][a] Then
            Else 
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('overall'), [], ([], [If([(ArrayCell(Id('a'), [IntLiteral(4)]), [], []), (
        ArrayCell(Id('a'), [Id('a'), Id('a'), Id('a')]), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_86(self):
        """ Overall """
        input = """
        Function: overall
        Body:
            Return 5*a > b+5*0&&67;
        EndBody.
        """
        expect = Program([FuncDecl(Id('overall'), [], ([], [Return(BinaryOp('>', BinaryOp('*', IntLiteral(5), Id('a')),
                                                                            BinaryOp('&&', BinaryOp('+', Id('b'),
                                                                                                    BinaryOp('*',
                                                                                                             IntLiteral(
                                                                                                                 5),
                                                                                                             IntLiteral(
                                                                                                                 0))),
                                                                                     IntLiteral(67))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_87(self):
        """ Overall """
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
        expect = Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], None),
                          VarDecl(Id('t'), [], IntLiteral(6)), VarDecl(Id('t'), [], IntLiteral(8)),
                          VarDecl(Id('t'), [], IntLiteral(9)), FuncDecl(Id('main'), [], ([], [])),
                          FuncDecl(Id('main'), [], ([], [])),
                          FuncDecl(Id('main'), [VarDecl(Id('x'), [], None)], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_88(self):
        """ Overall """
        input = """
        Function: overall
        Body:
        ** comment **
            Return;
        ** comment **
        **
        *
        *
        Comment
        **
        EndBody.
        """
        expect = Program([FuncDecl(Id("overall"), [], ([], [Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_89(self):
        """ Overall """
        input = """
        Function: main
        Body:
            a =foo(a[1+2][a*func()])[a < b];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [], ([], [Assign(Id('a'), ArrayCell(CallExpr(Id('foo'), [
            ArrayCell(Id('a'), [BinaryOp('+', IntLiteral(1), IntLiteral(2)),
                                BinaryOp('*', Id('a'), CallExpr(Id('func'), []))])]), [BinaryOp('<', Id('a'),
                                                                                                Id('b'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_90(self):
        """ Overall """
        input = """
        Function: overall
        Body:
            a = "Hello";
            b = 1;
            c = True;
            d = {1,2};
        EndBody.
        """
        expect = Program([FuncDecl(Id("overall"), [], ([], [Assign(Id("a"), StringLiteral("Hello")),
                                                            Assign(Id("b"), IntLiteral(1)),
                                                            Assign(Id("c"), BooleanLiteral(True)), Assign(Id("d"),
                                                                                                          ArrayLiteral([
                                                                                                                           IntLiteral(
                                                                                                                               1),
                                                                                                                           IntLiteral(
                                                                                                                               2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_91(self):
        """ Overall """
        input = """
        Function: overall
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
        expect = Program([FuncDecl(Id('overall'), [VarDecl(Id('x'), [], None)], ([], [If([(BinaryOp('||', BinaryOp('==',
                                                                                                                   Id('x'),
                                                                                                                   IntLiteral(
                                                                                                                       1)),
                                                                                                    BinaryOp('==',
                                                                                                             Id('x'),
                                                                                                             IntLiteral(
                                                                                                                 0))),
                                                                                           [],
                                                                                           [Return(IntLiteral(1))])], (
                                                                                         [], [Return(BinaryOp('+',
                                                                                                              CallExpr(
                                                                                                                  Id('fibo'),
                                                                                                                  [
                                                                                                                      BinaryOp(
                                                                                                                          '-',
                                                                                                                          Id('x'),
                                                                                                                          IntLiteral(
                                                                                                                              1))]),
                                                                                                              CallExpr(
                                                                                                                  Id('fibo'),
                                                                                                                  [
                                                                                                                      BinaryOp(
                                                                                                                          '-',
                                                                                                                          Id('x'),
                                                                                                                          IntLiteral(
                                                                                                                              2))])))]))])),
                          FuncDecl(Id('main'), [], ([], [CallStmt(Id('fibo'), [IntLiteral(3)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_92(self):
        """ Overall """
        input = """
        Function: main
        Body:
            r = !(r+5%4) * -7;
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [], ([], [Assign(Id('r'), BinaryOp('*', UnaryOp('!',
                                                                                               BinaryOp('+', Id('r'),
                                                                                                        BinaryOp('%',
                                                                                                                 IntLiteral(
                                                                                                                     5),
                                                                                                                 IntLiteral(
                                                                                                                     4)))),
                                                                                  UnaryOp('-', IntLiteral(7))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_93(self):
        """ Overall """
        input = """
        Function: overall
        Body:

        EndBody.
        """
        expect = Program([FuncDecl(Id("overall"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_94(self):
        """ Overall """
        input = """
        Function: overall
        Body:

        EndBody.
        Function: overall
        Body:

        EndBody.
        Function: overall
        Body:

        EndBody.
        """
        expect = Program([FuncDecl(Id("overall"), [], ([], [])), FuncDecl(Id("overall"), [], ([], [])),
                          FuncDecl(Id("overall"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_95(self):
        """ Overall """
        input = """
        Function: overall
        Body:
            x = "dfd\\rfsd";
        EndBody.
        """
        expect = Program([FuncDecl(Id('overall'), [], ([], [Assign(Id('x'), StringLiteral('dfd\\rfsd'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_96(self):
        """ Overall """
        input = """
        Function: main
        Body:
            foo(2,3e-4,"rt",True);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [], (
        [], [CallStmt(Id('foo'), [IntLiteral(2), FloatLiteral(0.0003), StringLiteral('rt'), BooleanLiteral(True)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_97(self):
        """ Overall """
        input = """
        Function: overall
        Body:
            Return({});
        EndBody.
        """
        expect = Program([FuncDecl(Id("overall"), [], ([], [Return(ArrayLiteral([]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_98(self):
        """ Overall """
        input = """
        Function: main
        Body:
            a = !a * !e % !!(-5);
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [], ([], [Assign(Id('a'), BinaryOp('%',
                                                                                  BinaryOp('*', UnaryOp('!', Id('a')),
                                                                                           UnaryOp('!', Id('e'))),
                                                                                  UnaryOp('!', UnaryOp('!', UnaryOp('-',
                                                                                                                    IntLiteral(
                                                                                                                        5))))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_99(self):
        """ Overall """
        input = """Var: a[0x1][0o7][56] = {"True", True}, literal, array;"""
        expect = Program([VarDecl(Id('a'), [1, 7, 56], ArrayLiteral([StringLiteral('True'), BooleanLiteral(True)])),
                          VarDecl(Id('literal'), [], None), VarDecl(Id('array'), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_100(self):
        """ Overall """
        input = """
        **
            THE END! THANKs FOR YOUR ATTENTION
        **
        """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))
