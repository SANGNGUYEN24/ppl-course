import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_program_class_undeclared(self):
        print("____Test 0____")
        i = """
                    Class A : C{
                    }
                """
        e = "No Entry Point"
        self.assertTrue(TestChecker.test(i, e, 0))

    def test_undeclared_class(self):
        print("____Test 1____")
        i = """
                    Class Program{
                        main(){}
                    }
                    Class A : C{
                    }
                """
        e = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(i, e, 1))

    def test_without_main(self):
        print("____Test 2____")
        i = """
                Class Program{}
                Class A{}
            """
        e = "No Entry Point"
        self.assertTrue(TestChecker.test(i, e, 2))

    def test_main_with_param(self):
        print("____Test 3____")
        i = """
                    Class Program{
                        main(a: Int){}
                    }
                    Class A : C{
                    }
                """
        e = "No Entry Point"
        self.assertTrue(TestChecker.test(i, e, 3))

    def test_undeclared_class_2(self):
        print("____Test 4____")
        i = """
                    Class Program{
                        main(){}
                    }
                    Class A{}
                    Class B : A{}
                    Class C: D{}
                """
        e = "Undeclared Class: D"
        self.assertTrue(TestChecker.test(i, e, 4))

    def test_redeclared_attribute(self):
        print("____Test 5____")
        i = """
                    Class Program{
                        main(){}
                    }
                    Class A{
                        Var a : Int = 3;
                        Val a : Boolean = True;
                    }
                """
        e = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(i, e, 5))

    def test_redeclared_method(self):
        print("____Test 6____")
        i = """
                    Class Program{
                        main(){}
                    }
                    Class A{
                        foo(){}
                        foo(){}
                    }
                """
        e = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(i, e, 6))













