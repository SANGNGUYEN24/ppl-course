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
        e = "Error on line 5 col 74: ;"
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
                    X.print("speed is: " +.  "20km/h");
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
                    Var aa, be, $ce, de: Float = 978.063e129, 8_7_6_2.029e99, 98_1.23e-10, hldjkhf;
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
                        X.print(Bruh);
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
                        X.print(Bruh);
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
                    X.X.print("Hello");
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
                        X.X.print("Hello");
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
                        X.X.print("Hello");
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
                        X.X.print("Hello");
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
                        X.X.print("Hello");
                    }
                }
            }

            Class Adam : Human{
                Val name: String = "Eva pro";
                run(){
                    X.print("Adam: " + Eva::$fun("nikhao", 10);)
                }
            }
            """
        e = """Error on line 21 col 62: ;"""
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
                        X.X.print("Hello");
                    }
                }
            }

            Class Adam : Human{
                Val name: String = "Eva pro";
                run(){
                    X.print("Adam: " + Eva::$fun("nikhao", 10));
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
                        X.X.print("Hello");
                    }
                }
            }

            Class Adam : Human{
                Val name: String = "Eva pro";
                run(){
                    X.print("Adam: " + Eva::$fun("nikhao", 10));
                }
            }
            """
        e = """Error on line 5 col 36: 00"""
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
                        X.X.print("Hello");
                    }
                }
            }

            Class Adam : Human{
                Val name: String = "Eva pro";
                run(){
                    X.print("Adam: " + Eva::$fun("nikhao", 10));
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
                    Var r, s: Int = 1000,hskdf + 7826;
                    r = 2.0 - 10.e+19;
                    Var a, b: Array[Int, 5];
                    s = r * r * Self.myPhi;
                    a[0] = s;
                    }
                }
            }
            """
        e = """Error on line 4 col 23: ("""
        self.assertTrue(TestParser.test(i,e,128))
    # 129
    def test_block_statement_1(self):
        i = """
            Class Adam{
                $fun(){}
                art()
                {
                    Var r, s: Int = 1000,102;
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
    #131
    def test_class_random_201(self):
        i = """
            Class Error3 {
                ;
            }
            """
        e = """Error on line 3 col 16: ;"""
        self.assertTrue(TestParser.test(i, e, 131))

    # 132
    def test_class_random_202(self):
        i = """
            Class A{
                Constructor(a, b, c, d, e: String; c, d, e: Int){
                   If(1+2 == 3){
                    If(!False){}
                    Elseif(3==7){

                    }
                   }Else{
                    a = 12;
                   }
                }
                ## This is a comment ##
                Var array: Array[Float, 10];
                Var array2: Array[Array[Int, 3], 3];
                Val _a, b_, d12: Int = expr, expr, expr;
                Var $abcd: String = expr;
                Var abcd, abc: Float;

                a(hi, hello, nikhao: Int){}

                Destructor(){}
            }
            """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 132))

    # 133
    def test_class_random_203(self):
        i = """
            Class Center {
                Var c,d,e-:String;
                Var a: Array[Int, 4] = Array(1, 3, 4, 5);
            }
           """
        e = """Error on line 3 col 25: -"""
        self.assertTrue(TestParser.test(i, e, 133))

    #134
    def test_class_random_204(self):
        i = """
            Class Center {
                Var c,d,e:String;
                Var a: Array[Int, 4] = Array(1, 3, 4, 5);
            }
           """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 134))

    #135
    def test_class_random_205(self):
        i = """
            Class __Center {
                method() {
                    If (1 == 2) {
                        Return asd;
                    }
                    Elseif (2 == 3) {
                        Break;
                        Continue;
                    }
                    Else {
                        Return 233;
                    }
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 135))

    #136
    def test_class_random_206(self):
        i = """
            Class __Center {
                method() {
                    Foreach (asd In RVJjpoz >= IzShZxMbKBioj::$A9npv1lnysU4w0oJ7kbL() .. R6n5wEX6zQurDF * IkIS4E) {
                        vFL_cXn0mVPGSJPJCy = NZmYmG >= IzShZxMbKBioj::$A9npv1lnysU4w0oJ7kbL();
                    }
                    Return Nonsense;
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 136))

    # 137
    def test_class_random_207(self):
        i = """
            Class Error {
                method(s) {
                }
            }
            """
        e = """Error on line 3 col 24: )"""
        self.assertTrue(TestParser.test(i, e, 137))

    # 138
    def test_class_random_208(self):
        i = """
            Class Error {
                Var If ;
            }
            """
        e = """Error on line 3 col 20: If"""
        self.assertTrue(TestParser.test(i, e, 138))

    #139
    def test_class_random_209(self):
        i = """
            Class Error {
                Constructor(param: String) {}
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 139))

    #140
    def test_class_random_210(self):
        i = """
            Class _____ {
                Constructor(param: Int);
            }
            """
        e = """Error on line 3 col 39: ;"""
        self.assertTrue(TestParser.test(i, e, 140))

    #141
    def test_class_random_211(self):
        i = """
            Class Adam : Human {
                Var a: Int = 12.e23;
                jolie() {
                    Self.a = 0x759AL;
                }
            }
            """
        e = """Error on line 5 col 35: L"""
        self.assertTrue(TestParser.test(i, e, 141))

    #145
    def test_class_random_212(self):
        i = """
            Class Adam : Human {
                Var a: Int = 12.e23;
                jskhldfd() {
                    e = Self.x + Self.y;
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 145))

    # 146
    def test_class_random_213(self):
        i = """
            Class Adam : Human {
                Var a: Int = 12.e23;
                method_() {
                    e = Self.x + Self.y;
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 146))

    #147
    def test_class_random_214(self):
        i = """
            Class Adam : Human {
                Var a: Int = 12.e23;
                a = 32;
                method_() {

                }
            }
            """
        e = """Error on line 4 col 18: ="""
        self.assertTrue(TestParser.test(i, e, 147))

    #148
    def test_class_random_215(self):
        i = """
            Class Adam : Human {
                Var a: Int = 12.e23;
                method_() {
                    a.$function();
                }
            }
            """
        e = """Error on line 5 col 22: $function"""
        self.assertTrue(TestParser.test(i, e, 148))

    #149
    def test_class_random_216(self):
        i = """
            Class Adam : Human {
                Var a: Int = 12.e23;
                method_() {
                    a::$function();
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 149))

    #150
    def test_class_random_217(self):
        i = """
            Class Adam : Human {
                Var a: Int = 12.e23;
                method_() {
                    a[123]["ss"][1 + "233"] = Array("asd", "sss");
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 150))

    #151
    def test_class_random_218(self):
        i = """
            Class Adam : Human {
                Var a: Int = 12.e23;
                method_() {
                    a[123]["ss"][1 + "233"] = New X().Y();
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 151))

    #152
    def test_class_random_219(self):
        i = """
            Class Adam : Human {
                Var a: Int = 12.e23;
                method_() {
                    a[123]["ss"][1 + "233"] = New X(Array(22)).Y(759);
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 152))

    #153
    def test_class_random_220(self):
        i = """
            Class Adam : Human {
                Var a: Int = 12.e23;
                method_() {
                    Var $a: String;
                }
            }
            """
        e = """Error on line 5 col 24: $a"""
        self.assertTrue(TestParser.test(i, e, 153))

    #154
    def test_class_random_221(self):
        i = """
            Class Adam : Human {
                If (1 + 1 == 0) {
                    Out.X.print(1 + 2);
                }
                Elseif (1 + 2 == 3) {
                    System.sus(11 - "3222");
                }
                Else {
                    Break;
                    Return;
                }
            }
            """
        e = """Error on line 3 col 16: If"""
        self.assertTrue(TestParser.test(i, e, 154))

    #155
    def test_class_random_222(self):
        i = """
            Class Adam : Human {
                method() {
                    If (1 + 1 == 0) {
                        Out.X.print(1 + 2);
                    }
                    Elseif (1 + 2 == 3) {
                        System.sus(11 - "3222");
                    }
                    Else {
                        Break;
                        Return;
                    }
                }
            }
            """
        e = """successful"""
        self.assertTrue(TestParser.test(i, e, 155))


    #156
    def test_class_random_201_1(self):
        i = """Class main{}"""
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 156))

    #157
    def test_class_random_202_1(self):

        i = """Class Rectangle: Human {
        getArea() {
        Return self.length * self.width;
    }
}"""
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 157))

    #158
    def test_class_random_203_1(self):

        i = """Var a: Array[Array[Int,5],5];"""
        e = "Error on line 1 col 0: Var"
        self.assertTrue(TestParser.test(i, e, 158))

    #159
    def test_class_random_204_1(self):

        i = """1 + 1 + a.function()"""
        e = "Error on line 1 col 0: 1"
        self.assertTrue(TestParser.test(i, e, 159))

    #160
    def test_class_random_205_1(self):

        i = """
    Class Human {
        $getNumOfHuman( {
            Return self.length * self.width;
        }
    }
"""
        e = "Error on line 3 col 24: {"
        self.assertTrue(TestParser.test(i, e, 160))

    #161
    def test_class_random_206_1(self):

        i = """
    Class Human {
        function(){
            a[b[1]][c][function()] = 1;
        }
        Var e,f : Int = 1 + 1, 1 - 2;
    }
"""
        e = "Error on line 4 col 31: ("
        self.assertTrue(TestParser.test(i, e, 161))

    #162
    def test_class_random_207_1(self):

        i = """
Class Human2 {
    $getNumOfHuman() {
        If (a == (1+1) ){
            Var b,c:Boolean = True, False;
        }
        Foreach (i In 1 .. 100 By 2) {
             Var a:Boolean = True;
        }
    }
}
"""
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 162))

    #163
    def test_class_random_208_1(self):

        i = """
    Class Human {
        sum(a,b:Int; c,d:Float){}
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 163))

    #164
    def test_class_random_209_1(self):

        i = """
    Class Human {
        Var a :Array[Array[Int,2],2] = Array(Array(1,1),Array(1,1));
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 164))
    #165
    def test_class_random_210_1(self):

        i = """
    Class Human {
        function(){
            Var a: Boolean = !!True;
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 165))
    #166
    def test_class_random_211_1(self):

        i = """
    Class Human {
        function(){
            function2(1+1,"a"+."b","a"==."b");
        }
    }
    """
        e = "Error on line 4 col 21: ("
        self.assertTrue(TestParser.test(i, e, 166))
    #167
    def test_class_random_212_1(self):

        i = """
    Class Human {
        Val $numOfHuman: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        $getNumOfHuman() {
            Return $numOfHuman;
        }
    }
    Class Rectangle: Human {
        getArea() {
            Return self.length * self.width;
        }
    }
    Class Program {
        main() {
            Out.printInt(Human::$numOfHuman);
        }
    }
    """
        e = "Error on line 7 col 19: $numOfHuman"
        self.assertTrue(TestParser.test(i, e, 167))
    #168
    def test_class_random_213_1(self):

        i = """
    Class Human {
        Constructor(width, height : Int; name:String){
            Self.Area=Self.width*Self.height;
            Self.name="shape"+.name;
        }
        Destructor(){}
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 168))
    #169
    def test_class_random_214_1(self):

        i = """
    Class Human {
        function(){
            a=1------1+1--1;
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 169))
    #170
    def test_class_random_215_1(self):

        i = """
    Class Human {
        function(){
            a=New X().Y();
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 170))
    #171
    def test_class_random_216_1(self):

        i = """
    Class Human {
        function(){
            a();
        }
    }
    """
        e = "Error on line 4 col 13: ("
        self.assertTrue(TestParser.test(i, e, 171))
    #172
    def test_class_random_217_1(self):

        i = """
    Class Human {
        function(){
            Var a();
        }
    }
    """
        e = "Error on line 4 col 17: ("
        self.assertTrue(TestParser.test(i, e, 172))
    #173
    def test_class_random_218_1(self):

        i = """
    Class Human {
        function(){
            Var r, s: Int;
            r = 2.0;
            Var a, b: Array[Int, 5];
            s = r * r * Self.myPI;
            a[0] = s;
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 173))
    #174
    def test_class_random_218_1(self):

        i = """
    Class Human {
        function(){
            a.b();
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 174))
    #175
    def test_class_random_219_1(self):

        i = """
    Class Human {
        function(){
            a=b.c.d.e;
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 175))
    #176
    def test_class_random_220_1(self):

        i = """
    Class Human {
        function(){
            Foreach (i In (1+2) .. (100*2-3) By (16-14)) {
                Out.printInt(i);
            }
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 176))
    #177
    def test_class_random_221_1(self):

        i = """
    Class Human {
        function(){
            ;
        }
    }
    """
        e = "Error on line 4 col 12: ;"
        self.assertTrue(TestParser.test(i, e, 177))
    #178
    def test_class_random_222_1(self):

        i = """
    Class Human {
        function(){
            Foreach (i In a[1] .. function() By _123()) {}
        }
    }
    """
        e = "Error on line 4 col 42: ("
        self.assertTrue(TestParser.test(i, e, 178))
    #179
    def test_class_random_223_1(self):

        i = """
    Class Human {
        function(){
            a = !!!!!!!!!!!!True + !!!!!!!!!!!!!!False;
            b = -------------100_10000;
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 179))
    #180
    def test_class_random_224_1(self):

        i = """
    Class Eva {
        function(){
            a = !!!!!!!!!!!!True;
            b = ------------5;
            c=d.d.d.d.d.d.d.d.ljhsdf.o384.lks;
            e=f[1][1][1][1+328];
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 180))
    #181
    def test_class_random_225(self):

        i = """
    Class Eva {
        function(){
            a = (b==c) == True;
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 182))
    #183
    def test_class_random_226(self):

        i = """
    Class Eva {
        function(){
            a = b == c  == True;
        }
    }
    """
        e = "Error on line 4 col 24: =="
        self.assertTrue(TestParser.test(i, e, 183))
    #184
    def test_class_random_227(self):

        i = """
    Class Eva {
        function(){
            a = (b < c)  == True;
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 184))
    #185
    def test_class_random_228(self):

        i = """
    Class Eva {
        function(){
            a = (b < c) < True;
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 185))
    #186
    def test_class_random_228(self):

        i = """
    Class Eva {
        function(){
            a = b < c < True;
        }
    }
    """
        e = "Error on line 4 col 22: <"
        self.assertTrue(TestParser.test(i, e, 186))
    #187
    def test_class_random_229(self):

        i = """
    Class Eva {
        function(){
            a = ("a"+."b")+."b";
            c = ("a"==."a")==True;
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 187))
    #188
    def test_class_random_230(self):

        i = """
    Class Eva {
        function(){
            a = "a"+."b"+."b";
        }
    }
    """
        e = "Error on line 4 col 24: +."
        self.assertTrue(TestParser.test(i, e, 188))
    #189
    def test_class_random_231(self):

        i = """
    Class Eva : Human {
        function(){
            a = "a"==."b"==."b";
        }
    }
    """
        e = "Error on line 4 col 25: ==."
        self.assertTrue(TestParser.test(i, e, 189))
    #190
    def test_class_random_232(self):

        i = """
    Class Eva : Human:a{}
    """
        e = "Error on line 2 col 21: :"
        self.assertTrue(TestParser.test(i, e, 190))
    #191
    def test_class_random_233(self):

        i = """
    Class Eva : Human {
        function(){
            a::$b__7_78jh=2;
            a::$e_____o76978();
            a::$c::$d=2;
        }
    }
    """
        e = "Error on line 6 col 17: ::"
        self.assertTrue(TestParser.test(i, e, 192))
    #193
    def test_class_random_234(self):

        i = """
    Class Eva : Human {
        function(){
            a::$b__7_78jh=2;
            a::$e_____o76978();
            a::$c()::$d=2;
        }
    }
    """
        e = "Error on line 6 col 19: ::"
        self.assertTrue(TestParser.test(i, e, 194))
    #195
    def test_class_random_235(self):

        i = """
            Class Eva : Human {
                function(){
                a+=1;
                }
            }
            """
        e = "Error on line 4 col 18: ="
        self.assertTrue(TestParser.test(i, e, 195))
    #196
    def test_class_random_236(self):

        i = """
    Class Eva : Human {
        function(){
        a=+1;
        }
    }
    """
        e = "Error on line 4 col 10: +"
        self.assertTrue(TestParser.test(i, e, 196))
    #197
    def test_class_random_237(self):
        i = """
            Class Eva : Human {
                function(){
                a=-1+1;
                b=1+-1;
                }
            }
            """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 197))
    #198
    def test_class_random_238(self):

        i = """
    Class Eva : Human {
        function(){
            a=-1+1;
            b=1+-1--1+-1---1;
        }
    }
    """
        e = "successful"
        self.assertTrue(TestParser.test(i, e, 198))
    #199
    def test_class_random_239(self):

        i = """
    Class Eva : Human {
        function(){
        b=1+-1--1+-1-+-1;
        }
    }
    """
        e = "Error on line 4 col 21: +"
        self.assertTrue(TestParser.test(i, e, 199))
    #200
    def test_class_random_240(self):

        i = """
    Class Eva : Human {
        function(){
        Var a :Int = $1-----5;
        }
    }
    """
        e = "Error on line 4 col 21: $1"
        self.assertTrue(TestParser.test(i, e, 200))

    def test_class_random_241(self):
        i = """
                Class Eva : Human{
                    function(){
                        a = New X().Y();
                        Var a: Array[Int, 0];
                    }
                }

            """
        output = """Error on line 5 col 42: 0"""
        self.assertTrue(TestParser.test(i, output, 241))

    def test_class_random_242(self):
        i = """
                Class Eva : Human{
                    function(){
                        b::$f=1;
                    }
                    a = 19783642;
                }

            """
        output = """Error on line 6 col 22: ="""
        self.assertTrue(TestParser.test(i, output, 242))

    def test_class_random_243(self):
        i = """
                Class Eva : Human{
                    function(){
                        a=1;
                    }
                    Foreach (x In 1 .. 100 by 2){}
                }

            """
        output = """Error on line 6 col 20: Foreach"""
        self.assertTrue(TestParser.test(i, output, 243))

    def test_class_random_244(self):
        i = """
                Class Eva : Human{
                    function(){}
                    Class Nupakachi{}
                }

            """
        output = """Error on line 4 col 20: Class"""
        self.assertTrue(TestParser.test(i, output, 244))

    def test_class_random_245(self):
        i = """
                Class Eva : Human{
                    function(){
                        Class Nupakachi{}
                    }
                }

            """
        output = """Error on line 4 col 24: Class"""
        self.assertTrue(TestParser.test(i, output, 245))

    def test_class_random_246(self):
        i = """
                Class Eva : Human{
                    function(){
                        Var a: Array[Int, 01];
                        Var aaaa: Array[Int, 0x1];
                        Var a_kjhsdf: Array[Int, 0X1];
                        Var ajs: Array[Int, 0b1];
                        Var acm: Array[Int, 0B1];
                        Var a: Array[Int, 15678_65];
                        Var a: Array[Int, 00];
                    }
                }

            """
        output = """Error on line 10 col 42: 00"""
        self.assertTrue(TestParser.test(i, output, 246))

    def test_class_random_247(self):
        i = """
                Class Eva : Human{
                    function(){
                        Var a: Array[Int, 0b0];
                    }
                }

            """
        output = """Error on line 4 col 42: 0b0"""
        self.assertTrue(TestParser.test(i, output, 247))

    def test_class_random_248(self):
        i = """
                Class Eva : Human{
                    function(){
                        Var a: Array[Int, 0x0];
                    }
                }

            """
        output = """Error on line 4 col 42: 0x0"""
        self.assertTrue(TestParser.test(i, output, 248))




