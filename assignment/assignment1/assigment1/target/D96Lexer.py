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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u0227\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\7\2\u0096")
        buf.write("\n\2\f\2\16\2\u0099\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0171\n\65\3")
        buf.write("\66\3\66\3\67\3\67\3\67\3\67\5\67\u0179\n\67\38\38\38")
        buf.write("\38\58\u017f\n8\39\39\3:\3:\3;\3;\3<\3<\3=\3=\5=\u018b")
        buf.write("\n=\3=\6=\u018e\n=\r=\16=\u018f\3>\3>\3>\5>\u0195\n>\3")
        buf.write(">\6>\u0198\n>\r>\16>\u0199\3>\3>\7>\u019e\n>\f>\16>\u01a1")
        buf.write("\13>\3>\6>\u01a4\n>\r>\16>\u01a5\5>\u01a8\n>\3?\3?\6?")
        buf.write("\u01ac\n?\r?\16?\u01ad\3?\3?\7?\u01b2\n?\f?\16?\u01b5")
        buf.write("\13?\3?\6?\u01b8\n?\r?\16?\u01b9\3@\3@\6@\u01be\n@\r@")
        buf.write("\16@\u01bf\3@\3@\7@\u01c4\n@\f@\16@\u01c7\13@\3@\6@\u01ca")
        buf.write("\n@\r@\16@\u01cb\3A\3A\6A\u01d0\nA\rA\16A\u01d1\3A\3A")
        buf.write("\7A\u01d6\nA\fA\16A\u01d9\13A\3A\6A\u01dc\nA\rA\16A\u01dd")
        buf.write("\3B\3B\3B\3B\5B\u01e4\nB\3B\3B\3C\3C\3C\5C\u01eb\nC\3")
        buf.write("C\5C\u01ee\nC\3C\3C\3C\3C\3C\5C\u01f5\nC\3C\3C\5C\u01f9")
        buf.write("\nC\3C\3C\3D\3D\3D\3D\3D\3D\3D\3D\3D\5D\u0206\nD\3E\3")
        buf.write("E\3E\7E\u020b\nE\fE\16E\u020e\13E\3E\3E\3F\5F\u0213\n")
        buf.write("F\3F\7F\u0216\nF\fF\16F\u0219\13F\3G\3G\6G\u021d\nG\r")
        buf.write("G\16G\u021e\3H\6H\u0222\nH\rH\16H\u0223\3H\3H\4\u0097")
        buf.write("\u020c\2I\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\2g\2i\64k\2")
        buf.write("m\2o\2q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\65\u0085")
        buf.write("\66\u0087\67\u00898\u008b9\u008d:\u008f;\3\2\r\5\2\62")
        buf.write(";CHch\3\2\629\3\2\62\63\3\2\62;\4\2GGgg\4\2--//\3\2\63")
        buf.write(";\4\2$$^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"")
        buf.write("\2\u023f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2i\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2")
        buf.write("\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\3\u0091\3\2\2\2\5\u009f\3\2\2\2\7\u00a5\3\2\2")
        buf.write("\2\t\u00ae\3\2\2\2\13\u00b1\3\2\2\2\r\u00b8\3\2\2\2\17")
        buf.write("\u00bd\3\2\2\2\21\u00c5\3\2\2\2\23\u00cb\3\2\2\2\25\u00ce")
        buf.write("\3\2\2\2\27\u00d2\3\2\2\2\31\u00d8\3\2\2\2\33\u00e0\3")
        buf.write("\2\2\2\35\u00e7\3\2\2\2\37\u00ee\3\2\2\2!\u00f3\3\2\2")
        buf.write("\2#\u00f9\3\2\2\2%\u00fd\3\2\2\2\'\u0101\3\2\2\2)\u010d")
        buf.write("\3\2\2\2+\u0118\3\2\2\2-\u011c\3\2\2\2/\u011f\3\2\2\2")
        buf.write("\61\u0121\3\2\2\2\63\u0123\3\2\2\2\65\u0126\3\2\2\2\67")
        buf.write("\u0129\3\2\2\29\u012c\3\2\2\2;\u012f\3\2\2\2=\u0131\3")
        buf.write("\2\2\2?\u0133\3\2\2\2A\u0135\3\2\2\2C\u0137\3\2\2\2E\u0139")
        buf.write("\3\2\2\2G\u013b\3\2\2\2I\u013e\3\2\2\2K\u0140\3\2\2\2")
        buf.write("M\u0143\3\2\2\2O\u0146\3\2\2\2Q\u014a\3\2\2\2S\u014c\3")
        buf.write("\2\2\2U\u014e\3\2\2\2W\u0150\3\2\2\2Y\u0152\3\2\2\2[\u0154")
        buf.write("\3\2\2\2]\u0156\3\2\2\2_\u0158\3\2\2\2a\u015a\3\2\2\2")
        buf.write("c\u015c\3\2\2\2e\u015e\3\2\2\2g\u0160\3\2\2\2i\u0170\3")
        buf.write("\2\2\2k\u0172\3\2\2\2m\u0178\3\2\2\2o\u017e\3\2\2\2q\u0180")
        buf.write("\3\2\2\2s\u0182\3\2\2\2u\u0184\3\2\2\2w\u0186\3\2\2\2")
        buf.write("y\u0188\3\2\2\2{\u01a7\3\2\2\2}\u01a9\3\2\2\2\177\u01bb")
        buf.write("\3\2\2\2\u0081\u01cd\3\2\2\2\u0083\u01e3\3\2\2\2\u0085")
        buf.write("\u01f8\3\2\2\2\u0087\u0205\3\2\2\2\u0089\u0207\3\2\2\2")
        buf.write("\u008b\u0212\3\2\2\2\u008d\u021a\3\2\2\2\u008f\u0221\3")
        buf.write("\2\2\2\u0091\u0092\7%\2\2\u0092\u0093\7%\2\2\u0093\u0097")
        buf.write("\3\2\2\2\u0094\u0096\13\2\2\2\u0095\u0094\3\2\2\2\u0096")
        buf.write("\u0099\3\2\2\2\u0097\u0098\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0098\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b\7")
        buf.write("%\2\2\u009b\u009c\7%\2\2\u009c\u009d\3\2\2\2\u009d\u009e")
        buf.write("\b\2\2\2\u009e\4\3\2\2\2\u009f\u00a0\7D\2\2\u00a0\u00a1")
        buf.write("\7t\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4")
        buf.write("\7m\2\2\u00a4\6\3\2\2\2\u00a5\u00a6\7E\2\2\u00a6\u00a7")
        buf.write("\7q\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa")
        buf.write("\7k\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7g\2\2\u00ad\b\3\2\2\2\u00ae\u00af\7K\2\2\u00af\u00b0")
        buf.write("\7h\2\2\u00b0\n\3\2\2\2\u00b1\u00b2\7G\2\2\u00b2\u00b3")
        buf.write("\7n\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6")
        buf.write("\7k\2\2\u00b6\u00b7\7h\2\2\u00b7\f\3\2\2\2\u00b8\u00b9")
        buf.write("\7G\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\16\3\2\2\2\u00bd\u00be\7H\2\2\u00be\u00bf")
        buf.write("\7q\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2")
        buf.write("\7c\2\2\u00c2\u00c3\7e\2\2\u00c3\u00c4\7j\2\2\u00c4\20")
        buf.write("\3\2\2\2\u00c5\u00c6\7C\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7{\2\2\u00ca\22")
        buf.write("\3\2\2\2\u00cb\u00cc\7K\2\2\u00cc\u00cd\7p\2\2\u00cd\24")
        buf.write("\3\2\2\2\u00ce\u00cf\7K\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1")
        buf.write("\7v\2\2\u00d1\26\3\2\2\2\u00d2\u00d3\7H\2\2\u00d3\u00d4")
        buf.write("\7n\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7")
        buf.write("\7v\2\2\u00d7\30\3\2\2\2\u00d8\u00d9\7D\2\2\u00d9\u00da")
        buf.write("\7q\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7p\2\2\u00df\32")
        buf.write("\3\2\2\2\u00e0\u00e1\7U\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3")
        buf.write("\7t\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6")
        buf.write("\7i\2\2\u00e6\34\3\2\2\2\u00e7\u00e8\7T\2\2\u00e8\u00e9")
        buf.write("\7g\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\u00ed\7p\2\2\u00ed\36\3\2\2\2\u00ee\u00ef")
        buf.write("\7P\2\2\u00ef\u00f0\7w\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2")
        buf.write("\7n\2\2\u00f2 \3\2\2\2\u00f3\u00f4\7E\2\2\u00f4\u00f5")
        buf.write("\7n\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7\7u\2\2\u00f7\u00f8")
        buf.write("\7u\2\2\u00f8\"\3\2\2\2\u00f9\u00fa\7X\2\2\u00fa\u00fb")
        buf.write("\7c\2\2\u00fb\u00fc\7n\2\2\u00fc$\3\2\2\2\u00fd\u00fe")
        buf.write("\7X\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7t\2\2\u0100&\3")
        buf.write("\2\2\2\u0101\u0102\7E\2\2\u0102\u0103\7q\2\2\u0103\u0104")
        buf.write("\7p\2\2\u0104\u0105\7u\2\2\u0105\u0106\7v\2\2\u0106\u0107")
        buf.write("\7t\2\2\u0107\u0108\7w\2\2\u0108\u0109\7e\2\2\u0109\u010a")
        buf.write("\7v\2\2\u010a\u010b\7q\2\2\u010b\u010c\7t\2\2\u010c(\3")
        buf.write("\2\2\2\u010d\u010e\7F\2\2\u010e\u010f\7g\2\2\u010f\u0110")
        buf.write("\7u\2\2\u0110\u0111\7v\2\2\u0111\u0112\7t\2\2\u0112\u0113")
        buf.write("\7w\2\2\u0113\u0114\7e\2\2\u0114\u0115\7v\2\2\u0115\u0116")
        buf.write("\7q\2\2\u0116\u0117\7t\2\2\u0117*\3\2\2\2\u0118\u0119")
        buf.write("\7P\2\2\u0119\u011a\7g\2\2\u011a\u011b\7y\2\2\u011b,\3")
        buf.write("\2\2\2\u011c\u011d\7D\2\2\u011d\u011e\7{\2\2\u011e.\3")
        buf.write("\2\2\2\u011f\u0120\7?\2\2\u0120\60\3\2\2\2\u0121\u0122")
        buf.write("\7#\2\2\u0122\62\3\2\2\2\u0123\u0124\7~\2\2\u0124\u0125")
        buf.write("\7~\2\2\u0125\64\3\2\2\2\u0126\u0127\7(\2\2\u0127\u0128")
        buf.write("\7(\2\2\u0128\66\3\2\2\2\u0129\u012a\7?\2\2\u012a\u012b")
        buf.write("\7?\2\2\u012b8\3\2\2\2\u012c\u012d\7#\2\2\u012d\u012e")
        buf.write("\7?\2\2\u012e:\3\2\2\2\u012f\u0130\7\'\2\2\u0130<\3\2")
        buf.write("\2\2\u0131\u0132\7-\2\2\u0132>\3\2\2\2\u0133\u0134\7/")
        buf.write("\2\2\u0134@\3\2\2\2\u0135\u0136\7,\2\2\u0136B\3\2\2\2")
        buf.write("\u0137\u0138\7\61\2\2\u0138D\3\2\2\2\u0139\u013a\7>\2")
        buf.write("\2\u013aF\3\2\2\2\u013b\u013c\7>\2\2\u013c\u013d\7?\2")
        buf.write("\2\u013dH\3\2\2\2\u013e\u013f\7@\2\2\u013fJ\3\2\2\2\u0140")
        buf.write("\u0141\7@\2\2\u0141\u0142\7?\2\2\u0142L\3\2\2\2\u0143")
        buf.write("\u0144\7-\2\2\u0144\u0145\7\60\2\2\u0145N\3\2\2\2\u0146")
        buf.write("\u0147\7?\2\2\u0147\u0148\7?\2\2\u0148\u0149\7\60\2\2")
        buf.write("\u0149P\3\2\2\2\u014a\u014b\7*\2\2\u014bR\3\2\2\2\u014c")
        buf.write("\u014d\7+\2\2\u014dT\3\2\2\2\u014e\u014f\7]\2\2\u014f")
        buf.write("V\3\2\2\2\u0150\u0151\7_\2\2\u0151X\3\2\2\2\u0152\u0153")
        buf.write("\7\60\2\2\u0153Z\3\2\2\2\u0154\u0155\7.\2\2\u0155\\\3")
        buf.write("\2\2\2\u0156\u0157\7<\2\2\u0157^\3\2\2\2\u0158\u0159\7")
        buf.write("=\2\2\u0159`\3\2\2\2\u015a\u015b\7}\2\2\u015bb\3\2\2\2")
        buf.write("\u015c\u015d\7\177\2\2\u015dd\3\2\2\2\u015e\u015f\7)\2")
        buf.write("\2\u015ff\3\2\2\2\u0160\u0161\7$\2\2\u0161h\3\2\2\2\u0162")
        buf.write("\u0163\7)\2\2\u0163\u0171\7$\2\2\u0164\u0165\7^\2\2\u0165")
        buf.write("\u0171\7d\2\2\u0166\u0167\7^\2\2\u0167\u0171\7h\2\2\u0168")
        buf.write("\u0169\7^\2\2\u0169\u0171\7t\2\2\u016a\u016b\7^\2\2\u016b")
        buf.write("\u0171\7p\2\2\u016c\u016d\7^\2\2\u016d\u0171\7v\2\2\u016e")
        buf.write("\u016f\7^\2\2\u016f\u0171\7^\2\2\u0170\u0162\3\2\2\2\u0170")
        buf.write("\u0164\3\2\2\2\u0170\u0166\3\2\2\2\u0170\u0168\3\2\2\2")
        buf.write("\u0170\u016a\3\2\2\2\u0170\u016c\3\2\2\2\u0170\u016e\3")
        buf.write("\2\2\2\u0171j\3\2\2\2\u0172\u0173\7\62\2\2\u0173l\3\2")
        buf.write("\2\2\u0174\u0175\7\62\2\2\u0175\u0179\7z\2\2\u0176\u0177")
        buf.write("\7\62\2\2\u0177\u0179\7Z\2\2\u0178\u0174\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0179n\3\2\2\2\u017a\u017b\7\62\2\2\u017b")
        buf.write("\u017f\7d\2\2\u017c\u017d\7\62\2\2\u017d\u017f\7D\2\2")
        buf.write("\u017e\u017a\3\2\2\2\u017e\u017c\3\2\2\2\u017fp\3\2\2")
        buf.write("\2\u0180\u0181\t\2\2\2\u0181r\3\2\2\2\u0182\u0183\t\3")
        buf.write("\2\2\u0183t\3\2\2\2\u0184\u0185\t\4\2\2\u0185v\3\2\2\2")
        buf.write("\u0186\u0187\t\5\2\2\u0187x\3\2\2\2\u0188\u018a\t\6\2")
        buf.write("\2\u0189\u018b\t\7\2\2\u018a\u0189\3\2\2\2\u018a\u018b")
        buf.write("\3\2\2\2\u018b\u018d\3\2\2\2\u018c\u018e\5{>\2\u018d\u018c")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190z\3\2\2\2\u0191\u01a8\5w<\2\u0192")
        buf.write("\u0194\t\b\2\2\u0193\u0195\7a\2\2\u0194\u0193\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195\u019f\3\2\2\2\u0196\u0198\5")
        buf.write("w<\2\u0197\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\3\2\2\2\u019b")
        buf.write("\u019c\7a\2\2\u019c\u019e\3\2\2\2\u019d\u0197\3\2\2\2")
        buf.write("\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3")
        buf.write("\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a4")
        buf.write("\5w<\2\u01a3\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a8\3\2\2\2\u01a7")
        buf.write("\u0191\3\2\2\2\u01a7\u0192\3\2\2\2\u01a8|\3\2\2\2\u01a9")
        buf.write("\u01b3\5k\66\2\u01aa\u01ac\5s:\2\u01ab\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ad\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01af\u01b0\7a\2\2\u01b0\u01b2\3")
        buf.write("\2\2\2\u01b1\u01ab\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b6\u01b8\5s:\2\u01b7\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2")
        buf.write("\u01ba~\3\2\2\2\u01bb\u01c5\5m\67\2\u01bc\u01be\5q9\2")
        buf.write("\u01bd\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01bd\3")
        buf.write("\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2")
        buf.write("\7a\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01bd\3\2\2\2\u01c4")
        buf.write("\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01ca\5")
        buf.write("q9\2\u01c9\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01c9")
        buf.write("\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u0080\3\2\2\2\u01cd")
        buf.write("\u01d7\5o8\2\u01ce\u01d0\5u;\2\u01cf\u01ce\3\2\2\2\u01d0")
        buf.write("\u01d1\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2")
        buf.write("\u01d2\u01d3\3\2\2\2\u01d3\u01d4\7a\2\2\u01d4\u01d6\3")
        buf.write("\2\2\2\u01d5\u01cf\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5")
        buf.write("\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9")
        buf.write("\u01d7\3\2\2\2\u01da\u01dc\5u;\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("\u01dd\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u0082\3\2\2\2\u01df\u01e4\5{>\2\u01e0\u01e4\5}")
        buf.write("?\2\u01e1\u01e4\5\177@\2\u01e2\u01e4\5\u0081A\2\u01e3")
        buf.write("\u01df\3\2\2\2\u01e3\u01e0\3\2\2\2\u01e3\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6\b")
        buf.write("B\3\2\u01e6\u0084\3\2\2\2\u01e7\u01e8\5{>\2\u01e8\u01ea")
        buf.write("\5Y-\2\u01e9\u01eb\5{>\2\u01ea\u01e9\3\2\2\2\u01ea\u01eb")
        buf.write("\3\2\2\2\u01eb\u01ed\3\2\2\2\u01ec\u01ee\5y=\2\u01ed\u01ec")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f9\3\2\2\2\u01ef")
        buf.write("\u01f0\5{>\2\u01f0\u01f1\5y=\2\u01f1\u01f9\3\2\2\2\u01f2")
        buf.write("\u01f4\5Y-\2\u01f3\u01f5\5{>\2\u01f4\u01f3\3\2\2\2\u01f4")
        buf.write("\u01f5\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7\5y=\2\u01f7")
        buf.write("\u01f9\3\2\2\2\u01f8\u01e7\3\2\2\2\u01f8\u01ef\3\2\2\2")
        buf.write("\u01f8\u01f2\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fb\b")
        buf.write("C\4\2\u01fb\u0086\3\2\2\2\u01fc\u01fd\7V\2\2\u01fd\u01fe")
        buf.write("\7t\2\2\u01fe\u01ff\7w\2\2\u01ff\u0206\7g\2\2\u0200\u0201")
        buf.write("\7H\2\2\u0201\u0202\7c\2\2\u0202\u0203\7n\2\2\u0203\u0204")
        buf.write("\7u\2\2\u0204\u0206\7g\2\2\u0205\u01fc\3\2\2\2\u0205\u0200")
        buf.write("\3\2\2\2\u0206\u0088\3\2\2\2\u0207\u020c\5g\64\2\u0208")
        buf.write("\u020b\5i\65\2\u0209\u020b\n\t\2\2\u020a\u0208\3\2\2\2")
        buf.write("\u020a\u0209\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020d\3")
        buf.write("\2\2\2\u020c\u020a\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u020c")
        buf.write("\3\2\2\2\u020f\u0210\5g\64\2\u0210\u008a\3\2\2\2\u0211")
        buf.write("\u0213\t\n\2\2\u0212\u0211\3\2\2\2\u0213\u0217\3\2\2\2")
        buf.write("\u0214\u0216\t\13\2\2\u0215\u0214\3\2\2\2\u0216\u0219")
        buf.write("\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218")
        buf.write("\u008c\3\2\2\2\u0219\u0217\3\2\2\2\u021a\u021c\7&\2\2")
        buf.write("\u021b\u021d\t\13\2\2\u021c\u021b\3\2\2\2\u021d\u021e")
        buf.write("\3\2\2\2\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f")
        buf.write("\u008e\3\2\2\2\u0220\u0222\t\f\2\2\u0221\u0220\3\2\2\2")
        buf.write("\u0222\u0223\3\2\2\2\u0223\u0221\3\2\2\2\u0223\u0224\3")
        buf.write("\2\2\2\u0224\u0225\3\2\2\2\u0225\u0226\bH\2\2\u0226\u0090")
        buf.write("\3\2\2\2%\2\u0097\u0170\u0178\u017e\u018a\u018f\u0194")
        buf.write("\u0199\u019f\u01a5\u01a7\u01ad\u01b3\u01b9\u01bf\u01c5")
        buf.write("\u01cb\u01d1\u01d7\u01dd\u01e3\u01ea\u01ed\u01f4\u01f8")
        buf.write("\u0205\u020a\u020c\u0212\u0215\u0217\u021c\u021e\u0223")
        buf.write("\5\b\2\2\3B\2\3C\3")
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
    OP_ASSIGN = 23
    OP_LOGICAL_NOT = 24
    OP_LOGICAL_OR = 25
    OP_LOGICAL_AND = 26
    OP_IS_EQUAL_TO = 27
    OP_NOT_EQUAL_TO = 28
    OP_MODULO = 29
    OP_ADDTION = 30
    OP_SUBTRACTION = 31
    OP_MULTIPLICATION = 32
    OP_DIVISION = 33
    OP_LESS_THAN = 34
    OP_LESS_THAN_EQUAL = 35
    OP_GREATER_THAN = 36
    OP_GREATER_THAN_EQUAL = 37
    OP_STRING_CONCATENATION = 38
    OP_TWO_SAME_STRING = 39
    LEFT_PAREN = 40
    RIGHT_PAREN = 41
    LEFT_SQUARE_BRACKET = 42
    RIGHT_SQUARE_BRACKET = 43
    DOT = 44
    COMMA = 45
    COLON = 46
    SEMICOLON = 47
    LEFT_CURLY_BRACKET = 48
    RIGHT_CURLY_BRACKET = 49
    ESCAPE = 50
    LITERAL_INTEGER = 51
    LITERAL_FLOAT = 52
    LITERAL_BOOLEAN = 53
    LITERAL_STRING = 54
    IDENTIFER = 55
    DOLAR_IDENTIFIER = 56
    WHITE_SPACE = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
            "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'='", "'!'", "'||'", "'&&'", 
            "'=='", "'!='", "'%'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", 
            "'>'", "'>='", "'+.'", "'==.'", "'('", "')'", "'['", "']'", 
            "'.'", "','", "':'", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", "K_ELSE", 
            "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", 
            "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", "K_VAL", "K_VAR", 
            "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", "K_BY", "OP_ASSIGN", 
            "OP_LOGICAL_NOT", "OP_LOGICAL_OR", "OP_LOGICAL_AND", "OP_IS_EQUAL_TO", 
            "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", "OP_SUBTRACTION", 
            "OP_MULTIPLICATION", "OP_DIVISION", "OP_LESS_THAN", "OP_LESS_THAN_EQUAL", 
            "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", "OP_STRING_CONCATENATION", 
            "OP_TWO_SAME_STRING", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", 
            "RIGHT_SQUARE_BRACKET", "DOT", "COMMA", "COLON", "SEMICOLON", 
            "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "ESCAPE", "LITERAL_INTEGER", 
            "LITERAL_FLOAT", "LITERAL_BOOLEAN", "LITERAL_STRING", "IDENTIFER", 
            "DOLAR_IDENTIFIER", "WHITE_SPACE" ]

    ruleNames = [ "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", 
                  "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", 
                  "K_BOOLEAN", "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", 
                  "K_VAL", "K_VAR", "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", 
                  "K_BY", "OP_ASSIGN", "OP_LOGICAL_NOT", "OP_LOGICAL_OR", 
                  "OP_LOGICAL_AND", "OP_IS_EQUAL_TO", "OP_NOT_EQUAL_TO", 
                  "OP_MODULO", "OP_ADDTION", "OP_SUBTRACTION", "OP_MULTIPLICATION", 
                  "OP_DIVISION", "OP_LESS_THAN", "OP_LESS_THAN_EQUAL", "OP_GREATER_THAN", 
                  "OP_GREATER_THAN_EQUAL", "OP_STRING_CONCATENATION", "OP_TWO_SAME_STRING", 
                  "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                  "DOT", "COMMA", "COLON", "SEMICOLON", "LEFT_CURLY_BRACKET", 
                  "RIGHT_CURLY_BRACKET", "SINGLE_QUOTE", "DOUBLE_QUOTE", 
                  "ESCAPE", "OCTAL_NOTATION", "HEXA_NOTATION", "BINARY_NOTATION", 
                  "HEXA_DIGIT", "OCTAL_DIGIT", "BINARY_DIGIT", "DECIMAL_DIGIT", 
                  "EXPONENT", "DECIMAL", "OCTAL", "HEXA", "BINARY", "LITERAL_INTEGER", 
                  "LITERAL_FLOAT", "LITERAL_BOOLEAN", "LITERAL_STRING", 
                  "IDENTIFER", "DOLAR_IDENTIFIER", "WHITE_SPACE" ]

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
            actions[64] = self.LITERAL_INTEGER_action 
            actions[65] = self.LITERAL_FLOAT_action 
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
     


