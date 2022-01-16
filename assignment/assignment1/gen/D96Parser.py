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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\7\2\16\n")
        buf.write("\2\f\2\16\2\21\13\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\6\4 \n\4\r\4\16\4!\3\4\5\4")
        buf.write("%\n\4\3\4\3\4\3\4\6\4*\n\4\r\4\16\4+\3\4\5\4/\n\4\3\4")
        buf.write("\3\4\3\4\6\4\64\n\4\r\4\16\4\65\3\4\5\49\n\4\3\4\3\4\3")
        buf.write("\4\6\4>\n\4\r\4\16\4?\3\4\5\4C\n\4\5\4E\n\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\6\5O\n\5\r\5\16\5P\3\5\3\5\5\5")
        buf.write("U\n\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6]\n\6\3\6\2\2\7\2\4\6")
        buf.write("\b\n\2\4\3\2$\'\3\2()\2k\2\17\3\2\2\2\4\30\3\2\2\2\6\32")
        buf.write("\3\2\2\2\bH\3\2\2\2\n\\\3\2\2\2\f\16\7#\2\2\r\f\3\2\2")
        buf.write("\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\25\3\2")
        buf.write("\2\2\21\17\3\2\2\2\22\24\t\2\2\2\23\22\3\2\2\2\24\27\3")
        buf.write("\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\3\3\2\2\2\27\25")
        buf.write("\3\2\2\2\30\31\t\3\2\2\31\5\3\2\2\2\32\33\7\n\2\2\33D")
        buf.write("\7\31\2\2\34%\7$\2\2\35\36\7$\2\2\36 \7\36\2\2\37\35\3")
        buf.write("\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#%\7")
        buf.write("$\2\2$\34\3\2\2\2$\37\3\2\2\2%E\3\2\2\2&/\7%\2\2\'(\7")
        buf.write("%\2\2(*\7\36\2\2)\'\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2")
        buf.write("\2\2,-\3\2\2\2-/\7%\2\2.&\3\2\2\2.)\3\2\2\2/E\3\2\2\2")
        buf.write("\609\7&\2\2\61\62\7&\2\2\62\64\7\36\2\2\63\61\3\2\2\2")
        buf.write("\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2")
        buf.write("\2\679\7&\2\28\60\3\2\2\28\63\3\2\2\29E\3\2\2\2:C\7\'")
        buf.write("\2\2;<\7\'\2\2<>\7\36\2\2=;\3\2\2\2>?\3\2\2\2?=\3\2\2")
        buf.write("\2?@\3\2\2\2@A\3\2\2\2AC\7\'\2\2B:\3\2\2\2B=\3\2\2\2C")
        buf.write("E\3\2\2\2D$\3\2\2\2D.\3\2\2\2D8\3\2\2\2DB\3\2\2\2EF\3")
        buf.write("\2\2\2FG\7\32\2\2G\7\3\2\2\2HI\7\n\2\2IT\7\31\2\2JU\5")
        buf.write("\6\4\2KL\5\6\4\2LM\7\36\2\2MO\3\2\2\2NK\3\2\2\2OP\3\2")
        buf.write("\2\2PN\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RS\5\6\4\2SU\3\2\2\2")
        buf.write("TJ\3\2\2\2TN\3\2\2\2UV\3\2\2\2VW\7\32\2\2W\t\3\2\2\2X")
        buf.write("]\5\2\2\2Y]\5\4\3\2Z]\5\6\4\2[]\5\b\5\2\\X\3\2\2\2\\Y")
        buf.write("\3\2\2\2\\Z\3\2\2\2\\[\3\2\2\2]\13\3\2\2\2\20\17\25!$")
        buf.write("+.\658?BDPT\\")
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
                      "ESCAPE", "SIGN", "LITERAL_INTEGER", "LITERAL_FLOAT", 
                      "LITERAL_BOOLEAN", "LITERAL_STRING", "IDENTIFER", 
                      "DOLAR_IDENTIFIER", "WHITE_SPACE" ]

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
    LITERAL_FLOAT=35
    LITERAL_BOOLEAN=36
    LITERAL_STRING=37
    IDENTIFER=38
    DOLAR_IDENTIFIER=39
    WHITE_SPACE=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LiteralContext(ParserRuleContext):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifer" ):
                listener.enterIdentifer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifer" ):
                listener.exitIdentifer(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexedArray" ):
                listener.enterIndexedArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexedArray" ):
                listener.exitIndexedArray(self)

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
            self.state = 24
            self.match(D96Parser.K_ARRAY)
            self.state = 25
            self.match(D96Parser.LEFT_PAREN)
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LITERAL_INTEGER]:
                self.state = 34
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 26
                    self.match(D96Parser.LITERAL_INTEGER)
                    pass

                elif la_ == 2:
                    self.state = 29 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 27
                            self.match(D96Parser.LITERAL_INTEGER)
                            self.state = 28
                            self.match(D96Parser.COMMA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 31 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    self.state = 33
                    self.match(D96Parser.LITERAL_INTEGER)
                    pass


                pass
            elif token in [D96Parser.LITERAL_FLOAT]:
                self.state = 44
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 36
                    self.match(D96Parser.LITERAL_FLOAT)
                    pass

                elif la_ == 2:
                    self.state = 39 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 37
                            self.match(D96Parser.LITERAL_FLOAT)
                            self.state = 38
                            self.match(D96Parser.COMMA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 41 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                    self.state = 43
                    self.match(D96Parser.LITERAL_FLOAT)
                    pass


                pass
            elif token in [D96Parser.LITERAL_BOOLEAN]:
                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 46
                    self.match(D96Parser.LITERAL_BOOLEAN)
                    pass

                elif la_ == 2:
                    self.state = 49 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 47
                            self.match(D96Parser.LITERAL_BOOLEAN)
                            self.state = 48
                            self.match(D96Parser.COMMA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 51 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                    self.state = 53
                    self.match(D96Parser.LITERAL_BOOLEAN)
                    pass


                pass
            elif token in [D96Parser.LITERAL_STRING]:
                self.state = 64
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 56
                    self.match(D96Parser.LITERAL_STRING)
                    pass

                elif la_ == 2:
                    self.state = 59 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 57
                            self.match(D96Parser.LITERAL_STRING)
                            self.state = 58
                            self.match(D96Parser.COMMA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 61 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                    self.state = 63
                    self.match(D96Parser.LITERAL_STRING)
                    pass


                pass
            else:
                raise NoViableAltException(self)

            self.state = 68
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiDimentionalArrayContext(ParserRuleContext):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiDimentionalArray" ):
                listener.enterMultiDimentionalArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiDimentionalArray" ):
                listener.exitMultiDimentionalArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiDimentionalArray" ):
                return visitor.visitMultiDimentionalArray(self)
            else:
                return visitor.visitChildren(self)




    def multiDimentionalArray(self):

        localctx = D96Parser.MultiDimentionalArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_multiDimentionalArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(D96Parser.K_ARRAY)
            self.state = 71
            self.match(D96Parser.LEFT_PAREN)
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 72
                self.indexedArray()
                pass

            elif la_ == 2:
                self.state = 76 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 73
                        self.indexedArray()
                        self.state = 74
                        self.match(D96Parser.COMMA)

                    else:
                        raise NoViableAltException(self)
                    self.state = 78 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 80
                self.indexedArray()
                pass


            self.state = 84
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AllTestContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllTest" ):
                listener.enterAllTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllTest" ):
                listener.exitAllTest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllTest" ):
                return visitor.visitAllTest(self)
            else:
                return visitor.visitChildren(self)




    def allTest(self):

        localctx = D96Parser.AllTestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_allTest)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.identifer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.indexedArray()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.multiDimentionalArray()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





