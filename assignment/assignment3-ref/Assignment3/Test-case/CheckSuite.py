import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_variable(self):
        """Simple program: main"""
        input = """
                Var: a;
                Var: a;
                Function: main
                    Body: 
                        foo();
                EndBody.
                """
        expect = str(Redeclared(Variable(),"a"))
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_call_stmt_late_decl(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("f2"),[])])),
            FuncDecl(Id("f2"),[],([],[]))])
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_no_main_function(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("notmain"),[],([],[]))])

        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_type_cannot_be_inferred(self):
        input = """ 
                Var: a;
                Var: b;
                Function: main
                Body:
                    a = b;
                EndBody.
                 """
        expect = str(TypeCannotBeInferred(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_type_mismatch(self):
        input = """ 
                Var: a;
                Var: b;
                Function: main
                Body:
                    a = 4;
                    b = 3.0;
                    a = b;
                EndBody.
                 """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_type_mismatch_2(self):
        input = """ 
                Var: a = 3;
                Var: b;
                Function: main
                Body:
                    a = b;
                    b = True;
                EndBody.

                Function: foo
                Body:
                    Return 3;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id('b'),BooleanLiteral('true'))))
        self.assertTrue(TestChecker.test(input,expect,406))
    
    def test_type_mismatch_3(self):
        input = """ 
                Var: a = 3.0;
                Var: b;
                Function: main
                Body:
                    Var: y;
                    y  = a + b;
                    b = 2;
                EndBody.
                 """
        expect = str(TypeMismatchInExpression(BinaryOp('+',Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_type_mismatch_4(self):
        input = """ 
                Var: a = 3;
                Var: b;
                Function: main
                Body:
                    Var: y;
                    y  = a +. b;
                    b = 2;
                EndBody.
                 """
        expect = str(TypeMismatchInExpression(BinaryOp('+.',Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_type_mismatch_5(self):
        input = """ 
                Var: a = 3.0;
                Var: b;
                Function: main
                Body:
                    Var: y;
                    y  = a \\ b;
                    b = 2;
                EndBody.
                 """
        expect = str(TypeMismatchInExpression(BinaryOp('\\',Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_type_mismatch_6(self):
        input = """ 
                Var: a = 3.0;
                Function: main
                Body:
                    Var: y;
                    y  = -a;
                EndBody.
                 """
        expect = str(TypeMismatchInExpression(UnaryOp('-',Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_type_mismatch_7(self):
        input = """ 
                Var: a = 3.0;
                Var: b;
                Function: main
                Body:
                    Var: y;
                    y  = a + 1;
                EndBody.
                 """
        expect = str(TypeMismatchInExpression(BinaryOp('+',Id('a'),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_type_mismatch_8(self):
        input = """ 
                Function: main
                Body:
                    Return;
                EndBody.
                """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_parameter(self):
        input = """ 
                Function: main
                Parameter: x
                Body:
                    x = x + foo();
                EndBody.

                Function: foo
                Body:
                    Return 1.4;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.4))))
        self.assertTrue(TestChecker.test(input,expect,413))
    
    def test_parameter_2(self):
        input = """ 
                Function: main
                Body:
                    Return;
                EndBody.

                Function: foo
                Parameter: a, b
                Body:
                    a = 2;
                    b = 3.0;
                    a = b;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_parameter_3(self):
        input = """ 
                Function: main
                Body:
                    Return;
                EndBody.

                Function: foo
                Parameter: a, b
                Body:
                    a = 2;
                    c = 3;
                EndBody.
                """
        expect = str(Undeclared(Identifier(),'c'))
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test_number_of_parameter(self):
        input = """ 
                Function: main
                Body:
                    Var: a, b, c;
                    foo(a,b,c);
                EndBody.

                Function: foo
                Parameter: a, b
                Body:
                    a = 2;
                    b = 3;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[Id('a'),Id('b'),Id('c')])))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_built_in_func(self):
        input = """ 
                Function: main
                Body:
                    Var: a, b, c;
                EndBody.

                Function: read
                Parameter: a, b
                Body:
                    a = 2;
                    b = 3;
                EndBody.
                """
        expect = str(Redeclared(Function(),"read"))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_if_stmt(self):
        input = """ 
                Function: main
                Body:
                    If 1 Then
                    EndIf.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(If([(IntLiteral(1),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_starting_to_get_lazy_of_naming(self):
        input = """
        Var: x;
        Function: main
        Parameter: a,b
        Body:
            x = a + b;
            x = 3.5;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(3.5))))
        self.assertTrue(TestChecker.test(input,expect,419))          
 
    def test_20(self):
        input = """
        Var: x; 
        Function: main
        Parameter: a,b
        Body:
            x = a + b + test();
        EndBody.

        Function: test
        Body:
            Return 3.5;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(3.5))))
        self.assertTrue(TestChecker.test(input,expect,420)) 

    def test_21(self):
        input = """
        Function: main
        Body:
            test(1, 2);
            test(3.0, 4.0);
        EndBody.

        Function: test
        Parameter: a, b
        Body:
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("test"),[FloatLiteral(3.0),FloatLiteral(4.0)])))
        self.assertTrue(TestChecker.test(input,expect,421)) 

    def test_22(self):
        input = """
        Var: x;
        Var: y;
        Function: main
        Body:
            test(1, 2.0);
            test(x, y);
            x = x + y;
        EndBody.

        Function: test
        Parameter: a, b
        Body:
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+',Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input,expect,422)) 

    def test_23(self):
        input = """
        Function: main
        Body:
            Var: x;
            x = x + test()
        EndBody.

        Function: test
        Body:
            Return 1.9;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.9))))
        self.assertTrue(TestChecker.test(input,expect,423)) 

    def test_24(self):
        input = """
        Var: a, b;
        Function: main
        Parameter: x, y
        Body:
            x = 2;
            y = 3.5;
            main(a,b);
            a = 3.5;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),FloatLiteral(3.5))))
        self.assertTrue(TestChecker.test(input,expect,424)) 

    def test_25(self):
        input = """
        Function: main
        Parameter: x, y, z
        Body:
            x = 5;
            z = 6;
            main(5, x, 3.0);
            y = 3.5;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[IntLiteral(5),Id('x'),FloatLiteral(3.0)])))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_26(self):
        input = """
        Function: main
        Parameter: x, y
        Body:
            x = 5;
            main(5, x);
            y = 3.5;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("y"),FloatLiteral(3.5))))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_27(self):
        input = """
        Function: main
        Parameter: x, x
        Body:
        EndBody.
        """
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_28(self):
        input = """
        Var: x;

        Function: main
        Body:
            x = 3;
            x = foo2();
        EndBody.

        Function: foo2
        Body:
            Return 2.0;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(2.0))))
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_29(self):
        input = """
        Var: x;

        Function: main
        Body:
            x = foo2();
        EndBody.

        Function: foo2
        Body:
            Return 2.0;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('x'),CallExpr(Id('foo2'),[]))))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_30(self):
        input = """ 
                Function: main
                Body:
                    foo();
                EndBody.
                 """
        expect = str(Undeclared(Function(),'foo'))
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_31(self):
        input = """ 
                Function: main
                Body:
                    foo();
                EndBody.

                Function: foo
                Body:
                EndBody.
                 """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_32(self):
        input = """ 
        Function: main
        Body:
            For (x = 1, x < 1, x + 1) Do

            EndFor.
        EndBody.

            """
        expect = str(Undeclared(Identifier(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_33(self):
        input = """ 
        Function: main
        Body:
            Var: x;
            For (x = 1.0, x < 1, x + 1) Do

            EndFor.
        EndBody.

            """
        expect = str(TypeMismatchInStatement(For(Id('x'),FloatLiteral(1.0),BinaryOp('<',Id('x'),IntLiteral(1)),BinaryOp('+',Id('x'),IntLiteral(1)),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_34(self):
        input = """ 
        Function: main
        Body:
            Var: x;
            For (x = 1, True, x -. 1.9) Do

            EndFor.
        EndBody.
            """
        expect = str(TypeMismatchInExpression(BinaryOp('-.',Id('x'),FloatLiteral(1.9))))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_35(self):
        input = """ 
        Function: main
        Body:
            Var: x;
            For (x = 1, True, x - 1) Do
                x = True;
            EndFor.
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),BooleanLiteral('True'))))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_36(self):
        input = """ 
        Function: main
        Body:
            Var: x;
            Do x = 1;
            While 1
            EndDo.
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Dowhile(([],[Assign(Id('x'),IntLiteral(1))]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_37(self):
        input = """ 
        Function: main
        Body:
            Var: x;
            Do x = 1;
            While x
            EndDo.
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Dowhile(([],[Assign(Id('x'),IntLiteral(1))]),Id('x'))))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_38(self):
        input = """ 
        Function: main
        Body:
            While 1
            Do
            EndWhile.
        EndBody.
            """
        expect = str(TypeMismatchInStatement(While(IntLiteral(1),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_39(self):
        input = """ 
        Function: main
        Body:
            Var: x;
            While x
            Do
                x = 2;
            EndWhile.
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_40(self):
        input = """ 
        Function: main
        Body:
            Var: x;
            Var: y;
            While x
            Do
                y = 4;
            EndWhile.

            y = 3.0;
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id('y'),FloatLiteral(3.0))))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_41(self):
        input = """ 
        Function: main
        Body:
            While True
            Do
                Var: x = 4;
                While True
                Do
                    x = 5.0;
                EndWhile.
            EndWhile.
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),FloatLiteral(5.0))))
        self.assertTrue(TestChecker.test(input,expect,441))
    

    # def test_diff_numofparam_stmt(self):
    #     """Complex program"""
    #     input = """Function: main  
    #                Body:
    #                     printStrLn();
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function: main 
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"),[],([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[
    #                     CallExpr(Id("read"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,405))