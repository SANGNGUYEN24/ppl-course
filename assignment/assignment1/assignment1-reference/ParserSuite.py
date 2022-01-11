# Lu Anh Khoa - 1852112

import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_program(self):
        input = """
        Var: a,b,c,d;

        Function: main
        Body:
            Var: q;
            If q Then 
                a = b;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_var(self):
        input = """Var: a = {1,2,3}, b = 2, c,d ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_var_2(self):
        input = """Var: a[3][4][7][8][9] = {1,2,3}, b = 2, c,d ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_var_3(self):
        input = """Var: a[0x3] = {1,2,3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_var_4(self):
        input = """Var: a[0o7] = {{1},{2,2},3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_var_5(self):
        input = """Var: a[3.] = {1,2,3};"""
        expect = "Error on line 1 col 7: 3."
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_var_6(self):
        input = """Var: a[True] = {1,2,3};"""
        expect = "Error on line 1 col 7: True"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_var_7(self):
        input = """Var: a[] = {1,2,3};"""
        expect = "Error on line 1 col 7: ]"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_var_8(self):
        input = """Var: a[**3**] = {1,2,3};"""
        expect = "Error on line 1 col 12: ]"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_var_9(self):
        input = """Var: a[123] = ;"""
        expect = "Error on line 1 col 14: ;"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_var_10(self):
        input = """Var: a = t;"""
        expect = "Error on line 1 col 9: t"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_var_11(self):
        input = """Var: a = 2+9;"""
        expect = "Error on line 1 col 10: +"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_var_12(self):
        input = """Var: f = 4 = a;"""
        expect = "Error on line 1 col 11: ="
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_var_13(self):
        input = """Var: a,c,d; Var b,d,f"""
        expect = "Error on line 1 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_var_14(self):
        input = """Var: a,r,3,b;"""
        expect = "Error on line 1 col 9: 3"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_var_15(self):
        input = """Var: a, ;"""
        expect = "Error on line 1 col 8: ;"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_expr(self):
        input = \
        """
        Function: main
        Body:
            a = 2;
            Return a < b;
            a();
            a(2,3,4);
            a[r(3) + t(7,2)] = {5,6};
            a = a + -b * c \\ e \\. d +. f;
            b = b && c || a && !!b ;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_expr_2(self):
        input = \
        """
        Function: main
        Body:
            (a+b)[4] = 5;
        EndBody.
        """
        expect = "Error on line 4 col 12: ("
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_expr_3(self):
        input = \
        r"""
        Function: main
        Body:
            Return ({3,4,5} + foo(3)) ;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_expr_4(self):
        input = \
        r"""
        Function: main
        Body:
            Return (a,1,3) ;
        EndBody.
        """
        expect = "Error on line 4 col 21: ,"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_expr_5(self):
        input = \
        r"""
        Function: main
        Body:
            Return a<b<c>e;
        EndBody.
        """
        expect = "Error on line 4 col 22: <"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_expr_6(self):
        input = \
        r"""
        Function: main
        Body:
            a[a[d]] = 45;
            a[a[{3,4,5}]] = 45;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_expr_7(self):
        input = \
        r"""
        Function: main
        Body:
            a+b = c;
        EndBody.
        """
        expect = "Error on line 4 col 13: +"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_expr_8(self):
        input = \
        r"""
        Function: main
        Body:
            45 = c;
        EndBody.
        """
        expect = "Error on line 4 col 12: 45"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_expr_9(self):
        input = \
        r"""
        Function: main
        Body:
            a = foo(2, 3, foo(2, 3, a[a[foo(2,3,4) + f || 9]]));
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_expr_10(self):
        input = \
        r"""
        Function: main
        Body:
            foo[foo[2]][foo[2]] = foo(3,5,6);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_expr_11(self):
        input = \
        r"""
        Function: main
        Body:
            a = --.-.-.-.-.----.---- 4.5;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_expr_12(self):
        input = \
        r"""
        Function: main
        Body:
            a = foo({2,3});
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_expr_13(self):
        input = \
        r"""
        Function: main
        Body:
            a = () ;
        EndBody.
        """
        expect = "Error on line 4 col 17: )"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_function_decl(self):
        input = \
        r"""
        Function: main
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))


    def test_function_decl_2(self):
        input = \
        r"""
        Function: main
        Parameter: a,b,c
        Body:
            Var: b;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_function_decl_3(self):
        input = \
        r"""
        Function: main
        Parameter: a,b,
        Body:
            Var: b;
        EndBody.
        """
        expect = "Error on line 4 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_function_decl_4(self):
        input = \
        r"""
        Function: main
        Parameter: a,4
        Body:
            Var: b;
        EndBody.
        """
        expect = "Error on line 3 col 21: 4"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_function_decl_5(self):
        input = \
        r"""
        Function: main
        Parameter: a[2][3][4][5]
        Body:
            Var: b;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_function_decl_6(self):
        input = \
        r"""
        Function: main
        Parameter: 
        Body:
            Var: b;
        EndBody.
        """
        expect = "Error on line 4 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_function_decl_7(self):
        input = \
        r"""
        Function: main
        Parameter: a=4,b=5
        Body:
            Var: b;
        EndBody.
        """
        expect = "Error on line 3 col 20: ="
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_function_decl_8(self):
        """ wrong keyword """

        input = \
        r"""
        Function: main
        Parameter: a,b
        Body:
            Var: b;
        Endbody.
        """
        expect = "E" # what happened ?
        self.assertTrue(TestParser.checkParser(input,expect,239))
        

    def test_function_decl_9(self):
        input = \
        r"""
        Function: main
        Parameter: a[n]
        Body:
            Var: b;
        EndBody.
        """
        expect = "Error on line 3 col 21: n"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_function_decl_10(self):
        input = \
        r"""
        Function: main
        Parameter: a
        Body:
            Var: b;
        EndBody
        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_function_decl_11(self):
        input = \
        r"""
        Function: main
        Parameter: a
        Body:
            Var: b;
        EndBody

        Function: main2
        Parameter: a
        Body:
            Var: b;
        EndBody.
        """
        expect = "Error on line 8 col 8: Function"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_stmt_if(self):
        """ If ... Then ... EndIf. """
        input = \
        r"""
        Function: main
        Body:
            If a==3 Then
                a = 5;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_stmt_if_2(self):
        """ If ... Then ... Else ... EndIf. """
        input = \
        r"""
        Function: main
        Body:
            If a==3 Then
                a = 5;
            Else
                a = 6;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_stmt_if_3(self):
        """ If ... Then ... 
        ElseIf ... Then ...
        EndIf. """
        input = \
        r"""
        Function: main
        Body:
            If a == 3 Then
                a = 5;
            ElseIf a == b Then
                a = 6;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_stmt_if_4(self):
        """ If ... Then ... 
        ElseIf ... Then ...
        ElseIf ... Then ...
        EndIf. """
        input = \
        r"""
        Function: main
        Body:
            If a == 3 Then
                a = 5;
            ElseIf a == b Then
                a = 6;
            ElseIf a == c Then
                a = 7;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_stmt_if_5(self):
        """ If ... Then ... 
        ElseIf ... Then ...
        ElseIf ... Then ... 
        Else ... EndIf. """

        input = \
        r"""
        Function: main
        Body:
            If a == 3 Then
                a = 5;
            ElseIf a == b Then
                a = 6;
            ElseIf a == c Then
                a = 7;
            Else
                a = 8;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_stmt_if_6(self):
        """No EndIf"""

        input = \
        r"""
        Function: main
        Body:
            If a == 3 Then
                a = 5;
            ElseIf a == b Then
                a = 6;
            ElseIf a == c Then
                a = 7;
            Else
                a = 8;
            
        EndBody.
        """
        expect = "Error on line 13 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_stmt_if_7(self):
        """Nested If(s)"""

        input = \
        r"""
        Function: main
        Body:
            If a == b Then
                If b == c Then
                    If d == e Then
                    EndIf.
                EndIf.
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_stmt_if_8(self):
        """Nested If(s), with Else"""

        input = \
        r"""
        Function: main
        Body:
            If a == b Then
                If b == c Then
                    If d == e Then
                    Else 
                        If e == d Then
                        EndIf.
                    EndIf.
                Else 
                    If c > b Then
                    EndIf.
                EndIf.
            Else 
                If b && a Then
                EndIf.
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_for(self):
        input = \
        r"""
        Function: main
        Body:
            Var: i;
            For(i = 0, i < 10, i+1) Do
                a = a *. 5;
                If (a == 10) Then
                    b = b + 9;
                EndIf.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_for_2(self):
        """expecting expr, got stmt: i=i+1"""
        input = \
        r"""
        Function: main
        Body:
            Var: i;
            For(i = 0, i < 10, i = i+1) Do
                a = a *. 5;
                If (a == 10) Then
                    b = b + 9;
                EndIf.
            EndFor.
        EndBody.
        """
        expect = "Error on line 5 col 33: ="
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_for_3(self):
        """expect scalar var, got composite var"""
        input = \
        r"""
        Function: main
        Body:
            Var: i;
            For(a[i] = 0, i < 10, i = i+1) Do
            EndFor.
        EndBody.
        """
        expect = "Error on line 5 col 17: ["
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_for_4(self):
        """expect scalar var, got composite var, but with intlit"""
        input = \
        r"""
        Function: main
        Body:
            Var: i;
            For(a[4] = 0, i < 10, i = i+1) Do
            EndFor.
        EndBody.
        """
        expect = "Error on line 5 col 17: ["
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_for_5(self):
        """nested for"""
        input = \
        r"""
        Function: main
        Parameter: a[10][10]
        Body:
            Var: i, j, s;
            s = 0;
            For(i=0, i<10, 1) Do
                For(j=0, j<10, 1) Do
                    s = s + a[i][j];
                EndFor.
            EndFor. 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_for_6(self):
        """empty body"""
        input = \
        r"""
        Function: main
        Parameter: a[10][10]
        Body:
            Var: i, j, s;
            s = 0;
            For(i=0, i<10, 1) Do
            EndFor. 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_whiledo(self):    
        input = \
        r"""
        Function: main
        Body:
            Var: a;
            While True Do
                a = a + 1;
                Continue;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_dowhile(self):
        input = \
        r"""
        Function: main
        Body:
            Var : a;
            Do 
                a = a + 1;
                Break;
            While True EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_dowhile_whiledo_mixed(self):
        input = \
        r"""
        Function: main
        Body:
            Var : a;
            Do 
                a = a + 1;
                Break;
            While True Do
                a = a + 2;
                Break;
            EndWhile. 
            EndDo.
        EndBody.
        """
        expect = "Error on line 12 col 12: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_dowhile_whiledo_mixed_2(self):
        input = \
        r"""
        Function: main
        Body:
            Var: a;
            While True Do
                a = a + 2;
                Break;
            While True EndDo.
            EndWhile. 
            
        EndBody.
        """
        expect = "Error on line 8 col 12: While"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_call(self):
        input = \
        r"""
        Function: main
        Body:
            fact();
            fact(4,5,6,7,8);
            fact(a,b,c,d,e,f);
            fact("True", True, False, {1,2}, b, 56);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_call_2(self):
        input = \
        r"""
        Function: main
        Body:
            fact(a=5);
        EndBody.
        """
        expect = "Error on line 4 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_call_3(self):
        input = \
        r"""
        Function: main
        Body:
            fact(a, b, 3* 4 \. abc, True, False);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_call_4(self):
        input = \
        r"""
        Function: main
        Body:
            fact(2)[78];
        EndBody.
        """
        expect = "Error on line 4 col 19: ["
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_call_5(self):
        input = \
        r"""
        Function: main
        Body:
            fact(fact(fact(2, fact(2))));
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_call_6(self):
        input = \
        r"""
        Function: main
        Body:
            fact(5) + fact(5);
        EndBody.
        """
        expect = "Error on line 4 col 20: +"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_call_7(self):
        input = \
        r"""
        Function: main
        Body:
            print("Function: main\nBody:\nEndBody.");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_return(self):
        input = \
        r"""
        Function: main
        Body:
            Return;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_return_2(self):
        input = \
        r"""
        Function: main
        Body:
            Return 123;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_return_3(self):
        input = \
        r"""
        Function: main
        Body:
            Return fact(2,3,4) + True + "45678";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_return_4(self):
        input = \
        r"""
        Function: main
        Body:
        EndBody.

        Return;
        """
        expect = "Error on line 6 col 8: Return"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_return_5(self):
        input = \
        r"""
        Function: main
        Body:
            Return Var: a;
        EndBody.
        """
        expect = "Error on line 4 col 19: Var"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_call_without_parentheses(self):
        input = \
        r"""
        Function: main
        Body:
            main ;
        EndBody.
        """
        expect = "Error on line 4 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    
    def test_call_with_newlines(self):
        input = \
        r"""
        Function: main
        Body:
            foo(2,            3 
            ,4,5,6
            );
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_return_6(self):
        input = \
        r"""
        Function: main
        Body:
            Return "ab
            cde";
        EndBody.
        """
        expect = "ab\n" # what happened ... ?
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_return_7(self):
        input = \
        r"""
        Function: main
        Body:
            Return **GIT GUD**;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_empty_file(self):
        input = \
        r"""
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_var_decl_after_func_decl(self):
        input = \
        r"""
        Function: main
        Body:
        EndBody.
        Var: x;
        """
        expect = "Error on line 5 col 8: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_multiple_functions(self):
        input = \
        r"""
        Function: abc
        Body:
        EndBody.

        Function: zyx
        Body:
        EndBody.
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    
    def test_do_nowhile(self):
        input = \
        r"""
        Function: main
        Body:
            Do
                Var: x;
            EndDo.
        EndBody.
        
        """
        expect = "Error on line 6 col 12: EndDo"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_var_neg_value(self):
        input = \
        r"""
        Function: main
        Body:
            Var: x = -7;
        EndBody.
        
        """
        expect = "Error on line 4 col 21: -"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_var_initvalue_is_var(self):
        input = \
        r"""
        Function: main
        Parameter: x
        Body:
            Var: y = x;
        EndBody.
        
        """
        expect = "Error on line 5 col 21: x"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_mixed_1(self):
        input = \
        r"""
        Var: n, a[10];
        Function: main
        Body:
            Var: i;
            n = -1;
            For(i = 0, i < 10, 1) Do
                If (n+9 < 4) Then
                    ** sud du sumthin'* **
                    a[1] = a[1] + 3;
                ElseIf a[0] == 3 Then
                    Var: j = 0;
                    j = j - 6;

                Else
                    someThing();
                EndIf.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_mixed_2(self):
        input = \
        r"""
        Function: Fibo
        Parameter: x
        Body:
            If (x == 0) || (x == 1) || (x == 2) Then
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
        expect = "F" # to pay respect ? (no lexer match with Fibo)
        self.assertTrue(TestParser.checkParser(input, expect, 284))
    
    def test_mixed_3(self):
        input = \
        r"""
        Function: fibo
        Parameter: x
        Body:
            If (x == 0) || (x == 1) || (x == 2) Then
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
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_mixed_4(self):
        input = \
        r"""
        Function: Function
        Body:
            Var :x = 10 ;
            While (x > 0) Do
                x = x - 1.;
            EndWhile.
        EndBody.
        """
        expect = "Error on line 2 col 18: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_mixed_5(self):
        input = \
        r"""
        Function: main
        Body:
            Var :x = 10 ;
            While (x > 0) Do
                x = x - 1.;
                Break;
                Break;
                Break;
                Break;
                Continue;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_mixed_nested_function(self):
        input = \
        r"""
        Function: main
        Body:
            Function: submain
            Body:
            EndBody.

        EndBody.
        """
        expect = "Error on line 4 col 12: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_mixed_function_nobody(self):
        input = \
        r"""
        Var: x,y;
        Function: main
        EndBody.
        """
        expect = "Error on line 4 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_for_literal_eveywhere(self):
        input = \
        r"""
        Var: x,y;
        Function: main
        Body:
            For(4=4,True,0) Do
            EndFor.
        EndBody.
        """
        expect = "Error on line 5 col 16: 4"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_while_not_true(self):
        input = \
        r"""
        Var: x,y;
        Function: main
        Body:
            While !!!!!!True Do
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_call_function_with_array(self):
        input = \
        r"""
        Function: main
        Body:
            f({x , y , "True", 6537864}) ;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_var_initvalue_is_array_of_var(self):
        input = \
        r"""
        Function: main
        Parameter: x
        Body:
            Var: y = {{x}, {{}}, {x}};
        EndBody.
        
        """
        expect = "Error on line 5 col 23: x"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_var_initvalue_is_array_of_val(self):
        input = \
        r"""
        Function: main
        Parameter: x
        Body:
            Var: y = {{5,5.,0x3}, {{False}}, {"True"}};
        EndBody.
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_function_decl_12(self):
        input = \
        r"""
        Function: main
        Parameter: x
        Body:
            a = 0;
            Var x;
        EndBody.
        """
        expect = "Error on line 6 col 12: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_expr_14(self):
        input = \
        r"""
        Function: main
        Parameter: x
        Body:
            Return ((a < b) == (True < False));
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))
    
    def test_expr_15(self):
        input = \
        r"""
        Function: main
        Parameter: x
        Body:
            Return !((a < b + c + d + e && 567. ) == True);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))


    def test_expr_16(self):
        input = \
        r"""
        Function: main
        Parameter: x
        Body:
            Return (2*3 < 5);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))
