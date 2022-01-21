# Generated from d:\Study2\HCMUT\semester212\PPL\code\assignment\assignment1\assigment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u027a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u00d9\n\7\f\7\16\7\u00dc")
        buf.write("\13\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\39\39")
        buf.write("\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\5>\u01c4\n>\3?\3?\3@\3@\3@\3@\5@\u01cc\n")
        buf.write("@\3A\3A\3A\3A\5A\u01d2\nA\3B\3B\3C\3C\3D\3D\3E\3E\3F\3")
        buf.write("F\5F\u01de\nF\3F\6F\u01e1\nF\rF\16F\u01e2\3G\3G\3G\5G")
        buf.write("\u01e8\nG\3G\6G\u01eb\nG\rG\16G\u01ec\3G\5G\u01f0\nG\7")
        buf.write("G\u01f2\nG\fG\16G\u01f5\13G\3G\5G\u01f8\nG\3H\3H\3H\3")
        buf.write("H\6H\u01fe\nH\rH\16H\u01ff\3H\5H\u0203\nH\7H\u0205\nH")
        buf.write("\fH\16H\u0208\13H\3H\5H\u020b\nH\3I\3I\3I\3I\6I\u0211")
        buf.write("\nI\rI\16I\u0212\3I\5I\u0216\nI\7I\u0218\nI\fI\16I\u021b")
        buf.write("\13I\3I\5I\u021e\nI\3J\3J\3J\3J\6J\u0224\nJ\rJ\16J\u0225")
        buf.write("\3J\5J\u0229\nJ\7J\u022b\nJ\fJ\16J\u022e\13J\3J\5J\u0231")
        buf.write("\nJ\3K\3K\3K\3K\3K\3K\5K\u0239\nK\3L\3L\3L\5L\u023e\n")
        buf.write("L\3L\5L\u0241\nL\3L\3L\3L\3L\3L\5L\u0248\nL\3L\3L\5L\u024c")
        buf.write("\nL\3L\3L\3M\3M\3M\3M\3M\3M\3M\3M\3M\5M\u0259\nM\3N\3")
        buf.write("N\3N\7N\u025e\nN\fN\16N\u0261\13N\3N\3N\3O\5O\u0266\n")
        buf.write("O\3O\7O\u0269\nO\fO\16O\u026c\13O\3P\3P\6P\u0270\nP\r")
        buf.write("P\16P\u0271\3Q\6Q\u0275\nQ\rQ\16Q\u0276\3Q\3Q\4\u00da")
        buf.write("\u025f\2R\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w\2y\2{=}\2\177\2\u0081\2\u0083\2\u0085\2")
        buf.write("\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093")
        buf.write("\2\u0095>\u0097?\u0099@\u009bA\u009dB\u009fC\u00a1D\3")
        buf.write("\2\17\5\2\62;CHch\3\2\629\3\2\62\63\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\3\2\63;\3\2\639\5\2\63;CHch\4\2$$^^\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u0295\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2{\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2\2\5\u00ab")
        buf.write("\3\2\2\2\7\u00b7\3\2\2\2\t\u00bc\3\2\2\2\13\u00ca\3\2")
        buf.write("\2\2\r\u00d4\3\2\2\2\17\u00e2\3\2\2\2\21\u00e8\3\2\2\2")
        buf.write("\23\u00f1\3\2\2\2\25\u00f4\3\2\2\2\27\u00fb\3\2\2\2\31")
        buf.write("\u0100\3\2\2\2\33\u0108\3\2\2\2\35\u010e\3\2\2\2\37\u0111")
        buf.write("\3\2\2\2!\u0115\3\2\2\2#\u011b\3\2\2\2%\u0123\3\2\2\2")
        buf.write("\'\u012a\3\2\2\2)\u0131\3\2\2\2+\u0136\3\2\2\2-\u013c")
        buf.write("\3\2\2\2/\u0140\3\2\2\2\61\u0144\3\2\2\2\63\u0150\3\2")
        buf.write("\2\2\65\u015b\3\2\2\2\67\u015f\3\2\2\29\u0162\3\2\2\2")
        buf.write(";\u0167\3\2\2\2=\u016c\3\2\2\2?\u016e\3\2\2\2A\u0170\3")
        buf.write("\2\2\2C\u0173\3\2\2\2E\u0176\3\2\2\2G\u0179\3\2\2\2I\u017c")
        buf.write("\3\2\2\2K\u017e\3\2\2\2M\u0180\3\2\2\2O\u0182\3\2\2\2")
        buf.write("Q\u0184\3\2\2\2S\u0186\3\2\2\2U\u0188\3\2\2\2W\u018b\3")
        buf.write("\2\2\2Y\u018d\3\2\2\2[\u0190\3\2\2\2]\u0193\3\2\2\2_\u0197")
        buf.write("\3\2\2\2a\u0199\3\2\2\2c\u019b\3\2\2\2e\u019d\3\2\2\2")
        buf.write("g\u019f\3\2\2\2i\u01a1\3\2\2\2k\u01a4\3\2\2\2m\u01a6\3")
        buf.write("\2\2\2o\u01a8\3\2\2\2q\u01ab\3\2\2\2s\u01ad\3\2\2\2u\u01af")
        buf.write("\3\2\2\2w\u01b1\3\2\2\2y\u01b3\3\2\2\2{\u01c3\3\2\2\2")
        buf.write("}\u01c5\3\2\2\2\177\u01cb\3\2\2\2\u0081\u01d1\3\2\2\2")
        buf.write("\u0083\u01d3\3\2\2\2\u0085\u01d5\3\2\2\2\u0087\u01d7\3")
        buf.write("\2\2\2\u0089\u01d9\3\2\2\2\u008b\u01db\3\2\2\2\u008d\u01f7")
        buf.write("\3\2\2\2\u008f\u01f9\3\2\2\2\u0091\u020c\3\2\2\2\u0093")
        buf.write("\u021f\3\2\2\2\u0095\u0238\3\2\2\2\u0097\u024b\3\2\2\2")
        buf.write("\u0099\u0258\3\2\2\2\u009b\u025a\3\2\2\2\u009d\u0265\3")
        buf.write("\2\2\2\u009f\u026d\3\2\2\2\u00a1\u0274\3\2\2\2\u00a3\u00a4")
        buf.write("\7R\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7")
        buf.write("\7i\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa")
        buf.write("\7o\2\2\u00aa\4\3\2\2\2\u00ab\u00ac\7o\2\2\u00ac\u00ad")
        buf.write("\7g\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7j\2\2\u00af\u00b0")
        buf.write("\7q\2\2\u00b0\u00b1\7f\2\2\u00b1\u00b2\7\"\2\2\u00b2\u00b3")
        buf.write("\7d\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7f\2\2\u00b5\u00b6")
        buf.write("\7{\2\2\u00b6\6\3\2\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9")
        buf.write("\7z\2\2\u00b9\u00ba\7r\2\2\u00ba\u00bb\7t\2\2\u00bb\b")
        buf.write("\3\2\2\2\u00bc\u00bd\7h\2\2\u00bd\u00be\7w\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\u00c0\7e\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2")
        buf.write("\7k\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5")
        buf.write("\7\"\2\2\u00c5\u00c6\7e\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8")
        buf.write("\7n\2\2\u00c8\u00c9\7n\2\2\u00c9\n\3\2\2\2\u00ca\u00cb")
        buf.write("\7u\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce")
        buf.write("\7v\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7o\2\2\u00d0\u00d1")
        buf.write("\7g\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7v\2\2\u00d3\f")
        buf.write("\3\2\2\2\u00d4\u00d5\7%\2\2\u00d5\u00d6\7%\2\2\u00d6\u00da")
        buf.write("\3\2\2\2\u00d7\u00d9\13\2\2\2\u00d8\u00d7\3\2\2\2\u00d9")
        buf.write("\u00dc\3\2\2\2\u00da\u00db\3\2\2\2\u00da\u00d8\3\2\2\2")
        buf.write("\u00db\u00dd\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00de\7")
        buf.write("%\2\2\u00de\u00df\7%\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1")
        buf.write("\b\7\2\2\u00e1\16\3\2\2\2\u00e2\u00e3\7D\2\2\u00e3\u00e4")
        buf.write("\7t\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7")
        buf.write("\7m\2\2\u00e7\20\3\2\2\2\u00e8\u00e9\7E\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7w\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0\22\3\2\2\2\u00f1\u00f2\7K\2\2\u00f2\u00f3")
        buf.write("\7h\2\2\u00f3\24\3\2\2\2\u00f4\u00f5\7G\2\2\u00f5\u00f6")
        buf.write("\7n\2\2\u00f6\u00f7\7u\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9")
        buf.write("\7k\2\2\u00f9\u00fa\7h\2\2\u00fa\26\3\2\2\2\u00fb\u00fc")
        buf.write("\7G\2\2\u00fc\u00fd\7n\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff")
        buf.write("\7g\2\2\u00ff\30\3\2\2\2\u0100\u0101\7H\2\2\u0101\u0102")
        buf.write("\7q\2\2\u0102\u0103\7t\2\2\u0103\u0104\7g\2\2\u0104\u0105")
        buf.write("\7c\2\2\u0105\u0106\7e\2\2\u0106\u0107\7j\2\2\u0107\32")
        buf.write("\3\2\2\2\u0108\u0109\7C\2\2\u0109\u010a\7t\2\2\u010a\u010b")
        buf.write("\7t\2\2\u010b\u010c\7c\2\2\u010c\u010d\7{\2\2\u010d\34")
        buf.write("\3\2\2\2\u010e\u010f\7K\2\2\u010f\u0110\7p\2\2\u0110\36")
        buf.write("\3\2\2\2\u0111\u0112\7K\2\2\u0112\u0113\7p\2\2\u0113\u0114")
        buf.write("\7v\2\2\u0114 \3\2\2\2\u0115\u0116\7H\2\2\u0116\u0117")
        buf.write("\7n\2\2\u0117\u0118\7q\2\2\u0118\u0119\7c\2\2\u0119\u011a")
        buf.write("\7v\2\2\u011a\"\3\2\2\2\u011b\u011c\7D\2\2\u011c\u011d")
        buf.write("\7q\2\2\u011d\u011e\7q\2\2\u011e\u011f\7n\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120\u0121\7c\2\2\u0121\u0122\7p\2\2\u0122$\3")
        buf.write("\2\2\2\u0123\u0124\7U\2\2\u0124\u0125\7v\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126\u0127\7k\2\2\u0127\u0128\7p\2\2\u0128\u0129")
        buf.write("\7i\2\2\u0129&\3\2\2\2\u012a\u012b\7T\2\2\u012b\u012c")
        buf.write("\7g\2\2\u012c\u012d\7v\2\2\u012d\u012e\7w\2\2\u012e\u012f")
        buf.write("\7t\2\2\u012f\u0130\7p\2\2\u0130(\3\2\2\2\u0131\u0132")
        buf.write("\7P\2\2\u0132\u0133\7w\2\2\u0133\u0134\7n\2\2\u0134\u0135")
        buf.write("\7n\2\2\u0135*\3\2\2\2\u0136\u0137\7E\2\2\u0137\u0138")
        buf.write("\7n\2\2\u0138\u0139\7c\2\2\u0139\u013a\7u\2\2\u013a\u013b")
        buf.write("\7u\2\2\u013b,\3\2\2\2\u013c\u013d\7X\2\2\u013d\u013e")
        buf.write("\7c\2\2\u013e\u013f\7n\2\2\u013f.\3\2\2\2\u0140\u0141")
        buf.write("\7X\2\2\u0141\u0142\7c\2\2\u0142\u0143\7t\2\2\u0143\60")
        buf.write("\3\2\2\2\u0144\u0145\7E\2\2\u0145\u0146\7q\2\2\u0146\u0147")
        buf.write("\7p\2\2\u0147\u0148\7u\2\2\u0148\u0149\7v\2\2\u0149\u014a")
        buf.write("\7t\2\2\u014a\u014b\7w\2\2\u014b\u014c\7e\2\2\u014c\u014d")
        buf.write("\7v\2\2\u014d\u014e\7q\2\2\u014e\u014f\7t\2\2\u014f\62")
        buf.write("\3\2\2\2\u0150\u0151\7F\2\2\u0151\u0152\7g\2\2\u0152\u0153")
        buf.write("\7u\2\2\u0153\u0154\7v\2\2\u0154\u0155\7t\2\2\u0155\u0156")
        buf.write("\7w\2\2\u0156\u0157\7e\2\2\u0157\u0158\7v\2\2\u0158\u0159")
        buf.write("\7q\2\2\u0159\u015a\7t\2\2\u015a\64\3\2\2\2\u015b\u015c")
        buf.write("\7P\2\2\u015c\u015d\7g\2\2\u015d\u015e\7y\2\2\u015e\66")
        buf.write("\3\2\2\2\u015f\u0160\7D\2\2\u0160\u0161\7{\2\2\u01618")
        buf.write("\3\2\2\2\u0162\u0163\7o\2\2\u0163\u0164\7c\2\2\u0164\u0165")
        buf.write("\7k\2\2\u0165\u0166\7p\2\2\u0166:\3\2\2\2\u0167\u0168")
        buf.write("\7u\2\2\u0168\u0169\7g\2\2\u0169\u016a\7n\2\2\u016a\u016b")
        buf.write("\7h\2\2\u016b<\3\2\2\2\u016c\u016d\7?\2\2\u016d>\3\2\2")
        buf.write("\2\u016e\u016f\7#\2\2\u016f@\3\2\2\2\u0170\u0171\7~\2")
        buf.write("\2\u0171\u0172\7~\2\2\u0172B\3\2\2\2\u0173\u0174\7(\2")
        buf.write("\2\u0174\u0175\7(\2\2\u0175D\3\2\2\2\u0176\u0177\7?\2")
        buf.write("\2\u0177\u0178\7?\2\2\u0178F\3\2\2\2\u0179\u017a\7#\2")
        buf.write("\2\u017a\u017b\7?\2\2\u017bH\3\2\2\2\u017c\u017d\7\'\2")
        buf.write("\2\u017dJ\3\2\2\2\u017e\u017f\7-\2\2\u017fL\3\2\2\2\u0180")
        buf.write("\u0181\7/\2\2\u0181N\3\2\2\2\u0182\u0183\7,\2\2\u0183")
        buf.write("P\3\2\2\2\u0184\u0185\7\61\2\2\u0185R\3\2\2\2\u0186\u0187")
        buf.write("\7>\2\2\u0187T\3\2\2\2\u0188\u0189\7>\2\2\u0189\u018a")
        buf.write("\7?\2\2\u018aV\3\2\2\2\u018b\u018c\7@\2\2\u018cX\3\2\2")
        buf.write("\2\u018d\u018e\7@\2\2\u018e\u018f\7?\2\2\u018fZ\3\2\2")
        buf.write("\2\u0190\u0191\7-\2\2\u0191\u0192\7\60\2\2\u0192\\\3\2")
        buf.write("\2\2\u0193\u0194\7?\2\2\u0194\u0195\7?\2\2\u0195\u0196")
        buf.write("\7\60\2\2\u0196^\3\2\2\2\u0197\u0198\7*\2\2\u0198`\3\2")
        buf.write("\2\2\u0199\u019a\7+\2\2\u019ab\3\2\2\2\u019b\u019c\7]")
        buf.write("\2\2\u019cd\3\2\2\2\u019d\u019e\7_\2\2\u019ef\3\2\2\2")
        buf.write("\u019f\u01a0\7\60\2\2\u01a0h\3\2\2\2\u01a1\u01a2\7\60")
        buf.write("\2\2\u01a2\u01a3\7\60\2\2\u01a3j\3\2\2\2\u01a4\u01a5\7")
        buf.write(".\2\2\u01a5l\3\2\2\2\u01a6\u01a7\7<\2\2\u01a7n\3\2\2\2")
        buf.write("\u01a8\u01a9\7<\2\2\u01a9\u01aa\7<\2\2\u01aap\3\2\2\2")
        buf.write("\u01ab\u01ac\7=\2\2\u01acr\3\2\2\2\u01ad\u01ae\7}\2\2")
        buf.write("\u01aet\3\2\2\2\u01af\u01b0\7\177\2\2\u01b0v\3\2\2\2\u01b1")
        buf.write("\u01b2\7)\2\2\u01b2x\3\2\2\2\u01b3\u01b4\7$\2\2\u01b4")
        buf.write("z\3\2\2\2\u01b5\u01b6\7)\2\2\u01b6\u01c4\7$\2\2\u01b7")
        buf.write("\u01b8\7^\2\2\u01b8\u01c4\7d\2\2\u01b9\u01ba\7^\2\2\u01ba")
        buf.write("\u01c4\7h\2\2\u01bb\u01bc\7^\2\2\u01bc\u01c4\7t\2\2\u01bd")
        buf.write("\u01be\7^\2\2\u01be\u01c4\7p\2\2\u01bf\u01c0\7^\2\2\u01c0")
        buf.write("\u01c4\7v\2\2\u01c1\u01c2\7^\2\2\u01c2\u01c4\7^\2\2\u01c3")
        buf.write("\u01b5\3\2\2\2\u01c3\u01b7\3\2\2\2\u01c3\u01b9\3\2\2\2")
        buf.write("\u01c3\u01bb\3\2\2\2\u01c3\u01bd\3\2\2\2\u01c3\u01bf\3")
        buf.write("\2\2\2\u01c3\u01c1\3\2\2\2\u01c4|\3\2\2\2\u01c5\u01c6")
        buf.write("\7\62\2\2\u01c6~\3\2\2\2\u01c7\u01c8\7\62\2\2\u01c8\u01cc")
        buf.write("\7z\2\2\u01c9\u01ca\7\62\2\2\u01ca\u01cc\7Z\2\2\u01cb")
        buf.write("\u01c7\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u0080\3\2\2\2")
        buf.write("\u01cd\u01ce\7\62\2\2\u01ce\u01d2\7d\2\2\u01cf\u01d0\7")
        buf.write("\62\2\2\u01d0\u01d2\7D\2\2\u01d1\u01cd\3\2\2\2\u01d1\u01cf")
        buf.write("\3\2\2\2\u01d2\u0082\3\2\2\2\u01d3\u01d4\t\2\2\2\u01d4")
        buf.write("\u0084\3\2\2\2\u01d5\u01d6\t\3\2\2\u01d6\u0086\3\2\2\2")
        buf.write("\u01d7\u01d8\t\4\2\2\u01d8\u0088\3\2\2\2\u01d9\u01da\t")
        buf.write("\5\2\2\u01da\u008a\3\2\2\2\u01db\u01dd\t\6\2\2\u01dc\u01de")
        buf.write("\t\7\2\2\u01dd\u01dc\3\2\2\2\u01dd\u01de\3\2\2\2\u01de")
        buf.write("\u01e0\3\2\2\2\u01df\u01e1\5\u008dG\2\u01e0\u01df\3\2")
        buf.write("\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3")
        buf.write("\3\2\2\2\u01e3\u008c\3\2\2\2\u01e4\u01f8\5\u0089E\2\u01e5")
        buf.write("\u01e7\t\b\2\2\u01e6\u01e8\7a\2\2\u01e7\u01e6\3\2\2\2")
        buf.write("\u01e7\u01e8\3\2\2\2\u01e8\u01f3\3\2\2\2\u01e9\u01eb\5")
        buf.write("\u0089E\2\u01ea\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec")
        buf.write("\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01ef\3\2\2\2")
        buf.write("\u01ee\u01f0\7a\2\2\u01ef\u01ee\3\2\2\2\u01ef\u01f0\3")
        buf.write("\2\2\2\u01f0\u01f2\3\2\2\2\u01f1\u01ea\3\2\2\2\u01f2\u01f5")
        buf.write("\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4")
        buf.write("\u01f6\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f6\u01f8\5\u0089")
        buf.write("E\2\u01f7\u01e4\3\2\2\2\u01f7\u01e5\3\2\2\2\u01f8\u008e")
        buf.write("\3\2\2\2\u01f9\u020a\5}?\2\u01fa\u020b\7\62\2\2\u01fb")
        buf.write("\u0206\t\t\2\2\u01fc\u01fe\5\u0085C\2\u01fd\u01fc\3\2")
        buf.write("\2\2\u01fe\u01ff\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200")
        buf.write("\3\2\2\2\u0200\u0202\3\2\2\2\u0201\u0203\7a\2\2\u0202")
        buf.write("\u0201\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0205\3\2\2\2")
        buf.write("\u0204\u01fd\3\2\2\2\u0205\u0208\3\2\2\2\u0206\u0204\3")
        buf.write("\2\2\2\u0206\u0207\3\2\2\2\u0207\u0209\3\2\2\2\u0208\u0206")
        buf.write("\3\2\2\2\u0209\u020b\5\u0085C\2\u020a\u01fa\3\2\2\2\u020a")
        buf.write("\u01fb\3\2\2\2\u020b\u0090\3\2\2\2\u020c\u021d\5\177@")
        buf.write("\2\u020d\u021e\7\62\2\2\u020e\u0219\t\n\2\2\u020f\u0211")
        buf.write("\5\u0083B\2\u0210\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212")
        buf.write("\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0215\3\2\2\2")
        buf.write("\u0214\u0216\7a\2\2\u0215\u0214\3\2\2\2\u0215\u0216\3")
        buf.write("\2\2\2\u0216\u0218\3\2\2\2\u0217\u0210\3\2\2\2\u0218\u021b")
        buf.write("\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u021a\3\2\2\2\u021a")
        buf.write("\u021c\3\2\2\2\u021b\u0219\3\2\2\2\u021c\u021e\5\u0083")
        buf.write("B\2\u021d\u020d\3\2\2\2\u021d\u020e\3\2\2\2\u021e\u0092")
        buf.write("\3\2\2\2\u021f\u0230\5\u0081A\2\u0220\u0231\7\62\2\2\u0221")
        buf.write("\u022c\7\63\2\2\u0222\u0224\5\u0087D\2\u0223\u0222\3\2")
        buf.write("\2\2\u0224\u0225\3\2\2\2\u0225\u0223\3\2\2\2\u0225\u0226")
        buf.write("\3\2\2\2\u0226\u0228\3\2\2\2\u0227\u0229\7a\2\2\u0228")
        buf.write("\u0227\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022b\3\2\2\2")
        buf.write("\u022a\u0223\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022a\3")
        buf.write("\2\2\2\u022c\u022d\3\2\2\2\u022d\u022f\3\2\2\2\u022e\u022c")
        buf.write("\3\2\2\2\u022f\u0231\5\u0087D\2\u0230\u0220\3\2\2\2\u0230")
        buf.write("\u0221\3\2\2\2\u0231\u0094\3\2\2\2\u0232\u0239\5\u008d")
        buf.write("G\2\u0233\u0239\5\u008fH\2\u0234\u0239\5\u0091I\2\u0235")
        buf.write("\u0236\5\u0093J\2\u0236\u0237\bK\3\2\u0237\u0239\3\2\2")
        buf.write("\2\u0238\u0232\3\2\2\2\u0238\u0233\3\2\2\2\u0238\u0234")
        buf.write("\3\2\2\2\u0238\u0235\3\2\2\2\u0239\u0096\3\2\2\2\u023a")
        buf.write("\u023b\5\u008dG\2\u023b\u023d\5g\64\2\u023c\u023e\5\u008d")
        buf.write("G\2\u023d\u023c\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u0240")
        buf.write("\3\2\2\2\u023f\u0241\5\u008bF\2\u0240\u023f\3\2\2\2\u0240")
        buf.write("\u0241\3\2\2\2\u0241\u024c\3\2\2\2\u0242\u0243\5\u008d")
        buf.write("G\2\u0243\u0244\5\u008bF\2\u0244\u024c\3\2\2\2\u0245\u0247")
        buf.write("\5g\64\2\u0246\u0248\5\u008dG\2\u0247\u0246\3\2\2\2\u0247")
        buf.write("\u0248\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024a\5\u008b")
        buf.write("F\2\u024a\u024c\3\2\2\2\u024b\u023a\3\2\2\2\u024b\u0242")
        buf.write("\3\2\2\2\u024b\u0245\3\2\2\2\u024c\u024d\3\2\2\2\u024d")
        buf.write("\u024e\bL\4\2\u024e\u0098\3\2\2\2\u024f\u0250\7V\2\2\u0250")
        buf.write("\u0251\7t\2\2\u0251\u0252\7w\2\2\u0252\u0259\7g\2\2\u0253")
        buf.write("\u0254\7H\2\2\u0254\u0255\7c\2\2\u0255\u0256\7n\2\2\u0256")
        buf.write("\u0257\7u\2\2\u0257\u0259\7g\2\2\u0258\u024f\3\2\2\2\u0258")
        buf.write("\u0253\3\2\2\2\u0259\u009a\3\2\2\2\u025a\u025f\5y=\2\u025b")
        buf.write("\u025e\5{>\2\u025c\u025e\n\13\2\2\u025d\u025b\3\2\2\2")
        buf.write("\u025d\u025c\3\2\2\2\u025e\u0261\3\2\2\2\u025f\u0260\3")
        buf.write("\2\2\2\u025f\u025d\3\2\2\2\u0260\u0262\3\2\2\2\u0261\u025f")
        buf.write("\3\2\2\2\u0262\u0263\5y=\2\u0263\u009c\3\2\2\2\u0264\u0266")
        buf.write("\t\f\2\2\u0265\u0264\3\2\2\2\u0266\u026a\3\2\2\2\u0267")
        buf.write("\u0269\t\r\2\2\u0268\u0267\3\2\2\2\u0269\u026c\3\2\2\2")
        buf.write("\u026a\u0268\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u009e\3")
        buf.write("\2\2\2\u026c\u026a\3\2\2\2\u026d\u026f\7&\2\2\u026e\u0270")
        buf.write("\t\r\2\2\u026f\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271")
        buf.write("\u026f\3\2\2\2\u0271\u0272\3\2\2\2\u0272\u00a0\3\2\2\2")
        buf.write("\u0273\u0275\t\16\2\2\u0274\u0273\3\2\2\2\u0275\u0276")
        buf.write("\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2\u0277")
        buf.write("\u0278\3\2\2\2\u0278\u0279\bQ\2\2\u0279\u00a2\3\2\2\2")
        buf.write("(\2\u00da\u01c3\u01cb\u01d1\u01dd\u01e2\u01e7\u01ec\u01ef")
        buf.write("\u01f3\u01f7\u01ff\u0202\u0206\u020a\u0212\u0215\u0219")
        buf.write("\u021d\u0225\u0228\u022c\u0230\u0238\u023d\u0240\u0247")
        buf.write("\u024b\u0258\u025d\u025f\u0265\u0268\u026a\u026f\u0271")
        buf.write("\u0276\5\b\2\2\3K\2\3L\3")
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
    K_SELF = 29
    OP_ASSIGN = 30
    OP_LOGICAL_NOT = 31
    OP_LOGICAL_OR = 32
    OP_LOGICAL_AND = 33
    OP_IS_EQUAL_TO = 34
    OP_NOT_EQUAL_TO = 35
    OP_MODULO = 36
    OP_ADDTION = 37
    OP_SUBTRACTION = 38
    OP_MULTIPLICATION = 39
    OP_DIVISION = 40
    OP_LESS_THAN = 41
    OP_LESS_THAN_EQUAL = 42
    OP_GREATER_THAN = 43
    OP_GREATER_THAN_EQUAL = 44
    OP_STRING_CONCATENATION = 45
    OP_TWO_SAME_STRING = 46
    LEFT_PAREN = 47
    RIGHT_PAREN = 48
    LEFT_SQUARE_BRACKET = 49
    RIGHT_SQUARE_BRACKET = 50
    DOT = 51
    DOUBLE_DOT = 52
    COMMA = 53
    COLON = 54
    DOUBLE_COLON = 55
    SEMI_COLON = 56
    LEFT_CURLY_BRACKET = 57
    RIGHT_CURLY_BRACKET = 58
    ESCAPE = 59
    INTEGER_LITERAL = 60
    FLOAT_LITERAL = 61
    BOOLEAN_LITERAL = 62
    STRING_LITERAL = 63
    IDENTIFIER = 64
    DOLAR_IDENTIFIER = 65
    WHITE_SPACE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'method body'", "'expr'", "'function call'", "'statement'", 
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
            "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'main'", "'self'", "'='", 
            "'!'", "'||'", "'&&'", "'=='", "'!='", "'%'", "'+'", "'-'", 
            "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", "'+.'", "'==.'", 
            "'('", "')'", "'['", "']'", "'.'", "'..'", "','", "':'", "'::'", 
            "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", "K_ELSE", 
            "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", 
            "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", "K_VAL", "K_VAR", 
            "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", "K_BY", "K_MAIN", 
            "K_SELF", "OP_ASSIGN", "OP_LOGICAL_NOT", "OP_LOGICAL_OR", "OP_LOGICAL_AND", 
            "OP_IS_EQUAL_TO", "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", 
            "OP_SUBTRACTION", "OP_MULTIPLICATION", "OP_DIVISION", "OP_LESS_THAN", 
            "OP_LESS_THAN_EQUAL", "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", 
            "OP_STRING_CONCATENATION", "OP_TWO_SAME_STRING", "LEFT_PAREN", 
            "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
            "DOT", "DOUBLE_DOT", "COMMA", "COLON", "DOUBLE_COLON", "SEMI_COLON", 
            "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "ESCAPE", "INTEGER_LITERAL", 
            "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", "IDENTIFIER", 
            "DOLAR_IDENTIFIER", "WHITE_SPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "COMMENT", "K_BREAK", 
                  "K_CONTINUE", "K_IF", "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", 
                  "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", 
                  "K_RETURN", "K_NULL", "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", 
                  "K_DESTRUCTOR", "K_NEW", "K_BY", "K_MAIN", "K_SELF", "OP_ASSIGN", 
                  "OP_LOGICAL_NOT", "OP_LOGICAL_OR", "OP_LOGICAL_AND", "OP_IS_EQUAL_TO", 
                  "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", "OP_SUBTRACTION", 
                  "OP_MULTIPLICATION", "OP_DIVISION", "OP_LESS_THAN", "OP_LESS_THAN_EQUAL", 
                  "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", "OP_STRING_CONCATENATION", 
                  "OP_TWO_SAME_STRING", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", 
                  "RIGHT_SQUARE_BRACKET", "DOT", "DOUBLE_DOT", "COMMA", 
                  "COLON", "DOUBLE_COLON", "SEMI_COLON", "LEFT_CURLY_BRACKET", 
                  "RIGHT_CURLY_BRACKET", "SINGLE_QUOTE", "DOUBLE_QUOTE", 
                  "ESCAPE", "OCTAL_NOTATION", "HEXA_NOTATION", "BINARY_NOTATION", 
                  "HEXA_DIGIT", "OCTAL_DIGIT", "BINARY_DIGIT", "DECIMAL_DIGIT", 
                  "EXPONENT", "DECIMAL", "OCTAL", "HEXA", "BINARY", "INTEGER_LITERAL", 
                  "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                  "IDENTIFIER", "DOLAR_IDENTIFIER", "WHITE_SPACE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[73] = self.INTEGER_LITERAL_action 
            actions[74] = self.FLOAT_LITERAL_action 
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
     


