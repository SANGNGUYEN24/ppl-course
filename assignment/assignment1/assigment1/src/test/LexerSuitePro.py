import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    #==================== Test literal ====================
    def testLiteralInteger(self):
        self.assertTrue(TestLexer.test("123456","123456,<EOF>",101))

