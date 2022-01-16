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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("Y\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\7\2\16\n")
        buf.write("\2\f\2\16\2\21\13\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\7\4 \n\4\f\4\16\4#\13\4\5\4")
        buf.write("%\n\4\3\4\3\4\3\4\7\4*\n\4\f\4\16\4-\13\4\3\4\3\4\3\4")
        buf.write("\7\4\62\n\4\f\4\16\4\65\13\4\3\4\3\4\3\4\7\4:\n\4\f\4")
        buf.write("\16\4=\13\4\5\4?\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\6")
        buf.write("\5I\n\5\r\5\16\5J\3\5\3\5\5\5O\n\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\5\6W\n\6\3\6\2\2\7\2\4\6\b\n\2\4\3\2\64\67\3\289")
        buf.write("\2b\2\17\3\2\2\2\4\30\3\2\2\2\6\32\3\2\2\2\bB\3\2\2\2")
        buf.write("\nV\3\2\2\2\f\16\7\63\2\2\r\f\3\2\2\2\16\21\3\2\2\2\17")
        buf.write("\r\3\2\2\2\17\20\3\2\2\2\20\25\3\2\2\2\21\17\3\2\2\2\22")
        buf.write("\24\t\2\2\2\23\22\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2")
        buf.write("\25\26\3\2\2\2\26\3\3\2\2\2\27\25\3\2\2\2\30\31\t\3\2")
        buf.write("\2\31\5\3\2\2\2\32\33\7\n\2\2\33>\7)\2\2\34!\7\64\2\2")
        buf.write("\35\36\7.\2\2\36 \7\64\2\2\37\35\3\2\2\2 #\3\2\2\2!\37")
        buf.write("\3\2\2\2!\"\3\2\2\2\"%\3\2\2\2#!\3\2\2\2$\34\3\2\2\2$")
        buf.write("%\3\2\2\2%?\3\2\2\2&+\7\65\2\2\'(\7.\2\2(*\7\65\2\2)\'")
        buf.write("\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,?\3\2\2\2-+\3\2")
        buf.write("\2\2.\63\7\66\2\2/\60\7.\2\2\60\62\7\66\2\2\61/\3\2\2")
        buf.write("\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64?\3\2\2")
        buf.write("\2\65\63\3\2\2\2\66;\7\67\2\2\678\7.\2\28:\7\67\2\29\67")
        buf.write("\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<?\3\2\2\2=;\3\2")
        buf.write("\2\2>$\3\2\2\2>&\3\2\2\2>.\3\2\2\2>\66\3\2\2\2?@\3\2\2")
        buf.write("\2@A\7*\2\2A\7\3\2\2\2BC\7\n\2\2CN\7)\2\2DO\5\6\4\2EF")
        buf.write("\5\6\4\2FG\7.\2\2GI\3\2\2\2HE\3\2\2\2IJ\3\2\2\2JH\3\2")
        buf.write("\2\2JK\3\2\2\2KL\3\2\2\2LM\5\6\4\2MO\3\2\2\2ND\3\2\2\2")
        buf.write("NH\3\2\2\2OP\3\2\2\2PQ\7*\2\2Q\t\3\2\2\2RW\5\2\2\2SW\5")
        buf.write("\4\3\2TW\5\6\4\2UW\5\b\5\2VR\3\2\2\2VS\3\2\2\2VT\3\2\2")
        buf.write("\2VU\3\2\2\2W\13\3\2\2\2\r\17\25!$+\63;>JNV")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
                     "'Constructor'", "'Destructor'", "'New'", "'By'", "'!'", 
                     "'||'", "'&&'", "'=='", "'!='", "'%'", "'+'", "'-'", 
                     "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", "'+.'", 
                     "'==.'", "'('", "')'", "'['", "']'", "'.'", "','", 
                     "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", 
                      "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", 
                      "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", "K_RETURN", 
                      "K_NULL", "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", 
                      "K_DESTRUCTOR", "K_NEW", "K_BY", "OP_LOGICAL_NOT", 
                      "OP_LOGICAL_OR", "OP_LOGICAL_AND", "OP_IS_EQUAL_TO", 
                      "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", "OP_SUBTRACTION", 
                      "OP_MULTIPLICATION", "OP_DIVISION", "OP_LESS_THAN", 
                      "OP_LESS_THAN_EQUAL", "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", 
                      "OP_STRING_CONCATENATION", "OP_TWO_SAME_STRING", "LEFT_PAREN", 
                      "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                      "DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", 
                      "RIGHT_CURLY_BRACKET", "ESCAPE", "SIGN", "LITERAL_INTEGER", 
                      "LITERAL_FLOAT", "LITERAL_BOOLEAN", "LITERAL_STRING", 
                      "IDENTIFER", "DOLAR_IDENTIFIER", "WHITE_SPACE" ]

    RULE_literal = 0
    RULE_identifer = 1
    RULE_indexedArray = 2
    RULE_multiDimentionalArray = 3
    RULE_allTest = 4

    ruleNames =  [ "literal", "identifer", "indexedArray", "multiDimentionalArray", 
                   "allTest" ]

    EOF = Token.EOF
    COMMENT=1
    K_BREAK=2
    K_CONTINUE=3
    K_IF=4
    K_ELSE_IF=5
    K_ELSE=6
    K_FOR_EACH=7
    K_ARRAY=8
    K_IN=9
    K_INT=10
    K_FLOAT=11
    K_BOOLEAN=12
    K_STRING=13
    K_RETURN=14
    K_NULL=15
    K_CLASS=16
    K_VAL=17
    K_VAR=18
    K_CONSTRUCTOR=19
    K_DESTRUCTOR=20
    K_NEW=21
    K_BY=22
    OP_LOGICAL_NOT=23
    OP_LOGICAL_OR=24
    OP_LOGICAL_AND=25
    OP_IS_EQUAL_TO=26
    OP_NOT_EQUAL_TO=27
    OP_MODULO=28
    OP_ADDTION=29
    OP_SUBTRACTION=30
    OP_MULTIPLICATION=31
    OP_DIVISION=32
    OP_LESS_THAN=33
    OP_LESS_THAN_EQUAL=34
    OP_GREATER_THAN=35
    OP_GREATER_THAN_EQUAL=36
    OP_STRING_CONCATENATION=37
    OP_TWO_SAME_STRING=38
    LEFT_PAREN=39
    RIGHT_PAREN=40
    LEFT_SQUARE_BRACKET=41
    RIGHT_SQUARE_BRACKET=42
    DOT=43
    COMMA=44
    SEMICOLON=45
    LEFT_CURLY_BRACKET=46
    RIGHT_CURLY_BRACKET=47
    ESCAPE=48
    SIGN=49
    LITERAL_INTEGER=50
    LITERAL_FLOAT=51
    LITERAL_BOOLEAN=52
    LITERAL_STRING=53
    IDENTIFER=54
    DOLAR_IDENTIFIER=55
    WHITE_SPACE=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LiteralContext(ParserRuleContext):

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
            return D96Parser.RULE_literal




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SIGN:
                self.state = 10
                self.match(D96Parser.SIGN)
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INTEGER) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_STRING))) != 0):
                self.state = 16
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LITERAL_INTEGER) | (1 << D96Parser.LITERAL_FLOAT) | (1 << D96Parser.LITERAL_BOOLEAN) | (1 << D96Parser.LITERAL_STRING))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 21
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
            self.state = 22
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

        def K_ARRAY(self):
            return self.getToken(D96Parser.K_ARRAY, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def LITERAL_FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LITERAL_FLOAT)
            else:
                return self.getToken(D96Parser.LITERAL_FLOAT, i)

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

        def LITERAL_INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LITERAL_INTEGER)
            else:
                return self.getToken(D96Parser.LITERAL_INTEGER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_indexedArray




    def indexedArray(self):

        localctx = D96Parser.IndexedArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_indexedArray)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(D96Parser.K_ARRAY)
            self.state = 25
            self.match(D96Parser.LEFT_PAREN)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RIGHT_PAREN, D96Parser.LITERAL_INTEGER]:
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.LITERAL_INTEGER:
                    self.state = 26
                    self.match(D96Parser.LITERAL_INTEGER)
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.COMMA:
                        self.state = 27
                        self.match(D96Parser.COMMA)
                        self.state = 28
                        self.match(D96Parser.LITERAL_INTEGER)
                        self.state = 33
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                pass
            elif token in [D96Parser.LITERAL_FLOAT]:
                self.state = 36
                self.match(D96Parser.LITERAL_FLOAT)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 37
                    self.match(D96Parser.COMMA)
                    self.state = 38
                    self.match(D96Parser.LITERAL_FLOAT)
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.LITERAL_BOOLEAN]:
                self.state = 44
                self.match(D96Parser.LITERAL_BOOLEAN)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 45
                    self.match(D96Parser.COMMA)
                    self.state = 46
                    self.match(D96Parser.LITERAL_BOOLEAN)
                    self.state = 51
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.LITERAL_STRING]:
                self.state = 52
                self.match(D96Parser.LITERAL_STRING)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 53
                    self.match(D96Parser.COMMA)
                    self.state = 54
                    self.match(D96Parser.LITERAL_STRING)
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 62
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiDimentionalArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ARRAY(self):
            return self.getToken(D96Parser.K_ARRAY, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def indexedArray(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IndexedArrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.IndexedArrayContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_multiDimentionalArray




    def multiDimentionalArray(self):

        localctx = D96Parser.MultiDimentionalArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_multiDimentionalArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(D96Parser.K_ARRAY)
            self.state = 65
            self.match(D96Parser.LEFT_PAREN)
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 66
                self.indexedArray()
                pass

            elif la_ == 2:
                self.state = 70 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 67
                        self.indexedArray()
                        self.state = 68
                        self.match(D96Parser.COMMA)

                    else:
                        raise NoViableAltException(self)
                    self.state = 72 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 74
                self.indexedArray()
                pass


            self.state = 78
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AllTestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def identifer(self):
            return self.getTypedRuleContext(D96Parser.IdentiferContext,0)


        def indexedArray(self):
            return self.getTypedRuleContext(D96Parser.IndexedArrayContext,0)


        def multiDimentionalArray(self):
            return self.getTypedRuleContext(D96Parser.MultiDimentionalArrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_allTest




    def allTest(self):

        localctx = D96Parser.AllTestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_allTest)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.identifer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.indexedArray()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.multiDimentionalArray()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





