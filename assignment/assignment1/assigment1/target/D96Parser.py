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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\2\7\2\20\n\2\f\2\16\2\23\13\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\6\4\34\n\4\r\4\16\4\35\3\4\5\4!\n\4\3\4\3\4\3")
        buf.write("\4\6\4&\n\4\r\4\16\4\'\3\4\5\4+\n\4\3\4\3\4\3\4\6\4\60")
        buf.write("\n\4\r\4\16\4\61\3\4\5\4\65\n\4\5\4\67\n\4\3\4\3\4\3\4")
        buf.write("\2\2\5\2\4\6\2\4\3\2\'-\3\2\5\6\2A\2\13\3\2\2\2\4\24\3")
        buf.write("\2\2\2\6\26\3\2\2\2\b\n\7&\2\2\t\b\3\2\2\2\n\r\3\2\2\2")
        buf.write("\13\t\3\2\2\2\13\f\3\2\2\2\f\21\3\2\2\2\r\13\3\2\2\2\16")
        buf.write("\20\t\2\2\2\17\16\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2")
        buf.write("\21\22\3\2\2\2\22\3\3\2\2\2\23\21\3\2\2\2\24\25\t\3\2")
        buf.write("\2\25\5\3\2\2\2\26\27\7\r\2\2\27\66\7\34\2\2\30!\7\'\2")
        buf.write("\2\31\32\7\'\2\2\32\34\7!\2\2\33\31\3\2\2\2\34\35\3\2")
        buf.write("\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2\37!\7\'")
        buf.write("\2\2 \30\3\2\2\2 \33\3\2\2\2!\67\3\2\2\2\"+\7(\2\2#$\7")
        buf.write("(\2\2$&\7!\2\2%#\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2")
        buf.write("\2\2()\3\2\2\2)+\7(\2\2*\"\3\2\2\2*%\3\2\2\2+\67\3\2\2")
        buf.write("\2,\65\7)\2\2-.\7)\2\2.\60\7!\2\2/-\3\2\2\2\60\61\3\2")
        buf.write("\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2\2\63\65\7)")
        buf.write("\2\2\64,\3\2\2\2\64/\3\2\2\2\65\67\3\2\2\2\66 \3\2\2\2")
        buf.write("\66*\3\2\2\2\66\64\3\2\2\2\678\3\2\2\289\7\35\2\29\7\3")
        buf.write("\2\2\2\13\13\21\35 \'*\61\64\66")
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
                      "LITERAL_BOOLEAN", "LITERAL_STRING" ]

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

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LiteralnessContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralness" ):
                return visitor.visitLiteralness(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFER(self):
            return self.getToken(D96Parser.IDENTIFER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_identifer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifer" ):
                return visitor.visitIdentifer(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_indexedArray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexedArray" ):
                return visitor.visitIndexedArray(self)
            else:
                return visitor.visitChildren(self)




    def indexedArray(self):

        localctx = D96Parser.IndexedArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_indexedArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(D96Parser.K_ARRAY)
            self.state = 21
            self.match(D96Parser.LEFT_PAREN)
            self.state = 52
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
            else:
                raise NoViableAltException(self)

            self.state = 54
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





