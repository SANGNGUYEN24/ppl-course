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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3.")
        buf.write("\31\4\2\t\2\4\3\t\3\4\4\t\4\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\2\7\2\20\n\2\f\2\16\2\23\13\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\2\2\5\2\4\6\2\4\3\2\'-\3\2\5\6\2\27\2\13\3\2\2\2\4\24")
        buf.write("\3\2\2\2\6\26\3\2\2\2\b\n\7&\2\2\t\b\3\2\2\2\n\r\3\2\2")
        buf.write("\2\13\t\3\2\2\2\13\f\3\2\2\2\f\21\3\2\2\2\r\13\3\2\2\2")
        buf.write("\16\20\t\2\2\2\17\16\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2")
        buf.write("\2\21\22\3\2\2\2\22\3\3\2\2\2\23\21\3\2\2\2\24\25\t\3")
        buf.write("\2\2\25\5\3\2\2\2\26\27\7.\2\2\27\7\3\2\2\2\4\13\21")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'Array'", "'In'", "'Int'", 
                     "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", 
                     "'Class'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "'('", "')'", "'['", "']'", "'.'", 
                     "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "WHITE_SPACE", "COMMENT", "IDENTIFER", 
                      "DOLAR_IDENTIFIER", "K_BREAK", "K_CONTINUE", "K_IF", 
                      "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", 
                      "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", "K_RETURN", 
                      "K_NULL", "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", 
                      "K_DESTRUCTOR", "K_NEW", "K_BY", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "DOT", 
                      "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                      "ESCAPE", "SIGN", "LITERAL_INTEGER", "LITERAL_OCTAL", 
                      "LITERAL_HEXA", "LITERAL_BINARY", "LITERAL_FLOAT", 
                      "LITERAL_BOOLEAN", "LITERAL_STRING", "INDEXED_ARRAY" ]

    RULE_literalness = 0
    RULE_identifer = 1
    RULE_indexedArray = 2

    ruleNames =  [ "literalness", "identifer", "indexedArray" ]

    EOF = Token.EOF
    WHITE_SPACE=1
    COMMENT=2
    IDENTIFER=3
    DOLAR_IDENTIFIER=4
    K_BREAK=5
    K_CONTINUE=6
    K_IF=7
    K_ELSE_IF=8
    K_ELSE=9
    K_FOR_EACH=10
    K_ARRAY=11
    K_IN=12
    K_INT=13
    K_FLOAT=14
    K_BOOLEAN=15
    K_STRING=16
    K_RETURN=17
    K_NULL=18
    K_CLASS=19
    K_VAL=20
    K_VAR=21
    K_CONSTRUCTOR=22
    K_DESTRUCTOR=23
    K_NEW=24
    K_BY=25
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
    SIGN=36
    LITERAL_INTEGER=37
    LITERAL_OCTAL=38
    LITERAL_HEXA=39
    LITERAL_BINARY=40
    LITERAL_FLOAT=41
    LITERAL_BOOLEAN=42
    LITERAL_STRING=43
    INDEXED_ARRAY=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LiteralnessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIGN(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SIGN)
            else:
                return self.getToken(D96Parser.SIGN, i)

        def LITERAL_INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LITERAL_INTEGER)
            else:
                return self.getToken(D96Parser.LITERAL_INTEGER, i)

        def LITERAL_FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LITERAL_FLOAT)
            else:
                return self.getToken(D96Parser.LITERAL_FLOAT, i)

        def LITERAL_OCTAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LITERAL_OCTAL)
            else:
                return self.getToken(D96Parser.LITERAL_OCTAL, i)

        def LITERAL_HEXA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LITERAL_HEXA)
            else:
                return self.getToken(D96Parser.LITERAL_HEXA, i)

        def LITERAL_BINARY(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LITERAL_BINARY)
            else:
                return self.getToken(D96Parser.LITERAL_BINARY, i)

        def LITERAL_BOOLEAN(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LITERAL_BOOLEAN)
            else:
                return self.getToken(D96Parser.LITERAL_BOOLEAN, i)

        def LITERAL_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LITERAL_STRING)
            else:
                return self.getToken(D96Parser.LITERAL_STRING, i)

        def getRuleIndex(self):
            return D96Parser.RULE_literalness




    def literalness(self):

        localctx = D96Parser.LiteralnessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_literalness)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SIGN:
                self.state = 6
                self.match(D96Parser.SIGN)
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INTEGER) | (1 << D96Parser.LITERAL_OCTAL) | (1 << D96Parser.LITERAL_HEXA) | (1 << D96Parser.LITERAL_BINARY) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_STRING))) != 0):
                self.state = 12
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INTEGER) | (1 << D96Parser.LITERAL_OCTAL) | (1 << D96Parser.LITERAL_HEXA) | (1 << D96Parser.LITERAL_BINARY) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_STRING))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentiferContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFER(self):
            return self.getToken(D96Parser.IDENTIFER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_identifer




    def identifer(self):

        localctx = D96Parser.IdentiferContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_identifer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            _la = self._input.LA(1)
            if not(_la==D96Parser.IDENTIFER or _la==D96Parser.DOLAR_IDENTIFIER):
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


    class IndexedArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDEXED_ARRAY(self):
            return self.getToken(D96Parser.INDEXED_ARRAY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_indexedArray




    def indexedArray(self):

        localctx = D96Parser.IndexedArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_indexedArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(D96Parser.INDEXED_ARRAY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





