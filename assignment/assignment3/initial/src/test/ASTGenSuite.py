import unittest
from TestUtils import TestAST
from AST import *


# from initial.src.main.d96.utils.AST import *

class ASTGenSuite(unittest.TestCase):
    def testEmptyClass(self):
        i = """Class Adam{}"""
        e = str(Program(
            [ClassDecl(
                Id("Adam"),
                []
            )]
        ))
        self.assertTrue(TestAST.test(i, e, 1))

    def testClassWithSuperClass(self):
        i = "Class Eva : Human{}"
        e = str(Program(
            [ClassDecl(
                Id("Eva"),
                [],
                Id("Human")
            )]
        ))
        self.assertTrue(TestAST.test(i, e, 2))

    def testMainMethodInClass(self):
        i = """
            Class Adam : Human{
                main(){}
            }
            Class Program: SuperClass{
                main(){}
            }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Program"),
                    [MethodDecl(
                        Static(),
                        Id("main"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 3))

    def testSimpleMultiClass(self):
        i = """
                Class Adam: Human{}
                Class Eva{}
                Class Nova: Human{}
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Adam"),
                        [],
                        Id("Human")
                    ),
                    ClassDecl(
                        Id("Eva"),
                        [],
                    ),
                    ClassDecl(
                        Id("Nova"),
                        [],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 4))

    def testClassWithStaticMethod(self):
        i = """
            Class _Adam : Human{
                $eatApple(){}
            }
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Adam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [],
                                Block([])
                            )
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 5))

    def testClassWithStaticMethodAndConstructorDestructor(self):
        i = """
            Class _Adam : Human{
                $eatApple(){}
                Constructor(){}
                Destructor(){}
            }
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Adam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 6))

    def testOneParameterInMethod(self):
        i = """
            Class _Adam : Human{
                $eatApple(var1, var2: Int){}
                Constructor(){}
                Destructor(){}
            }
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Adam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("var1"), IntType()),
                                    VarDecl(Id("var2"), IntType())
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 7))

    def testMultiParameterInMethod(self):
        i = """
                Class _Adam : Human{
                    $eatApple(var1: Int; var3, var4: Float){}
                    Constructor(){}
                    Destructor(){}
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Adam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("var1"), IntType()),
                                    VarDecl(Id("var3"), FloatType()),
                                    VarDecl(Id("var4"), FloatType()),
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 8))

    def testMultiParameterInMethod2(self):
        i = """
                Class _Adam : Human{
                    $eatApple(var1: Int; var3, var4: Float){}
                    Constructor(
                        s1, s2, s3: String;
                        b1: Boolean
                    ){}
                    Destructor(){}
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Adam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("var1"), IntType()),
                                    VarDecl(Id("var3"), FloatType()),
                                    VarDecl(Id("var4"), FloatType()),
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [
                                    VarDecl(Id("s1"), StringType()),
                                    VarDecl(Id("s2"), StringType()),
                                    VarDecl(Id("s3"), StringType()),
                                    VarDecl(Id("b1"), BoolType())
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 9))

    def testMultiParameterInMethod3(self):
        i = """
                Class _Adam : Human{
                    $eatApple(
                        var1: Int;
                        var3, var4: Float;
                        o1, o2: SangHandsome
                    ){}
                    Constructor(
                        s1, s2, s3: String;
                        b1: Boolean
                    ){}
                    Destructor(){}
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Adam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("var1"), IntType()),
                                    VarDecl(Id("var3"), FloatType()),
                                    VarDecl(Id("var4"), FloatType()),
                                    VarDecl(Id("o1"), ClassType(Id("SangHandsome"))),
                                    VarDecl(Id("o2"), ClassType(Id("SangHandsome")))
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [
                                    VarDecl(Id("s1"), StringType()),
                                    VarDecl(Id("s2"), StringType()),
                                    VarDecl(Id("s3"), StringType()),
                                    VarDecl(Id("b1"), BoolType())
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 10))

    def testMultiParameterInMethodWithArrayType(self):
        i = """
                Class _Adam : Human{
                    $eatApple(
                        var1: Int;
                        var3, var4: Float;
                        o1, o2: SangHandsome
                    ){}
                    eatEva(
                        var5: Array[Int, 4];
                        var6: Array[String, 1_000]
                    ){}
                    Constructor(
                        s1, s2, s3: String;
                        b1: Boolean
                    ){}
                    Destructor(){}
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Adam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("var1"), IntType()),
                                    VarDecl(Id("var3"), FloatType()),
                                    VarDecl(Id("var4"), FloatType()),
                                    VarDecl(Id("o1"), ClassType(Id("SangHandsome"))),
                                    VarDecl(Id("o2"), ClassType(Id("SangHandsome")))
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("eatEva"),
                                [
                                    VarDecl(Id("var5"), ArrayType(4, IntType())),
                                    VarDecl(Id("var6"), ArrayType(1000, StringType())),
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [
                                    VarDecl(Id("s1"), StringType()),
                                    VarDecl(Id("s2"), StringType()),
                                    VarDecl(Id("s3"), StringType()),
                                    VarDecl(Id("b1"), BoolType())
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 11))

    def testParameterInMethodWithNestedArrayType(self):
        i = """
                Class _Adam : Human{
                    $eatApple(
                        var1: Int;
                        var3, var4: Float;
                        o1, o2: SangHandsome
                    ){}
                    eatEva(
                        var6: Array[Array[Int, 1_2_3_4], 1_000]
                    ){}
                    Constructor(
                        s1, s2, s3: String;
                        b1: Boolean
                    ){}
                    Destructor(){}
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Adam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("var1"), IntType()),
                                    VarDecl(Id("var3"), FloatType()),
                                    VarDecl(Id("var4"), FloatType()),
                                    VarDecl(Id("o1"), ClassType(Id("SangHandsome"))),
                                    VarDecl(Id("o2"), ClassType(Id("SangHandsome")))
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("eatEva"),
                                [
                                    VarDecl(
                                        Id("var6"),
                                        ArrayType(1000, ArrayType(1234, IntType()))
                                    ),
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [
                                    VarDecl(Id("s1"), StringType()),
                                    VarDecl(Id("s2"), StringType()),
                                    VarDecl(Id("s3"), StringType()),
                                    VarDecl(Id("b1"), BoolType())
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 12))

    def testParameterInMethodWithSuperNestedArrayType(self):
        i = """
                Class _Adam : Human{
                    $eatApple(
                        var1: Int;
                        var3, var4: Float;
                        o1, o2: SangHandsome
                    ){}
                    eatEva(
                        var6: Array[Array[Array[Array[String, 4], 2_000], 1_2_3_4], 1_000]
                    ){}
                    Constructor(
                        s1, s2, s3: String;
                        b1: Boolean
                    ){}
                    Destructor(){}
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Adam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("var1"), IntType()),
                                    VarDecl(Id("var3"), FloatType()),
                                    VarDecl(Id("var4"), FloatType()),
                                    VarDecl(Id("o1"), ClassType(Id("SangHandsome"))),
                                    VarDecl(Id("o2"), ClassType(Id("SangHandsome")))
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("eatEva"),
                                [
                                    VarDecl(
                                        Id("var6"),
                                        ArrayType(
                                            1000,
                                            ArrayType(
                                                1234,
                                                ArrayType(
                                                    2000,
                                                    ArrayType(
                                                        4,
                                                        StringType()
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [
                                    VarDecl(Id("s1"), StringType()),
                                    VarDecl(Id("s2"), StringType()),
                                    VarDecl(Id("s3"), StringType()),
                                    VarDecl(Id("b1"), BoolType())
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 13))

    def testAttributeWithoutInitialValue(self):
        i = """
            Class Eva{
                Var a,b: Boolean;
            }
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Eva"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("a"), BoolType())
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("b"), BoolType())
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 14))

    def testAttributeWithoutInitialValue2(self):
        i = """
            Class Eva{
                Val a: Array[Int, 3] = Array(2, 3, 4);
                Var c, $d: Array[Array[String, 4], 1_000];
            }
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Eva"),
                        [
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("a"),
                                    ArrayType(
                                        3,
                                        IntType()
                                    ),
                                    ArrayLiteral(
                                        [
                                            IntLiteral(2),
                                            IntLiteral(3),
                                            IntLiteral(4)
                                        ]
                                    )
                                )
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("c"), ArrayType(1000, ArrayType(4, StringType())), None)
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(Id("$d"), ArrayType(1000, ArrayType(4, StringType())), None)
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 15))

    def testAttrConstDecl(self):
        i = """
                Class Program {
                    Var a: Int;
                    Val a, b:Int = 2, 6;
                }
                """
        e = str(
            Program([
                ClassDecl(
                    Id("Program"),
                    [
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id('a'),
                                IntType()
                            )
                        ),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(
                                Id('a'),
                                IntType(),
                                IntLiteral(2)
                            )
                        ),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(
                                Id('b'),
                                IntType(),
                                IntLiteral(6)
                            )
                        )
                    ]
                )
            ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 16))

    def testAttributeWithInitialValue(self):
        i = """
            Class Eva{
                Var a, b: Boolean = True, False;
            }
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Eva"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("a"), BoolType(), BooleanLiteral(True))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("b"), BoolType(), BooleanLiteral(False))
                            ),

                        ],
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(i, e, 17))

    def testAttributeWithInitialInt(self):
        i = """
                Class Eva{
                        Var s,a : Int = 0X2_4, 0x24; ## Hexa -> 36 ##
                        Val n,$g : Int = 02_4, 02004;  ## Octal -> 20, 1028 ##
                        Var $d,z : Int = 0b11_0_11, 0B11_011; ## Binary -> 27##
                        Val v,l : Int = 0, 24;       ## Decimal ##
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Eva"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("s"), IntType(), IntLiteral(36))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("a"), IntType(), IntLiteral(36))
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(Id("n"), IntType(), IntLiteral(20))
                            ),
                            AttributeDecl(
                                Static(),
                                ConstDecl(Id("$g"), IntType(), IntLiteral(1028))
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(Id("$d"), IntType(), IntLiteral(27))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("z"), IntType(), IntLiteral(27))
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(Id("v"), IntType(), IntLiteral(0))
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(Id("l"), IntType(), IntLiteral(24))
                            )
                        ],
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(i, e, 18))

    def testAttributeWithInitialFloat(self):
        i = """
                Class Eva{
                        Var I, WANT, TEN, MARK : Float =  1.234, 1.2e3, 7E-5, 1_234.567;
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Eva"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("I"), FloatType(), FloatLiteral(1.234))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("WANT"), FloatType(), FloatLiteral(1200.0))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("TEN"), FloatType(), FloatLiteral(7e-05))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("MARK"), FloatType(), FloatLiteral(1234.567))
                            )
                        ],
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(i, e, 19))

    def testClassType(self):
        i = """
                Class Eva{
                    Val haizz: Node = New Node();
                    Var $haizz: Node = New Node("Em dep lam");
                    Var newNode: Node;
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Eva"),
                        [
                            AttributeDecl(
                                Instance(),
                                ConstDecl(Id("haizz"), ClassType(Id("Node")), NewExpr(Id("Node"), []))
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(Id("$haizz"), ClassType(Id("Node")),
                                        NewExpr(Id("Node"), [StringLiteral("Em dep lam")]))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("newNode"), ClassType(Id("Node")), NullLiteral())
                            )
                        ],
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(i, e, 20))

    def testVariableDeclarationWithObjectCreation(self):
        i = """
               Class Adam : Human{
                   main(){
                        Var a, b : A = New A(), New A();
                   }
               }
               Class Program: SuperClass{
                   main(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            VarDecl(Id("a"), ClassType(Id("A")), NewExpr(Id("A"), [])),
                            VarDecl(Id("b"), ClassType(Id("A")), NewExpr(Id("A"), []))
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Program"),
                    [MethodDecl(
                        Static(),
                        Id("main"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 21))

    def testVariableDeclarationWithPrimitiveTypeAndSelf(self):
        i = """
               Class Adam : Human{
                   main(){
                        Val a, b : Int = Self.br, Self.uh;
                   }
               }
               Class Program: SuperClass{
                   main(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            ConstDecl(Id("a"), IntType(), FieldAccess(SelfLiteral(), Id("br"))),
                            ConstDecl(Id("b"), IntType(), FieldAccess(SelfLiteral(), Id("uh")))
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Program"),
                    [MethodDecl(
                        Static(),
                        Id("main"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 22))

    def testVariableDeclarationWithPrimitiveTypeAndSelf2(self):
        i = """
               Class Adam : Human{
                   main(){
                        Val a, b : Int = Self.a.b.c.d, Self.e.f.h.i;
                   }
               }
               Class Program: SuperClass{
                   main(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            ConstDecl(
                                Id("a"), IntType(),
                                FieldAccess(
                                    FieldAccess(
                                        FieldAccess(
                                            FieldAccess(
                                                SelfLiteral(),
                                                Id("a")
                                            ),
                                            Id("b")
                                        ),
                                        Id("c")
                                    ),
                                    Id("d")
                                )
                            ),
                            ConstDecl(
                                Id("b"), IntType(),
                                FieldAccess(
                                    FieldAccess(
                                        FieldAccess(
                                            FieldAccess(
                                                SelfLiteral(),
                                                Id("e")
                                            ),
                                            Id("f")
                                        ),
                                        Id("h")
                                    ),
                                    Id("i")
                                )
                            )
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Program"),
                    [MethodDecl(
                        Static(),
                        Id("main"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 23))

    def testMethodInvocationStatic1(self):
        i = """
               Class Adam : Human{
                   main(){
                        Eva::$hura();
                   }
               }
               Class Eva: SuperClass{
                   $hura(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            CallStmt(
                                obj=Id("Eva"),
                                method=Id("$hura"),
                                param=[]
                            )
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Eva"),
                    [MethodDecl(
                        Static(),
                        Id("$hura"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 24))

    def testMethodInvocationStatic2(self):
        i = """
               Class Adam : Human{
                   main(){
                        Eva::$bara();
                   }
               }
               Class Eva: SuperClass{
                   $hura(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            CallStmt(
                                obj=Id("Eva"),
                                method=Id("$bara"),
                                param=[]
                            )
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Eva"),
                    [MethodDecl(
                        Static(),
                        Id("$hura"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 25))

    def testFieldAccessInstance(self):
        i = """
               Class Adam : Human{
                   main(){
                        Var a : String = Eva::$a.b.c;
                   }
               }
               Class Eva: SuperClass{
                   $hura(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            VarDecl(
                                variable=Id("a"),
                                varType=StringType(),
                                varInit=FieldAccess(
                                    obj=FieldAccess(
                                        obj=FieldAccess(
                                            obj=Id("Eva"),
                                            fieldname=Id("$a")
                                        ),
                                        fieldname=Id("b")
                                    ),
                                    fieldname=Id("c")
                                )
                            )
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Eva"),
                    [MethodDecl(
                        Static(),
                        Id("$hura"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 26))

    def testFieldAccessStatic(self):
        i = """
               Class Adam : Human{
                   main(){
                        Var a : String = Eva::$a.b.c(0x24);
                   }
               }
               Class Eva: SuperClass{
                   $hura(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            VarDecl(
                                variable=Id("a"),
                                varType=StringType(),
                                varInit=CallExpr(
                                    obj=FieldAccess(
                                        obj=FieldAccess(
                                            obj=Id("Eva"),
                                            fieldname=Id("$a")
                                        ),
                                        fieldname=Id("b")
                                    ),
                                    method=Id("c"),
                                    param=[IntLiteral(36)]
                                )
                            )
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Eva"),
                    [MethodDecl(
                        Static(),
                        Id("$hura"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 27))

    def testMethodInvocationInstance(self):
        i = """
               Class Adam : Human{
                   main(){
                        Var a : String = Eva.a.b.c();
                   }
               }
               Class Eva: SuperClass{
                   $hura(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            VarDecl(
                                variable=Id("a"),
                                varType=StringType(),
                                varInit=CallExpr(
                                    obj=FieldAccess(
                                        obj=FieldAccess(
                                            obj=Id("Eva"),
                                            fieldname=Id("a")
                                        ),
                                        fieldname=Id("b")
                                    ),
                                    method=Id("c"),
                                    param=[]
                                )
                            )
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Eva"),
                    [MethodDecl(
                        Static(),
                        Id("$hura"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 28))

    def testAssignStatementNotExpr(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        a = !True;
                   }
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                Assign(
                                    lhs=Id("a"),
                                    exp=UnaryOp(
                                        op="!",
                                        body=BooleanLiteral(True)
                                    )
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 29))

    def testAssignStatementSignExpr(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        a = -10_000;
                   }
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                Assign(
                                    lhs=Id("a"),
                                    exp=UnaryOp(

                                        op="-",
                                        body=IntLiteral(10000)

                                    )
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 30))

    def testAssignStatementNotExpr2(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        a = !(-0X24); ## 0X24 = 36 ##
                   }
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                Assign(
                                    lhs=Id("a"),
                                    exp=UnaryOp(
                                        op="!",
                                        body=UnaryOp(

                                            op="-",
                                            body=IntLiteral(36)

                                        )
                                    )
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 31))

    def testAssignStatementMulAddMolExpr(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        a = 20.5 * 10 / 2 % 5;
                   }
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                Assign(
                                    lhs=Id("a"),
                                    exp=BinaryOp(
                                        op="%",
                                        left=BinaryOp(
                                            op="/",
                                            left=BinaryOp(
                                                op="*",
                                                left=FloatLiteral(20.5),
                                                right=IntLiteral(10)
                                            ),
                                            right=IntLiteral(2)
                                        ),
                                        right=IntLiteral(5)
                                    )
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 32))

    def testAssignStatementAddSubExpr(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        a = (20.5 + 2) * (10 / (2 % 5)) + 10;
                   }
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                Assign(
                                    lhs=Id("a"),
                                    exp=BinaryOp(
                                        op="+",
                                        left=BinaryOp(
                                            op="*",
                                            left=BinaryOp(
                                                op="+",
                                                left=FloatLiteral(20.5),
                                                right=IntLiteral(2)
                                            ),
                                            right=BinaryOp(
                                                op="/",
                                                left=IntLiteral(10),
                                                right=BinaryOp(
                                                    op="%",
                                                    left=IntLiteral(2),
                                                    right=IntLiteral(5)
                                                )
                                            )
                                        ),
                                        right=IntLiteral(10)
                                    )
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 33))

    def testAssignStatementAndOrExpr(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        a = !(Eva.a || Eva.b) && Adam::$a;
                   }
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                Assign(
                                    lhs=Id("a"),
                                    exp=BinaryOp(
                                        op="&&",
                                        left=UnaryOp(
                                            op="!",
                                            body=BinaryOp(
                                                op="||",
                                                left=FieldAccess(
                                                    obj=Id("Eva"),
                                                    fieldname=Id("a")
                                                ),
                                                right=FieldAccess(
                                                    obj=Id("Eva"),
                                                    fieldname=Id("b")
                                                )
                                            )
                                        ),
                                        right=FieldAccess(
                                            Id("Adam"),
                                            fieldname=Id("$a")
                                        )
                                    )
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 34))

    def testIfStatementRelationalExpr(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([])
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 35))

    def testIfStatementRelationalExpr2(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){
                            a = !(Eva.a || Eva.b) && Adam::$a;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block(
                                        [
                                            Assign(
                                                lhs=Id("a"),
                                                exp=BinaryOp(
                                                    op="&&",
                                                    left=UnaryOp(
                                                        op="!",
                                                        body=BinaryOp(
                                                            op="||",
                                                            left=FieldAccess(
                                                                obj=Id("Eva"),
                                                                fieldname=Id("a")
                                                            ),
                                                            right=FieldAccess(
                                                                obj=Id("Eva"),
                                                                fieldname=Id("b")
                                                            )
                                                        )
                                                    ),
                                                    right=FieldAccess(
                                                        Id("Adam"),
                                                        fieldname=Id("$a")
                                                    )
                                                )
                                            )
                                        ]
                                    )

                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 36))

    def testIfStatementRelationalExpr3(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Else{
                            a = 20;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=IntLiteral(20)
                                        )
                                    ]),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 37))

    def testIfStatementRelationalExpr4(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Elseif(b){}
                        Else{
                            a = 20;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=If(
                                        expr=Id("b"),
                                        thenStmt=Block([]),
                                        elseStmt=Block([
                                            Assign(
                                                lhs=Id("a"),
                                                exp=IntLiteral(20)
                                            )
                                        ])
                                    ),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 38))

    def testIfStatementRelationalExpr5(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){
                            Var a: Int;
                            If(k == 10){}
                            Else{
                                k = k * 2;
                            }
                        }
                        Elseif(b){}
                        Else{
                            a = 20;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([
                                        VarDecl(
                                            variable=Id("a"),
                                            varType=IntType(),
                                        ),
                                        If(
                                            expr=BinaryOp(
                                                op="==",
                                                left=Id("k"),
                                                right=IntLiteral(10)
                                            ),
                                            thenStmt=Block([]),
                                            elseStmt=Block([
                                                Assign(
                                                    lhs=Id("k"),
                                                    exp=BinaryOp(
                                                        op="*",
                                                        left=Id("k"),
                                                        right=IntLiteral(2)
                                                    )
                                                )
                                            ])
                                        )
                                    ]),
                                    elseStmt=If(
                                        expr=Id("b"),
                                        thenStmt=Block([]),
                                        elseStmt=Block([
                                            Assign(
                                                lhs=Id("a"),
                                                exp=IntLiteral(20)
                                            )
                                        ])
                                    ),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 39))

    def testIfStmtWithManyElseif(self):
        i = """
               Class Program : Human{
                   main(){}
                   assign(){
                        If(a == 10){}
                        Elseif(b){}
                        Elseif(c){}
                        Elseif(d){}
                        Else{
                            a = 20;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Instance(),
                            Id("assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=If(
                                        expr=Id("b"),
                                        thenStmt=Block([]),
                                        elseStmt=If(
                                            expr=Id("c"),
                                            thenStmt=Block([]),
                                            elseStmt=If(
                                                expr=Id("d"),
                                                thenStmt=Block([]),
                                                elseStmt=Block([
                                                    Assign(
                                                        lhs=Id("a"),
                                                        exp=IntLiteral(20)
                                                    )
                                                ])
                                            )
                                        )
                                    ),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 40))

    def testForStmt(self):
        i = """
               Class Program : Human{
                   main(){
                        Foreach(i In 1 .. 100_100 By 1 + 2){
                            S.print("Hello");
                        }
                   }
                   assign(){
                        If(a == 10){}
                        Elseif(b){}
                        Elseif(c){}
                        Elseif(d){}
                        Else{
                            a = 20;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([
                                For(
                                    id=Id("i"),
                                    expr1=IntLiteral(1),
                                    expr2=IntLiteral(100100),
                                    loop=Block([
                                        CallStmt(
                                            obj=Id("S"),
                                            method=Id("print"),
                                            param=[
                                                StringLiteral("Hello")
                                            ]
                                        )
                                    ]),
                                    expr3=BinaryOp(
                                        op="+",
                                        left=IntLiteral(1),
                                        right=IntLiteral(2)
                                    )
                                )
                            ])
                        ),
                        MethodDecl(
                            Instance(),
                            Id("assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=If(
                                        expr=Id("b"),
                                        thenStmt=Block([]),
                                        elseStmt=If(
                                            expr=Id("c"),
                                            thenStmt=Block([]),
                                            elseStmt=If(
                                                expr=Id("d"),
                                                thenStmt=Block([]),
                                                elseStmt=Block([
                                                    Assign(
                                                        lhs=Id("a"),
                                                        exp=IntLiteral(20)
                                                    )
                                                ])
                                            )
                                        )
                                    ),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 41))

    def testForStmtAndBreakContinue(self):
        i = """
               Class Program : Human{
                   main(){
                        Foreach(i In 1 .. 100_100 By 1 + 2){
                            S.print("Hello");
                            If(a + b == "Sangs"){
                                Break;
                            }
                            Else{
                                Continue;
                            }
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([
                                For(
                                    id=Id("i"),
                                    expr1=IntLiteral(1),
                                    expr2=IntLiteral(100100),
                                    loop=Block([
                                        CallStmt(
                                            obj=Id("S"),
                                            method=Id("print"),
                                            param=[
                                                StringLiteral("Hello")
                                            ]
                                        ),
                                        If(
                                            expr=BinaryOp(
                                                op="==",
                                                left=BinaryOp(
                                                    op="+",
                                                    left=Id("a"),
                                                    right=Id("b")
                                                ),
                                                right=StringLiteral("Sangs")
                                            ),
                                            thenStmt=Block([
                                                Break()
                                            ]),
                                            elseStmt=Block([
                                                Continue()
                                            ])
                                        )
                                    ]),
                                    expr3=BinaryOp(
                                        op="+",
                                        left=IntLiteral(1),
                                        right=IntLiteral(2)
                                    )
                                )
                            ])
                        ),
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 42))

    def testNestedBlockStmt(self):
        i = """
               Class Program : Human{
                   main(){
                        Foreach(i In 1 .. 100_100 By 1 + 2){
                            S.print("Hello");
                            If(a + b == "Sangs"){
                                {
                                    Val b: Float = 10.e10;
                                    Break;
                                }
                            }
                            Else{
                                Continue;
                            }
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([
                                For(
                                    id=Id("i"),
                                    expr1=IntLiteral(1),
                                    expr2=IntLiteral(100100),
                                    loop=Block([
                                        CallStmt(
                                            obj=Id("S"),
                                            method=Id("print"),
                                            param=[
                                                StringLiteral("Hello")
                                            ]
                                        ),
                                        If(
                                            expr=BinaryOp(
                                                op="==",
                                                left=BinaryOp(
                                                    op="+",
                                                    left=Id("a"),
                                                    right=Id("b")
                                                ),
                                                right=StringLiteral("Sangs")
                                            ),
                                            thenStmt=Block([
                                                Block([
                                                    ConstDecl(
                                                        constant=Id("b"),
                                                        constType=FloatType(),
                                                        value=FloatLiteral(10.e10)
                                                    ),
                                                    Break()
                                                ])
                                            ]),
                                            elseStmt=Block([
                                                Continue()
                                            ])
                                        )
                                    ]),
                                    expr3=BinaryOp(
                                        op="+",
                                        left=IntLiteral(1),
                                        right=IntLiteral(2)
                                    )
                                )
                            ])
                        ),
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 42))

    def testReturnStmt(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Else{
                            a = 20;
                            Return a <= b;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=IntLiteral(20)
                                        ),
                                        Return(
                                            expr=BinaryOp(
                                                op="<=",
                                                left=Id("a"),
                                                right=Id("b")
                                            )
                                        )
                                    ]),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 44))

    def testElementExpression(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Else{
                            a = a[10];
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=ArrayCell(
                                                arr=Id("a"),
                                                idx=[IntLiteral(10)]
                                            )
                                        )
                                    ]),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 45))

    def testElementExpression2(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Else{
                            a = a[10][20];
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=ArrayCell(
                                                arr=Id("a"),
                                                idx=[
                                                    IntLiteral(10),
                                                    IntLiteral(20)
                                                ]
                                            )
                                        )
                                    ]),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 46))

    def testElementExpression3(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Else{
                            a = a[10][20][a[30][40]];
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=ArrayCell(
                                                arr=Id("a"),
                                                idx=[
                                                    IntLiteral(10),
                                                    IntLiteral(20),
                                                    ArrayCell(
                                                        arr=Id("a"),
                                                        idx=[
                                                            IntLiteral(30),
                                                            IntLiteral(40)
                                                        ]
                                                    )
                                                ]
                                            )
                                        )
                                    ]),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 47))

    def testForStmtWithIfStmt(self):
        i = """
               Class Adam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Else{
                            a = a[10][20][a[30][40]];
                        }
                        Foreach(i In 1 .. 200){ a = b;}
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=ArrayCell(
                                                arr=Id("a"),
                                                idx=[
                                                    IntLiteral(10),
                                                    IntLiteral(20),
                                                    ArrayCell(
                                                        arr=Id("a"),
                                                        idx=[
                                                            IntLiteral(30),
                                                            IntLiteral(40)
                                                        ]
                                                    )
                                                ]
                                            )
                                        )
                                    ]),
                                ),
                                For(
                                    id=Id("i"),
                                    expr1=IntLiteral(1),
                                    expr2=IntLiteral(200),
                                    loop=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=Id("b")
                                        )
                                    ]),
                                    expr3=IntLiteral(1)
                                )
                            ]
                            )
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 48))

    def testSimpleMethod(self):
        i = """
               Class Adam : Human{
                   main(){
                        Var a: Int = 3;
                    }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Adam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([
                                VarDecl(
                                    Id("a"),
                                    IntType(),
                                    IntLiteral(3)
                                )
                            ])
                        ),
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 49))

    def testSimpleClass(self):
        i = """
               Class Madam : Human{
                   main(){
                        Var a: Int = 3;
                    }
               }
               Class Ura : Human{} 
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([
                                VarDecl(
                                    Id("a"),
                                    IntType(),
                                    IntLiteral(3)
                                )
                            ])
                        ),
                    ],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Ura"),
                    [],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 50))

    def testEmptyClassX(self):
        i = """Class Madam{}"""
        e = str(Program(
            [ClassDecl(
                Id("Madam"),
                []
            )]
        ))
        self.assertTrue(TestAST.test(i, e, 51))

    def testEmptyClassXX(self):
        i = """Class Madam{}"""
        e = str(Program(
            [ClassDecl(
                Id("Madam"),
                []
            )]
        ))
        self.assertTrue(TestAST.test(i, e, 52))

    def testClassWithSuperClassX(self):
        i = "Class Ura : Human{}"
        e = str(Program(
            [ClassDecl(
                Id("Ura"),
                [],
                Id("Human")
            )]
        ))
        self.assertTrue(TestAST.test(i, e, 52))

    def testMainMethodInClassX(self):
        i = """
            Class Madam : Human{
                main(){}
            }
            Class Program: SuperClass{
                main(){}
            }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Program"),
                    [MethodDecl(
                        Static(),
                        Id("main"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 53))

    def testSimpleMultiClassX(self):
        i = """
                Class Madam: Human{}
                Class Ura{}
                Class Nova: Human{}
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Madam"),
                        [],
                        Id("Human")
                    ),
                    ClassDecl(
                        Id("Ura"),
                        [],
                    ),
                    ClassDecl(
                        Id("Nova"),
                        [],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 54))

    def testClassWithStaticMethodX(self):
        i = """
            Class _Madam : Human{
                $eatApple(){}
            }
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Madam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [],
                                Block([])
                            )
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 55))

    def testClassWithStaticMethodAndConstructorDestructorX(self):
        i = """
            Class _Madam : Human{
                $eatApple(){}
                Constructor(){}
                Destructor(){}
            }
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Madam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 56))

    def testOneParameterInMethodX(self):
        i = """
            Class _Madam : Human{
                $eatApple(space1, space2: Int){}
                Constructor(){}
                Destructor(){}
            }
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Madam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("space1"), IntType()),
                                    VarDecl(Id("space2"), IntType())
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 57))

    def testMultiParameterInMethodX(self):
        i = """
                Class _Madam : Human{
                    $eatApple(space1: Int; var3, var4: Float){}
                    Constructor(){}
                    Destructor(){}
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Madam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("space1"), IntType()),
                                    VarDecl(Id("var3"), FloatType()),
                                    VarDecl(Id("var4"), FloatType()),
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 58))

    def testMultiParameterInMethod2X(self):
        i = """
                Class _Madam : Human{
                    $eatApple(space1: Int; var3, var4: Float){}
                    Constructor(
                        s1, s2, s3: String;
                        b1: Boolean
                    ){}
                    Destructor(){}
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Madam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("space1"), IntType()),
                                    VarDecl(Id("var3"), FloatType()),
                                    VarDecl(Id("var4"), FloatType()),
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [
                                    VarDecl(Id("s1"), StringType()),
                                    VarDecl(Id("s2"), StringType()),
                                    VarDecl(Id("s3"), StringType()),
                                    VarDecl(Id("b1"), BoolType())
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 59))

    def testMultiParameterInMethod3X(self):
        i = """
                Class _Madam : Human{
                    $eatApple(
                        space1: Int;
                        var3, var4: Float;
                        o1, o2: SangHandsome
                    ){}
                    Constructor(
                        s1, s2, s3: String;
                        b1: Boolean
                    ){}
                    Destructor(){}
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Madam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("space1"), IntType()),
                                    VarDecl(Id("var3"), FloatType()),
                                    VarDecl(Id("var4"), FloatType()),
                                    VarDecl(Id("o1"), ClassType(Id("SangHandsome"))),
                                    VarDecl(Id("o2"), ClassType(Id("SangHandsome")))
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [
                                    VarDecl(Id("s1"), StringType()),
                                    VarDecl(Id("s2"), StringType()),
                                    VarDecl(Id("s3"), StringType()),
                                    VarDecl(Id("b1"), BoolType())
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 60))

    def testMultiParameterInMethodWithArrayTypeX(self):
        i = """
                Class _Madam : Human{
                    $eatApple(
                        space1: Int;
                        var3, var4: Float;
                        o1, o2: SangHandsome
                    ){}
                    eatUra(
                        var5: Array[Int, 4];
                        var6: Array[String, 1_000]
                    ){}
                    Constructor(
                        s1, s2, s3: String;
                        b1: Boolean
                    ){}
                    Destructor(){}
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Madam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("space1"), IntType()),
                                    VarDecl(Id("var3"), FloatType()),
                                    VarDecl(Id("var4"), FloatType()),
                                    VarDecl(Id("o1"), ClassType(Id("SangHandsome"))),
                                    VarDecl(Id("o2"), ClassType(Id("SangHandsome")))
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("eatUra"),
                                [
                                    VarDecl(Id("var5"), ArrayType(4, IntType())),
                                    VarDecl(Id("var6"), ArrayType(1000, StringType())),
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [
                                    VarDecl(Id("s1"), StringType()),
                                    VarDecl(Id("s2"), StringType()),
                                    VarDecl(Id("s3"), StringType()),
                                    VarDecl(Id("b1"), BoolType())
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 11))

    def testParameterInMethodWithNestedArrayTypeX(self):
        i = """
                Class _Madam : Human{
                    $eatApple(
                        space1: Int;
                        var3, var4: Float;
                        o1, o2: SangHandsome
                    ){}
                    eatUra(
                        var6: Array[Array[Int, 1_2_3_4], 1_000]
                    ){}
                    Constructor(
                        s1, s2, s3: String;
                        b1: Boolean
                    ){}
                    Destructor(){}
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Madam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("space1"), IntType()),
                                    VarDecl(Id("var3"), FloatType()),
                                    VarDecl(Id("var4"), FloatType()),
                                    VarDecl(Id("o1"), ClassType(Id("SangHandsome"))),
                                    VarDecl(Id("o2"), ClassType(Id("SangHandsome")))
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("eatUra"),
                                [
                                    VarDecl(
                                        Id("var6"),
                                        ArrayType(1000, ArrayType(1234, IntType()))
                                    ),
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [
                                    VarDecl(Id("s1"), StringType()),
                                    VarDecl(Id("s2"), StringType()),
                                    VarDecl(Id("s3"), StringType()),
                                    VarDecl(Id("b1"), BoolType())
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 62))

    def testParameterInMethodWithSuperNestedArrayTypeX(self):
        i = """
                Class _Madam : Human{
                    $eatApple(
                        space1: Int;
                        var3, var4: Float;
                        o1, o2: SangHandsome
                    ){}
                    eatUra(
                        var6: Array[Array[Array[Array[String, 4], 2_000], 1_2_3_4], 1_000]
                    ){}
                    Constructor(
                        s1, s2, s3: String;
                        b1: Boolean
                    ){}
                    Destructor(){}
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("_Madam"),
                        [
                            MethodDecl(
                                Static(),
                                Id("$eatApple"),
                                [
                                    VarDecl(Id("space1"), IntType()),
                                    VarDecl(Id("var3"), FloatType()),
                                    VarDecl(Id("var4"), FloatType()),
                                    VarDecl(Id("o1"), ClassType(Id("SangHandsome"))),
                                    VarDecl(Id("o2"), ClassType(Id("SangHandsome")))
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("eatUra"),
                                [
                                    VarDecl(
                                        Id("var6"),
                                        ArrayType(
                                            1000,
                                            ArrayType(
                                                1234,
                                                ArrayType(
                                                    2000,
                                                    ArrayType(
                                                        4,
                                                        StringType()
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Constructor"),
                                [
                                    VarDecl(Id("s1"), StringType()),
                                    VarDecl(Id("s2"), StringType()),
                                    VarDecl(Id("s3"), StringType()),
                                    VarDecl(Id("b1"), BoolType())
                                ],
                                Block([])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("Destructor"),
                                [],
                                Block([])
                            ),
                        ],
                        Id("Human")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 63))

    def testAttributeWithoutInitialValueX(self):
        i = """
            Class Ura{
                Var a,b: Boolean;
            }
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Ura"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("a"), BoolType())
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("b"), BoolType())
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 64))

    def testAttributeWithoutInitialValue2X(self):
        i = """
            Class Ura{
                Val a: Array[Int, 3] = Array(2, 3, 4);
                Var c, $d: Array[Array[String, 4], 1_000];
            }
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Ura"),
                        [
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("a"),
                                    ArrayType(
                                        3,
                                        IntType()
                                    ),
                                    ArrayLiteral(
                                        [
                                            IntLiteral(2),
                                            IntLiteral(3),
                                            IntLiteral(4)
                                        ]
                                    )
                                )
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("c"), ArrayType(1000, ArrayType(4, StringType())))
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(Id("$d"), ArrayType(1000, ArrayType(4, StringType())))
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 65))

    def testAttrConstDeclX(self):
        i = """
                Class Program {
                    Var a: Int;
                    Val a, b:Int = 2, 6;
                }
                """
        e = str(
            Program([
                ClassDecl(
                    Id("Program"),
                    [
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id('a'),
                                IntType()
                            )
                        ),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(
                                Id('a'),
                                IntType(),
                                IntLiteral(2)
                            )
                        ),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(
                                Id('b'),
                                IntType(),
                                IntLiteral(6)
                            )
                        )
                    ]
                )
            ]
            )
        )
        self.assertTrue(TestAST.test(i, e, 66))

    def testAttributeWithInitialValueX(self):
        i = """
            Class Ura{
                Var a, b: Boolean = True, False;
            }
        """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Ura"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("a"), BoolType(), BooleanLiteral(True))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("b"), BoolType(), BooleanLiteral(False))
                            ),

                        ],
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(i, e, 67))

    def testAttributeWithInitialIntX(self):
        i = """
                Class Ura{
                        Var s,a : Int = 0X2_4, 0x24; ## Hexa -> 36 ##
                        Val n,$g : Int = 02_4, 02004;  ## Octal -> 20, 1028 ##
                        Var $d,z : Int = 0b11_0_11, 0B11_011; ## Binary -> 27##
                        Val v,l : Int = 0, 24;       ## Decimal ##
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Ura"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("s"), IntType(), IntLiteral(36))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("a"), IntType(), IntLiteral(36))
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(Id("n"), IntType(), IntLiteral(20))
                            ),
                            AttributeDecl(
                                Static(),
                                ConstDecl(Id("$g"), IntType(), IntLiteral(1028))
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(Id("$d"), IntType(), IntLiteral(27))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("z"), IntType(), IntLiteral(27))
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(Id("v"), IntType(), IntLiteral(0))
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(Id("l"), IntType(), IntLiteral(24))
                            )
                        ],
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(i, e, 68))

    def testAttributeWithInitialFloatX(self):
        i = """
                Class Ura{
                        Var I, WANT, TEN, MARK : Float =  1.234, 1.2e3, 7E-5, 1_234.567;
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Ura"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("I"), FloatType(), FloatLiteral(1.234))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("WANT"), FloatType(), FloatLiteral(1200.0))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("TEN"), FloatType(), FloatLiteral(7e-05))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("MARK"), FloatType(), FloatLiteral(1234.567))
                            )
                        ],
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(i, e, 69))

    def testClassTypeX(self):
        i = """
                Class Ura{
                    Val haizz: Node = New Node();
                    Var $haizz: Node = New Node("Em dep lam");
                    Var newNode: Node;
                }
            """
        e = str(
            Program(
                [
                    ClassDecl(
                        Id("Ura"),
                        [
                            AttributeDecl(
                                Instance(),
                                ConstDecl(Id("haizz"), ClassType(Id("Node")), NewExpr(Id("Node"), []))
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(Id("$haizz"), ClassType(Id("Node")),
                                        NewExpr(Id("Node"), [StringLiteral("Em dep lam")]))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("newNode"), ClassType(Id("Node")), NullLiteral())
                            )
                        ],
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(i, e, 70))

    def testVariableDeclarationWithObjectCreationX(self):
        i = """
               Class Madam : Human{
                   main(){
                        Var a, b : A = New A(), New A();
                   }
               }
               Class Program: SuperClass{
                   main(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            VarDecl(Id("a"), ClassType(Id("A")), NewExpr(Id("A"), [])),
                            VarDecl(Id("b"), ClassType(Id("A")), NewExpr(Id("A"), []))
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Program"),
                    [MethodDecl(
                        Static(),
                        Id("main"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 71))

    def testVariableDeclarationWithPrimitiveTypeAndSelfX(self):
        i = """
               Class Madam : Human{
                   main(){
                        Val a, b : Int = Self.br, Self.uh;
                   }
               }
               Class Program: SuperClass{
                   main(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            ConstDecl(Id("a"), IntType(), FieldAccess(SelfLiteral(), Id("br"))),
                            ConstDecl(Id("b"), IntType(), FieldAccess(SelfLiteral(), Id("uh")))
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Program"),
                    [MethodDecl(
                        Static(),
                        Id("main"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 72))

    def testVariableDeclarationWithPrimitiveTypeAndSelf2X(self):
        i = """
               Class Madam : Human{
                   main(){
                        Val a, b : Int = Self.a.b.c.d, Self.e.f.h.i;
                   }
               }
               Class Program: SuperClass{
                   main(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            ConstDecl(
                                Id("a"), IntType(),
                                FieldAccess(
                                    FieldAccess(
                                        FieldAccess(
                                            FieldAccess(
                                                SelfLiteral(),
                                                Id("a")
                                            ),
                                            Id("b")
                                        ),
                                        Id("c")
                                    ),
                                    Id("d")
                                )
                            ),
                            ConstDecl(
                                Id("b"), IntType(),
                                FieldAccess(
                                    FieldAccess(
                                        FieldAccess(
                                            FieldAccess(
                                                SelfLiteral(),
                                                Id("e")
                                            ),
                                            Id("f")
                                        ),
                                        Id("h")
                                    ),
                                    Id("i")
                                )
                            )
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Program"),
                    [MethodDecl(
                        Static(),
                        Id("main"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 73))

    def testMethodInvocationStatic1X(self):
        i = """
               Class Madam : Human{
                   main(){
                        Ura::$hura();
                   }
               }
               Class Ura: SuperClass{
                   $hura(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            CallStmt(
                                obj=Id("Ura"),
                                method=Id("$hura"),
                                param=[]
                            )
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Ura"),
                    [MethodDecl(
                        Static(),
                        Id("$hura"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 74))

    def testMethodInvocationStatic2X(self):
        i = """
               Class Madam : Human{
                   main(){
                        Ura::$bara();
                   }
               }
               Class Ura: SuperClass{
                   $hura(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            CallStmt(
                                obj=Id("Ura"),
                                method=Id("$bara"),
                                param=[]
                            )
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Ura"),
                    [MethodDecl(
                        Static(),
                        Id("$hura"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 75))

    def testFieldAccessInstanceX(self):
        i = """
               Class Madam : Human{
                   main(){
                        Var a : String = Ura::$a.b.c;
                   }
               }
               Class Ura: SuperClass{
                   $hura(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            VarDecl(
                                variable=Id("a"),
                                varType=StringType(),
                                varInit=FieldAccess(
                                    obj=FieldAccess(
                                        obj=FieldAccess(
                                            obj=Id("Ura"),
                                            fieldname=Id("$a")
                                        ),
                                        fieldname=Id("b")
                                    ),
                                    fieldname=Id("c")
                                )
                            )
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Ura"),
                    [MethodDecl(
                        Static(),
                        Id("$hura"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 76))

    def testFieldAccessStaticX(self):
        i = """
               Class Madam : Human{
                   main(){
                        Var a : String = Ura::$a.b.c(0x24);
                   }
               }
               Class Ura: SuperClass{
                   $hura(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            VarDecl(
                                variable=Id("a"),
                                varType=StringType(),
                                varInit=CallExpr(
                                    obj=FieldAccess(
                                        obj=FieldAccess(
                                            obj=Id("Ura"),
                                            fieldname=Id("$a")
                                        ),
                                        fieldname=Id("b")
                                    ),
                                    method=Id("c"),
                                    param=[IntLiteral(36)]
                                )
                            )
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Ura"),
                    [MethodDecl(
                        Static(),
                        Id("$hura"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 77))

    def testMethodInvocationInstanceX(self):
        i = """
               Class Madam : Human{
                   main(){
                        Var a : String = Ura.a.b.c();
                   }
               }
               Class Ura: SuperClass{
                   $hura(){}
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        Block([
                            VarDecl(
                                variable=Id("a"),
                                varType=StringType(),
                                varInit=CallExpr(
                                    obj=FieldAccess(
                                        obj=FieldAccess(
                                            obj=Id("Ura"),
                                            fieldname=Id("a")
                                        ),
                                        fieldname=Id("b")
                                    ),
                                    method=Id("c"),
                                    param=[]
                                )
                            )
                        ])
                    )],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Ura"),
                    [MethodDecl(
                        Static(),
                        Id("$hura"),
                        [],
                        Block([])
                    )],
                    Id("SuperClass")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 78))

    def testAssignStatementNotExprX(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        a = !True;
                   }
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                Assign(
                                    lhs=Id("a"),
                                    exp=UnaryOp(
                                        op="!",
                                        body=BooleanLiteral(True)
                                    )
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 79))

    def testAssignStatementSignExprX(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        a = -10_000;
                   }
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                Assign(
                                    lhs=Id("a"),
                                    exp=UnaryOp(

                                        op="-",
                                        body=IntLiteral(10000)

                                    )
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 80))

    def testAssignStatementNotExpr2X(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        a = !(-0X24); ## 0X24 = 36 ##
                   }
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                Assign(
                                    lhs=Id("a"),
                                    exp=UnaryOp(
                                        op="!",
                                        body=UnaryOp(

                                            op="-",
                                            body=IntLiteral(36)

                                        )
                                    )
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 81))

    def testAssignStatementMulAddMolExprX(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        a = 20.5 * 10 / 2 % 5;
                   }
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                Assign(
                                    lhs=Id("a"),
                                    exp=BinaryOp(
                                        op="%",
                                        left=BinaryOp(
                                            op="/",
                                            left=BinaryOp(
                                                op="*",
                                                left=FloatLiteral(20.5),
                                                right=IntLiteral(10)
                                            ),
                                            right=IntLiteral(2)
                                        ),
                                        right=IntLiteral(5)
                                    )
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 82))

    def testAssignStatementAddSubExprX(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        a = (20.5 + 2) * (10 / (2 % 5)) + 10;
                   }
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                Assign(
                                    lhs=Id("a"),
                                    exp=BinaryOp(
                                        op="+",
                                        left=BinaryOp(
                                            op="*",
                                            left=BinaryOp(
                                                op="+",
                                                left=FloatLiteral(20.5),
                                                right=IntLiteral(2)
                                            ),
                                            right=BinaryOp(
                                                op="/",
                                                left=IntLiteral(10),
                                                right=BinaryOp(
                                                    op="%",
                                                    left=IntLiteral(2),
                                                    right=IntLiteral(5)
                                                )
                                            )
                                        ),
                                        right=IntLiteral(10)
                                    )
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 83))

    def testAssignStatementAndOrExprX(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        a = !(Ura.a || Ura.b) && Madam::$a;
                   }
               }
               """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                Assign(
                                    lhs=Id("a"),
                                    exp=BinaryOp(
                                        op="&&",
                                        left=UnaryOp(
                                            op="!",
                                            body=BinaryOp(
                                                op="||",
                                                left=FieldAccess(
                                                    obj=Id("Ura"),
                                                    fieldname=Id("a")
                                                ),
                                                right=FieldAccess(
                                                    obj=Id("Ura"),
                                                    fieldname=Id("b")
                                                )
                                            )
                                        ),
                                        right=FieldAccess(
                                            Id("Madam"),
                                            fieldname=Id("$a")
                                        )
                                    )
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 84))

    def testIfStatementRelationalExprX(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([])
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 85))

    def testIfStatementRelationalExpr2X(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){
                            a = !(Ura.a || Ura.b) && Madam::$a;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block(
                                        [
                                            Assign(
                                                lhs=Id("a"),
                                                exp=BinaryOp(
                                                    op="&&",
                                                    left=UnaryOp(
                                                        op="!",
                                                        body=BinaryOp(
                                                            op="||",
                                                            left=FieldAccess(
                                                                obj=Id("Ura"),
                                                                fieldname=Id("a")
                                                            ),
                                                            right=FieldAccess(
                                                                obj=Id("Ura"),
                                                                fieldname=Id("b")
                                                            )
                                                        )
                                                    ),
                                                    right=FieldAccess(
                                                        Id("Madam"),
                                                        fieldname=Id("$a")
                                                    )
                                                )
                                            )
                                        ]
                                    )

                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 86))

    def testIfStatementRelationalExpr3X(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Else{
                            a = 20;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=IntLiteral(20)
                                        )
                                    ]),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 87))

    def testIfStatementRelationalExpr4X(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Elseif(b){}
                        Else{
                            a = 20;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=If(
                                        expr=Id("b"),
                                        thenStmt=Block([]),
                                        elseStmt=Block([
                                            Assign(
                                                lhs=Id("a"),
                                                exp=IntLiteral(20)
                                            )
                                        ])
                                    ),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 88))

    def testIfStatementRelationalExpr5X(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){
                            Var a: Int;
                            If(k == 10){}
                            Else{
                                k = k * 2;
                            }
                        }
                        Elseif(b){}
                        Else{
                            a = 20;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([
                                        VarDecl(
                                            variable=Id("a"),
                                            varType=IntType(),
                                        ),
                                        If(
                                            expr=BinaryOp(
                                                op="==",
                                                left=Id("k"),
                                                right=IntLiteral(10)
                                            ),
                                            thenStmt=Block([]),
                                            elseStmt=Block([
                                                Assign(
                                                    lhs=Id("k"),
                                                    exp=BinaryOp(
                                                        op="*",
                                                        left=Id("k"),
                                                        right=IntLiteral(2)
                                                    )
                                                )
                                            ])
                                        )
                                    ]),
                                    elseStmt=If(
                                        expr=Id("b"),
                                        thenStmt=Block([]),
                                        elseStmt=Block([
                                            Assign(
                                                lhs=Id("a"),
                                                exp=IntLiteral(20)
                                            )
                                        ])
                                    ),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 89))

    def testIfStmtWithManyElseifX(self):
        i = """
               Class Program : Human{
                   main(){}
                   assign(){
                        If(a == 10){}
                        Elseif(b){}
                        Elseif(c){}
                        Elseif(d){}
                        Else{
                            a = 20;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Instance(),
                            Id("assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=If(
                                        expr=Id("b"),
                                        thenStmt=Block([]),
                                        elseStmt=If(
                                            expr=Id("c"),
                                            thenStmt=Block([]),
                                            elseStmt=If(
                                                expr=Id("d"),
                                                thenStmt=Block([]),
                                                elseStmt=Block([
                                                    Assign(
                                                        lhs=Id("a"),
                                                        exp=IntLiteral(20)
                                                    )
                                                ])
                                            )
                                        )
                                    ),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 90))

    def testForStmtX(self):
        i = """
               Class Program : Human{
                   main(){
                        Foreach(i In 1 .. 100_100 By 1 + 2){
                            S.print("Hello");
                        }
                   }
                   assign(){
                        If(a == 10){}
                        Elseif(b){}
                        Elseif(c){}
                        Elseif(d){}
                        Else{
                            a = 20;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([
                                For(
                                    id=Id("i"),
                                    expr1=IntLiteral(1),
                                    expr2=IntLiteral(100100),
                                    loop=Block([
                                        CallStmt(
                                            obj=Id("S"),
                                            method=Id("print"),
                                            param=[
                                                StringLiteral("Hello")
                                            ]
                                        )
                                    ]),
                                    expr3=BinaryOp(
                                        op="+",
                                        left=IntLiteral(1),
                                        right=IntLiteral(2)
                                    )
                                )
                            ])
                        ),
                        MethodDecl(
                            Instance(),
                            Id("assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=If(
                                        expr=Id("b"),
                                        thenStmt=Block([]),
                                        elseStmt=If(
                                            expr=Id("c"),
                                            thenStmt=Block([]),
                                            elseStmt=If(
                                                expr=Id("d"),
                                                thenStmt=Block([]),
                                                elseStmt=Block([
                                                    Assign(
                                                        lhs=Id("a"),
                                                        exp=IntLiteral(20)
                                                    )
                                                ])
                                            )
                                        )
                                    ),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 91))

    def testForStmtAndBreakContinueX(self):
        i = """
               Class Program : Human{
                   main(){
                        Foreach(i In 1 .. 100_100 By 1 + 2){
                            S.print("Hello");
                            If(a + b == "Sangs"){
                                Break;
                            }
                            Else{
                                Continue;
                            }
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([
                                For(
                                    id=Id("i"),
                                    expr1=IntLiteral(1),
                                    expr2=IntLiteral(100100),
                                    loop=Block([
                                        CallStmt(
                                            obj=Id("S"),
                                            method=Id("print"),
                                            param=[
                                                StringLiteral("Hello")
                                            ]
                                        ),
                                        If(
                                            expr=BinaryOp(
                                                op="==",
                                                left=BinaryOp(
                                                    op="+",
                                                    left=Id("a"),
                                                    right=Id("b")
                                                ),
                                                right=StringLiteral("Sangs")
                                            ),
                                            thenStmt=Block([
                                                Break()
                                            ]),
                                            elseStmt=Block([
                                                Continue()
                                            ])
                                        )
                                    ]),
                                    expr3=BinaryOp(
                                        op="+",
                                        left=IntLiteral(1),
                                        right=IntLiteral(2)
                                    )
                                )
                            ])
                        ),
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 92))

    def testNestedBlockStmtX(self):
        i = """
               Class Program : Human{
                   main(){
                        Foreach(i In 1 .. 100_100 By 1 + 2){
                            S.print("Hello");
                            If(a + b == "Sangs"){
                                {
                                    Val b: Float = 10.e10;
                                    Break;
                                }
                            }
                            Else{
                                Continue;
                            }
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([
                                For(
                                    id=Id("i"),
                                    expr1=IntLiteral(1),
                                    expr2=IntLiteral(100100),
                                    loop=Block([
                                        CallStmt(
                                            obj=Id("S"),
                                            method=Id("print"),
                                            param=[
                                                StringLiteral("Hello")
                                            ]
                                        ),
                                        If(
                                            expr=BinaryOp(
                                                op="==",
                                                left=BinaryOp(
                                                    op="+",
                                                    left=Id("a"),
                                                    right=Id("b")
                                                ),
                                                right=StringLiteral("Sangs")
                                            ),
                                            thenStmt=Block([
                                                Block([
                                                    ConstDecl(
                                                        constant=Id("b"),
                                                        constType=FloatType(),
                                                        value=FloatLiteral(10.e10)
                                                    ),
                                                    Break()
                                                ])
                                            ]),
                                            elseStmt=Block([
                                                Continue()
                                            ])
                                        )
                                    ]),
                                    expr3=BinaryOp(
                                        op="+",
                                        left=IntLiteral(1),
                                        right=IntLiteral(2)
                                    )
                                )
                            ])
                        ),
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 93))

    def testReturnStmtX(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Else{
                            a = 20;
                            Return a <= b;
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=IntLiteral(20)
                                        ),
                                        Return(
                                            expr=BinaryOp(
                                                op="<=",
                                                left=Id("a"),
                                                right=Id("b")
                                            )
                                        )
                                    ]),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 94))

    def testElementExpressionX(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Else{
                            a = a[10];
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=ArrayCell(
                                                arr=Id("a"),
                                                idx=[IntLiteral(10)]
                                            )
                                        )
                                    ]),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 95))

    def testElementExpression2X(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Else{
                            a = a[10][20];
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=ArrayCell(
                                                arr=Id("a"),
                                                idx=[
                                                    IntLiteral(10),
                                                    IntLiteral(20)
                                                ]
                                            )
                                        )
                                    ]),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 96))

    def testElementExpression3X(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Else{
                            a = a[10][20][a[30][40]];
                        }
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=ArrayCell(
                                                arr=Id("a"),
                                                idx=[
                                                    IntLiteral(10),
                                                    IntLiteral(20),
                                                    ArrayCell(
                                                        arr=Id("a"),
                                                        idx=[
                                                            IntLiteral(30),
                                                            IntLiteral(40)
                                                        ]
                                                    )
                                                ]
                                            )
                                        )
                                    ]),
                                )
                            ])
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 97))

    def testForStmtWithIfStmtX(self):
        i = """
               Class Madam : Human{
                   main(){}
                   $assign(){
                        If(a == 10){}
                        Else{
                            a[1][1+2] = a[10][20][a[30][40]];
                        }
                        Foreach(i In 1 .. 200){ a = b;}
                   }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        MethodDecl(
                            Static(),
                            Id("$assign"),
                            [],
                            Block([
                                If(
                                    expr=BinaryOp(
                                        op="==",
                                        left=Id("a"),
                                        right=IntLiteral(10)
                                    ),
                                    thenStmt=Block([]),
                                    elseStmt=Block([
                                        Assign(
                                            lhs=ArrayCell(
                                                arr=Id("a"),
                                                idx=[
                                                    IntLiteral(1),
                                                    BinaryOp(
                                                        op="+",
                                                        left=IntLiteral(1),
                                                        right=IntLiteral(2)
                                                    )
                                                ]
                                            ),
                                            exp=ArrayCell(
                                                arr=Id("a"),
                                                idx=[
                                                    IntLiteral(10),
                                                    IntLiteral(20),
                                                    ArrayCell(
                                                        arr=Id("a"),
                                                        idx=[
                                                            IntLiteral(30),
                                                            IntLiteral(40)
                                                        ]
                                                    )
                                                ]
                                            )
                                        )
                                    ]),
                                ),
                                For(
                                    id=Id("i"),
                                    expr1=IntLiteral(1),
                                    expr2=IntLiteral(200),
                                    loop=Block([
                                        Assign(
                                            lhs=Id("a"),
                                            exp=Id("b")
                                        )
                                    ]),
                                    expr3=IntLiteral(1)
                                )
                            ]
                            )
                        )
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 98))

    def testSimpleMethodX(self):
        i = """
               Class Madam : Human{
                   main(){
                        Var a: Int = 3;
                    }
               }
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([
                                VarDecl(
                                    Id("a"),
                                    IntType(),
                                    IntLiteral(3)
                                )
                            ])
                        ),
                    ],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 99))

    def testSimpleClassX(self):
        i = """
               Class Madam : Human{
                   main(){
                        Var a: Int = 3;
                    }
               }
               Class Ura : Human{} 
            """
        e = str(Program(
            [
                ClassDecl(
                    Id("Madam"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("main"),
                            [],
                            Block([
                                VarDecl(
                                    Id("a"),
                                    IntType(),
                                    IntLiteral(3)
                                )
                            ])
                        ),
                    ],
                    Id("Human")
                ),
                ClassDecl(
                    Id("Ura"),
                    [],
                    Id("Human")
                )
            ]
        ))
        self.assertTrue(TestAST.test(i, e, 100))

















