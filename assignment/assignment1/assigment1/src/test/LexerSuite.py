import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # Identifiers
    def test_identifier_1(self):
        self.assertTrue(TestLexer.test("_1", "_1,<EOF>", 101))

    def test_identifier_2(self):
        self.assertTrue(TestLexer.test("a1_23", "a1_23,<EOF>", 102))

    def test_identifier_3(self):
        self.assertTrue(TestLexer.test("_a123", "_a123,<EOF>", 103))

    def test_identifier_4(self):
        self.assertTrue(TestLexer.test("__A1_2_3", "__A1_2_3,<EOF>", 104))

    def test_identifier_5(self):
        self.assertTrue(TestLexer.test("$_abc", "$_abc,<EOF>", 105))

    def test_identifier_6(self):
        self.assertTrue(TestLexer.test("$9", "$9,<EOF>", 106))

    def test_identifier_7(self):
        self.assertTrue(TestLexer.test(
            "abc_cd $_95 ABCxre _293cjSjdl;", "abc_cd,$_95,ABCxre,_293cjSjdl,;,<EOF>", 107))

    def test_identifier_8(self):
        self.assertTrue(TestLexer.test("abc$_129_139avfe",
                        "abc,$_129_139avfe,<EOF>", 108))

    def test_identifier_9(self):
        self.assertTrue(TestLexer.test("$hle_2;$0$___sIF39____42",
                        "$hle_2,;,$0,$___sIF39____42,<EOF>", 109))

    def test_identifier_10(self):
        self.assertTrue(TestLexer.test("", "<EOF>", 110))
