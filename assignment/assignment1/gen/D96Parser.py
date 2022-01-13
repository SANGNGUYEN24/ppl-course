# Generated from D:/Study2/HCMUT/semester212/PPL/code/assignment/assignment1/assigment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3/")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\3\3\2)/\2\5\2\4\3\2\2")
        buf.write("\2\4\5\t\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
                     "'False'", "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "WHITE_SPACE", "COMMENT", "BREAK", "CONTINUE", "IF", 
                      "ELSE_IF", "ELSE", "FOR_EACH", "TRUE", "FALSE", "ARRAY", 
                      "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", 
                      "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", 
                      "RIGHT_SQUARE_BRACKET", "DOT", "COMMA", "SEMICOLON", 
                      "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "ESCAPE", 
                      "INTEGER", "OCTAL_LITERALNESS", "HEXA_LITERALNESS", 
                      "BINARY_LITERALNESS", "FLOAT_LITERALNESS", "BOOLEAN_LITERALNESS", 
                      "STRING_LITERALNESS" ]

    RULE_testType = 0

    ruleNames =  [ "testType" ]

    EOF = Token.EOF
    ERROR_CHAR=1
    UNCLOSE_STRING=2
    ILLEGAL_ESCAPE=3
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

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TestTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(D96Parser.INTEGER, 0)

        def FLOAT_LITERALNESS(self):
            return self.getToken(D96Parser.FLOAT_LITERALNESS, 0)

        def OCTAL_LITERALNESS(self):
            return self.getToken(D96Parser.OCTAL_LITERALNESS, 0)

        def HEXA_LITERALNESS(self):
            return self.getToken(D96Parser.HEXA_LITERALNESS, 0)

        def BINARY_LITERALNESS(self):
            return self.getToken(D96Parser.BINARY_LITERALNESS, 0)

        def BOOLEAN_LITERALNESS(self):
            return self.getToken(D96Parser.BOOLEAN_LITERALNESS, 0)

        def STRING_LITERALNESS(self):
            return self.getToken(D96Parser.STRING_LITERALNESS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_testType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTestType" ):
                listener.enterTestType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTestType" ):
                listener.exitTestType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTestType" ):
                return visitor.visitTestType(self)
            else:
                return visitor.visitChildren(self)




    def testType(self):

        localctx = D96Parser.TestTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_testType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTEGER) | (1 << D96Parser.OCTAL_LITERALNESS) | (1 << D96Parser.HEXA_LITERALNESS) | (1 << D96Parser.BINARY_LITERALNESS) | (1 << D96Parser.FLOAT_LITERALNESS) | (1 << D96Parser.BOOLEAN_LITERALNESS) | (1 << D96Parser.STRING_LITERALNESS))) != 0)):
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





