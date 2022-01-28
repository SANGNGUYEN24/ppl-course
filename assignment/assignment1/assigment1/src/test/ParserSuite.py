# import unittest
# from TestUtils import TestParser
#
# class ParserSuite(unittest.TestCase):
#     #101
#     def test_simple_class(self):
#         i = "Class A{}"
#         e = "successful"
#         self.assertTrue(TestParser.test(i,e,101))
#     #102
#     def test_simple_class_missing_bracket(self):
#         i = "Class B{"
#         e = "Error on line 1 col 8: <EOF>"
#         self.assertTrue(TestParser.test(i,e,102))
#     #103
#     def test_simple_class_with_superclass(self):
#         i = "Class Car : Vehicle{}"
#         e = "successful"
#         self.assertTrue(TestParser.test(i,e,103))
#     #104
#     def test_class_with_attribute_declaration_missing_assign_expr(self):
#         i = """
#             ## Define class Car ##
#             Class Car : Vehicle{
#                 Val speed: Float = 0;
#                 Val $model, tireNum: Int;
#             }
#
#         """
#         e = "successful"
#         self.assertTrue(TestParser.test(i,e,104))
#     #105
#     def test_class_with_attribute_declaration(self):
#         i = """
#                     ## Define class Car ##
#                     Class Car : Vehicle{
#                         Val speed: Float = 0;
#                         Val $model, tireNum: Int = 1 * 3 + 4 - 4 / 100_000;
#                     }
#             """
#         e = "successful"
#         self.assertTrue(TestParser.test(i,e,105))
#     #106
#     def test_method_declaration(self):
#         i = """
#             Class Adam{
#             getSpeed(a, b, c, $d: Int){}
#             }
#             """
#         e = "Error on line 3 col 30: $d"
#         self.assertTrue(TestParser.test(i,e,106))
#     #107
#     def test_method_declaration_with_body(self):
#         i = """
#             Class Eva{
#                 getSpeed(a, b, c: Int; d, e: String){
#                     print("speed is: " +.  "20km/h");
#                 }
#             }
#             """
#         e = "successful"
#         self.assertTrue(TestParser.test(i,e,107))
#     #108
#     def test_class_named_main(self):
#         i = "Class main{}"
#         e = "successful"
#         self.assertTrue(TestParser.test(i,e,108))
#     #109
#     def test_attribute_decl_primitive_type(self):
#         i = """
#             Class Eva{
#                 Val a, b, __b: Boolean: True, False, !True;
#                 Var aa, be, $ce, de: Float = 978.063e129, 8_7_6_2.029e99, 98_1.23e-10
#             }
#             """
#         e = "Error on line 3 col 38: :"
#         self.assertTrue(TestParser.test(i,e,109))
#     #110
#     def test_attribute_decl_primitive_type_2(self):
#         i = """
#             Class Eva{
#                 Val a, b, __b: Boolean = True, False, !True;
#                 Var aa, be, $ce, de: Float = 978.063e129, 8_7_6_2.029e99, 98_1.23e-10
#             }
#             """
#         e = "Error on line 5 col 12: }"
#         self.assertTrue(TestParser.test(i,e,110))
#     #111
#     def test_attribute_decl_primitive_type_3(self):
#         i = """
#             Class Eva{
#                 Val a, b, __b: Boolean = True, False, !True;
#                 Var aa, be, $ce, de: Float = 978.063e129, 8_7_6_2.029e99, 98_1.23e-10
#             }
#             """
#         e = "Error on line 5 col 12: }"
#         self.assertTrue(TestParser.test(i,e,111))
#     #112
#     def test_attribute_decl_primitive_type_4(self):
#         i = """
#                 Class Eva{
#                     Val a, b, __b: Boolean = True, False, !True;
#                     Var aa, be, $ce, de: Float = 978.063e129, 8_7_6_2.029e99, 98_1.23e-10;
#                 }
#             """
#         e = "successful"
#         self.assertTrue(TestParser.test(i,e,112))
#     #113
#     def test_assign_statement(self):
#         i = """
#             Class Adam{
#                 a = 2 % (3%4_0) %5 * (-4/(3*5)+6 - 5) + 6;
#             }
#             """
#         e = """Error on line 3 col 18: =""" # Assign chi nam trong block statement
#         self.assertTrue(TestParser.test(i,e,113))
#     #114
#     def test_assign_statement_2(self):
#         i = """
#             Class Adam{
#                 fun(){
#                     a = 2 % (3%4_0) %5 * (-4/(3*5)+6 - 5) + 6;
#                 }
#             }
#             """
#         e = """successful"""
#         self.assertTrue(TestParser.test(i,e,114))
#     #115
#     def test_if_else_statement(self):
#         i = """
#             Class AdamEva{
#                 $func(a, b: Int){
#                     If (True){
#                         If (_a + e == "String"){
#                             Return;
#                         }
#                         Elseif(1 + 1 == 2){
#                             Return Self.x * Self.y;
#                         }
#                     }
#                     Else{
#                         print(Bruh);
#                     }
#                 }
#             }
#             """
#         e = """successful"""
#         self.assertTrue(TestParser.test(i,e,115))
#     #116
#     def test_class_assign_statement_in_if_condition(self):
#         i = """
#             Class AdamEva{
#                 $func(a, b: Int){
#                     If (True){
#                         If (_a + e == "String"){
#                             Return;
#                         }
#                         Elseif(1 + 1 = 2){
#                             Return Self.x * Self.y;
#                         }
#                     }
#                     Else{
#                         print(Bruh);
#                     }
#                 }
#             }
#             """
#         e = """Error on line 8 col 37: ="""
#         self.assertTrue(TestParser.test(i,e,116))
#     #117
#     def test_else_if_condition_without_expression(self):
#         i = """
#             Class Eva{
#                 fun(a, b: String){
#                     a = "Sang handsome!";
#                     If("Sang" ==. hand_some){ a = "Right";}
#                     Elseif(){
#                         Return False;
#                     }
#                 }
#             }
#             """
#         e = """Error on line 6 col 27: )"""
#         self.assertTrue(TestParser.test(i,e,117))
#     #118
#     def test_else_if_condition_with_expression(self):
#         i = """
#             Class Eva{
#                 fun(a, b: String){
#                     a = "Sang handsome!";
#                     If("Sang" ==. hand_some){ a = "Right";}
#                     Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
#                         Return False;
#                     }
#                 }
#             }
#             """
#         e = """successful"""
#         self.assertTrue(TestParser.test(i,e,118))
#     #119
#     def test_for_in_statement_wrong_place(self):
#         i = """
#             Class Eva{
#                 Foreach(i In 1 .. 100_100 By 1 + 2){
#                     X.print("Hello");
#                 }
#                 fun(a, b: String){
#                     a = "Sang handsome!";
#                     If("Sang" ==. hand_some){ a = "Right";}
#                     Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
#                         Return False;
#                     }
#                 }
#             }
#             """
#         e = """Error on line 3 col 16: Foreach"""
#         self.assertTrue(TestParser.test(i,e,119))
#     #120
#     def test_for_in_statement(self):
#         i = """
#             Class Eva{
#                 fun(a, b: String){
#                     a = "Sang handsome!";
#                     If("Sang" ==. hand_some){ a = "Right";}
#                     Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
#                         Return False;
#                     }
#
#                     Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
#                         X.print("Hello");
#                     }
#                 }
#             }
#             """
#         e = """successful"""
#         self.assertTrue(TestParser.test(i,e,120))
#     #121
#     def test_var_val_statement(self):
#         i = """
#             Class Eva{
#                 Val abc, $a_bc, ab_c : Boolean = True && False, !False, 1+3*10;
#                 fun(a, b: String){
#                     a = "Sang handsome!";
#                     If("Sang" ==. hand_some){ a = "Right";}
#                     Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
#                         Return False;
#                     }
#
#                     Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
#                         X.print("Hello");
#                     }
#                 }
#             }
#             """
#         e = """successful"""
#         self.assertTrue(TestParser.test(i,e,121))
#
#     # 122
#     def test_assign_statement_float(self):
#         i = """
#             Class Eva{
#                 Val abc, $a_bc, ab_c : Boolean = True && False, !False, 1+3*10;
#                 Var a: Float = 100e100_100;
#                 fun(a, b: String){
#                     a = "Sang handsome!";
#                     If("Sang" ==. hand_some){ a = "Right";}
#                     Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
#                         Return False;
#                     }
#
#                     Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
#                         X.print("Hello");
#                     }
#                 }
#             }
#             """
#         e = """Error on line 4 col 38: _100"""
#         self.assertTrue(TestParser.test(i, e, 122))
#     # 123
#     def test_assign_statement_superclass(self):
#         i = """
#             Class Eva : Human{
#                 Val abc, $a_bc, ab_c : Boolean = True && False, !False, 1+3*10;
#                 Var a: Float = 100e-100;
#                 $fun(a, b: String){
#                     a = "Sang handsome!";
#                     If("Sang" ==. hand_some){ a = "Right";}
#                     Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
#                         Return False;
#                     }
#
#                     Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
#                         X.print("Hello");
#                     }
#                 }
#             }
#
#             Class Adam : Human{
#                 Val name: String = "Eva pro";
#                 run(){
#                     print("Adam: " + Eva::$fun("nikhao", 10);)
#                 }
#             }
#             """
#         e = """Error on line 21 col 60: ;"""
#         self.assertTrue(TestParser.test(i, e, 123))
#
#     # 124
#     def test_assign_statement_superclass_true(self):
#         i = """
#             Class Eva : Human{
#                 Val abc, $a_bc, ab_c : Boolean = True && False, !False, 1+3*10;
#                 Var a: Float = 100e-100;
#                 $fun(a, b: String){
#                     a = "Sang handsome!";
#                     If("Sang" ==. hand_some){ a = "Right";}
#                     Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
#                         Return False;
#                     }
#
#                     Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
#                         X.print("Hello");
#                     }
#                 }
#             }
#
#             Class Adam : Human{
#                 Val name: String = "Eva pro";
#                 run(){
#                     print("Adam: " + Eva::$fun("nikhao", 10));
#                 }
#             }
#             """
#         e = """successful"""
#         self.assertTrue(TestParser.test(i, e, 124))
#     # 125
#     def test_assign_statement_array(self):
#         i = """
#             Class Eva : Human{
#                 Val abc, $a_bc, ab_c : Boolean = True && False, !False, 1+3*10;
#                 Var a: Float = 100e-100;
#                 Val bbb: Array[Int, 00123];
#                 Var _bbb: Array[Array[Int,3], 0123];
#                 $fun(a, b: String){
#                     a = "Sang handsome!";
#                     If("Sang" ==. hand_some){ a = "Right";}
#                     Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
#                         Return False;
#                     }
#
#                     Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
#                         X.print("Hello");
#                     }
#                 }
#             }
#
#             Class Adam : Human{
#                 Val name: String = "Eva pro";
#                 run(){
#                     print("Adam: " + Eva::$fun("nikhao", 10));
#                 }
#             }
#             """
#         e = """Error on line 5 col 39: 123"""
#         self.assertTrue(TestParser.test(i, e, 125))
#     # 126
#     def test_assign_statement_multi_dimentional_array(self):
#         i = """
#             Class Eva : Human{
#                 Val abc, $a_bc, ab_c : Boolean = True && False, !False, 1+3*10;
#                 Var a: Float = 100e-100;
#                  Val bbb: Array[Int, 2] = Array(1,2);
#                 Var _bbb: Array[Array[Array[String, 50],3], 0123];
#                 $fun(a, b: String){
#                     a = "Sang handsome!";
#                     If("Sang" ==. hand_some){ a = "Right";}
#                     Elseif((1 + 2 - 3 * 4) % 10 + Adam::$getApplePiece()){
#                         Return False;
#                     }
#
#                     Foreach(i In 1*2-10/1_111 .. 100_100/a.getX() By 1 + 2){
#                         X.print("Hello");
#                     }
#                 }
#             }
#
#             Class Adam : Human{
#                 Val name: String = "Eva pro";
#                 run(){
#                     print("Adam: " + Eva::$fun("nikhao", 10));
#                 }
#             }
#             """
#         e = """successful"""
#         self.assertTrue(TestParser.test(i, e, 126))
#     #127
#     def test_index_operator(self):
#         i = """
#             Class Eva{
#                 main(){
#                     System.out(a[i+1000-99/12][i][j][h][k]);
#                     a = (1+2.e100 * 3).getX();
#
#                 }
#             }
#             """
#         e = """successful"""
#         self.assertTrue(TestParser.test(i,e,127))
#     #128
#     def test_block_statement(self):
#         i = """
#             Class Adam{
#                 $fun(){
#                     art(){
#                     Var r, s: Int = 1000;
#                     r = 2.0 - 10.e+19;
#                     Var a, b: Array[Int, 5];
#                     s = r * r * Self.myPhi;
#                     a[0] = s;
#                     }
#                 }
#             }
#             """
#         e = """Error on line 4 col 25: {"""
#         self.assertTrue(TestParser.test(i,e,128))
#     # 129
#     def test_block_statement_1(self):
#         i = """
#             Class Adam{
#                 $fun(){}
#                 art()
#                 {
#                     Var r, s: Int = 1000;
#                     r = 2.0 - 10.e+19;
#                     Var a, b: Array[Int, 5];
#                     s = r * r * Self.myPhi;
#                     a[0] = s;
#                 }
#             }
#             """
#         e = """successful"""
#         self.assertTrue(TestParser.test(i, e, 129))
#     #130
#     def test_break_continue_statement(self):
#         i = """
#             Class Eva{
#                 Fun(){
#                     Foreach(j In 1 .. 16e188 + 0x841){
#                         If (j == 5){
#                             Continue;
#                         }
#                         Else
#                         {
#                             print.out("Hello: " +. j);
#                         }
#                     }
#                 }
#             }
#             """
#         e = """successful"""
#         self.assertTrue(TestParser.test(i,e,130))
#
#
#
#

#
# def test_201(self):
#     input = """
#         Class Error3 {
#             ;
#         }
#         """
#     expect = """Error on line 3 col 12: ;"""
#     self.assertTrue(TestParser.test(input, expect, 201))
#
#
# def test_202(self):
#     input = """
#         Class A{
#             Constructor(a, b, c, d, e: String; c, d, e: Int){
#                If(1+2 == 3){
#                 If(!False){}
#                 Elseif(3==7){
#
#                 }
#                }Else{
#                 a = 12;
#                }
#             }
#             ## This is a comment ##
#             Var array: Array[Float, 10];
#             Var array2: Array[Array[Int, 3], 3];
#             Val _a, b_, d12: Int = expr, expr, expr;
#             Var $abcd: String = expr;
#             Var abcd, abc: Float;
#
#             a(hi, hello, nikhao: Int){}
#
#             Destructor(){}
#         }
#         """
#     expect = "successful"
#     self.assertTrue(TestParser.test(input, expect, 202))
#
#
# def test_203(self):
#     input = """
#         Class Right__ {
#             Var c,d,e-:String;
#             Var a: Array[Int, 4] = Array(1, 3, 4, 5);
#         }
#        """
#     expect = """Error on line 3 col 21: -"""
#     self.assertTrue(TestParser.test(input, expect, 203))
#
#
# def test_204(self):
#     input = """
#         Class Right__ {
#             Var c,d,e:String;
#             Var a: Array[Int, 4] = Array(1, 3, 4, 5);
#         }
#        """
#     expect = """successful"""
#     self.assertTrue(TestParser.test(input, expect, 204))
#
#
# def test_205(self):
#     input = """
#         Class __Right__ {
#             method() {
#                 If (1 == 2) {
#                     Return asd;
#                 }
#                 Elseif (2 == 3) {
#                     Break;
#                     Continue;
#                 }
#                 Else {
#                     Return 233;
#                 }
#             }
#         }
#         """
#     expect = """successful"""
#     self.assertTrue(TestParser.test(input, expect, 205))
#
#
# def test_206(self):
#     input = """
#         Class __Right__ {
#             method() {
#                 Foreach (asd In RVJjpoz >= IzShZxMbKBioj::$A9npv1lnysU4w0oJ7kbL() .. R6n5wEX6zQurDF * IkIS4E) {
#                     vFL_cXn0mVPGSJPJCy = NZmYmG >= IzShZxMbKBioj::$A9npv1lnysU4w0oJ7kbL();
#                 }
#                 Return Nonsense;
#             }
#         }
#         """
#     expect = """successful"""
#     self.assertTrue(TestParser.test(input, expect, 206))
#
#
# def test_207(self):
#     input = """
#         Class Error {
#             method(s) {
#             }
#         }
#         """
#     expect = """Error on line 3 col 20: )"""
#     self.assertTrue(TestParser.test(input, expect, 207))
#
#
# def test_208(self):
#     input = """
#         Class Error {
#             Var If ;
#         }
#         """
#     expect = """Error on line 3 col 16: If"""
#     self.assertTrue(TestParser.test(input, expect, 208))
#
#
# def test_209(self):
#     input = """
#         Class Error {
#             Constructor(param: String) {}
#         }
#         """
#     expect = """successful"""
#     self.assertTrue(TestParser.test(input, expect, 209))
#
#
# def test_210(self):
#     input = """
#         Class _____ {
#             Constructor(param: Int);
#         }
#         """
#     expect = """Error on line 3 col 35: ;"""
#     self.assertTrue(TestParser.test(input, expect, 210))
#
#
# def test_211(self):
#     input = """
#         Class __CCDeSua__ {
#             Var a: Int = 12.e23;
#             method_Kokomi() {
#                 Self.a = 0x333AL;
#             }
#         }
#         """
#     expect = """Error on line 5 col 31: L"""
#     self.assertTrue(TestParser.test(input, expect, 211))
#
#
# def test_212(self):
#     input = """
#         Class __CCDeSua__ {
#             Var a: Int = 12.e23;
#             method_Kokomi() {
#                 Self = Self + Self;
#             }
#         }
#         """
#     expect = """Error on line 5 col 21: ="""
#     self.assertTrue(TestParser.test(input, expect, 212))
#
#
# def test_213(self):
#     input = """
#         Class __CCDeSua__ {
#             Var a: Int = 12.e23;
#             method_() {
#                 Self = Self + Self;
#             }
#         }
#         """
#     expect = """Error on line 5 col 21: ="""
#     self.assertTrue(TestParser.test(input, expect, 213))
#
#
# def test_214(self):
#     input = """
#         Class __CCDeSua__ {
#             Var a: Int = 12.e23;
#             a = 32;
#             method_() {
#
#             }
#         }
#         """
#     expect = """Error on line 4 col 14: ="""
#     self.assertTrue(TestParser.test(input, expect, 214))
#
#
# def test_215(self):
#     input = """
#         Class __CCDeSua__ {
#             Var a: Int = 12.e23;
#             method_() {
#                 a.$foo();
#             }
#         }
#         """
#     expect = """Error on line 5 col 18: $foo"""
#     self.assertTrue(TestParser.test(input, expect, 215))
#
#
# def test_216(self):
#     input = """
#         Class __CCDeSua__ {
#             Var a: Int = 12.e23;
#             method_() {
#                 a::$foo();
#             }
#         }
#         """
#     expect = """successful"""
#     self.assertTrue(TestParser.test(input, expect, 216))
#
#
# def test_217(self):
#     input = """
#         Class __CCDeSua__ {
#             Var a: Int = 12.e23;
#             method_() {
#                 a[123]["ss"][1 + "233"] = Array("asd", "sss");
#             }
#         }
#         """
#     expect = """successful"""
#     self.assertTrue(TestParser.test(input, expect, 217))
#
#
# def test_218(self):
#     input = """
#         Class __CCDeSua__ {
#             Var a: Int = 12.e23;
#             method_() {
#                 a[123]["ss"][1 + "233"] = New X().Y();
#             }
#         }
#         """
#     expect = """successful"""
#     self.assertTrue(TestParser.test(input, expect, 218))
#
#
# def test_219(self):
#     input = """
#         Class __CCDeSua__ {
#             Var a: Int = 12.e23;
#             method_() {
#                 a[123]["ss"][1 + "233"] = New X(Array(22)).Y(333);
#             }
#         }
#         """
#     expect = """successful"""
#     self.assertTrue(TestParser.test(input, expect, 219))
#
#
# def test_220(self):
#     input = """
#         Class __CCDeSua__ {
#             Var a: Int = 12.e23;
#             method_() {
#                 Var $a: String;
#             }
#         }
#         """
#     expect = """Error on line 5 col 20: $a"""
#     self.assertTrue(TestParser.test(input, expect, 220))
#
#
# def test_221(self):
#     input = """
#         Class __CCDeSua__ {
#             If (1 + 1 == 0) {
#                 Out.print(1 + 2);
#             }
#             Elseif (1 + 2 == 3) {
#                 System.sus(11 - "3222");
#             }
#             Else {
#                 Break;
#                 Return;
#             }
#         }
#         """
#     expect = """Error on line 3 col 12: If"""
#     self.assertTrue(TestParser.test(input, expect, 221))
#
#
# def test_222(self):
#     input = """
#         Class __CCDeSua__ {
#             method() {
#                 If (1 + 1 == 0) {
#                     Out.print(1 + 2);
#                 }
#                 Elseif (1 + 2 == 3) {
#                     System.sus(11 - "3222");
#                 }
#                 Else {
#                     Break;
#                     Return;
#                 }
#             }
#         }
#         """
#     expect = """successful"""
#     self.assertTrue(TestParser.test(input, expect, 222))
#
#
#
# import unittest
# from TestUtils import TestParser
#
#
# class ParserSuite(unittest.TestCase):
#     def test_201(self):
#         """Simple program: int main() {} """
#         input = """Class main{}"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 201))
#
#     def test_202(self):
#         """More complex program"""
#         input = """Class Rectangle: Shape {
#         getArea() {
#         Return self.length * self.width;
#     }
# }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 202))
#
#     def test_203(self):
#         """More complex program"""
#         input = """Var a: Array[Array[Int,5],5];"""
#         expect = "Error on line 1 col 0: Var"
#         self.assertTrue(TestParser.test(input, expect, 203))
#
#     def test_204(self):
#         """More complex program"""
#         input = """1 + 1 + a.foo()"""
#         expect = "Error on line 1 col 0: 1"
#         self.assertTrue(TestParser.test(input, expect, 204))
#
#     def test_205(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         $getNumOfShape( {
#             Return self.length * self.width;
#         }
#     }
# """
#         expect = "Error on line 3 col 24: {"
#         self.assertTrue(TestParser.test(input, expect, 205))
#
#     def test_206(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a[b[1]][c][foo()] = 1;
#         }
#         Var e,f : Int = 1 + 1, 1 - 2;
#     }
# """
#         expect = "Error on line 4 col 26: ("
#         self.assertTrue(TestParser.test(input, expect, 206))
#
#     def test_207(self):
#         """More complex program"""
#         input = """
# Class Shape2 {
#     $getNumOfShape() {
#         If (a == (1+1) ){
#             Var b,c:Boolean = True, False;
#         }
#         Foreach (i In 1 .. 100 By 2) {
#              Var a:Boolean = True;
#         }
#     }
# }
# """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 207))
#
#     def test_208(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         sum(a,b:Int; c,d:Float){}
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 208))
#
#     def test_209(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         Var a :Array[Array[Int,2],2] = Array(Array(1,1),Array(1,1));
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 209))
#
#     def test_210(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             Var a: Boolean = !!True;
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 210))
#
#     def test_211(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             foo2(1+1,"a"+."b","a"==."b");
#         }
#     }
#     """
#         expect = "Error on line 4 col 16: ("
#         self.assertTrue(TestParser.test(input, expect, 211))
#
#     def test_212(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         Val $numOfShape: Int = 0;
#         Val immutableAttribute: Int = 0;
#         Var length, width: Int;
#         $getNumOfShape() {
#             Return $numOfShape;
#         }
#     }
#     Class Rectangle: Shape {
#         getArea() {
#             Return self.length * self.width;
#         }
#     }
#     Class Program {
#         main() {
#             Out.printInt(Shape::$numOfShape);
#         }
#     }
#     """
#         expect = "Error on line 7 col 19: $numOfShape"
#         self.assertTrue(TestParser.test(input, expect, 212))
#
#     def test_213(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         Constructor(width, height : Int; name:String){
#             Self.Area=Self.width*Self.height;
#             Self.name="shape"+.name;
#         }
#         Destructor(){}
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 213))
#
#     def test_214(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a=1------1+1--1;
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 214))
#
#     def test_215(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a=New X().Y();
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 215))
#
#     def test_216(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a();
#         }
#     }
#     """
#         expect = "Error on line 4 col 13: ("
#         self.assertTrue(TestParser.test(input, expect, 216))
#
#     def test_217(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             Var a();
#         }
#     }
#     """
#         expect = "Error on line 4 col 17: ("
#         self.assertTrue(TestParser.test(input, expect, 217))
#
#     def test_218(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             Var r, s: Int;
#             r = 2.0;
#             Var a, b: Array[Int, 5];
#             s = r * r * Self.myPI;
#             a[0] = s;
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 218))
#
#     def test_218(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a.b();
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 218))
#
#     def test_219(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a=b.c.d.e;
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 219))
#
#     def test_220(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             Foreach (i In (1+2) .. (100*2-3) By (16-14)) {
#                 Out.printInt(i);
#             }
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 220))
#
#     def test_221(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             ;
#         }
#     }
#     """
#         expect = "Error on line 4 col 12: ;"
#         self.assertTrue(TestParser.test(input, expect, 221))
#
#     def test_222(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             Foreach (i In a[1] .. foo() By _123()) {}
#         }
#     }
#     """
#         expect = "Error on line 4 col 37: ("
#         self.assertTrue(TestParser.test(input, expect, 222))
#
#     def test_223(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a = !!!!!!!!!!!!True;
#             b = ------------5;
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 223))
#
#     def test_224(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a = !!!!!!!!!!!!True;
#             b = ------------5;
#             c=d.d.d.d.d.d.d.d;
#             e=f[1][1][1][1];
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 224))
#
#     def test_225(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a = (b==c) == True;
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 225))
#
#     def test_226(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a = b == c  == True;
#         }
#     }
#     """
#         expect = "Error on line 4 col 24: =="
#         self.assertTrue(TestParser.test(input, expect, 226))
#
#     def test_227(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a = (b < c)  == True;
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 227))
#
#     def test_228(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a = (b < c) < True;
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 228))
#
#     def test_228(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a = b < c < True;
#         }
#     }
#     """
#         expect = "Error on line 4 col 22: <"
#         self.assertTrue(TestParser.test(input, expect, 228))
#
#     def test_229(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a = ("a"+."b")+."b";
#             c = ("a"==."a")==True;
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 229))
#
#     def test_230(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a = "a"+."b"+."b";
#         }
#     }
#     """
#         expect = "Error on line 4 col 24: +."
#         self.assertTrue(TestParser.test(input, expect, 230))
#
#     def test_231(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a = "a"==."b"==."b";
#         }
#     }
#     """
#         expect = "Error on line 4 col 25: ==."
#         self.assertTrue(TestParser.test(input, expect, 231))
#
#     def test_232(self):
#         """More complex program"""
#         input = """
#     Class Shape:a:b{}
#     """
#         expect = "Error on line 2 col 17: :"
#         self.assertTrue(TestParser.test(input, expect, 232))
#
#     def test_233(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a::$b=2;
#             a::$e();
#             a::$c::$d=2;
#         }
#     }
#     """
#         expect = "Error on line 6 col 17: ::"
#         self.assertTrue(TestParser.test(input, expect, 233))
#
#     def test_234(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a::$b=2;
#             a::$e();
#             a::$c()::$d=2;
#         }
#     }
#     """
#         expect = "Error on line 6 col 19: ::"
#         self.assertTrue(TestParser.test(input, expect, 234))
#
#     def test_235(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#         a+=1;
#         }
#     }
#     """
#         expect = "Error on line 4 col 9: +"
#         self.assertTrue(TestParser.test(input, expect, 235))
#
#     def test_236(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#         a=+1;
#         }
#     }
#     """
#         expect = "Error on line 4 col 10: +"
#         self.assertTrue(TestParser.test(input, expect, 236))
#
#     def test_237(self):
#         input = """
#             Class Shape {
#                 foo(){
#                 a=-1+1;
#                 b=1+-1;
#                 }
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 236))
#
#     def test_238(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#             a=-1+1;
#             b=1+-1--1+-1---1;
#         }
#     }
#     """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 238))
#
#     def test_239(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#         b=1+-1--1+-1-+-1;
#         }
#     }
#     """
#         expect = "Error on line 4 col 21: +"
#         self.assertTrue(TestParser.test(input, expect, 239))
#
#     def test_240(self):
#         """More complex program"""
#         input = """
#     Class Shape {
#         foo(){
#         Var a :Int = $1-----5;
#         }
#     }
#     """
#         expect = "Error on line 4 col 21: $1"
#         self.assertTrue(TestParser.test(input, expect, 240))
#
#     def test_241(self):
#         input = """
#                 Class Shape{
#                     foo(){
#                         a = New X().Y();
#                         Var a: Array[Int, 0];
#                     }
#                 }
#
#             """
#         output = """Error on line 5 col 42: 0"""
#         self.assertTrue(TestParser.test(input, output, 241))
#
#     def test_242(self):
#         input = """
#                 Class Shape{
#                     foo(){
#                         b::$f=1;
#                     }
#                     a = 1;
#                 }
#
#             """
#         output = """Error on line 6 col 22: ="""
#         self.assertTrue(TestParser.test(input, output, 242))
#
#     def test_243(self):
#         input = """
#                 Class Shape{
#                     foo(){
#                         a=1;
#                     }
#                     Foreach (x In 1 .. 100 by 2){}
#                 }
#
#             """
#         output = """Error on line 6 col 20: Foreach"""
#         self.assertTrue(TestParser.test(input, output, 243))
#
#     def test_244(self):
#         input = """
#                 Class Shape{
#                     foo(){}
#                     Class LamTestMetVaiLoz{}
#                 }
#
#             """
#         output = """Error on line 4 col 20: Class"""
#         self.assertTrue(TestParser.test(input, output, 244))
#
#     def test_245(self):
#         input = """
#                 Class Shape{
#                     foo(){
#                         Class LamTestMetVaiLoz{}
#                     }
#                 }
#
#             """
#         output = """Error on line 4 col 24: Class"""
#         self.assertTrue(TestParser.test(input, output, 245))
#
#     def test_246(self):
#         input = """
#                 Class Shape{
#                     foo(){
#                         Var a: Array[Int, 01];
#                         Var a: Array[Int, 0x1];
#                         Var a: Array[Int, 0X1];
#                         Var a: Array[Int, 0b1];
#                         Var a: Array[Int, 0B1];
#                         Var a: Array[Int, 1];
#                         Var a: Array[Int, 00];
#                     }
#                 }
#
#             """
#         output = """Error on line 10 col 42: 00"""
#         self.assertTrue(TestParser.test(input, output, 246))
#
#     def test_247(self):
#         input = """
#                 Class Shape{
#                     foo(){
#                         Var a: Array[Int, 0b0];
#                     }
#                 }
#
#             """
#         output = """Error on line 4 col 42: 0b0"""
#         self.assertTrue(TestParser.test(input, output, 247))
#
#     def test_248(self):
#         input = """
#                 Class Shape{
#                     foo(){
#                         Var a: Array[Int, 0x0];
#                     }
#                 }
#
#             """
#         output = """Error on line 4 col 42: 0x0"""
#         self.assertTrue(TestParser.test(input, output, 248))
#
#     def test_249(self):
#         input = """
#                 Class Shape{
#                     foo(){
#                         Var a: Array[Int, 1_23.456e+7];
#                     }
#                 }
#
#             """
#         output = """Error on line 4 col 42: 123.456e+7"""
#         self.assertTrue(TestParser.test(input, output, 249))
#
#     def test_250(self):
#         input = """
#                 Class Shape{
#                     foo(){
#                         Var a: Array[Int, b::$c.foo()];
#                     }
#                 }
#
#             """
#         output = """Error on line 4 col 42: b"""
#         self.assertTrue(TestParser.test(input, output, 250))





from cmath import exp
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_1(self):
        ## TODO: Test utils:
        input = """
				Class TestCase : TestParser {
					Var x: ClassIT = 123*125/24*0b1%335-aabc;
					Test1() {
						x::$a = "She said that'"Int World'"";
					}
				}
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1))

    def test_2(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Var x: ClassIT = 123*125/24*0b1%335-aabc;
					Test1() {
						x::$a = "She said that '"Int World '"";
					}
				}
				Class Program {}
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 2))

    def test_3(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Var x: ClassIT = 123*125/24*0b1%335-aabc;
					Test1() {
						x::$a = "She said that '"Hello World '"";
						Var $def: Int = "123456";
					}
				}
				Class Program {}
			"""
        expect = "Error on line 6 col 10: $def"
        self.assertTrue(TestParser.test(input, expect, 3))

    def test_4(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Var x: ClassIT = 123*125/24*0b1%335-aabc;
					Test1() {
						x::$a = "She said that '"Hello World '"";
						Var def: Int = "123456";
						Val abc: Array[Array[Int, 0b1],0] = Array();
					}
				}
				Class Program {}
			"""
        expect = "Error on line 7 col 37: 0"
        self.assertTrue(TestParser.test(input, expect, 4))

    def test_5(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Var x: ClassIT = 123*125/24*0b1%335-aabc;
					Test1() {
						x::$a = "She said that '"Hello World '"";
						Var def: Int = "123456";
						Val abc: Array[Array[Int, 0b1],0x1] = Array();
						If (True) {
							Continue;
						}
					}
				}
				Class Program {}
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 5))

    def test_6(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Var x: ClassIT = 123*125/24*0b1%335-aabc;
					Test1() {
						x::$a = "She said that '"Int World '"";
						Var def: Int = "123456";
						Val abc: Array[Array[Int, 0b1],0x1] = Array();
						If (True) {
							Continue;
							a = b * c + d.foo().f;
						} Elseif (False) {
							Var a, b, d: Int = 1,2;
						}
					}
				}
				Class Program {}
			"""
        expect = "Error on line 12 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 6))

    def test_7(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Var x: ClassIT = 123*125/24*0b1%335-aabc;
					Test1() {
						x::$a = "She said that '"Int World '"";
						Var def: Int = "123456";
						Val abc: Array[Array[Int, 0b1],0x1] = Array();
						If (True) {
							Continue;
							a = b * c + d.foo().f;
						} Elseif (False) {
							Var a, b, d: Int = 1,2,3;
							Break;
							If (1/2*3-4) {
								Out.prinln("I'm you but private");
							} Else {}
						}
					}
				}
				Class Program {}
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 7))

    def test_8(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Var x: ClassIT = 123*125/24*0b1%335-aabc;
					Test1() {
						x::$a = "She said that '"Int World '"";
						Var def: Int = "123456";
						Val abc: Array[Array[Int, 0b1],0x1] = Array();
						If (True) {
							Continue;
							a = b * c + d.foo().f;
						} Elseif (False) {
							Var a, b, d: Int = 1,2,3;
							Break;
							If (1/2*3-4) {
								Out.prinln("I'm you but private");
							} Else {
								vari*3/4*5[a] = 19/83*New A(bcd)[b];
							}
						}
					}
				}
				Class Program {}
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 8))

    def test_9(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Var x: ClassIT = 123*125/24*0b1%335-aabc;
					Test1() {
						x::$a = "She said that '"Int World '"";
						Var def: Int = "123456";
						Val abc: Array[Array[Int, 0b1],0x1] = Array();
						If (True) {
							Continue;
							a = b * c + d.foo().f;
						} Elseif (False) {
							Var a, b, d: Int = 1,2,3;
							Break;
							If (1/2*3-4) {
								Out.prinln("I'm you but private");
							} Else {
								vari*3/4*5[a] = 19/83*New A(bcd)[b];
								a = "This is string contain \t";
							}
						}
					}
				}
				Class Program {}
			"""
        expect = "This is string contain "
        self.assertTrue(TestParser.test(input, expect, 9))

    def test_10(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Var x: ClassIT = 123*125/24*0b1%335-aabc;
					Test1() {
						x::$a = "She said that '"Int World '"";
						Var def: Int = "123456";
						Val abc: Array[Array[Int, 0b1],0x1] = Array();
						If (True) {
							Continue;
							a = b * c + d.foo().f;
						} Elseif (False) {
							Var a, b, d: Int = 1,2,3;
							Break;
							If (1/2*3-4) {
								Out.prinln("I'm you but private");
							} Else {
								vari*3/4*5[a] = 19/83*New A(bcd)[b];
								a = "This is string contain \\t";
							}
						}
					}
					Test2() {
						Foraech(x In 1 .. 2){}
					}
				}
				Class Program {}
			"""
        expect = "Error on line 23 col 13: ("
        self.assertTrue(TestParser.test(input, expect, 10))

    def test_11(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Test2() {
						Foreach(a[0] In 1 .. 2){}
					}
				}
				Class Program {}
			"""
        expect = "Error on line 4 col 19: In"
        self.assertTrue(TestParser.test(input, expect, 11))

    def test_12(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Test2() {
						Foreach(a::$foo().b In abc .. def By "This is abc" +. "def"){}
					}
				}
				Class Program {}
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 12))

    def test_13(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Test2() {
						Foreach(a::$foo().b In abc .. def By "This is abc" +. "def"){
							If (!True) {
								a = (((!123) >= ((234 && (345 + 456)) || 567)) <= (678 != x::$a));
							}
						}
					}
				}
				Class Program {}
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 13))

    def test_14(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Test2() {
						Foreach(a::$foo().b In abc .. def By "This is abc" +. "def"){
							If (!True) {
								a = (((!123) >= ((234 && (345 + 456)) || 567)) <= (678 != x::$a));
							} Else {
								x.a() = abc * def / 0b10;
							}
						}
					}
				}
				Class Program {}
			"""
        expect = "Error on line 8 col 14: ="
        self.assertTrue(TestParser.test(input, expect, 14))

    def test_15(self):
        ## TODO: Test utils:
        input = """
				Class TestUtils : TestCase {
					Test2() {
						Foreach(a::$foo().b In abc .. def By "This is abc" +. "def"){
							If (!True) {
								a = (((!123) >= ((234 && (345 + 456)) || 567)) <= (678 != x::$a));
							} Else {
								x.a().f = abc * def / 010;
								a = b % c * "Int def";
							}
						}
					}
				}
				Class Program {}
			"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 15))







