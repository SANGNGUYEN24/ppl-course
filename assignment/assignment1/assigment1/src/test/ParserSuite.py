import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    #101
    def test_simple_class(self):
        i = "Class A{}"
        e = "successful"
        self.assertTrue(TestParser.test(i,e,101))
    #102
    def test_simple_class_missing_bracket(self):
        i = "Class B{"
        e = "Error on line 1 col 8: <EOF>"
        self.assertTrue(TestParser.test(i,e,102))
    #103
    def test_simple_class_with_superclass(self):
        i = "Class Car : Vehicle{}"
        e = "successful"
        self.assertTrue(TestParser.test(i,e,103))
    #104
    def test_class_with_attribute_declaration_missing_assign_expr(self):
        i = """
            ## Define class Car ##
            Class Car : Vehicle{
                Val speed: Float = 0;
                Val $model, tireNum: Int;
            }
            
        """
        e = "Error on line 5 col 40: ;"
        self.assertTrue(TestParser.test(i,e,104))
    #105
    def test_class_with_attribute_declaration(self):
        i = """
                    ## Define class Car ##
                    Class Car : Vehicle{
                        Val speed: Float = 0;
                        Val $model, tireNum: Int = 1 * 3 + 4 - 4 / 100_000;
                    }

            """
        e = "successful"
        self.assertTrue(TestParser.test(i,e,105))
    #106
    def test_method_declaration(self):
        i = """
            Class Adam{
            getSpeed(a, b, c, $d: Int){}
            }            
            """
        e = "Error on line 3 col 30: $d"
        self.assertTrue(TestParser.test(i,e,106))
    #107
    def test_method_declaration_with_body(self):
        i = """
            Class Eva{
                getSpeed(a, b, c: Int; d, e: String){
                    print("speed is: " +.  "20km/h");
                }
            }
            """
        e = "successful"
        self.assertTrue(TestParser.test(i,e,107))
    #108
    def test_class_named_main(self):
        i = "Class main{}"
        e = "successful"
        self.assertTrue(TestParser.test(i,e,108))
    #109
    def test_attribute_decl_primitive_type(self):
        i = """
            Class Eva{
                Val a, b, __b: Boolean: True, False, !True;
                Var aa, be, $ce, de: Float = 978.063e129, 8_7_6_2.029e99, 98_1.23e-10
            }
            """
        e = "Error on line 3 col 38: :"
        self.assertTrue(TestParser.test(i,e,109))
    #110
    def test_attribute_decl_primitive_type_2(self):
        i = """
            Class Eva{
                Val a, b, __b: Boolean = True, False, !True;
                Var aa, be, $ce, de: Float = 978.063e129, 8_7_6_2.029e99, 98_1.23e-10
            }
            """
        e = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(i,e,110))
    #111
    def test_attribute_decl_primitive_type_3(self):
        i = """
            Class Eva{
                Val a, b, __b: Boolean = True, False, !True;
                Var aa, be, $ce, de: Float = 978.063e129, 8_7_6_2.029e99, 98_1.23e-10
            }
            """
        e = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(i,e,111))
    #112
    def test_attribute_decl_primitive_type_4(self):
        i = """
                Class Eva{
                    Val a, b, __b: Boolean = True, False, !True;
                    Var aa, be, $ce, de: Float = 978.063e129, 8_7_6_2.029e99, 98_1.23e-10;
                }
            """
        e = "successful"
        self.assertTrue(TestParser.test(i,e,112))
    #113
    def test_assign_statement(self):
        i = """
            Class Adam{
                a = 2 % (3%4_0) %5 * (-4/(3*5)+6 - 5) + 6;
            }
            """
        e = """Error on line 3 col 18: =""" # Assign chi nam trong block statement
        self.assertTrue(TestParser.test(i,e,113))
    #114
    def test_assign_statement_2(self):
        i = """
            Class Adam{
                fun(){
                    a = 2 % (3%4_0) %5 * (-4/(3*5)+6 - 5) + 6;
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i,e,114))
    #115
    def test_if_else_statement(self):
        i = """
            Class AdamEva{
                $func(a, b: Int){
                    If (True){
                        If (_a + e == "String"){
                            Return;
                        }
                        Elseif(1 + 1 == 2){
                            Return Self.x * Self.y;
                        }                        
                    }
                    Else{
                        print(Bruh);
                    }
                }
                
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i,e,115))

