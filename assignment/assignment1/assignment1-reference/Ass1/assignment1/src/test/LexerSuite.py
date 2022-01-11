import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_1(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("""000""","""0,0,0,<EOF>""",101))

    def test_2(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("""-1852717""","""-,1852717,<EOF>""",102))

    def test_3(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("""0x0812A""","""0,x0812A,<EOF>""",103))

    def test_4(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("""0XA012""","""0XA012,<EOF>""",104))

    def test_5(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("""0oA12""","""0,oA12,<EOF>""",105))

    def test_6(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("""0O12""","""0O12,<EOF>""",106))
    
    def test_7(self):
        self.assertTrue(TestLexer.checkLexeme("""0o12A""","""0o12,Error Token A""",107))

    def test_8(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("""0xHE12""","""0,xHE12,<EOF>""",108))

    def test_9(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("""0O12OA""","""0O12,Error Token O""",109))

    def test_10(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("""0XA17 001 0O00""","""0XA17,0,0,1,0,Error Token O""",110))

    def test_11(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("""If(a=2) ThenWhile (a=2) Do a++ Else Return function(a,b)""","""If,(,a,=,2,),Then,While,(,a,=,2,),Do,a,+,+,Else,Return,function,(,a,,,b,),<EOF>""",111))

    def test_12(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("""returnabc WhileA==2""","""returnabc,While,Error Token A""",112))

    def test_13(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("""For(a=0;a<0x2AF;a++)Returna=0o101""","""For,(,a,=,0,;,a,<,0x2AF,;,a,+,+,),Return,a,=,0o101,<EOF>""",113))

    def test_14(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme("""int a[2][3]=b*c[d[12]]-add(12,13)""","""int,a,[,2,],[,3,],=,b,*,c,[,d,[,12,],],-,add,(,12,,,13,),<EOF>""",114))

    def test_15(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme("""Body{a=2;b.node=foo();}A""","""Body,{,a,=,2,;,b,.,node,=,foo,(,),;,},Error Token A""",115))

    def test_16(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("""If(2>=.2.0e12)Return 2=/=3""","""If,(,2,>=.,2.0e12,),Return,2,=/=,3,<EOF>""",116))

    def test_17(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("""a+.-12e-13%23\.0.12*3""","""a,+.,-,12e-13,%,23,\.,0.12,*,3,<EOF>""",117))

    def test_18(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("""While(a&&b;c||d;!e)DoReturna+b-C*.2.12""","""While,(,a,&&,b,;,c,||,d,;,!,e,),Do,Return,a,+,b,-,Error Token C""",118))

    def test_19(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(""".+..*\*.-.\.===>><<=.=/=""",""".,+.,.,*,\,*.,-.,\.,==,=,>,>,<,<=.,=/=,<EOF>""",119))

    def test_20(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("""* .>and.-. While == && !C Do Return 1 || 2""","""*,.,>,and,.,-.,While,==,&&,!,Error Token C""",120))

    def test_21(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("""-12.0e3""","""-,12.0e3,<EOF>""",121))

    def test_22(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("""-0.0001E-123""","""-,0.0001E-123,<EOF>""",122))

    def test_23(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("""1291 10100e+123-12""","""1291,10100e+123,-,12,<EOF>""",123))

    def test_24(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("""0012+E-123""","""0,0,12,+,Error Token E""",124))

    def test_25(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("""e-132e+002""","""e,-,132e+002,<EOF>""",125))

    def test_26(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("""100.0012E-12.0e31""","""100.0012E-12,.,0e31,<EOF>""",126))

    def test_27(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("""0.123.E123-12""","""0.123,.,Error Token E""",127))

    def test_28(self):
        """test boolean"""
        self.assertTrue(TestLexer.checkLexeme("""If(a==2) let True = -1||2 Else returnfalse""","""If,(,a,==,2,),let,True,=,-,1,||,2,Else,returnfalse,<EOF>""",128))
    
    def test_29(self):
        """test boolean"""
        self.assertTrue(TestLexer.checkLexeme("""a=c Whileb==FALSE""","""a,=,c,While,b,==,Error Token F""",129))

    def test_30(self):
        """test boolean"""
        self.assertTrue(TestLexer.checkLexeme("""trueABC FalseABC""","""trueABC,False,Error Token A""",130))

    def test_31(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("""empty string: ""  "This is not empty" ""","""empty,string,:,,This is not empty,<EOF>""",131))

    def test_32(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Nhan is my friend" ""","""Nhan is my friend,<EOF>""",132))

    def test_33(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \t" ""","""This is a string containing tab \t,<EOF>""",133))

    def test_34(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("""  "He asked me: '"Where is John?'""  ""","""He asked me: '"Where is John?'",<EOF>""",134))

    def test_35(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "He like me.\b but he dont want to say it.\t I really dont know why?\f" ""","""He like me.\b but he dont want to say it.\t I really dont know why?\f,<EOF>""",135))

    def test_36(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Not error" Error ""","""Not error,Error Token E""",136))

    def test_37(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Free space in string" can not free space here ""","""Free space in string,can,not,free,space,here,<EOF>""",137))

    def test_38(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("""escape not in string: \b ""","""escape,not,in,string,:,Error Token \b""",138))

    def test_39(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("""escape in string: "bold\b horizontalTab\t cr\\r formFeed\f"  ""","""escape,in,string,:,bold\b horizontalTab\t cr\\r formFeed\f,<EOF>""",139))

    def test_40(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme("""this is a string: "I said '"It is a string, right\b'"". this is not: this is not a string ""","""this,is,a,string,:,I said '"It is a string, right\b'",.,this,is,not,:,this,is,not,a,string,<EOF>""",140))

    def test_41(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""numOfStudent maxTeacherInClass has_prerequesite check_medicine ""","""numOfStudent,maxTeacherInClass,has_prerequesite,check_medicine,<EOF>""",141))

    def test_42(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""1ditgitInAlphabet has2Letter has_2litter""","""1,ditgitInAlphabet,has2Letter,has_2litter,<EOF>""",142))

    def test_43(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""check_letter _not_good""","""check_letter,Error Token _""",143))

    def test_44(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""1_studentInClass""","""1,Error Token _""",144))

    def test_45(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("""DoNotUnderstand""","""Do,Error Token N""",145))

    def test_46(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme("""{2,4,1,2}""","""{,2,,,4,,,1,,,2,},<EOF>""",146))

    def test_47(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme("""{{1,2},{"a","ab"},{True,False},{2.012,2.01e-13}}""","""{,{,1,,,2,},,,{,a,,,ab,},,,{,True,,,False,},,,{,2.012,,,2.01e-13,},},<EOF>""",147))

    def test_48(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Array of different type: " {1,True,"abc",2.03e12}""","""Array of different type: ,{,1,,,True,,,abc,,,2.03e12,},<EOF>""",148))

    def test_49(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Wrong array literal" {{{{} ""","""Wrong array literal,{,{,{,{,},<EOF>""",149))

    def test_50(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme("""{{1},{2},{3}}""","""{,{,1,},,,{,2,},,,{,3,},},<EOF>""",150))

    def test_51(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Forgot comma:" {{1,2}3{4,5}} ""","""Forgot comma:,{,{,1,,,2,},3,{,4,,,5,},},<EOF>""",151))

    def test_52(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Error in array element: " {{1,2},{A,B}} ""","""Error in array element: ,{,{,1,,,2,},,,{,Error Token A""",152))

    def test_53(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Empty array: " {} ""","""Empty array: ,{,},<EOF>""",153))

    def test_54(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Nested empty array inside array: " {{{{}}}} ""","""Nested empty array inside array: ,{,{,{,{,},},},},<EOF>""",154))

    def test_55(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Space, tab inside array: " {    1     } ""","""Space, tab inside array: ,{,1,},<EOF>""",155))

    def test_56(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Space, tab inside array: " {    1   , 2,     12  } ""","""Space, tab inside array: ,{,1,,,2,,,12,},<EOF>""",156))

    def test_57(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Space, tab inside array: " { { 1  ,  2},  {  },{"a","b"}} ""","""Space, tab inside array: ,{,{,1,,,2,},,,{,},,,{,a,,,b,},},<EOF>""",157))

    def test_58(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" {\"a\", \"b\", \"c\"} ""","""{,a,,,b,,,c,},<EOF>""",158))

    def test_59(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Int Array: " {0,120,0xBA12,0O71} ""","""Int Array: ,{,0,,,120,,,0xBA12,,,0O71,},<EOF>""",159))

    def test_60(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Float Array: " {2.012,001.2E-12,12000.,021E20} ""","""Float Array: ,{,2.012,,,001.2E-12,,,12000.,,,021E20,},<EOF>""",160))

    def test_61(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Boolean Array: " {True,False,False,True} ""","""Boolean Array: ,{,True,,,False,,,False,,,True,},<EOF>""",161))

    def test_62(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "String Array: " {"First String\\b","Second String\\f","Third String\\r"} ""","""String Array: ,{,First String\\b,,,Second String\\f,,,Third String\\r,},<EOF>""",162))

    def test_63(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Nested Array: " {{1,  2,1} , {"A", "B",    "C"},   {True,False},{}} ""","""Nested Array: ,{,{,1,,,2,,,1,},,,{,A,,,B,,,C,},,,{,True,,,False,},,,{,},},<EOF>""",163))

    def test_64(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Nested Array: " {{{2,3},{"a","C"}},{},{{},{}},{True,False}} ""","""Nested Array: ,{,{,{,2,,,3,},,,{,a,,,C,},},,,{,},,,{,{,},,,{,},},,,{,True,,,False,},},<EOF>""",164))

    def test_65(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Wrong element type inside array: " {{{True,False},False},{},{2,2.3}} ""","""Wrong element type inside array: ,{,{,{,True,,,False,},,,False,},,,{,},,,{,2,,,2.3,},},<EOF>""",165))

    def test_66(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Array of Keyword: " {{{Do, While},{Return}},{For}, {Var,Else},{{If}}} ""","""Array of Keyword: ,{,{,{,Do,,,While,},,,{,Return,},},,,{,For,},,,{,Var,,,Else,},,,{,{,If,},},},<EOF>""",166))

    def test_67(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Int exceptions: " {0012, 00013, 000} ""","""Int exceptions: ,{,0,0,12,,,0,0,0,13,,,0,0,0,},<EOF>""",167))

    def test_68(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Number of '"{'" not equal '"}'": " {{1,2}}}{{{},{}} ""","""Number of '"{'" not equal '"}'": ,{,{,1,,,2,},},},{,{,{,},,,{,},},<EOF>""",168))

    def test_69(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("""
            "Multiline Comment: "
            ** This is a multiline comment
            * line 1
            * line 2
            **    
        ""","""Multiline Comment: ,<EOF>""",169))

    def test_70(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("""
        "Multiline Comment: "
        ** This is another multiline comment
        line 1
        line 2
        **
        ""","""Multiline Comment: ,<EOF>""",170))

    def test_71(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("""this is single line comment: ** This will not be read ** ""","""this,is,single,line,comment,:,<EOF>""",171))

    def test_72(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(""" "This comment is in the string: ** This is a string not a comment **" ""","""This comment is in the string: ** This is a string not a comment **,<EOF>""",172))

    def test_73(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(""" ** This is a single-line comment. ** ""","""<EOF>""",173))

    def test_74(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(""" "This will not be read either:" ** \t\b\a\s\c\a\s\n *+- ** ""","""This will not be read either:,<EOF>""",174))

    def test_75(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(""" ** "Sorry string still not be read in here" ** ""","""<EOF>""",175))

    def test_76(self):
        """test ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("""basic error: Error""","""basic,error,:,Error Token E""",176))

    def test_77(self):
        """test ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("""wrong identifiers: _1list""","""wrong,identifiers,:,Error Token _""",177))

    def test_78(self):
        """test ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme(""" "Wrong identifiers after keyword" Return~a ""","""Wrong identifiers after keyword,Return,Error Token ~""",178))

    def test_79(self):
        """test ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme(""" "Not included operator:" / ""","""Not included operator:,Error Token /""",179))

    def test_80(self):
        """test ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme(""" "Not included operator:" ? ""","""Not included operator:,Error Token ?""",180))

    def test_81(self):
        """test ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" " \ " ""","""Illegal Escape In String:  \ """,181))

    def test_82(self):
        """test ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "I am the winner\ aaaa" ""","""Illegal Escape In String: I am the winner\ """,182))

    def test_83(self):
        """test ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def\a" ""","""Illegal Escape In String: abc\\h""",183))

    def test_84(self):
        """test ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" " If (a == 2) \\t b = 2 \\b c = 3 \\a" ""","""Illegal Escape In String:  If (a == 2) \\t b = 2 \\b c = 3 \\a""",184))

    def test_85(self):
        """test ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\\\\a \\a" ""","""Illegal Escape In String: abcd\\\\a \\a""",185))

    def test_86(self):
        """test UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "This is an unclosed string ""","""Unclosed String: This is an unclosed string """,186))

    def test_87(self):
        """test UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "There is a single quote '" ""","""Unclosed String: There is a single quote '" """,187))

    def test_88(self):
        """test UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" " ""","""Unclosed String:  """,188))

    def test_89(self):
        """test UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "Forgot single quote before double quote: '"Here is it" " ""","""Forgot single quote before double quote: '"Here is it,Unclosed String:  """,189))

    def test_90(self):
        """test UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "\nabc" ""","""Unclosed String: \n\n""",190))

    def test_91(self):
        """test UNTERMINATED_COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" ** this comment is error ""","""Unterminated Comment""",191))

    def test_92(self):
        """test UNTERMINATED_COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" ** where is my end comment abc* ""","""Unterminated Comment""",192))

    def test_93(self):
        """test UNTERMINATED_COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" "So many comments: " ********** ""","""So many comments: ,Unterminated Comment""",193))

    def test_94(self):
        """test UNTERMINATED_COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" "Multiline comments: " 
        ** This is a multiline comment
        * Line 1
        * Line 2
        Oups only 1 star at the end
        *
        ""","""Multiline comments: ,Unterminated Comment""",194))

    def test_95(self):
        """test UNTERMINATED_COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" ** No double star appear to create unterminated comment error * *, *a*, a*,* *\*/* *aa*1* ""","""Unterminated Comment""",195))

    def test_96(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme(""" "Let\\'s create some combination: " Var a = 0xAF13, If (b = {{"Abc","Def"},{},{True}}) Return 02.00e-14 ** Still a float ** ""","""Let\\'s create some combination: ,Var,a,=,0xAF13,,,If,(,b,=,{,{,Abc,,,Def,},,,{,},,,{,True,},},),Return,02.00e-14,<EOF>""",196))

    def test_97(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme(""" "Let\\'s see some common mistake: " int b = {{},{2,{"ABC","h"}},True} ** Element is not the same type in array ** If(a=b)thenReturnTrue ** Misunderstand string and keyword ** bool a = true ** Wrong letter t **""","""Let\\'s see some common mistake: ,int,b,=,{,{,},,,{,2,,,{,ABC,,,h,},},,,True,},If,(,a,=,b,),thenReturnTrue,bool,a,=,true,<EOF>""",197))

    def test_98(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme(""" ** Empty ** ""","""<EOF>""",198))

    def test_99(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme(""" \n ""","""<EOF>""",199))

    def test_100(self):
        """test all"""
        self.assertTrue(TestLexer.checkLexeme(""" "End of Lexer Test-case. I try my best to figure out all the possible test-case. Thanks for reading" ""","""End of Lexer Test-case. I try my best to figure out all the possible test-case. Thanks for reading,<EOF>""",200))



