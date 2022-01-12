# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\62")
        buf.write("%\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\5\6!\n\6\3\6\3\6\3\6\2\2\7\2\4\6\b")
        buf.write("\n\2\3\3\2\4\5\2!\2\f\3\2\2\2\4\27\3\2\2\2\6\31\3\2\2")
        buf.write("\2\b\34\3\2\2\2\n\36\3\2\2\2\f\r\5\4\3\2\r\16\7\3\2\2")
        buf.write("\16\17\7\37\2\2\17\20\7 \2\2\20\22\7&\2\2\21\23\5\6\4")
        buf.write("\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2\2\24\25\7\'")
        buf.write("\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30\t\2\2\2\30\5\3\2")
        buf.write("\2\2\31\32\5\n\6\2\32\33\7%\2\2\33\7\3\2\2\2\34\35\5\n")
        buf.write("\6\2\35\t\3\2\2\2\36 \7\37\2\2\37!\5\b\5\2 \37\3\2\2\2")
        buf.write(" !\3\2\2\2!\"\3\2\2\2\"#\7 \2\2#\13\3\2\2\2\4\22 ")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'int'", "'void'", "<INVALID>", 
                     "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
                     "'Constructor'", "'Destructor'", "'New'", "'By'", "'('", 
                     "')'", "'['", "']'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INTTYPE", "VOIDTYPE", "WHITE_SPACE", 
                      "COMMENT", "BREAK", "CONTINUE", "IF", "ELSE_IF", "ELSE", 
                      "FOR_EACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", 
                      "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", 
                      "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                      "BY", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", 
                      "RIGHT_SQUARE_BRACKET", "DOT", "COMMA", "SEMICOLON", 
                      "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "ESCAPE", 
                      "INTEGER", "OCTAL_LITERALNESS", "HEXA_LITERALNESS", 
                      "BINARY_LITERALNESS", "FLOAT_LITERALNESS", "BOOLEAN_LITERALNESS", 
                      "STRING_LITERALNESS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4

    ruleNames =  [ "program", "mptype", "body", "exp", "funcall" ]

    EOF = Token.EOF
    T__0=1
    INTTYPE=2
    VOIDTYPE=3
    WHITE_SPACE=4
    COMMENT=5
    BREAK=6
    CONTINUE=7
    IF=8
    ELSE_IF=9
    ELSE=10
    FOR_EACH=11
    TRUE=12
    FALSE=13
    ARRAY=14
    IN=15
    INT=16
    FLOAT=17
    BOOLEAN=18
    STRING=19
    RETURN=20
    NULL=21
    CLASS=22
    VAL=23
    VAR=24
    CONSTRUCTOR=25
    DESTRUCTOR=26
    NEW=27
    BY=28
    LEFT_PAREN=29
    RIGHT_PAREN=30
    LEFT_SQUARE_BRACKET=31
    RIGHT_SQUARE_BRACKET=32
    DOT=33
    COMMA=34
    SEMICOLON=35
    LEFT_CURLY_BRACKET=36
    RIGHT_CURLY_BRACKET=37
    ESCAPE=38
    INTEGER=39
    OCTAL_LITERALNESS=40
    HEXA_LITERALNESS=41
    BINARY_LITERALNESS=42
    FLOAT_LITERALNESS=43
    BOOLEAN_LITERALNESS=44
    STRING_LITERALNESS=45
    ERROR_CHAR=46
    UNCLOSE_STRING=47
    ILLEGAL_ESCAPE=48

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

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(D96Parser.BodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.mptype()
            self.state = 11
            self.match(D96Parser.T__0)
            self.state = 12
            self.match(D96Parser.LEFT_PAREN)
            self.state = 13
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 14
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.LEFT_PAREN:
                self.state = 15
                self.body()


            self.state = 18
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
            self.state = 19
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(D96Parser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = D96Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if not(_la==D96Parser.INTTYPE or _la==D96Parser.VOIDTYPE):
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

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.funcall()
            self.state = 24
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.funcall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = D96Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(D96Parser.LEFT_PAREN)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.LEFT_PAREN:
                self.state = 29
                self.exp()


            self.state = 32
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





