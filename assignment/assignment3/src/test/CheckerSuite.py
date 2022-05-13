import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # def test_program_class_undeclared(self):
    #     print("____Test 0____")
    #     i = """
    #                 Class A : C{
    #                 }
    #             """
    #     e = "No Entry Point"
    #     self.assertTrue(TestChecker.test(i, e, 0))
    #
    # def test_undeclared_class(self):
    #     print("____Test 1____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A : C{
    #                 }
    #             """
    #     e = "Undeclared Class: C"
    #     self.assertTrue(TestChecker.test(i, e, 1))
    #
    # def test_without_main(self):
    #     print("____Test 2____")
    #     i = """
    #             Class Program{}
    #             Class A{}
    #         """
    #     e = "No Entry Point"
    #     self.assertTrue(TestChecker.test(i, e, 2))
    #
    # def test_main_with_param(self):
    #     print("____Test 3____")
    #     i = """
    #                 Class Program{
    #                     main(a: Int){}
    #                 }
    #                 Class A : C{
    #                 }
    #             """
    #     e = "No Entry Point"
    #     self.assertTrue(TestChecker.test(i, e, 3))
    #
    # def test_undeclared_class_2(self):
    #     print("____Test 4____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{}
    #                 Class B : A{}
    #                 Class C: D{}
    #             """
    #     e = "Undeclared Class: D"
    #     self.assertTrue(TestChecker.test(i, e, 4))
    #
    # #
    # def test_redeclared_attribute(self):
    #     print("____Test 5____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     Var a : Int = 3;
    #                     Val a : Boolean = True;
    #                 }
    #             """
    #     e = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(i, e, 5))
    #
    # def test_redeclared_method(self):
    #     print("____Test 6____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     foo(){}
    #                     foo(){}
    #                 }
    #             """
    #     e = "Redeclared Method: foo"
    #     self.assertTrue(TestChecker.test(i, e, 6))
    #
    # def test_redeclared_method_2(self):
    #     print("____Test 7____")
    #     i = """
    #                     Class Program{
    #                         main(){}
    #                     }
    #                     Class A{
    #                         foo(){}
    #                         foo2(){}
    #                         function(){}
    #                         foo(){}
    #                     }
    #                 """
    #     e = "Redeclared Method: foo"
    #     self.assertTrue(TestChecker.test(i, e, 7))
    #
    # #
    # def test_redeclared_method_3(self):
    #     print("____Test 8____")
    #     i = """
    #                     Class Program{
    #                         main(){}
    #                     }
    #                     Class A{
    #                         foo(){}
    #                         foo2(){}
    #                         function(){}
    #                         foo2(){}
    #                     }
    #                 """
    #     e = "Redeclared Method: foo2"
    #     self.assertTrue(TestChecker.test(i, e, 8))
    #
    # def test_redeclared_method_in_program(self):
    #     print("____Test 9____")
    #     i = """
    #                     Class Program{
    #                         main(){}
    #                         main(){}
    #                     }
    #                 """
    #     e = "Redeclared Method: main"
    #     self.assertTrue(TestChecker.test(i, e, 9))
    #
    # def test_redeclared_variable(self):
    #     print("____Test 10____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     foo(){
    #                         Var a : Int = 4;
    #                         Var a : Float;
    #                     }
    #                 }
    #             """
    #     e = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(i, e, 10))
    #
    # def test_redeclared_const(self):
    #     print("____Test 11____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     foo(){
    #                         Var a : Int = 4;
    #                         Val a : Int = 10;
    #                     }
    #                 }
    #             """
    #     e = "Redeclared Constant: a"
    #     self.assertTrue(TestChecker.test(i, e, 11))
    #
    # def test_redeclared_variable_2(self):
    #     print("____Test 12____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     foo(a : Int){
    #                         Var a : Int = 4;
    #                     }
    #                 }
    #             """
    #     e = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(i, e, 12))
    #
    # def test_redeclared_param(self):
    #     print("____Test 13____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     foo(a, b, c, b : Int){
    #                         Var a : Int = 4;
    #                     }
    #                 }
    #             """
    #     e = "Redeclared Parameter: b"
    #     self.assertTrue(TestChecker.test(i, e, 13))
    #
    # def test_redeclared_variable_3(self):
    #     print("____Test 14____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     foo(a, b: Int){
    #                         Var a : Int = 4;
    #                     }
    #                 }
    #             """
    #     e = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(i, e, 14))
    #
    # def test_redeclared_class(self):
    #     print("____Test 15____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{}
    #                 Class A{}
    #             """
    #     e = "Redeclared Class: A"
    #     self.assertTrue(TestChecker.test(i, e, 15))
    #
    # def test_redeclared_class_2(self):
    #     print("____Test 16____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{}
    #                 Class B : A{}
    #                 Class C : A{}
    #                 Class B{}
    #             """
    #     e = "Redeclared Class: B"
    #     self.assertTrue(TestChecker.test(i, e, 16))
    #
    # def test_cannot_assign_to_constant(self):
    #     print("____Test 17____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     foo(a, b: Int){
    #                         Val c : Int = 4;
    #                         c = 10;
    #                     }
    #                 }
    #             """
    #     e = "Cannot Assign To Constant: AssignStmt(Id(c),IntLit(10))"
    #     self.assertTrue(TestChecker.test(i, e, 17))
    #
    # def test_cannot_assign_to_constant_1(self):
    #     print("____Test 18____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     Val c: Int = 4;
    #                     foo(a, b: Int){
    #                         c = 10;
    #                     }
    #                 }
    #             """
    #     e = "Cannot Assign To Constant: AssignStmt(Id(c),IntLit(10))"
    #     self.assertTrue(TestChecker.test(i, e, 18))
    #
    # def test_type_mismatch_in_constant(self):
    #     print("____Test 19____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     foo(a, b: Int){
    #                         Val c : Int = 1.2;
    #                     }
    #                 }
    #             """
    #     e = "Type Mismatch In Constant Declaration: ConstDecl(Id(c),IntType,FloatLit(1.2))"
    #     self.assertTrue(TestChecker.test(i, e, 19))
    #
    # def test_type_mismatch_in_constant_1(self):
    #     print("____Test 20____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     foo(a, b: Int){
    #                         Val c : Boolean = 1;
    #                     }
    #                 }
    #             """
    #     e = "Type Mismatch In Constant Declaration: ConstDecl(Id(c),BoolType,IntLit(1))"
    #     self.assertTrue(TestChecker.test(i, e, 20))
    #
    # def test_illegal_constant_expr(self):
    #     print("____Test 21____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     foo(a, b: Int){
    #                         Val c : Boolean;
    #                     }
    #                 }
    #             """
    #     e = "Illegal Constant Expression: None"
    #     self.assertTrue(TestChecker.test(i, e, 21))
    #
    # def test_undeclared_identifier_attribute(self):
    #     print("____Test 22____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     Val b : Int = a;
    #                 }
    #             """
    #     e = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(i, e, 22))
    #
    # def test_undeclared_identifier_attribute_2(self):
    #     print("____Test 23____")
    #     i = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A{
    #                     Var b : Int = a;
    #                 }
    #             """
    #     e = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(i, e, 23))
    #
    # def test_undeclared_identifier_attribute_in_program(self):
    #     print("____Test 25____")
    #     i = """
    #                 Class Program{
    #                     Val b : Int = c;
    #                     main(){}
    #                 }
    #                 Class A{
    #                 }
    #             """
    #     e = "Undeclared Identifier: c"
    #     self.assertTrue(TestChecker.test(i, e, 24))
    #
    # def test_undeclared_identifier_method(self):
    #     print("____Test 25____")
    #     i = """
    #                Class Program{
    #                    main(){}
    #                }
    #                Class A{
    #                    foo(){
    #                        Var b : Int = a;
    #                    }
    #                }
    #            """
    #     e = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(i, e, 25))
    #
    # def test_undeclared_identifier_in_class(self):
    #     print("____Test 26____")
    #     i = """
    #                Class Program{
    #                    main(){}
    #                }
    #                Class A{
    #                     Var b : Int = c + 1;
    #                }
    #            """
    #     e = "Undeclared Identifier: c"
    #     self.assertTrue(TestChecker.test(i, e, 26))
    #
    # def test_type_mismatch_in_expr(self):
    #     print("____Test 27____")
    #     i = """
    #                Class Program{
    #                    main(){}
    #                }
    #                Class A{
    #                     Var b : Int = True + 1;
    #                }
    #            """
    #     e = "Type Mismatch In Expression: BinaryOp(+,BooleanLit(True),IntLit(1))"
    #     self.assertTrue(TestChecker.test(i, e, 27))
    #
    # def test_undeclared_attribute(self):
    #     print("____Test 28____")
    #     i = """
    #                Class Program{
    #                    main(){}
    #                }
    #                Class A{}
    #                Class B{
    #                     Var a : Int = A.b;
    #                }
    #            """
    #     e = "Undeclared Attribute: b"
    #     self.assertTrue(TestChecker.test(i, e, 28))
    #
    # def test_undeclared_class_3(self):
    #     print("____Test 29____")
    #     i = """
    #                Class Program{
    #                    main(){}
    #                }
    #                Class B{
    #                     Var a : Int = A.b;
    #                }
    #            """
    #     e = "Undeclared Class: A"
    #     self.assertTrue(TestChecker.test(i, e, 29))
    #
    # def test_undeclared_attribute_const(self):
    #     print("____Test 30____")
    #     i = """
    #                Class Program{
    #                    main(){}
    #                }
    #                Class A{}
    #                Class B{
    #                     Val a : Int = A.b;
    #                }
    #            """
    #     e = "Undeclared Attribute: b"
    #     self.assertTrue(TestChecker.test(i, e, 30))
    #
    # def test_undeclared_identifier(self):
    #     print("____Test 30____")
    #     i = """
    #                Class Program{
    #                    main(){}
    #                }
    #
    #                Class B{
    #                     foo(){
    #                         Val a : Int = A.b;
    #                     }
    #                }
    #            """
    #     e = "Undeclared Class: A"
    #     self.assertTrue(TestChecker.test(i, e, 30))
    #
    # def test_undeclared_identifier_2(self):
    #     print("____Test 31____")
    #     i = """
    #                Class Program{
    #                    main(){}
    #                }
    #                Class A{}
    #                Class B{
    #                     foo(){
    #                         Val a : Int = A.b;
    #                     }
    #                }
    #            """
    #     e = "Undeclared Attribute: b"
    #     self.assertTrue(TestChecker.test(i, e, 31))
    #
    # def test_type_mismatch_in_statement(self):
    #     print("____Test 33____")
    #     i = """
    #                Class Program{
    #                    main(){}
    #                }
    #                Class A{
    #                     Val b: Float = 5.0;
    #                }
    #                Class B{
    #                     Var a : Int = A.b;
    #                }
    #            """
    #     e = "Type Mismatch In Statement: AttributeDecl(Instance,VarDecl(Id(a),IntType,FieldAccess(Id(A),Id(b))))"
    #     self.assertTrue(TestChecker.test(i, e, 33))
    #
    # def test_type_mismatch_in_const(self):
    #     print("____Test 34____")
    #     i = """
    #                Class Program{
    #                    main(){}
    #                }
    #                Class A{
    #                     Val b: Float = 5.0;
    #                }
    #                Class B{
    #                     Val a : Int = A.b;
    #                }
    #            """
    #     e = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FieldAccess(Id(A),Id(b)))"
    #     self.assertTrue(TestChecker.test(i, e, 34))
    #
    # def test_undeclared_method(self):
    #     print("____Test 36____")
    #     i = """
    #                Class Program{
    #                    main(){}
    #                }
    #                Class A{
    #                     Val b: Float = 5.0;
    #                }
    #                Class B{
    #                     Val a : Int = A.b();
    #                }
    #            """
    #     e = "Undeclared Method: b"
    #     self.assertTrue(TestChecker.test(i, e, 36))
    #
    # def test_condition_in_if(self):
    #     print("____Test 37____")
    #     i = """
    #                Class Program{
    #                    main(){}
    #                }
    #                Class A{
    #                     foo(){
    #                         If (1 == 1){
    #                         }
    #                         Else{}
    #                     }
    #                }
    #            """
    #     e = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(i, e, 37))

    def test_redeclared_attribute(self):
        print("____Test 37____")
        i = """
                   Class Program{
                       main(){}
                   }
                   Class A{
                        Var a : String = "Hello";
                        Var a: Int; 
                   }
               """
        e = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(i, e, 37))



