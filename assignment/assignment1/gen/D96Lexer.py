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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u01d6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\7")
        buf.write("\2t\n\2\f\2\16\2w\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\5#\u0122\n#\3$\3$\3%\3%\3&\3&\3&\3&\5&\u012c\n")
        buf.write("&\3\'\3\'\3\'\3\'\5\'\u0132\n\'\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\5,\u013e\n,\3,\6,\u0141\n,\r,\16,\u0142\3-\3-")
        buf.write("\3-\5-\u0148\n-\3-\6-\u014b\n-\r-\16-\u014c\3-\3-\7-\u0151")
        buf.write("\n-\f-\16-\u0154\13-\3-\6-\u0157\n-\r-\16-\u0158\5-\u015b")
        buf.write("\n-\3.\3.\6.\u015f\n.\r.\16.\u0160\3.\3.\7.\u0165\n.\f")
        buf.write(".\16.\u0168\13.\3.\6.\u016b\n.\r.\16.\u016c\3/\3/\6/\u0171")
        buf.write("\n/\r/\16/\u0172\3/\3/\7/\u0177\n/\f/\16/\u017a\13/\3")
        buf.write("/\6/\u017d\n/\r/\16/\u017e\3\60\3\60\6\60\u0183\n\60\r")
        buf.write("\60\16\60\u0184\3\60\3\60\7\60\u0189\n\60\f\60\16\60\u018c")
        buf.write("\13\60\3\60\6\60\u018f\n\60\r\60\16\60\u0190\3\61\3\61")
        buf.write("\3\61\3\61\5\61\u0197\n\61\3\61\3\61\3\62\3\62\3\62\3")
        buf.write("\62\5\62\u019f\n\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\5\62\u01a8\n\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\5\63\u01b5\n\63\3\64\3\64\3\64\7\64")
        buf.write("\u01ba\n\64\f\64\16\64\u01bd\13\64\3\64\3\64\3\65\5\65")
        buf.write("\u01c2\n\65\3\65\7\65\u01c5\n\65\f\65\16\65\u01c8\13\65")
        buf.write("\3\66\3\66\6\66\u01cc\n\66\r\66\16\66\u01cd\3\67\6\67")
        buf.write("\u01d1\n\67\r\67\16\67\u01d2\3\67\3\67\4u\u01bb\28\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\2C\2E\"G#I\2K\2M\2")
        buf.write("O\2Q\2S\2U\2W\2Y\2[\2]\2_\2a$c%e&g\'i(k)m*\3\2\r\4\2-")
        buf.write("-//\5\2\62;CHch\3\2\629\3\2\62\63\3\2\62;\4\2GGgg\3\2")
        buf.write("\63;\4\2$$^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17")
        buf.write("\"\"\2\u01ec\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\3o\3\2\2\2\5}\3\2\2\2\7\u0083\3\2\2\2\t\u008c\3\2")
        buf.write("\2\2\13\u008f\3\2\2\2\r\u0096\3\2\2\2\17\u009b\3\2\2\2")
        buf.write("\21\u00a3\3\2\2\2\23\u00a9\3\2\2\2\25\u00ac\3\2\2\2\27")
        buf.write("\u00b0\3\2\2\2\31\u00b6\3\2\2\2\33\u00be\3\2\2\2\35\u00c5")
        buf.write("\3\2\2\2\37\u00cc\3\2\2\2!\u00d1\3\2\2\2#\u00d7\3\2\2")
        buf.write("\2%\u00db\3\2\2\2\'\u00df\3\2\2\2)\u00eb\3\2\2\2+\u00f6")
        buf.write("\3\2\2\2-\u00fa\3\2\2\2/\u00fd\3\2\2\2\61\u00ff\3\2\2")
        buf.write("\2\63\u0101\3\2\2\2\65\u0103\3\2\2\2\67\u0105\3\2\2\2")
        buf.write("9\u0107\3\2\2\2;\u0109\3\2\2\2=\u010b\3\2\2\2?\u010d\3")
        buf.write("\2\2\2A\u010f\3\2\2\2C\u0111\3\2\2\2E\u0121\3\2\2\2G\u0123")
        buf.write("\3\2\2\2I\u0125\3\2\2\2K\u012b\3\2\2\2M\u0131\3\2\2\2")
        buf.write("O\u0133\3\2\2\2Q\u0135\3\2\2\2S\u0137\3\2\2\2U\u0139\3")
        buf.write("\2\2\2W\u013b\3\2\2\2Y\u015a\3\2\2\2[\u015c\3\2\2\2]\u016e")
        buf.write("\3\2\2\2_\u0180\3\2\2\2a\u0196\3\2\2\2c\u01a7\3\2\2\2")
        buf.write("e\u01b4\3\2\2\2g\u01b6\3\2\2\2i\u01c1\3\2\2\2k\u01c9\3")
        buf.write("\2\2\2m\u01d0\3\2\2\2op\7%\2\2pq\7%\2\2qu\3\2\2\2rt\13")
        buf.write("\2\2\2sr\3\2\2\2tw\3\2\2\2uv\3\2\2\2us\3\2\2\2vx\3\2\2")
        buf.write("\2wu\3\2\2\2xy\7%\2\2yz\7%\2\2z{\3\2\2\2{|\b\2\2\2|\4")
        buf.write("\3\2\2\2}~\7D\2\2~\177\7t\2\2\177\u0080\7g\2\2\u0080\u0081")
        buf.write("\7c\2\2\u0081\u0082\7m\2\2\u0082\6\3\2\2\2\u0083\u0084")
        buf.write("\7E\2\2\u0084\u0085\7q\2\2\u0085\u0086\7p\2\2\u0086\u0087")
        buf.write("\7v\2\2\u0087\u0088\7k\2\2\u0088\u0089\7p\2\2\u0089\u008a")
        buf.write("\7w\2\2\u008a\u008b\7g\2\2\u008b\b\3\2\2\2\u008c\u008d")
        buf.write("\7K\2\2\u008d\u008e\7h\2\2\u008e\n\3\2\2\2\u008f\u0090")
        buf.write("\7G\2\2\u0090\u0091\7n\2\2\u0091\u0092\7u\2\2\u0092\u0093")
        buf.write("\7g\2\2\u0093\u0094\7k\2\2\u0094\u0095\7h\2\2\u0095\f")
        buf.write("\3\2\2\2\u0096\u0097\7G\2\2\u0097\u0098\7n\2\2\u0098\u0099")
        buf.write("\7u\2\2\u0099\u009a\7g\2\2\u009a\16\3\2\2\2\u009b\u009c")
        buf.write("\7H\2\2\u009c\u009d\7q\2\2\u009d\u009e\7t\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1\7e\2\2\u00a1\u00a2")
        buf.write("\7j\2\2\u00a2\20\3\2\2\2\u00a3\u00a4\7C\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8")
        buf.write("\7{\2\2\u00a8\22\3\2\2\2\u00a9\u00aa\7K\2\2\u00aa\u00ab")
        buf.write("\7p\2\2\u00ab\24\3\2\2\2\u00ac\u00ad\7K\2\2\u00ad\u00ae")
        buf.write("\7p\2\2\u00ae\u00af\7v\2\2\u00af\26\3\2\2\2\u00b0\u00b1")
        buf.write("\7H\2\2\u00b1\u00b2\7n\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4")
        buf.write("\7c\2\2\u00b4\u00b5\7v\2\2\u00b5\30\3\2\2\2\u00b6\u00b7")
        buf.write("\7D\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba")
        buf.write("\7n\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd")
        buf.write("\7p\2\2\u00bd\32\3\2\2\2\u00be\u00bf\7U\2\2\u00bf\u00c0")
        buf.write("\7v\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3")
        buf.write("\7p\2\2\u00c3\u00c4\7i\2\2\u00c4\34\3\2\2\2\u00c5\u00c6")
        buf.write("\7T\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9")
        buf.write("\7w\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7p\2\2\u00cb\36")
        buf.write("\3\2\2\2\u00cc\u00cd\7P\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf")
        buf.write("\7n\2\2\u00cf\u00d0\7n\2\2\u00d0 \3\2\2\2\u00d1\u00d2")
        buf.write("\7E\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5")
        buf.write("\7u\2\2\u00d5\u00d6\7u\2\2\u00d6\"\3\2\2\2\u00d7\u00d8")
        buf.write("\7X\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da\7n\2\2\u00da$\3")
        buf.write("\2\2\2\u00db\u00dc\7X\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de&\3\2\2\2\u00df\u00e0\7E\2\2\u00e0\u00e1")
        buf.write("\7q\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7u\2\2\u00e3\u00e4")
        buf.write("\7v\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7w\2\2\u00e6\u00e7")
        buf.write("\7e\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea")
        buf.write("\7t\2\2\u00ea(\3\2\2\2\u00eb\u00ec\7F\2\2\u00ec\u00ed")
        buf.write("\7g\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0")
        buf.write("\7t\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2\7e\2\2\u00f2\u00f3")
        buf.write("\7v\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5\7t\2\2\u00f5*\3")
        buf.write("\2\2\2\u00f6\u00f7\7P\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9")
        buf.write("\7y\2\2\u00f9,\3\2\2\2\u00fa\u00fb\7D\2\2\u00fb\u00fc")
        buf.write("\7{\2\2\u00fc.\3\2\2\2\u00fd\u00fe\7*\2\2\u00fe\60\3\2")
        buf.write("\2\2\u00ff\u0100\7+\2\2\u0100\62\3\2\2\2\u0101\u0102\7")
        buf.write("]\2\2\u0102\64\3\2\2\2\u0103\u0104\7_\2\2\u0104\66\3\2")
        buf.write("\2\2\u0105\u0106\7\60\2\2\u01068\3\2\2\2\u0107\u0108\7")
        buf.write(".\2\2\u0108:\3\2\2\2\u0109\u010a\7=\2\2\u010a<\3\2\2\2")
        buf.write("\u010b\u010c\7}\2\2\u010c>\3\2\2\2\u010d\u010e\7\177\2")
        buf.write("\2\u010e@\3\2\2\2\u010f\u0110\7)\2\2\u0110B\3\2\2\2\u0111")
        buf.write("\u0112\7$\2\2\u0112D\3\2\2\2\u0113\u0114\7)\2\2\u0114")
        buf.write("\u0122\7$\2\2\u0115\u0116\7^\2\2\u0116\u0122\7d\2\2\u0117")
        buf.write("\u0118\7^\2\2\u0118\u0122\7h\2\2\u0119\u011a\7^\2\2\u011a")
        buf.write("\u0122\7t\2\2\u011b\u011c\7^\2\2\u011c\u0122\7p\2\2\u011d")
        buf.write("\u011e\7^\2\2\u011e\u0122\7v\2\2\u011f\u0120\7^\2\2\u0120")
        buf.write("\u0122\7^\2\2\u0121\u0113\3\2\2\2\u0121\u0115\3\2\2\2")
        buf.write("\u0121\u0117\3\2\2\2\u0121\u0119\3\2\2\2\u0121\u011b\3")
        buf.write("\2\2\2\u0121\u011d\3\2\2\2\u0121\u011f\3\2\2\2\u0122F")
        buf.write("\3\2\2\2\u0123\u0124\t\2\2\2\u0124H\3\2\2\2\u0125\u0126")
        buf.write("\7\62\2\2\u0126J\3\2\2\2\u0127\u0128\7\62\2\2\u0128\u012c")
        buf.write("\7z\2\2\u0129\u012a\7\62\2\2\u012a\u012c\7Z\2\2\u012b")
        buf.write("\u0127\3\2\2\2\u012b\u0129\3\2\2\2\u012cL\3\2\2\2\u012d")
        buf.write("\u012e\7\62\2\2\u012e\u0132\7d\2\2\u012f\u0130\7\62\2")
        buf.write("\2\u0130\u0132\7D\2\2\u0131\u012d\3\2\2\2\u0131\u012f")
        buf.write("\3\2\2\2\u0132N\3\2\2\2\u0133\u0134\t\3\2\2\u0134P\3\2")
        buf.write("\2\2\u0135\u0136\t\4\2\2\u0136R\3\2\2\2\u0137\u0138\t")
        buf.write("\5\2\2\u0138T\3\2\2\2\u0139\u013a\t\6\2\2\u013aV\3\2\2")
        buf.write("\2\u013b\u013d\t\7\2\2\u013c\u013e\t\2\2\2\u013d\u013c")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0140\3\2\2\2\u013f")
        buf.write("\u0141\5Y-\2\u0140\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142")
        buf.write("\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143X\3\2\2\2\u0144")
        buf.write("\u015b\5U+\2\u0145\u0147\t\b\2\2\u0146\u0148\7a\2\2\u0147")
        buf.write("\u0146\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0152\3\2\2\2")
        buf.write("\u0149\u014b\5U+\2\u014a\u0149\3\2\2\2\u014b\u014c\3\2")
        buf.write("\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e\u014f\7a\2\2\u014f\u0151\3\2\2\2\u0150")
        buf.write("\u014a\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2")
        buf.write("\u0152\u0153\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152\3")
        buf.write("\2\2\2\u0155\u0157\5U+\2\u0156\u0155\3\2\2\2\u0157\u0158")
        buf.write("\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write("\u015b\3\2\2\2\u015a\u0144\3\2\2\2\u015a\u0145\3\2\2\2")
        buf.write("\u015bZ\3\2\2\2\u015c\u0166\5I%\2\u015d\u015f\5Q)\2\u015e")
        buf.write("\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0160\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\7")
        buf.write("a\2\2\u0163\u0165\3\2\2\2\u0164\u015e\3\2\2\2\u0165\u0168")
        buf.write("\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016b\5Q)\2\u016a")
        buf.write("\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016d\\\3\2\2\2\u016e\u0178\5K&\2")
        buf.write("\u016f\u0171\5O(\2\u0170\u016f\3\2\2\2\u0171\u0172\3\2")
        buf.write("\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174")
        buf.write("\3\2\2\2\u0174\u0175\7a\2\2\u0175\u0177\3\2\2\2\u0176")
        buf.write("\u0170\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3")
        buf.write("\2\2\2\u017b\u017d\5O(\2\u017c\u017b\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("^\3\2\2\2\u0180\u018a\5M\'\2\u0181\u0183\5S*\2\u0182\u0181")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\7a\2\2")
        buf.write("\u0187\u0189\3\2\2\2\u0188\u0182\3\2\2\2\u0189\u018c\3")
        buf.write("\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018e")
        buf.write("\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018f\5S*\2\u018e\u018d")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u018e\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191`\3\2\2\2\u0192\u0197\5Y-\2\u0193")
        buf.write("\u0197\5[.\2\u0194\u0197\5]/\2\u0195\u0197\5_\60\2\u0196")
        buf.write("\u0192\3\2\2\2\u0196\u0193\3\2\2\2\u0196\u0194\3\2\2\2")
        buf.write("\u0196\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\b")
        buf.write("\61\3\2\u0199b\3\2\2\2\u019a\u019b\5Y-\2\u019b\u019c\5")
        buf.write("\67\34\2\u019c\u019e\5Y-\2\u019d\u019f\5W,\2\u019e\u019d")
        buf.write("\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a8\3\2\2\2\u01a0")
        buf.write("\u01a1\5Y-\2\u01a1\u01a2\5W,\2\u01a2\u01a8\3\2\2\2\u01a3")
        buf.write("\u01a4\5\67\34\2\u01a4\u01a5\5Y-\2\u01a5\u01a6\5W,\2\u01a6")
        buf.write("\u01a8\3\2\2\2\u01a7\u019a\3\2\2\2\u01a7\u01a0\3\2\2\2")
        buf.write("\u01a7\u01a3\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\b")
        buf.write("\62\4\2\u01aad\3\2\2\2\u01ab\u01ac\7V\2\2\u01ac\u01ad")
        buf.write("\7t\2\2\u01ad\u01ae\7w\2\2\u01ae\u01b5\7g\2\2\u01af\u01b0")
        buf.write("\7H\2\2\u01b0\u01b1\7c\2\2\u01b1\u01b2\7n\2\2\u01b2\u01b3")
        buf.write("\7u\2\2\u01b3\u01b5\7g\2\2\u01b4\u01ab\3\2\2\2\u01b4\u01af")
        buf.write("\3\2\2\2\u01b5f\3\2\2\2\u01b6\u01bb\5C\"\2\u01b7\u01ba")
        buf.write("\5E#\2\u01b8\u01ba\n\t\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01be\u01bf\5C\"\2\u01bfh\3\2\2\2\u01c0\u01c2\t\n\2\2")
        buf.write("\u01c1\u01c0\3\2\2\2\u01c2\u01c6\3\2\2\2\u01c3\u01c5\t")
        buf.write("\13\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7j\3\2\2\2\u01c8")
        buf.write("\u01c6\3\2\2\2\u01c9\u01cb\7&\2\2\u01ca\u01cc\t\13\2\2")
        buf.write("\u01cb\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cb\3")
        buf.write("\2\2\2\u01cd\u01ce\3\2\2\2\u01cel\3\2\2\2\u01cf\u01d1")
        buf.write("\t\f\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d4\3\2\2\2")
        buf.write("\u01d4\u01d5\b\67\2\2\u01d5n\3\2\2\2#\2u\u0121\u012b\u0131")
        buf.write("\u013d\u0142\u0147\u014c\u0152\u0158\u015a\u0160\u0166")
        buf.write("\u016c\u0172\u0178\u017e\u0184\u018a\u0190\u0196\u019e")
        buf.write("\u01a7\u01b4\u01b9\u01bb\u01c1\u01c4\u01c6\u01cb\u01cd")
        buf.write("\u01d2\5\b\2\2\3\61\2\3\62\3")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    K_BREAK = 2
    K_CONTINUE = 3
    K_IF = 4
    K_ELSE_IF = 5
    K_ELSE = 6
    K_FOR_EACH = 7
    K_ARRAY = 8
    K_IN = 9
    K_INT = 10
    K_FLOAT = 11
    K_BOOLEAN = 12
    K_STRING = 13
    K_RETURN = 14
    K_NULL = 15
    K_CLASS = 16
    K_VAL = 17
    K_VAR = 18
    K_CONSTRUCTOR = 19
    K_DESTRUCTOR = 20
    K_NEW = 21
    K_BY = 22
    LEFT_PAREN = 23
    RIGHT_PAREN = 24
    LEFT_SQUARE_BRACKET = 25
    RIGHT_SQUARE_BRACKET = 26
    DOT = 27
    COMMA = 28
    SEMICOLON = 29
    LEFT_CURLY_BRACKET = 30
    RIGHT_CURLY_BRACKET = 31
    ESCAPE = 32
    SIGN = 33
    LITERAL_INTEGER = 34
    LITERAL_FLOAT = 35
    LITERAL_BOOLEAN = 36
    LITERAL_STRING = 37
    IDENTIFER = 38
    DOLAR_IDENTIFIER = 39
    WHITE_SPACE = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
            "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'('", "')'", "'['", "']'", 
            "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", "K_ELSE", 
            "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", 
            "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", "K_VAL", "K_VAR", 
            "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", "K_BY", "LEFT_PAREN", 
            "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
            "DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
            "ESCAPE", "SIGN", "LITERAL_INTEGER", "LITERAL_FLOAT", "LITERAL_BOOLEAN", 
            "LITERAL_STRING", "IDENTIFER", "DOLAR_IDENTIFIER", "WHITE_SPACE" ]

    ruleNames = [ "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", 
                  "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", 
                  "K_BOOLEAN", "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", 
                  "K_VAL", "K_VAR", "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", 
                  "K_BY", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", 
                  "RIGHT_SQUARE_BRACKET", "DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", 
                  "RIGHT_CURLY_BRACKET", "SINGLE_QUOTE", "DOUBLE_QUOTE", 
                  "ESCAPE", "SIGN", "OCTAL_NOTATION", "HEXA_NOTATION", "BINARY_NOTATION", 
                  "HEXA_DIGIT", "OCTAL_DIGIT", "BINARY_DIGIT", "DECIMAL_DIGIT", 
                  "EXPONENT", "DECIMAL", "OCTAL", "HEXA", "BINARY", "LITERAL_INTEGER", 
                  "LITERAL_FLOAT", "LITERAL_BOOLEAN", "LITERAL_STRING", 
                  "IDENTIFER", "DOLAR_IDENTIFIER", "WHITE_SPACE" ]

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
            actions[47] = self.LITERAL_INTEGER_action 
            actions[48] = self.LITERAL_FLOAT_action 
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
     


