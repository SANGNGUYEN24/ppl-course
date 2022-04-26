import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_101(self):
        # TODO: Test parameters in main() of Program class
        input = """
			Class Program {
				main(a: Int; b,c: Float) {}
			}
		"""
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),FloatType)],Block([]))])])"""
        self.assertTrue(TestAST.test(input, expect, 101))

    def test_102(self):
        # TODO: Test Return in main() pf Program class -v1
        input = """
			Class Program {
				main() { Return abc; }
			}
		"""
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(Id(abc))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 102))

    def test_103(self):
        # TODO: Test method declaration except main() in Program
        input = """
				Class Program {
					main() {
						Out.printStatus("Program is running");
					}

					println(a,b: Int) {
         		Return Out.printInt(a, b);
					}
					
					renderComp(c1, c2: Component) {
						Program.render(c1, c2);
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printStatus),[StringLit(Program is running)])])),MethodDecl(Id(println),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(CallExpr(Id(Out),Id(printInt),[Id(a),Id(b)]))])),MethodDecl(Id(renderComp),Instance,[param(Id(c1),ClassType(Id(Component))),param(Id(c2),ClassType(Id(Component)))],Block([Call(Id(Program),Id(render),[Id(c1),Id(c2)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 103))

    def test_104(self):
        # TODO: Test attribute declaration except main() in Program
        input = """
				Class Program {
					Val a, b: Int = 123, 0x56;
					Var c, d, e: Float = 1.20, 4.3e5, 15;

					printFloat(a: Float) {
						Return Out.printInt(a, b);
					}

					main() {
						Out.printStatus("Program is running");
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(123))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(86))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(1.2))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(430000.0))),AttributeDecl(Instance,VarDecl(Id(e),FloatType,IntLit(15))),MethodDecl(Id(printFloat),Instance,[param(Id(a),FloatType)],Block([Return(CallExpr(Id(Out),Id(printInt),[Id(a),Id(b)]))])),MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printStatus),[StringLit(Program is running)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 104))

    def test_105(self):
        # TODO: Test attribute declaration in class -v2:
        input = """
				Class People {
					Val $numOfPeople, Id: Int = 0x0, 123456789;
					Var name: String;
				}

				Class Student : People {
					Var stuID, $birthDate: MixedType = 1234567, "1/1/1970";
					Val $1per: Int = 0xA;
				}

				Class grade : FloatType {}
			"""
        expect = r"""Program([ClassDecl(Id(People),[AttributeDecl(Static,ConstDecl(Id($numOfPeople),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(Id),IntType,IntLit(123456789))),AttributeDecl(Instance,VarDecl(Id(name),StringType))]),ClassDecl(Id(Student),Id(People),[AttributeDecl(Instance,VarDecl(Id(stuID),ClassType(Id(MixedType)),IntLit(1234567))),AttributeDecl(Static,VarDecl(Id($birthDate),ClassType(Id(MixedType)),StringLit(1/1/1970))),AttributeDecl(Static,ConstDecl(Id($1per),IntType,IntLit(10)))]),ClassDecl(Id(grade),Id(FloatType),[])])"""
        self.assertTrue(TestAST.test(input, expect, 105))

    def test_106(self):
        # TODO: Test attribute declaration in class -v4:
        input = """
				Class People {
					Val $numOfPeople, Id: Int = 0x0, 123456789;
					Var name: String;
				}

				Class Student : People {
					Var stuID, $birthDate: MixedType = 1234567, "1/1/1970";
					Val $1per: Int = 0xA;
					Val listGrade: Array[Float, 0b1];
					Var $listOfListGrade: Array[Array[Float, 01], 0x2];
				}

				Class grade : FloatType {}
			"""
        expect = r"""Program([ClassDecl(Id(People),[AttributeDecl(Static,ConstDecl(Id($numOfPeople),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(Id),IntType,IntLit(123456789))),AttributeDecl(Instance,VarDecl(Id(name),StringType))]),ClassDecl(Id(Student),Id(People),[AttributeDecl(Instance,VarDecl(Id(stuID),ClassType(Id(MixedType)),IntLit(1234567))),AttributeDecl(Static,VarDecl(Id($birthDate),ClassType(Id(MixedType)),StringLit(1/1/1970))),AttributeDecl(Static,ConstDecl(Id($1per),IntType,IntLit(10))),AttributeDecl(Instance,ConstDecl(Id(listGrade),ArrayType(1,FloatType),None)),AttributeDecl(Static,VarDecl(Id($listOfListGrade),ArrayType(2,ArrayType(1,FloatType))))]),ClassDecl(Id(grade),Id(FloatType),[])])"""
        self.assertTrue(TestAST.test(input, expect, 106))

    def test_107(self):
        # TODO: Test attribute declaration in class -v5:
        input = """
				Class People {
					Val $numOfPeople, Id: Int = 0x0, 123456789;
					Var name: String;
				}

				Class Student : People {
					Var stuID, $birthDate: MixedType = 1234567, "1/1/1970";
					Val $1per: Int = 0xA;
					Val listGrade: Array[Float, 0b1];
					Var $listOfListGrade: Array[Array[Float, 01], 0x2] = Array(
						Array(
							New Grade(1)
						),
						Array(
							New Grade(2)
						)
					);
				}

				Class grade: FloatType {
					Var mark: Int;
				}
			"""
        expect = r"""Program([ClassDecl(Id(People),[AttributeDecl(Static,ConstDecl(Id($numOfPeople),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(Id),IntType,IntLit(123456789))),AttributeDecl(Instance,VarDecl(Id(name),StringType))]),ClassDecl(Id(Student),Id(People),[AttributeDecl(Instance,VarDecl(Id(stuID),ClassType(Id(MixedType)),IntLit(1234567))),AttributeDecl(Static,VarDecl(Id($birthDate),ClassType(Id(MixedType)),StringLit(1/1/1970))),AttributeDecl(Static,ConstDecl(Id($1per),IntType,IntLit(10))),AttributeDecl(Instance,ConstDecl(Id(listGrade),ArrayType(1,FloatType),None)),AttributeDecl(Static,VarDecl(Id($listOfListGrade),ArrayType(2,ArrayType(1,FloatType)),[[NewExpr(Id(Grade),[IntLit(1)])],[NewExpr(Id(Grade),[IntLit(2)])]]))]),ClassDecl(Id(grade),Id(FloatType),[AttributeDecl(Instance,VarDecl(Id(mark),IntType))])])"""
        self.assertTrue(TestAST.test(input, expect, 107))

    def test_108(self):
        # TODO: Test constructor and destructor -v1:
        input = """
				Class People {
					Val $numOfPeople, Id: Int = 0x0, 123456789;
					Var name: String;
				}

				Class Student : People {
					Var stuID, $birthDate: MixedType = 1234567, "1/1/1970";
					Val $1per: Int = 0xA;
					Val listGrade: Array[Float, 0b1];
					Var $listOfListGrade: Array[Array[Float, 01], 0x2] = Array(
						Array(
							New Grade(1)
						),
						Array(
							New Grade(2)
						)
					);

					$123setStudentID (a, b: String; c: RanNumb) {
						Return Student::$stuID;
					}
				}

				Class grade: FloatType {
					Var mark: Int;
					Constructor () {}
					Destructor () {
						Return grade::$a;
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(People),[AttributeDecl(Static,ConstDecl(Id($numOfPeople),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(Id),IntType,IntLit(123456789))),AttributeDecl(Instance,VarDecl(Id(name),StringType))]),ClassDecl(Id(Student),Id(People),[AttributeDecl(Instance,VarDecl(Id(stuID),ClassType(Id(MixedType)),IntLit(1234567))),AttributeDecl(Static,VarDecl(Id($birthDate),ClassType(Id(MixedType)),StringLit(1/1/1970))),AttributeDecl(Static,ConstDecl(Id($1per),IntType,IntLit(10))),AttributeDecl(Instance,ConstDecl(Id(listGrade),ArrayType(1,FloatType),None)),AttributeDecl(Static,VarDecl(Id($listOfListGrade),ArrayType(2,ArrayType(1,FloatType)),[[NewExpr(Id(Grade),[IntLit(1)])],[NewExpr(Id(Grade),[IntLit(2)])]])),MethodDecl(Id($123setStudentID),Static,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),ClassType(Id(RanNumb)))],Block([Return(FieldAccess(Id(Student),Id($stuID)))]))]),ClassDecl(Id(grade),Id(FloatType),[AttributeDecl(Instance,VarDecl(Id(mark),IntType)),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([Return(FieldAccess(Id(grade),Id($a)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 108))

    def test_109(self):
        # TODO: Test constructor and destructor -v3:
        input = """
				Class People {
					Val $numOfPeople, Id: Int = 0x0, 123456789;
					Var name: String;
				}

				Class Student : People {
					Var stuID, $birthDate: MixedType = 1234567, "1/1/1970";
					Val $1per: Int = 0xA;
					Val listGrade: Array[Float, 0b1];
					Var $listOfListGrade: Array[Array[Float, 01], 0x2] = Array(
						Array(
							New Grade(1)
						),
						Array(
							New Grade(2)
						)
					);

					$123setStudentID (a, b: String; c: RanNumb) {
						Return Student::$stuID;
					}
				}

				Class grade: FloatType {
					Var mark: Int;
					Constructor (a, b: IntType) {
						mark = grade::$a;
					}
					Destructor () {
						Out.printStatus("Destructor of grade");
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(People),[AttributeDecl(Static,ConstDecl(Id($numOfPeople),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(Id),IntType,IntLit(123456789))),AttributeDecl(Instance,VarDecl(Id(name),StringType))]),ClassDecl(Id(Student),Id(People),[AttributeDecl(Instance,VarDecl(Id(stuID),ClassType(Id(MixedType)),IntLit(1234567))),AttributeDecl(Static,VarDecl(Id($birthDate),ClassType(Id(MixedType)),StringLit(1/1/1970))),AttributeDecl(Static,ConstDecl(Id($1per),IntType,IntLit(10))),AttributeDecl(Instance,ConstDecl(Id(listGrade),ArrayType(1,FloatType),None)),AttributeDecl(Static,VarDecl(Id($listOfListGrade),ArrayType(2,ArrayType(1,FloatType)),[[NewExpr(Id(Grade),[IntLit(1)])],[NewExpr(Id(Grade),[IntLit(2)])]])),MethodDecl(Id($123setStudentID),Static,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),ClassType(Id(RanNumb)))],Block([Return(FieldAccess(Id(Student),Id($stuID)))]))]),ClassDecl(Id(grade),Id(FloatType),[AttributeDecl(Instance,VarDecl(Id(mark),IntType)),MethodDecl(Id(Constructor),Instance,[param(Id(a),ClassType(Id(IntType))),param(Id(b),ClassType(Id(IntType)))],Block([AssignStmt(Id(mark),FieldAccess(Id(grade),Id($a)))])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(Out),Id(printStatus),[StringLit(Destructor of grade)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 109))

    def test_110(self):
        # TODO: Test literals -v3:
        input = """
				Class TestLiterals {
					IntLit() {
						Val a, b, c: Int = 0x123, 0b0, 0765;
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestLiterals),[MethodDecl(Id(IntLit),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(291)),ConstDecl(Id(b),IntType,IntLit(0)),ConstDecl(Id(c),IntType,IntLit(501))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 110))

    def test_111(self):
        # TODO: Test literals -v5:
        input = """
				Class TestLiterals {
					IntLit() {
						Val a, b, c: Int = 0x1_2_3, 0b0, 07_6_5;
					}
					FloatLit() {
						Var x1, x2: Float = 1.e234, 5E678;
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestLiterals),[MethodDecl(Id(IntLit),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(291)),ConstDecl(Id(b),IntType,IntLit(0)),ConstDecl(Id(c),IntType,IntLit(501))])),MethodDecl(Id(FloatLit),Instance,[],Block([VarDecl(Id(x1),FloatType,FloatLit(1e+234)),VarDecl(Id(x2),FloatType,FloatLit(inf))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 111))

    def test_112(self):
        # TODO: Test literals -v9:
        input = """
				Class TestLiterals {
					IntLit() {
						Val a, b, c: Int = 0x1_2_3, 0b0, 07_6_5;
					}
					FloatLit() {
						Var x1, x2: Float = 1.e234, 5E-678;
						Val x3, x4: Float = 1_234E567, 0.E123;
						Val x5: Float = 0.123;
						Var x6, x7: Float = 12.3e5, 1.e+2;
					}
					BoolLit() {
						Val a : Bool = True;
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestLiterals),[MethodDecl(Id(IntLit),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(291)),ConstDecl(Id(b),IntType,IntLit(0)),ConstDecl(Id(c),IntType,IntLit(501))])),MethodDecl(Id(FloatLit),Instance,[],Block([VarDecl(Id(x1),FloatType,FloatLit(1e+234)),VarDecl(Id(x2),FloatType,FloatLit(0.0)),ConstDecl(Id(x3),FloatType,FloatLit(inf)),ConstDecl(Id(x4),FloatType,FloatLit(0.0)),ConstDecl(Id(x5),FloatType,FloatLit(0.123)),VarDecl(Id(x6),FloatType,FloatLit(1230000.0)),VarDecl(Id(x7),FloatType,FloatLit(100.0))])),MethodDecl(Id(BoolLit),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(Bool)),BooleanLit(True))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 112))

    def test_113(self):
        # TODO: Test literals -v10:
        input = """
				Class TestLiterals {
					IntLit() {
						Val a, b, c: Int = 0x1_2_3, 0b0, 07_6_5;
					}
					FloatLit() {
						Var x1, x2: Float = 1.e234, 5E-678;
						Val x3, x4: Float = 1_234E567, 0.E123;
						Val x5: Float = 0.123;
						Var x6, x7: Float = 12.3e5, 1.e+2;
					}
					BoolLit() {
						Val a : Bool = True;
					}
					StringLit() {
						Var str1: String = "Left-hand-side tab string \\t, Right-hand-side";
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestLiterals),[MethodDecl(Id(IntLit),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(291)),ConstDecl(Id(b),IntType,IntLit(0)),ConstDecl(Id(c),IntType,IntLit(501))])),MethodDecl(Id(FloatLit),Instance,[],Block([VarDecl(Id(x1),FloatType,FloatLit(1e+234)),VarDecl(Id(x2),FloatType,FloatLit(0.0)),ConstDecl(Id(x3),FloatType,FloatLit(inf)),ConstDecl(Id(x4),FloatType,FloatLit(0.0)),ConstDecl(Id(x5),FloatType,FloatLit(0.123)),VarDecl(Id(x6),FloatType,FloatLit(1230000.0)),VarDecl(Id(x7),FloatType,FloatLit(100.0))])),MethodDecl(Id(BoolLit),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(Bool)),BooleanLit(True))])),MethodDecl(Id(StringLit),Instance,[],Block([VarDecl(Id(str1),StringType,StringLit(Left-hand-side tab string \t, Right-hand-side))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 113))

    def test_114(self):
        # TODO: Test literals -v11:
        input = """
				Class TestLiterals {
					IntLit() {
						Val a, b, c: Int = 0x1_2_3, 0b0, 07_6_5;
					}
					FloatLit() {
						Var x1, x2: Float = 1.e234, 5E-678;
						Val x3, x4: Float = 1_234E567, 0.E123;
						Val x5: Float = 0.123;
						Var x6, x7: Float = 12.3e5, 1.e+2;
					}
					BoolLit() {
						Val a : Bool = True;
					}
					StringLit() {
						Var str1: String = "Left-hand-side tab string \\t" +. "Right-hand-side";
						Val str2: String = "She asked me: '"When do you finish your work?'"";
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestLiterals),[MethodDecl(Id(IntLit),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(291)),ConstDecl(Id(b),IntType,IntLit(0)),ConstDecl(Id(c),IntType,IntLit(501))])),MethodDecl(Id(FloatLit),Instance,[],Block([VarDecl(Id(x1),FloatType,FloatLit(1e+234)),VarDecl(Id(x2),FloatType,FloatLit(0.0)),ConstDecl(Id(x3),FloatType,FloatLit(inf)),ConstDecl(Id(x4),FloatType,FloatLit(0.0)),ConstDecl(Id(x5),FloatType,FloatLit(0.123)),VarDecl(Id(x6),FloatType,FloatLit(1230000.0)),VarDecl(Id(x7),FloatType,FloatLit(100.0))])),MethodDecl(Id(BoolLit),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(Bool)),BooleanLit(True))])),MethodDecl(Id(StringLit),Instance,[],Block([VarDecl(Id(str1),StringType,BinaryOp(+.,StringLit(Left-hand-side tab string \t),StringLit(Right-hand-side))),ConstDecl(Id(str2),StringType,StringLit(She asked me: '"When do you finish your work?'"))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 114))

    def test_115(self):
        # TODO: Test literals -v13:
        input = """
				Class TestLiterals {
					IntLit() {
						Val a, b, c: Int = 0x1_2_3, 0b0, 07_6_5;
					}
					FloatLit() {
						Var x1, x2: Float = 1.e234, 5E-678;
						Val x3, x4: Float = 1_234E567, 0.E123;
						Val x5: Float = 0.123;
						Var x6, x7: Float = 12.3e5, 1.e+2;
					}
					BoolLit() {
						Val a : Bool = True;
					}
					StringLit() {
						Var str1: String = "Left-hand-side tab string" +. "Right-hand-side";
						Val str2: String = "She asked me: '"When do you finish your work?'" \\b\\f\\r\\n\\t\\'to buy some food";
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestLiterals),[MethodDecl(Id(IntLit),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(291)),ConstDecl(Id(b),IntType,IntLit(0)),ConstDecl(Id(c),IntType,IntLit(501))])),MethodDecl(Id(FloatLit),Instance,[],Block([VarDecl(Id(x1),FloatType,FloatLit(1e+234)),VarDecl(Id(x2),FloatType,FloatLit(0.0)),ConstDecl(Id(x3),FloatType,FloatLit(inf)),ConstDecl(Id(x4),FloatType,FloatLit(0.0)),ConstDecl(Id(x5),FloatType,FloatLit(0.123)),VarDecl(Id(x6),FloatType,FloatLit(1230000.0)),VarDecl(Id(x7),FloatType,FloatLit(100.0))])),MethodDecl(Id(BoolLit),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(Bool)),BooleanLit(True))])),MethodDecl(Id(StringLit),Instance,[],Block([VarDecl(Id(str1),StringType,BinaryOp(+.,StringLit(Left-hand-side tab string),StringLit(Right-hand-side))),ConstDecl(Id(str2),StringType,StringLit(She asked me: '"When do you finish your work?'" \b\f\r\n\t\'to buy some food))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 115))

    def test_116(self):
        # TODO: Test literals -v14:
        input = """
				Class TestLiterals {
					IntLit() {
						Val a, b, c: Int = 0x1_2_3, 0b0, 07_6_5;
					}
					FloatLit() {
						Var x1, x2: Float = 1.e234, 5E-678;
						Val x3, x4: Float = 1_234E567, 0.E123;
						Val x5: Float = 0.123;
						Var x6, x7: Float = 12.3e5, 1.e+2;
					}
					BoolLit() {
						Val a : Bool = True;
					}
					StringLit() {
						Var str1: String = "Left-hand-side tab string" +. "Right-hand-side";
						Val str2: String = "She asked me: '"When do you finish your work?'" \\b\\f\\r\\n\\t\\'to buy some food";
					}
					ArrayLit() {
						Val arr1: Array[String, 3] = Array(
							123,
							1E+23,
							".e23"
						);
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestLiterals),[MethodDecl(Id(IntLit),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(291)),ConstDecl(Id(b),IntType,IntLit(0)),ConstDecl(Id(c),IntType,IntLit(501))])),MethodDecl(Id(FloatLit),Instance,[],Block([VarDecl(Id(x1),FloatType,FloatLit(1e+234)),VarDecl(Id(x2),FloatType,FloatLit(0.0)),ConstDecl(Id(x3),FloatType,FloatLit(inf)),ConstDecl(Id(x4),FloatType,FloatLit(0.0)),ConstDecl(Id(x5),FloatType,FloatLit(0.123)),VarDecl(Id(x6),FloatType,FloatLit(1230000.0)),VarDecl(Id(x7),FloatType,FloatLit(100.0))])),MethodDecl(Id(BoolLit),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(Bool)),BooleanLit(True))])),MethodDecl(Id(StringLit),Instance,[],Block([VarDecl(Id(str1),StringType,BinaryOp(+.,StringLit(Left-hand-side tab string),StringLit(Right-hand-side))),ConstDecl(Id(str2),StringType,StringLit(She asked me: '"When do you finish your work?'" \b\f\r\n\t\'to buy some food))])),MethodDecl(Id(ArrayLit),Instance,[],Block([ConstDecl(Id(arr1),ArrayType(3,StringType),[IntLit(123),FloatLit(1e+23),StringLit(.e23)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 116))

    def test_117(self):
        # TODO: Test expression -v1
        input = """
				Class TestExpression {
					Val $a: Float = 0XAF08/0b11*(0x7-4)+05%-7.E-8;
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestExpression),[AttributeDecl(Static,ConstDecl(Id($a),FloatType,BinaryOp(+,BinaryOp(*,BinaryOp(/,IntLit(44808),IntLit(3)),BinaryOp(-,IntLit(7),IntLit(4))),BinaryOp(%,IntLit(5),UnaryOp(-,FloatLit(7e-08))))))])])"""
        self.assertTrue(TestAST.test(input, expect, 117))

    def test_118(self):
        # TODO: Test expression -v4
        input = """
				Class TestExpression {
					Val $a: Float = 0XAF08/0b11*(0x7-4)+05%-7.E-8;
					Var b: Float = !123 >= 234 && 345 + 456 || 567 - (678 != TestExpression::$a);
					Var c: String = "First Part" +. "Second Part" - "Third Part";
					Val $d: Expr4 = New Expr4(a + (b || c) % 10 / 11, a);
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestExpression),[AttributeDecl(Static,ConstDecl(Id($a),FloatType,BinaryOp(+,BinaryOp(*,BinaryOp(/,IntLit(44808),IntLit(3)),BinaryOp(-,IntLit(7),IntLit(4))),BinaryOp(%,IntLit(5),UnaryOp(-,FloatLit(7e-08)))))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,BinaryOp(>=,UnaryOp(!,IntLit(123)),BinaryOp(||,BinaryOp(&&,IntLit(234),BinaryOp(+,IntLit(345),IntLit(456))),BinaryOp(-,IntLit(567),BinaryOp(!=,IntLit(678),FieldAccess(Id(TestExpression),Id($a)))))))),AttributeDecl(Instance,VarDecl(Id(c),StringType,BinaryOp(+.,StringLit(First Part),BinaryOp(-,StringLit(Second Part),StringLit(Third Part))))),AttributeDecl(Static,ConstDecl(Id($d),ClassType(Id(Expr4)),NewExpr(Id(Expr4),[BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(%,BinaryOp(||,Id(b),Id(c)),IntLit(10)),IntLit(11))),Id(a)])))])])"""
        self.assertTrue(TestAST.test(input, expect, 118))

    def test_119(self):
        # TODO: Test expression -v5
        input = """
				Class TestExpression {
					Val $a: Float = 0XAF08/0b11*(0x7-4)+05%-7.E-8;
					Var b: Float = !123 >= 234 && 345 + 456 || 567 - (678 != TestExpression::$a);
					Var c: String = "First Part" +. "Second Part" - "Third Part";
					Val $d: Expr4 = New Expr4(a + (b || c) % 10 / 11, a);

          Expr() {
            Var e: Expr5 = Expr5::$name("120" +. "numbers of persons", 50);
          }
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestExpression),[AttributeDecl(Static,ConstDecl(Id($a),FloatType,BinaryOp(+,BinaryOp(*,BinaryOp(/,IntLit(44808),IntLit(3)),BinaryOp(-,IntLit(7),IntLit(4))),BinaryOp(%,IntLit(5),UnaryOp(-,FloatLit(7e-08)))))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,BinaryOp(>=,UnaryOp(!,IntLit(123)),BinaryOp(||,BinaryOp(&&,IntLit(234),BinaryOp(+,IntLit(345),IntLit(456))),BinaryOp(-,IntLit(567),BinaryOp(!=,IntLit(678),FieldAccess(Id(TestExpression),Id($a)))))))),AttributeDecl(Instance,VarDecl(Id(c),StringType,BinaryOp(+.,StringLit(First Part),BinaryOp(-,StringLit(Second Part),StringLit(Third Part))))),AttributeDecl(Static,ConstDecl(Id($d),ClassType(Id(Expr4)),NewExpr(Id(Expr4),[BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(%,BinaryOp(||,Id(b),Id(c)),IntLit(10)),IntLit(11))),Id(a)]))),MethodDecl(Id(Expr),Instance,[],Block([VarDecl(Id(e),ClassType(Id(Expr5)),CallExpr(Id(Expr5),Id($name),[BinaryOp(+.,StringLit(120),StringLit(numbers of persons)),IntLit(50)]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 119))

    def test_120(self):
        # TODO: Test expression -v6
        input = """
				Class TestExpression {
					Val $a: Float = 0XAF08/0b11*(0x7-4)+05%-7.E-8;
					Var b: Float = !123 >= 234 && 345 + 456 || 567 - (678 != TestExpression::$a);
					Var c: String = "First Part" +. "Second Part" - "Third Part";
					Val $d: Expr4 = New Expr4(a + (b || c) % 10 / 11, a);

          Expr() {
						Var e: Expr5 = Expr5::$name("120" +. "numbers of persons", 50);
          	Val f: Array[Float, 2] = Array(
              New Expr6(1%2-34*9/10 ==. "Last string part"),
              New Expr6(New Expr7(6 + 1 + 2/10 * 3 || d))
            );
          }
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestExpression),[AttributeDecl(Static,ConstDecl(Id($a),FloatType,BinaryOp(+,BinaryOp(*,BinaryOp(/,IntLit(44808),IntLit(3)),BinaryOp(-,IntLit(7),IntLit(4))),BinaryOp(%,IntLit(5),UnaryOp(-,FloatLit(7e-08)))))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,BinaryOp(>=,UnaryOp(!,IntLit(123)),BinaryOp(||,BinaryOp(&&,IntLit(234),BinaryOp(+,IntLit(345),IntLit(456))),BinaryOp(-,IntLit(567),BinaryOp(!=,IntLit(678),FieldAccess(Id(TestExpression),Id($a)))))))),AttributeDecl(Instance,VarDecl(Id(c),StringType,BinaryOp(+.,StringLit(First Part),BinaryOp(-,StringLit(Second Part),StringLit(Third Part))))),AttributeDecl(Static,ConstDecl(Id($d),ClassType(Id(Expr4)),NewExpr(Id(Expr4),[BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(%,BinaryOp(||,Id(b),Id(c)),IntLit(10)),IntLit(11))),Id(a)]))),MethodDecl(Id(Expr),Instance,[],Block([VarDecl(Id(e),ClassType(Id(Expr5)),CallExpr(Id(Expr5),Id($name),[BinaryOp(+.,StringLit(120),StringLit(numbers of persons)),IntLit(50)])),ConstDecl(Id(f),ArrayType(2,FloatType),[NewExpr(Id(Expr6),[BinaryOp(==.,BinaryOp(-,BinaryOp(%,IntLit(1),IntLit(2)),BinaryOp(/,BinaryOp(*,IntLit(34),IntLit(9)),IntLit(10))),StringLit(Last string part))]),NewExpr(Id(Expr6),[NewExpr(Id(Expr7),[BinaryOp(||,BinaryOp(+,BinaryOp(+,IntLit(6),IntLit(1)),BinaryOp(*,BinaryOp(/,IntLit(2),IntLit(10)),IntLit(3))),Id(d))])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 120))

    def test_121(self):
        # TODO: Test expression -v7
        input = """
				Class TestExpression {
					Val $a: Float = 0XAF08/0b11*(0x7-4)+05%-7.E-8;
					Var b: Float = !123 >= 234 && 345 + 456 || 567 - (678 != TestExpression::$a);
					Var c: String = "First Part" +. "Second Part" - "Third Part";
					Val $d: Expr4 = New Expr4(a + (b || c) % 10 / 11, a);

          Expr() {
					  Var e: Expr5 = Expr5::$name("120" +. "numbers of persons", 50);
            Val f: Array[Float, 2] = Array(
                New Expr6(1%2-34*9/10 ==. "Last string part"),
                New Expr6(New Expr7(6 + 1 + 2/10 * 3 || d))
            );
            Var g: Array[Array[String, 1], 2] = Array(
                Array(
                    "Lorem ipsum dolor sit amet" ==. "consectetur adipiscing elit. Integer vel.",
                    "abc".xyz
                ),
                Array(
                    C.foo()
                )
            );
        	}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestExpression),[AttributeDecl(Static,ConstDecl(Id($a),FloatType,BinaryOp(+,BinaryOp(*,BinaryOp(/,IntLit(44808),IntLit(3)),BinaryOp(-,IntLit(7),IntLit(4))),BinaryOp(%,IntLit(5),UnaryOp(-,FloatLit(7e-08)))))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,BinaryOp(>=,UnaryOp(!,IntLit(123)),BinaryOp(||,BinaryOp(&&,IntLit(234),BinaryOp(+,IntLit(345),IntLit(456))),BinaryOp(-,IntLit(567),BinaryOp(!=,IntLit(678),FieldAccess(Id(TestExpression),Id($a)))))))),AttributeDecl(Instance,VarDecl(Id(c),StringType,BinaryOp(+.,StringLit(First Part),BinaryOp(-,StringLit(Second Part),StringLit(Third Part))))),AttributeDecl(Static,ConstDecl(Id($d),ClassType(Id(Expr4)),NewExpr(Id(Expr4),[BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(%,BinaryOp(||,Id(b),Id(c)),IntLit(10)),IntLit(11))),Id(a)]))),MethodDecl(Id(Expr),Instance,[],Block([VarDecl(Id(e),ClassType(Id(Expr5)),CallExpr(Id(Expr5),Id($name),[BinaryOp(+.,StringLit(120),StringLit(numbers of persons)),IntLit(50)])),ConstDecl(Id(f),ArrayType(2,FloatType),[NewExpr(Id(Expr6),[BinaryOp(==.,BinaryOp(-,BinaryOp(%,IntLit(1),IntLit(2)),BinaryOp(/,BinaryOp(*,IntLit(34),IntLit(9)),IntLit(10))),StringLit(Last string part))]),NewExpr(Id(Expr6),[NewExpr(Id(Expr7),[BinaryOp(||,BinaryOp(+,BinaryOp(+,IntLit(6),IntLit(1)),BinaryOp(*,BinaryOp(/,IntLit(2),IntLit(10)),IntLit(3))),Id(d))])])]),VarDecl(Id(g),ArrayType(2,ArrayType(1,StringType)),[[BinaryOp(==.,StringLit(Lorem ipsum dolor sit amet),StringLit(consectetur adipiscing elit. Integer vel.)),FieldAccess(StringLit(abc),Id(xyz))],[CallExpr(Id(C),Id(foo),[])]])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 121))

    def test_122(self):
        # TODO: Test expression -v10
        input = """
				Class TestExpression {
					Val $a: Float = 0XAF08/0b11*(0x7-4)+05%-7.E-8;
					Var b: Float = !123 >= 234 && 345 + 456 || 567 - (678 != TestExpression::$a);
					Var c: String = "First Part" +. "Second Part" - "Third Part";
					Val $d: Expr4 = New Expr4(a + (b || c) % 10 / 11, a);

          Expr() {
					  Var e: Expr5 = Expr5::$name("120" +. "numbers of persons", 50);
            Val f: Array[Float, 2] = Array(
                New Expr6(1%2-34*9/10 ==. "Last string part"),
                New Expr6(New Expr7(6 + 1 + 2/10 * 3 || d))
            );
            Var g: Array[Array[String, 1], 2] = Array(
                Array(
                    "Lorem ipsum dolor sit amet" ==. "consectetur adipiscing elit. Integer vel.",
                    "abc".xyz
                ),
                Array(
                    C.foo()
                )
            );
            Val h: Expr8 = a.foo();
            Var i: Expr9 = b._xyz;
            Val j: Expr10 = New X().Y();
          }
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestExpression),[AttributeDecl(Static,ConstDecl(Id($a),FloatType,BinaryOp(+,BinaryOp(*,BinaryOp(/,IntLit(44808),IntLit(3)),BinaryOp(-,IntLit(7),IntLit(4))),BinaryOp(%,IntLit(5),UnaryOp(-,FloatLit(7e-08)))))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,BinaryOp(>=,UnaryOp(!,IntLit(123)),BinaryOp(||,BinaryOp(&&,IntLit(234),BinaryOp(+,IntLit(345),IntLit(456))),BinaryOp(-,IntLit(567),BinaryOp(!=,IntLit(678),FieldAccess(Id(TestExpression),Id($a)))))))),AttributeDecl(Instance,VarDecl(Id(c),StringType,BinaryOp(+.,StringLit(First Part),BinaryOp(-,StringLit(Second Part),StringLit(Third Part))))),AttributeDecl(Static,ConstDecl(Id($d),ClassType(Id(Expr4)),NewExpr(Id(Expr4),[BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(%,BinaryOp(||,Id(b),Id(c)),IntLit(10)),IntLit(11))),Id(a)]))),MethodDecl(Id(Expr),Instance,[],Block([VarDecl(Id(e),ClassType(Id(Expr5)),CallExpr(Id(Expr5),Id($name),[BinaryOp(+.,StringLit(120),StringLit(numbers of persons)),IntLit(50)])),ConstDecl(Id(f),ArrayType(2,FloatType),[NewExpr(Id(Expr6),[BinaryOp(==.,BinaryOp(-,BinaryOp(%,IntLit(1),IntLit(2)),BinaryOp(/,BinaryOp(*,IntLit(34),IntLit(9)),IntLit(10))),StringLit(Last string part))]),NewExpr(Id(Expr6),[NewExpr(Id(Expr7),[BinaryOp(||,BinaryOp(+,BinaryOp(+,IntLit(6),IntLit(1)),BinaryOp(*,BinaryOp(/,IntLit(2),IntLit(10)),IntLit(3))),Id(d))])])]),VarDecl(Id(g),ArrayType(2,ArrayType(1,StringType)),[[BinaryOp(==.,StringLit(Lorem ipsum dolor sit amet),StringLit(consectetur adipiscing elit. Integer vel.)),FieldAccess(StringLit(abc),Id(xyz))],[CallExpr(Id(C),Id(foo),[])]]),ConstDecl(Id(h),ClassType(Id(Expr8)),CallExpr(Id(a),Id(foo),[])),VarDecl(Id(i),ClassType(Id(Expr9)),FieldAccess(Id(b),Id(_xyz))),ConstDecl(Id(j),ClassType(Id(Expr10)),CallExpr(NewExpr(Id(X),[]),Id(Y),[]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 122))

    def test_123(self):
        # TODO: Test expression -v10
        input = """
				Class TestExpression {
					Val $a: Float = 0XAF08/0b11*(0x7-4)+05%-7.E-8;
					Var b: Float = !123 >= 234 && 345 + 456 || 567 - (678 != TestExpression::$a);
					Var c: String = "First Part" +. "Second Part" - "Third Part";
					Val $d: Expr4 = New Expr4(a + (b || c) % 10 / 11, a);

          Expr() {
					  Var e: Expr5 = Expr5::$name("120" +. "numbers of persons", 50);
            Val f: Array[Float, 2] = Array(
                New Expr6(1%2-34*9/10 ==. "Last string part"),
                New Expr6(New Expr7(6 + 1 + 2/10 * 3 || d))
            );
            Var g: Array[Array[String, 1], 2] = Array(
                Array(
                    "Lorem ipsum dolor sit amet" ==. "consectetur adipiscing elit. Integer vel.",
                    "abc".xyz
                ),
                Array(
                    C.foo()
                )
            );
            Val h: Expr8 = a.foo();
            Var i: Expr9 = b._xyz;
            Val j: Expr10 = New X().Y();
          }

					Expr1() {
						Var x: Int = New A(Self.foo()+!a[b::$foo()*(Self.b-10%11-15)*25]%50&&True>=False||New B(6));
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestExpression),[AttributeDecl(Static,ConstDecl(Id($a),FloatType,BinaryOp(+,BinaryOp(*,BinaryOp(/,IntLit(44808),IntLit(3)),BinaryOp(-,IntLit(7),IntLit(4))),BinaryOp(%,IntLit(5),UnaryOp(-,FloatLit(7e-08)))))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,BinaryOp(>=,UnaryOp(!,IntLit(123)),BinaryOp(||,BinaryOp(&&,IntLit(234),BinaryOp(+,IntLit(345),IntLit(456))),BinaryOp(-,IntLit(567),BinaryOp(!=,IntLit(678),FieldAccess(Id(TestExpression),Id($a)))))))),AttributeDecl(Instance,VarDecl(Id(c),StringType,BinaryOp(+.,StringLit(First Part),BinaryOp(-,StringLit(Second Part),StringLit(Third Part))))),AttributeDecl(Static,ConstDecl(Id($d),ClassType(Id(Expr4)),NewExpr(Id(Expr4),[BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(%,BinaryOp(||,Id(b),Id(c)),IntLit(10)),IntLit(11))),Id(a)]))),MethodDecl(Id(Expr),Instance,[],Block([VarDecl(Id(e),ClassType(Id(Expr5)),CallExpr(Id(Expr5),Id($name),[BinaryOp(+.,StringLit(120),StringLit(numbers of persons)),IntLit(50)])),ConstDecl(Id(f),ArrayType(2,FloatType),[NewExpr(Id(Expr6),[BinaryOp(==.,BinaryOp(-,BinaryOp(%,IntLit(1),IntLit(2)),BinaryOp(/,BinaryOp(*,IntLit(34),IntLit(9)),IntLit(10))),StringLit(Last string part))]),NewExpr(Id(Expr6),[NewExpr(Id(Expr7),[BinaryOp(||,BinaryOp(+,BinaryOp(+,IntLit(6),IntLit(1)),BinaryOp(*,BinaryOp(/,IntLit(2),IntLit(10)),IntLit(3))),Id(d))])])]),VarDecl(Id(g),ArrayType(2,ArrayType(1,StringType)),[[BinaryOp(==.,StringLit(Lorem ipsum dolor sit amet),StringLit(consectetur adipiscing elit. Integer vel.)),FieldAccess(StringLit(abc),Id(xyz))],[CallExpr(Id(C),Id(foo),[])]]),ConstDecl(Id(h),ClassType(Id(Expr8)),CallExpr(Id(a),Id(foo),[])),VarDecl(Id(i),ClassType(Id(Expr9)),FieldAccess(Id(b),Id(_xyz))),ConstDecl(Id(j),ClassType(Id(Expr10)),CallExpr(NewExpr(Id(X),[]),Id(Y),[]))])),MethodDecl(Id(Expr1),Instance,[],Block([VarDecl(Id(x),IntType,NewExpr(Id(A),[BinaryOp(>=,BinaryOp(&&,BinaryOp(+,CallExpr(Self(),Id(foo),[]),BinaryOp(%,UnaryOp(!,ArrayCell(Id(a),[BinaryOp(*,BinaryOp(*,CallExpr(Id(b),Id($foo),[]),BinaryOp(-,BinaryOp(-,FieldAccess(Self(),Id(b)),BinaryOp(%,IntLit(10),IntLit(11))),IntLit(15))),IntLit(25))])),IntLit(50))),BooleanLit(True)),BinaryOp(||,BooleanLit(False),NewExpr(Id(B),[IntLit(6)])))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 123))

    def test_124(self):
        # TODO: Test statement
        input = """
					Class TestStatement {
						AssignSmt() {
							x::$atb = 123;
							x.attr = 456;
							y::$abc = 789*10%245&&True||!(1345-133);
							y::$a[1] = New X(-a[0]*3/10-102+5&&6||7<=20);
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(AssignSmt),Instance,[],Block([AssignStmt(FieldAccess(Id(x),Id($atb)),IntLit(123)),AssignStmt(FieldAccess(Id(x),Id(attr)),IntLit(456)),AssignStmt(FieldAccess(Id(y),Id($abc)),BinaryOp(||,BinaryOp(&&,BinaryOp(%,BinaryOp(*,IntLit(789),IntLit(10)),IntLit(245)),BooleanLit(True)),UnaryOp(!,BinaryOp(-,IntLit(1345),IntLit(133))))),AssignStmt(ArrayCell(FieldAccess(Id(y),Id($a)),[IntLit(1)]),NewExpr(Id(X),[BinaryOp(<=,BinaryOp(||,BinaryOp(&&,BinaryOp(+,BinaryOp(-,BinaryOp(/,BinaryOp(*,UnaryOp(-,ArrayCell(Id(a),[IntLit(0)])),IntLit(3)),IntLit(10)),IntLit(102)),IntLit(5)),IntLit(6)),IntLit(7)),IntLit(20))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 124))

    def test_125(self):
        # TODO: Test statement
        input = """
					Class TestStatement {
						AssignSmt() {
							x::$atb = 123;
							x.attr = 456;
							y::$a[1] = New X(-a[0]*3/10-102+5&&6||7<=20);
							y::$abc = 789*10%245&&True||!(1345-133);
							Self.xyz = Array(Array(
								!abc[10],
								-def*10
							), False&&1);
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(AssignSmt),Instance,[],Block([AssignStmt(FieldAccess(Id(x),Id($atb)),IntLit(123)),AssignStmt(FieldAccess(Id(x),Id(attr)),IntLit(456)),AssignStmt(ArrayCell(FieldAccess(Id(y),Id($a)),[IntLit(1)]),NewExpr(Id(X),[BinaryOp(<=,BinaryOp(||,BinaryOp(&&,BinaryOp(+,BinaryOp(-,BinaryOp(/,BinaryOp(*,UnaryOp(-,ArrayCell(Id(a),[IntLit(0)])),IntLit(3)),IntLit(10)),IntLit(102)),IntLit(5)),IntLit(6)),IntLit(7)),IntLit(20))])),AssignStmt(FieldAccess(Id(y),Id($abc)),BinaryOp(||,BinaryOp(&&,BinaryOp(%,BinaryOp(*,IntLit(789),IntLit(10)),IntLit(245)),BooleanLit(True)),UnaryOp(!,BinaryOp(-,IntLit(1345),IntLit(133))))),AssignStmt(FieldAccess(Self(),Id(xyz)),[[UnaryOp(!,ArrayCell(Id(abc),[IntLit(10)])),BinaryOp(*,UnaryOp(-,Id(def)),IntLit(10))],BinaryOp(&&,BooleanLit(False),IntLit(1))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 125))

    def test_126(self):
        # TODO: Test statement
        input = """
					Class TestStatement {
						AssignSmt() {
							x::$atb = 123;
							x.attr = 456;
							y::$a[1] = New X(-a[0]*3/10-102+5&&6||7<=20);
							y::$abc = 789*10%245&&True||!(1345-133);
							Self.xyz = Array(Array(
								!abc[10],
								-def*10
							), False&&1);
							str = "Lorem ipsum dolor sit amet. \\n";
							x1 = Self.a[New A()];
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(AssignSmt),Instance,[],Block([AssignStmt(FieldAccess(Id(x),Id($atb)),IntLit(123)),AssignStmt(FieldAccess(Id(x),Id(attr)),IntLit(456)),AssignStmt(ArrayCell(FieldAccess(Id(y),Id($a)),[IntLit(1)]),NewExpr(Id(X),[BinaryOp(<=,BinaryOp(||,BinaryOp(&&,BinaryOp(+,BinaryOp(-,BinaryOp(/,BinaryOp(*,UnaryOp(-,ArrayCell(Id(a),[IntLit(0)])),IntLit(3)),IntLit(10)),IntLit(102)),IntLit(5)),IntLit(6)),IntLit(7)),IntLit(20))])),AssignStmt(FieldAccess(Id(y),Id($abc)),BinaryOp(||,BinaryOp(&&,BinaryOp(%,BinaryOp(*,IntLit(789),IntLit(10)),IntLit(245)),BooleanLit(True)),UnaryOp(!,BinaryOp(-,IntLit(1345),IntLit(133))))),AssignStmt(FieldAccess(Self(),Id(xyz)),[[UnaryOp(!,ArrayCell(Id(abc),[IntLit(10)])),BinaryOp(*,UnaryOp(-,Id(def)),IntLit(10))],BinaryOp(&&,BooleanLit(False),IntLit(1))]),AssignStmt(Id(str),StringLit(Lorem ipsum dolor sit amet. \n)),AssignStmt(Id(x1),ArrayCell(FieldAccess(Self(),Id(a)),[NewExpr(Id(A),[])]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 126))

    def test_127(self):
        # TODO: Test statement
        input = """
					Class TestStatement {
						IfSmt() {
							If (0) {
								ele = True;
							}
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(IfSmt),Instance,[],Block([If(IntLit(0),Block([AssignStmt(Id(ele),BooleanLit(True))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 127))

    def test_128(self):
        # TODO: Test statement
        input = """
					Class TestStatement {
						IfSmt() {
							If (0) {
								ele = True;
							} Elseif (Array(1,2,3,4).length >= 10) {
								ele = 10;
							}
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(IfSmt),Instance,[],Block([If(IntLit(0),Block([AssignStmt(Id(ele),BooleanLit(True))]),If(BinaryOp(>=,FieldAccess([IntLit(1),IntLit(2),IntLit(3),IntLit(4)],Id(length)),IntLit(10)),Block([AssignStmt(Id(ele),IntLit(10))])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 128))

    def test_129(self):
        # TODO: Test statement
        input = """
					Class TestStatement {
						IfSmt() {
							If (0) {
								ele = True;
							} Elseif (Array(1,2,3,4).length >= 10) {
								ele = 10;
							} Elseif ("abc" +. "def") {
								ele = "abcdef";
							} Else {
								ele = False;
							}
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(IfSmt),Instance,[],Block([If(IntLit(0),Block([AssignStmt(Id(ele),BooleanLit(True))]),If(BinaryOp(>=,FieldAccess([IntLit(1),IntLit(2),IntLit(3),IntLit(4)],Id(length)),IntLit(10)),Block([AssignStmt(Id(ele),IntLit(10))]),If(BinaryOp(+.,StringLit(abc),StringLit(def)),Block([AssignStmt(Id(ele),StringLit(abcdef))]),Block([AssignStmt(Id(ele),BooleanLit(False))]))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 129))

    def test_130(self):
        # TODO: Test statement
        input = """
					Class TestStatement {
						IfSmt() {
							If (0) {
								ele = True;
							} Elseif (Array(1,2,3,4).length >= 10) {
								ele = 10;
							} Elseif ("abc" +. "def") {
								ele = "abcdef";
							} Else {
								ele = False;
								If ("a-z" > "A-Z") {
									ele = "a-z";
									Break;
								}
							}
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(IfSmt),Instance,[],Block([If(IntLit(0),Block([AssignStmt(Id(ele),BooleanLit(True))]),If(BinaryOp(>=,FieldAccess([IntLit(1),IntLit(2),IntLit(3),IntLit(4)],Id(length)),IntLit(10)),Block([AssignStmt(Id(ele),IntLit(10))]),If(BinaryOp(+.,StringLit(abc),StringLit(def)),Block([AssignStmt(Id(ele),StringLit(abcdef))]),Block([AssignStmt(Id(ele),BooleanLit(False)),If(BinaryOp(>,StringLit(a-z),StringLit(A-Z)),Block([AssignStmt(Id(ele),StringLit(a-z)),Break]))]))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 130))

    def test_131(self):
        # TODO: Test statement
        input = """
					Class TestStatement {
						IfSmt() {
							If (0) {
								ele = True;
							} Elseif (Array(1,2,3,4).length >= 10) {
								ele = 10;
							} Elseif ("abc" +. "def") {
								ele = "abcdef";
							} Else {
								ele = False;
								If ("a-z" > "A-Z") {
									ele = "a-z";
								} Else {
									ele = "A-Z";
									Return ele;
								}
							}
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(IfSmt),Instance,[],Block([If(IntLit(0),Block([AssignStmt(Id(ele),BooleanLit(True))]),If(BinaryOp(>=,FieldAccess([IntLit(1),IntLit(2),IntLit(3),IntLit(4)],Id(length)),IntLit(10)),Block([AssignStmt(Id(ele),IntLit(10))]),If(BinaryOp(+.,StringLit(abc),StringLit(def)),Block([AssignStmt(Id(ele),StringLit(abcdef))]),Block([AssignStmt(Id(ele),BooleanLit(False)),If(BinaryOp(>,StringLit(a-z),StringLit(A-Z)),Block([AssignStmt(Id(ele),StringLit(a-z))]),Block([AssignStmt(Id(ele),StringLit(A-Z)),Return(Id(ele))]))]))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 131))

    def test_132(self):
        # TODO: Test statement
        input = """
				Class TestStatement {
					LoopSmt() {
						Foreach ("abc".def In (3+1*(4-!10)) .. True&&100%50>=1) {}
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(LoopSmt),Instance,[],Block([For(FieldAccess(StringLit(abc),Id(def)),BinaryOp(+,IntLit(3),BinaryOp(*,IntLit(1),BinaryOp(-,IntLit(4),UnaryOp(!,IntLit(10))))),BinaryOp(>=,BinaryOp(&&,BooleanLit(True),BinaryOp(%,IntLit(100),IntLit(50))),IntLit(1)),IntLit(1),Block([])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 132))

    def test_133(self):
        # TODO: Test statement
        input = """
				Class TestStatement {
					LoopSmt() {
						Foreach ("abc".def In (3+1*(4-!10)) .. True&&100%50>=1 By Self[1]) {}
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(LoopSmt),Instance,[],Block([For(FieldAccess(StringLit(abc),Id(def)),BinaryOp(+,IntLit(3),BinaryOp(*,IntLit(1),BinaryOp(-,IntLit(4),UnaryOp(!,IntLit(10))))),BinaryOp(>=,BinaryOp(&&,BooleanLit(True),BinaryOp(%,IntLit(100),IntLit(50))),IntLit(1)),ArrayCell(Self(),[IntLit(1)]),Block([])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 133))

    def test_134(self):
        # TODO: Test statement
        input = """
				Class TestStatement {
					LoopSmt() {
						Foreach ("abc".def In (3+1*(4-!10)) .. True&&100%50>=1 By New X((1*ArrList[5]).def)) {
							Foreach(TestStatement::$x In ghi::$jkl() .. 123[5]) {
								If (TestStatement::$_123[Self.abc]) { Continue; }
								Return arr[New X()];
								var = New X().str;
								Val x: Array[Array[Array[Array[Int,0b1],0x1],01],1];
							}
						}

					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(LoopSmt),Instance,[],Block([For(FieldAccess(StringLit(abc),Id(def)),BinaryOp(+,IntLit(3),BinaryOp(*,IntLit(1),BinaryOp(-,IntLit(4),UnaryOp(!,IntLit(10))))),BinaryOp(>=,BinaryOp(&&,BooleanLit(True),BinaryOp(%,IntLit(100),IntLit(50))),IntLit(1)),NewExpr(Id(X),[FieldAccess(BinaryOp(*,IntLit(1),ArrayCell(Id(ArrList),[IntLit(5)])),Id(def))]),Block([For(FieldAccess(Id(TestStatement),Id($x)),CallExpr(Id(ghi),Id($jkl),[]),ArrayCell(IntLit(123),[IntLit(5)]),IntLit(1),Block([If(ArrayCell(FieldAccess(Id(TestStatement),Id($_123)),[FieldAccess(Self(),Id(abc))]),Block([Continue])),Return(ArrayCell(Id(arr),[NewExpr(Id(X),[])])),AssignStmt(Id(var),FieldAccess(NewExpr(Id(X),[]),Id(str))),ConstDecl(Id(x),ArrayType(1,ArrayType(1,ArrayType(1,ArrayType(1,IntType)))),None)])])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 134))

    def test_135(self):
        # TODO: Test statement
        input = """
				Class TestStatement {
					LoopSmt() {
						Foreach ("abc".def In (3+1*(4-!10)) .. True&&100%50>=1 By New X((1*ArrList[5]).def)) {
							Foreach(TestStatement::$x In ghi::$jkl() .. 123[5]) {
								If (TestStatement::$_123[Self.abc]) { Continue; }
								Return arr[New X()];
								var = New X().str;
								Val x: Array[Array[Array[Array[Int,0b1],0x1],01],1];
							}
							X::$getValue();
							Y.scrollToView(char::$abc);
							Obj.foo().name = "Lorem ipsum dolor sit amet \\n" +. "\\t\'"\\b";
						}
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(LoopSmt),Instance,[],Block([For(FieldAccess(StringLit(abc),Id(def)),BinaryOp(+,IntLit(3),BinaryOp(*,IntLit(1),BinaryOp(-,IntLit(4),UnaryOp(!,IntLit(10))))),BinaryOp(>=,BinaryOp(&&,BooleanLit(True),BinaryOp(%,IntLit(100),IntLit(50))),IntLit(1)),NewExpr(Id(X),[FieldAccess(BinaryOp(*,IntLit(1),ArrayCell(Id(ArrList),[IntLit(5)])),Id(def))]),Block([For(FieldAccess(Id(TestStatement),Id($x)),CallExpr(Id(ghi),Id($jkl),[]),ArrayCell(IntLit(123),[IntLit(5)]),IntLit(1),Block([If(ArrayCell(FieldAccess(Id(TestStatement),Id($_123)),[FieldAccess(Self(),Id(abc))]),Block([Continue])),Return(ArrayCell(Id(arr),[NewExpr(Id(X),[])])),AssignStmt(Id(var),FieldAccess(NewExpr(Id(X),[]),Id(str))),ConstDecl(Id(x),ArrayType(1,ArrayType(1,ArrayType(1,ArrayType(1,IntType)))),None)])]),Call(Id(X),Id($getValue),[]),Call(Id(Y),Id(scrollToView),[FieldAccess(Id(char),Id($abc))]),AssignStmt(FieldAccess(CallExpr(Id(Obj),Id(foo),[]),Id(name)),BinaryOp(+.,StringLit(Lorem ipsum dolor sit amet \n),StringLit(\t'"\b)))])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 135))

    def test_136(self):
        # TODO: Test statement:
        input = """
				Class TestStatement {
					LoopSmt() {
						Foreach ("abc".def In (3+1*(4-!10)) .. True&&100%50>=1 By New X((1*ArrList[5]).def)) {
							Foreach(TestStatement::$x In ghi::$jkl() .. 123[5]) {
								If (TestStatement::$_123[Self.abc]) { Continue; }
								Return arr[New X()];
								var = New X().str;
								Val x: Array[Array[Array[Array[Int,0b1],0x1],01],1];
							}
							X::$getValue();
							Y.scrollToView(char::$abc);
							Obj.foo().name = "Lorem ipsum dolor sit amet \\n" +. "\\t\'"\\b";
							Val listArr: Array[Array[Float, 0XAF], 0b1011] = Array(Array(Array(Array(1), Array(1)), Array(Array(1), Array(1))), Array(Array(Array(1), Array(1)), Array(Array(1), Array(1))));
						}
					}
				}
			"""
        expect = r"""Program([ClassDecl(Id(TestStatement),[MethodDecl(Id(LoopSmt),Instance,[],Block([For(FieldAccess(StringLit(abc),Id(def)),BinaryOp(+,IntLit(3),BinaryOp(*,IntLit(1),BinaryOp(-,IntLit(4),UnaryOp(!,IntLit(10))))),BinaryOp(>=,BinaryOp(&&,BooleanLit(True),BinaryOp(%,IntLit(100),IntLit(50))),IntLit(1)),NewExpr(Id(X),[FieldAccess(BinaryOp(*,IntLit(1),ArrayCell(Id(ArrList),[IntLit(5)])),Id(def))]),Block([For(FieldAccess(Id(TestStatement),Id($x)),CallExpr(Id(ghi),Id($jkl),[]),ArrayCell(IntLit(123),[IntLit(5)]),IntLit(1),Block([If(ArrayCell(FieldAccess(Id(TestStatement),Id($_123)),[FieldAccess(Self(),Id(abc))]),Block([Continue])),Return(ArrayCell(Id(arr),[NewExpr(Id(X),[])])),AssignStmt(Id(var),FieldAccess(NewExpr(Id(X),[]),Id(str))),ConstDecl(Id(x),ArrayType(1,ArrayType(1,ArrayType(1,ArrayType(1,IntType)))),None)])]),Call(Id(X),Id($getValue),[]),Call(Id(Y),Id(scrollToView),[FieldAccess(Id(char),Id($abc))]),AssignStmt(FieldAccess(CallExpr(Id(Obj),Id(foo),[]),Id(name)),BinaryOp(+.,StringLit(Lorem ipsum dolor sit amet \n),StringLit(\t'"\b))),ConstDecl(Id(listArr),ArrayType(11,ArrayType(175,FloatType)),[[[[IntLit(1)],[IntLit(1)]],[[IntLit(1)],[IntLit(1)]]],[[[IntLit(1)],[IntLit(1)]],[[IntLit(1)],[IntLit(1)]]]])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 136))

    def test_137(self):
        # TODO: Test extras:
        input = """
					Class TestExtras {
						Test1(x: Number){ x=-1; }
						Test2(){
							x1::$a = New X(New Y().z);
							x2 = Array(123,"abc","def",456) - x3::$2803_01[x.y()];
						}
						Test3(){ x = "Lorem ipsum dolor sit amet,\\n consectetur adipiscing elit"; }
						Test4(){
							(19>(_18._28())*Cat::$getObj().name[125])[True] = (23>18&&(15%New X(New ABC(86*!0)))/Dog::$numDogs)[15];
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestExtras),[MethodDecl(Id(Test1),Instance,[param(Id(x),ClassType(Id(Number)))],Block([AssignStmt(Id(x),UnaryOp(-,IntLit(1)))])),MethodDecl(Id(Test2),Instance,[],Block([AssignStmt(FieldAccess(Id(x1),Id($a)),NewExpr(Id(X),[FieldAccess(NewExpr(Id(Y),[]),Id(z))])),AssignStmt(Id(x2),BinaryOp(-,[IntLit(123),StringLit(abc),StringLit(def),IntLit(456)],ArrayCell(FieldAccess(Id(x3),Id($2803_01)),[CallExpr(Id(x),Id(y),[])])))])),MethodDecl(Id(Test3),Instance,[],Block([AssignStmt(Id(x),StringLit(Lorem ipsum dolor sit amet,\n consectetur adipiscing elit))])),MethodDecl(Id(Test4),Instance,[],Block([AssignStmt(ArrayCell(BinaryOp(>,IntLit(19),BinaryOp(*,CallExpr(Id(_18),Id(_28),[]),ArrayCell(FieldAccess(CallExpr(Id(Cat),Id($getObj),[]),Id(name)),[IntLit(125)]))),[BooleanLit(True)]),ArrayCell(BinaryOp(>,IntLit(23),BinaryOp(&&,IntLit(18),BinaryOp(/,BinaryOp(%,IntLit(15),NewExpr(Id(X),[NewExpr(Id(ABC),[BinaryOp(*,IntLit(86),UnaryOp(!,IntLit(0)))])])),FieldAccess(Id(Dog),Id($numDogs))))),[IntLit(15)]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 137))

    def test_138(self):
        # TODO: Test extras:
        input = """
					Class TestExtras {
						Test1(x: Number){ x=-1; }
						Test2(){
							x1::$a = New X(New Y().z);
							x2 = Array(123,"abc","def",456) - x3::$2803_01[x.y()];
						}
						Test3(){ x = "Lorem ipsum dolor sit amet,\\n consectetur adipiscing elit"; }
						Test4(){ (19>(_18._28())*Cat::$getObj().name[125])[True] = (23>18&&(15%New X(New ABC(86*!0)))/Dog::$numDogs)[15]; }
						Test5(){
							legalSmt = (((!123) >= ((234 && (345 > 456)) || 567)) <= (678 != Num::$a));
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestExtras),[MethodDecl(Id(Test1),Instance,[param(Id(x),ClassType(Id(Number)))],Block([AssignStmt(Id(x),UnaryOp(-,IntLit(1)))])),MethodDecl(Id(Test2),Instance,[],Block([AssignStmt(FieldAccess(Id(x1),Id($a)),NewExpr(Id(X),[FieldAccess(NewExpr(Id(Y),[]),Id(z))])),AssignStmt(Id(x2),BinaryOp(-,[IntLit(123),StringLit(abc),StringLit(def),IntLit(456)],ArrayCell(FieldAccess(Id(x3),Id($2803_01)),[CallExpr(Id(x),Id(y),[])])))])),MethodDecl(Id(Test3),Instance,[],Block([AssignStmt(Id(x),StringLit(Lorem ipsum dolor sit amet,\n consectetur adipiscing elit))])),MethodDecl(Id(Test4),Instance,[],Block([AssignStmt(ArrayCell(BinaryOp(>,IntLit(19),BinaryOp(*,CallExpr(Id(_18),Id(_28),[]),ArrayCell(FieldAccess(CallExpr(Id(Cat),Id($getObj),[]),Id(name)),[IntLit(125)]))),[BooleanLit(True)]),ArrayCell(BinaryOp(>,IntLit(23),BinaryOp(&&,IntLit(18),BinaryOp(/,BinaryOp(%,IntLit(15),NewExpr(Id(X),[NewExpr(Id(ABC),[BinaryOp(*,IntLit(86),UnaryOp(!,IntLit(0)))])])),FieldAccess(Id(Dog),Id($numDogs))))),[IntLit(15)]))])),MethodDecl(Id(Test5),Instance,[],Block([AssignStmt(Id(legalSmt),BinaryOp(<=,BinaryOp(>=,UnaryOp(!,IntLit(123)),BinaryOp(||,BinaryOp(&&,IntLit(234),BinaryOp(>,IntLit(345),IntLit(456))),IntLit(567))),BinaryOp(!=,IntLit(678),FieldAccess(Id(Num),Id($a)))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 138))

    def test_139(self):
        # TODO: Test extras:
        input = """
					Class TestExtras {
						Test1(x: Number){ x=-1; }
						Test2(){
							x1::$a = New X(New Y().z);
							x2 = Array(123,"abc","def",456) - x3::$2803_01[x.y()];
						}
						Test3(){ x = "Lorem ipsum dolor sit amet,\\n consectetur adipiscing elit"; }
						Test4(){ (19>(_18._28())*Cat::$getObj().name[125])[True] = (23>18&&(15%New X(New ABC(86*!0)))/Dog::$numDogs)[15]; }
						Test5(){ legalSmt = (((!123) >= ((234 && (345 > 456)) || 567)) <= (678 != Num::$a)); }
						Test6(){
							arr = Array(x::$listFloat()) >= Array(y.value) % -_nav * -Array();
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestExtras),[MethodDecl(Id(Test1),Instance,[param(Id(x),ClassType(Id(Number)))],Block([AssignStmt(Id(x),UnaryOp(-,IntLit(1)))])),MethodDecl(Id(Test2),Instance,[],Block([AssignStmt(FieldAccess(Id(x1),Id($a)),NewExpr(Id(X),[FieldAccess(NewExpr(Id(Y),[]),Id(z))])),AssignStmt(Id(x2),BinaryOp(-,[IntLit(123),StringLit(abc),StringLit(def),IntLit(456)],ArrayCell(FieldAccess(Id(x3),Id($2803_01)),[CallExpr(Id(x),Id(y),[])])))])),MethodDecl(Id(Test3),Instance,[],Block([AssignStmt(Id(x),StringLit(Lorem ipsum dolor sit amet,\n consectetur adipiscing elit))])),MethodDecl(Id(Test4),Instance,[],Block([AssignStmt(ArrayCell(BinaryOp(>,IntLit(19),BinaryOp(*,CallExpr(Id(_18),Id(_28),[]),ArrayCell(FieldAccess(CallExpr(Id(Cat),Id($getObj),[]),Id(name)),[IntLit(125)]))),[BooleanLit(True)]),ArrayCell(BinaryOp(>,IntLit(23),BinaryOp(&&,IntLit(18),BinaryOp(/,BinaryOp(%,IntLit(15),NewExpr(Id(X),[NewExpr(Id(ABC),[BinaryOp(*,IntLit(86),UnaryOp(!,IntLit(0)))])])),FieldAccess(Id(Dog),Id($numDogs))))),[IntLit(15)]))])),MethodDecl(Id(Test5),Instance,[],Block([AssignStmt(Id(legalSmt),BinaryOp(<=,BinaryOp(>=,UnaryOp(!,IntLit(123)),BinaryOp(||,BinaryOp(&&,IntLit(234),BinaryOp(>,IntLit(345),IntLit(456))),IntLit(567))),BinaryOp(!=,IntLit(678),FieldAccess(Id(Num),Id($a)))))])),MethodDecl(Id(Test6),Instance,[],Block([AssignStmt(Id(arr),BinaryOp(>=,[CallExpr(Id(x),Id($listFloat),[])],BinaryOp(*,BinaryOp(%,[FieldAccess(Id(y),Id(value))],UnaryOp(-,Id(_nav))),UnaryOp(-,[]))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 139))

    def test_140(self):
        # TODO: Test extras:
        input = """
					Class TestExtras {
						Test1(x: Number){ x=-1; }
						Test2(){
							x1::$a = New X(New Y().z);
							x2 = Array(123,"abc","def",456) - x3::$2803_01[x.y()];
						}
						Test3(){ x = "Lorem ipsum dolor sit amet,\\n consectetur adipiscing elit"; }
						Test4(){ (19>(_18._28())*Cat::$getObj().name[125])[True] = (23>18&&(15%New X(New ABC(86*!0)))/Dog::$numDogs)[15]; }
						Test6(){ arr = Array(x::$listFloat()) >= Array(y.value) % -_nav * -Array(); }
						Test7(){
							self = Self + Self;
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestExtras),[MethodDecl(Id(Test1),Instance,[param(Id(x),ClassType(Id(Number)))],Block([AssignStmt(Id(x),UnaryOp(-,IntLit(1)))])),MethodDecl(Id(Test2),Instance,[],Block([AssignStmt(FieldAccess(Id(x1),Id($a)),NewExpr(Id(X),[FieldAccess(NewExpr(Id(Y),[]),Id(z))])),AssignStmt(Id(x2),BinaryOp(-,[IntLit(123),StringLit(abc),StringLit(def),IntLit(456)],ArrayCell(FieldAccess(Id(x3),Id($2803_01)),[CallExpr(Id(x),Id(y),[])])))])),MethodDecl(Id(Test3),Instance,[],Block([AssignStmt(Id(x),StringLit(Lorem ipsum dolor sit amet,\n consectetur adipiscing elit))])),MethodDecl(Id(Test4),Instance,[],Block([AssignStmt(ArrayCell(BinaryOp(>,IntLit(19),BinaryOp(*,CallExpr(Id(_18),Id(_28),[]),ArrayCell(FieldAccess(CallExpr(Id(Cat),Id($getObj),[]),Id(name)),[IntLit(125)]))),[BooleanLit(True)]),ArrayCell(BinaryOp(>,IntLit(23),BinaryOp(&&,IntLit(18),BinaryOp(/,BinaryOp(%,IntLit(15),NewExpr(Id(X),[NewExpr(Id(ABC),[BinaryOp(*,IntLit(86),UnaryOp(!,IntLit(0)))])])),FieldAccess(Id(Dog),Id($numDogs))))),[IntLit(15)]))])),MethodDecl(Id(Test6),Instance,[],Block([AssignStmt(Id(arr),BinaryOp(>=,[CallExpr(Id(x),Id($listFloat),[])],BinaryOp(*,BinaryOp(%,[FieldAccess(Id(y),Id(value))],UnaryOp(-,Id(_nav))),UnaryOp(-,[]))))])),MethodDecl(Id(Test7),Instance,[],Block([AssignStmt(Id(self),BinaryOp(+,Self(),Self()))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 140))

    def test_141(self):
        # TODO: Test block inside block
        input = """
					Class TestExtras {
						Test1(x: Number){ x=-1; }
						Test2(){
							x1::$a = New X(New Y().z);
							x2 = Array(123,"abc","def",456) - x3::$2803_01[x.y()];
						}
						Test3(){ x = "Lorem ipsum dolor sit amet,\\n consectetur adipiscing elit"; }
						Test4(){ (19>(_18._28())*Cat::$getObj().name[125])[True] = (23>18&&(15%New X(New ABC(86*!0)))/Dog::$numDogs)[15]; }
						Test6(){ arr = Array(x::$listFloat()) >= Array(y.value) % -_nav * -Array(); }
						Test7(){ self = Self.a + Self.foo().b; }
						Test8(){ Window.console_log("Print a test case"); }
						Test9(){ Foreach(x In 1 .. 2) { Return x; } }
						Test10(){ If(x) { Out.println("##Value of X:\\t $x"); } }
						Test11() {
							{
								Val a: Int = 28.03E+2001;
							}
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestExtras),[MethodDecl(Id(Test1),Instance,[param(Id(x),ClassType(Id(Number)))],Block([AssignStmt(Id(x),UnaryOp(-,IntLit(1)))])),MethodDecl(Id(Test2),Instance,[],Block([AssignStmt(FieldAccess(Id(x1),Id($a)),NewExpr(Id(X),[FieldAccess(NewExpr(Id(Y),[]),Id(z))])),AssignStmt(Id(x2),BinaryOp(-,[IntLit(123),StringLit(abc),StringLit(def),IntLit(456)],ArrayCell(FieldAccess(Id(x3),Id($2803_01)),[CallExpr(Id(x),Id(y),[])])))])),MethodDecl(Id(Test3),Instance,[],Block([AssignStmt(Id(x),StringLit(Lorem ipsum dolor sit amet,\n consectetur adipiscing elit))])),MethodDecl(Id(Test4),Instance,[],Block([AssignStmt(ArrayCell(BinaryOp(>,IntLit(19),BinaryOp(*,CallExpr(Id(_18),Id(_28),[]),ArrayCell(FieldAccess(CallExpr(Id(Cat),Id($getObj),[]),Id(name)),[IntLit(125)]))),[BooleanLit(True)]),ArrayCell(BinaryOp(>,IntLit(23),BinaryOp(&&,IntLit(18),BinaryOp(/,BinaryOp(%,IntLit(15),NewExpr(Id(X),[NewExpr(Id(ABC),[BinaryOp(*,IntLit(86),UnaryOp(!,IntLit(0)))])])),FieldAccess(Id(Dog),Id($numDogs))))),[IntLit(15)]))])),MethodDecl(Id(Test6),Instance,[],Block([AssignStmt(Id(arr),BinaryOp(>=,[CallExpr(Id(x),Id($listFloat),[])],BinaryOp(*,BinaryOp(%,[FieldAccess(Id(y),Id(value))],UnaryOp(-,Id(_nav))),UnaryOp(-,[]))))])),MethodDecl(Id(Test7),Instance,[],Block([AssignStmt(Id(self),BinaryOp(+,FieldAccess(Self(),Id(a)),FieldAccess(CallExpr(Self(),Id(foo),[]),Id(b))))])),MethodDecl(Id(Test8),Instance,[],Block([Call(Id(Window),Id(console_log),[StringLit(Print a test case)])])),MethodDecl(Id(Test9),Instance,[],Block([For(Id(x),IntLit(1),IntLit(2),IntLit(1),Block([Return(Id(x))])])])),MethodDecl(Id(Test10),Instance,[],Block([If(Id(x),Block([Call(Id(Out),Id(println),[StringLit(##Value of X:\t $x)])]))])),MethodDecl(Id(Test11),Instance,[],Block([Block([ConstDecl(Id(a),IntType,FloatLit(inf))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 141))

    def test_142(self):
        # TODO: Test float expression
        input = """
					Class TestExtras {
						Test1(x: Number){ x=-1; }
						Test2(){
							x1::$a = New X(New Y().z);
							x2 = Array(123,"abc","def",456) - x3::$2803_01[x.y()];
						}
						Test3(){ x = "Lorem ipsum dolor sit amet,\\n consectetur adipiscing elit"; }
						Test4(){ (19>(_18._28())*Cat::$getObj().name[125])[True] = (23>18&&(15%New X(New ABC(86*!0)))/Dog::$numDogs)[15]; }
						Test6(){ arr = Array(x::$listFloat()) >= Array(y.value) % -_nav * -Array(); }
						Test7(){ self = Self.a + Self.foo().b; }
						Test8(){ Window.console_log("Print a test case"); }
						Test9(){ Foreach(x In 1 .. 2) { Return x; } }
						Test10(){ If(x) { Out.println("##Value of X:\\t $x"); } }
						Test11() {}
						Test12() {
							Var a: Float = (0.124e18 * (- 0.e+225) / 15_12E925 && 0.E335)[15.6];
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestExtras),[MethodDecl(Id(Test1),Instance,[param(Id(x),ClassType(Id(Number)))],Block([AssignStmt(Id(x),UnaryOp(-,IntLit(1)))])),MethodDecl(Id(Test2),Instance,[],Block([AssignStmt(FieldAccess(Id(x1),Id($a)),NewExpr(Id(X),[FieldAccess(NewExpr(Id(Y),[]),Id(z))])),AssignStmt(Id(x2),BinaryOp(-,[IntLit(123),StringLit(abc),StringLit(def),IntLit(456)],ArrayCell(FieldAccess(Id(x3),Id($2803_01)),[CallExpr(Id(x),Id(y),[])])))])),MethodDecl(Id(Test3),Instance,[],Block([AssignStmt(Id(x),StringLit(Lorem ipsum dolor sit amet,\n consectetur adipiscing elit))])),MethodDecl(Id(Test4),Instance,[],Block([AssignStmt(ArrayCell(BinaryOp(>,IntLit(19),BinaryOp(*,CallExpr(Id(_18),Id(_28),[]),ArrayCell(FieldAccess(CallExpr(Id(Cat),Id($getObj),[]),Id(name)),[IntLit(125)]))),[BooleanLit(True)]),ArrayCell(BinaryOp(>,IntLit(23),BinaryOp(&&,IntLit(18),BinaryOp(/,BinaryOp(%,IntLit(15),NewExpr(Id(X),[NewExpr(Id(ABC),[BinaryOp(*,IntLit(86),UnaryOp(!,IntLit(0)))])])),FieldAccess(Id(Dog),Id($numDogs))))),[IntLit(15)]))])),MethodDecl(Id(Test6),Instance,[],Block([AssignStmt(Id(arr),BinaryOp(>=,[CallExpr(Id(x),Id($listFloat),[])],BinaryOp(*,BinaryOp(%,[FieldAccess(Id(y),Id(value))],UnaryOp(-,Id(_nav))),UnaryOp(-,[]))))])),MethodDecl(Id(Test7),Instance,[],Block([AssignStmt(Id(self),BinaryOp(+,FieldAccess(Self(),Id(a)),FieldAccess(CallExpr(Self(),Id(foo),[]),Id(b))))])),MethodDecl(Id(Test8),Instance,[],Block([Call(Id(Window),Id(console_log),[StringLit(Print a test case)])])),MethodDecl(Id(Test9),Instance,[],Block([For(Id(x),IntLit(1),IntLit(2),IntLit(1),Block([Return(Id(x))])])])),MethodDecl(Id(Test10),Instance,[],Block([If(Id(x),Block([Call(Id(Out),Id(println),[StringLit(##Value of X:\t $x)])]))])),MethodDecl(Id(Test11),Instance,[],Block([])),MethodDecl(Id(Test12),Instance,[],Block([VarDecl(Id(a),FloatType,ArrayCell(BinaryOp(&&,BinaryOp(/,BinaryOp(*,FloatLit(1.24e+17),UnaryOp(-,FloatLit(0.0))),FloatLit(inf)),FloatLit(0.0)),[FloatLit(15.6)]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 142))

    def test_143(self):
        # TODO: Test float expression
        input = """
					Class TestExtras {
						Test1(x: Number){ x=-1; }
						Test2(){
							x1::$a = New X(New Y().z);
							x2 = Array(123,"abc","def",456) - x3::$2803_01[x.y()];
						}
						Test3(){ x = "Lorem ipsum dolor sit amet,\\n consectetur adipiscing elit"; }
						Test4(){ (19>(_18._28())*Cat::$getObj().name[125])[True] = (23>18&&(15%New X(New ABC(86*!0)))/Dog::$numDogs)[15]; }
						Test6(){ arr = Array(x::$listFloat()) >= Array(y.value) % -_nav * -Array(); }
						Test7(){ self = Self.a + Self.foo().b; }
						Test8(){ Window.console_log("Print a test case"); }
						Test9(){ Foreach(x In 1 .. 2) { Return x; } }
						Test10(){ If(x) { Out.println("##Value of X:\\t $x"); } }
						Test11() {}
						Test12() {
							Var a: Float = (0.124e18 * (- 0.e+225) / 15_12E925 && 0.E335)[15.6];
							Val b: Array[Float, 012357];
						}
					}

					Class TestUtils : TestExtras {
						Val x: Array[Float, 0XA1245];
						ErrorParms (a, b: String; d: Number) {}
						ErrorScalar () {
							If (1/2*3-4) {
									Out.prinln("I'm you but private");
								} Else {
									var[a] = 19/83*New A(bcd)[b];
									a = "This is string contain \\t";
							}
							x::$a = "She said that '"Hello World '"";
							Var def: Int = "123456";
							Val abc: Array[Array[Boolean, 0b1],0x1] = Array();
							If (True) {
								Continue;
								a = b * c + d.foo().f;
							} Elseif (False) {
								Var a, b, d: Int = 1,2,3;
								Break;
								Foreach(Cat.getType().type In "Black" .. "White") {
									Window.console.log("Cat.type");
								}
							}
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestExtras),[MethodDecl(Id(Test1),Instance,[param(Id(x),ClassType(Id(Number)))],Block([AssignStmt(Id(x),UnaryOp(-,IntLit(1)))])),MethodDecl(Id(Test2),Instance,[],Block([AssignStmt(FieldAccess(Id(x1),Id($a)),NewExpr(Id(X),[FieldAccess(NewExpr(Id(Y),[]),Id(z))])),AssignStmt(Id(x2),BinaryOp(-,[IntLit(123),StringLit(abc),StringLit(def),IntLit(456)],ArrayCell(FieldAccess(Id(x3),Id($2803_01)),[CallExpr(Id(x),Id(y),[])])))])),MethodDecl(Id(Test3),Instance,[],Block([AssignStmt(Id(x),StringLit(Lorem ipsum dolor sit amet,\n consectetur adipiscing elit))])),MethodDecl(Id(Test4),Instance,[],Block([AssignStmt(ArrayCell(BinaryOp(>,IntLit(19),BinaryOp(*,CallExpr(Id(_18),Id(_28),[]),ArrayCell(FieldAccess(CallExpr(Id(Cat),Id($getObj),[]),Id(name)),[IntLit(125)]))),[BooleanLit(True)]),ArrayCell(BinaryOp(>,IntLit(23),BinaryOp(&&,IntLit(18),BinaryOp(/,BinaryOp(%,IntLit(15),NewExpr(Id(X),[NewExpr(Id(ABC),[BinaryOp(*,IntLit(86),UnaryOp(!,IntLit(0)))])])),FieldAccess(Id(Dog),Id($numDogs))))),[IntLit(15)]))])),MethodDecl(Id(Test6),Instance,[],Block([AssignStmt(Id(arr),BinaryOp(>=,[CallExpr(Id(x),Id($listFloat),[])],BinaryOp(*,BinaryOp(%,[FieldAccess(Id(y),Id(value))],UnaryOp(-,Id(_nav))),UnaryOp(-,[]))))])),MethodDecl(Id(Test7),Instance,[],Block([AssignStmt(Id(self),BinaryOp(+,FieldAccess(Self(),Id(a)),FieldAccess(CallExpr(Self(),Id(foo),[]),Id(b))))])),MethodDecl(Id(Test8),Instance,[],Block([Call(Id(Window),Id(console_log),[StringLit(Print a test case)])])),MethodDecl(Id(Test9),Instance,[],Block([For(Id(x),IntLit(1),IntLit(2),IntLit(1),Block([Return(Id(x))])])])),MethodDecl(Id(Test10),Instance,[],Block([If(Id(x),Block([Call(Id(Out),Id(println),[StringLit(##Value of X:\t $x)])]))])),MethodDecl(Id(Test11),Instance,[],Block([])),MethodDecl(Id(Test12),Instance,[],Block([VarDecl(Id(a),FloatType,ArrayCell(BinaryOp(&&,BinaryOp(/,BinaryOp(*,FloatLit(1.24e+17),UnaryOp(-,FloatLit(0.0))),FloatLit(inf)),FloatLit(0.0)),[FloatLit(15.6)])),ConstDecl(Id(b),ArrayType(5359,FloatType),None)]))]),ClassDecl(Id(TestUtils),Id(TestExtras),[AttributeDecl(Instance,ConstDecl(Id(x),ArrayType(660037,FloatType),None)),MethodDecl(Id(ErrorParms),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(d),ClassType(Id(Number)))],Block([])),MethodDecl(Id(ErrorScalar),Instance,[],Block([If(BinaryOp(-,BinaryOp(*,BinaryOp(/,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),Block([Call(Id(Out),Id(prinln),[StringLit(I'm you but private)])]),Block([AssignStmt(ArrayCell(Id(var),[Id(a)]),BinaryOp(*,BinaryOp(/,IntLit(19),IntLit(83)),ArrayCell(NewExpr(Id(A),[Id(bcd)]),[Id(b)]))),AssignStmt(Id(a),StringLit(This is string contain \t))])),AssignStmt(FieldAccess(Id(x),Id($a)),StringLit(She said that '"Hello World '")),VarDecl(Id(def),IntType,StringLit(123456)),ConstDecl(Id(abc),ArrayType(1,ArrayType(1,BoolType)),[]),If(BooleanLit(True),Block([Continue,AssignStmt(Id(a),BinaryOp(+,BinaryOp(*,Id(b),Id(c)),FieldAccess(CallExpr(Id(d),Id(foo),[]),Id(f))))]),If(BooleanLit(False),Block([VarDecl(Id(a),IntType,IntLit(1)),VarDecl(Id(b),IntType,IntLit(2)),VarDecl(Id(d),IntType,IntLit(3)),Break,For(FieldAccess(CallExpr(Id(Cat),Id(getType),[]),Id(type)),StringLit(Black),StringLit(White),IntLit(1),Block([Call(FieldAccess(Id(Window),Id(console)),Id(log),[StringLit(Cat.type)])])])])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 143))

    def test_144(self):
        # TODO: Test float expression
        input = """
					Class TestExtras {
						Test1(x: Number){ x=-1; }
						Test2(){
							x1::$a = New X(New Y().z);
							x2 = Array(123,"abc","def",456) - x3::$2803_01[x.y()];
						}
						Test3(){ x = "Lorem ipsum dolor sit amet,\\n consectetur adipiscing elit"; }
						Test4(){ (19>(_18._28())*Cat::$getObj().name[125])[True] = (23>18&&(15%New X(New ABC(86*!0)))/Dog::$numDogs)[15]; }
						Test6(){ arr = Array(x::$listFloat()) >= Array(y.value) % -_nav * -Array(); }
						Test7(){ self = Self.a + Self.foo().b; }
						Test8(){ Window.console_log("Print a test case"); }
						Test9(){ Foreach(x In 1 .. 2) { Return x; } }
						Test10(){ If(x) { Out.println("##Value of X:\\t $x"); } }
						Test11() {}
						Test12() {
							Var a: Float = (0.124e18 * (- 0.e+225) / 15_12E925 && 0.E335)[15.6];
							Val b: Array[Float, 012357];
						}
					}

					Class TestUtils : TestExtras {
						Val x: Array[Float, 0XA1245];
						ErrorParms (a, b: String; d: Number) {}
						ErrorScalar () {
							If (1/2*3-4) {
									Out.prinln("I'm you but private");
								} Else {
									var[a] = 19/83*New A(bcd)[b];
									a = "This is string contain \\t";
							}
							x::$a = "She said that '"Hello World '"";
							Var def: Int = "123456";
							Val abc: Array[Array[Boolean, 0b1],0x1] = Array();
							If (True) {
								Continue;
								a = b * c + d.foo().f;
							} Elseif (False) {
								Var a, b, d: Int = 1,2,3;
								Break;
								Foreach(Cat.getType().type In "Black" .. "White") {
									Window.console.log("Cat.type");
								}
							}
						}
						ErrorDeclr () {
							Var a, _targ_variable_, c: String;
							Foreach(a::$foo().b In abc .. def By "This is abc" +. "def"){
								If (!True) {
									a = (((!123) >= ((234 && (345 + 456)) || 567)) <= (678 != x::$a));
								} Else {
									x.a().f = abc * def / 010;
									a.foo1().foo2().value = b.value.Number() % c.getNum() * "def" +. "ghi";
								}
							}	
						}
						ErrorInAccess () {
							Val x: Int = abc.getList().findIdx(1).value[123];
							Foreach (ele In 1 .. 100) {
								If (ele % 2 != 0) {
									Foreach(eleIf In 100 .. 200 By 50) {
										If (True) {
											ele = ele[1245] * 148 % 100 - (1+1).foo();
											Break;
										} Elseif (False) {
											Master::$GenerateRandom(125.E55, "12345", Array("##String def", Array(125, Array(New X(y)))));
											Continue;
										}
									}
								} Else {
									Foreach(elseIf In 200 .. 300 By 25) {
										Self.func().magnitude = !89_125E120+56 + A[0.E-168];
										Return abc * def::$_123();
									}
								}
							}
						}
					}
			"""
        expect = r"""Program([ClassDecl(Id(TestExtras),[MethodDecl(Id(Test1),Instance,[param(Id(x),ClassType(Id(Number)))],Block([AssignStmt(Id(x),UnaryOp(-,IntLit(1)))])),MethodDecl(Id(Test2),Instance,[],Block([AssignStmt(FieldAccess(Id(x1),Id($a)),NewExpr(Id(X),[FieldAccess(NewExpr(Id(Y),[]),Id(z))])),AssignStmt(Id(x2),BinaryOp(-,[IntLit(123),StringLit(abc),StringLit(def),IntLit(456)],ArrayCell(FieldAccess(Id(x3),Id($2803_01)),[CallExpr(Id(x),Id(y),[])])))])),MethodDecl(Id(Test3),Instance,[],Block([AssignStmt(Id(x),StringLit(Lorem ipsum dolor sit amet,\n consectetur adipiscing elit))])),MethodDecl(Id(Test4),Instance,[],Block([AssignStmt(ArrayCell(BinaryOp(>,IntLit(19),BinaryOp(*,CallExpr(Id(_18),Id(_28),[]),ArrayCell(FieldAccess(CallExpr(Id(Cat),Id($getObj),[]),Id(name)),[IntLit(125)]))),[BooleanLit(True)]),ArrayCell(BinaryOp(>,IntLit(23),BinaryOp(&&,IntLit(18),BinaryOp(/,BinaryOp(%,IntLit(15),NewExpr(Id(X),[NewExpr(Id(ABC),[BinaryOp(*,IntLit(86),UnaryOp(!,IntLit(0)))])])),FieldAccess(Id(Dog),Id($numDogs))))),[IntLit(15)]))])),MethodDecl(Id(Test6),Instance,[],Block([AssignStmt(Id(arr),BinaryOp(>=,[CallExpr(Id(x),Id($listFloat),[])],BinaryOp(*,BinaryOp(%,[FieldAccess(Id(y),Id(value))],UnaryOp(-,Id(_nav))),UnaryOp(-,[]))))])),MethodDecl(Id(Test7),Instance,[],Block([AssignStmt(Id(self),BinaryOp(+,FieldAccess(Self(),Id(a)),FieldAccess(CallExpr(Self(),Id(foo),[]),Id(b))))])),MethodDecl(Id(Test8),Instance,[],Block([Call(Id(Window),Id(console_log),[StringLit(Print a test case)])])),MethodDecl(Id(Test9),Instance,[],Block([For(Id(x),IntLit(1),IntLit(2),IntLit(1),Block([Return(Id(x))])])])),MethodDecl(Id(Test10),Instance,[],Block([If(Id(x),Block([Call(Id(Out),Id(println),[StringLit(##Value of X:\t $x)])]))])),MethodDecl(Id(Test11),Instance,[],Block([])),MethodDecl(Id(Test12),Instance,[],Block([VarDecl(Id(a),FloatType,ArrayCell(BinaryOp(&&,BinaryOp(/,BinaryOp(*,FloatLit(1.24e+17),UnaryOp(-,FloatLit(0.0))),FloatLit(inf)),FloatLit(0.0)),[FloatLit(15.6)])),ConstDecl(Id(b),ArrayType(5359,FloatType),None)]))]),ClassDecl(Id(TestUtils),Id(TestExtras),[AttributeDecl(Instance,ConstDecl(Id(x),ArrayType(660037,FloatType),None)),MethodDecl(Id(ErrorParms),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(d),ClassType(Id(Number)))],Block([])),MethodDecl(Id(ErrorScalar),Instance,[],Block([If(BinaryOp(-,BinaryOp(*,BinaryOp(/,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),Block([Call(Id(Out),Id(prinln),[StringLit(I'm you but private)])]),Block([AssignStmt(ArrayCell(Id(var),[Id(a)]),BinaryOp(*,BinaryOp(/,IntLit(19),IntLit(83)),ArrayCell(NewExpr(Id(A),[Id(bcd)]),[Id(b)]))),AssignStmt(Id(a),StringLit(This is string contain \t))])),AssignStmt(FieldAccess(Id(x),Id($a)),StringLit(She said that '"Hello World '")),VarDecl(Id(def),IntType,StringLit(123456)),ConstDecl(Id(abc),ArrayType(1,ArrayType(1,BoolType)),[]),If(BooleanLit(True),Block([Continue,AssignStmt(Id(a),BinaryOp(+,BinaryOp(*,Id(b),Id(c)),FieldAccess(CallExpr(Id(d),Id(foo),[]),Id(f))))]),If(BooleanLit(False),Block([VarDecl(Id(a),IntType,IntLit(1)),VarDecl(Id(b),IntType,IntLit(2)),VarDecl(Id(d),IntType,IntLit(3)),Break,For(FieldAccess(CallExpr(Id(Cat),Id(getType),[]),Id(type)),StringLit(Black),StringLit(White),IntLit(1),Block([Call(FieldAccess(Id(Window),Id(console)),Id(log),[StringLit(Cat.type)])])])])))])),MethodDecl(Id(ErrorDeclr),Instance,[],Block([VarDecl(Id(a),StringType),VarDecl(Id(_targ_variable_),StringType),VarDecl(Id(c),StringType),For(FieldAccess(CallExpr(Id(a),Id($foo),[]),Id(b)),Id(abc),Id(def),BinaryOp(+.,StringLit(This is abc),StringLit(def)),Block([If(UnaryOp(!,BooleanLit(True)),Block([AssignStmt(Id(a),BinaryOp(<=,BinaryOp(>=,UnaryOp(!,IntLit(123)),BinaryOp(||,BinaryOp(&&,IntLit(234),BinaryOp(+,IntLit(345),IntLit(456))),IntLit(567))),BinaryOp(!=,IntLit(678),FieldAccess(Id(x),Id($a)))))]),Block([AssignStmt(FieldAccess(CallExpr(Id(x),Id(a),[]),Id(f)),BinaryOp(/,BinaryOp(*,Id(abc),Id(def)),IntLit(8))),AssignStmt(FieldAccess(CallExpr(CallExpr(Id(a),Id(foo1),[]),Id(foo2),[]),Id(value)),BinaryOp(+.,BinaryOp(*,BinaryOp(%,CallExpr(FieldAccess(Id(b),Id(value)),Id(Number),[]),CallExpr(Id(c),Id(getNum),[])),StringLit(def)),StringLit(ghi)))]))])])])),MethodDecl(Id(ErrorInAccess),Instance,[],Block([ConstDecl(Id(x),IntType,ArrayCell(FieldAccess(CallExpr(CallExpr(Id(abc),Id(getList),[]),Id(findIdx),[IntLit(1)]),Id(value)),[IntLit(123)])),For(Id(ele),IntLit(1),IntLit(100),IntLit(1),Block([If(BinaryOp(!=,BinaryOp(%,Id(ele),IntLit(2)),IntLit(0)),Block([For(Id(eleIf),IntLit(100),IntLit(200),IntLit(50),Block([If(BooleanLit(True),Block([AssignStmt(Id(ele),BinaryOp(-,BinaryOp(%,BinaryOp(*,ArrayCell(Id(ele),[IntLit(1245)]),IntLit(148)),IntLit(100)),CallExpr(BinaryOp(+,IntLit(1),IntLit(1)),Id(foo),[]))),Break]),If(BooleanLit(False),Block([Call(Id(Master),Id($GenerateRandom),[FloatLit(1.25e+57),StringLit(12345),[StringLit(##String def),[IntLit(125),[NewExpr(Id(X),[Id(y)])]]]]),Continue])))])])]),Block([For(Id(elseIf),IntLit(200),IntLit(300),IntLit(25),Block([AssignStmt(FieldAccess(CallExpr(Self(),Id(func),[]),Id(magnitude)),BinaryOp(+,BinaryOp(+,UnaryOp(!,FloatLit(8.9125e+124)),IntLit(56)),ArrayCell(Id(A),[FloatLit(0.0)]))),Return(BinaryOp(*,Id(abc),CallExpr(Id(def),Id($_123),[])))])])]))])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 144))

    def test_145(self):
        # TODO: Test Null literals:
        input = """
				Class Program {
					main() {
						x = Null + "abc";
					}
				}
		"""
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(x),BinaryOp(+,NullLiteral(),StringLit(abc)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 145))

    def test_146(self):
        # TODO: Test uninitialized variable of Class Type
        input = """
				Class Program {
					Var $y: QWER;
					main() {
						Val x: WASD;
					}
				}
		"""
        expect = r"""Program([ClassDecl(Id(Program),[AttributeDecl(Static,VarDecl(Id($y),ClassType(Id(QWER)),NullLiteral())),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(x),ClassType(Id(WASD)),NullLiteral())]))])])"""
        self.assertTrue(TestAST.test(input, expect, 146))

    def test_147(self):
        # TODO: Test Self literals:
        input = """
				Class Program {
					main() {
						x = Self + "abc";
					}
				}
		"""
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(x),BinaryOp(+,Self(),StringLit(abc)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 147))

    def test_148(self):
        # TODO: Test main methods:
        input = """
				Class Program {
					main() {
						x = "abc" + "def";
					}
					main() {
						y = "ghi" + "jkl";
					}
				}
		"""
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(x),BinaryOp(+,StringLit(abc),StringLit(def)))])),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(y),BinaryOp(+,StringLit(ghi),StringLit(jkl)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 148))

    def test_149(self):
        # TODO: Test array of array:
        input = """
				Class Program {
					main () {
						a[1][2][3][4][5] = b[6][7][8][9][0];
					}
				}
		"""
        expect = r"""Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]),ArrayCell(Id(b),[IntLit(6),IntLit(7),IntLit(8),IntLit(9),IntLit(0)]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 149))
