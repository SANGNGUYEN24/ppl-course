# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2-")
        buf.write("\u01ab\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\3\2\6\2o\n\2\r\2\16\2p\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\7\3y\n\3\f\3\16\3|\13\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\5\4\u0084\n\4\3\4\7\4\u0087\n\4\f\4\16\4")
        buf.write("\u008a\13\4\3\5\3\5\6\5\u008e\n\5\r\5\16\5\u008f\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\5&\u0136\n&\3\'\3\'\3(\3(\3(\3(\5")
        buf.write("(\u013e\n(\3)\3)\3)\3)\5)\u0144\n)\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\5.\u0150\n.\3.\6.\u0153\n.\r.\16.\u0154\3/")
        buf.write("\3/\3\60\3\60\3\60\3\60\7\60\u015d\n\60\f\60\16\60\u0160")
        buf.write("\13\60\3\60\5\60\u0163\n\60\3\61\3\61\6\61\u0167\n\61")
        buf.write("\r\61\16\61\u0168\3\62\3\62\6\62\u016d\n\62\r\62\16\62")
        buf.write("\u016e\3\63\3\63\6\63\u0173\n\63\r\63\16\63\u0174\3\64")
        buf.write("\6\64\u0178\n\64\r\64\16\64\u0179\3\64\3\64\7\64\u017e")
        buf.write("\n\64\f\64\16\64\u0181\13\64\3\64\5\64\u0184\n\64\3\64")
        buf.write("\6\64\u0187\n\64\r\64\16\64\u0188\3\64\5\64\u018c\n\64")
        buf.write("\3\64\3\64\6\64\u0190\n\64\r\64\16\64\u0191\3\64\5\64")
        buf.write("\u0195\n\64\5\64\u0197\n\64\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\5\65\u01a2\n\65\3\66\3\66\3\66\7\66")
        buf.write("\u01a7\n\66\f\66\16\66\u01aa\13\66\4z\u01a8\2\67\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G\2I\2K%M\2O\2Q\2")
        buf.write("S\2U\2W\2Y\2[\2]&_\'a(c)e*g+i,k-\3\2\r\5\2\13\f\17\17")
        buf.write("\"\"\5\2C\\aac|\6\2\62;C\\aac|\5\2\62;CHch\3\2\629\3\2")
        buf.write("\62\63\3\2\62;\4\2GGgg\4\2--//\3\2\63;\4\2$$^^\2\u01bf")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2K\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\3n\3\2\2\2\5t\3\2\2\2\7\u0083")
        buf.write("\3\2\2\2\t\u008b\3\2\2\2\13\u0091\3\2\2\2\r\u0097\3\2")
        buf.write("\2\2\17\u00a0\3\2\2\2\21\u00a3\3\2\2\2\23\u00aa\3\2\2")
        buf.write("\2\25\u00af\3\2\2\2\27\u00b7\3\2\2\2\31\u00bd\3\2\2\2")
        buf.write("\33\u00c0\3\2\2\2\35\u00c4\3\2\2\2\37\u00ca\3\2\2\2!\u00d2")
        buf.write("\3\2\2\2#\u00d9\3\2\2\2%\u00e0\3\2\2\2\'\u00e5\3\2\2\2")
        buf.write(")\u00eb\3\2\2\2+\u00ef\3\2\2\2-\u00f3\3\2\2\2/\u00ff\3")
        buf.write("\2\2\2\61\u010a\3\2\2\2\63\u010e\3\2\2\2\65\u0111\3\2")
        buf.write("\2\2\67\u0113\3\2\2\29\u0115\3\2\2\2;\u0117\3\2\2\2=\u0119")
        buf.write("\3\2\2\2?\u011b\3\2\2\2A\u011d\3\2\2\2C\u011f\3\2\2\2")
        buf.write("E\u0121\3\2\2\2G\u0123\3\2\2\2I\u0125\3\2\2\2K\u0135\3")
        buf.write("\2\2\2M\u0137\3\2\2\2O\u013d\3\2\2\2Q\u0143\3\2\2\2S\u0145")
        buf.write("\3\2\2\2U\u0147\3\2\2\2W\u0149\3\2\2\2Y\u014b\3\2\2\2")
        buf.write("[\u014d\3\2\2\2]\u0156\3\2\2\2_\u0162\3\2\2\2a\u0164\3")
        buf.write("\2\2\2c\u016a\3\2\2\2e\u0170\3\2\2\2g\u0196\3\2\2\2i\u01a1")
        buf.write("\3\2\2\2k\u01a3\3\2\2\2mo\t\2\2\2nm\3\2\2\2op\3\2\2\2")
        buf.write("pn\3\2\2\2pq\3\2\2\2qr\3\2\2\2rs\b\2\2\2s\4\3\2\2\2tu")
        buf.write("\7%\2\2uv\7%\2\2vz\3\2\2\2wy\13\2\2\2xw\3\2\2\2y|\3\2")
        buf.write("\2\2z{\3\2\2\2zx\3\2\2\2{}\3\2\2\2|z\3\2\2\2}~\7%\2\2")
        buf.write("~\177\7%\2\2\177\u0080\3\2\2\2\u0080\u0081\b\3\2\2\u0081")
        buf.write("\6\3\2\2\2\u0082\u0084\t\3\2\2\u0083\u0082\3\2\2\2\u0084")
        buf.write("\u0088\3\2\2\2\u0085\u0087\t\4\2\2\u0086\u0085\3\2\2\2")
        buf.write("\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3")
        buf.write("\2\2\2\u0089\b\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008d")
        buf.write("\7&\2\2\u008c\u008e\t\4\2\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\n\3\2\2\2\u0091\u0092\7D\2\2\u0092\u0093\7t\2\2")
        buf.write("\u0093\u0094\7g\2\2\u0094\u0095\7c\2\2\u0095\u0096\7m")
        buf.write("\2\2\u0096\f\3\2\2\2\u0097\u0098\7E\2\2\u0098\u0099\7")
        buf.write("q\2\2\u0099\u009a\7p\2\2\u009a\u009b\7v\2\2\u009b\u009c")
        buf.write("\7k\2\2\u009c\u009d\7p\2\2\u009d\u009e\7w\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\16\3\2\2\2\u00a0\u00a1\7K\2\2\u00a1\u00a2")
        buf.write("\7h\2\2\u00a2\20\3\2\2\2\u00a3\u00a4\7G\2\2\u00a4\u00a5")
        buf.write("\7n\2\2\u00a5\u00a6\7u\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8")
        buf.write("\7k\2\2\u00a8\u00a9\7h\2\2\u00a9\22\3\2\2\2\u00aa\u00ab")
        buf.write("\7G\2\2\u00ab\u00ac\7n\2\2\u00ac\u00ad\7u\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\24\3\2\2\2\u00af\u00b0\7H\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4")
        buf.write("\7c\2\2\u00b4\u00b5\7e\2\2\u00b5\u00b6\7j\2\2\u00b6\26")
        buf.write("\3\2\2\2\u00b7\u00b8\7C\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7{\2\2\u00bc\30")
        buf.write("\3\2\2\2\u00bd\u00be\7K\2\2\u00be\u00bf\7p\2\2\u00bf\32")
        buf.write("\3\2\2\2\u00c0\u00c1\7K\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3")
        buf.write("\7v\2\2\u00c3\34\3\2\2\2\u00c4\u00c5\7H\2\2\u00c5\u00c6")
        buf.write("\7n\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\36\3\2\2\2\u00ca\u00cb\7D\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7n\2\2\u00ce\u00cf")
        buf.write("\7g\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7p\2\2\u00d1 \3")
        buf.write("\2\2\2\u00d2\u00d3\7U\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7t\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8")
        buf.write("\7i\2\2\u00d8\"\3\2\2\2\u00d9\u00da\7T\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7w\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de\u00df\7p\2\2\u00df$\3\2\2\2\u00e0\u00e1")
        buf.write("\7P\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4")
        buf.write("\7n\2\2\u00e4&\3\2\2\2\u00e5\u00e6\7E\2\2\u00e6\u00e7")
        buf.write("\7n\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea")
        buf.write("\7u\2\2\u00ea(\3\2\2\2\u00eb\u00ec\7X\2\2\u00ec\u00ed")
        buf.write("\7c\2\2\u00ed\u00ee\7n\2\2\u00ee*\3\2\2\2\u00ef\u00f0")
        buf.write("\7X\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7t\2\2\u00f2,\3")
        buf.write("\2\2\2\u00f3\u00f4\7E\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6\u00f7\7u\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9")
        buf.write("\7t\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc")
        buf.write("\7v\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe\7t\2\2\u00fe.\3")
        buf.write("\2\2\2\u00ff\u0100\7F\2\2\u0100\u0101\7g\2\2\u0101\u0102")
        buf.write("\7u\2\2\u0102\u0103\7v\2\2\u0103\u0104\7t\2\2\u0104\u0105")
        buf.write("\7w\2\2\u0105\u0106\7e\2\2\u0106\u0107\7v\2\2\u0107\u0108")
        buf.write("\7q\2\2\u0108\u0109\7t\2\2\u0109\60\3\2\2\2\u010a\u010b")
        buf.write("\7P\2\2\u010b\u010c\7g\2\2\u010c\u010d\7y\2\2\u010d\62")
        buf.write("\3\2\2\2\u010e\u010f\7D\2\2\u010f\u0110\7{\2\2\u0110\64")
        buf.write("\3\2\2\2\u0111\u0112\7*\2\2\u0112\66\3\2\2\2\u0113\u0114")
        buf.write("\7+\2\2\u01148\3\2\2\2\u0115\u0116\7]\2\2\u0116:\3\2\2")
        buf.write("\2\u0117\u0118\7_\2\2\u0118<\3\2\2\2\u0119\u011a\7\60")
        buf.write("\2\2\u011a>\3\2\2\2\u011b\u011c\7.\2\2\u011c@\3\2\2\2")
        buf.write("\u011d\u011e\7=\2\2\u011eB\3\2\2\2\u011f\u0120\7}\2\2")
        buf.write("\u0120D\3\2\2\2\u0121\u0122\7\177\2\2\u0122F\3\2\2\2\u0123")
        buf.write("\u0124\7)\2\2\u0124H\3\2\2\2\u0125\u0126\7$\2\2\u0126")
        buf.write("J\3\2\2\2\u0127\u0128\7)\2\2\u0128\u0136\7$\2\2\u0129")
        buf.write("\u012a\7^\2\2\u012a\u0136\7d\2\2\u012b\u012c\7^\2\2\u012c")
        buf.write("\u0136\7h\2\2\u012d\u012e\7^\2\2\u012e\u0136\7t\2\2\u012f")
        buf.write("\u0130\7^\2\2\u0130\u0136\7p\2\2\u0131\u0132\7^\2\2\u0132")
        buf.write("\u0136\7v\2\2\u0133\u0134\7^\2\2\u0134\u0136\7^\2\2\u0135")
        buf.write("\u0127\3\2\2\2\u0135\u0129\3\2\2\2\u0135\u012b\3\2\2\2")
        buf.write("\u0135\u012d\3\2\2\2\u0135\u012f\3\2\2\2\u0135\u0131\3")
        buf.write("\2\2\2\u0135\u0133\3\2\2\2\u0136L\3\2\2\2\u0137\u0138")
        buf.write("\7\62\2\2\u0138N\3\2\2\2\u0139\u013a\7\62\2\2\u013a\u013e")
        buf.write("\7z\2\2\u013b\u013c\7\62\2\2\u013c\u013e\7Z\2\2\u013d")
        buf.write("\u0139\3\2\2\2\u013d\u013b\3\2\2\2\u013eP\3\2\2\2\u013f")
        buf.write("\u0140\7\62\2\2\u0140\u0144\7d\2\2\u0141\u0142\7\62\2")
        buf.write("\2\u0142\u0144\7D\2\2\u0143\u013f\3\2\2\2\u0143\u0141")
        buf.write("\3\2\2\2\u0144R\3\2\2\2\u0145\u0146\t\5\2\2\u0146T\3\2")
        buf.write("\2\2\u0147\u0148\t\6\2\2\u0148V\3\2\2\2\u0149\u014a\t")
        buf.write("\7\2\2\u014aX\3\2\2\2\u014b\u014c\t\b\2\2\u014cZ\3\2\2")
        buf.write("\2\u014d\u014f\t\t\2\2\u014e\u0150\t\n\2\2\u014f\u014e")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0152\3\2\2\2\u0151")
        buf.write("\u0153\5_\60\2\u0152\u0151\3\2\2\2\u0153\u0154\3\2\2\2")
        buf.write("\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\\\3\2\2")
        buf.write("\2\u0156\u0157\t\n\2\2\u0157^\3\2\2\2\u0158\u0163\5Y-")
        buf.write("\2\u0159\u015e\t\13\2\2\u015a\u015d\5Y-\2\u015b\u015d")
        buf.write("\7a\2\2\u015c\u015a\3\2\2\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f\u0161\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0163\b")
        buf.write("\60\3\2\u0162\u0158\3\2\2\2\u0162\u0159\3\2\2\2\u0163")
        buf.write("`\3\2\2\2\u0164\u0166\5M\'\2\u0165\u0167\5U+\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0166\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169b\3\2\2\2\u016a\u016c\5O(\2\u016b")
        buf.write("\u016d\5S*\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016fd\3\2\2\2\u0170")
        buf.write("\u0172\5Q)\2\u0171\u0173\5W,\2\u0172\u0171\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175f\3\2\2\2\u0176\u0178\5_\60\2\u0177\u0176\3\2\2")
        buf.write("\2\u0178\u0179\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017f\5=\37\2\u017c")
        buf.write("\u017e\5_\60\2\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2")
        buf.write("\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0183\3")
        buf.write("\2\2\2\u0181\u017f\3\2\2\2\u0182\u0184\5[.\2\u0183\u0182")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0197\3\2\2\2\u0185")
        buf.write("\u0187\t\13\2\2\u0186\u0185\3\2\2\2\u0187\u0188\3\2\2")
        buf.write("\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018b")
        buf.write("\3\2\2\2\u018a\u018c\5[.\2\u018b\u018a\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018f\5=\37\2\u018e")
        buf.write("\u0190\5_\60\2\u018f\u018e\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0194\3")
        buf.write("\2\2\2\u0193\u0195\5[.\2\u0194\u0193\3\2\2\2\u0194\u0195")
        buf.write("\3\2\2\2\u0195\u0197\3\2\2\2\u0196\u0177\3\2\2\2\u0196")
        buf.write("\u0186\3\2\2\2\u0197h\3\2\2\2\u0198\u0199\7V\2\2\u0199")
        buf.write("\u019a\7t\2\2\u019a\u019b\7w\2\2\u019b\u01a2\7g\2\2\u019c")
        buf.write("\u019d\7H\2\2\u019d\u019e\7c\2\2\u019e\u019f\7n\2\2\u019f")
        buf.write("\u01a0\7u\2\2\u01a0\u01a2\7g\2\2\u01a1\u0198\3\2\2\2\u01a1")
        buf.write("\u019c\3\2\2\2\u01a2j\3\2\2\2\u01a3\u01a8\5I%\2\u01a4")
        buf.write("\u01a7\5K&\2\u01a5\u01a7\n\f\2\2\u01a6\u01a4\3\2\2\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a8\u01a6\3\2\2\2\u01a9l\3\2\2\2\u01aa\u01a8\3\2\2")
        buf.write("\2 \2pz\u0083\u0086\u0088\u008d\u008f\u0135\u013d\u0143")
        buf.write("\u014f\u0154\u015c\u015e\u0162\u0168\u016e\u0174\u0179")
        buf.write("\u017f\u0183\u0188\u018b\u0191\u0194\u0196\u01a1\u01a6")
        buf.write("\u01a8\4\b\2\2\3\60\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WHITE_SPACE = 1
    COMMENT = 2
    IDENTIFER = 3
    DOLAR_IDENTIFIER = 4
    K_BREAK = 5
    K_CONTINUE = 6
    K_IF = 7
    K_ELSE_IF = 8
    K_ELSE = 9
    K_FOR_EACH = 10
    K_ARRAY = 11
    K_IN = 12
    K_INT = 13
    K_FLOAT = 14
    K_BOOLEAN = 15
    K_STRING = 16
    K_RETURN = 17
    K_NULL = 18
    K_CLASS = 19
    K_VAL = 20
    K_VAR = 21
    K_CONSTRUCTOR = 22
    K_DESTRUCTOR = 23
    K_NEW = 24
    K_BY = 25
    LEFT_PAREN = 26
    RIGHT_PAREN = 27
    LEFT_SQUARE_BRACKET = 28
    RIGHT_SQUARE_BRACKET = 29
    DOT = 30
    COMMA = 31
    SEMICOLON = 32
    LEFT_CURLY_BRACKET = 33
    RIGHT_CURLY_BRACKET = 34
    ESCAPE = 35
    SIGN = 36
    LITERAL_INTEGER = 37
    LITERAL_OCTAL = 38
    LITERAL_HEXA = 39
    LITERAL_BINARY = 40
    LITERAL_FLOAT = 41
    LITERAL_BOOLEAN = 42
    LITERAL_STRING = 43

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
            "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'('", "')'", "'['", "']'", 
            "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "WHITE_SPACE", "COMMENT", "IDENTIFER", "DOLAR_IDENTIFIER", "K_BREAK", 
            "K_CONTINUE", "K_IF", "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", "K_ARRAY", 
            "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", "K_RETURN", 
            "K_NULL", "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", "K_DESTRUCTOR", 
            "K_NEW", "K_BY", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", 
            "RIGHT_SQUARE_BRACKET", "DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", 
            "RIGHT_CURLY_BRACKET", "ESCAPE", "SIGN", "LITERAL_INTEGER", 
            "LITERAL_OCTAL", "LITERAL_HEXA", "LITERAL_BINARY", "LITERAL_FLOAT", 
            "LITERAL_BOOLEAN", "LITERAL_STRING" ]

    ruleNames = [ "WHITE_SPACE", "COMMENT", "IDENTIFER", "DOLAR_IDENTIFIER", 
                  "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", "K_ELSE", 
                  "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", 
                  "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", "K_VAL", 
                  "K_VAR", "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", "K_BY", 
                  "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                  "DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                  "SINGLE_QUOTE", "DOUBLE_QUOTE", "ESCAPE", "OCTAL_NOTATION", 
                  "HEXA_NOTATION", "BINARY_NOTATION", "HEXA_DIGIT", "OCTAL_DIGIT", 
                  "BINARY_DIGIT", "DECIMAL_DIGIT", "EXPONENT", "SIGN", "LITERAL_INTEGER", 
                  "LITERAL_OCTAL", "LITERAL_HEXA", "LITERAL_BINARY", "LITERAL_FLOAT", 
                  "LITERAL_BOOLEAN", "LITERAL_STRING" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[46] = self.LITERAL_INTEGER_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def LITERAL_INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     


