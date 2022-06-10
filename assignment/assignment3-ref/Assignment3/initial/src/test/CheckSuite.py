# Trieu Minh Sang - 1852717

import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_1(self):
        """ Redeclared Variable/Function/Parameter """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("x"),[],None)
                ])
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_2(self):
        """ Redeclared Variable/Function/Parameter """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                    FuncDecl(
                        Id("x"),
                        [],
                        ([],[])
                    )
                ])
        expect = str(Redeclared(Function(),"x"))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_3(self):
        """ Redeclared Variable/Function/Parameter """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("b"),[],None)],[])
                    )
                ])
        expect = str(Redeclared(Variable(),"b"))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_4(self):
        """ Redeclared Variable/Function/Parameter """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("m"),[],None)],[])
                    )
                ])
        expect = str(Redeclared(Parameter(),"x"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_5(self):
        """ Redeclared Variable/Function/Parameter """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                    FuncDecl(
                        Id("foo"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("m"),[],None)],[])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("m"),[],None)],[])
                    )
                ])
        expect = str(Redeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_6(self):
        """ Redeclared Variable/Function/Parameter """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                    FuncDecl(
                        Id("foo1"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("m"),[],None)],[])
                    ),
                    FuncDecl(
                        Id("foo2"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("m"),[],None)],[])
                    ),
                    FuncDecl(
                        Id("main"),
                        [],
                        ([],[])
                    )
                ])
        expect = str(Redeclared(Parameter(),"x"))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_7(self):
        """ Redeclared Variable/Function/Parameter """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                    FuncDecl(
                        Id("printStrLn"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("m"),[],None)],[])
                    ),
                ])
        expect = str(Redeclared(Function(),"printStrLn"))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_8(self):
        """ Redeclared Variable/Function/Parameter """
        input = Program([
                    VarDecl(Id("printStrLn"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                    FuncDecl(
                        Id("foo"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("m"),[],None)],[])
                    ),
                ])
        expect = str(Redeclared(Variable(),"printStrLn"))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_9(self):
        """ Redeclared Variable/Function/Parameter """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("x"),[],None)],[])
                    ),
                ])
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_10(self):
        """ Redeclared Variable/Function/Parameter """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[],None),VarDecl(Id("n"),[],None)],[])
                    ),
                ])
        expect = str(Redeclared(Variable(),"n"))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_11(self):
        """ Redeclared Variable/Function/Parameter """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("foo"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                    FuncDecl(
                        Id("foo1"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("m"),[],None)],[])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [],
                        ([],[])
                    ),
                ])
        expect = str(Redeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_12(self):
        """ Redeclared Variable/Function/Parameter """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                    FuncDecl(
                        Id("foo1"),
                        [VarDecl(Id("foo1"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("m"),[],None)],[])
                    ),
                    FuncDecl(
                        Id("foo2"),
                        [VarDecl(Id("foo2"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("foo2"),[],None)],[])
                    ),
                    FuncDecl(
                        Id("main"),
                        [],
                        ([],[])
                    )
                ])
        expect = str(Redeclared(Variable(),"foo2"))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_13(self):
        """ No Entry Point """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                    FuncDecl(
                        Id("foo1"),
                        [VarDecl(Id("foo1"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([VarDecl(Id("m"),[],None)],[])
                    ),
                    FuncDecl(
                        Id("foo2"),
                        [],
                        ([],[])
                    )
                ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_14(self):
        """ No Entry Point """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[1,2,3],IntLiteral(3)),
                ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_15(self):
        """ No Entry Point """
        input = Program([
                    VarDecl(Id("main"),[],None)
                ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_16(self):
        """ No Entry Point """
        input = Program([
                    VarDecl(Id("main"),[],None),
                    FuncDecl(
                        Id("main"),
                        [],
                        ([],[])
                    )
                ])
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_17(self):
        """ Undeclared Identifier/Function """
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [],
                        ([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [],
                        ([VarDecl(Id("z"),[],None)],[Assign(Id("z"),Id("x"))])
                    )
                ])
        expect = str(Undeclared(Identifier(),"x"))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_18(self):
        """ Undeclared Identifier/Function """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    FuncDecl(
                        Id("main"),
                        [],
                        ([],[Assign(Id("x"),Id("y"))])
                    )
                ])
        expect = str(Undeclared(Identifier(),"y"))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_19(self):
        """ Undeclared Identifier/Function """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    FuncDecl(
                        Id("main"),
                        [],
                        ([],[Assign(Id("x"),CallExpr(Id("foo"),[]))])
                    )
                ])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_20(self):
        """ Undeclared Identifier/Function """
        input = Program([
                    FuncDecl(
                        Id("x"),
                        [],
                        ([],[])
                    ),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([],[CallStmt(Id("foo"),[])])
                    ),
                ])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_21(self):
        """ Undeclared Identifier/Function """
        input = Program([
                    VarDecl(Id("foo"),[],None),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([],[Assign(Id("x"),CallExpr(Id("foo"),[]))])
                    )
                ])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_22(self):
        """  Type Cannot Be Inferred """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("y"),[],None)],
                        ([],[Assign(Id("x"),Id("y"))])
                    )
                ])
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_23(self):
        """  Type Cannot Be Inferred """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[],None),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],
                        ([],[Assign(Id("x"),Id("y"))])
                    )
                ])
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_24(self):
        """  Type Cannot Be Inferred """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[],None),
                    VarDecl(Id("z"),[],None),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("m"),[],None)],
                        ([],[
                                Assign(Id("x"),IntLiteral(2)),
                                Assign(Id("y"),Id("x")),
                                Assign(Id("z"),Id("m")),
                            ])
                    )
                ])
        expect = str(TypeCannotBeInferred(Assign(Id("z"),Id("m"))))
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_25(self):
        """  Type Cannot Be Inferred """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[],None),
                    VarDecl(Id("z"),[],None),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],
                        ([],[
                                Assign(Id("x"),IntLiteral(2)),
                                Assign(Id("y"),Id("x")),
                                Assign(Id("z"),Id("x")),
                            ])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [],
                        ([VarDecl(Id("m"),[],None)],[
                                Assign(Id("m"),Id("x")),
                            ])
                    )
                ])
        expect = str(TypeCannotBeInferred(Assign(Id("m"),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_26(self):
        """  Type Cannot Be Inferred """
        input = Program([
                    VarDecl(Id("x"),[],None),
                    VarDecl(Id("y"),[],None),
                    VarDecl(Id("z"),[],None),
                    FuncDecl(
                        Id("main"),
                        [],
                        ([],[
                                Assign(Id("x"),IntLiteral(2)),
                                Assign(Id("y"),Id("x")),
                                Assign(Id("z"),Id("x")),
                            ])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],
                        ([VarDecl(Id("m"),[],None)],[
                                Assign(Id("z"),Id("x")),
                                Assign(Id("m"),Id("y")),
                            ])
                    )
                ])
        expect = str(TypeCannotBeInferred(Assign(Id("m"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_27(self):
        """  Type Cannot Be Inferred """
        input = Program([
                    VarDecl(Id("x"),[],IntLiteral(2)),
                    VarDecl(Id("y"),[],BooleanLiteral(True)),
                    VarDecl(Id("z"),[],None),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("y"),[],None),VarDecl(Id("m"),[],None)],
                        ([],[
                                Assign(Id("m"),Id("y")),
                            ])
                    )
                ])
        expect = str(TypeCannotBeInferred(Assign(Id("m"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_28(self):
        """  Type Cannot Be Inferred """
        input = Program([
                    VarDecl(Id("x"),[],IntLiteral(2)),
                    FuncDecl(
                        Id("foo"),
                        [VarDecl(Id("y"),[],None),VarDecl(Id("m"),[],None)],
                        ([],[
                            Assign(Id("y"),IntLiteral(2))
                        ])
                    ),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("y"),[],None),VarDecl(Id("m"),[],None)],
                        ([],[
                                CallStmt(Id("foo"),[Id("x"),Id("y")]),
                                Assign(Id("y"),Id("m"))
                            ])
                    )
                ])
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("x"),Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_29(self):
        """  Type Cannot Be Inferred """
        input = Program([
                    VarDecl(Id("foo"),[],None),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([],[Assign(Id("x"),CallExpr(Id("foo"),[]))])
                    )
                ])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_30(self):
        """  Type Cannot Be Inferred """
        input = Program([
                    VarDecl(Id("foo"),[],None),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([],[Assign(Id("x"),CallExpr(Id("foo"),[]))])
                    )
                ])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_31(self):
        input = Program([
                    VarDecl(Id("foo"),[],None),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([],[Assign(Id("x"),CallExpr(Id("foo"),[]))])
                    )
                ])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_32(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                Assign(Id("x"),FloatLiteral(1.0)),
                                CallStmt(Id("main"),[Id("y")])
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,431))
        
    def test_33(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                Assign(Id("x"),FloatLiteral(1.0)),
                                CallStmt(Id("main"),[Id("y")])
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_34(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                CallStmt(Id("main"),[Id("y")]),
                                Assign(Id("x"),FloatLiteral(1.0))
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_35(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [VarDecl(Id("y"),[],None)],
                        ([VarDecl(Id("x"),[],IntLiteral(1)),VarDecl(Id("z"),[],FloatLiteral(1.2))],[
                            CallStmt(Id("main"),[Id("x")]),
                            CallStmt(Id("main"),[Id("y")]),
                            CallStmt(Id("foo"),[Id("z")])
                        ])
                    )
                ])
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("z")])))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_36(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_37(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_38(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                Assign(Id("x"),FloatLiteral(1.0)),
                                Assign(Id("x"),CallExpr(Id("string_of_int"),[Id("y")]))
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("string_of_int"),[Id("y")]))))
        self.assertTrue(TestChecker.test(input,expect,437))
    
    def test_39(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],
                        ([],[
                                Assign(Id("x"),IntLiteral(1)),
                                CallStmt(Id("main"),[FloatLiteral(1.1),IntLiteral(1)]),
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[FloatLiteral(1.1),IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_40(self):
        input = Program([
                    FuncDecl(
                        Id("foo"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],
                        ([],[

                        ])
                    ),
                    FuncDecl(
                        Id("main"),
                        [],
                        ([],[
                            CallStmt(Id("foo"),[IntLiteral(1),IntLiteral(2)]),
                            CallStmt(Id("foo"),[FloatLiteral(1.1),FloatLiteral(2.2)])
                        ])
                    )
                ])
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[FloatLiteral(1.1),FloatLiteral(2.2)])))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_41(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [],
                        ([],[
                                Return(IntLiteral(1)),
                                Return(FloatLiteral(1.1))
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_42(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [],
                        ([],[
                                Return(None),
                                Return(StringLiteral("abc"))
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Return(StringLiteral("abc"))))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_43(self):
        input = Program([
                    FuncDecl(
                        Id("foo"),
                        [],
                        ([],[

                            ])
                    ),
                    FuncDecl(
                        Id("main"),
                        [],
                        ([VarDecl(Id("x"),[],IntLiteral(1)),VarDecl(Id("b"),[],BooleanLiteral(False))],[
                                Assign(Id("x"),CallExpr(Id("foo"),[])),
                                Assign(Id("b"),CallExpr(Id("foo"),[]))
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("b"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_44(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("a"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                Assign(Id("a"),CallExpr(Id("foo"),[])),
                            ])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [],
                        ([],[
                                Return(IntLiteral(1)),
                            ])
                    )
                ])
        expect = str(TypeCannotBeInferred(Assign(Id("a"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_45(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                                Assign(Id("a"),CallExpr(Id("foo"),[])),
                            ])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [],
                        ([],[
                                Return(FloatLiteral(1.1)),
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_46(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [],
                        ([VarDecl(Id("x"),[],None)],[
                                CallStmt(Id("foo"),[Id("x")]),
                            ])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [],
                        ([],[

                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_47(self):
        input = Program([
                    FuncDecl(
                        Id("foo1"),
                        [VarDecl(Id("x"),[],None)],
                        ([],[
                                Return(IntLiteral(1))
                            ])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [],
                        ([],[
                                Return(CallExpr(Id("foo1"),[CallExpr(Id("foo1"),[IntLiteral(3)])]))
                            ])
                    ),
                    FuncDecl(
                        Id("main"),
                        [],
                        ([VarDecl(Id("x"),[],FloatLiteral(1.))],[
                                Assign(Id("x"),CallExpr(Id("foo"),[])),
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_48(self):
        input = Program([
                    FuncDecl(
                        Id("f1"),
                        [VarDecl(Id("x"),[],None)],
                        ([],[
                                Return(IntLiteral(0))
                            ])
                    ),
                    FuncDecl(
                        Id("main"),
                        [],
                        ([VarDecl(Id("a"),[],IntLiteral(1)),VarDecl(Id("n"),[],None)],[
                                Assign(
                                    Id("a"),
                                    CallExpr(Id("f1"),[CallExpr(Id("f2"),[CallExpr(Id("f3"),[Id("n")])])])
                                )
                            ])
                    ),
                    FuncDecl(
                        Id("f2"),
                        [VarDecl(Id("x"),[],None)],
                        ([],[
                                Return(IntLiteral(0))
                            ])
                    ),
                    FuncDecl(
                        Id("f3"),
                        [VarDecl(Id("x"),[],None)],
                        ([],[
                                Return(IntLiteral(0))
                            ])
                    )
                ])
        expect = str(TypeCannotBeInferred(Assign(Id("a"),CallExpr(Id("f1"),[CallExpr(Id("f2"),[CallExpr(Id("f3"),[Id("n")])])]))))
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_49(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([],[
                                CallStmt(Id("main"),[CallExpr(Id("main"),[IntLiteral(5)])])
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[CallExpr(Id("main"),[IntLiteral(5)])])))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_50(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                CallStmt(Id("main"),[Id("y")]),
                                Assign(Id("x"),FloatLiteral(1.0))
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,449))

    # Here

    def test_51(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                CallStmt(Id("main"),[BinaryOp("+",Id("y"),Id("y"))]),
                                Assign(Id("x"),FloatLiteral(1.0))
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_52(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],
                        ([VarDecl(Id("m"),[],FloatLiteral(1))],[
                                Assign(Id("x"),BinaryOp("+",Id("x"),Id("y"))),
                                CallStmt(Id("main"),[FloatLiteral(1.),FloatLiteral(2.)])
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[FloatLiteral(1.),FloatLiteral(2.)])))
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_53(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1)),VarDecl(Id("z"),[],StringLiteral("abc")),VarDecl(Id("m"),[],BooleanLiteral(True))],[
                                Assign(Id("x"),BinaryOp("+",Id("y"),Id("z")))
                            ])
                    )
                ])
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("y"),Id("z"))))
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_54(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [],
                        ([VarDecl(Id("x"),[],None)],[
                                Assign(Id("x"),CallExpr(Id("foo"),[Id("x")]))
                            ])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [],
                        ([],[

                            ])
                    )
                ])
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_55(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1)),VarDecl(Id("z"),[],FloatLiteral(1.)),VarDecl(Id("m"),[],FloatLiteral(2.))],[
                                Assign(Id("x"),BinaryOp("+",BinaryOp("+.",Id("y"),Id("z")),Id("y")))
                            ])
                    )
                ])
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("y"),Id("z"))))
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_56(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1)),VarDecl(Id("z"),[],FloatLiteral(1.)),VarDecl(Id("m"),[],FloatLiteral(2.))],[
                                Assign(Id("x"),BinaryOp("+",Id("y"),BinaryOp("+.",Id("y"),Id("z"))))
                            ])
                    )
                ])
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("y"),Id("z"))))
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_57(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1)),VarDecl(Id("z"),[],FloatLiteral(1.)),VarDecl(Id("m"),[],FloatLiteral(2.))],[
                                Assign(Id("x"),BinaryOp("+",Id("y"),BinaryOp("+.",Id("m"),Id("z"))))
                            ])
                    )
                ])
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("y"),BinaryOp("+.",Id("m"),Id("z")))))
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_58(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1)),VarDecl(Id("z"),[],FloatLiteral(1.)),VarDecl(Id("m"),[],FloatLiteral(2.))],[
                                Assign(Id("y"),BinaryOp("-.",BinaryOp("+.",Id("m"),Id("z")),BinaryOp("+.",Id("m"),Id("z"))))
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("y"),BinaryOp("-.",BinaryOp("+.",Id("m"),Id("z")),BinaryOp("+.",Id("m"),Id("z"))))))
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_59(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                Assign(Id("x"),UnaryOp("-",Id("y"))),
                                CallStmt(Id("main"),[FloatLiteral(1.2)])
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[FloatLiteral(1.2)])))
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_60(self):
        input = Program([
                    FuncDecl(
                        Id("foo"),
                        [VarDecl(Id("x"),[],None)],
                        ([],[
                                Return(IntLiteral(2))
                            ])
                    ),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],None),VarDecl(Id("a"),[],None)],[
                                Assign(Id("y"),BinaryOp("+",Id("a"),CallExpr(Id("foo"),[Id("x")])))
                            ])
                    )
                ])
        expect = str(TypeCannotBeInferred(Assign(Id("y"),BinaryOp("+",Id("a"),CallExpr(Id("foo"),[Id("x")])))))
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_61(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [],
                        ([],[
                                Return(None)
                            ])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
                        ([],[
                                Assign(Id("a"),IntLiteral(3)),
                                Assign(Id("b"),FloatLiteral(4.2)),
                                Assign(Id("a"),Id("b"))
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_62(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                Assign(Id("x"),BinaryOp("+",Id("x"),CallExpr(Id("foo"),[])))
                            ])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [],
                        ([],[
                                Return(None)
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Return(None)))
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_63(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                Assign(Id("x"),UnaryOp("-",BinaryOp("-.",Id("x"),CallExpr(Id("foo"),[]))))
                            ])
                    ),
                    FuncDecl(
                        Id("foo"),
                        [],
                        ([],[
                                Return(None)
                            ])
                    )
                ])
        expect = str(TypeMismatchInExpression(UnaryOp("-",BinaryOp("-.",Id("x"),CallExpr(Id("foo"),[])))))
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_64(self):
        input = Program([
                    FuncDecl(
                        Id("foo"),
                        [VarDecl(Id("x"),[],None)],
                        ([],[
                                Return(FloatLiteral(1.))
                            ])
                    ),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1)),VarDecl(Id("m"),[],None)],[
                                Assign(Id("x"),UnaryOp("-",BinaryOp("-.",Id("x"),CallExpr(Id("foo"),[Id("m")]))))
                            ])
                    )
                ])
        expect = str(TypeCannotBeInferred(Assign(Id("x"),UnaryOp("-",BinaryOp("-.",Id("x"),CallExpr(Id("foo"),[Id("m")]))))))
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_65(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                If([(IntLiteral(1),[],[])],([],[]))
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(If([(IntLiteral(1),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_66(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                If([(Id("x"),[],[])],([],[])),
                                Assign(Id("x"),Id("y"))
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_67(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("y"),[],IntLiteral(1))],[
                                If(
                                    [
                                        (Id("x"),
                                        [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("x"),[],None)],
                                        [])
                                    ],
                                    (
                                        [],
                                        []
                                    )
                                ),
                            ])
                    )
                ])
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_68(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                                If(
                                    [
                                        (BinaryOp(">",Id("a"),IntLiteral(3)),
                                        [],
                                        [
                                            Return(IntLiteral(1))
                                        ])
                                    ],
                                    (
                                        [],
                                        [
                                            Return(FloatLiteral(2.))
                                        ]
                                    )
                                ),
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(2.))))
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_69(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                                If(
                                    [
                                        (BinaryOp(">",Id("a"),IntLiteral(3)),
                                        [VarDecl(Id("x"),[],None)],
                                        [
                                            Assign(Id("x"),IntLiteral(1))
                                        ]),
                                        (BinaryOp(">",Id("a"),IntLiteral(3)),
                                        [],
                                        [
                                            CallStmt(Id("main"),[Id("x")])
                                        ])
                                    ],
                                    (
                                        [],
                                        [
                                            Return(FloatLiteral(2.))
                                        ]
                                    )
                                ),
                            ])
                    )
                ])
        expect = str(TypeCannotBeInferred(CallStmt(Id("main"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_70(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                                If(
                                    [
                                        (BinaryOp(">",Id("a"),IntLiteral(3)),
                                        [],
                                        [
                                            Assign(Id("x"),FloatLiteral(1))
                                        ]),
                                        (BinaryOp(">",Id("a"),IntLiteral(3)),
                                        [],
                                        [
                                            Assign(Id("a"),CallExpr(Id("main"),[Id("x")]))
                                        ])
                                    ],
                                    (
                                        [],
                                        [
                                            Return(FloatLiteral(2.))
                                        ]
                                    )
                                ),
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(2.))))
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_71(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                                If(
                                    [
                                        (BinaryOp(">",Id("a"),IntLiteral(3)),
                                        [VarDecl(Id("b"),[],None)],
                                        [
                                            Assign(Id("x"),FloatLiteral(1))
                                        ]),
                                        (BinaryOp(">",Id("a"),IntLiteral(3)),
                                        [],
                                        [
                                            Assign(Id("b"),CallExpr(Id("main"),[Id("x")]))
                                        ])
                                    ],
                                    (
                                        [],
                                        [
                                            Return(FloatLiteral(2.))
                                        ]
                                    )
                                ),
                            ])
                    )
                ])
        expect = str(Undeclared(Identifier(),"b"))
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_72(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                                If(
                                    [
                                        (BinaryOp(">",Id("a"),IntLiteral(3)),
                                        [VarDecl(Id("b"),[],None)],
                                        [
                                            Assign(Id("x"),FloatLiteral(1))
                                        ]),
                                        (BinaryOp(">",Id("a"),IntLiteral(3)),
                                        [],
                                        [
                                            Assign(Id("a"),CallExpr(Id("main"),[Id("x")]))
                                        ])
                                    ],
                                    (
                                        [],
                                        [
                                            Assign(Id("b"),CallExpr(Id("main"),[Id("x")]))
                                        ]
                                    )
                                ),
                            ])
                    )
                ])
        expect = str(Undeclared(Identifier(),"b"))
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_73(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                                If(
                                    [
                                        (Id("x"),
                                        [VarDecl(Id("b"),[],None)],
                                        [
                                            Assign(Id("x"),FloatLiteral(1))
                                        ])
                                    ],
                                    (
                                        [],
                                        [

                                        ]
                                    )
                                ),
                            ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_74(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],FloatLiteral(1.))],[
                            For(
                                Id("a"),
                                IntLiteral(1),
                                BooleanLiteral(True),
                                IntLiteral(2),
                                ([],[])
                            )
                        ])
                    )
                ])
        expect = str(TypeMismatchInStatement(For(
                                    Id("a"),
                                    IntLiteral(1),
                                    BooleanLiteral(True),
                                    IntLiteral(2),
                                    ([],[])
                                )))
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_75(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                            For(
                                Id("a"),
                                FloatLiteral(1.),
                                BooleanLiteral(True),
                                IntLiteral(2),
                                ([],[])
                            )
                        ])
                    )
                ])
        expect = str(TypeMismatchInStatement(For(
                                    Id("a"),
                                    FloatLiteral(1.),
                                    BooleanLiteral(True),
                                    IntLiteral(2),
                                    ([],[])
                                )))
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_76(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                            For(
                                Id("a"),
                                IntLiteral(1),
                                IntLiteral(2),
                                IntLiteral(2),
                                ([],[])
                            )
                        ])
                    )
                ])
        expect = str(TypeMismatchInStatement(For(
                                    Id("a"),
                                    IntLiteral(1),
                                    IntLiteral(2),
                                    IntLiteral(2),
                                    ([],[])
                                )))
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_77(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                            For(
                                Id("a"),
                                IntLiteral(1),
                                BooleanLiteral(True),
                                CallExpr(Id("main"),[Id("x")]),
                                ([],[])
                            )
                        ])
                    )
                ])
        expect = str(TypeCannotBeInferred(For(
                                    Id("a"),
                                    IntLiteral(1),
                                    BooleanLiteral(True),
                                    CallExpr(Id("main"),[Id("x")]),
                                    ([],[])
                                )))
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_78(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                            For(
                                Id("a"),
                                IntLiteral(1),
                                BooleanLiteral(True),
                                Id("x"),
                                ([],[
                                    CallStmt(Id("main"),[FloatLiteral(1.)])
                                ])
                            )
                        ])
                    )
                ])
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[FloatLiteral(1.)])))
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_79(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                            For(
                                Id("a"),
                                IntLiteral(1),
                                CallExpr(Id("main"),[FloatLiteral(1.)]),
                                Id("x"),
                                ([],[

                                ])
                            )                   
                        ])
                    )
                ])
        expect = str(TypeMismatchInStatement(For(
                                Id("a"),
                                IntLiteral(1),
                                CallExpr(Id("main"),[FloatLiteral(1.)]),
                                Id("x"),
                                ([],[
                                    
                                ])
                            )))
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_80(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                            For(
                                Id("a"),
                                IntLiteral(1),
                                CallExpr(Id("main"),[FloatLiteral(1.)]),
                                Id("a"),
                                ([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[
                                    Assign(Id("x"),Id("y"))
                                ])
                            )                   
                        ])
                    )
                ])
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_81(self):
        input = Program([
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("x"),[],None)],
                        ([VarDecl(Id("a"),[],IntLiteral(1))],[
                            For(
                                Id("a"),
                                IntLiteral(1),
                                CallExpr(Id("main"),[FloatLiteral(1.)]),
                                Id("a"),
                                ([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[
                                    
                                ])
                            ),
                            Assign(Id("x"),Id("y"))                   
                        ])
                    ),
                ])
        expect = str(Undeclared(Identifier(),"y"))
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_82(self):
        input = Program([
                    VarDecl(Id("x"),[],ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([FloatLiteral(1.),FloatLiteral(2.)])])]),IntLiteral(3),IntLiteral(4)])),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("a"),[],None),VarDecl(Id("y"),[],None)],
                        ([],[
                            Assign(ArrayCell(Id("x"),[IntLiteral(2),IntLiteral(1),IntLiteral(9),IntLiteral(5)]),Id("a")),
                            Assign(Id("a"),IntLiteral(1))
                        ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("a"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,481))

    #Here

    def test_83(self):
        input = """
        Function: foo
        Body:
            Var: x[5], y[5];
            x = y;
        EndBody.
        Function: main
        Body:
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_84(self):
        input = """ 
        Function: main
        Body:
            Var: x;
            For (x = 1, True, x -. 1.9) Do

            EndFor.
        EndBody.
            """
        expect = str(TypeMismatchInExpression(BinaryOp('-.',Id('x'),FloatLiteral(1.9))))
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_85(self):
        input = """ 
        Function: main
        Body:
            Var: x;
            Do x = 1;
            While 1
            EndDo.
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Dowhile(([],[Assign(Id('x'),IntLiteral(1))]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_86(self):
        input = """ 
        Function: main
        Body:
            While 1
            Do
            EndWhile.
        EndBody.
            """
        expect = str(TypeMismatchInStatement(While(IntLiteral(1),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_87(self):
        input = """
        Function: a
        Parameter: x
        Body:
            Return x + 1;
        EndBody.
        Function: b
        Parameter: x
        Body:
            Return a(x);
        EndBody.
        Function: c
        Parameter: x
        Body:
            Return b(x);
        EndBody.
        Function: main
        Parameter: x
        Body:
            While a(b(x)) == b(c(x)) Do
                Do
                    x = x + 1;
                While c(b(x)) == b(a(x)) EndDo.
            EndWhile.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_88(self):
        input = """ 
        Function: main
        Body:
            While True
            Do
                Var: x = 4;
                While True
                Do
                    x = 5.0;
                EndWhile.
            EndWhile.
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),FloatLiteral(5.0))))
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_89(self):
        input = """
        Function: main
        Body:
            Return int_of_float(a(1.0));
        EndBody.
        Function: a
        Parameter: x
        Body:
            Return main();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(CallExpr(Id("main"),[]))))
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_90(self):
        input = """
        Function: main
        Parameter: main
        Body:
            If main Then
                Var: main;
                For (main = main, main == main, main) Do
                    Var: main;
                    While main =/= main Do
                        Var: main;
                        Do
                            Return main;
                        While main && main EndDo.
                    EndWhile.
                EndFor.
            EndIf.
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id("main"))))
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_91(self):
        input = """
        Function: main
        Body:
            Var: x = 0;
            If f(g(x)) == g(f(x)) Then
                printStrLn("Hello World");
            EndIf.
        EndBody.
        Function: f
        Parameter: x
        Body:
            Return f(x);
        EndBody.
        Function: g
        Parameter: x
        Body:
            Return g(x);
        EndBody.
        """
        expect = str(TypeCannotBeInferred(If([(BinaryOp("==",CallExpr(Id("f"),[CallExpr(Id("g"),[Id("x")])]),CallExpr(Id("g"),[CallExpr(Id("f"),[Id("x")])])),[],[CallStmt(Id("printStrLn"),[StringLiteral("Hello World")])])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_92(self):
        input = Program([
                    VarDecl(Id("x"),[],ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([FloatLiteral(1.),FloatLiteral(2.)])])]),IntLiteral(3),IntLiteral(4)])),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("a"),[],None),VarDecl(Id("y"),[],None)],
                        ([],[
                            Assign(ArrayCell(Id("x"),[IntLiteral(2),IntLiteral(1),IntLiteral(9),IntLiteral(5)]),Id("a")),
                            Assign(Id("a"),IntLiteral(1))
                        ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("a"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,491))


    def test_93(self):
        input = """
        Function: main
        Body:
            printStrLn("Hello World!");
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_94(self):
        input = Program([
                    VarDecl(Id("x"),[],ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([FloatLiteral(1.),FloatLiteral(2.)])])]),IntLiteral(3),IntLiteral(4)])),
                    FuncDecl(
                        Id("main"),
                        [VarDecl(Id("a"),[],None),VarDecl(Id("y"),[],None)],
                        ([],[
                            Assign(ArrayCell(Id("x"),[IntLiteral(2),IntLiteral(1),IntLiteral(9),IntLiteral(5)]),Id("a")),
                            Assign(Id("a"),IntLiteral(1))
                        ])
                    )
                ])
        expect = str(TypeMismatchInStatement(Assign(Id("a"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_95(self):
        input = """
        Var: x;

        Function: main
        Body:
            x = foo2();
        EndBody.

        Function: foo2
        Body:
            Return 2.0;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('x'),CallExpr(Id('foo2'),[]))))
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_96(self):
        input = """
        Function: foo
        Parameter: x
        Body:
            Return -.main(foo(x));
        EndBody.
        Function: main
        Parameter: x
        Body:
            Return -.x;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(UnaryOp("-.",CallExpr(Id("main"),[CallExpr(Id("foo"),[Id("x")])])))))
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_97(self):
        input = """
        Function: main
        Body:
            Var: x;
            x = foo(5.0) + 1;
        EndBody.
        Function: foo
        Parameter: a
        Body:
            Return a;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id("a"))))
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_98(self):
        input = """
        Function: main
        Body:
            Var: x;
            x = x + test();
        EndBody.

        Function: test
        Body:
            Return 1.9;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.9))))
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_99(self):
        input = """
        Var: x; 
        Function: main
        Parameter: a,b
        Body:
            x = a + b + test();
        EndBody.

        Function: test
        Body:
            Return 3.5;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(3.5))))
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_100(self):
        input = """
        Function: main
        Body:
            printStrLn("The End! Thanks for reading");
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,499))
