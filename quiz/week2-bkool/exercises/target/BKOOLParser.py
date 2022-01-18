# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\7\4")
        buf.write("(\n\4\f\4\16\4+\13\4\3\5\3\5\5\5/\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\5\78\n\7\3\b\3\b\3\b\7\b=\n\b\f\b\16\b@\13")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\5\nI\n\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\5\13Q\n\13\3\f\3\f\3\f\3\f\7\fW\n\f\f\f")
        buf.write("\16\fZ\13\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\2\2\20")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\3\3\2\3\4\2[\2")
        buf.write("\36\3\2\2\2\4!\3\2\2\2\6)\3\2\2\2\b.\3\2\2\2\n\60\3\2")
        buf.write("\2\2\f\67\3\2\2\2\16>\3\2\2\2\20A\3\2\2\2\22F\3\2\2\2")
        buf.write("\24P\3\2\2\2\26X\3\2\2\2\30[\3\2\2\2\32^\3\2\2\2\34`\3")
        buf.write("\2\2\2\36\37\5\4\3\2\37 \7\2\2\3 \3\3\2\2\2!\"\5\b\5\2")
        buf.write("\"#\5\6\4\2#\5\3\2\2\2$%\5\b\5\2%&\5\6\4\2&(\3\2\2\2\'")
        buf.write("$\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\7\3\2\2\2+)")
        buf.write("\3\2\2\2,/\5\n\6\2-/\5\20\t\2.,\3\2\2\2.-\3\2\2\2/\t\3")
        buf.write("\2\2\2\60\61\5\32\16\2\61\62\5\f\7\2\62\63\7\6\2\2\63")
        buf.write("\13\3\2\2\2\648\7\f\2\2\65\66\7\f\2\2\668\5\16\b\2\67")
        buf.write("\64\3\2\2\2\67\65\3\2\2\28\r\3\2\2\29:\7\7\2\2:;\7\f\2")
        buf.write("\2;=\5\16\b\2<9\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2")
        buf.write("?\17\3\2\2\2@>\3\2\2\2AB\5\32\16\2BC\7\f\2\2CD\5\22\n")
        buf.write("\2DE\5\34\17\2E\21\3\2\2\2FH\7\b\2\2GI\5\24\13\2HG\3\2")
        buf.write("\2\2HI\3\2\2\2IJ\3\2\2\2JK\7\t\2\2K\23\3\2\2\2LQ\5\30")
        buf.write("\r\2MN\5\30\r\2NO\5\26\f\2OQ\3\2\2\2PL\3\2\2\2PM\3\2\2")
        buf.write("\2Q\25\3\2\2\2RS\7\6\2\2ST\5\30\r\2TU\5\26\f\2UW\3\2\2")
        buf.write("\2VR\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y\27\3\2\2\2")
        buf.write("ZX\3\2\2\2[\\\5\32\16\2\\]\5\f\7\2]\31\3\2\2\2^_\t\2\2")
        buf.write("\2_\33\3\2\2\2`a\7\5\2\2a\35\3\2\2\2\t).\67>HPX")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'body'", "';'", "','", 
                     "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SEMI_COLON", "COMMA", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "ID", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_many_declaration = 1
    RULE_declaration_list = 2
    RULE_one_declaration = 3
    RULE_variable_declaration = 4
    RULE_identifer_list = 5
    RULE_identifer_list_tail = 6
    RULE_function_declaration = 7
    RULE_parameter = 8
    RULE_parameter_list = 9
    RULE_parameter_list_tail = 10
    RULE_one_parameter = 11
    RULE_typeVar = 12
    RULE_body = 13

    ruleNames =  [ "program", "many_declaration", "declaration_list", "one_declaration", 
                   "variable_declaration", "identifer_list", "identifer_list_tail", 
                   "function_declaration", "parameter", "parameter_list", 
                   "parameter_list_tail", "one_parameter", "typeVar", "body" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    SEMI_COLON=4
    COMMA=5
    LEFT_PAREN=6
    RIGHT_PAREN=7
    LEFT_CURLY_BRACKET=8
    RIGHT_CURLY_BRACKET=9
    ID=10
    WS=11
    ERROR_CHAR=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def many_declaration(self):
            return self.getTypedRuleContext(BKOOLParser.Many_declarationContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.many_declaration()
            self.state = 29
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def one_declaration(self):
            return self.getTypedRuleContext(BKOOLParser.One_declarationContext,0)


        def declaration_list(self):
            return self.getTypedRuleContext(BKOOLParser.Declaration_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_many_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_declaration" ):
                return visitor.visitMany_declaration(self)
            else:
                return visitor.visitChildren(self)




    def many_declaration(self):

        localctx = BKOOLParser.Many_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_many_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.one_declaration()
            self.state = 32
            self.declaration_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def one_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.One_declarationContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.One_declarationContext,i)


        def declaration_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Declaration_listContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Declaration_listContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_declaration_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_list" ):
                return visitor.visitDeclaration_list(self)
            else:
                return visitor.visitChildren(self)




    def declaration_list(self):

        localctx = BKOOLParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 34
                    self.one_declaration()
                    self.state = 35
                    self.declaration_list() 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(BKOOLParser.Variable_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(BKOOLParser.Function_declarationContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_one_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_declaration" ):
                return visitor.visitOne_declaration(self)
            else:
                return visitor.visitChildren(self)




    def one_declaration(self):

        localctx = BKOOLParser.One_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_one_declaration)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.function_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeVar(self):
            return self.getTypedRuleContext(BKOOLParser.TypeVarContext,0)


        def identifer_list(self):
            return self.getTypedRuleContext(BKOOLParser.Identifer_listContext,0)


        def SEMI_COLON(self):
            return self.getToken(BKOOLParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = BKOOLParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.typeVar()
            self.state = 47
            self.identifer_list()
            self.state = 48
            self.match(BKOOLParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifer_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def identifer_list_tail(self):
            return self.getTypedRuleContext(BKOOLParser.Identifer_list_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_identifer_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifer_list" ):
                return visitor.visitIdentifer_list(self)
            else:
                return visitor.visitChildren(self)




    def identifer_list(self):

        localctx = BKOOLParser.Identifer_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifer_list)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(BKOOLParser.ID)
                self.state = 52
                self.identifer_list_tail()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifer_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def identifer_list_tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Identifer_list_tailContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Identifer_list_tailContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_identifer_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifer_list_tail" ):
                return visitor.visitIdentifer_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def identifer_list_tail(self):

        localctx = BKOOLParser.Identifer_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_identifer_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 55
                    self.match(BKOOLParser.COMMA)
                    self.state = 56
                    self.match(BKOOLParser.ID)
                    self.state = 57
                    self.identifer_list_tail() 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeVar(self):
            return self.getTypedRuleContext(BKOOLParser.TypeVarContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def parameter(self):
            return self.getTypedRuleContext(BKOOLParser.ParameterContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = BKOOLParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.typeVar()
            self.state = 64
            self.match(BKOOLParser.ID)
            self.state = 65
            self.parameter()
            self.state = 66
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(BKOOLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BKOOLParser.RIGHT_PAREN, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(BKOOLParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = BKOOLParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(BKOOLParser.LEFT_PAREN)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.T__0 or _la==BKOOLParser.T__1:
                self.state = 69
                self.parameter_list()


            self.state = 72
            self.match(BKOOLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def one_parameter(self):
            return self.getTypedRuleContext(BKOOLParser.One_parameterContext,0)


        def parameter_list_tail(self):
            return self.getTypedRuleContext(BKOOLParser.Parameter_list_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = BKOOLParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameter_list)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.one_parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.one_parameter()
                self.state = 76
                self.parameter_list_tail()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMI_COLON)
            else:
                return self.getToken(BKOOLParser.SEMI_COLON, i)

        def one_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.One_parameterContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.One_parameterContext,i)


        def parameter_list_tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Parameter_list_tailContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Parameter_list_tailContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_parameter_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list_tail" ):
                return visitor.visitParameter_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list_tail(self):

        localctx = BKOOLParser.Parameter_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 80
                    self.match(BKOOLParser.SEMI_COLON)
                    self.state = 81
                    self.one_parameter()
                    self.state = 82
                    self.parameter_list_tail() 
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeVar(self):
            return self.getTypedRuleContext(BKOOLParser.TypeVarContext,0)


        def identifer_list(self):
            return self.getTypedRuleContext(BKOOLParser.Identifer_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_one_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_parameter" ):
                return visitor.visitOne_parameter(self)
            else:
                return visitor.visitChildren(self)




    def one_parameter(self):

        localctx = BKOOLParser.One_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_one_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.typeVar()
            self.state = 90
            self.identifer_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_typeVar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeVar" ):
                return visitor.visitTypeVar(self)
            else:
                return visitor.visitChildren(self)




    def typeVar(self):

        localctx = BKOOLParser.TypeVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_typeVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.T__0 or _la==BKOOLParser.T__1):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(BKOOLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





