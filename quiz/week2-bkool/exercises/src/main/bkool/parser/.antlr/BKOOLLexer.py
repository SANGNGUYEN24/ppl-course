# Generated from d:\Study2\HCMUT\semester212\PPL\code\quiz\week2-bkool\exercises\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("\u0103\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3")
        buf.write("\r\3\16\3\16\3\17\3\17\3\20\6\20j\n\20\r\20\16\20k\3\20")
        buf.write("\7\20o\n\20\f\20\16\20r\13\20\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\5\22z\n\22\3\23\3\23\3\23\3\23\5\23\u0080\n\23\3")
        buf.write("\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\5\30")
        buf.write("\u008c\n\30\3\30\6\30\u008f\n\30\r\30\16\30\u0090\3\31")
        buf.write("\3\31\3\31\5\31\u0096\n\31\3\31\6\31\u0099\n\31\r\31\16")
        buf.write("\31\u009a\3\31\3\31\7\31\u009f\n\31\f\31\16\31\u00a2\13")
        buf.write("\31\3\31\6\31\u00a5\n\31\r\31\16\31\u00a6\5\31\u00a9\n")
        buf.write("\31\3\32\3\32\6\32\u00ad\n\32\r\32\16\32\u00ae\3\32\3")
        buf.write("\32\7\32\u00b3\n\32\f\32\16\32\u00b6\13\32\3\32\6\32\u00b9")
        buf.write("\n\32\r\32\16\32\u00ba\3\33\3\33\6\33\u00bf\n\33\r\33")
        buf.write("\16\33\u00c0\3\33\3\33\7\33\u00c5\n\33\f\33\16\33\u00c8")
        buf.write("\13\33\3\33\6\33\u00cb\n\33\r\33\16\33\u00cc\3\34\3\34")
        buf.write("\6\34\u00d1\n\34\r\34\16\34\u00d2\3\34\3\34\7\34\u00d7")
        buf.write("\n\34\f\34\16\34\u00da\13\34\3\34\6\34\u00dd\n\34\r\34")
        buf.write("\16\34\u00de\3\35\3\35\3\35\3\35\5\35\u00e5\n\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\5\36\u00ec\n\36\3\36\5\36\u00ef\n")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\5\36\u00f6\n\36\3\36\5\36")
        buf.write("\u00f9\n\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \2\2")
        buf.write("!\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63")
        buf.write("\2\65\2\67\29\22;\23=\24?\25\3\2\f\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\5\2\62;CHch\3\2\629\3\2\62\63\3\2\62;\4\2GGgg")
        buf.write("\4\2--//\3\2\63;\5\2\13\f\17\17\"\"\2\u0112\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\3A\3\2\2\2\5E\3\2\2\2\7K\3\2\2\2\tR\3\2\2\2")
        buf.write("\13T\3\2\2\2\rV\3\2\2\2\17X\3\2\2\2\21Z\3\2\2\2\23\\\3")
        buf.write("\2\2\2\25^\3\2\2\2\27`\3\2\2\2\31b\3\2\2\2\33d\3\2\2\2")
        buf.write("\35f\3\2\2\2\37i\3\2\2\2!s\3\2\2\2#y\3\2\2\2%\177\3\2")
        buf.write("\2\2\'\u0081\3\2\2\2)\u0083\3\2\2\2+\u0085\3\2\2\2-\u0087")
        buf.write("\3\2\2\2/\u0089\3\2\2\2\61\u00a8\3\2\2\2\63\u00aa\3\2")
        buf.write("\2\2\65\u00bc\3\2\2\2\67\u00ce\3\2\2\29\u00e4\3\2\2\2")
        buf.write(";\u00f8\3\2\2\2=\u00fc\3\2\2\2?\u0100\3\2\2\2AB\7k\2\2")
        buf.write("BC\7p\2\2CD\7v\2\2D\4\3\2\2\2EF\7h\2\2FG\7n\2\2GH\7q\2")
        buf.write("\2HI\7c\2\2IJ\7v\2\2J\6\3\2\2\2KL\7t\2\2LM\7g\2\2MN\7")
        buf.write("v\2\2NO\7w\2\2OP\7t\2\2PQ\7p\2\2Q\b\3\2\2\2RS\7-\2\2S")
        buf.write("\n\3\2\2\2TU\7/\2\2U\f\3\2\2\2VW\7,\2\2W\16\3\2\2\2XY")
        buf.write("\7\61\2\2Y\20\3\2\2\2Z[\7=\2\2[\22\3\2\2\2\\]\7.\2\2]")
        buf.write("\24\3\2\2\2^_\7*\2\2_\26\3\2\2\2`a\7+\2\2a\30\3\2\2\2")
        buf.write("bc\7}\2\2c\32\3\2\2\2de\7\177\2\2e\34\3\2\2\2fg\7?\2\2")
        buf.write("g\36\3\2\2\2hj\t\2\2\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2k")
        buf.write("l\3\2\2\2lp\3\2\2\2mo\t\3\2\2nm\3\2\2\2or\3\2\2\2pn\3")
        buf.write("\2\2\2pq\3\2\2\2q \3\2\2\2rp\3\2\2\2st\7\62\2\2t\"\3\2")
        buf.write("\2\2uv\7\62\2\2vz\7z\2\2wx\7\62\2\2xz\7Z\2\2yu\3\2\2\2")
        buf.write("yw\3\2\2\2z$\3\2\2\2{|\7\62\2\2|\u0080\7d\2\2}~\7\62\2")
        buf.write("\2~\u0080\7D\2\2\177{\3\2\2\2\177}\3\2\2\2\u0080&\3\2")
        buf.write("\2\2\u0081\u0082\t\4\2\2\u0082(\3\2\2\2\u0083\u0084\t")
        buf.write("\5\2\2\u0084*\3\2\2\2\u0085\u0086\t\6\2\2\u0086,\3\2\2")
        buf.write("\2\u0087\u0088\t\7\2\2\u0088.\3\2\2\2\u0089\u008b\t\b")
        buf.write("\2\2\u008a\u008c\t\t\2\2\u008b\u008a\3\2\2\2\u008b\u008c")
        buf.write("\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u008f\5\61\31\2\u008e")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\60\3\2\2\2\u0092\u00a9\5-\27")
        buf.write("\2\u0093\u0095\t\n\2\2\u0094\u0096\7a\2\2\u0095\u0094")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u00a0\3\2\2\2\u0097")
        buf.write("\u0099\5-\27\2\u0098\u0097\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\3")
        buf.write("\2\2\2\u009c\u009d\7a\2\2\u009d\u009f\3\2\2\2\u009e\u0098")
        buf.write("\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2")
        buf.write("\u00a3\u00a5\5-\27\2\u00a4\u00a3\3\2\2\2\u00a5\u00a6\3")
        buf.write("\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9")
        buf.write("\3\2\2\2\u00a8\u0092\3\2\2\2\u00a8\u0093\3\2\2\2\u00a9")
        buf.write("\62\3\2\2\2\u00aa\u00b4\5!\21\2\u00ab\u00ad\5)\25\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00ae\u00af\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\7")
        buf.write("a\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00ac\3\2\2\2\u00b3\u00b6")
        buf.write("\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b9\5)\25\2")
        buf.write("\u00b8\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00b8\3")
        buf.write("\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\64\3\2\2\2\u00bc\u00c6")
        buf.write("\5#\22\2\u00bd\u00bf\5\'\24\2\u00be\u00bd\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2")
        buf.write("\u00c1\u00c2\3\2\2\2\u00c2\u00c3\7a\2\2\u00c3\u00c5\3")
        buf.write("\2\2\2\u00c4\u00be\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4")
        buf.write("\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8")
        buf.write("\u00c6\3\2\2\2\u00c9\u00cb\5\'\24\2\u00ca\u00c9\3\2\2")
        buf.write("\2\u00cb\u00cc\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\66\3\2\2\2\u00ce\u00d8\5%\23\2\u00cf\u00d1")
        buf.write("\5+\26\2\u00d0\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\u00d5\7a\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00d0\3")
        buf.write("\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00db")
        buf.write("\u00dd\5+\26\2\u00dc\u00db\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df8\3\2\2")
        buf.write("\2\u00e0\u00e5\5\61\31\2\u00e1\u00e5\5\63\32\2\u00e2\u00e5")
        buf.write("\5\65\33\2\u00e3\u00e5\5\67\34\2\u00e4\u00e0\3\2\2\2\u00e4")
        buf.write("\u00e1\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\u00e7\b\35\2\2\u00e7:\3\2\2")
        buf.write("\2\u00e8\u00e9\5\61\31\2\u00e9\u00eb\7\60\2\2\u00ea\u00ec")
        buf.write("\5\61\31\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write("\u00ee\3\2\2\2\u00ed\u00ef\5/\30\2\u00ee\u00ed\3\2\2\2")
        buf.write("\u00ee\u00ef\3\2\2\2\u00ef\u00f9\3\2\2\2\u00f0\u00f1\5")
        buf.write("\61\31\2\u00f1\u00f2\5/\30\2\u00f2\u00f9\3\2\2\2\u00f3")
        buf.write("\u00f5\7\60\2\2\u00f4\u00f6\5\61\31\2\u00f5\u00f4\3\2")
        buf.write("\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9")
        buf.write("\5/\30\2\u00f8\u00e8\3\2\2\2\u00f8\u00f0\3\2\2\2\u00f8")
        buf.write("\u00f3\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\b\36\3")
        buf.write("\2\u00fb<\3\2\2\2\u00fc\u00fd\t\13\2\2\u00fd\u00fe\3\2")
        buf.write("\2\2\u00fe\u00ff\b\37\4\2\u00ff>\3\2\2\2\u0100\u0101\13")
        buf.write("\2\2\2\u0101\u0102\b \5\2\u0102@\3\2\2\2\34\2kpy\177\u008b")
        buf.write("\u0090\u0095\u009a\u00a0\u00a6\u00a8\u00ae\u00b4\u00ba")
        buf.write("\u00c0\u00c6\u00cc\u00d2\u00d8\u00de\u00e4\u00eb\u00ee")
        buf.write("\u00f5\u00f8\6\3\35\2\3\36\3\b\2\2\3 \4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    SEMI_COLON = 8
    COMMA = 9
    LEFT_PAREN = 10
    RIGHT_PAREN = 11
    LEFT_CURLY_BRACKET = 12
    RIGHT_CURLY_BRACKET = 13
    ASSIGN = 14
    ID = 15
    LITERAL_INTEGER = 16
    LITERAL_FLOAT = 17
    WS = 18
    ERROR_CHAR = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'return'", "'+'", "'-'", "'*'", "'/'", 
            "';'", "','", "'('", "')'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "SEMI_COLON", "COMMA", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_CURLY_BRACKET", 
            "RIGHT_CURLY_BRACKET", "ASSIGN", "ID", "LITERAL_INTEGER", "LITERAL_FLOAT", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "SEMI_COLON", "COMMA", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_CURLY_BRACKET", 
                  "RIGHT_CURLY_BRACKET", "ASSIGN", "ID", "OCTAL_NOTATION", 
                  "HEXA_NOTATION", "BINARY_NOTATION", "HEXA_DIGIT", "OCTAL_DIGIT", 
                  "BINARY_DIGIT", "DECIMAL_DIGIT", "EXPONENT", "DECIMAL", 
                  "OCTAL", "HEXA", "BINARY", "LITERAL_INTEGER", "LITERAL_FLOAT", 
                  "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[27] = self.LITERAL_INTEGER_action 
            actions[28] = self.LITERAL_FLOAT_action 
            actions[30] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def LITERAL_INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def LITERAL_FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


