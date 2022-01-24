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

    # Integer

    def test_integer_1(self):
        self.assertTrue(TestLexer.test(
            "1234 1_234_534 001234 0xA12D", "1234,1234534,00,1234,0xA12D,<EOF>", 111))

    def test_integer_2(self):
        self.assertTrue(TestLexer.test(
            "0b11111 7_0_0_0_1", "0b11111,70001,<EOF>", 112))

    def test_integer_3(self):
        self.assertTrue(TestLexer.test("07_0_0_0_1", "070001,<EOF>", 113))

    def test_integer_4(self):
        self.assertTrue(TestLexer.test("1", "1,<EOF>", 114))

    def test_integer_5(self):
        self.assertTrue(TestLexer.test("00123_2_0_1_1_0",
                        "00,12320110,<EOF>", 115))  # octal

    def test_integer_6(self):
        self.assertTrue(TestLexer.test(
            "0X9_12ADC", "0X912ADC,<EOF>", 116))  # hexa

    def test_integer_7(self):
        self.assertTrue(TestLexer.test(
            "0x0_1A9_1_0B", "0x0,_1A9_1_0B,<EOF>", 117))  # hexa

    def test_integer_8(self):
        self.assertTrue(TestLexer.test(
            "0x0_19_1_0", "0x0,_19_1_0,<EOF>", 118))  # hexa

    def test_integer_9(self):
        self.assertTrue(TestLexer.test("0B0_1_0_1_1_0",
                        "0B0,_1_0_1_1_0,<EOF>", 119))  # bin

    def test_integer_10(self):
        self.assertTrue(TestLexer.test(
            "0_120 0x123_12ACD0 0B012 0.10", "0,_120,0x12312ACD0,0B0,12,0.10,<EOF>", 120))

     # Floating
    def test_floating_1(self):
        self.assertTrue(TestLexer.test("1.234 1. .e3 1.0e-2 10.e-2",
                        "1.234,1.,.e3,1.0e-2,10.e-2,<EOF>", 121))

    def test_floating_2(self):
        self.assertTrue(TestLexer.test("1.2e3 90E3 12E+12400",
                        "1.2e3,90E3,12E+12400,<EOF>", 122))

    def test_floating_3(self):
        self.assertTrue(TestLexer.test("7E-10", "7E-10,<EOF>", 123))

    def test_floating_4(self):
        self.assertTrue(TestLexer.test("1_234.567", "1234.567,<EOF>", 124))

    def test_floating_5(self):
        self.assertTrue(TestLexer.test("1_2.5e-34", "12.5e-34,<EOF>", 125))

    def test_floating_6(self):
        self.assertTrue(TestLexer.test("1_2.34", "12.34,<EOF>", 126))

    def test_floating_7(self):
        self.assertTrue(TestLexer.test("1_2.01e-11", "12.01e-11,<EOF>", 127))

    def test_floating_8(self):
        self.assertTrue(TestLexer.test("1.E0_235", "1.E0,_235,<EOF>", 128))

    def test_floating_9(self):
        self.assertTrue(TestLexer.test("0.01", "0.01,<EOF>", 129))

    def test_floating_10(self):
        self.assertTrue(TestLexer.test(".01E+11", ".01E+11,<EOF>", 130))
