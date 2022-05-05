import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program"""
        input = """
                    Class A : C{
                        Var b : Int = 5;
                        main(){
                            Var a: Int = 3;
                        }
                    }
                    Class B : C{}
                    """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 0))