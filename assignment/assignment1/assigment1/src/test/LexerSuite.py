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

    def test_comment_7(self):
        self.assertTrue(TestLexer.test("## Hello ##", "<EOF>", 157))

    def test_comment_8(self):
        self.assertTrue(TestLexer.test(
            "## !!!=23242_here ###", "Error Token #", 158))

    # Mixed
    def test_mixed_1(self):
      self.assertTrue(TestLexer.test(
          "## Hello there ## $_9 abc , 1_20e0-123", "$_9,abc,,,120e0,-,123,<EOF>", 159))

    def test_mixed_2(self):
        self.assertTrue(TestLexer.test(
            "0XA_BC_D_E_1_2_F_0 00.01e-3 __1 ##", "0XABCDE12F0,00,.01e-3,__1,<EOF>", 160))

    def test_mixed_3(self):
        inp = """ 
            Class program {
                Var x : Int = 10;
                get(ac,d,f: Int, b: Float) {
                    Var _12, a : Float = 12, 10.0;
                }
            }
        """
        exp = "Class,program,{,Var,x,:,Int,=,10,;,get,(,ac,,,d,,,f,:,Int,,,b,:,Float,),{,Var,_12,,,a,:,Float,=,12,,,10.0,;,},},<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, 161))

    def test_mixed_4(self):
        inp = """ 
            Class program {
                Var x,y : Int = 10;
                Val $x, yz = 10;
            }
        """
        exp = "Class,program,{,Var,x,,,y,:,Int,=,10,;,Val,$x,,,yz,=,10,;,},<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, 162))

    def test_mixed_5(self):
        inp = """ 
            Class program {
                get() {
                    If(1 == 1) {
                        ForEach(x In 1 .. 100)
                    }
                Var a : X =  New X();
                Val i : Float = 1.23_3e-1;
            }
            }
        """
        exp = "Class,program,{,get,(,),{,If,(,1,==,1,),{,ForEach,(,x,In,1,..,100,),},Var,a,:,X,=,New,X,(,),;,Val,i,:,Float,=,1.233e-1,;,},},<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, 163))

    def test_mixed_6(self):
        inp = """ 
            Class program {
                get() {
                Var a : X =  New X();
                Val i : Float = 1.233e-1;
            }
            Class foo {
                Var $a, b, c : Int = 1, 2, ;
                get() {
                    If(1 == 1) {
                        ForEach(x In 1 .. 100)
                    }
                    ELseif(2 - 1 = 1) {

                    }
                    Else {
                        Var a : X =  New X();
                        Val i : Float = 1.23_3e-1;
                    }
                }
            }
        """
        exp = "Class,program,{,get,(,),{,Var,a,:,X,=,New,X,(,),;,Val,i,:,Float,=,1.233e-1,;,},Class,foo,{,Var,$a,,,b,,,c,:,Int,=,1,,,2,,,;,get,(,),{,If,(,1,==,1,),{,ForEach,(,x,In,1,..,100,),},ELseif,(,2,-,1,=,1,),{,},Else,{,Var,a,:,X,=,New,X,(,),;,Val,i,:,Float,=,1.233e-1,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, 164))

    def test_mixed_7(self):
        inp = """ 
            Class foo {
                Var $a, b, c : Int = 1, 2, ;
                Var $x,y : Int = 1, 2 ;
                Val c, d : Int = 1, 2,3 ;
            }
        """
        exp = "Class,foo,{,Var,$a,,,b,,,c,:,Int,=,1,,,2,,,;,Var,$x,,,y,:,Int,=,1,,,2,;,Val,c,,,d,:,Int,=,1,,,2,,,3,;,},<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, 165))

    def test_mixed_8(self):
        inp = """ 
            Class foo {
                get() {
                             ## New year ##
                             <block statement>
                         If(1 <= 2 && 3 > 4 || 6 < 7 && !True || 1 != 4)
                     }
            }
        """
        exp = "Class,foo,{,get,(,),{,<,block,statement,>,If,(,1,<=,2,&&,3,>,4,||,6,<,7,&&,!,True,||,1,!=,4,),},},<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, 166))

    #TODO Dieu kien String
    # def test_mixed_9(self):
    #     inp = """ 
    #         Class foo {
    #             Var a : Int = New A(a[1][2] % 20 ==. "Floating" ++. New x(1, 2, 3, foo()));
    #         }
    #     """
    #     exp = "Class,foo,{,Var,a,:,Int,=,New,A,(,a,[,1,],[,2,],%,20,==.,Floating,+,+.,New,x,(,1,,,2,,,3,,,foo,(,),),),;,},<EOF>"
    #     self.assertTrue(TestLexer.test(inp, exp, 167))

    def test_mixed_10(self):
        inp = """ 
            Class foo {
                Var a : Int = Self.x() + $a.$10 % _12::_abc2 * _84.a12 - 09 + 0xBN;
            }
        """
        exp = "Class,foo,{,Var,a,:,Int,=,Self,.,x,(,),+,$a,.,$10,%,_12,::,_abc2,*,_84,.,a12,-,0,9,+,0xB,N,;,},<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, 168))

    # Random
    # def test_random_1(self):
    #     inp = """ 
    #         _Ix__EANDoCsd6hBO _zvnSUb4tgkfj02"## == 6"uP6 p3u##i_GfOKsx_rEE */##Fzj"l"##bN9KB3tRM1p_kWtZMjK Ae YFImeKCzTB3M7drVKLzVXrh_9=##"\k930B.6 9##4l"6"=="$sn_ _9/=="-10X8 _0b7036"_QD__
    #     """
    #     exp = "_Ix__EANDoCsd6hBO,_zvnSUb4tgkfj02,## == 6,uP6,p3u,Fzj,l,Illegal Escape In String: \k"
    #     self.assertTrue(TestLexer.test(inp, exp, 169))

    def test_random_2(self):
        inp = """ 
            uYiUuCz_Q xU_####QrvhIYE
        """
        exp = "uYiUuCz_Q,xU_,QrvhIYE,<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, 170))

    # def test_random_3(self):
    #     inp = """ 
    #        "69060+e_dl_fYz##"xq==.$
    #     """
    #     exp = "69060+e_dl_fYz##,xq,==.,Error Token $"
    #     self.assertTrue(TestLexer.test(inp, exp, 171))

    def test_random_4(self):
        inp = """ 
           K e7##==.7"2Q##a FGO"2H%50B6_        """
        exp = "K,e7,a,FGO,Unclosed String: 2H%50B6_        "
        self.assertTrue(TestLexer.test(inp, exp, 172))

    def test_random_5(self):
        inp = """ 
           XjQ e####BU ####KCpJ_EGP_1+==
        """
        exp = "XjQ,e,BU,KCpJ_EGP_1,+,==,<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, 173))

    def test_random_6(self):
        inp = """ 
           20o__e*53 0x0x0b9EE081++
        """
        exp = "20,o__e,*,53,0x0,x0b9EE081,+,+,<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, 174))

    def test_random_7(self):
        inp = """ 
           ei8Fat p Z81qnWy 9IH_6e
        """
        exp = "ei8Fat,p,Z81qnWy,9,IH_6e,<EOF>"
        self.assertTrue(TestLexer.test(inp, exp, 175))

    # def test_random_8(self):
    #     inp = """ 
    #        8a_a_G_P9%120b.E30XyK_ggp_J1-/2.7+##v##.+197##-0==W__3tw
    #     """
    #     exp = """8,a_a_G_P9,%,120,b,.E30,XyK_ggp_J1,-,/,2.7,+,.,+,197,<EOF>"""
    #     self.assertTrue(TestLexer.test(inp, exp, 176))

    # def test_random_9(self):
    #     inp = """ 
    #        /-===."\\tKa9d_cIfe"83d_ybDHicn5ivaUKAPJDvpKJ i+.uF0H1Gb H
    #     """
    #     exp = """/,-,==,=,.,\\tKa9d_cIfe,83,d_ybDHicn5ivaUKAPJDvpKJ,i,+.,uF0H1Gb,H,<EOF>"""
    #     self.assertTrue(TestLexer.test(inp, exp, 177))

    # def test_random_10(self):
    #     inp = """ 
    #        SY##"## "\\16u_##_BT_ZRDr_Wevo_acTI##\\b1eYFl_D0Q7mtLJ##==.pT
    #     """
    #     exp = """SY,Illegal Escape In String: \\1"""
    #     self.assertTrue(TestLexer.test(inp, exp, 178))
