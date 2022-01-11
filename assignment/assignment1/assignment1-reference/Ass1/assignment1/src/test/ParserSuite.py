import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        """ Test global variable declaration """
        input = """Var: a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_2(self):
        """ Test global variable declaration """
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}}, a[3][5][1][10] = {{},{2,3,5},{"ab","Cd"},{True,False}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_3(self):
        """ Test global variable declaration """
        input = """Var: c, d = 6, e, f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_4(self):
        """ Test global variable declaration """
        input = """Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_5(self):
        """ Test global variable declaration """
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_6(self):
        """ Test global variable declaration """
        input = """Var: w = 5+2;"""
        expect = "Error on line 1 col 10: +"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_7(self):
        """ Test global variable declaration """
        input = """Var: a = b = c = 2;"""
        expect = "Error on line 1 col 9: b"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_8(self):
        """ Test global variable declaration """
        input = """Var: a[2.12];"""
        expect = "Error on line 1 col 7: 2.12"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_9(self):
        """ Test global variable declaration """
        input = """Var: b[12] = "Not an array";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_10(self):
        """ Test global variable declaration """
        input = """Varr: a = 2,b,c;"""
        expect = "Error on line 1 col 3: r"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_11(self):
        """ Test global variable declaration """
        input = """Var: a[4] = True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_12(self):
        """ Test global variable declaration """
        input = """Var: a = {  1, 2,     4,   7 };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_13(self):
        """ Test global variable declaration """
        input = """ """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_14(self):
        """ Test global variable declaration """
        input = """Var: a[] = {1,2,3};"""
        expect = "Error on line 1 col 7: ]"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_15(self):
        """ Test global variable declaration """
        input = """Var: arr[4] = True, b = {{1,2},{"Ab","CD"},{}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_16(self):
        """ Test global variable declaration """
        input = """** check comment ** Var: a = 2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_17(self):
        """ Test global variable declaration """
        input = """
        Var: a, b, c = "Check", d = {1,2,3};
        Var: e = {}, f[13] = True;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_18(self):
        """ Test global variable declaration """
        input = """Var: x = 3, a = x;"""
        expect = "Error on line 1 col 16: x"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_19(self):
        """ Test global variable declaration """
        input = """Var: a[13] = {{**Comment**"a", 2},True};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_20(self):
        """ Test global variable declaration """
        input = """
        Var: x[12] = {True,"a",0o13};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_21(self):
        """ Test global function declaration """
        input = """
        Var: x;
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact(n - 1);
                EndIf.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_22(self):
        """ Test global function declaration """
        input = """Function: foo Parameter: a[5], b Body: Var: i = 0; While (i < 5) Do a[i] = b + 1.0; i = i + 1; EndWhile. EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_23(self):
        """ Test global function declaration """
        input = """
        Function: increase
        Parameter: x
        Body:
            x = x + 1;
        EndBody.
        Function: decrease
        Parameter: y
        Body:
            y = y - 1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_24(self):
        """ Test global function declaration """
        input = """
        Function: test
        Parameter: y
        Body:
            a = 2;
            Return a < b;
            foo(2,3);
            a[arr[2] + arr[4]] = 15;
            bool = a && c || d && e;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_25(self):
        """ Test global function declaration """
        input = """
        Function: array
        Parameter: z,d,e
        Body:
            (z + d + e)[12] = {1,2,3,4};
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_26(self):
        """ Test global function declaration """
        input = """
        Function array
        Parameter z
        Body
            Return 2;
        EndBody.
        """
        expect = "Error on line 2 col 17: array"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_27(self):
        """ Test global function declaration """
        input = """
        Function: arr
        Parameter: z
        Body:
            b = 12;
            a = 0O12;
            foo(a);
            return 1;
        EndBody.
        """
        expect = "Error on line 8 col 19: 1"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_28(self):
        """ Test global function declaration """
        input = """
        Function: a
        Body:
            Return {   1 ,   12,{   },"h"  };
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_29(self):
        """ Test global function declaration """
        input = """
        Var: a = {2,{},"a"};
        Function:   for
        Parameter: x,t
        Body:
            x = t + {1,{},"c"};
            For (x = 1, x > 2, x + 1) Do
                If (x == 1) Then
                    Continue;
                EndIf.
            EndFor.
            If (x > 3) Then
                Break;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_30(self):
        """ Test global function declaration """
        input = """
        Function: test_array
        Body:
            a[x[{{},"abc",2}]] = 2;
            b[1.2] = {1,{12,{}}};
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_31(self):
        """ Test assignment statement """
        input = """
        Var: a, b
        Body:
            a + b = {1,2,3} + {4,5,6};
            Return c;
        EndBody. 
        """
        expect = "Error on line 3 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_32(self):
        """ Test assignment statement """
        input = """
        Var: assignment;
        Function: foo
        Parameter: a,b
        Body:
            a[{1,2,3}][True]["c"] = a && b || a >=. 2.12;
            Return b =/= 12E-13;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_33(self):
        """ Test assignment statement """
        input = """
        Var: x,t;
        x = foo(1);
        Return a;
        """
        expect = "Error on line 3 col 8: x"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_34(self):
        """ Test assignment statement """
        input = """
        Function: assignment
        Parameter: x, t[15]
        Body:
            Var: b;
            x = b;
            t[incr(12) * 3.12] = 0o12;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_35(self):
        """ Test assignment statement """
        input = """
        Function: test
        Parameter: num_of_student
        Body:
            num_of_student = foo({1,2,{},{"a","b"}});
            num_of_student = num_of_student + num_of_student;
            Return num_of_student;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_36(self):
        """ Test if statement """
        input = """
        Var: x = True;
        Function: normal_if_statement
        Body:
            If (x == False) Then
                x = x + 1;
                x[foo(x)] = 0xAF;
                Return x;
            EndIf.
            Return;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_37(self):
        """ Test if statement """
        input = """
        Var: x = True;
        Function: elseif_else_if_statement
        Body:
            If (x == False) Then
                x = x + 1;
                x[foo(x)] = 0xAF;
                Return x;
            ElseIf (x == 12) Then
                x = x * foo(12);
                Return y;
            Else
                x = 1 + 2 + 3 + 4  + 5;
            EndIf.
            Return;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_38(self):
        """ Test if statement """
        input = """
        Function: loop_if_statement
        Body:
            If (x == False) Then
                x = x + 1;
                If (x > 1) Then
                    x = x * x;
                    If (x > 100) Then
                        x = x * x * x;
                        If (x < 1000) Then
                            x =y;
                        EndIf.
                    EndIf.
                EndIf.
            EndIf.
            Return;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_39(self):
        """ Test if statement """
        input = """
        Function: blank_if_stmt
        Body:
            If (x == True) Then

            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_40(self):
        """ Test if statement """
        input = """
        Function: no_then_if_stmt
        Body:
            If (a == 10)
                b = b + 9;
            EndIf.
        EndBody.
        """
        expect = "Error on line 5 col 16: b"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_41(self):
        """ Test for statement """
        input = """
        Function: test_for_stmt
        Parameter: x, y
        Body:
            For (x = foo(1 + 2), x >. -2.12e-13, x + 1) Do
                y = {2,{},"a"} + a["bc"];
                Return y;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_42(self):
        """ Test for statement """
        input = """
        Function: test_for_stmt
        Body:
            Var: i = 0, j = 10, foo;
            For (i = 0, i < j, i + 1)
                foo(i);
                If (i == j - 1) Then
                    foo(0);
                EndIf.
                If (i == -1) Then
                    Break;
                EndIf.
            EndFor.
            Return for(i,j,foo);
        EndBody.
        """
        expect = "Error on line 6 col 16: foo"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_43(self):
        """ Test for statement """
        input = """
        Function: nested_for_stmt
        Parameter: i, j, foo
        Body:
            Var: y = 1;
            For (x = i, x != j, x * x) Do
                For (y = 0, y <. True, !False) Do
                    For (z = y, a[True], z[False]) Do
                        ** Nested For loop **
                            i = i + 1;
                            Return 12;
                        ** The End **
                    EndFor.
                EndFor.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_44(self):
        """ Test for statement """
        input = """
        ** C++ style **
        Function: c_for
        Body:
            for (int i = 0; i < 10; i++) {
                i = i + 1;
                if (i = 12) break;
            }
            return i;
        EndBody.
        """
        expect = "Error on line 5 col 21: i"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_45(self):
        """ Test for statement """
        input = """
        Function: for
        Body:
            For (a[12] = 3, a > 12, a \ 12) Do
                Return 12;
            EndFor.
        EndBody.
        """
        expect = "Error on line 4 col 18: ["
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_46(self):
        """ Test while statement """
        input = """
        Var: a[12] = {1,{"a",True,{1,2}},False};
        Function: while_stmt
        Parameter: a
        Body:
            While a < {1,{},True,{"a",** null **True,"a"}} Do
                a = b \. 003e150;
                If (a == 12) Then
                    Break;
                ElseIf (a *. 1.) Then
                    a[while_stmt(13)] = while_stmt(13);
                ElseIf (a != False) Then
                    a[12] = True;
                ElseIf (a + b) Then
                    a[b] = a[b()];
                Else
                    Break;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_47(self):
        """ Test while statement """
        input = """
        While (a < 1) Do
            Return a;
        EndWhile.
        """
        expect = "Error on line 2 col 8: While"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_48(self):
        """ Test while statement """
        input = """
        Function: test_while
        Body:
            While (x <. 12.) Do
                For (x = 1., x >. 0., x + 1e10) Do
                    x = (x + 1) * 2 - a[foo(15)];
                    Return x;
                EndFor.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_49(self):
        """ Test while statement """
        input = """
        Function: foo
        Parameter: x,y
        Body:
            While True Do
                a[foo(foo(foo({1,2,{}, 13})))] = True;
                If (a[foo(foo(12))] + foo(1)) Then
                    Break;
                EndIf.
                Continue;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_50(self):
        """ Test while statement """
        input = """
        Var: foo;
        Function: nested_while
        Parameter: a
        Body:
        While (a[foo] == a[(a[12] + foo(12)) * 13]) Do
        While (foo(12) + 1) Do
        While (a[12] \. foo()) Do
        While (False == True) Do
        Return a;
        Continue;
        EndWhile.
        EndWhile.
        EndWhile.
        EndBody.
        """
        expect = "Error on line 15 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_51(self):
        """ Test do-while statement """
        input = """
        Do
            a[12] = foo();
            Break;
            If (b[a] == 1) Then
                Return 1;
            EndIf.
        While a[foo(x(12))] >= 3
        EndDo.
        """
        expect = "Error on line 2 col 8: Do"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_52(self):
        """ Test do-while statement """
        input = """
        Function: main
        Body:
            Var : a;
            Do 
                x = y + 1;
            While True Do
                a = a + 2;
                Return x;
                Break;
            EndWhile. 
            EndDo.
        EndBody.
        """
        expect = "Error on line 12 col 12: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_53(self):
        """ Test do-while statement """
        input = """
        Function: nested_dowhile_stmt
        Parameter: a
        Body:
            Do
                Do
                    Do 
                        Do
                        
                        While False
                        EndDo.
                    While (False)
                    EndDo.
                While (True)
                EndDo.
            While (a[((foo(1) * 1) + (b \. 0e12))] =/= 31E12)
            EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_54(self):
        """ Test do-while statement """
        input = """
        Function: while_dowhile_stmt
        Body:
            Do
                While x =/= False Do
                    x = ((((x + y) - 2) * 3) \. 1.2e3);
                    Do
                        Return a;
                    While (False)
                    EndDo.
                EndWhile.
            While (a == True)
            EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_55(self):
        """ Test do-while statement """
        input = """
        Function: foo
        Body:
            Do
                a = a + 1;
            While (x == True)
            Return 2;
        EndBody.
        """
        expect = "Error on line 7 col 12: Return"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_56(self):
        """ Test break statement """
        input = """Break;"""
        expect = "Error on line 1 col 0: Break"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_57(self):
        """ Test break statement """
        input = """
        Function: foo
        Parameter: x
        Body:
            break;
        EndBody.
        """
        expect = "Error on line 5 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_58(self):
        """ Test break statement """
        input = """
        Function: multybreak
        Parameter: x
        Body:
            Break; Break; Break; Break; Break;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_59(self):
        """ Test continue statement """
        input = """
        Var: i = 0;
        For (x = i, i < 10, i + 1) Do
            if (i == 5) Then
                x = 0;
                Continue;
            EndIf.
        EndFor.
        """
        expect = "Error on line 3 col 8: For"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_60(self):
        """ Test continue statement """
        input = """
        Function: foo
        Parameter: x
        Body:
            For (x = i, i < 10, i + 1) Do
                If (i == 5) Then
                    x = 0;
                    Continue;
                EndIf.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_61(self):
        """ Test continue statement """
        input = """
        Function: continue
        Body:
            Continue;
            Break;
            Continue;
            ** continue again **
            Continue;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_62(self):
        """ Test return statement """
        input = """
        Function: main
        Parameter: char, argv
        Body:
            Return 1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_63(self):
        """ Test return statement """
        input = """
        Function: main
        Parameter: char, argv
        Body:
            Var: x, y;
            Break;
            Return (arr[foo(foo(foo))] == True) + False * True \. 2.1e13;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_64(self):
        """ Test return statement """
        input = """
        Var: b, a;
        Function: return
        Body:
            Continue;
            Return  Function: return_stmt
                    Parameter: x
                    Body:
                        Return 2;
                    EndBody.
        EndBody.
        """
        expect = "Error on line 6 col 20: Function"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_65(self):
        """ Test call statement """
        input = """
        Var: x, y, foo;
        foo(x);
        """
        expect = "Error on line 3 col 8: foo"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_66(self):
        """ Test call statement """
        input = """
        Function: nested_functioncall
        Body:
            foo(foo() + foo({1,2,3}));
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_67(self):
        """ Test call statement """
        input = """
        Function: nested_functioncall
        Body:
            foo(foo() + foo({1,2,3}) * foo(foo(foo(foo() + 2))));
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_68(self):
        """ Test call statement """
        input = """
        Function: nested_functioncall
        Body:
            foo(foo(foo(1,2,{1,2})) + foo({1,2,3}) * foo(foo(foo(foo() + 2)) + foo(foo(foo("a") * (foo() + 0xAFE)))));
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_69(self):
        """ Test call statement """
        input = """
        Function: functioncall_in_array
        Body:
            a[foo(foo(foo(foo())))] = foo((a * {1,2,3}) + foo(a[13]));
            Return a[foo(a[x * 12])];
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_70(self):
        """ Test call statement """
        input = """
        Function: functioncall_in_array
        Body:
            Return a[Foo(a[x * 12])];
        EndBody.
        """
        expect = "F"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_71(self):
        """ Test variable declaration statement """
        input = """
        Function: var_test
        Body:
            Var: foo = {1,{"a", 2, True}, False}, a[12];
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_72(self):
        """ Test variable declaration statement """
        input = """
        Function: var_test
        Body:
            Var: x[foo(12)] = {1,2,"a",True};
            Return x;
        EndBody.
        """
        expect = "Error on line 4 col 19: foo"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_73(self):
        """ Test multiple function """
        input = """
        Function: nhan_test
        Parameter: x,y
        Body:
            a[someFunc(22) + 33] = a[22*14 + anotherFunc() + a[2]] * 5;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_74(self):
        """ Test multiple function """
        input = """
        Function: foo_a
        Body:
        EndBody.
        Function: foo_b
        Body:
        EndBody.
        Function: foo_c
        Body:
        EndBody.
        Function: foo_d
        Body:
        EndBody.
        Function: foo_e
        Body:
        EndBody.
        Function: foo_f
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_75(self):
        """ Test multiple function """
        input = """
        Function: sum
        Parameter: x, y
        Body:
            Return x + y;
        EndBody.
        Function: sub
        Parameter: x, y
        Body:
            Return x - y;
        EndBody.
        Function: mul
        Parameter: x, y
        Body:
            Return x * y;
        EndBody.
        Function: div
        Parameter: x, y
        Body:
            Return x \. y;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_76(self):
        """ Test multiple function """
        input = """
        Var: x = 0, y = 1;
        Function: foo
        Parameter: x, y
        Body:
            Return x + y;
        EndBody.
        Return x - y;
        """
        expect = "Error on line 8 col 8: Return"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_77(self):
        """ Test multiple function """
        input = """
        Function: my_test
        Parameter: x
        Body:
            If (x == 0) || !y || a[foo({1,{},"////"})] Then
                Return 1;
            EndIf.

            Return fibo(x-1) + fibo(x-2);
        EndBody.

        Function: main
        Body:
            Var: a[10], i; 
            For(i = 0, i < 10, 1) 
            Do
                a[i] = fibo(i);
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_78(self):
        """ Test multiple function """
        input = """
        Function: func_a
        Body:
            Function: func_b
                Body:
                Function: func_c
                Body:
                    Function: func_d
                    Body:
                        Function: func_e
                        Body:
                            Functino: func_f
                            Body:

                            EndBody.
                        EndBody.
                    EndBody.
                EndBody.
            EndBody.
        EndBody.
        """
        expect = "Error on line 4 col 12: Function"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_79(self):
        """ Test multiple function """
        input = """
        ** Functional programming **
        Function: functional_prog
        Body:
            Return (Function: foo
                    Parameter: x, t
                    Body:
                        Return x * t;
                    EndBody.
                    );
        EndBody.
        """
        expect = "Error on line 5 col 20: Function"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_80(self):
        """ Find the largest element using recursion """
        input = """
        Function: max
        Parameter: a, b
        Body:
            If (a >= b) Then
                Return a;
            EndIf.
            Return b;
        EndBody.

        Function: findMax
        Parameter: arr_ptr, length
        Body:
            If (length == 1) Then
                Return arr_ptr[0];
            EndIf.
            Return max(arr[length - 1], findMax(arr, length - 1));
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_81(self):
        """ Convert from Decimal to Binary """
        input = """
        Function: decimalToBinary
        Parameter: decimal_number
        Body:
            If (decimal_number == 0) Then
                Return 0;
            Else
                Return decimal_number % 2 + 10 * decimalToBinary(decimal_number \ 2);
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_82(self):
        """ Other """
        input = """
        Var: a = 10;
        Function: main
        Parameter: arr[a]
        Body:
            Var: arr;
            Return arr;
        EndBody.
        """
        expect = "Error on line 4 col 23: a"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_83(self):
        """ Other """
        input = """
        Function: main
        Parameter: a,b
        Body:
            Var: b;
        Endbody.
        """
        expect = "E"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_84(self):
        """ Other """
        input = """
        ** No parameter **
        Function: foo
        Parameter:
        Body:
            Return 1;
        EndBody.
        """
        expect = "Error on line 5 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_85(self):
        """ Other """
        input = """
        Var: a[1][2][3][4][5][6][7][8][9][10][11][12][13][14][15][16][17][18][19][20][21][22][23][24][25][26][27][28][29][30];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_86(self):
        """ Other """
        input = """
         ** This array declaraion does not accepted **
        Var: a["13"] = {1,2,  3,{} ,""   };
        Function: for
        Body:
            ** This is accepted **
            a["13"] = {1, 2, 3, {},    "12"};
        EndBody.
        """
        expect = "Error on line 3 col 15: 13"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_87(self):
        """ Other """
        input = """
        Function: loop_functioncall
        Body:
            Return loop_functioncall(loop_functioncall(loop_functioncall(loop_functioncall(loop_functioncall(loop_functioncall(1))))));
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_88(self):
        """ Other """
        input = """
        ** No declaration **

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_89(self):
        """ Other """
        input = """
        ** Error variable declaration **
        Var: 1student, NumOfStudent, _class;
        """
        expect = "Error on line 3 col 13: 1"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_90(self):
        """ Other """
        input = """
        Function: main
        Body:
            foo;
        EndBody.
        """
        expect = "Error on line 4 col 15: ;"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_91(self):
        """ Other """
        input = """
        Function: main
        Body:
            array[foo(2,            3 
            ,4,5,6                  , foo(foo(x * foo(a + b)) + {1,2,3})
            )] = {1,True,{1,"a",{}}};
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_92(self):
        """ Other """
        input = """
        Var: a, b, c = 0;
        ** No Function **
        a = 2;
        While (a < 1) Do
            a = a + 1;
        EndWhile.
        b = 2;
        Return c;
        """
        expect = "Error on line 4 col 8: a"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_93(self):
        """ Other """
        input = """
        ** Error String **
        Function: main
        Body:
            Return "a b\\t \\n c d\\f e";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_94(self):
        """ Other """
        input = """
        Function: comment_return
        Body:
            Return **   ABC
                        * DEF
                        *  GHI
                        * JKL
                        * MNO
                        PQRSTUV
                        QWXYZ
                    **;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_95(self):
        """ Other """
        input = """
        Var a
        Function foo
        Body
            Return 1 + 1;
        EndBody
        """
        expect = "Error on line 2 col 12: a"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_96(self):
        """ Other """
        input = """
        Var: a, b, c;
        Function: foo
        Parameter: x, y
        Body:
            a[1 + a - c * d == e + h ] = ((foo(a + b \ a) - 0xAED) - a[13]);
            b[foo(1 - c =/= e) - ((h || e) * b && c)] = b[a[foo(1 + 2 - a && d) - b =/= e + ! h - (-a + c - 13 + (-13))]];
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_97(self):
        """ Other """
        input = """
        Var: a;
        Function: foo
        Body:
            a = c;
            c = d;
            e[a != b] = e;
            Break;
            For (a = b; c < d; i++) {
                Return a;
            }
            Return;
        EndBody.
        """
        expect = "Error on line 9 col 22: ;"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_98(self):
        """ Other """
        input = """
        ** Missing Body **
        Var: x = {1, {},      "a", {"b", ** Comment ** "d"}};
        Function: foo
            a = a + 1;
            Break;
            Return a;
        EndBody.
        """
        expect = "Error on line 5 col 12: a"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_99(self):
        """ Other """
        input = """
        Function: operator
        Body:
            a = !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!False;
            b = (((((((((((((((((((((((((((((((e)))))))))))))))))))))))))))))));
            Return a + b;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_100(self):
        """ Other """
        input = """
        Var a;
        Var b;
        Function a
            a = a + 1;
            Return a;
        EndFunction
        Return 1;
        """
        expect = "Error on line 2 col 12: a"
        self.assertTrue(TestParser.checkParser(input,expect,300))