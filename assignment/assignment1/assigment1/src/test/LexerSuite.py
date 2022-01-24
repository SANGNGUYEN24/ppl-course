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

    # Keywords, separators, operators
    def test_keyword_1(self):
        self.assertTrue(TestLexer.test("Int Break ForEach 1 + 2 Destructor",
                        "Int,Break,ForEach,1,+,2,Destructor,<EOF>", 131))

    def test_keyword_2(self):
        self.assertTrue(TestLexer.test(
            "+. ==. . ## # 1 ##", "+.,==.,.,<EOF>", 132))

    def test_keyword_3(self):
        self.assertTrue(TestLexer.test(",;::x++/SelfBooleanInArray",
                        ",,;,::,x,+,+,/,SelfBooleanInArray,<EOF>", 133))

    def test_keyword_4(self):
        self.assertTrue(TestLexer.test("0xContinue 0xBreak 0xFalse 0xString Val Var New",
                        "0xC,ontinue,0xB,reak,0xF,alse,0,xString,Val,Var,New,<EOF>", 134))

    def test_keyword_5(self):
        self.assertTrue(TestLexer.test(
            "({/By Array In If}[.].&&!::+.||)", "(,{,/,By,Array,In,If,},[,.,],.,&&,!,::,+.,||,),<EOF>", 135))

    def test_keyword_6(self):
        self.assertTrue(TestLexer.test("==,-.(<<=>>=,)",
                        "==,,,-,.,(,<,<=,>,>=,,,),<EOF>", 136))

    def test_keyword_7(self):
        self.assertTrue(TestLexer.test("=!####The end of file<>!+=*#",
                        "=,!,The,end,of,file,<,>,!,+,=,*,Error Token #", 137))

    def test_keyword_8(self):
        self.assertTrue(TestLexer.test("..::In+Break-Array%Constructor",
                        "..,::,In,+,Break,-,Array,%,Constructor,<EOF>", 138))

    def test_keyword_9(self):
        self.assertTrue(TestLexer.test("ELSEIFIF-If,ElseIf+.==.Else##new##Return(.,)",
                        "ELSEIFIF,-,If,,,ElseIf,+.,==.,Else,Return,(,.,,,),<EOF>", 139))

    def test_keyword_10(self):
        self.assertTrue(TestLexer.test(
            "!-=[<!_33>]SelfIf,./!==", "!,-,=,[,<,!,_33,>,],SelfIf,,,.,/,!=,=,<EOF>", 140))

    # Comments

    def test_comment_1(self):
        self.assertTrue(TestLexer.test("### Hello there ##", "<EOF>", 151))

    # def test_comment_2(self):
    #     self.assertTrue(TestLexer.test("## !_203 Hello ## ####", "<EOF>", 152))

    # def test_comment_3(self):
    #     self.assertTrue(TestLexer.test("## Hello there ## ##", "<EOF>", 153))

    # def test_comment_4(self):
    #     self.assertTrue(TestLexer.test(
    #         "## Hello there 12232 ## 3232 ##", "3232,<EOF>", 154))

    # def test_comment_5(self):
    #     self.assertTrue(TestLexer.test("####", "<EOF>", 155))

    # def test_comment_6(self):
    #     self.assertTrue(TestLexer.test("##", "<EOF>", 156))

    # TODO Xem lai testcase nay
    # def testString(self):
    #     self.assertTrue(TestLexer.test(""" "abc \\h def" """, "abc \\h def, <EDF>", 152))

    # Testcase cua Viet
    def test_101(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_102(self):
        self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 102))

    def test_103(self):
        self.assertTrue(TestLexer.test("Break", "Break,<EOF>", 103))

    def test_BK_3(self):
        self.assertTrue(TestLexer.test("ab?svn", "ab,Error Token ?", 104))

    def test_105(self):
        self.assertTrue(TestLexer.test("Return x;", "Return,x,;,<EOF>", 105))

    def test_106(self):
        self.assertTrue(TestLexer.test(""" "abc\\h def" """, """Illegal Escape In String: abc\\h""", 106))

    def test_107(self):
        self.assertTrue(TestLexer.test(""" "abc def """, """Unclosed String: abc def """, 107))

    def test_108(self):
        self.assertTrue(TestLexer.test(""" "abc\\\\h def" """, """"abc\\\\h def",<EOF>""", 108))

    def test_109(self):
        self.assertTrue(TestLexer.test(""" "abc\\a def" """, """Illegal Escape In String: abc\\a""", 109))

    def test_110(self):
        self.assertTrue(TestLexer.test(""" "abc\\' def" """, """"abc\\' def",<EOF>""", 110))

    def test_111(self):
        self.assertTrue(TestLexer.test(""" 12345 """, """12345,<EOF>""", 111))

    def test_112(self):
        self.assertTrue(TestLexer.test(""" "abc\\\\ def" """, """"abc\\\\ def",<EOF>""", 112))

    def test_113(self):
        self.assertTrue(TestLexer.test(""" "abc\\\\h def" """, """"abc\\\\h def",<EOF>""", 113))

    def test_114(self):
        self.assertTrue(TestLexer.test(""" 1.23e-15 """, """1.23e-15,<EOF>""", 114))

    def test_115(self):
        self.assertTrue(TestLexer.test(""" 1.23e15 """, """1.23e15,<EOF>""", 115))

    def test_116(self):
        self.assertTrue(TestLexer.test("""1_234_567.123""", """1234567.123,<EOF>""", 116))

    def test_117(self):
        self.assertTrue(TestLexer.test("""7E-10""", """7E-10,<EOF>""", 117))

    def test_118(self):
        self.assertTrue(TestLexer.test("""7E-10""", """7E-10,<EOF>""", 118))

    def test_119(self):
        self.assertTrue(TestLexer.test(""""The string \\""", """Unclosed String: The string """, 119))

    def test_120(self):
        self.assertTrue(
            TestLexer.test(""" "\\b \\f \\r \\n \\t \\' \\\\ '" " """, """"\\b \\f \\r \\n \\t \\' \\\\ '" ",<EOF>""",
                           120))

    def test_121(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \\t" """,
                                       """"This is a string containing tab \\t",<EOF>""", 121))

    def test_122(self):
        self.assertTrue(
            TestLexer.test(""" "He asked me:'"Where is John?'"" """, """"He asked me:'"Where is John?'"",<EOF>""", 122))

    def test_123(self):
        self.assertTrue(TestLexer.test(""" "abc \\n def" """, """"abc \\n def",<EOF>""", 123))

    def test_124(self):
        self.assertTrue(TestLexer.test("1323_a_321_1", "1323,_a_321_1,<EOF>", 124))

    def test_125(self):
        self.assertTrue(TestLexer.test("1_234.567_789e246_357", "1234.567,_789e246_357,<EOF>", 125))

    def test_126(self):
        self.assertTrue(TestLexer.test("0x13A2D_321_D_1", "0x13A2D321D1,<EOF>", 126))

    def test_127(self):
        self.assertTrue(TestLexer.test("0X12_AB_Aabc", "0X12ABA,abc,<EOF>", 127))

    def test_128(self):
        self.assertTrue(TestLexer.test("0X12_AB_Aabc123", "0X12ABA,abc123,<EOF>", 128))

    def test_129(self):
        self.assertTrue(TestLexer.test("0x12_AB_Aabc123", "0x12ABA,abc123,<EOF>", 129))

    def test_130(self):
        self.assertTrue(TestLexer.test("071010788", "0710107,88,<EOF>", 130))

    def test_131(self):
        self.assertTrue(TestLexer.test("071010788xo123", "0710107,88,xo123,<EOF>", 131))

    def test_132(self):
        self.assertTrue(TestLexer.test("071__010788", "071,__010788,<EOF>", 132))

    def test_133(self):
        self.assertTrue(TestLexer.test("098076", "0,98076,<EOF>", 133))

    def test_134(self):
        self.assertTrue(TestLexer.test("0x12BAC", "0x12BAC,<EOF>", 134))

    def test_135(self):
        self.assertTrue(TestLexer.test("0x12bac", "0x12,bac,<EOF>", 135))

    def test_136(self):
        self.assertTrue(TestLexer.test(""" "Hello\nworld" """, "Unclosed String: Hello", 136))

    def test_137(self):
        self.assertTrue(TestLexer.test("071010_788", "0710107,88,<EOF>", 137))

    def test_138(self):
        self.assertTrue(TestLexer.test("New York", "New,York,<EOF>", 138))

    def test_139(self):
        self.assertTrue(TestLexer.test("Var a:Int=1+1;", "Var,a,:,Int,=,1,+,1,;,<EOF>", 139))

    def test_140(self):
        self.assertTrue(TestLexer.test("Var a:Int;", "Var,a,:,Int,;,<EOF>", 140))

    def test_141(self):
        self.assertTrue(TestLexer.test("foo(a,b:Int;c:String){}", "foo,(,a,,,b,:,Int,;,c,:,String,),{,},<EOF>", 141))

    def test_142(self):
        self.assertTrue(TestLexer.test("foo(){}", "foo,(,),{,},<EOF>", 142))

    def test_143(self):
        self.assertTrue(TestLexer.test("Class Shape{}", "Class,Shape,{,},<EOF>", 143))

    def test_144(self):
        self.assertTrue(TestLexer.test("a[b[012]][foo()]", "a,[,b,[,012,],],[,foo,(,),],<EOF>", 144))

    def test_145(self):
        self.assertTrue(TestLexer.test("a.b", "a,.,b,<EOF>", 145))

    def test_146(self):
        self.assertTrue(TestLexer.test("Var a:Array[Int,5];", "Var,a,:,Array,[,Int,,,5,],;,<EOF>", 146))

    def test_147(self):
        self.assertTrue(
            TestLexer.test("Array(Array(1,1),Array(1,1))", "Array,(,Array,(,1,,,1,),,,Array,(,1,,,1,),),<EOF>", 147))

    def test_148(self):
        self.assertTrue(TestLexer.test(""" Array("abc \\\\h") """, """Array,(,"abc \\\\h",),<EOF>""", 148))

    def test_149(self):
        self.assertTrue(TestLexer.test("Array(1,1)", "Array,(,1,,,1,),<EOF>", 149))

    def test_150(self):
        self.assertTrue(TestLexer.test(""" Array("abc \\h") """, """Array,(,Illegal Escape In String: abc \\h""", 150))

    def test_151(self):
        self.assertTrue(TestLexer.test("26.11-2", "26.11,-,2,<EOF>", 151))

    def test_152(self):
        self.assertTrue(TestLexer.test("26.", "26.,<EOF>", 152))

    def test_153(self):
        self.assertTrue(TestLexer.test("0x26.11e-", "0x26,.,11,e,-,<EOF>", 153))

    def test_154(self):
        self.assertTrue(TestLexer.test("0x26.11e-2", "0x26,.11e-2,<EOF>", 154))

    def test_155(self):
        self.assertTrue(TestLexer.test("0xABCDEFGHI", "0xABCDEF,GHI,<EOF>", 155))

    def test_156(self):
        self.assertTrue(TestLexer.test("0_123", "0,_123,<EOF>", 156))

    def test_157(self):
        self.assertTrue(TestLexer.test(".26", ".,26,<EOF>", 157))

    def test_158(self):
        self.assertTrue(TestLexer.test("## This is a\\n multi-line \\n comment.\\n ##", "<EOF>", 158))

    def test_159(self):
        self.assertTrue(TestLexer.test("##Hello## ##world##", "<EOF>", 159))

    def test_160(self):
        self.assertTrue(TestLexer.test("##Hello#another#world\\h##", "<EOF>", 160))

    def test_161(self):
        self.assertTrue(TestLexer.test("""abc"This is a string containing tab \\v 12asd"23xyz""",
                                       "abc,Illegal Escape In String: This is a string containing tab \\v", 161))

    def test_162(self):
        self.assertTrue(TestLexer.test("""abc"This is a string containing tab \\n 12asd"23xyz""",
                                       """abc,"This is a string containing tab \\n 12asd",23,xyz,<EOF>""", 162))

    def test_163(self):
        self.assertTrue(TestLexer.test("##Hello#another#world\\h##", "<EOF>", 163))

    def test_164(self):
        self.assertTrue(TestLexer.test("##Hello#another#world\\h\\n##abc# ", "abc,Error Token #", 164))

    def test_165(self):
        self.assertTrue(TestLexer.test("##Hello#another#world\\h#\\h#", "Error Token #", 165))

    def test_166(self):
        self.assertTrue(TestLexer.test("""abc"avc \\m abv "abc""", """abc,Illegal Escape In String: avc \\m""", 166))

    def test_167(self):
        self.assertTrue(TestLexer.test("abc#abc", "abc,Error Token #", 167))

    def test_168(self):
        self.assertTrue(TestLexer.test("123##123##", "123,<EOF>", 168))

    def test_169(self):
        self.assertTrue(TestLexer.test("1-1##1-1##1-1", "1,-,1,1,-,1,<EOF>", 169))

    def test_170(self):
        self.assertTrue(TestLexer.test("1------1+1", "1,-,-,-,-,-,-,1,+,1,<EOF>", 170))

    def test_171(self):
        self.assertTrue(TestLexer.test(""" ## This is the first comment. ## """, "<EOF>", 171))

    def test_172(self):
        self.assertTrue(TestLexer.test("(abcdef)", "(,abcdef,),<EOF>", 172))

    def test_173(self):
        self.assertTrue(TestLexer.test("1_2_3_4_5", "12345,<EOF>", 173))

    def test_174(self):
        self.assertTrue(TestLexer.test("0b1_0101", "0b10101,<EOF>", 174))

    def test_175(self):
        self.assertTrue(TestLexer.test("0x1_2_3AB 0X4_5_CDE", "0x123AB,0X45CDE,<EOF>", 175))

    def test_176(self):
        self.assertTrue(TestLexer.test("0x00_A_BC", "0x0,0,_A_BC,<EOF>", 176))

    def test_177(self):
        self.assertTrue(TestLexer.test("00xAB_C", "00,xAB_C,<EOF>", 177))

    def test_178(self):
        self.assertTrue(TestLexer.test(""" 0xABCD_E_FG """, "0xABCDEF,G,<EOF>", 178))

    def test_179(self):
        self.assertTrue(TestLexer.test("00123_67 0O10007", "00,12367,0,O10007,<EOF>", 179))

    def test_180(self):
        self.assertTrue(TestLexer.test("0b00101001", "0b0,0101001,<EOF>", 180))

    def test_181(self):
        self.assertTrue(TestLexer.test(""" "abc\\'def gh" """, """"abc\\'def gh",<EOF>""", 181))

    def test_182(self):
        self.assertTrue(TestLexer.test(""" "'abcdef" """, """"'abcdef",<EOF>""", 182))

    def test_183(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \\t" """,
                                       """"This is a string containing tab \\t",<EOF>""", 183))

    def test_184(self):
        self.assertTrue(TestLexer.test("!!!!a", "!,!,!,!,a,<EOF>", 184))

    def test_185(self):
        self.assertTrue(TestLexer.test(""" "++.--.* *.\\\\.<<.>>.<=<=.>=>=.===/=" """,
                                       """"++.--.* *.\\\\.<<.>>.<=<=.>=>=.===/=",<EOF>""", 185))

    def test_186(self):
        self.assertTrue(TestLexer.test(""" "abcdef" """, """"abcdef",<EOF>""", 186))

    def test_187(self):
        self.assertTrue(TestLexer.test("1 + 2 * 3 ** 4 ** * 5", """1,+,2,*,3,*,*,4,*,*,*,5,<EOF>""", 187))

    def test_188(self):
        self.assertTrue(TestLexer.test("True && True False || False", "True,&&,True,False,||,False,<EOF>", 188))

    def test_189(self):
        self.assertTrue(TestLexer.test(""" "1.0 +. 0.1 1.2 =/= 1.2 5.5 \\. 1.1" """,
                                       """Illegal Escape In String: 1.0 +. 0.1 1.2 =/= 1.2 5.5 \.""", 189))

    def test_190(self):
        self.assertTrue(TestLexer.test(""" "TrueFalseTrueFalse' " """, """"TrueFalseTrueFalse' ",<EOF>""", 190))

    def test_191(self):
        self.assertTrue(TestLexer.test(""" "abc\\" """, """Illegal Escape In String: abc\\\"""", 191))

    def test_192(self):
        self.assertTrue(TestLexer.test("000_x123", "00,0,_x123,<EOF>", 192))

    def test_193(self):
        self.assertTrue(TestLexer.test("""He asked me: 'Where is John?'""", "He,asked,me,:,Error Token '", 193))

    def test_194(self):
        self.assertTrue(TestLexer.test("1_234.567_789e246_357", "1234.567,_789e246_357,<EOF>", 194))

    def test_195(self):
        self.assertTrue(TestLexer.test("Something \ ", """Something,Error Token \\""", 195))

    def test_196(self):
        self.assertTrue(TestLexer.test(""" abc" """, """abc,Unclosed String:  """, 196))

    def test_197(self):
        self.assertTrue(TestLexer.test(""" "'abc """, """Unclosed String: 'abc """, 197))

    def test_198(self):
        self.assertTrue(TestLexer.test(""" 123.1e3000 0X1D """, """123.1e3000,0X1D,<EOF>""", 198))

    def test_199(self):
        self.assertTrue(TestLexer.test(""" "abc\n\abc\" """, """Unclosed String: abc""", 199))

    def test_200(self):
        self.assertTrue(TestLexer.test(""" $a123 """, """$a123,<EOF>""", 200))




