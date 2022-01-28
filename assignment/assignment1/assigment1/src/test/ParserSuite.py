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
        e = "successful"
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
    #116
    def test_class_assign_statement_in_if_condition(self):
        i = """
            Class AdamEva{
                $func(a, b: Int){
                    If (True){
                        If (_a + e == "String"){
                            Return;
                        }
                        Elseif(1 + 1 = 2){
                            Return Self.x * Self.y;
                        }                        
                    }
                    Else{
                        print(Bruh);
                    }
                }
            }
            """
        e = """Error on line 8 col 37: ="""
        self.assertTrue(TestParser.test(i,e,116))
    #117
    def test_else_if_condition_without_expression(self):
        i = """
            Class Eva{
                fun(a, b: String){
                    a = "Sang handsome!";
                    If("Sang" ==. hand_some){ a = "Right";}
                    Elseif(){
                        Return False;
                    }
                }                
            }
            """
        e = """Error on line 6 col 27: )"""
        self.assertTrue(TestParser.test(i,e,117))
    #118
    def test_else_if_condition_with_expression(self):
        i = """
            Class Eva{
                fun(a, b: String){
                    a = "Sang handsome!";
                    If("Sang" ==. hand_some){ a = "Right";}
                    Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
                        Return False;
                    }
                }                
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i,e,118))
    #119
    def test_for_in_statement_wrong_place(self):
        i = """
            Class Eva{
                Foreach(i In 1 .. 100_100 By 1 + 2){
                    X.print("Hello");
                }
                fun(a, b: String){
                    a = "Sang handsome!";
                    If("Sang" ==. hand_some){ a = "Right";}
                    Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
                        Return False;
                    }
                }                
            }
            """
        e = """Error on line 3 col 16: Foreach"""
        self.assertTrue(TestParser.test(i,e,119))
    #120
    def test_for_in_statement(self):
        i = """
            Class Eva{
                fun(a, b: String){
                    a = "Sang handsome!";
                    If("Sang" ==. hand_some){ a = "Right";}
                    Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
                        Return False;
                    }
                    
                    Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
                        X.print("Hello");
                    }
                }                
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i,e,120))
    #121
    def test_var_val_statement(self):
        i = """
            Class Eva{
                Val abc, $a_bc, ab_c : Boolean = True && False, !False, 1+3*10;
                fun(a, b: String){
                    a = "Sang handsome!";
                    If("Sang" ==. hand_some){ a = "Right";}
                    Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
                        Return False;
                    }
                    
                    Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
                        X.print("Hello");
                    }
                }                
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i,e,121))

    # 122
    def test_assign_statement_float(self):
        i = """
            Class Eva{
                Val abc, $a_bc, ab_c : Boolean = True && False, !False, 1+3*10;
                Var a: Float = 100e100_100;
                fun(a, b: String){
                    a = "Sang handsome!";
                    If("Sang" ==. hand_some){ a = "Right";}
                    Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
                        Return False;
                    }

                    Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
                        X.print("Hello");
                    }
                }                
            }
            """
        e = """Error on line 4 col 38: _100"""
        self.assertTrue(TestParser.test(i, e, 122))
    # 123
    def test_assign_statement_superclass(self):
        i = """
            Class Eva : Human{
                Val abc, $a_bc, ab_c : Boolean = True && False, !False, 1+3*10;
                Var a: Float = 100e-100;
                $fun(a, b: String){
                    a = "Sang handsome!";
                    If("Sang" ==. hand_some){ a = "Right";}
                    Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
                        Return False;
                    }

                    Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
                        X.print("Hello");
                    }
                }                
            }
            
            Class Adam : Human{
                Val name: String = "Eva pro";
                run(){
                    print("Adam: " + Eva::$fun("nikhao", 10);)
                }
            }
            """
        e = """Error on line 21 col 60: ;"""
        self.assertTrue(TestParser.test(i, e, 123))

    # 124
    def test_assign_statement_superclass_true(self):
        i = """
            Class Eva : Human{
                Val abc, $a_bc, ab_c : Boolean = True && False, !False, 1+3*10;
                Var a: Float = 100e-100;
                $fun(a, b: String){
                    a = "Sang handsome!";
                    If("Sang" ==. hand_some){ a = "Right";}
                    Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
                        Return False;
                    }

                    Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
                        X.print("Hello");
                    }
                }                
            }

            Class Adam : Human{
                Val name: String = "Eva pro";
                run(){
                    print("Adam: " + Eva::$fun("nikhao", 10));
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 124))
    # 125
    def test_assign_statement_array(self):
        i = """
            Class Eva : Human{
                Val abc, $a_bc, ab_c : Boolean = True && False, !False, 1+3*10;
                Var a: Float = 100e-100;
                 Val bbb: Array[Int, 00123];
                Var _bbb: Array[Array[Int,3], 0123];
                $fun(a, b: String){
                    a = "Sang handsome!";
                    If("Sang" ==. hand_some){ a = "Right";}
                    Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
                        Return False;
                    }

                    Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
                        X.print("Hello");
                    }
                }                
            }

            Class Adam : Human{
                Val name: String = "Eva pro";
                run(){
                    print("Adam: " + Eva::$fun("nikhao", 10));
                }
            }
            """
        e = """Error on line 5 col 39: 123"""
        self.assertTrue(TestParser.test(i, e, 125))
    # 126
    def test_assign_statement_multi_dimentional_array(self):
        i = """
            Class Eva : Human{
                Val abc, $a_bc, ab_c : Boolean = True && False, !False, 1+3*10;
                Var a: Float = 100e-100;
                 Val bbb: Array[Int, 2] = Array(1,2);
                Var _bbb: Array[Array[Array[String, 50],3], 0123];
                $fun(a, b: String){
                    a = "Sang handsome!";
                    If("Sang" ==. hand_some){ a = "Right";}
                    Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
                        Return False;
                    }

                    Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
                        X.print("Hello");
                    }
                }                
            }

            Class Adam : Human{
                Val name: String = "Eva pro";
                run(){
                    print("Adam: " + Eva::$fun("nikhao", 10));
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 126))
    #127
    def test_index_operator(self):
        i = """
            Class Eva{
                main(){
                    System.out(a[i+1000-99/12][i][j][h][k]);
                    a = (1+2.e100 * 3).getX();
                       
                }         
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i,e,127))
    #128
    def test_block_statement(self):
        i = """
            Class Adam{
                $fun(){
                    art(){
                    Var r, s: Int = 1000;
                    r = 2.0 - 10.e+19;
                    Var a, b: Array[Int, 5];
                    s = r * r * Self.myPhi;
                    a[0] = s;
                    }
                }
            }
            """
        e = """Error on line 4 col 25: {"""
        self.assertTrue(TestParser.test(i,e,128))
    # 129
    def test_block_statement_1(self):
        i = """
            Class Adam{
                $fun(){}
                art()
                {
                    Var r, s: Int = 1000;
                    r = 2.0 - 10.e+19;
                    Var a, b: Array[Int, 5];
                    s = r * r * Self.myPhi;
                    a[0] = s;
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 129))
    #130
    def test_break_continue_statement(self):
        i = """
            Class Eva{
                Fun(){
                    Foreach(j In 1 .. 16e188 + 0x841){
                        If (j == 5){
                            Continue;
                        }
                        Else
                        {
                            print.out("Hello: " +. j);
                        }
                    }
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i,e,130))




