import unittest
from TestUtils import TestAST

# TODO import lai dong nay
from AST import *

# from initial-old.src.main.d96.utils.AST import *


class ASTGenSuite(unittest.TestCase):
    def testEmptyClass(self):
        i = """Class Adam{}"""
        e = str(Program([ClassDecl(Id("Adam"), [])]))
        self.assertTrue(TestAST.test(i, e, 1))
