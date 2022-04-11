import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

<<<<<<< HEAD
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
=======
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
    #23
    def test_string_simple(self):
        i = """ "Hi, What is your name?" """
        e = """Hi, What is your name?,<EOF>"""
        self.assertTrue(TestLexer.test(i,e,23))
    #24
    def test_string_with_escape(self):
        i = """ "Lorem \\b Ipsum \\t is \\n simply \\f dummy \\r text \\\ of ' the printing and typesetting industry." """
        e = """Lorem \\b Ipsum \\t is \\n simply \\f dummy \\r text \\\ of ' the printing and typesetting industry.,<EOF>"""
        self.assertTrue(TestLexer.test(i,e,24))
    #25
    def test_string_with_escape_in_python(self):
        i = """ "Lorem \t Ipsum \\t is \\n simply \\f dummy \\r text \\\ of the printing and typesetting industry." """
        e = """Unclosed String: Lorem """
        self.assertTrue(TestLexer.test(i,e,25))
    #26
    def test_string_with_escape_single_quote(self):
        i = """ "Lorem ' Ipsum is simply dummy text of the printing and typesetting industry." """
        e = "Lorem ' Ipsum is simply dummy text of the printing and typesetting industry.,<EOF>"
        self.assertTrue(TestLexer.test(i,e,26))
    #27
    def test_string_with_double_quote(self):
        i = """ "Lorem '" Ipsum is simply dummy text of the printing and typesetting industry." """
        e = """Lorem '" Ipsum is simply dummy text of the printing and typesetting industry.,<EOF>"""
        self.assertTrue(TestLexer.test(i,e,27))
    #28
    def test_string_unclosed(self):
        i = """ "Lorem Ipsum is simply dummy text of the printing and typesetting industry."""
        e = """Unclosed String: Lorem Ipsum is simply dummy text of the printing and typesetting industry."""
        self.assertTrue(TestLexer.test(i,e,28))
    #29
    def test_string_with_double_quote_2(self):
        i = """ "Lorem " Ipsum is simply dummy text of the printing and typesetting industry." """
        e = """Lorem ,Ipsum,is,simply,dummy,text,of,the,printing,and,typesetting,industry,.,Unclosed String:  """
        self.assertTrue(TestLexer.test(i,e,29))
    #30
    def test_string_with_comment_inside(self):
        i = """ "Lorem ## Ipsum is simply ## dummy text of the printing and typesetting industry." """
        e = """Lorem ## Ipsum is simply ## dummy text of the printing and typesetting industry.,<EOF>"""
        self.assertTrue(TestLexer.test(i,e,30))
    #31
    def test_string_illegal_escape(self):
        i = """ "Lorem \\k Ipsum is simply dummy text of the printing and typesetting industry." """
        e = """Illegal Escape In String: Lorem \k"""
        self.assertTrue(TestLexer.test(i,e,31))
    #32
    def test_string_multiple_illegal_escape(self):
        i = """ "Lorem \\s Ipsum \\k is simply dummy text of the printing and typesetting industry." """
        e = """Illegal Escape In String: Lorem \s"""
        self.assertTrue(TestLexer.test(i,e,32))
    #33
    def test_string_with_tab_escape(self):
        i = """ "Lorem       Ipsum is simply        dummy text of the printing \\b \\t \\n \\f \\r ' \\\ and typesetting industry." """
        e = """Lorem       Ipsum is simply        dummy text of the printing \\b \\t \\n \\f \\r ' \\\ and typesetting industry.,<EOF>"""
        self.assertTrue(TestLexer.test(i,e,33))
    #34
    def test_string_all_ascii_char(self):
        i = """ "All ASCII characters here: !'"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'" " """
        e = """All ASCII characters here: !'"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'" ,<EOF>"""
        self.assertTrue(TestLexer.test(i,e,34))
    #35
    def test_string_unclosed_with_escape(self):
        i = """ "Lorem Ipsum is simply dummy text of the \\b \\f \\r \\n \\t ' \\\ printing and typesetting industry."""
        e = """Unclosed String: Lorem Ipsum is simply dummy text of the \\b \\f \\r \\n \\t ' \\\ printing and typesetting industry."""
        self.assertTrue(TestLexer.test(i,e,35))
    #36
    def test_string_unclosed_with_illegal_escape(self):
        i = """ "Lorem Ipsum is simply dummy \\j text of the printing and typesetting industry."""
        e = """Illegal Escape In String: Lorem Ipsum is simply dummy \j"""
        self.assertTrue(TestLexer.test(i,e,36))
    #37
    def test_string_with_double_quote_at_the_end(self):
        i = """ Lorem Ipsum is simply dummy \\j text of the printing and typesetting industry." """
        e = """Lorem,Ipsum,is,simply,dummy,Error Token \\"""
        self.assertTrue(TestLexer.test(i,e,37))
    #38
    def test_string_with_double_quote_at_the_end_2(self):
        i = """ Lorem Ipsum is simply dummy text of the printing and typesetting industry" Sang handsome"""
        e = """Lorem,Ipsum,is,simply,dummy,text,of,the,printing,and,typesetting,industry,Unclosed String:  Sang handsome"""
        self.assertTrue(TestLexer.test(i,e,38))
    #39
    def test_comment_with_expression(self):
        i = "(val1 +. val2 == val3 +. val4) && (v5 + v6 - v7 * v8 / v9 != a[Circle::b]) ## This is a complex expression## fun.foo()"
        e = "(,val1,+.,val2,==,val3,+.,val4,),&&,(,v5,+,v6,-,v7,*,v8,/,v9,!=,a,[,Circle,::,b,],),fun,.,foo,(,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,39))
    #40
    def test_string_unclosed_2(self):
        i = """ "abc \t \f " """
        e = """Unclosed String: abc """
        self.assertTrue(TestLexer.test(i,e,40))
    #41
    def test_indexed_array_int(self):
        i = "Array(1, 5, 7, 12)"
        e = "Array,(,1,,,5,,,7,,,12,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,41))
    #42
    def test_indexed_array_int_long(self):
        i = "Array(1, 5, 7, 12, 0x1232ACF, 0b1011, 01234567, 0, 1,23,9_8_7_65432_1_0, 07_6_5432_1 )"
        e = "Array,(,1,,,5,,,7,,,12,,,0x1232ACF,,,0b1011,,,01234567,,,0,,,1,,,23,,,9876543210,,,07654321,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,42))
    #43
    def test_indexed_array_empty(self):
        i = "Array()"
        e = "Array,(,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,43))
    #44
    def test_indexed_array_boolean(self):
        i = "Array(True, False, False, True)"
        e = "Array,(,True,,,False,,,False,,,True,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,44))
    #45
    def test_indexed_array_string(self):
        i = """Array("a","b","c")"""
        e = "Array,(,a,,,b,,,c,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,45))
    #46
    def test_indexed_array_mixed(self):
        i = """Array(1, 2, 10.e10, "string", "kjshdfh", True, False)"""
        e = "Array,(,1,,,2,,,10.e10,,,string,,,kjshdfh,,,True,,,False,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,46))
    #47
    def test_indexed_array_float(self):
        i = "Array(10.e10, .e+1238, 10.e-191823)"
        e = "Array,(,10.e10,,,.e+1238,,,10.e-191823,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,47))
    #48
    def test_multi_dimentional_array(self):
        i = """Array(Array(1,2,3,4,5), Array(10.10, 10.e10, 23.e-263, -72364.e108))"""
        e = "Array,(,Array,(,1,,,2,,,3,,,4,,,5,),,,Array,(,10.10,,,10.e10,,,23.e-263,,,-,72364.e108,),),<EOF>"
        self.assertTrue(TestLexer.test(i,e,48))
    #49
    def test_multi_dementional_array_2(self):
        i = "Array(Array(Array(1,2,3)), Array(Array()))"
        e = "Array,(,Array,(,Array,(,1,,,2,,,3,),),,,Array,(,Array,(,),),),<EOF>"
        self.assertTrue(TestLexer.test(i,e,49))
    #50
    def test_multi_dimentinal_array_3(self):
        i = """Array (
                Array("Volvo", "22", "18"),
                Array("Saab", "5", "2"),
                Array("Land Rover", "17", "15")
            )"""
        e = "Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>"
        self.assertTrue(TestLexer.test(i,e,50))
    #51
    def test_primitive_type_int(self):
        i = "Int"
        e = "Int,<EOF>"
        self.assertTrue(TestLexer.test(i,e,51))
    #52
    def test_primitive_type_float(self):
        i = "Float"
        e = "Float,<EOF>"
        self.assertTrue(TestLexer.test(i,e,52))
    #53
    def test_primitive_type_Boolean(self):
        i = "Boolean"
        e = "Boolean,<EOF>"
        self.assertTrue(TestLexer.test(i,e,53))
    #54
    def test_boolean_with_operator(self):
        i = "!(2+3) && (val1 == val2) || val3 != val4 "
        e = "!,(,2,+,3,),&&,(,val1,==,val2,),||,val3,!=,val4,<EOF>"
        self.assertTrue(TestLexer.test(i,e,54))
    #55
    def test_int_with_operator(self):
        i = "a = 1 * 2 + 3 / 4; a >= 2; a > 4; a <= 5; a <6 "
        e = "a,=,1,*,2,+,3,/,4,;,a,>=,2,;,a,>,4,;,a,<=,5,;,a,<,6,<EOF>"
        self.assertTrue(TestLexer.test(i,e,55))
    #56
    def test_string_with_operator(self):
        i = """ "Sang" +. "is"+. "handsome" ==. "Sang is handsome" """
        e = "Sang,+.,is,+.,handsome,==.,Sang is handsome,<EOF>"
        self.assertTrue(TestLexer.test(i,e,56))
    #57
    def test_array_type_int(self):
        i = "Var a: Array[Int, 5]"
        e = "Var,a,:,Array,[,Int,,,5,],<EOF>"
        self.assertTrue(TestLexer.test(i,e,57))
    #58
    def test_array_type_float(self):
        i = "Var a: Array[Float, 5]"
        e = "Var,a,:,Array,[,Float,,,5,],<EOF>"
        self.assertTrue(TestLexer.test(i,e,58))
    #59
    def test_array_type_boolean(self):
        i = "Var a: Array[Boolean, 6_18_2_7_6]"
        e = "Var,a,:,Array,[,Boolean,,,618276,],<EOF>"
        self.assertTrue(TestLexer.test(i,e,59))
    #60
    def test_array_type_array(self):
        i = "Var a: Array[Array, 12_23]"
        e = "Var,a,:,Array,[,Array,,,1223,],<EOF>"
        self.assertTrue(TestLexer.test(i,e,60))
    #61
    def test_array_type_string(self):
        i = "Val a, b, c: Array[String, 98_211]"
        e = "Val,a,,,b,,,c,:,Array,[,String,,,98211,],<EOF>"
        self.assertTrue(TestLexer.test(i,e,61))
    #62
    def test_array_element(self):
        i = "a[Point.x][Point.y] a[1+2][123_898][getZ()]"
        e = "a,[,Point,.,x,],[,Point,.,y,],a,[,1,+,2,],[,123898,],[,getZ,(,),],<EOF>"
        self.assertTrue(TestLexer.test(i,e,62))
    #63
    def test_class_type(self):
        i = "Var a: A = New A()"
        e = "Var,a,:,A,=,New,A,(,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,63))
    #64
    def test_class_type_2(self):
        i = """Var x: X = New X(1 + 3_72, 3*Shape::$a, "Hello")"""
        e = "Var,x,:,X,=,New,X,(,1,+,372,,,3,*,Shape,::,$a,,,Hello,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,64))
    #65
    def test_class_type_3(self):
        i = "Var $a, $a2, a3, a4, $a5: X = New X()"
        e = "Var,$a,,,$a2,,,a3,,,a4,,,$a5,:,X,=,New,X,(,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,65))
    #66
    def test_expression_alrithmetic_operator(self):
        i = "1_000 + 2_000 - _3x * 4_000 / 5 + 2 % 5 "
        e = "1000,+,2000,-,_3x,*,4000,/,5,+,2,%,5,<EOF>"
        self.assertTrue(TestLexer.test(i,e,66))
    #67
    def test_expression_boolean_operator(self):
        i = "20 // \ && || "
        e = "20,/,/,Error Token \\"
        self.assertTrue(TestLexer.test(i,e,67))
    #68
    def test_expression_string_operator(self):
        i = """ "I want 10" +. "In this assignment """
        e = """I want 10,+.,Unclosed String: In this assignment """
        self.assertTrue(TestLexer.test(i,e,68))
    #69
    def test_expression_string_operator_2(self):
        i = """ "I want 10" ==. "In this assignment" """
        e = """I want 10,==.,In this assignment,<EOF>"""
        self.assertTrue(TestLexer.test(i,e,69))
    #70
    def test_expression_relational_operator(self):
        i = " 1 == 2 != 3 < 4 > 5 <= 6 >= 7"
        e = "1,==,2,!=,3,<,4,>,5,<=,6,>=,7,<EOF>"
        self.assertTrue(TestLexer.test(i,e,70))
    #71
    def test_expression_index_operator(self):
        i = "Val a = getShape()[1][2-3]"
        e = "Val,a,=,getShape,(,),[,1,],[,2,-,3,],<EOF>"
        self.assertTrue(TestLexer.test(i,e,71))
    #72
    def test_expression_member_access(self):
        i = "getAClass().value \\"
        e = "getAClass,(,),.,value,Error Token \\"
        self.assertTrue(TestLexer.test(i,e,72))
    #73
    def test_expression_static_attribute_access(self):
        i = "Car::$speed"
        e = "Car,::,$speed,<EOF>"
        self.assertTrue(TestLexer.test(i,e,73))
    #74
    def test_expression_instance_method_invocation(self):
        i = "TenScoreObject.calculateScore(10,9,8)"
        e = "TenScoreObject,.,calculateScore,(,10,,,9,,,8,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,74))
    #75
    def test_expression_static_method_invocation(self):
        i = "Shape::$draw(radius, 10_000)"
        e = "Shape,::,$draw,(,radius,,,10000,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,75))
    #76
    def test_expression_self(self):
        i = "Return Self.x + Self.y + 20_000"
        e = "Return,Self,.,x,+,Self,.,y,+,20000,<EOF>"
        self.assertTrue(TestLexer.test(i,e,76))
    #77
    def test_assignment_statement(self):
        i = "a = 500_000;"
        e = "a,=,500000,;,<EOF>"
        self.assertTrue(TestLexer.test(i,e,77))
    #78
    def test_if_statement(self):
        i = """
            If (a[1 + OOP.getX()] == False){
                If (a + 2 = b){
                    Return True;
                }
                Elseif( a == b){
                    Return False;
                }
            }Else{
                print("Hong be oi, em khong follow anh ma em doi xin in4 cua anh");
            }

            """
        e = "If,(,a,[,1,+,OOP,.,getX,(,),],==,False,),{,If,(,a,+,2,=,b,),{,Return,True,;,},Elseif,(,a,==,b,),{,Return,False,;,},},Else,{,print,(,Hong be oi, em khong follow anh ma em doi xin in4 cua anh,),;,},<EOF>"
        self.assertTrue(TestLexer.test(i,e,78))
    #79
    def test_for_in_statement(self):
        i = """
                Foreach (i In 1_000 .. 100_000 By (a*b)) {
                    Out.printInt(i);
                }
                Foreach (x In 5 .. 2) {
                    Out.printInt(arr[x]);
                }

        """
        e = "Foreach,(,i,In,1000,..,100000,By,(,a,*,b,),),{,Out,.,printInt,(,i,),;,},Foreach,(,x,In,5,..,2,),{,Out,.,printInt,(,arr,[,x,],),;,},<EOF>"
        self.assertTrue(TestLexer.test(i,e,79))
    #80
    def test_break_statement(self):
        i = "Break;"
        e = "Break,;,<EOF>"
        self.assertTrue(TestLexer.test(i,e,80))
    #81
    def test_string_random_with_newline(self):
        i = """
            "My string

            Hello"
        """
        e = "Unclosed String: My string"
        self.assertTrue(TestLexer.test(i,e,81))
    #82
    def test_continue_statement(self):
        i = "Continue;"
        e = "Continue,;,<EOF>"
        self.assertTrue(TestLexer.test(i,e,82))
    #83
    def test_return_statement(self):
        i = "Return x.getX(10000)"
        e = "Return,x,.,getX,(,10000,),<EOF>"
        self.assertTrue(TestLexer.test(i,e,83))
    #84
    def test_method_invocation_statement(self):
        i = "Shape::$getNumOfShape(count);"
        e = "Shape,::,$getNumOfShape,(,count,),;,<EOF>"
        self.assertTrue(TestLexer.test(i,e,84))
    #85
    def test_random(self):
        i = """
            Class S{
                Val a: Int = 1_111_111;
                print("Every moment is a opportunity");
            }
        """
        e = "Class,S,{,Val,a,:,Int,=,1111111,;,print,(,Every moment is a opportunity,),;,},<EOF>"
        self.assertTrue(TestLexer.test(i,e,85))
    #86
    def test_random_1(self):
        i = "00000hkajhf9827364ljsbdb'p]W0JLJDHF283079PHNDVHALKD;AF"
        e = "00,00,0,hkajhf9827364ljsbdb,Error Token '"
        self.assertTrue(TestLexer.test(i,e,86))
    #87
    def test_random_2(self):
        i = "         abc\\sj\\ksdh"
        e = "abc,Error Token \\"
        self.assertTrue(TestLexer.test(i,e,87))
    #88
    def test_random_3(self):
        i = """ .//. "sang"  """
        e = ".,/,/,.,sang,<EOF>"
        self.assertTrue(TestLexer.test(i,e,88))
    #89
    def test_random_4(self):
        i = "000x0000123484567 10.e29hs-o28+jf"
        e = "00,0x0,00,01234,84567,10.e29,hs,-,o28,+,jf,<EOF>"
        self.assertTrue(TestLexer.test(i,e,89))
    #90
    def test_random_5(self):
        i = "_a.doo := (a>b)<=c;"
        e = "_a,.,doo,:,=,(,a,>,b,),<=,c,;,<EOF>"
        self.assertTrue(TestLexer.test(i,e,90))
    #91
    def test_random_6(self):
        i = "23456789098trewertyuklkjhgfxcvbnm0987654567890xcg987u"
        e = "23456789098,trewertyuklkjhgfxcvbnm0987654567890xcg987u,<EOF>"
        self.assertTrue(TestLexer.test(i,e,91))
    #92
    def test_random_comment(self):
        i = """
        ## Line 1

            Line 2 \\n \\
        """
        e = "Error Token #"
        self.assertTrue(TestLexer.test(i,e,92))
    #93
    def test_random_comment_1(self):
        i = """
                ## Line 1

                    Line 2 \\n \\
                ##
                """
        e = "<EOF>"
        self.assertTrue(TestLexer.test(i,e,93))
    #94
    def test_random_7(self):
        i = "00000000xxxxx001111000110bbbc0001111"
        e = "00,00,00,00,xxxxx001111000110bbbc0001111,<EOF>"
        self.assertTrue(TestLexer.test(i,e,94))
    #95
    def test_random_8(self):
        i = "123.4E+5677238 12123.4e+5678 123.4123E-5678 12233.4e-561378"
        e = "123.4E+5677238,12123.4e+5678,123.4123E-5678,12233.4e-561378,<EOF>"
        self.assertTrue(TestLexer.test(i,e,95))
    #96
    def test_random_9(self):
        i = """
        Val a, $b, $c: Int = 1 + 2, 1+3, 23-9;
        ## This will be skipped ##

        """
        e = "Val,a,,,$b,,,$c,:,Int,=,1,+,2,,,1,+,3,,,23,-,9,;,<EOF>"
        self.assertTrue(TestLexer.test(i,e,96))
    #97
    def test_random_10(self):
        i = """
            Val a, $b, $c: Int = 1 + 2, 1+3, 23-9;
            ## This will be skipped ##
            Hello(a[i+7]);
            ## This also ##

        """
        e = "Val,a,,,$b,,,$c,:,Int,=,1,+,2,,,1,+,3,,,23,-,9,;,Hello,(,a,[,i,+,7,],),;,<EOF>"
        self.assertTrue(TestLexer.test(i,e,97))
    #98
    def test_random_11(self):
        i = "0x0x00x0x0x0x00x0x0x0b0b0b0z0x0x0x0______0090901101100022230"
        e = "0x0,x00x0x0x0x00x0x0x0b0b0b0z0x0x0x0______0090901101100022230,<EOF>"
        self.assertTrue(TestLexer.test(i,e,98))
    #99
    def test_random_12(self):
        i = ""
        e = "<EOF>"
        self.assertTrue(TestLexer.test(i,e,99))
    #100
    def test_final(self):
        i = "All parameters/variables declared in the body block have the method scope"
        e = "All,parameters,/,variables,declared,in,the,body,block,have,the,method,scope,<EOF>"
        self.assertTrue(TestLexer.test(i,e,100))



>>>>>>> develop
