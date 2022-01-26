import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # Program comment
    # 1
    def test_program_comment_simple(self):
        i = "## This a comment ##"
        e = "<EOF>"
        self.assertTrue(TestLexer.test(i, e, 1))
    # 2
    def test_program_comment_with_tab(self):
        i = "## This    a   comment     with    tab      ##"
        e = "<EOF>"
        self.assertTrue(TestLexer.test(i, e, 2))
    # 3
    def test_program_comment_with_tab_enter(self):
        i = """## This    a   comment     
            with    tab     and     enter
             
             ##"""
        e = "<EOF>"
        self.assertTrue(TestLexer.test(i, e, 3))
    # 4
    def test_program_comment_with_tab_enter_all_acsii_char(self):
        i = """## This    a   comment     
            with    tab     and     enter
            ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~';
             ##"""
        e = "<EOF>"
        self.assertTrue(TestLexer.test(i, e, 4))
    # 5
    def test_program_comment_unclosed_comment(self):
        i = "## This is an unclosed comment"
        e = "Error Token #"
        self.assertTrue(TestLexer.test(i, e, 5))
    # 6
    def test_program_comment_unclosed_reversed(self):
        i = "This is an unclosed comment ##"
        e = "This,is,an,unclosed,comment,Error Token #"
        self.assertTrue(TestLexer.test(i, e, 6))
    # Identifiers
    # 7
    def test_identifier_simple(self):
        i = "_GDeiame wGeevieae ___gtevicm $_GETDEVICNAM012345678 $_G_DE_N $GDeieNa"
        e = "_GDeiame,wGeevieae,___gtevicm,$_GETDEVICNAM012345678,$_G_DE_N,$GDeieNa,<EOF>"
        self.assertTrue(TestLexer.test(i, e, 7))
    # 8
    def test_identifier_begin_with_number(self):
        i = "0jsbwefv"
        e = "0,jsbwefv,<EOF>"
        self.assertTrue(TestLexer.test(i, e, 8))
    # 9
    def test_dollar_identifier_with_double_dollar_sign(self):
        i = "$$aher8236b"
        e = "Error Token $"
        self.assertTrue(TestLexer.test(i, e, 9))
    # 10
    def test_dollar_identifier_with_error_token(self):
        i = "$sldcjne.ihad"
        e = "$sldcjne,.,ihad,<EOF>"
        self.assertTrue(TestLexer.test(i, e, 10))
    # 11
    def test_keyword(self):
        i = "Break Continue If Elseif Else Foreach True False Array In Int Float Boolean String Return Null Class Val Var Self Constructor Destructor New By"
        e = "Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,Null,Class,Val,Var,Self,Constructor,Destructor,New,By,<EOF>"
        self.assertTrue(TestLexer.test(i, e, 11))
    # 12
    def test_operator_seperator(self):
        i = "+ - * / % ! && || == = != < <= > >= ==. +. . :: New ( ) [ ] . , ; : { }"
        e = "+,-,*,/,%,!,&&,||,==,=,!=,<,<=,>,>=,==.,+.,.,::,New,(,),[,],.,,,;,:,{,},<EOF>"
        self.assertTrue(TestLexer.test(i, e, 12))
    # Literals
    # 13
    def test_literal_integer_simple(self):
        i = "0 1 2 3 4 5 6 7 8 9 00 0x0 0X0 0b0 0B0 9876543210 07654321 0x987654321ABCDEF 0b10101110001"
        e = "0,1,2,3,4,5,6,7,8,9,00,0x0,0X0,0b0,0B0,9876543210,07654321,0x987654321ABCDEF,0b10101110001,<EOF>"
        self.assertTrue(TestLexer.test(i, e, 13))
    # 14
    def test_literal_integer_simple_with_underscore(self):
        i = "0_0 0x_0 0X_0 0b_0 0B_0 9_8_7_65432_1_0 07_6_5432_1 0x9_8_765_4321_ABCD_EF 0b1_0_10111_0001"
        e = "0,_0,0,x_0,0,X_0,0,b_0,0,B_0,9876543210,07654321,0x987654321ABCDEF,0b10101110001,<EOF>"
        self.assertTrue(TestLexer.test(i, e, 14))
    # 15
    def test_literal_integer(self):
        i = "0_0 0x_0 0X_0 0b_0 0B_0 9_8_7_65432_1_0 07_6_5432_1 0x9_8_765_4321_ABCD_EF 0b1_0_10111_0001"
        e = "0,_0,0,x_0,0,X_0,0,b_0,0,B_0,9876543210,07654321,0x987654321ABCDEF,0b10101110001,<EOF>"
        self.assertTrue(TestLexer.test(i, e, 15))
    # 16
    def test_literal_integer_with_0_after_prefix(self):
        i = "00000 0000012897 0x004385ABC 0b0101010"
        e = "00,00,0,00,00,012,897,0x0,043,85,ABC,0b0,101010,<EOF>"
        self.assertTrue(TestLexer.test(i, e, 16))
    #17
    def test_literal_integer_with_double_underscore(self):
        i = "123__8723 0__086734 0b101___010101111 0x123ACD_"
        e = "123,__8723,0,__086734,0b101,___010101111,0x123ACD,_,<EOF>"
        self.assertTrue(TestLexer.test(i,e,17))

    #18
    def test_float_full_3_part(self):
        i = "978.063e129 8_7_6_2.029e99 98_1.23e-10 24.928e+0230"
        e = "978.063e129,8762.029e99,981.23e-10,24.928e+0230,<EOF>"
        self.assertTrue(TestLexer.test(i,e,18))
    #19
    def test_float_without_integer_part(self):
        i = ".8374e128 .294e-8734 .02763e+0263 .3_6e8283"
        e = ".8374e128,.294e-8734,.02763e+0263,.,36e8283,<EOF>"
        self.assertTrue(TestLexer.test(i,e,19))
    #20
    def test_float_without_decimal_part(self):
        i = "28e+1972836 76e5_976 0287e-000172 0_837e87 8E-10"
        e = "28e+1972836,76e5,_976,02,87e-000172,0,_837e87,8E-10,<EOF>"
        self.assertTrue(TestLexer.test(i,e,20))

    #21
    def test_float_without_exponent_part(self):
        i = "3809.98762 973.37e 09843.5934 83_9673.983_78 39_87.832"
        e = "3809.98762,973.37,e,0,9843.5934,839673.983,_78,3987.832,<EOF>"
        self.assertTrue(TestLexer.test(i,e,21))
    #22
    def test_boolean(self):
        i = "True False"
        e = "True,False,<EOF>"
        self.assertTrue(TestLexer.test(i,e,22))







