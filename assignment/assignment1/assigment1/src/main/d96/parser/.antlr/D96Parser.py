# Generated from d:\Study2\HCMUT\semester212\PPL\code\assignment\assignment1\assigment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\26\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\7\2\13\n\2\f\2\16")
        buf.write("\2\16\13\2\3\2\3\2\3\3\3\3\5\3\24\n\3\3\3\2\2\4\2\4\2")
        buf.write("\2\2\25\2\6\3\2\2\2\4\23\3\2\2\2\6\7\7$\2\2\7\f\5\4\3")
        buf.write("\2\b\t\7\"\2\2\t\13\5\4\3\2\n\b\3\2\2\2\13\16\3\2\2\2")
        buf.write("\f\n\3\2\2\2\f\r\3\2\2\2\r\17\3\2\2\2\16\f\3\2\2\2\17")
        buf.write("\20\7%\2\2\20\3\3\2\2\2\21\24\5\2\2\2\22\24\7\3\2\2\23")
        buf.write("\21\3\2\2\2\23\22\3\2\2\2\24\5\3\2\2\2\4\f\23")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
                     "'Foreach'", "'True'", "'False'", "'Array'", "'In'", 
                     "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", 
                     "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
                     "'Destructor'", "'New'", "'By'", "'('", "')'", "'['", 
                     "']'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "TEST", "WHITE_SPACE", "COMMENT", "BREAK", 
                      "CONTINUE", "IF", "ELSE_IF", "ELSE", "FOR_EACH", "TRUE", 
                      "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
                      "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", 
                      "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "LEFT_PAREN", 
                      "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                      "DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", 
                      "RIGHT_CURLY_BRACKET", "ESCAPE", "INTEGER", "OCTAL_LITERALNESS", 
                      "HEXA_LITERALNESS", "BINARY_LITERALNESS", "FLOAT_LITERALNESS", 
                      "BOOLEAN_LITERALNESS", "STRING_LITERALNESS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_init = 0
    RULE_value = 1

    ruleNames =  [ "init", "value" ]

    EOF = Token.EOF
    TEST=1
    WHITE_SPACE=2
    COMMENT=3
    BREAK=4
    CONTINUE=5
    IF=6
    ELSE_IF=7
    ELSE=8
    FOR_EACH=9
    TRUE=10
    FALSE=11
    ARRAY=12
    IN=13
    INT=14
    FLOAT=15
    BOOLEAN=16
    STRING=17
    RETURN=18
    NULL=19
    CLASS=20
    VAL=21
    VAR=22
    CONSTRUCTOR=23
    DESTRUCTOR=24
    NEW=25
    BY=26
    LEFT_PAREN=27
    RIGHT_PAREN=28
    LEFT_SQUARE_BRACKET=29
    RIGHT_SQUARE_BRACKET=30
    DOT=31
    COMMA=32
    SEMICOLON=33
    LEFT_CURLY_BRACKET=34
    RIGHT_CURLY_BRACKET=35
    ESCAPE=36
    INTEGER=37
    OCTAL_LITERALNESS=38
    HEXA_LITERALNESS=39
    BINARY_LITERALNESS=40
    FLOAT_LITERALNESS=41
    BOOLEAN_LITERALNESS=42
    STRING_LITERALNESS=43
    ERROR_CHAR=44
    UNCLOSE_STRING=45
    ILLEGAL_ESCAPE=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ValueContext)
            else:
                return self.getTypedRuleContext(D96Parser.ValueContext,i)


        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_init




    def init(self):

        localctx = D96Parser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 5
            self.value()
            self.state = 10
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 6
                self.match(D96Parser.COMMA)
                self.state = 7
                self.value()
                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 13
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init(self):
            return self.getTypedRuleContext(D96Parser.InitContext,0)


        def TEST(self):
            return self.getToken(D96Parser.TEST, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_value




    def value(self):

        localctx = D96Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_value)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LEFT_CURLY_BRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.init()
                pass
            elif token in [D96Parser.TEST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(D96Parser.TEST)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





