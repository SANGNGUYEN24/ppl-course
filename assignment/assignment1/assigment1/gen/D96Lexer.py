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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0269\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\7\7\u00d3\n\7\f\7\16\7\u00d6\13\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;")
        buf.write("\3;\3;\3;\3;\5;\u01b3\n;\3<\3<\3=\3=\3=\3=\5=\u01bb\n")
        buf.write("=\3>\3>\3>\3>\5>\u01c1\n>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3")
        buf.write("C\5C\u01cd\nC\3C\6C\u01d0\nC\rC\16C\u01d1\3D\3D\3D\5D")
        buf.write("\u01d7\nD\3D\6D\u01da\nD\rD\16D\u01db\3D\3D\7D\u01e0\n")
        buf.write("D\fD\16D\u01e3\13D\3D\6D\u01e6\nD\rD\16D\u01e7\5D\u01ea")
        buf.write("\nD\3E\3E\6E\u01ee\nE\rE\16E\u01ef\3E\3E\7E\u01f4\nE\f")
        buf.write("E\16E\u01f7\13E\3E\6E\u01fa\nE\rE\16E\u01fb\3F\3F\6F\u0200")
        buf.write("\nF\rF\16F\u0201\3F\3F\7F\u0206\nF\fF\16F\u0209\13F\3")
        buf.write("F\6F\u020c\nF\rF\16F\u020d\3G\3G\6G\u0212\nG\rG\16G\u0213")
        buf.write("\3G\3G\7G\u0218\nG\fG\16G\u021b\13G\3G\6G\u021e\nG\rG")
        buf.write("\16G\u021f\3H\3H\3H\3H\5H\u0226\nH\3H\3H\3I\3I\3I\5I\u022d")
        buf.write("\nI\3I\5I\u0230\nI\3I\3I\3I\3I\3I\5I\u0237\nI\3I\3I\5")
        buf.write("I\u023b\nI\3I\3I\3J\3J\3J\3J\3J\3J\3J\3J\3J\5J\u0248\n")
        buf.write("J\3K\3K\3K\7K\u024d\nK\fK\16K\u0250\13K\3K\3K\3L\5L\u0255")
        buf.write("\nL\3L\7L\u0258\nL\fL\16L\u025b\13L\3M\3M\6M\u025f\nM")
        buf.write("\rM\16M\u0260\3N\6N\u0264\nN\rN\16N\u0265\3N\3N\4\u00d4")
        buf.write("\u024e\2O\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q\2s\2u:w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085")
        buf.write("\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f;\u0091<\u0093")
        buf.write("=\u0095>\u0097?\u0099@\u009bA\3\2\r\5\2\62;CHch\3\2\62")
        buf.write("9\3\2\62\63\3\2\62;\4\2GGgg\4\2--//\3\2\63;\4\2$$^^\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u0281\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2u")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\3\u009d\3\2\2\2\5\u00a5\3\2\2\2\7\u00b1\3\2\2")
        buf.write("\2\t\u00bb\3\2\2\2\13\u00c0\3\2\2\2\r\u00ce\3\2\2\2\17")
        buf.write("\u00dc\3\2\2\2\21\u00e2\3\2\2\2\23\u00eb\3\2\2\2\25\u00ee")
        buf.write("\3\2\2\2\27\u00f5\3\2\2\2\31\u00fa\3\2\2\2\33\u0102\3")
        buf.write("\2\2\2\35\u0108\3\2\2\2\37\u010b\3\2\2\2!\u010f\3\2\2")
        buf.write("\2#\u0115\3\2\2\2%\u011d\3\2\2\2\'\u0124\3\2\2\2)\u012b")
        buf.write("\3\2\2\2+\u0130\3\2\2\2-\u0136\3\2\2\2/\u013a\3\2\2\2")
        buf.write("\61\u013e\3\2\2\2\63\u014a\3\2\2\2\65\u0155\3\2\2\2\67")
        buf.write("\u0159\3\2\2\29\u015c\3\2\2\2;\u0161\3\2\2\2=\u0163\3")
        buf.write("\2\2\2?\u0165\3\2\2\2A\u0168\3\2\2\2C\u016b\3\2\2\2E\u016e")
        buf.write("\3\2\2\2G\u0171\3\2\2\2I\u0173\3\2\2\2K\u0175\3\2\2\2")
        buf.write("M\u0177\3\2\2\2O\u0179\3\2\2\2Q\u017b\3\2\2\2S\u017d\3")
        buf.write("\2\2\2U\u0180\3\2\2\2W\u0182\3\2\2\2Y\u0185\3\2\2\2[\u0188")
        buf.write("\3\2\2\2]\u018c\3\2\2\2_\u018e\3\2\2\2a\u0190\3\2\2\2")
        buf.write("c\u0192\3\2\2\2e\u0194\3\2\2\2g\u0196\3\2\2\2i\u0198\3")
        buf.write("\2\2\2k\u019a\3\2\2\2m\u019c\3\2\2\2o\u019e\3\2\2\2q\u01a0")
        buf.write("\3\2\2\2s\u01a2\3\2\2\2u\u01b2\3\2\2\2w\u01b4\3\2\2\2")
        buf.write("y\u01ba\3\2\2\2{\u01c0\3\2\2\2}\u01c2\3\2\2\2\177\u01c4")
        buf.write("\3\2\2\2\u0081\u01c6\3\2\2\2\u0083\u01c8\3\2\2\2\u0085")
        buf.write("\u01ca\3\2\2\2\u0087\u01e9\3\2\2\2\u0089\u01eb\3\2\2\2")
        buf.write("\u008b\u01fd\3\2\2\2\u008d\u020f\3\2\2\2\u008f\u0225\3")
        buf.write("\2\2\2\u0091\u023a\3\2\2\2\u0093\u0247\3\2\2\2\u0095\u0249")
        buf.write("\3\2\2\2\u0097\u0254\3\2\2\2\u0099\u025c\3\2\2\2\u009b")
        buf.write("\u0263\3\2\2\2\u009d\u009e\7R\2\2\u009e\u009f\7t\2\2\u009f")
        buf.write("\u00a0\7q\2\2\u00a0\u00a1\7i\2\2\u00a1\u00a2\7t\2\2\u00a2")
        buf.write("\u00a3\7c\2\2\u00a3\u00a4\7o\2\2\u00a4\4\3\2\2\2\u00a5")
        buf.write("\u00a6\7o\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7v\2\2\u00a8")
        buf.write("\u00a9\7j\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7f\2\2\u00ab")
        buf.write("\u00ac\7\"\2\2\u00ac\u00ad\7d\2\2\u00ad\u00ae\7q\2\2\u00ae")
        buf.write("\u00af\7f\2\2\u00af\u00b0\7{\2\2\u00b0\6\3\2\2\2\u00b1")
        buf.write("\u00b2\7u\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7c\2\2\u00b4")
        buf.write("\u00b5\7v\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7o\2\2\u00b7")
        buf.write("\u00b8\7g\2\2\u00b8\u00b9\7p\2\2\u00b9\u00ba\7v\2\2\u00ba")
        buf.write("\b\3\2\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7z\2\2\u00bd")
        buf.write("\u00be\7r\2\2\u00be\u00bf\7t\2\2\u00bf\n\3\2\2\2\u00c0")
        buf.write("\u00c1\7h\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3\7p\2\2\u00c3")
        buf.write("\u00c4\7e\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6\7k\2\2\u00c6")
        buf.write("\u00c7\7q\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7\"\2\2\u00c9")
        buf.write("\u00ca\7e\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7n\2\2\u00cc")
        buf.write("\u00cd\7n\2\2\u00cd\f\3\2\2\2\u00ce\u00cf\7%\2\2\u00cf")
        buf.write("\u00d0\7%\2\2\u00d0\u00d4\3\2\2\2\u00d1\u00d3\13\2\2\2")
        buf.write("\u00d2\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d5\3")
        buf.write("\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d7\u00d8\7%\2\2\u00d8\u00d9\7%\2\2\u00d9\u00da")
        buf.write("\3\2\2\2\u00da\u00db\b\7\2\2\u00db\16\3\2\2\2\u00dc\u00dd")
        buf.write("\7D\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7c\2\2\u00e0\u00e1\7m\2\2\u00e1\20\3\2\2\2\u00e2\u00e3")
        buf.write("\7E\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7w\2\2\u00e9\u00ea\7g\2\2\u00ea\22\3\2\2\2\u00eb\u00ec")
        buf.write("\7K\2\2\u00ec\u00ed\7h\2\2\u00ed\24\3\2\2\2\u00ee\u00ef")
        buf.write("\7G\2\2\u00ef\u00f0\7n\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4\7h\2\2\u00f4\26")
        buf.write("\3\2\2\2\u00f5\u00f6\7G\2\2\u00f6\u00f7\7n\2\2\u00f7\u00f8")
        buf.write("\7u\2\2\u00f8\u00f9\7g\2\2\u00f9\30\3\2\2\2\u00fa\u00fb")
        buf.write("\7H\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe")
        buf.write("\7g\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7e\2\2\u0100\u0101")
        buf.write("\7j\2\2\u0101\32\3\2\2\2\u0102\u0103\7C\2\2\u0103\u0104")
        buf.write("\7t\2\2\u0104\u0105\7t\2\2\u0105\u0106\7c\2\2\u0106\u0107")
        buf.write("\7{\2\2\u0107\34\3\2\2\2\u0108\u0109\7K\2\2\u0109\u010a")
        buf.write("\7p\2\2\u010a\36\3\2\2\2\u010b\u010c\7K\2\2\u010c\u010d")
        buf.write("\7p\2\2\u010d\u010e\7v\2\2\u010e \3\2\2\2\u010f\u0110")
        buf.write("\7H\2\2\u0110\u0111\7n\2\2\u0111\u0112\7q\2\2\u0112\u0113")
        buf.write("\7c\2\2\u0113\u0114\7v\2\2\u0114\"\3\2\2\2\u0115\u0116")
        buf.write("\7D\2\2\u0116\u0117\7q\2\2\u0117\u0118\7q\2\2\u0118\u0119")
        buf.write("\7n\2\2\u0119\u011a\7g\2\2\u011a\u011b\7c\2\2\u011b\u011c")
        buf.write("\7p\2\2\u011c$\3\2\2\2\u011d\u011e\7U\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\u0120\7t\2\2\u0120\u0121\7k\2\2\u0121\u0122")
        buf.write("\7p\2\2\u0122\u0123\7i\2\2\u0123&\3\2\2\2\u0124\u0125")
        buf.write("\7T\2\2\u0125\u0126\7g\2\2\u0126\u0127\7v\2\2\u0127\u0128")
        buf.write("\7w\2\2\u0128\u0129\7t\2\2\u0129\u012a\7p\2\2\u012a(\3")
        buf.write("\2\2\2\u012b\u012c\7P\2\2\u012c\u012d\7w\2\2\u012d\u012e")
        buf.write("\7n\2\2\u012e\u012f\7n\2\2\u012f*\3\2\2\2\u0130\u0131")
        buf.write("\7E\2\2\u0131\u0132\7n\2\2\u0132\u0133\7c\2\2\u0133\u0134")
        buf.write("\7u\2\2\u0134\u0135\7u\2\2\u0135,\3\2\2\2\u0136\u0137")
        buf.write("\7X\2\2\u0137\u0138\7c\2\2\u0138\u0139\7n\2\2\u0139.\3")
        buf.write("\2\2\2\u013a\u013b\7X\2\2\u013b\u013c\7c\2\2\u013c\u013d")
        buf.write("\7t\2\2\u013d\60\3\2\2\2\u013e\u013f\7E\2\2\u013f\u0140")
        buf.write("\7q\2\2\u0140\u0141\7p\2\2\u0141\u0142\7u\2\2\u0142\u0143")
        buf.write("\7v\2\2\u0143\u0144\7t\2\2\u0144\u0145\7w\2\2\u0145\u0146")
        buf.write("\7e\2\2\u0146\u0147\7v\2\2\u0147\u0148\7q\2\2\u0148\u0149")
        buf.write("\7t\2\2\u0149\62\3\2\2\2\u014a\u014b\7F\2\2\u014b\u014c")
        buf.write("\7g\2\2\u014c\u014d\7u\2\2\u014d\u014e\7v\2\2\u014e\u014f")
        buf.write("\7t\2\2\u014f\u0150\7w\2\2\u0150\u0151\7e\2\2\u0151\u0152")
        buf.write("\7v\2\2\u0152\u0153\7q\2\2\u0153\u0154\7t\2\2\u0154\64")
        buf.write("\3\2\2\2\u0155\u0156\7P\2\2\u0156\u0157\7g\2\2\u0157\u0158")
        buf.write("\7y\2\2\u0158\66\3\2\2\2\u0159\u015a\7D\2\2\u015a\u015b")
        buf.write("\7{\2\2\u015b8\3\2\2\2\u015c\u015d\7o\2\2\u015d\u015e")
        buf.write("\7c\2\2\u015e\u015f\7k\2\2\u015f\u0160\7p\2\2\u0160:\3")
        buf.write("\2\2\2\u0161\u0162\7?\2\2\u0162<\3\2\2\2\u0163\u0164\7")
        buf.write("#\2\2\u0164>\3\2\2\2\u0165\u0166\7~\2\2\u0166\u0167\7")
        buf.write("~\2\2\u0167@\3\2\2\2\u0168\u0169\7(\2\2\u0169\u016a\7")
        buf.write("(\2\2\u016aB\3\2\2\2\u016b\u016c\7?\2\2\u016c\u016d\7")
        buf.write("?\2\2\u016dD\3\2\2\2\u016e\u016f\7#\2\2\u016f\u0170\7")
        buf.write("?\2\2\u0170F\3\2\2\2\u0171\u0172\7\'\2\2\u0172H\3\2\2")
        buf.write("\2\u0173\u0174\7-\2\2\u0174J\3\2\2\2\u0175\u0176\7/\2")
        buf.write("\2\u0176L\3\2\2\2\u0177\u0178\7,\2\2\u0178N\3\2\2\2\u0179")
        buf.write("\u017a\7\61\2\2\u017aP\3\2\2\2\u017b\u017c\7>\2\2\u017c")
        buf.write("R\3\2\2\2\u017d\u017e\7>\2\2\u017e\u017f\7?\2\2\u017f")
        buf.write("T\3\2\2\2\u0180\u0181\7@\2\2\u0181V\3\2\2\2\u0182\u0183")
        buf.write("\7@\2\2\u0183\u0184\7?\2\2\u0184X\3\2\2\2\u0185\u0186")
        buf.write("\7-\2\2\u0186\u0187\7\60\2\2\u0187Z\3\2\2\2\u0188\u0189")
        buf.write("\7?\2\2\u0189\u018a\7?\2\2\u018a\u018b\7\60\2\2\u018b")
        buf.write("\\\3\2\2\2\u018c\u018d\7*\2\2\u018d^\3\2\2\2\u018e\u018f")
        buf.write("\7+\2\2\u018f`\3\2\2\2\u0190\u0191\7]\2\2\u0191b\3\2\2")
        buf.write("\2\u0192\u0193\7_\2\2\u0193d\3\2\2\2\u0194\u0195\7\60")
        buf.write("\2\2\u0195f\3\2\2\2\u0196\u0197\7.\2\2\u0197h\3\2\2\2")
        buf.write("\u0198\u0199\7<\2\2\u0199j\3\2\2\2\u019a\u019b\7=\2\2")
        buf.write("\u019bl\3\2\2\2\u019c\u019d\7}\2\2\u019dn\3\2\2\2\u019e")
        buf.write("\u019f\7\177\2\2\u019fp\3\2\2\2\u01a0\u01a1\7)\2\2\u01a1")
        buf.write("r\3\2\2\2\u01a2\u01a3\7$\2\2\u01a3t\3\2\2\2\u01a4\u01a5")
        buf.write("\7)\2\2\u01a5\u01b3\7$\2\2\u01a6\u01a7\7^\2\2\u01a7\u01b3")
        buf.write("\7d\2\2\u01a8\u01a9\7^\2\2\u01a9\u01b3\7h\2\2\u01aa\u01ab")
        buf.write("\7^\2\2\u01ab\u01b3\7t\2\2\u01ac\u01ad\7^\2\2\u01ad\u01b3")
        buf.write("\7p\2\2\u01ae\u01af\7^\2\2\u01af\u01b3\7v\2\2\u01b0\u01b1")
        buf.write("\7^\2\2\u01b1\u01b3\7^\2\2\u01b2\u01a4\3\2\2\2\u01b2\u01a6")
        buf.write("\3\2\2\2\u01b2\u01a8\3\2\2\2\u01b2\u01aa\3\2\2\2\u01b2")
        buf.write("\u01ac\3\2\2\2\u01b2\u01ae\3\2\2\2\u01b2\u01b0\3\2\2\2")
        buf.write("\u01b3v\3\2\2\2\u01b4\u01b5\7\62\2\2\u01b5x\3\2\2\2\u01b6")
        buf.write("\u01b7\7\62\2\2\u01b7\u01bb\7z\2\2\u01b8\u01b9\7\62\2")
        buf.write("\2\u01b9\u01bb\7Z\2\2\u01ba\u01b6\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01bbz\3\2\2\2\u01bc\u01bd\7\62\2\2\u01bd\u01c1")
        buf.write("\7d\2\2\u01be\u01bf\7\62\2\2\u01bf\u01c1\7D\2\2\u01c0")
        buf.write("\u01bc\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1|\3\2\2\2\u01c2")
        buf.write("\u01c3\t\2\2\2\u01c3~\3\2\2\2\u01c4\u01c5\t\3\2\2\u01c5")
        buf.write("\u0080\3\2\2\2\u01c6\u01c7\t\4\2\2\u01c7\u0082\3\2\2\2")
        buf.write("\u01c8\u01c9\t\5\2\2\u01c9\u0084\3\2\2\2\u01ca\u01cc\t")
        buf.write("\6\2\2\u01cb\u01cd\t\7\2\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd")
        buf.write("\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01d0\5\u0087D\2\u01cf")
        buf.write("\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01cf\3\2\2\2")
        buf.write("\u01d1\u01d2\3\2\2\2\u01d2\u0086\3\2\2\2\u01d3\u01ea\5")
        buf.write("\u0083B\2\u01d4\u01d6\t\b\2\2\u01d5\u01d7\7a\2\2\u01d6")
        buf.write("\u01d5\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01e1\3\2\2\2")
        buf.write("\u01d8\u01da\5\u0083B\2\u01d9\u01d8\3\2\2\2\u01da\u01db")
        buf.write("\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc")
        buf.write("\u01dd\3\2\2\2\u01dd\u01de\7a\2\2\u01de\u01e0\3\2\2\2")
        buf.write("\u01df\u01d9\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3")
        buf.write("\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1")
        buf.write("\3\2\2\2\u01e4\u01e6\5\u0083B\2\u01e5\u01e4\3\2\2\2\u01e6")
        buf.write("\u01e7\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e8\u01ea\3\2\2\2\u01e9\u01d3\3\2\2\2\u01e9\u01d4\3")
        buf.write("\2\2\2\u01ea\u0088\3\2\2\2\u01eb\u01f5\5w<\2\u01ec\u01ee")
        buf.write("\5\177@\2\u01ed\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\3\2\2\2")
        buf.write("\u01f1\u01f2\7a\2\2\u01f2\u01f4\3\2\2\2\u01f3\u01ed\3")
        buf.write("\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6")
        buf.write("\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8")
        buf.write("\u01fa\5\177@\2\u01f9\u01f8\3\2\2\2\u01fa\u01fb\3\2\2")
        buf.write("\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u008a")
        buf.write("\3\2\2\2\u01fd\u0207\5y=\2\u01fe\u0200\5}?\2\u01ff\u01fe")
        buf.write("\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u01ff\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0204\7a\2\2")
        buf.write("\u0204\u0206\3\2\2\2\u0205\u01ff\3\2\2\2\u0206\u0209\3")
        buf.write("\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u020b")
        buf.write("\3\2\2\2\u0209\u0207\3\2\2\2\u020a\u020c\5}?\2\u020b\u020a")
        buf.write("\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020b\3\2\2\2\u020d")
        buf.write("\u020e\3\2\2\2\u020e\u008c\3\2\2\2\u020f\u0219\5{>\2\u0210")
        buf.write("\u0212\5\u0081A\2\u0211\u0210\3\2\2\2\u0212\u0213\3\2")
        buf.write("\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0215")
        buf.write("\3\2\2\2\u0215\u0216\7a\2\2\u0216\u0218\3\2\2\2\u0217")
        buf.write("\u0211\3\2\2\2\u0218\u021b\3\2\2\2\u0219\u0217\3\2\2\2")
        buf.write("\u0219\u021a\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3")
        buf.write("\2\2\2\u021c\u021e\5\u0081A\2\u021d\u021c\3\2\2\2\u021e")
        buf.write("\u021f\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220\3\2\2\2")
        buf.write("\u0220\u008e\3\2\2\2\u0221\u0226\5\u0087D\2\u0222\u0226")
        buf.write("\5\u0089E\2\u0223\u0226\5\u008bF\2\u0224\u0226\5\u008d")
        buf.write("G\2\u0225\u0221\3\2\2\2\u0225\u0222\3\2\2\2\u0225\u0223")
        buf.write("\3\2\2\2\u0225\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227")
        buf.write("\u0228\bH\3\2\u0228\u0090\3\2\2\2\u0229\u022a\5\u0087")
        buf.write("D\2\u022a\u022c\5e\63\2\u022b\u022d\5\u0087D\2\u022c\u022b")
        buf.write("\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022f\3\2\2\2\u022e")
        buf.write("\u0230\5\u0085C\2\u022f\u022e\3\2\2\2\u022f\u0230\3\2")
        buf.write("\2\2\u0230\u023b\3\2\2\2\u0231\u0232\5\u0087D\2\u0232")
        buf.write("\u0233\5\u0085C\2\u0233\u023b\3\2\2\2\u0234\u0236\5e\63")
        buf.write("\2\u0235\u0237\5\u0087D\2\u0236\u0235\3\2\2\2\u0236\u0237")
        buf.write("\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u0239\5\u0085C\2\u0239")
        buf.write("\u023b\3\2\2\2\u023a\u0229\3\2\2\2\u023a\u0231\3\2\2\2")
        buf.write("\u023a\u0234\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023d\b")
        buf.write("I\4\2\u023d\u0092\3\2\2\2\u023e\u023f\7V\2\2\u023f\u0240")
        buf.write("\7t\2\2\u0240\u0241\7w\2\2\u0241\u0248\7g\2\2\u0242\u0243")
        buf.write("\7H\2\2\u0243\u0244\7c\2\2\u0244\u0245\7n\2\2\u0245\u0246")
        buf.write("\7u\2\2\u0246\u0248\7g\2\2\u0247\u023e\3\2\2\2\u0247\u0242")
        buf.write("\3\2\2\2\u0248\u0094\3\2\2\2\u0249\u024e\5s:\2\u024a\u024d")
        buf.write("\5u;\2\u024b\u024d\n\t\2\2\u024c\u024a\3\2\2\2\u024c\u024b")
        buf.write("\3\2\2\2\u024d\u0250\3\2\2\2\u024e\u024f\3\2\2\2\u024e")
        buf.write("\u024c\3\2\2\2\u024f\u0251\3\2\2\2\u0250\u024e\3\2\2\2")
        buf.write("\u0251\u0252\5s:\2\u0252\u0096\3\2\2\2\u0253\u0255\t\n")
        buf.write("\2\2\u0254\u0253\3\2\2\2\u0255\u0259\3\2\2\2\u0256\u0258")
        buf.write("\t\13\2\2\u0257\u0256\3\2\2\2\u0258\u025b\3\2\2\2\u0259")
        buf.write("\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u0098\3\2\2\2")
        buf.write("\u025b\u0259\3\2\2\2\u025c\u025e\7&\2\2\u025d\u025f\t")
        buf.write("\13\2\2\u025e\u025d\3\2\2\2\u025f\u0260\3\2\2\2\u0260")
        buf.write("\u025e\3\2\2\2\u0260\u0261\3\2\2\2\u0261\u009a\3\2\2\2")
        buf.write("\u0262\u0264\t\f\2\2\u0263\u0262\3\2\2\2\u0264\u0265\3")
        buf.write("\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0267")
        buf.write("\3\2\2\2\u0267\u0268\bN\2\2\u0268\u009c\3\2\2\2%\2\u00d4")
        buf.write("\u01b2\u01ba\u01c0\u01cc\u01d1\u01d6\u01db\u01e1\u01e7")
        buf.write("\u01e9\u01ef\u01f5\u01fb\u0201\u0207\u020d\u0213\u0219")
        buf.write("\u021f\u0225\u022c\u022f\u0236\u023a\u0247\u024c\u024e")
        buf.write("\u0254\u0257\u0259\u025e\u0260\u0265\5\b\2\2\3H\2\3I\3")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    COMMENT = 6
    K_BREAK = 7
    K_CONTINUE = 8
    K_IF = 9
    K_ELSE_IF = 10
    K_ELSE = 11
    K_FOR_EACH = 12
    K_ARRAY = 13
    K_IN = 14
    K_INT = 15
    K_FLOAT = 16
    K_BOOLEAN = 17
    K_STRING = 18
    K_RETURN = 19
    K_NULL = 20
    K_CLASS = 21
    K_VAL = 22
    K_VAR = 23
    K_CONSTRUCTOR = 24
    K_DESTRUCTOR = 25
    K_NEW = 26
    K_BY = 27
    K_MAIN = 28
    OP_ASSIGN = 29
    OP_LOGICAL_NOT = 30
    OP_LOGICAL_OR = 31
    OP_LOGICAL_AND = 32
    OP_IS_EQUAL_TO = 33
    OP_NOT_EQUAL_TO = 34
    OP_MODULO = 35
    OP_ADDTION = 36
    OP_SUBTRACTION = 37
    OP_MULTIPLICATION = 38
    OP_DIVISION = 39
    OP_LESS_THAN = 40
    OP_LESS_THAN_EQUAL = 41
    OP_GREATER_THAN = 42
    OP_GREATER_THAN_EQUAL = 43
    OP_STRING_CONCATENATION = 44
    OP_TWO_SAME_STRING = 45
    LEFT_PAREN = 46
    RIGHT_PAREN = 47
    LEFT_SQUARE_BRACKET = 48
    RIGHT_SQUARE_BRACKET = 49
    DOT = 50
    COMMA = 51
    COLON = 52
    SEMI_COLON = 53
    LEFT_CURLY_BRACKET = 54
    RIGHT_CURLY_BRACKET = 55
    ESCAPE = 56
    INTEGER_LITERAL = 57
    FLOAT_LITERAL = 58
    BOOLEAN_LITERAL = 59
    STRING_LITERAL = 60
    IDENTIFIER = 61
    DOLAR_IDENTIFIER = 62
    WHITE_SPACE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'method body'", "'statement'", "'expr'", "'function call'", 
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
            "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'main'", "'='", "'!'", "'||'", 
            "'&&'", "'=='", "'!='", "'%'", "'+'", "'-'", "'*'", "'/'", "'<'", 
            "'<='", "'>'", "'>='", "'+.'", "'==.'", "'('", "')'", "'['", 
            "']'", "'.'", "','", "':'", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", "K_ELSE", 
            "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", 
            "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", "K_VAL", "K_VAR", 
            "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", "K_BY", "K_MAIN", 
            "OP_ASSIGN", "OP_LOGICAL_NOT", "OP_LOGICAL_OR", "OP_LOGICAL_AND", 
            "OP_IS_EQUAL_TO", "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", 
            "OP_SUBTRACTION", "OP_MULTIPLICATION", "OP_DIVISION", "OP_LESS_THAN", 
            "OP_LESS_THAN_EQUAL", "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", 
            "OP_STRING_CONCATENATION", "OP_TWO_SAME_STRING", "LEFT_PAREN", 
            "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
            "DOT", "COMMA", "COLON", "SEMI_COLON", "LEFT_CURLY_BRACKET", 
            "RIGHT_CURLY_BRACKET", "ESCAPE", "INTEGER_LITERAL", "FLOAT_LITERAL", 
            "BOOLEAN_LITERAL", "STRING_LITERAL", "IDENTIFIER", "DOLAR_IDENTIFIER", 
            "WHITE_SPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "COMMENT", "K_BREAK", 
                  "K_CONTINUE", "K_IF", "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", 
                  "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", 
                  "K_RETURN", "K_NULL", "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", 
                  "K_DESTRUCTOR", "K_NEW", "K_BY", "K_MAIN", "OP_ASSIGN", 
                  "OP_LOGICAL_NOT", "OP_LOGICAL_OR", "OP_LOGICAL_AND", "OP_IS_EQUAL_TO", 
                  "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", "OP_SUBTRACTION", 
                  "OP_MULTIPLICATION", "OP_DIVISION", "OP_LESS_THAN", "OP_LESS_THAN_EQUAL", 
                  "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", "OP_STRING_CONCATENATION", 
                  "OP_TWO_SAME_STRING", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", 
                  "RIGHT_SQUARE_BRACKET", "DOT", "COMMA", "COLON", "SEMI_COLON", 
                  "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "SINGLE_QUOTE", 
                  "DOUBLE_QUOTE", "ESCAPE", "OCTAL_NOTATION", "HEXA_NOTATION", 
                  "BINARY_NOTATION", "HEXA_DIGIT", "OCTAL_DIGIT", "BINARY_DIGIT", 
                  "DECIMAL_DIGIT", "EXPONENT", "DECIMAL", "OCTAL", "HEXA", 
                  "BINARY", "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", 
                  "STRING_LITERAL", "IDENTIFIER", "DOLAR_IDENTIFIER", "WHITE_SPACE" ]

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
            actions[70] = self.INTEGER_LITERAL_action 
            actions[71] = self.FLOAT_LITERAL_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOAT_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     


