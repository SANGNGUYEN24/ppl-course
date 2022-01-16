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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u0223\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\7\2\u0094\n")
        buf.write("\2\f\2\16\2\u0097\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
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
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3%")
        buf.write("\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\5\63\u016b\n\63\3\64\3\64\3\65\3\65\3")
        buf.write("\66\3\66\3\66\3\66\5\66\u0175\n\66\3\67\3\67\3\67\3\67")
        buf.write("\5\67\u017b\n\67\38\38\39\39\3:\3:\3;\3;\3<\3<\5<\u0187")
        buf.write("\n<\3<\6<\u018a\n<\r<\16<\u018b\3=\3=\3=\5=\u0191\n=\3")
        buf.write("=\6=\u0194\n=\r=\16=\u0195\3=\3=\7=\u019a\n=\f=\16=\u019d")
        buf.write("\13=\3=\6=\u01a0\n=\r=\16=\u01a1\5=\u01a4\n=\3>\3>\6>")
        buf.write("\u01a8\n>\r>\16>\u01a9\3>\3>\7>\u01ae\n>\f>\16>\u01b1")
        buf.write("\13>\3>\6>\u01b4\n>\r>\16>\u01b5\3?\3?\6?\u01ba\n?\r?")
        buf.write("\16?\u01bb\3?\3?\7?\u01c0\n?\f?\16?\u01c3\13?\3?\6?\u01c6")
        buf.write("\n?\r?\16?\u01c7\3@\3@\6@\u01cc\n@\r@\16@\u01cd\3@\3@")
        buf.write("\7@\u01d2\n@\f@\16@\u01d5\13@\3@\6@\u01d8\n@\r@\16@\u01d9")
        buf.write("\3A\3A\3A\3A\5A\u01e0\nA\3A\3A\3B\3B\3B\5B\u01e7\nB\3")
        buf.write("B\5B\u01ea\nB\3B\3B\3B\3B\3B\5B\u01f1\nB\3B\3B\5B\u01f5")
        buf.write("\nB\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3C\5C\u0202\nC\3D\3")
        buf.write("D\3D\7D\u0207\nD\fD\16D\u020a\13D\3D\3D\3E\5E\u020f\n")
        buf.write("E\3E\7E\u0212\nE\fE\16E\u0215\13E\3F\3F\6F\u0219\nF\r")
        buf.write("F\16F\u021a\3G\6G\u021e\nG\rG\16G\u021f\3G\3G\4\u0095")
        buf.write("\u0208\2H\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\2c\2e\62g\63i\2k\2m")
        buf.write("\2o\2q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\64\u0083\65\u0085")
        buf.write("\66\u0087\67\u00898\u008b9\u008d:\3\2\r\4\2--//\5\2\62")
        buf.write(";CHch\3\2\629\3\2\62\63\3\2\62;\4\2GGgg\3\2\63;\4\2$$")
        buf.write("^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u023b")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2")
        buf.write("\2\5\u009d\3\2\2\2\7\u00a3\3\2\2\2\t\u00ac\3\2\2\2\13")
        buf.write("\u00af\3\2\2\2\r\u00b6\3\2\2\2\17\u00bb\3\2\2\2\21\u00c3")
        buf.write("\3\2\2\2\23\u00c9\3\2\2\2\25\u00cc\3\2\2\2\27\u00d0\3")
        buf.write("\2\2\2\31\u00d6\3\2\2\2\33\u00de\3\2\2\2\35\u00e5\3\2")
        buf.write("\2\2\37\u00ec\3\2\2\2!\u00f1\3\2\2\2#\u00f7\3\2\2\2%\u00fb")
        buf.write("\3\2\2\2\'\u00ff\3\2\2\2)\u010b\3\2\2\2+\u0116\3\2\2\2")
        buf.write("-\u011a\3\2\2\2/\u011d\3\2\2\2\61\u011f\3\2\2\2\63\u0122")
        buf.write("\3\2\2\2\65\u0125\3\2\2\2\67\u0128\3\2\2\29\u012b\3\2")
        buf.write("\2\2;\u012d\3\2\2\2=\u012f\3\2\2\2?\u0131\3\2\2\2A\u0133")
        buf.write("\3\2\2\2C\u0135\3\2\2\2E\u0137\3\2\2\2G\u013a\3\2\2\2")
        buf.write("I\u013c\3\2\2\2K\u013f\3\2\2\2M\u0142\3\2\2\2O\u0146\3")
        buf.write("\2\2\2Q\u0148\3\2\2\2S\u014a\3\2\2\2U\u014c\3\2\2\2W\u014e")
        buf.write("\3\2\2\2Y\u0150\3\2\2\2[\u0152\3\2\2\2]\u0154\3\2\2\2")
        buf.write("_\u0156\3\2\2\2a\u0158\3\2\2\2c\u015a\3\2\2\2e\u016a\3")
        buf.write("\2\2\2g\u016c\3\2\2\2i\u016e\3\2\2\2k\u0174\3\2\2\2m\u017a")
        buf.write("\3\2\2\2o\u017c\3\2\2\2q\u017e\3\2\2\2s\u0180\3\2\2\2")
        buf.write("u\u0182\3\2\2\2w\u0184\3\2\2\2y\u01a3\3\2\2\2{\u01a5\3")
        buf.write("\2\2\2}\u01b7\3\2\2\2\177\u01c9\3\2\2\2\u0081\u01df\3")
        buf.write("\2\2\2\u0083\u01f4\3\2\2\2\u0085\u0201\3\2\2\2\u0087\u0203")
        buf.write("\3\2\2\2\u0089\u020e\3\2\2\2\u008b\u0216\3\2\2\2\u008d")
        buf.write("\u021d\3\2\2\2\u008f\u0090\7%\2\2\u0090\u0091\7%\2\2\u0091")
        buf.write("\u0095\3\2\2\2\u0092\u0094\13\2\2\2\u0093\u0092\3\2\2")
        buf.write("\2\u0094\u0097\3\2\2\2\u0095\u0096\3\2\2\2\u0095\u0093")
        buf.write("\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0095\3\2\2\2\u0098")
        buf.write("\u0099\7%\2\2\u0099\u009a\7%\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u009c\b\2\2\2\u009c\4\3\2\2\2\u009d\u009e\7D\2\2\u009e")
        buf.write("\u009f\7t\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7c\2\2\u00a1")
        buf.write("\u00a2\7m\2\2\u00a2\6\3\2\2\2\u00a3\u00a4\7E\2\2\u00a4")
        buf.write("\u00a5\7q\2\2\u00a5\u00a6\7p\2\2\u00a6\u00a7\7v\2\2\u00a7")
        buf.write("\u00a8\7k\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7w\2\2\u00aa")
        buf.write("\u00ab\7g\2\2\u00ab\b\3\2\2\2\u00ac\u00ad\7K\2\2\u00ad")
        buf.write("\u00ae\7h\2\2\u00ae\n\3\2\2\2\u00af\u00b0\7G\2\2\u00b0")
        buf.write("\u00b1\7n\2\2\u00b1\u00b2\7u\2\2\u00b2\u00b3\7g\2\2\u00b3")
        buf.write("\u00b4\7k\2\2\u00b4\u00b5\7h\2\2\u00b5\f\3\2\2\2\u00b6")
        buf.write("\u00b7\7G\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7u\2\2\u00b9")
        buf.write("\u00ba\7g\2\2\u00ba\16\3\2\2\2\u00bb\u00bc\7H\2\2\u00bc")
        buf.write("\u00bd\7q\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7g\2\2\u00bf")
        buf.write("\u00c0\7c\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2\7j\2\2\u00c2")
        buf.write("\20\3\2\2\2\u00c3\u00c4\7C\2\2\u00c4\u00c5\7t\2\2\u00c5")
        buf.write("\u00c6\7t\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7{\2\2\u00c8")
        buf.write("\22\3\2\2\2\u00c9\u00ca\7K\2\2\u00ca\u00cb\7p\2\2\u00cb")
        buf.write("\24\3\2\2\2\u00cc\u00cd\7K\2\2\u00cd\u00ce\7p\2\2\u00ce")
        buf.write("\u00cf\7v\2\2\u00cf\26\3\2\2\2\u00d0\u00d1\7H\2\2\u00d1")
        buf.write("\u00d2\7n\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7c\2\2\u00d4")
        buf.write("\u00d5\7v\2\2\u00d5\30\3\2\2\2\u00d6\u00d7\7D\2\2\u00d7")
        buf.write("\u00d8\7q\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7n\2\2\u00da")
        buf.write("\u00db\7g\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd\7p\2\2\u00dd")
        buf.write("\32\3\2\2\2\u00de\u00df\7U\2\2\u00df\u00e0\7v\2\2\u00e0")
        buf.write("\u00e1\7t\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3")
        buf.write("\u00e4\7i\2\2\u00e4\34\3\2\2\2\u00e5\u00e6\7T\2\2\u00e6")
        buf.write("\u00e7\7g\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7w\2\2\u00e9")
        buf.write("\u00ea\7t\2\2\u00ea\u00eb\7p\2\2\u00eb\36\3\2\2\2\u00ec")
        buf.write("\u00ed\7P\2\2\u00ed\u00ee\7w\2\2\u00ee\u00ef\7n\2\2\u00ef")
        buf.write("\u00f0\7n\2\2\u00f0 \3\2\2\2\u00f1\u00f2\7E\2\2\u00f2")
        buf.write("\u00f3\7n\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5\7u\2\2\u00f5")
        buf.write("\u00f6\7u\2\2\u00f6\"\3\2\2\2\u00f7\u00f8\7X\2\2\u00f8")
        buf.write("\u00f9\7c\2\2\u00f9\u00fa\7n\2\2\u00fa$\3\2\2\2\u00fb")
        buf.write("\u00fc\7X\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe\7t\2\2\u00fe")
        buf.write("&\3\2\2\2\u00ff\u0100\7E\2\2\u0100\u0101\7q\2\2\u0101")
        buf.write("\u0102\7p\2\2\u0102\u0103\7u\2\2\u0103\u0104\7v\2\2\u0104")
        buf.write("\u0105\7t\2\2\u0105\u0106\7w\2\2\u0106\u0107\7e\2\2\u0107")
        buf.write("\u0108\7v\2\2\u0108\u0109\7q\2\2\u0109\u010a\7t\2\2\u010a")
        buf.write("(\3\2\2\2\u010b\u010c\7F\2\2\u010c\u010d\7g\2\2\u010d")
        buf.write("\u010e\7u\2\2\u010e\u010f\7v\2\2\u010f\u0110\7t\2\2\u0110")
        buf.write("\u0111\7w\2\2\u0111\u0112\7e\2\2\u0112\u0113\7v\2\2\u0113")
        buf.write("\u0114\7q\2\2\u0114\u0115\7t\2\2\u0115*\3\2\2\2\u0116")
        buf.write("\u0117\7P\2\2\u0117\u0118\7g\2\2\u0118\u0119\7y\2\2\u0119")
        buf.write(",\3\2\2\2\u011a\u011b\7D\2\2\u011b\u011c\7{\2\2\u011c")
        buf.write(".\3\2\2\2\u011d\u011e\7#\2\2\u011e\60\3\2\2\2\u011f\u0120")
        buf.write("\7~\2\2\u0120\u0121\7~\2\2\u0121\62\3\2\2\2\u0122\u0123")
        buf.write("\7(\2\2\u0123\u0124\7(\2\2\u0124\64\3\2\2\2\u0125\u0126")
        buf.write("\7?\2\2\u0126\u0127\7?\2\2\u0127\66\3\2\2\2\u0128\u0129")
        buf.write("\7#\2\2\u0129\u012a\7?\2\2\u012a8\3\2\2\2\u012b\u012c")
        buf.write("\7\'\2\2\u012c:\3\2\2\2\u012d\u012e\7-\2\2\u012e<\3\2")
        buf.write("\2\2\u012f\u0130\7/\2\2\u0130>\3\2\2\2\u0131\u0132\7,")
        buf.write("\2\2\u0132@\3\2\2\2\u0133\u0134\7\61\2\2\u0134B\3\2\2")
        buf.write("\2\u0135\u0136\7>\2\2\u0136D\3\2\2\2\u0137\u0138\7>\2")
        buf.write("\2\u0138\u0139\7?\2\2\u0139F\3\2\2\2\u013a\u013b\7@\2")
        buf.write("\2\u013bH\3\2\2\2\u013c\u013d\7@\2\2\u013d\u013e\7?\2")
        buf.write("\2\u013eJ\3\2\2\2\u013f\u0140\7-\2\2\u0140\u0141\7\60")
        buf.write("\2\2\u0141L\3\2\2\2\u0142\u0143\7?\2\2\u0143\u0144\7?")
        buf.write("\2\2\u0144\u0145\7\60\2\2\u0145N\3\2\2\2\u0146\u0147\7")
        buf.write("*\2\2\u0147P\3\2\2\2\u0148\u0149\7+\2\2\u0149R\3\2\2\2")
        buf.write("\u014a\u014b\7]\2\2\u014bT\3\2\2\2\u014c\u014d\7_\2\2")
        buf.write("\u014dV\3\2\2\2\u014e\u014f\7\60\2\2\u014fX\3\2\2\2\u0150")
        buf.write("\u0151\7.\2\2\u0151Z\3\2\2\2\u0152\u0153\7=\2\2\u0153")
        buf.write("\\\3\2\2\2\u0154\u0155\7}\2\2\u0155^\3\2\2\2\u0156\u0157")
        buf.write("\7\177\2\2\u0157`\3\2\2\2\u0158\u0159\7)\2\2\u0159b\3")
        buf.write("\2\2\2\u015a\u015b\7$\2\2\u015bd\3\2\2\2\u015c\u015d\7")
        buf.write(")\2\2\u015d\u016b\7$\2\2\u015e\u015f\7^\2\2\u015f\u016b")
        buf.write("\7d\2\2\u0160\u0161\7^\2\2\u0161\u016b\7h\2\2\u0162\u0163")
        buf.write("\7^\2\2\u0163\u016b\7t\2\2\u0164\u0165\7^\2\2\u0165\u016b")
        buf.write("\7p\2\2\u0166\u0167\7^\2\2\u0167\u016b\7v\2\2\u0168\u0169")
        buf.write("\7^\2\2\u0169\u016b\7^\2\2\u016a\u015c\3\2\2\2\u016a\u015e")
        buf.write("\3\2\2\2\u016a\u0160\3\2\2\2\u016a\u0162\3\2\2\2\u016a")
        buf.write("\u0164\3\2\2\2\u016a\u0166\3\2\2\2\u016a\u0168\3\2\2\2")
        buf.write("\u016bf\3\2\2\2\u016c\u016d\t\2\2\2\u016dh\3\2\2\2\u016e")
        buf.write("\u016f\7\62\2\2\u016fj\3\2\2\2\u0170\u0171\7\62\2\2\u0171")
        buf.write("\u0175\7z\2\2\u0172\u0173\7\62\2\2\u0173\u0175\7Z\2\2")
        buf.write("\u0174\u0170\3\2\2\2\u0174\u0172\3\2\2\2\u0175l\3\2\2")
        buf.write("\2\u0176\u0177\7\62\2\2\u0177\u017b\7d\2\2\u0178\u0179")
        buf.write("\7\62\2\2\u0179\u017b\7D\2\2\u017a\u0176\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017bn\3\2\2\2\u017c\u017d\t\3\2\2\u017d")
        buf.write("p\3\2\2\2\u017e\u017f\t\4\2\2\u017fr\3\2\2\2\u0180\u0181")
        buf.write("\t\5\2\2\u0181t\3\2\2\2\u0182\u0183\t\6\2\2\u0183v\3\2")
        buf.write("\2\2\u0184\u0186\t\7\2\2\u0185\u0187\t\2\2\2\u0186\u0185")
        buf.write("\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0189\3\2\2\2\u0188")
        buf.write("\u018a\5y=\2\u0189\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018cx\3\2\2\2\u018d")
        buf.write("\u01a4\5u;\2\u018e\u0190\t\b\2\2\u018f\u0191\7a\2\2\u0190")
        buf.write("\u018f\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u019b\3\2\2\2")
        buf.write("\u0192\u0194\5u;\2\u0193\u0192\3\2\2\2\u0194\u0195\3\2")
        buf.write("\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197\u0198\7a\2\2\u0198\u019a\3\2\2\2\u0199")
        buf.write("\u0193\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2")
        buf.write("\u019b\u019c\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3")
        buf.write("\2\2\2\u019e\u01a0\5u;\2\u019f\u019e\3\2\2\2\u01a0\u01a1")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a4\3\2\2\2\u01a3\u018d\3\2\2\2\u01a3\u018e\3\2\2\2")
        buf.write("\u01a4z\3\2\2\2\u01a5\u01af\5i\65\2\u01a6\u01a8\5q9\2")
        buf.write("\u01a7\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3")
        buf.write("\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac")
        buf.write("\7a\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01a7\3\2\2\2\u01ae")
        buf.write("\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2")
        buf.write("\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b4\5")
        buf.write("q9\2\u01b3\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b3")
        buf.write("\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6|\3\2\2\2\u01b7\u01c1")
        buf.write("\5k\66\2\u01b8\u01ba\5o8\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb")
        buf.write("\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01be\7a\2\2\u01be\u01c0\3\2\2\2")
        buf.write("\u01bf\u01b9\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3")
        buf.write("\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3\u01c1")
        buf.write("\3\2\2\2\u01c4\u01c6\5o8\2\u01c5\u01c4\3\2\2\2\u01c6\u01c7")
        buf.write("\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("~\3\2\2\2\u01c9\u01d3\5m\67\2\u01ca\u01cc\5s:\2\u01cb")
        buf.write("\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01cd\u01ce\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\7")
        buf.write("a\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01cb\3\2\2\2\u01d2\u01d5")
        buf.write("\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4")
        buf.write("\u01d7\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d8\5s:\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01d7\3\2\2\2")
        buf.write("\u01d9\u01da\3\2\2\2\u01da\u0080\3\2\2\2\u01db\u01e0\5")
        buf.write("y=\2\u01dc\u01e0\5{>\2\u01dd\u01e0\5}?\2\u01de\u01e0\5")
        buf.write("\177@\2\u01df\u01db\3\2\2\2\u01df\u01dc\3\2\2\2\u01df")
        buf.write("\u01dd\3\2\2\2\u01df\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1\u01e2\bA\3\2\u01e2\u0082\3\2\2\2\u01e3\u01e4\5")
        buf.write("y=\2\u01e4\u01e6\5W,\2\u01e5\u01e7\5y=\2\u01e6\u01e5\3")
        buf.write("\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e9\3\2\2\2\u01e8\u01ea")
        buf.write("\5w<\2\u01e9\u01e8\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01f5")
        buf.write("\3\2\2\2\u01eb\u01ec\5y=\2\u01ec\u01ed\5w<\2\u01ed\u01f5")
        buf.write("\3\2\2\2\u01ee\u01f0\5W,\2\u01ef\u01f1\5y=\2\u01f0\u01ef")
        buf.write("\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2")
        buf.write("\u01f3\5w<\2\u01f3\u01f5\3\2\2\2\u01f4\u01e3\3\2\2\2\u01f4")
        buf.write("\u01eb\3\2\2\2\u01f4\u01ee\3\2\2\2\u01f5\u01f6\3\2\2\2")
        buf.write("\u01f6\u01f7\bB\4\2\u01f7\u0084\3\2\2\2\u01f8\u01f9\7")
        buf.write("V\2\2\u01f9\u01fa\7t\2\2\u01fa\u01fb\7w\2\2\u01fb\u0202")
        buf.write("\7g\2\2\u01fc\u01fd\7H\2\2\u01fd\u01fe\7c\2\2\u01fe\u01ff")
        buf.write("\7n\2\2\u01ff\u0200\7u\2\2\u0200\u0202\7g\2\2\u0201\u01f8")
        buf.write("\3\2\2\2\u0201\u01fc\3\2\2\2\u0202\u0086\3\2\2\2\u0203")
        buf.write("\u0208\5c\62\2\u0204\u0207\5e\63\2\u0205\u0207\n\t\2\2")
        buf.write("\u0206\u0204\3\2\2\2\u0206\u0205\3\2\2\2\u0207\u020a\3")
        buf.write("\2\2\2\u0208\u0209\3\2\2\2\u0208\u0206\3\2\2\2\u0209\u020b")
        buf.write("\3\2\2\2\u020a\u0208\3\2\2\2\u020b\u020c\5c\62\2\u020c")
        buf.write("\u0088\3\2\2\2\u020d\u020f\t\n\2\2\u020e\u020d\3\2\2\2")
        buf.write("\u020f\u0213\3\2\2\2\u0210\u0212\t\13\2\2\u0211\u0210")
        buf.write("\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213")
        buf.write("\u0214\3\2\2\2\u0214\u008a\3\2\2\2\u0215\u0213\3\2\2\2")
        buf.write("\u0216\u0218\7&\2\2\u0217\u0219\t\13\2\2\u0218\u0217\3")
        buf.write("\2\2\2\u0219\u021a\3\2\2\2\u021a\u0218\3\2\2\2\u021a\u021b")
        buf.write("\3\2\2\2\u021b\u008c\3\2\2\2\u021c\u021e\t\f\2\2\u021d")
        buf.write("\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u021d\3\2\2\2")
        buf.write("\u021f\u0220\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u0222\b")
        buf.write("G\2\2\u0222\u008e\3\2\2\2%\2\u0095\u016a\u0174\u017a\u0186")
        buf.write("\u018b\u0190\u0195\u019b\u01a1\u01a3\u01a9\u01af\u01b5")
        buf.write("\u01bb\u01c1\u01c7\u01cd\u01d3\u01d9\u01df\u01e6\u01e9")
        buf.write("\u01f0\u01f4\u0201\u0206\u0208\u020e\u0211\u0213\u0218")
        buf.write("\u021a\u021f\5\b\2\2\3A\2\3B\3")
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
    OP_LOGICAL_NOT = 23
    OP_LOGICAL_OR = 24
    OP_LOGICAL_AND = 25
    OP_IS_EQUAL_TO = 26
    OP_NOT_EQUAL_TO = 27
    OP_MODULO = 28
    OP_ADDTION = 29
    OP_SUBTRACTION = 30
    OP_MULTIPLICATION = 31
    OP_DIVISION = 32
    OP_LESS_THAN = 33
    OP_LESS_THAN_EQUAL = 34
    OP_GREATER_THAN = 35
    OP_GREATER_THAN_EQUAL = 36
    OP_STRING_CONCATENATION = 37
    OP_TWO_SAME_STRING = 38
    LEFT_PAREN = 39
    RIGHT_PAREN = 40
    LEFT_SQUARE_BRACKET = 41
    RIGHT_SQUARE_BRACKET = 42
    DOT = 43
    COMMA = 44
    SEMICOLON = 45
    LEFT_CURLY_BRACKET = 46
    RIGHT_CURLY_BRACKET = 47
    ESCAPE = 48
    SIGN = 49
    LITERAL_INTEGER = 50
    LITERAL_FLOAT = 51
    LITERAL_BOOLEAN = 52
    LITERAL_STRING = 53
    IDENTIFER = 54
    DOLAR_IDENTIFIER = 55
    WHITE_SPACE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
            "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'!'", "'||'", "'&&'", "'=='", 
            "'!='", "'%'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", "'>'", 
            "'>='", "'+.'", "'==.'", "'('", "')'", "'['", "']'", "'.'", 
            "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", "K_ELSE", 
            "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", 
            "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", "K_VAL", "K_VAR", 
            "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", "K_BY", "OP_LOGICAL_NOT", 
            "OP_LOGICAL_OR", "OP_LOGICAL_AND", "OP_IS_EQUAL_TO", "OP_NOT_EQUAL_TO", 
            "OP_MODULO", "OP_ADDTION", "OP_SUBTRACTION", "OP_MULTIPLICATION", 
            "OP_DIVISION", "OP_LESS_THAN", "OP_LESS_THAN_EQUAL", "OP_GREATER_THAN", 
            "OP_GREATER_THAN_EQUAL", "OP_STRING_CONCATENATION", "OP_TWO_SAME_STRING", 
            "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
            "DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
            "ESCAPE", "SIGN", "LITERAL_INTEGER", "LITERAL_FLOAT", "LITERAL_BOOLEAN", 
            "LITERAL_STRING", "IDENTIFER", "DOLAR_IDENTIFIER", "WHITE_SPACE" ]

    ruleNames = [ "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", 
                  "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", 
                  "K_BOOLEAN", "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", 
                  "K_VAL", "K_VAR", "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", 
                  "K_BY", "OP_LOGICAL_NOT", "OP_LOGICAL_OR", "OP_LOGICAL_AND", 
                  "OP_IS_EQUAL_TO", "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", 
                  "OP_SUBTRACTION", "OP_MULTIPLICATION", "OP_DIVISION", 
                  "OP_LESS_THAN", "OP_LESS_THAN_EQUAL", "OP_GREATER_THAN", 
                  "OP_GREATER_THAN_EQUAL", "OP_STRING_CONCATENATION", "OP_TWO_SAME_STRING", 
                  "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                  "DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                  "SINGLE_QUOTE", "DOUBLE_QUOTE", "ESCAPE", "SIGN", "OCTAL_NOTATION", 
                  "HEXA_NOTATION", "BINARY_NOTATION", "HEXA_DIGIT", "OCTAL_DIGIT", 
                  "BINARY_DIGIT", "DECIMAL_DIGIT", "EXPONENT", "DECIMAL", 
                  "OCTAL", "HEXA", "BINARY", "LITERAL_INTEGER", "LITERAL_FLOAT", 
                  "LITERAL_BOOLEAN", "LITERAL_STRING", "IDENTIFER", "DOLAR_IDENTIFIER", 
                  "WHITE_SPACE" ]

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
            actions[63] = self.LITERAL_INTEGER_action 
            actions[64] = self.LITERAL_FLOAT_action 
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
     


