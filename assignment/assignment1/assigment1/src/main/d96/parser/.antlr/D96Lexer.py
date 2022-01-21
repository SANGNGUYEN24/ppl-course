# Generated from d:\Study2\HCMUT\semester212\PPL\code\assignment\assignment1\assigment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u026f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6\u00cb\n\6\f\6\16\6\u00ce")
        buf.write("\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\5=\u01b6\n=\3>\3>\3?\3?\3?\3?\5?\u01be")
        buf.write("\n?\3@\3@\3@\3@\5@\u01c4\n@\3A\3A\3B\3B\3C\3C\3D\3D\3")
        buf.write("E\3E\5E\u01d0\nE\3E\6E\u01d3\nE\rE\16E\u01d4\3F\3F\3F")
        buf.write("\5F\u01da\nF\3F\6F\u01dd\nF\rF\16F\u01de\3F\5F\u01e2\n")
        buf.write("F\7F\u01e4\nF\fF\16F\u01e7\13F\3F\5F\u01ea\nF\3G\3G\3")
        buf.write("G\3G\6G\u01f0\nG\rG\16G\u01f1\3G\5G\u01f5\nG\7G\u01f7")
        buf.write("\nG\fG\16G\u01fa\13G\3G\5G\u01fd\nG\3H\3H\3H\3H\6H\u0203")
        buf.write("\nH\rH\16H\u0204\3H\5H\u0208\nH\7H\u020a\nH\fH\16H\u020d")
        buf.write("\13H\3H\5H\u0210\nH\3I\3I\3I\3I\6I\u0216\nI\rI\16I\u0217")
        buf.write("\3I\5I\u021b\nI\7I\u021d\nI\fI\16I\u0220\13I\3I\5I\u0223")
        buf.write("\nI\3J\3J\3J\3J\3J\3J\5J\u022b\nJ\3K\3K\3K\5K\u0230\n")
        buf.write("K\3K\5K\u0233\nK\3K\3K\3K\3K\3K\5K\u023a\nK\3K\3K\5K\u023e")
        buf.write("\nK\3K\3K\3L\3L\3L\3L\3L\3L\3L\3L\3L\5L\u024b\nL\3M\3")
        buf.write("M\3M\7M\u0250\nM\fM\16M\u0253\13M\3M\3M\3N\5N\u0258\n")
        buf.write("N\3N\7N\u025b\nN\fN\16N\u025e\13N\3O\3O\6O\u0262\nO\r")
        buf.write("O\16O\u0263\3P\6P\u0267\nP\rP\16P\u0268\3P\3P\3Q\3Q\3")
        buf.write("Q\4\u00cc\u0251\2R\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g")
        buf.write("\65i\66k\67m8o9q:s;u\2w\2y<{\2}\2\177\2\u0081\2\u0083")
        buf.write("\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091")
        buf.write("\2\u0093=\u0095>\u0097?\u0099@\u009bA\u009dB\u009fC\u00a1")
        buf.write("D\3\2\17\5\2\62;CHch\3\2\629\3\2\62\63\3\2\62;\4\2GGg")
        buf.write("g\4\2--//\3\2\63;\3\2\639\5\2\63;CHch\4\2$$^^\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u028a\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2y\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2")
        buf.write("\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2")
        buf.write("\2\5\u00ab\3\2\2\2\7\u00b7\3\2\2\2\t\u00bc\3\2\2\2\13")
        buf.write("\u00c6\3\2\2\2\r\u00d4\3\2\2\2\17\u00da\3\2\2\2\21\u00e3")
        buf.write("\3\2\2\2\23\u00e6\3\2\2\2\25\u00ed\3\2\2\2\27\u00f2\3")
        buf.write("\2\2\2\31\u00fa\3\2\2\2\33\u0100\3\2\2\2\35\u0103\3\2")
        buf.write("\2\2\37\u0107\3\2\2\2!\u010d\3\2\2\2#\u0115\3\2\2\2%\u011c")
        buf.write("\3\2\2\2\'\u0123\3\2\2\2)\u0128\3\2\2\2+\u012e\3\2\2\2")
        buf.write("-\u0132\3\2\2\2/\u0136\3\2\2\2\61\u0142\3\2\2\2\63\u014d")
        buf.write("\3\2\2\2\65\u0151\3\2\2\2\67\u0154\3\2\2\29\u0159\3\2")
        buf.write("\2\2;\u015e\3\2\2\2=\u0160\3\2\2\2?\u0162\3\2\2\2A\u0165")
        buf.write("\3\2\2\2C\u0168\3\2\2\2E\u016b\3\2\2\2G\u016e\3\2\2\2")
        buf.write("I\u0170\3\2\2\2K\u0172\3\2\2\2M\u0174\3\2\2\2O\u0176\3")
        buf.write("\2\2\2Q\u0178\3\2\2\2S\u017a\3\2\2\2U\u017d\3\2\2\2W\u017f")
        buf.write("\3\2\2\2Y\u0182\3\2\2\2[\u0185\3\2\2\2]\u0189\3\2\2\2")
        buf.write("_\u018b\3\2\2\2a\u018d\3\2\2\2c\u018f\3\2\2\2e\u0191\3")
        buf.write("\2\2\2g\u0193\3\2\2\2i\u0196\3\2\2\2k\u0198\3\2\2\2m\u019a")
        buf.write("\3\2\2\2o\u019d\3\2\2\2q\u019f\3\2\2\2s\u01a1\3\2\2\2")
        buf.write("u\u01a3\3\2\2\2w\u01a5\3\2\2\2y\u01b5\3\2\2\2{\u01b7\3")
        buf.write("\2\2\2}\u01bd\3\2\2\2\177\u01c3\3\2\2\2\u0081\u01c5\3")
        buf.write("\2\2\2\u0083\u01c7\3\2\2\2\u0085\u01c9\3\2\2\2\u0087\u01cb")
        buf.write("\3\2\2\2\u0089\u01cd\3\2\2\2\u008b\u01e9\3\2\2\2\u008d")
        buf.write("\u01eb\3\2\2\2\u008f\u01fe\3\2\2\2\u0091\u0211\3\2\2\2")
        buf.write("\u0093\u022a\3\2\2\2\u0095\u023d\3\2\2\2\u0097\u024a\3")
        buf.write("\2\2\2\u0099\u024c\3\2\2\2\u009b\u0257\3\2\2\2\u009d\u025f")
        buf.write("\3\2\2\2\u009f\u0266\3\2\2\2\u00a1\u026c\3\2\2\2\u00a3")
        buf.write("\u00a4\7R\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7q\2\2\u00a6")
        buf.write("\u00a7\7i\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7c\2\2\u00a9")
        buf.write("\u00aa\7o\2\2\u00aa\4\3\2\2\2\u00ab\u00ac\7o\2\2\u00ac")
        buf.write("\u00ad\7g\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7j\2\2\u00af")
        buf.write("\u00b0\7q\2\2\u00b0\u00b1\7f\2\2\u00b1\u00b2\7\"\2\2\u00b2")
        buf.write("\u00b3\7d\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7f\2\2\u00b5")
        buf.write("\u00b6\7{\2\2\u00b6\6\3\2\2\2\u00b7\u00b8\7g\2\2\u00b8")
        buf.write("\u00b9\7z\2\2\u00b9\u00ba\7r\2\2\u00ba\u00bb\7t\2\2\u00bb")
        buf.write("\b\3\2\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be\7v\2\2\u00be")
        buf.write("\u00bf\7c\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7g\2\2\u00c1")
        buf.write("\u00c2\7o\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7p\2\2\u00c4")
        buf.write("\u00c5\7v\2\2\u00c5\n\3\2\2\2\u00c6\u00c7\7%\2\2\u00c7")
        buf.write("\u00c8\7%\2\2\u00c8\u00cc\3\2\2\2\u00c9\u00cb\13\2\2\2")
        buf.write("\u00ca\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00cd\3")
        buf.write("\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00cc")
        buf.write("\3\2\2\2\u00cf\u00d0\7%\2\2\u00d0\u00d1\7%\2\2\u00d1\u00d2")
        buf.write("\3\2\2\2\u00d2\u00d3\b\6\2\2\u00d3\f\3\2\2\2\u00d4\u00d5")
        buf.write("\7D\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8")
        buf.write("\7c\2\2\u00d8\u00d9\7m\2\2\u00d9\16\3\2\2\2\u00da\u00db")
        buf.write("\7E\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de")
        buf.write("\7v\2\2\u00de\u00df\7k\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1")
        buf.write("\7w\2\2\u00e1\u00e2\7g\2\2\u00e2\20\3\2\2\2\u00e3\u00e4")
        buf.write("\7K\2\2\u00e4\u00e5\7h\2\2\u00e5\22\3\2\2\2\u00e6\u00e7")
        buf.write("\7G\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec\7h\2\2\u00ec\24")
        buf.write("\3\2\2\2\u00ed\u00ee\7G\2\2\u00ee\u00ef\7n\2\2\u00ef\u00f0")
        buf.write("\7u\2\2\u00f0\u00f1\7g\2\2\u00f1\26\3\2\2\2\u00f2\u00f3")
        buf.write("\7H\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6")
        buf.write("\7g\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7e\2\2\u00f8\u00f9")
        buf.write("\7j\2\2\u00f9\30\3\2\2\2\u00fa\u00fb\7C\2\2\u00fb\u00fc")
        buf.write("\7t\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff")
        buf.write("\7{\2\2\u00ff\32\3\2\2\2\u0100\u0101\7K\2\2\u0101\u0102")
        buf.write("\7p\2\2\u0102\34\3\2\2\2\u0103\u0104\7K\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105\u0106\7v\2\2\u0106\36\3\2\2\2\u0107\u0108")
        buf.write("\7H\2\2\u0108\u0109\7n\2\2\u0109\u010a\7q\2\2\u010a\u010b")
        buf.write("\7c\2\2\u010b\u010c\7v\2\2\u010c \3\2\2\2\u010d\u010e")
        buf.write("\7D\2\2\u010e\u010f\7q\2\2\u010f\u0110\7q\2\2\u0110\u0111")
        buf.write("\7n\2\2\u0111\u0112\7g\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7p\2\2\u0114\"\3\2\2\2\u0115\u0116\7U\2\2\u0116\u0117")
        buf.write("\7v\2\2\u0117\u0118\7t\2\2\u0118\u0119\7k\2\2\u0119\u011a")
        buf.write("\7p\2\2\u011a\u011b\7i\2\2\u011b$\3\2\2\2\u011c\u011d")
        buf.write("\7T\2\2\u011d\u011e\7g\2\2\u011e\u011f\7v\2\2\u011f\u0120")
        buf.write("\7w\2\2\u0120\u0121\7t\2\2\u0121\u0122\7p\2\2\u0122&\3")
        buf.write("\2\2\2\u0123\u0124\7P\2\2\u0124\u0125\7w\2\2\u0125\u0126")
        buf.write("\7n\2\2\u0126\u0127\7n\2\2\u0127(\3\2\2\2\u0128\u0129")
        buf.write("\7E\2\2\u0129\u012a\7n\2\2\u012a\u012b\7c\2\2\u012b\u012c")
        buf.write("\7u\2\2\u012c\u012d\7u\2\2\u012d*\3\2\2\2\u012e\u012f")
        buf.write("\7X\2\2\u012f\u0130\7c\2\2\u0130\u0131\7n\2\2\u0131,\3")
        buf.write("\2\2\2\u0132\u0133\7X\2\2\u0133\u0134\7c\2\2\u0134\u0135")
        buf.write("\7t\2\2\u0135.\3\2\2\2\u0136\u0137\7E\2\2\u0137\u0138")
        buf.write("\7q\2\2\u0138\u0139\7p\2\2\u0139\u013a\7u\2\2\u013a\u013b")
        buf.write("\7v\2\2\u013b\u013c\7t\2\2\u013c\u013d\7w\2\2\u013d\u013e")
        buf.write("\7e\2\2\u013e\u013f\7v\2\2\u013f\u0140\7q\2\2\u0140\u0141")
        buf.write("\7t\2\2\u0141\60\3\2\2\2\u0142\u0143\7F\2\2\u0143\u0144")
        buf.write("\7g\2\2\u0144\u0145\7u\2\2\u0145\u0146\7v\2\2\u0146\u0147")
        buf.write("\7t\2\2\u0147\u0148\7w\2\2\u0148\u0149\7e\2\2\u0149\u014a")
        buf.write("\7v\2\2\u014a\u014b\7q\2\2\u014b\u014c\7t\2\2\u014c\62")
        buf.write("\3\2\2\2\u014d\u014e\7P\2\2\u014e\u014f\7g\2\2\u014f\u0150")
        buf.write("\7y\2\2\u0150\64\3\2\2\2\u0151\u0152\7D\2\2\u0152\u0153")
        buf.write("\7{\2\2\u0153\66\3\2\2\2\u0154\u0155\7o\2\2\u0155\u0156")
        buf.write("\7c\2\2\u0156\u0157\7k\2\2\u0157\u0158\7p\2\2\u01588\3")
        buf.write("\2\2\2\u0159\u015a\7u\2\2\u015a\u015b\7g\2\2\u015b\u015c")
        buf.write("\7n\2\2\u015c\u015d\7h\2\2\u015d:\3\2\2\2\u015e\u015f")
        buf.write("\7?\2\2\u015f<\3\2\2\2\u0160\u0161\7#\2\2\u0161>\3\2\2")
        buf.write("\2\u0162\u0163\7~\2\2\u0163\u0164\7~\2\2\u0164@\3\2\2")
        buf.write("\2\u0165\u0166\7(\2\2\u0166\u0167\7(\2\2\u0167B\3\2\2")
        buf.write("\2\u0168\u0169\7?\2\2\u0169\u016a\7?\2\2\u016aD\3\2\2")
        buf.write("\2\u016b\u016c\7#\2\2\u016c\u016d\7?\2\2\u016dF\3\2\2")
        buf.write("\2\u016e\u016f\7\'\2\2\u016fH\3\2\2\2\u0170\u0171\7-\2")
        buf.write("\2\u0171J\3\2\2\2\u0172\u0173\7/\2\2\u0173L\3\2\2\2\u0174")
        buf.write("\u0175\7,\2\2\u0175N\3\2\2\2\u0176\u0177\7\61\2\2\u0177")
        buf.write("P\3\2\2\2\u0178\u0179\7>\2\2\u0179R\3\2\2\2\u017a\u017b")
        buf.write("\7>\2\2\u017b\u017c\7?\2\2\u017cT\3\2\2\2\u017d\u017e")
        buf.write("\7@\2\2\u017eV\3\2\2\2\u017f\u0180\7@\2\2\u0180\u0181")
        buf.write("\7?\2\2\u0181X\3\2\2\2\u0182\u0183\7-\2\2\u0183\u0184")
        buf.write("\7\60\2\2\u0184Z\3\2\2\2\u0185\u0186\7?\2\2\u0186\u0187")
        buf.write("\7?\2\2\u0187\u0188\7\60\2\2\u0188\\\3\2\2\2\u0189\u018a")
        buf.write("\7*\2\2\u018a^\3\2\2\2\u018b\u018c\7+\2\2\u018c`\3\2\2")
        buf.write("\2\u018d\u018e\7]\2\2\u018eb\3\2\2\2\u018f\u0190\7_\2")
        buf.write("\2\u0190d\3\2\2\2\u0191\u0192\7\60\2\2\u0192f\3\2\2\2")
        buf.write("\u0193\u0194\7\60\2\2\u0194\u0195\7\60\2\2\u0195h\3\2")
        buf.write("\2\2\u0196\u0197\7.\2\2\u0197j\3\2\2\2\u0198\u0199\7<")
        buf.write("\2\2\u0199l\3\2\2\2\u019a\u019b\7<\2\2\u019b\u019c\7<")
        buf.write("\2\2\u019cn\3\2\2\2\u019d\u019e\7=\2\2\u019ep\3\2\2\2")
        buf.write("\u019f\u01a0\7}\2\2\u01a0r\3\2\2\2\u01a1\u01a2\7\177\2")
        buf.write("\2\u01a2t\3\2\2\2\u01a3\u01a4\7)\2\2\u01a4v\3\2\2\2\u01a5")
        buf.write("\u01a6\7$\2\2\u01a6x\3\2\2\2\u01a7\u01a8\7)\2\2\u01a8")
        buf.write("\u01b6\7$\2\2\u01a9\u01aa\7^\2\2\u01aa\u01b6\7d\2\2\u01ab")
        buf.write("\u01ac\7^\2\2\u01ac\u01b6\7h\2\2\u01ad\u01ae\7^\2\2\u01ae")
        buf.write("\u01b6\7t\2\2\u01af\u01b0\7^\2\2\u01b0\u01b6\7p\2\2\u01b1")
        buf.write("\u01b2\7^\2\2\u01b2\u01b6\7v\2\2\u01b3\u01b4\7^\2\2\u01b4")
        buf.write("\u01b6\7^\2\2\u01b5\u01a7\3\2\2\2\u01b5\u01a9\3\2\2\2")
        buf.write("\u01b5\u01ab\3\2\2\2\u01b5\u01ad\3\2\2\2\u01b5\u01af\3")
        buf.write("\2\2\2\u01b5\u01b1\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6z")
        buf.write("\3\2\2\2\u01b7\u01b8\7\62\2\2\u01b8|\3\2\2\2\u01b9\u01ba")
        buf.write("\7\62\2\2\u01ba\u01be\7z\2\2\u01bb\u01bc\7\62\2\2\u01bc")
        buf.write("\u01be\7Z\2\2\u01bd\u01b9\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01be~\3\2\2\2\u01bf\u01c0\7\62\2\2\u01c0\u01c4\7d\2")
        buf.write("\2\u01c1\u01c2\7\62\2\2\u01c2\u01c4\7D\2\2\u01c3\u01bf")
        buf.write("\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u0080\3\2\2\2\u01c5")
        buf.write("\u01c6\t\2\2\2\u01c6\u0082\3\2\2\2\u01c7\u01c8\t\3\2\2")
        buf.write("\u01c8\u0084\3\2\2\2\u01c9\u01ca\t\4\2\2\u01ca\u0086\3")
        buf.write("\2\2\2\u01cb\u01cc\t\5\2\2\u01cc\u0088\3\2\2\2\u01cd\u01cf")
        buf.write("\t\6\2\2\u01ce\u01d0\t\7\2\2\u01cf\u01ce\3\2\2\2\u01cf")
        buf.write("\u01d0\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01d3\5\u008b")
        buf.write("F\2\u01d2\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d2")
        buf.write("\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u008a\3\2\2\2\u01d6")
        buf.write("\u01ea\5\u0087D\2\u01d7\u01d9\t\b\2\2\u01d8\u01da\7a\2")
        buf.write("\2\u01d9\u01d8\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01e5")
        buf.write("\3\2\2\2\u01db\u01dd\5\u0087D\2\u01dc\u01db\3\2\2\2\u01dd")
        buf.write("\u01de\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2")
        buf.write("\u01df\u01e1\3\2\2\2\u01e0\u01e2\7a\2\2\u01e1\u01e0\3")
        buf.write("\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01dc")
        buf.write("\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e6\u01e8\3\2\2\2\u01e7\u01e5\3\2\2\2")
        buf.write("\u01e8\u01ea\5\u0087D\2\u01e9\u01d6\3\2\2\2\u01e9\u01d7")
        buf.write("\3\2\2\2\u01ea\u008c\3\2\2\2\u01eb\u01fc\5{>\2\u01ec\u01fd")
        buf.write("\7\62\2\2\u01ed\u01f8\t\t\2\2\u01ee\u01f0\5\u0083B\2\u01ef")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01ef\3\2\2\2")
        buf.write("\u01f1\u01f2\3\2\2\2\u01f2\u01f4\3\2\2\2\u01f3\u01f5\7")
        buf.write("a\2\2\u01f4\u01f3\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f7")
        buf.write("\3\2\2\2\u01f6\u01ef\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb\3\2\2\2")
        buf.write("\u01fa\u01f8\3\2\2\2\u01fb\u01fd\5\u0083B\2\u01fc\u01ec")
        buf.write("\3\2\2\2\u01fc\u01ed\3\2\2\2\u01fd\u008e\3\2\2\2\u01fe")
        buf.write("\u020f\5}?\2\u01ff\u0210\7\62\2\2\u0200\u020b\t\n\2\2")
        buf.write("\u0201\u0203\5\u0081A\2\u0202\u0201\3\2\2\2\u0203\u0204")
        buf.write("\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205")
        buf.write("\u0207\3\2\2\2\u0206\u0208\7a\2\2\u0207\u0206\3\2\2\2")
        buf.write("\u0207\u0208\3\2\2\2\u0208\u020a\3\2\2\2\u0209\u0202\3")
        buf.write("\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020c")
        buf.write("\3\2\2\2\u020c\u020e\3\2\2\2\u020d\u020b\3\2\2\2\u020e")
        buf.write("\u0210\5\u0081A\2\u020f\u01ff\3\2\2\2\u020f\u0200\3\2")
        buf.write("\2\2\u0210\u0090\3\2\2\2\u0211\u0222\5\177@\2\u0212\u0223")
        buf.write("\7\62\2\2\u0213\u021e\7\63\2\2\u0214\u0216\5\u0085C\2")
        buf.write("\u0215\u0214\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0215\3")
        buf.write("\2\2\2\u0217\u0218\3\2\2\2\u0218\u021a\3\2\2\2\u0219\u021b")
        buf.write("\7a\2\2\u021a\u0219\3\2\2\2\u021a\u021b\3\2\2\2\u021b")
        buf.write("\u021d\3\2\2\2\u021c\u0215\3\2\2\2\u021d\u0220\3\2\2\2")
        buf.write("\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0221\3")
        buf.write("\2\2\2\u0220\u021e\3\2\2\2\u0221\u0223\5\u0085C\2\u0222")
        buf.write("\u0212\3\2\2\2\u0222\u0213\3\2\2\2\u0223\u0092\3\2\2\2")
        buf.write("\u0224\u022b\5\u008bF\2\u0225\u022b\5\u008dG\2\u0226\u022b")
        buf.write("\5\u008fH\2\u0227\u0228\5\u0091I\2\u0228\u0229\bJ\3\2")
        buf.write("\u0229\u022b\3\2\2\2\u022a\u0224\3\2\2\2\u022a\u0225\3")
        buf.write("\2\2\2\u022a\u0226\3\2\2\2\u022a\u0227\3\2\2\2\u022b\u0094")
        buf.write("\3\2\2\2\u022c\u022d\5\u008bF\2\u022d\u022f\5e\63\2\u022e")
        buf.write("\u0230\5\u008bF\2\u022f\u022e\3\2\2\2\u022f\u0230\3\2")
        buf.write("\2\2\u0230\u0232\3\2\2\2\u0231\u0233\5\u0089E\2\u0232")
        buf.write("\u0231\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u023e\3\2\2\2")
        buf.write("\u0234\u0235\5\u008bF\2\u0235\u0236\5\u0089E\2\u0236\u023e")
        buf.write("\3\2\2\2\u0237\u0239\5e\63\2\u0238\u023a\5\u008bF\2\u0239")
        buf.write("\u0238\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u023b\3\2\2\2")
        buf.write("\u023b\u023c\5\u0089E\2\u023c\u023e\3\2\2\2\u023d\u022c")
        buf.write("\3\2\2\2\u023d\u0234\3\2\2\2\u023d\u0237\3\2\2\2\u023e")
        buf.write("\u023f\3\2\2\2\u023f\u0240\bK\4\2\u0240\u0096\3\2\2\2")
        buf.write("\u0241\u0242\7V\2\2\u0242\u0243\7t\2\2\u0243\u0244\7w")
        buf.write("\2\2\u0244\u024b\7g\2\2\u0245\u0246\7H\2\2\u0246\u0247")
        buf.write("\7c\2\2\u0247\u0248\7n\2\2\u0248\u0249\7u\2\2\u0249\u024b")
        buf.write("\7g\2\2\u024a\u0241\3\2\2\2\u024a\u0245\3\2\2\2\u024b")
        buf.write("\u0098\3\2\2\2\u024c\u0251\5w<\2\u024d\u0250\5y=\2\u024e")
        buf.write("\u0250\n\13\2\2\u024f\u024d\3\2\2\2\u024f\u024e\3\2\2")
        buf.write("\2\u0250\u0253\3\2\2\2\u0251\u0252\3\2\2\2\u0251\u024f")
        buf.write("\3\2\2\2\u0252\u0254\3\2\2\2\u0253\u0251\3\2\2\2\u0254")
        buf.write("\u0255\5w<\2\u0255\u009a\3\2\2\2\u0256\u0258\t\f\2\2\u0257")
        buf.write("\u0256\3\2\2\2\u0258\u025c\3\2\2\2\u0259\u025b\t\r\2\2")
        buf.write("\u025a\u0259\3\2\2\2\u025b\u025e\3\2\2\2\u025c\u025a\3")
        buf.write("\2\2\2\u025c\u025d\3\2\2\2\u025d\u009c\3\2\2\2\u025e\u025c")
        buf.write("\3\2\2\2\u025f\u0261\7&\2\2\u0260\u0262\t\r\2\2\u0261")
        buf.write("\u0260\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0261\3\2\2\2")
        buf.write("\u0263\u0264\3\2\2\2\u0264\u009e\3\2\2\2\u0265\u0267\t")
        buf.write("\16\2\2\u0266\u0265\3\2\2\2\u0267\u0268\3\2\2\2\u0268")
        buf.write("\u0266\3\2\2\2\u0268\u0269\3\2\2\2\u0269\u026a\3\2\2\2")
        buf.write("\u026a\u026b\bP\2\2\u026b\u00a0\3\2\2\2\u026c\u026d\13")
        buf.write("\2\2\2\u026d\u026e\bQ\5\2\u026e\u00a2\3\2\2\2(\2\u00cc")
        buf.write("\u01b5\u01bd\u01c3\u01cf\u01d4\u01d9\u01de\u01e1\u01e5")
        buf.write("\u01e9\u01f1\u01f4\u01f8\u01fc\u0204\u0207\u020b\u020f")
        buf.write("\u0217\u021a\u021e\u0222\u022a\u022f\u0232\u0239\u023d")
        buf.write("\u024a\u024f\u0251\u0257\u025a\u025c\u0261\u0263\u0268")
        buf.write("\6\b\2\2\3J\2\3K\3\3Q\4")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    COMMENT = 5
    K_BREAK = 6
    K_CONTINUE = 7
    K_IF = 8
    K_ELSE_IF = 9
    K_ELSE = 10
    K_FOR_EACH = 11
    K_ARRAY = 12
    K_IN = 13
    K_INT = 14
    K_FLOAT = 15
    K_BOOLEAN = 16
    K_STRING = 17
    K_RETURN = 18
    K_NULL = 19
    K_CLASS = 20
    K_VAL = 21
    K_VAR = 22
    K_CONSTRUCTOR = 23
    K_DESTRUCTOR = 24
    K_NEW = 25
    K_BY = 26
    K_MAIN = 27
    K_SELF = 28
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
    DOUBLE_DOT = 51
    COMMA = 52
    COLON = 53
    DOUBLE_COLON = 54
    SEMI_COLON = 55
    LEFT_CURLY_BRACKET = 56
    RIGHT_CURLY_BRACKET = 57
    ESCAPE = 58
    INTEGER_LITERAL = 59
    FLOAT_LITERAL = 60
    BOOLEAN_LITERAL = 61
    STRING_LITERAL = 62
    IDENTIFIER = 63
    DOLAR_IDENTIFIER = 64
    WHITE_SPACE = 65
    ERROR_TOKEN = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'method body'", "'expr'", "'statement'", "'Break'", 
            "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Array'", 
            "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", 
            "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'main'", "'self'", "'='", "'!'", "'||'", "'&&'", 
            "'=='", "'!='", "'%'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", 
            "'>'", "'>='", "'+.'", "'==.'", "'('", "')'", "'['", "']'", 
            "'.'", "'..'", "','", "':'", "'::'", "';'", "'{'", "'}'" ]

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
            "DOLAR_IDENTIFIER", "WHITE_SPACE", "ERROR_TOKEN" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "COMMENT", "K_BREAK", 
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
                  "IDENTIFIER", "DOLAR_IDENTIFIER", "WHITE_SPACE", "ERROR_TOKEN" ]

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
            actions[72] = self.INTEGER_LITERAL_action 
            actions[73] = self.FLOAT_LITERAL_action 
            actions[79] = self.ERROR_TOKEN_action 
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
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


