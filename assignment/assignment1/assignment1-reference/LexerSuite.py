import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_1(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "" """, """,<EOF>""", 101))

    def test_2(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ " " """, """ ,<EOF>""", 102))

    def test_3(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\"\'" """, """,Error Token \'""", 103))

    def test_4(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\t" """, """\t,<EOF>""", 104))

    def test_5(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\\r" """, """\\r,<EOF>""", 105))

    def test_6(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\f" """, """\f,<EOF>""", 106))

    def test_7(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\b" """, """\b,<EOF>""", 107))

    def test_8(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\n" """, """Unclosed String: \n""", 108))

    def test_9(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\n\t\\\b\r\f" """, """Unclosed String: \n""", 109))

    def test_10(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "00" """, """00,<EOF>""", 110))

    def test_11(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "This is a string \\0" """, """Illegal Escape In String: This is a string \\0""", 111))

    def test_12(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\t8\t" """, """\t8\t,<EOF>""", 112))

    def test_13(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "123 ** comment **" """, """123 ** comment **,<EOF>""", 113))

    def test_14(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "ErrorToken" """, """ErrorToken,<EOF>""", 114))

    def test_15(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "He asked me: \'\"Where is John?\'\"" """, """He asked me: \'\"Where is John?\'\",<EOF>""", 115))

    def test_16(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "this is a very very very very very very very very very very long string" """, """this is a very very very very very very very very very very long string,<EOF>""", 116))

    def test_17(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "int float string if else return for do while true false" """, """int float string if else return for do while true false,<EOF>""", 117))

    def test_18(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "float-of-string" """, """float-of-string,<EOF>""", 118))

    def test_19(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "Unclosed String: \"" """, """Unclosed String: ,Unclosed String:  """, 119))

    def test_20(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\"\"" """, """,,<EOF>""", 120))

    def test_21(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ """" """, """<EOF>""", 121))

    def test_22(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "this is a very very very very very very very very very very long string" """, """this is a very very very very very very very very very very long string,<EOF>""", 122))

    def test_23(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "This is a string containing tab \t" """, """This is a string containing tab \t,<EOF>""", 123))

    def test_24(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "()[]:.,;{}" """, """()[]:.,;{},<EOF>""", 124))

    def test_25(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "`" """, """`,<EOF>""", 125))

    def test_26(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """ \\a """, """\,a,<EOF>""", 126))

    def test_27(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """True""", """True,<EOF>""", 127))

    def test_28(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """abc""", """abc,<EOF>""", 128))

    def test_29(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """00""", """0,0,<EOF>""", 129))

    def test_30(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """00 01""", """0,0,0,1,<EOF>""", 130))

    def test_31(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """0O77""", """0O77,<EOF>""", 131))

    def test_32(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """0o77""", """0o77,<EOF>""", 132))

    def test_33(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """-0X1234""", """-,0X1234,<EOF>""", 133))

    def test_34(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """-0x1234""", """-,0x1234,<EOF>""", 134))

    def test_35(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """10.e3""", """10.e3,<EOF>""", 135))

    def test_36(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """10e3""", """10e3,<EOF>""", 136))

    def test_37(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """0.01E-10""", """0.01E-10,<EOF>""", 137))

    def test_38(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """.1e""", """.,1,e,<EOF>""", 138))

    def test_39(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """1.23E-121""", """1.23E-121,<EOF>""", 139))

    def test_40(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """123 E - 123""", """123,Error Token E""", 140))

    def test_41(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """.1 .2 .3""", """.,1,.,2,.,3,<EOF>""", 141))

    def test_42(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """- 123E-1""", """-,123E-1,<EOF>""", 142))

    def test_43(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """0a""", """0,a,<EOF>""", 143))

    def test_44(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """-2637""", """-,2637,<EOF>""", 144))

    def test_45(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """EndWhileFor""", """EndWhile,For,<EOF>""", 145))

    def test_46(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """bool""", """bool,<EOF>""", 146))

    def test_47(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """If""", """If,<EOF>""", 147))

    def test_48(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """int""", """int,<EOF>""", 148))

    def test_49(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """Float""", """Error Token F""", 149))

    def test_50(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """string""", """string,<EOF>""", 150))

    def test_51(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """if""", """if,<EOF>""", 151))

    def test_52(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """else""", """else,<EOF>""", 152))

    def test_53(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """float_of_string""", """float_of_string,<EOF>""", 153))

    def test_54(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """for""", """for,<EOF>""", 154))

    def test_55(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """EOF""", """Error Token E""", 155))

    def test_56(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """int i, j, k = 10;""", """int,i,,,j,,,k,=,10,;,<EOF>""", 156))

    def test_57(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """boolean a[2]={false, false}; ** array declaration **""", """boolean,a,[,2,],=,{,false,,,false,},;,<EOF>""", 157))

    def test_58(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """v = (4. \. 3.)*.3.14""", """v,=,(,4.,\.,3.,),*.,3.14,<EOF>""", 158))

    def test_59(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """== != < <= >= > =/= <. >. <=. >=.""", """==,!=,<,<=,>=,>,=/=,<.,>.,<=.,>=.,<EOF>""", 159))

    def test_60(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """abc""", """abc,<EOF>""", 160))

    def test_61(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """tOkEn""", """tOkEn,<EOF>""", 161))

    def test_62(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """tOKEn1""", """tOKEn1,<EOF>""", 162))

    def test_63(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """_id""", """Error Token _""", 163))

    def test_64(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """id_""", """id_,<EOF>""", 164))

    def test_65(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """abc123_123abc__""", """abc123_123abc__,<EOF>""", 165))

    def test_66(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """var: identifier""", """var,:,identifier,<EOF>""", 166))

    def test_67(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """classA :: classB""", """classA,:,:,classB,<EOF>""", 167))

    def test_68(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""*p""", """*,p,<EOF>""", 168))

    def test_69(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """a--""", """a,-,-,<EOF>""", 169))

    def test_70(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """a++""", """a,+,+,<EOF>""", 170))

    def test_71(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """a && b == 1""", """a,&&,b,==,1,<EOF>""", 171))

    def test_72(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """a == 1""", """a,==,1,<EOF>""", 172))

    def test_73(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """a != 1""", """a,!=,1,<EOF>""", 173))

    def test_74(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """a >= b""", """a,>=,b,<EOF>""", 174))

    def test_75(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """a >=. b""", """a,>=.,b,<EOF>""", 175))

    def test_76(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """a =/= b""", """a,=/=,b,<EOF>""", 176))

    def test_77(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """foo(a)[x*y] = b[c[9]]+11;""", """foo,(,a,),[,x,*,y,],=,b,[,c,[,9,],],+,11,;,<EOF>""", 177))

    def test_78(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""abc""", """abc,<EOF>""", 178))

    def test_79(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """int foo(double n[80]) {""", """int,foo,(,double,n,[,80,],),{,<EOF>""", 179))

    def test_80(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """|""", """Error Token |""", 180))

    def test_81(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """?""", """Error Token ?""", 181))

    def test_82(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """~""", """Error Token ~""", 182))

    def test_83(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """@""", """Error Token @""", 183))

    def test_84(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """#""", """Error Token #""", 184))

    def test_85(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            """$""", """Error Token $""", 185))

    def test_86(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(
            """{1, 2.3, True}""", """{,1,,,2.3,,,True,},<EOF>""", 186))

    def test_87(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(
            """{""", """""", 187))

    def test_88(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(
            """""", """""", 188))

    def test_89(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(
            """""", """""", 189))

    def test_90(self):
        """"test array"""
        self.assertTrue(TestLexer.checkLexeme(
            """""", """""", 190))

    def test_91(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme("""{1,2,3,4}""", """{1,2,3,4},<EOF>""", 191))

    def test_92(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(
            """{\"a\", \"b\", \"c\"}""", """{\"a\", \"b\", \"c\"},<EOF>""", 192))

    def test_93(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(
            """{True,False,True,False}""", """{True,False,True,False},<EOF>""", 193))

    def test_94(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(
            """{0.2,10e2,77.1,12e2}""", """{0.2,10e2,77.1,12e2},<EOF>""", 194))

    def test_95(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme("""abc""", """abc,<EOF>""", 195))

    def test_96(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme("""abc""", """abc,<EOF>""", 196))

    def test_97(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""abc""", """abc,<EOF>""", 197))

    def test_98(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""abc""", """abc,<EOF>""", 198))

    def test_99(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""abc""", """abc,<EOF>""", 199))

    def test_100(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""abc""", """abc,<EOF>""", 200))
