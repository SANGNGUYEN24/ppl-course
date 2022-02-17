import unittest
from TestUtils import TestAST

# TODO import lai dong nay
# from AST import *

from initial.src.main.d96.utils.AST import *


class ASTGenSuite(unittest.TestCase):
    def testBreakStatement(self):
        i = """Class Adam{
                    Break;    
                }"""
        e = str(Program(ClassDecl()))
        self.assertTrue(TestAST.test(i, e, 300))
