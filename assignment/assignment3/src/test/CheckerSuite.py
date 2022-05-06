import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # def test_program_class_undeclared(self):
    #     """Simple program"""
    #     input = """
    #                 Class A : C{
    #                 }
    #             """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 0))
    #
    # def test_undeclared_class(self):
    #     """Simple program"""
    #     input = """
    #                 Class Program{
    #                     main(){}
    #                 }
    #                 Class A : C{
    #                 }
    #             """
    #     expect = "Undeclared Class: C"
    #     self.assertTrue(TestChecker.test(input, expect, 1))
    #
    # def test_program_without_main(self):
    #     """Simple program"""
    #     input = """     Class Program{}
    #                     Class A{}
    #                     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 2))
    #
    # def test_main_with_param(self):
    #     """Simple program"""
    #     input = """
    #                 Class Program{
    #                     main(a: Int){}
    #                 }
    #                 Class A : C{
    #                 }
    #             """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 3))

    def test_normal(self):
        """Simple program"""
        input = """
                    Class Program{
                        main(){}
                    }
                    Class A{}
                    Class B : A{}
                    Class C: A{}
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 4))











