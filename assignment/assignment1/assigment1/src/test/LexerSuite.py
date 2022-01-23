import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

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
