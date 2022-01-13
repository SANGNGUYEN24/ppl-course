# Generated from D:/Study2/HCMUT/semester212/PPL/code/assignment/assignment1/assigment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


 from lexererr import *
 


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2/")
        buf.write("\u01b1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\6\5z\n\5\r\5\16\5{\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\7\6\u0084\n\6\f\6\16\6\u0087\13\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u013d\n)\3*\3*\3+\3+\3")
        buf.write("+\3+\5+\u0145\n+\3,\3,\3,\3,\5,\u014b\n,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\5\61\u0157\n\61\3\61\6\61\u015a")
        buf.write("\n\61\r\61\16\61\u015b\3\62\5\62\u015f\n\62\3\62\3\62")
        buf.write("\3\62\3\62\5\62\u0165\n\62\7\62\u0167\n\62\f\62\16\62")
        buf.write("\u016a\13\62\5\62\u016c\n\62\3\62\3\62\3\63\3\63\6\63")
        buf.write("\u0172\n\63\r\63\16\63\u0173\3\64\3\64\6\64\u0178\n\64")
        buf.write("\r\64\16\64\u0179\3\65\3\65\6\65\u017e\n\65\r\65\16\65")
        buf.write("\u017f\3\66\6\66\u0183\n\66\r\66\16\66\u0184\3\66\3\66")
        buf.write("\7\66\u0189\n\66\f\66\16\66\u018c\13\66\3\66\5\66\u018f")
        buf.write("\n\66\3\66\6\66\u0192\n\66\r\66\16\66\u0193\3\66\5\66")
        buf.write("\u0197\n\66\3\66\3\66\6\66\u019b\n\66\r\66\16\66\u019c")
        buf.write("\3\66\5\66\u01a0\n\66\5\66\u01a2\n\66\3\67\3\67\5\67\u01a6")
        buf.write("\n\67\38\38\38\78\u01ab\n8\f8\168\u01ae\138\38\38\4\u0085")
        buf.write("\u01ac\29\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M\2O\2Q(S\2U\2W\2Y\2[\2]\2_\2a\2c)e*g+i,k-m.o")
        buf.write("/\3\2\f\5\2\13\f\17\17\"\"\5\2\62;CHch\3\2\629\3\2\62")
        buf.write("\63\3\2\62;\4\2GGgg\4\2--//\3\2\62\62\3\2\63;\3\2$$\2")
        buf.write("\u01c5\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2Q\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g")
        buf.write("\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3")
        buf.write("q\3\2\2\2\5t\3\2\2\2\7v\3\2\2\2\ty\3\2\2\2\13\177\3\2")
        buf.write("\2\2\r\u008d\3\2\2\2\17\u0093\3\2\2\2\21\u009c\3\2\2\2")
        buf.write("\23\u009f\3\2\2\2\25\u00a6\3\2\2\2\27\u00ab\3\2\2\2\31")
        buf.write("\u00b3\3\2\2\2\33\u00b8\3\2\2\2\35\u00be\3\2\2\2\37\u00c4")
        buf.write("\3\2\2\2!\u00c7\3\2\2\2#\u00cb\3\2\2\2%\u00d1\3\2\2\2")
        buf.write("\'\u00d9\3\2\2\2)\u00e0\3\2\2\2+\u00e7\3\2\2\2-\u00ec")
        buf.write("\3\2\2\2/\u00f2\3\2\2\2\61\u00f6\3\2\2\2\63\u00fa\3\2")
        buf.write("\2\2\65\u0106\3\2\2\2\67\u0111\3\2\2\29\u0115\3\2\2\2")
        buf.write(";\u0118\3\2\2\2=\u011a\3\2\2\2?\u011c\3\2\2\2A\u011e\3")
        buf.write("\2\2\2C\u0120\3\2\2\2E\u0122\3\2\2\2G\u0124\3\2\2\2I\u0126")
        buf.write("\3\2\2\2K\u0128\3\2\2\2M\u012a\3\2\2\2O\u012c\3\2\2\2")
        buf.write("Q\u013c\3\2\2\2S\u013e\3\2\2\2U\u0144\3\2\2\2W\u014a\3")
        buf.write("\2\2\2Y\u014c\3\2\2\2[\u014e\3\2\2\2]\u0150\3\2\2\2_\u0152")
        buf.write("\3\2\2\2a\u0154\3\2\2\2c\u015e\3\2\2\2e\u016f\3\2\2\2")
        buf.write("g\u0175\3\2\2\2i\u017b\3\2\2\2k\u01a1\3\2\2\2m\u01a5\3")
        buf.write("\2\2\2o\u01a7\3\2\2\2qr\13\2\2\2rs\b\2\2\2s\4\3\2\2\2")
        buf.write("tu\13\2\2\2u\6\3\2\2\2vw\13\2\2\2w\b\3\2\2\2xz\t\2\2\2")
        buf.write("yx\3\2\2\2z{\3\2\2\2{y\3\2\2\2{|\3\2\2\2|}\3\2\2\2}~\b")
        buf.write("\5\3\2~\n\3\2\2\2\177\u0080\7%\2\2\u0080\u0081\7%\2\2")
        buf.write("\u0081\u0085\3\2\2\2\u0082\u0084\13\2\2\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0086\3\2\2\2\u0085")
        buf.write("\u0083\3\2\2\2\u0086\u0088\3\2\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0088\u0089\7%\2\2\u0089\u008a\7%\2\2\u008a\u008b\3\2")
        buf.write("\2\2\u008b\u008c\b\6\3\2\u008c\f\3\2\2\2\u008d\u008e\7")
        buf.write("D\2\2\u008e\u008f\7t\2\2\u008f\u0090\7g\2\2\u0090\u0091")
        buf.write("\7c\2\2\u0091\u0092\7m\2\2\u0092\16\3\2\2\2\u0093\u0094")
        buf.write("\7E\2\2\u0094\u0095\7q\2\2\u0095\u0096\7p\2\2\u0096\u0097")
        buf.write("\7v\2\2\u0097\u0098\7k\2\2\u0098\u0099\7p\2\2\u0099\u009a")
        buf.write("\7w\2\2\u009a\u009b\7g\2\2\u009b\20\3\2\2\2\u009c\u009d")
        buf.write("\7K\2\2\u009d\u009e\7h\2\2\u009e\22\3\2\2\2\u009f\u00a0")
        buf.write("\7G\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2\7u\2\2\u00a2\u00a3")
        buf.write("\7g\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7h\2\2\u00a5\24")
        buf.write("\3\2\2\2\u00a6\u00a7\7G\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9")
        buf.write("\7u\2\2\u00a9\u00aa\7g\2\2\u00aa\26\3\2\2\2\u00ab\u00ac")
        buf.write("\7H\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af")
        buf.write("\7g\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1\7e\2\2\u00b1\u00b2")
        buf.write("\7j\2\2\u00b2\30\3\2\2\2\u00b3\u00b4\7V\2\2\u00b4\u00b5")
        buf.write("\7t\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7\7g\2\2\u00b7\32")
        buf.write("\3\2\2\2\u00b8\u00b9\7H\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb")
        buf.write("\7n\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd\7g\2\2\u00bd\34")
        buf.write("\3\2\2\2\u00be\u00bf\7C\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7t\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7{\2\2\u00c3\36")
        buf.write("\3\2\2\2\u00c4\u00c5\7K\2\2\u00c5\u00c6\7p\2\2\u00c6 ")
        buf.write("\3\2\2\2\u00c7\u00c8\7K\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\"\3\2\2\2\u00cb\u00cc\7H\2\2\u00cc\u00cd")
        buf.write("\7n\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0$\3\2\2\2\u00d1\u00d2\7D\2\2\u00d2\u00d3")
        buf.write("\7q\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7p\2\2\u00d8&\3")
        buf.write("\2\2\2\u00d9\u00da\7U\2\2\u00da\u00db\7v\2\2\u00db\u00dc")
        buf.write("\7t\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de\7p\2\2\u00de\u00df")
        buf.write("\7i\2\2\u00df(\3\2\2\2\u00e0\u00e1\7T\2\2\u00e1\u00e2")
        buf.write("\7g\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4\7w\2\2\u00e4\u00e5")
        buf.write("\7t\2\2\u00e5\u00e6\7p\2\2\u00e6*\3\2\2\2\u00e7\u00e8")
        buf.write("\7P\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb")
        buf.write("\7n\2\2\u00eb,\3\2\2\2\u00ec\u00ed\7E\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0\7u\2\2\u00f0\u00f1")
        buf.write("\7u\2\2\u00f1.\3\2\2\2\u00f2\u00f3\7X\2\2\u00f3\u00f4")
        buf.write("\7c\2\2\u00f4\u00f5\7n\2\2\u00f5\60\3\2\2\2\u00f6\u00f7")
        buf.write("\7X\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7t\2\2\u00f9\62")
        buf.write("\3\2\2\2\u00fa\u00fb\7E\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100\u0101\7w\2\2\u0101\u0102\7e\2\2\u0102\u0103")
        buf.write("\7v\2\2\u0103\u0104\7q\2\2\u0104\u0105\7t\2\2\u0105\64")
        buf.write("\3\2\2\2\u0106\u0107\7F\2\2\u0107\u0108\7g\2\2\u0108\u0109")
        buf.write("\7u\2\2\u0109\u010a\7v\2\2\u010a\u010b\7t\2\2\u010b\u010c")
        buf.write("\7w\2\2\u010c\u010d\7e\2\2\u010d\u010e\7v\2\2\u010e\u010f")
        buf.write("\7q\2\2\u010f\u0110\7t\2\2\u0110\66\3\2\2\2\u0111\u0112")
        buf.write("\7P\2\2\u0112\u0113\7g\2\2\u0113\u0114\7y\2\2\u01148\3")
        buf.write("\2\2\2\u0115\u0116\7D\2\2\u0116\u0117\7{\2\2\u0117:\3")
        buf.write("\2\2\2\u0118\u0119\7*\2\2\u0119<\3\2\2\2\u011a\u011b\7")
        buf.write("+\2\2\u011b>\3\2\2\2\u011c\u011d\7]\2\2\u011d@\3\2\2\2")
        buf.write("\u011e\u011f\7_\2\2\u011fB\3\2\2\2\u0120\u0121\7\60\2")
        buf.write("\2\u0121D\3\2\2\2\u0122\u0123\7.\2\2\u0123F\3\2\2\2\u0124")
        buf.write("\u0125\7=\2\2\u0125H\3\2\2\2\u0126\u0127\7}\2\2\u0127")
        buf.write("J\3\2\2\2\u0128\u0129\7\177\2\2\u0129L\3\2\2\2\u012a\u012b")
        buf.write("\7)\2\2\u012bN\3\2\2\2\u012c\u012d\7$\2\2\u012dP\3\2\2")
        buf.write("\2\u012e\u012f\7)\2\2\u012f\u013d\7$\2\2\u0130\u0131\7")
        buf.write("^\2\2\u0131\u013d\7d\2\2\u0132\u0133\7^\2\2\u0133\u013d")
        buf.write("\7h\2\2\u0134\u0135\7^\2\2\u0135\u013d\7t\2\2\u0136\u0137")
        buf.write("\7^\2\2\u0137\u013d\7p\2\2\u0138\u0139\7^\2\2\u0139\u013d")
        buf.write("\7v\2\2\u013a\u013b\7^\2\2\u013b\u013d\7^\2\2\u013c\u012e")
        buf.write("\3\2\2\2\u013c\u0130\3\2\2\2\u013c\u0132\3\2\2\2\u013c")
        buf.write("\u0134\3\2\2\2\u013c\u0136\3\2\2\2\u013c\u0138\3\2\2\2")
        buf.write("\u013c\u013a\3\2\2\2\u013dR\3\2\2\2\u013e\u013f\7\62\2")
        buf.write("\2\u013fT\3\2\2\2\u0140\u0141\7\62\2\2\u0141\u0145\7z")
        buf.write("\2\2\u0142\u0143\7\62\2\2\u0143\u0145\7Z\2\2\u0144\u0140")
        buf.write("\3\2\2\2\u0144\u0142\3\2\2\2\u0145V\3\2\2\2\u0146\u0147")
        buf.write("\7\62\2\2\u0147\u014b\7d\2\2\u0148\u0149\7\62\2\2\u0149")
        buf.write("\u014b\7D\2\2\u014a\u0146\3\2\2\2\u014a\u0148\3\2\2\2")
        buf.write("\u014bX\3\2\2\2\u014c\u014d\t\3\2\2\u014dZ\3\2\2\2\u014e")
        buf.write("\u014f\t\4\2\2\u014f\\\3\2\2\2\u0150\u0151\t\5\2\2\u0151")
        buf.write("^\3\2\2\2\u0152\u0153\t\6\2\2\u0153`\3\2\2\2\u0154\u0156")
        buf.write("\t\7\2\2\u0155\u0157\t\b\2\2\u0156\u0155\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u015a\5_\60\2")
        buf.write("\u0159\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0159\3")
        buf.write("\2\2\2\u015b\u015c\3\2\2\2\u015cb\3\2\2\2\u015d\u015f")
        buf.write("\t\b\2\2\u015e\u015d\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u016b\3\2\2\2\u0160\u016c\t\t\2\2\u0161\u0164\t\n\2\2")
        buf.write("\u0162\u0165\5_\60\2\u0163\u0165\7a\2\2\u0164\u0162\3")
        buf.write("\2\2\2\u0164\u0163\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0161")
        buf.write("\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2")
        buf.write("\u016b\u0160\3\2\2\2\u016b\u0168\3\2\2\2\u016c\u016d\3")
        buf.write("\2\2\2\u016d\u016e\b\62\4\2\u016ed\3\2\2\2\u016f\u0171")
        buf.write("\5S*\2\u0170\u0172\5[.\2\u0171\u0170\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("f\3\2\2\2\u0175\u0177\5U+\2\u0176\u0178\5Y-\2\u0177\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0177\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017ah\3\2\2\2\u017b\u017d\5W,\2\u017c")
        buf.write("\u017e\5]/\2\u017d\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180j\3\2\2\2\u0181")
        buf.write("\u0183\5c\62\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\3")
        buf.write("\2\2\2\u0186\u018a\5C\"\2\u0187\u0189\5_\60\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2")
        buf.write("\u018d\u018f\5a\61\2\u018e\u018d\3\2\2\2\u018e\u018f\3")
        buf.write("\2\2\2\u018f\u01a2\3\2\2\2\u0190\u0192\5c\62\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u0196\3\2\2\2\u0195\u0197\5a\61\2")
        buf.write("\u0196\u0195\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u01a2\3")
        buf.write("\2\2\2\u0198\u019a\5C\"\2\u0199\u019b\5_\60\2\u019a\u0199")
        buf.write("\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019a\3\2\2\2\u019c")
        buf.write("\u019d\3\2\2\2\u019d\u019f\3\2\2\2\u019e\u01a0\5a\61\2")
        buf.write("\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2\3")
        buf.write("\2\2\2\u01a1\u0182\3\2\2\2\u01a1\u0191\3\2\2\2\u01a1\u0198")
        buf.write("\3\2\2\2\u01a2l\3\2\2\2\u01a3\u01a6\5\31\r\2\u01a4\u01a6")
        buf.write("\5\33\16\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6")
        buf.write("n\3\2\2\2\u01a7\u01ac\5O(\2\u01a8\u01ab\5Q)\2\u01a9\u01ab")
        buf.write("\n\13\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab")
        buf.write("\u01ae\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ad\u01af\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b0\5")
        buf.write("O(\2\u01b0p\3\2\2\2\34\2{\u0085\u013c\u0144\u014a\u0156")
        buf.write("\u015b\u015e\u0164\u0168\u016b\u0173\u0179\u017f\u0184")
        buf.write("\u018a\u018e\u0193\u0196\u019c\u019f\u01a1\u01a5\u01aa")
        buf.write("\u01ac\5\3\2\2\b\2\2\3\62\3")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ERROR_CHAR = 1
    UNCLOSE_STRING = 2
    ILLEGAL_ESCAPE = 3
    WHITE_SPACE = 4
    COMMENT = 5
    BREAK = 6
    CONTINUE = 7
    IF = 8
    ELSE_IF = 9
    ELSE = 10
    FOR_EACH = 11
    TRUE = 12
    FALSE = 13
    ARRAY = 14
    IN = 15
    INT = 16
    FLOAT = 17
    BOOLEAN = 18
    STRING = 19
    RETURN = 20
    NULL = 21
    CLASS = 22
    VAL = 23
    VAR = 24
    CONSTRUCTOR = 25
    DESTRUCTOR = 26
    NEW = 27
    BY = 28
    LEFT_PAREN = 29
    RIGHT_PAREN = 30
    LEFT_SQUARE_BRACKET = 31
    RIGHT_SQUARE_BRACKET = 32
    DOT = 33
    COMMA = 34
    SEMICOLON = 35
    LEFT_CURLY_BRACKET = 36
    RIGHT_CURLY_BRACKET = 37
    ESCAPE = 38
    INTEGER = 39
    OCTAL_LITERALNESS = 40
    HEXA_LITERALNESS = 41
    BINARY_LITERALNESS = 42
    FLOAT_LITERALNESS = 43
    BOOLEAN_LITERALNESS = 44
    STRING_LITERALNESS = 45

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'('", 
            "')'", "'['", "']'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WHITE_SPACE", 
            "COMMENT", "BREAK", "CONTINUE", "IF", "ELSE_IF", "ELSE", "FOR_EACH", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", 
            "RIGHT_SQUARE_BRACKET", "DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", 
            "RIGHT_CURLY_BRACKET", "ESCAPE", "INTEGER", "OCTAL_LITERALNESS", 
            "HEXA_LITERALNESS", "BINARY_LITERALNESS", "FLOAT_LITERALNESS", 
            "BOOLEAN_LITERALNESS", "STRING_LITERALNESS" ]

    ruleNames = [ "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WHITE_SPACE", 
                  "COMMENT", "BREAK", "CONTINUE", "IF", "ELSE_IF", "ELSE", 
                  "FOR_EACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", 
                  "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", 
                  "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "LEFT_PAREN", 
                  "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                  "DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                  "SINGLE_QUOTE", "DOUBLE_QUOTE", "ESCAPE", "OCTAL_NOTATION", 
                  "HEXA_NOTATION", "BINARY_NOTATION", "HEXA_DIGIT", "OCTAL_DIGIT", 
                  "BINARY_DIGIT", "DECIMAL_DIGIT", "EXPONENT", "INTEGER", 
                  "OCTAL_LITERALNESS", "HEXA_LITERALNESS", "BINARY_LITERALNESS", 
                  "FLOAT_LITERALNESS", "BOOLEAN_LITERALNESS", "STRING_LITERALNESS" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.ERROR_CHAR_action 
            actions[48] = self.INTEGER_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken (self.text)
     

    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     


