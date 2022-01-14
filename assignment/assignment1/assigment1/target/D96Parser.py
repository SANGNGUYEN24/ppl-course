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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
                     "'Constructor'", "'New'", "'By'", "'Self'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'>'", "'>='", "'<'", "'<='", 
                     "'==.'", "'+.'", "'.'", "<INVALID>", "<INVALID>", "'('", 
                     "')'", "'{'", "'}'", "';'", "'['", "']'", "','", "':'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\"'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", 
                      "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                      "CLASS", "VAL", "VAR", "CONSTRUCTOR", "NEW", "BY", 
                      "SELF", "PLUS", "MINUS", "MULTI", "DIVIDE", "REMAIN", 
                      "NEGATION", "AND", "OR", "EQUIV", "ASSIGN", "DIFFER", 
                      "GREATER", "EQUALGREATER", "SMALLER", "EQUALLSMALLER", 
                      "EQUIVFLOAT", "PLUSFLOAT", "DOT", "STATICACESS", "INTLIT", 
                      "LB", "RB", "LP", "RP", "SEMI", "LSB", "RSB", "COMMA", 
                      "COLON", "WS", "CMT", "ID", "DOID", "INTEGER", "FLOATT", 
                      "BOOL", "STRINGG", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSEIF=4
    ELSE=5
    FOREACH=6
    TRUE=7
    FALSE=8
    ARRAY=9
    IN=10
    INT=11
    FLOAT=12
    BOOLEAN=13
    STRING=14
    RETURN=15
    NULL=16
    CLASS=17
    VAL=18
    VAR=19
    CONSTRUCTOR=20
    NEW=21
    BY=22
    SELF=23
    PLUS=24
    MINUS=25
    MULTI=26
    DIVIDE=27
    REMAIN=28
    NEGATION=29
    AND=30
    OR=31
    EQUIV=32
    ASSIGN=33
    DIFFER=34
    GREATER=35
    EQUALGREATER=36
    SMALLER=37
    EQUALLSMALLER=38
    EQUIVFLOAT=39
    PLUSFLOAT=40
    DOT=41
    STATICACESS=42
    INTLIT=43
    LB=44
    RB=45
    LP=46
    RP=47
    SEMI=48
    LSB=49
    RSB=50
    COMMA=51
    COLON=52
    WS=53
    CMT=54
    ID=55
    DOID=56
    INTEGER=57
    FLOATT=58
    BOOL=59
    STRINGG=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63

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

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

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





