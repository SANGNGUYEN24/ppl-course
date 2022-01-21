import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # ==================== Test literal ====================
    def testLiteralInteger1(self):
        # Decimal
        self.assertTrue(TestLexer.test("123456", "123456,<EOF>", 101))

    def testLiteralInteger2(self):
        # Negative decimal
        self.assertTrue(TestLexer.test("-123456", "-,123456,<EOF>", 102))

    def testLiteralInteger3(self):
        # Positive decimal
        self.assertTrue(TestLexer.test("+123456", "+,123456,<EOF>", 103))

    def testLiteralInteger4(self):
        # -+ decimal
        self.assertTrue(TestLexer.test("-+200401", "-,+,200401,<EOF>", 104))

    def testLiteralInteger5(self):
        # Underscore
        self.assertTrue(TestLexer.test("123_000_000", "123000000,<EOF>", 105))

    def testLiteralInteger6(self):
        self.assertTrue(TestLexer.test("123__000", "123,__000,<EOF>", 106))

    def testLiteralInteger7(self):
        self.assertTrue(TestLexer.test("_234__000", "_234__000,<EOF>", 106))
