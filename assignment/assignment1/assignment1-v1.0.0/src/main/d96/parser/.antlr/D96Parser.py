# Generated from d:\Study2\HCMUT\semester212\PPL\code\assignment\assignment1\assignment1-v1.0.0\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
                     "'False'", "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENT", "BREAK", "CONTINUE", 
                      "IF", "ELSE_IF", "ELSE", "FOR_EACH", "TRUE", "FALSE", 
                      "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
                      "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "DOT", 
                      "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                      "ESCAPE", "INTEGER", "OCTAL_LITERALNESS", "HEXA_LITERALNESS", 
                      "BINARY_LITERALNESS", "FLOAT_LITERALNESS", "BOOLEAN_LITERALNESS", 
                      "STRING_LITERALNESS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    WS=1
    COMMENT=2
    BREAK=3
    CONTINUE=4
    IF=5
    ELSE_IF=6
    ELSE=7
    FOR_EACH=8
    TRUE=9
    FALSE=10
    ARRAY=11
    IN=12
    INT=13
    FLOAT=14
    BOOLEAN=15
    STRING=16
    RETURN=17
    NULL=18
    CLASS=19
    VAL=20
    VAR=21
    CONSTRUCTOR=22
    DESTRUCTOR=23
    NEW=24
    BY=25
    LEFT_PAREN=26
    RIGHT_PAREN=27
    LEFT_SQUARE_BRACKET=28
    RIGHT_SQUARE_BRACKET=29
    DOT=30
    COMMA=31
    SEMICOLON=32
    LEFT_CURLY_BRACKET=33
    RIGHT_CURLY_BRACKET=34
    ESCAPE=35
    INTEGER=36
    OCTAL_LITERALNESS=37
    HEXA_LITERALNESS=38
    BINARY_LITERALNESS=39
    FLOAT_LITERALNESS=40
    BOOLEAN_LITERALNESS=41
    STRING_LITERALNESS=42
    ERROR_CHAR=43
    UNCLOSE_STRING=44
    ILLEGAL_ESCAPE=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





