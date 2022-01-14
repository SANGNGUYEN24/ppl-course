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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\2\7\2\20\n\2\f\2\16\2\23\13\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\6\4\34\n\4\r\4\16\4\35\3\4\5\4!\n\4\3\4\3\4\3")
        buf.write("\4\6\4&\n\4\r\4\16\4\'\3\4\5\4+\n\4\3\4\3\4\3\4\6\4\60")
        buf.write("\n\4\r\4\16\4\61\3\4\5\4\65\n\4\3\4\3\4\3\4\6\4:\n\4\r")
        buf.write("\4\16\4;\3\4\5\4?\n\4\3\4\3\4\3\4\6\4D\n\4\r\4\16\4E\3")
        buf.write("\4\5\4I\n\4\3\4\3\4\3\4\6\4N\n\4\r\4\16\4O\3\4\5\4S\n")
        buf.write("\4\3\4\3\4\3\4\6\4X\n\4\r\4\16\4Y\3\4\5\4]\n\4\5\4_\n")
        buf.write("\4\3\4\3\4\3\4\2\2\5\2\4\6\2\4\3\2$*\3\2+,\2u\2\13\3\2")
        buf.write("\2\2\4\24\3\2\2\2\6\26\3\2\2\2\b\n\7#\2\2\t\b\3\2\2\2")
        buf.write("\n\r\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\21\3\2\2\2\r")
        buf.write("\13\3\2\2\2\16\20\t\2\2\2\17\16\3\2\2\2\20\23\3\2\2\2")
        buf.write("\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\21\3\2\2")
        buf.write("\2\24\25\t\3\2\2\25\5\3\2\2\2\26\27\7\n\2\2\27^\7\31\2")
        buf.write("\2\30!\7$\2\2\31\32\7$\2\2\32\34\7\36\2\2\33\31\3\2\2")
        buf.write("\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\37\3\2")
        buf.write("\2\2\37!\7$\2\2 \30\3\2\2\2 \33\3\2\2\2!_\3\2\2\2\"+\7")
        buf.write("%\2\2#$\7%\2\2$&\7\36\2\2%#\3\2\2\2&\'\3\2\2\2\'%\3\2")
        buf.write("\2\2\'(\3\2\2\2()\3\2\2\2)+\7%\2\2*\"\3\2\2\2*%\3\2\2")
        buf.write("\2+_\3\2\2\2,\65\7&\2\2-.\7&\2\2.\60\7\36\2\2/-\3\2\2")
        buf.write("\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2")
        buf.write("\2\63\65\7&\2\2\64,\3\2\2\2\64/\3\2\2\2\65_\3\2\2\2\66")
        buf.write("?\7\'\2\2\678\7\'\2\28:\7\36\2\29\67\3\2\2\2:;\3\2\2\2")
        buf.write(";9\3\2\2\2;<\3\2\2\2<=\3\2\2\2=?\7\'\2\2>\66\3\2\2\2>")
        buf.write("9\3\2\2\2?_\3\2\2\2@I\7(\2\2AB\7(\2\2BD\7\36\2\2CA\3\2")
        buf.write("\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2GI\7(\2\2")
        buf.write("H@\3\2\2\2HC\3\2\2\2I_\3\2\2\2JS\7)\2\2KL\7)\2\2LN\7\36")
        buf.write("\2\2MK\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2PQ\3\2\2\2")
        buf.write("QS\7)\2\2RJ\3\2\2\2RM\3\2\2\2S_\3\2\2\2T]\7*\2\2UV\7*")
        buf.write("\2\2VX\7\36\2\2WU\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2")
        buf.write("\2Z[\3\2\2\2[]\7*\2\2\\T\3\2\2\2\\W\3\2\2\2]_\3\2\2\2")
        buf.write("^ \3\2\2\2^*\3\2\2\2^\64\3\2\2\2^>\3\2\2\2^H\3\2\2\2^")
        buf.write("R\3\2\2\2^\\\3\2\2\2_`\3\2\2\2`a\7\32\2\2a\7\3\2\2\2\23")
        buf.write("\13\21\35 \'*\61\64;>EHORY\\^")
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
                     "'Constructor'", "'Destructor'", "'New'", "'By'", "'('", 
                     "')'", "'['", "']'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", 
                      "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", 
                      "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", "K_RETURN", 
                      "K_NULL", "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", 
                      "K_DESTRUCTOR", "K_NEW", "K_BY", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "DOT", 
                      "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                      "ESCAPE", "SIGN", "LITERAL_INTEGER", "LITERAL_OCTAL", 
                      "LITERAL_HEXA", "LITERAL_BINARY", "LITERAL_FLOAT", 
                      "LITERAL_BOOLEAN", "LITERAL_STRING", "IDENTIFER", 
                      "DOLAR_IDENTIFIER", "WHITE_SPACE" ]

    RULE_literalness = 0
    RULE_identifer = 1
    RULE_indexedArray = 2

    ruleNames =  [ "literalness", "identifer", "indexedArray" ]

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
    LEFT_PAREN=23
    RIGHT_PAREN=24
    LEFT_SQUARE_BRACKET=25
    RIGHT_SQUARE_BRACKET=26
    DOT=27
    COMMA=28
    SEMICOLON=29
    LEFT_CURLY_BRACKET=30
    RIGHT_CURLY_BRACKET=31
    ESCAPE=32
    SIGN=33
    LITERAL_INTEGER=34
    LITERAL_OCTAL=35
    LITERAL_HEXA=36
    LITERAL_BINARY=37
    LITERAL_FLOAT=38
    LITERAL_BOOLEAN=39
    LITERAL_STRING=40
    IDENTIFER=41
    DOLAR_IDENTIFIER=42
    WHITE_SPACE=43

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

        def K_ARRAY(self):
            return self.getToken(D96Parser.K_ARRAY, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def LITERAL_INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LITERAL_INTEGER)
            else:
                return self.getToken(D96Parser.LITERAL_INTEGER, i)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(D96Parser.K_ARRAY)
            self.state = 21
            self.match(D96Parser.LEFT_PAREN)
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LITERAL_INTEGER]:
                self.state = 30
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 22
                    self.match(D96Parser.LITERAL_INTEGER)
                    pass

                elif la_ == 2:
                    self.state = 25 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 23
                            self.match(D96Parser.LITERAL_INTEGER)
                            self.state = 24
                            self.match(D96Parser.COMMA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 27 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    self.state = 29
                    self.match(D96Parser.LITERAL_INTEGER)
                    pass


                pass
            elif token in [D96Parser.LITERAL_OCTAL]:
                self.state = 40
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 32
                    self.match(D96Parser.LITERAL_OCTAL)
                    pass

                elif la_ == 2:
                    self.state = 35 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 33
                            self.match(D96Parser.LITERAL_OCTAL)
                            self.state = 34
                            self.match(D96Parser.COMMA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 37 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                    self.state = 39
                    self.match(D96Parser.LITERAL_OCTAL)
                    pass


                pass
            elif token in [D96Parser.LITERAL_HEXA]:
                self.state = 50
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 42
                    self.match(D96Parser.LITERAL_HEXA)
                    pass

                elif la_ == 2:
                    self.state = 45 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 43
                            self.match(D96Parser.LITERAL_HEXA)
                            self.state = 44
                            self.match(D96Parser.COMMA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 47 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                    self.state = 49
                    self.match(D96Parser.LITERAL_HEXA)
                    pass


                pass
            elif token in [D96Parser.LITERAL_BINARY]:
                self.state = 60
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 52
                    self.match(D96Parser.LITERAL_BINARY)
                    pass

                elif la_ == 2:
                    self.state = 55 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 53
                            self.match(D96Parser.LITERAL_BINARY)
                            self.state = 54
                            self.match(D96Parser.COMMA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 57 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                    self.state = 59
                    self.match(D96Parser.LITERAL_BINARY)
                    pass


                pass
            elif token in [D96Parser.LITERAL_FLOAT]:
                self.state = 70
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 62
                    self.match(D96Parser.LITERAL_FLOAT)
                    pass

                elif la_ == 2:
                    self.state = 65 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 63
                            self.match(D96Parser.LITERAL_FLOAT)
                            self.state = 64
                            self.match(D96Parser.COMMA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 67 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                    self.state = 69
                    self.match(D96Parser.LITERAL_FLOAT)
                    pass


                pass
            elif token in [D96Parser.LITERAL_BOOLEAN]:
                self.state = 80
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 72
                    self.match(D96Parser.LITERAL_BOOLEAN)
                    pass

                elif la_ == 2:
                    self.state = 75 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 73
                            self.match(D96Parser.LITERAL_BOOLEAN)
                            self.state = 74
                            self.match(D96Parser.COMMA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 77 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                    self.state = 79
                    self.match(D96Parser.LITERAL_BOOLEAN)
                    pass


                pass
            elif token in [D96Parser.LITERAL_STRING]:
                self.state = 90
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 82
                    self.match(D96Parser.LITERAL_STRING)
                    pass

                elif la_ == 2:
                    self.state = 85 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 83
                            self.match(D96Parser.LITERAL_STRING)
                            self.state = 84
                            self.match(D96Parser.COMMA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 87 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                    self.state = 89
                    self.match(D96Parser.LITERAL_STRING)
                    pass


                pass
            else:
                raise NoViableAltException(self)

            self.state = 94
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





