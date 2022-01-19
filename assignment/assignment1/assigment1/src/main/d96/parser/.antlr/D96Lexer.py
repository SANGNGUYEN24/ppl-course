# Generated from d:\Study2\HCMUT\semester212\PPL\code\assignment\assignment1\assigment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u025e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\7\6\u00c8\n\6\f\6\16\6\u00cb\13")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)")
        buf.write("\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\3:\3:\3:\3:")
        buf.write("\3:\3:\3:\3:\3:\3:\3:\5:\u01a8\n:\3;\3;\3<\3<\3<\3<\5")
        buf.write("<\u01b0\n<\3=\3=\3=\3=\5=\u01b6\n=\3>\3>\3?\3?\3@\3@\3")
        buf.write("A\3A\3B\3B\5B\u01c2\nB\3B\6B\u01c5\nB\rB\16B\u01c6\3C")
        buf.write("\3C\3C\5C\u01cc\nC\3C\6C\u01cf\nC\rC\16C\u01d0\3C\3C\7")
        buf.write("C\u01d5\nC\fC\16C\u01d8\13C\3C\6C\u01db\nC\rC\16C\u01dc")
        buf.write("\5C\u01df\nC\3D\3D\6D\u01e3\nD\rD\16D\u01e4\3D\3D\7D\u01e9")
        buf.write("\nD\fD\16D\u01ec\13D\3D\6D\u01ef\nD\rD\16D\u01f0\3E\3")
        buf.write("E\6E\u01f5\nE\rE\16E\u01f6\3E\3E\7E\u01fb\nE\fE\16E\u01fe")
        buf.write("\13E\3E\6E\u0201\nE\rE\16E\u0202\3F\3F\6F\u0207\nF\rF")
        buf.write("\16F\u0208\3F\3F\7F\u020d\nF\fF\16F\u0210\13F\3F\6F\u0213")
        buf.write("\nF\rF\16F\u0214\3G\3G\3G\3G\5G\u021b\nG\3G\3G\3H\3H\3")
        buf.write("H\5H\u0222\nH\3H\5H\u0225\nH\3H\3H\3H\3H\3H\5H\u022c\n")
        buf.write("H\3H\3H\5H\u0230\nH\3H\3H\3I\3I\3I\3I\3I\3I\3I\3I\3I\5")
        buf.write("I\u023d\nI\3J\3J\3J\7J\u0242\nJ\fJ\16J\u0245\13J\3J\3")
        buf.write("J\3K\5K\u024a\nK\3K\7K\u024d\nK\fK\16K\u0250\13K\3L\3")
        buf.write("L\6L\u0254\nL\rL\16L\u0255\3M\6M\u0259\nM\rM\16M\u025a")
        buf.write("\3M\3M\4\u00c9\u0243\2N\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o\2q\2s9u\2w\2y\2{\2}\2\177\2\u0081")
        buf.write("\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d:\u008f")
        buf.write(";\u0091<\u0093=\u0095>\u0097?\u0099@\3\2\r\5\2\62;CHc")
        buf.write("h\3\2\629\3\2\62\63\3\2\62;\4\2GGgg\4\2--//\3\2\63;\4")
        buf.write("\2$$^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2")
        buf.write("\u0276\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2s\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\3\u009b\3\2\2\2\5\u00a3\3\2\2\2\7\u00ad\3\2\2\2\t\u00b7")
        buf.write("\3\2\2\2\13\u00c3\3\2\2\2\r\u00d1\3\2\2\2\17\u00d7\3\2")
        buf.write("\2\2\21\u00e0\3\2\2\2\23\u00e3\3\2\2\2\25\u00ea\3\2\2")
        buf.write("\2\27\u00ef\3\2\2\2\31\u00f7\3\2\2\2\33\u00fd\3\2\2\2")
        buf.write("\35\u0100\3\2\2\2\37\u0104\3\2\2\2!\u010a\3\2\2\2#\u0112")
        buf.write("\3\2\2\2%\u0119\3\2\2\2\'\u0120\3\2\2\2)\u0125\3\2\2\2")
        buf.write("+\u012b\3\2\2\2-\u012f\3\2\2\2/\u0133\3\2\2\2\61\u013f")
        buf.write("\3\2\2\2\63\u014a\3\2\2\2\65\u014e\3\2\2\2\67\u0151\3")
        buf.write("\2\2\29\u0156\3\2\2\2;\u0158\3\2\2\2=\u015a\3\2\2\2?\u015d")
        buf.write("\3\2\2\2A\u0160\3\2\2\2C\u0163\3\2\2\2E\u0166\3\2\2\2")
        buf.write("G\u0168\3\2\2\2I\u016a\3\2\2\2K\u016c\3\2\2\2M\u016e\3")
        buf.write("\2\2\2O\u0170\3\2\2\2Q\u0172\3\2\2\2S\u0175\3\2\2\2U\u0177")
        buf.write("\3\2\2\2W\u017a\3\2\2\2Y\u017d\3\2\2\2[\u0181\3\2\2\2")
        buf.write("]\u0183\3\2\2\2_\u0185\3\2\2\2a\u0187\3\2\2\2c\u0189\3")
        buf.write("\2\2\2e\u018b\3\2\2\2g\u018d\3\2\2\2i\u018f\3\2\2\2k\u0191")
        buf.write("\3\2\2\2m\u0193\3\2\2\2o\u0195\3\2\2\2q\u0197\3\2\2\2")
        buf.write("s\u01a7\3\2\2\2u\u01a9\3\2\2\2w\u01af\3\2\2\2y\u01b5\3")
        buf.write("\2\2\2{\u01b7\3\2\2\2}\u01b9\3\2\2\2\177\u01bb\3\2\2\2")
        buf.write("\u0081\u01bd\3\2\2\2\u0083\u01bf\3\2\2\2\u0085\u01de\3")
        buf.write("\2\2\2\u0087\u01e0\3\2\2\2\u0089\u01f2\3\2\2\2\u008b\u0204")
        buf.write("\3\2\2\2\u008d\u021a\3\2\2\2\u008f\u022f\3\2\2\2\u0091")
        buf.write("\u023c\3\2\2\2\u0093\u023e\3\2\2\2\u0095\u0249\3\2\2\2")
        buf.write("\u0097\u0251\3\2\2\2\u0099\u0258\3\2\2\2\u009b\u009c\7")
        buf.write("R\2\2\u009c\u009d\7t\2\2\u009d\u009e\7q\2\2\u009e\u009f")
        buf.write("\7i\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2")
        buf.write("\7o\2\2\u00a2\4\3\2\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5")
        buf.write("\7v\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8")
        buf.write("\7k\2\2\u00a8\u00a9\7d\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\u00ac\7g\2\2\u00ac\6\3\2\2\2\u00ad\u00ae")
        buf.write("\7u\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3\7o\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7v\2\2\u00b6\b")
        buf.write("\3\2\2\2\u00b7\u00b8\7o\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba")
        buf.write("\7v\2\2\u00ba\u00bb\7j\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd")
        buf.write("\7f\2\2\u00bd\u00be\7\"\2\2\u00be\u00bf\7d\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7f\2\2\u00c1\u00c2\7{\2\2\u00c2\n")
        buf.write("\3\2\2\2\u00c3\u00c4\7%\2\2\u00c4\u00c5\7%\2\2\u00c5\u00c9")
        buf.write("\3\2\2\2\u00c6\u00c8\13\2\2\2\u00c7\u00c6\3\2\2\2\u00c8")
        buf.write("\u00cb\3\2\2\2\u00c9\u00ca\3\2\2\2\u00c9\u00c7\3\2\2\2")
        buf.write("\u00ca\u00cc\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\7")
        buf.write("%\2\2\u00cd\u00ce\7%\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0")
        buf.write("\b\6\2\2\u00d0\f\3\2\2\2\u00d1\u00d2\7D\2\2\u00d2\u00d3")
        buf.write("\7t\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6")
        buf.write("\7m\2\2\u00d6\16\3\2\2\2\u00d7\u00d8\7E\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7v\2\2\u00db\u00dc")
        buf.write("\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7w\2\2\u00de\u00df")
        buf.write("\7g\2\2\u00df\20\3\2\2\2\u00e0\u00e1\7K\2\2\u00e1\u00e2")
        buf.write("\7h\2\2\u00e2\22\3\2\2\2\u00e3\u00e4\7G\2\2\u00e4\u00e5")
        buf.write("\7n\2\2\u00e5\u00e6\7u\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8")
        buf.write("\7k\2\2\u00e8\u00e9\7h\2\2\u00e9\24\3\2\2\2\u00ea\u00eb")
        buf.write("\7G\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee\26\3\2\2\2\u00ef\u00f0\7H\2\2\u00f0\u00f1")
        buf.write("\7q\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4")
        buf.write("\7c\2\2\u00f4\u00f5\7e\2\2\u00f5\u00f6\7j\2\2\u00f6\30")
        buf.write("\3\2\2\2\u00f7\u00f8\7C\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7{\2\2\u00fc\32")
        buf.write("\3\2\2\2\u00fd\u00fe\7K\2\2\u00fe\u00ff\7p\2\2\u00ff\34")
        buf.write("\3\2\2\2\u0100\u0101\7K\2\2\u0101\u0102\7p\2\2\u0102\u0103")
        buf.write("\7v\2\2\u0103\36\3\2\2\2\u0104\u0105\7H\2\2\u0105\u0106")
        buf.write("\7n\2\2\u0106\u0107\7q\2\2\u0107\u0108\7c\2\2\u0108\u0109")
        buf.write("\7v\2\2\u0109 \3\2\2\2\u010a\u010b\7D\2\2\u010b\u010c")
        buf.write("\7q\2\2\u010c\u010d\7q\2\2\u010d\u010e\7n\2\2\u010e\u010f")
        buf.write("\7g\2\2\u010f\u0110\7c\2\2\u0110\u0111\7p\2\2\u0111\"")
        buf.write("\3\2\2\2\u0112\u0113\7U\2\2\u0113\u0114\7v\2\2\u0114\u0115")
        buf.write("\7t\2\2\u0115\u0116\7k\2\2\u0116\u0117\7p\2\2\u0117\u0118")
        buf.write("\7i\2\2\u0118$\3\2\2\2\u0119\u011a\7T\2\2\u011a\u011b")
        buf.write("\7g\2\2\u011b\u011c\7v\2\2\u011c\u011d\7w\2\2\u011d\u011e")
        buf.write("\7t\2\2\u011e\u011f\7p\2\2\u011f&\3\2\2\2\u0120\u0121")
        buf.write("\7P\2\2\u0121\u0122\7w\2\2\u0122\u0123\7n\2\2\u0123\u0124")
        buf.write("\7n\2\2\u0124(\3\2\2\2\u0125\u0126\7E\2\2\u0126\u0127")
        buf.write("\7n\2\2\u0127\u0128\7c\2\2\u0128\u0129\7u\2\2\u0129\u012a")
        buf.write("\7u\2\2\u012a*\3\2\2\2\u012b\u012c\7X\2\2\u012c\u012d")
        buf.write("\7c\2\2\u012d\u012e\7n\2\2\u012e,\3\2\2\2\u012f\u0130")
        buf.write("\7X\2\2\u0130\u0131\7c\2\2\u0131\u0132\7t\2\2\u0132.\3")
        buf.write("\2\2\2\u0133\u0134\7E\2\2\u0134\u0135\7q\2\2\u0135\u0136")
        buf.write("\7p\2\2\u0136\u0137\7u\2\2\u0137\u0138\7v\2\2\u0138\u0139")
        buf.write("\7t\2\2\u0139\u013a\7w\2\2\u013a\u013b\7e\2\2\u013b\u013c")
        buf.write("\7v\2\2\u013c\u013d\7q\2\2\u013d\u013e\7t\2\2\u013e\60")
        buf.write("\3\2\2\2\u013f\u0140\7F\2\2\u0140\u0141\7g\2\2\u0141\u0142")
        buf.write("\7u\2\2\u0142\u0143\7v\2\2\u0143\u0144\7t\2\2\u0144\u0145")
        buf.write("\7w\2\2\u0145\u0146\7e\2\2\u0146\u0147\7v\2\2\u0147\u0148")
        buf.write("\7q\2\2\u0148\u0149\7t\2\2\u0149\62\3\2\2\2\u014a\u014b")
        buf.write("\7P\2\2\u014b\u014c\7g\2\2\u014c\u014d\7y\2\2\u014d\64")
        buf.write("\3\2\2\2\u014e\u014f\7D\2\2\u014f\u0150\7{\2\2\u0150\66")
        buf.write("\3\2\2\2\u0151\u0152\7o\2\2\u0152\u0153\7c\2\2\u0153\u0154")
        buf.write("\7k\2\2\u0154\u0155\7p\2\2\u01558\3\2\2\2\u0156\u0157")
        buf.write("\7?\2\2\u0157:\3\2\2\2\u0158\u0159\7#\2\2\u0159<\3\2\2")
        buf.write("\2\u015a\u015b\7~\2\2\u015b\u015c\7~\2\2\u015c>\3\2\2")
        buf.write("\2\u015d\u015e\7(\2\2\u015e\u015f\7(\2\2\u015f@\3\2\2")
        buf.write("\2\u0160\u0161\7?\2\2\u0161\u0162\7?\2\2\u0162B\3\2\2")
        buf.write("\2\u0163\u0164\7#\2\2\u0164\u0165\7?\2\2\u0165D\3\2\2")
        buf.write("\2\u0166\u0167\7\'\2\2\u0167F\3\2\2\2\u0168\u0169\7-\2")
        buf.write("\2\u0169H\3\2\2\2\u016a\u016b\7/\2\2\u016bJ\3\2\2\2\u016c")
        buf.write("\u016d\7,\2\2\u016dL\3\2\2\2\u016e\u016f\7\61\2\2\u016f")
        buf.write("N\3\2\2\2\u0170\u0171\7>\2\2\u0171P\3\2\2\2\u0172\u0173")
        buf.write("\7>\2\2\u0173\u0174\7?\2\2\u0174R\3\2\2\2\u0175\u0176")
        buf.write("\7@\2\2\u0176T\3\2\2\2\u0177\u0178\7@\2\2\u0178\u0179")
        buf.write("\7?\2\2\u0179V\3\2\2\2\u017a\u017b\7-\2\2\u017b\u017c")
        buf.write("\7\60\2\2\u017cX\3\2\2\2\u017d\u017e\7?\2\2\u017e\u017f")
        buf.write("\7?\2\2\u017f\u0180\7\60\2\2\u0180Z\3\2\2\2\u0181\u0182")
        buf.write("\7*\2\2\u0182\\\3\2\2\2\u0183\u0184\7+\2\2\u0184^\3\2")
        buf.write("\2\2\u0185\u0186\7]\2\2\u0186`\3\2\2\2\u0187\u0188\7_")
        buf.write("\2\2\u0188b\3\2\2\2\u0189\u018a\7\60\2\2\u018ad\3\2\2")
        buf.write("\2\u018b\u018c\7.\2\2\u018cf\3\2\2\2\u018d\u018e\7<\2")
        buf.write("\2\u018eh\3\2\2\2\u018f\u0190\7=\2\2\u0190j\3\2\2\2\u0191")
        buf.write("\u0192\7}\2\2\u0192l\3\2\2\2\u0193\u0194\7\177\2\2\u0194")
        buf.write("n\3\2\2\2\u0195\u0196\7)\2\2\u0196p\3\2\2\2\u0197\u0198")
        buf.write("\7$\2\2\u0198r\3\2\2\2\u0199\u019a\7)\2\2\u019a\u01a8")
        buf.write("\7$\2\2\u019b\u019c\7^\2\2\u019c\u01a8\7d\2\2\u019d\u019e")
        buf.write("\7^\2\2\u019e\u01a8\7h\2\2\u019f\u01a0\7^\2\2\u01a0\u01a8")
        buf.write("\7t\2\2\u01a1\u01a2\7^\2\2\u01a2\u01a8\7p\2\2\u01a3\u01a4")
        buf.write("\7^\2\2\u01a4\u01a8\7v\2\2\u01a5\u01a6\7^\2\2\u01a6\u01a8")
        buf.write("\7^\2\2\u01a7\u0199\3\2\2\2\u01a7\u019b\3\2\2\2\u01a7")
        buf.write("\u019d\3\2\2\2\u01a7\u019f\3\2\2\2\u01a7\u01a1\3\2\2\2")
        buf.write("\u01a7\u01a3\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8t\3\2\2")
        buf.write("\2\u01a9\u01aa\7\62\2\2\u01aav\3\2\2\2\u01ab\u01ac\7\62")
        buf.write("\2\2\u01ac\u01b0\7z\2\2\u01ad\u01ae\7\62\2\2\u01ae\u01b0")
        buf.write("\7Z\2\2\u01af\u01ab\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0")
        buf.write("x\3\2\2\2\u01b1\u01b2\7\62\2\2\u01b2\u01b6\7d\2\2\u01b3")
        buf.write("\u01b4\7\62\2\2\u01b4\u01b6\7D\2\2\u01b5\u01b1\3\2\2\2")
        buf.write("\u01b5\u01b3\3\2\2\2\u01b6z\3\2\2\2\u01b7\u01b8\t\2\2")
        buf.write("\2\u01b8|\3\2\2\2\u01b9\u01ba\t\3\2\2\u01ba~\3\2\2\2\u01bb")
        buf.write("\u01bc\t\4\2\2\u01bc\u0080\3\2\2\2\u01bd\u01be\t\5\2\2")
        buf.write("\u01be\u0082\3\2\2\2\u01bf\u01c1\t\6\2\2\u01c0\u01c2\t")
        buf.write("\7\2\2\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c4")
        buf.write("\3\2\2\2\u01c3\u01c5\5\u0085C\2\u01c4\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2")
        buf.write("\u01c7\u0084\3\2\2\2\u01c8\u01df\5\u0081A\2\u01c9\u01cb")
        buf.write("\t\b\2\2\u01ca\u01cc\7a\2\2\u01cb\u01ca\3\2\2\2\u01cb")
        buf.write("\u01cc\3\2\2\2\u01cc\u01d6\3\2\2\2\u01cd\u01cf\5\u0081")
        buf.write("A\2\u01ce\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01ce")
        buf.write("\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2")
        buf.write("\u01d3\7a\2\2\u01d3\u01d5\3\2\2\2\u01d4\u01ce\3\2\2\2")
        buf.write("\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3")
        buf.write("\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01db")
        buf.write("\5\u0081A\2\u01da\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc")
        buf.write("\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2")
        buf.write("\u01de\u01c8\3\2\2\2\u01de\u01c9\3\2\2\2\u01df\u0086\3")
        buf.write("\2\2\2\u01e0\u01ea\5u;\2\u01e1\u01e3\5}?\2\u01e2\u01e1")
        buf.write("\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4")
        buf.write("\u01e5\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\7a\2\2")
        buf.write("\u01e7\u01e9\3\2\2\2\u01e8\u01e2\3\2\2\2\u01e9\u01ec\3")
        buf.write("\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ee")
        buf.write("\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ef\5}?\2\u01ee\u01ed")
        buf.write("\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0")
        buf.write("\u01f1\3\2\2\2\u01f1\u0088\3\2\2\2\u01f2\u01fc\5w<\2\u01f3")
        buf.write("\u01f5\5{>\2\u01f4\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write("\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u01f9\7a\2\2\u01f9\u01fb\3\2\2\2\u01fa\u01f4\3")
        buf.write("\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fd")
        buf.write("\3\2\2\2\u01fd\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01ff")
        buf.write("\u0201\5{>\2\u0200\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202")
        buf.write("\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u008a\3\2\2\2")
        buf.write("\u0204\u020e\5y=\2\u0205\u0207\5\177@\2\u0206\u0205\3")
        buf.write("\2\2\2\u0207\u0208\3\2\2\2\u0208\u0206\3\2\2\2\u0208\u0209")
        buf.write("\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020b\7a\2\2\u020b")
        buf.write("\u020d\3\2\2\2\u020c\u0206\3\2\2\2\u020d\u0210\3\2\2\2")
        buf.write("\u020e\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0212\3")
        buf.write("\2\2\2\u0210\u020e\3\2\2\2\u0211\u0213\5\177@\2\u0212")
        buf.write("\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0212\3\2\2\2")
        buf.write("\u0214\u0215\3\2\2\2\u0215\u008c\3\2\2\2\u0216\u021b\5")
        buf.write("\u0085C\2\u0217\u021b\5\u0087D\2\u0218\u021b\5\u0089E")
        buf.write("\2\u0219\u021b\5\u008bF\2\u021a\u0216\3\2\2\2\u021a\u0217")
        buf.write("\3\2\2\2\u021a\u0218\3\2\2\2\u021a\u0219\3\2\2\2\u021b")
        buf.write("\u021c\3\2\2\2\u021c\u021d\bG\3\2\u021d\u008e\3\2\2\2")
        buf.write("\u021e\u021f\5\u0085C\2\u021f\u0221\5c\62\2\u0220\u0222")
        buf.write("\5\u0085C\2\u0221\u0220\3\2\2\2\u0221\u0222\3\2\2\2\u0222")
        buf.write("\u0224\3\2\2\2\u0223\u0225\5\u0083B\2\u0224\u0223\3\2")
        buf.write("\2\2\u0224\u0225\3\2\2\2\u0225\u0230\3\2\2\2\u0226\u0227")
        buf.write("\5\u0085C\2\u0227\u0228\5\u0083B\2\u0228\u0230\3\2\2\2")
        buf.write("\u0229\u022b\5c\62\2\u022a\u022c\5\u0085C\2\u022b\u022a")
        buf.write("\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022d\3\2\2\2\u022d")
        buf.write("\u022e\5\u0083B\2\u022e\u0230\3\2\2\2\u022f\u021e\3\2")
        buf.write("\2\2\u022f\u0226\3\2\2\2\u022f\u0229\3\2\2\2\u0230\u0231")
        buf.write("\3\2\2\2\u0231\u0232\bH\4\2\u0232\u0090\3\2\2\2\u0233")
        buf.write("\u0234\7V\2\2\u0234\u0235\7t\2\2\u0235\u0236\7w\2\2\u0236")
        buf.write("\u023d\7g\2\2\u0237\u0238\7H\2\2\u0238\u0239\7c\2\2\u0239")
        buf.write("\u023a\7n\2\2\u023a\u023b\7u\2\2\u023b\u023d\7g\2\2\u023c")
        buf.write("\u0233\3\2\2\2\u023c\u0237\3\2\2\2\u023d\u0092\3\2\2\2")
        buf.write("\u023e\u0243\5q9\2\u023f\u0242\5s:\2\u0240\u0242\n\t\2")
        buf.write("\2\u0241\u023f\3\2\2\2\u0241\u0240\3\2\2\2\u0242\u0245")
        buf.write("\3\2\2\2\u0243\u0244\3\2\2\2\u0243\u0241\3\2\2\2\u0244")
        buf.write("\u0246\3\2\2\2\u0245\u0243\3\2\2\2\u0246\u0247\5q9\2\u0247")
        buf.write("\u0094\3\2\2\2\u0248\u024a\t\n\2\2\u0249\u0248\3\2\2\2")
        buf.write("\u024a\u024e\3\2\2\2\u024b\u024d\t\13\2\2\u024c\u024b")
        buf.write("\3\2\2\2\u024d\u0250\3\2\2\2\u024e\u024c\3\2\2\2\u024e")
        buf.write("\u024f\3\2\2\2\u024f\u0096\3\2\2\2\u0250\u024e\3\2\2\2")
        buf.write("\u0251\u0253\7&\2\2\u0252\u0254\t\13\2\2\u0253\u0252\3")
        buf.write("\2\2\2\u0254\u0255\3\2\2\2\u0255\u0253\3\2\2\2\u0255\u0256")
        buf.write("\3\2\2\2\u0256\u0098\3\2\2\2\u0257\u0259\t\f\2\2\u0258")
        buf.write("\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u0258\3\2\2\2")
        buf.write("\u025a\u025b\3\2\2\2\u025b\u025c\3\2\2\2\u025c\u025d\b")
        buf.write("M\2\2\u025d\u009a\3\2\2\2%\2\u00c9\u01a7\u01af\u01b5\u01c1")
        buf.write("\u01c6\u01cb\u01d0\u01d6\u01dc\u01de\u01e4\u01ea\u01f0")
        buf.write("\u01f6\u01fc\u0202\u0208\u020e\u0214\u021a\u0221\u0224")
        buf.write("\u022b\u022f\u023c\u0241\u0243\u0249\u024c\u024e\u0253")
        buf.write("\u0255\u025a\5\b\2\2\3G\2\3H\3")
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
    OP_ASSIGN = 28
    OP_LOGICAL_NOT = 29
    OP_LOGICAL_OR = 30
    OP_LOGICAL_AND = 31
    OP_IS_EQUAL_TO = 32
    OP_NOT_EQUAL_TO = 33
    OP_MODULO = 34
    OP_ADDTION = 35
    OP_SUBTRACTION = 36
    OP_MULTIPLICATION = 37
    OP_DIVISION = 38
    OP_LESS_THAN = 39
    OP_LESS_THAN_EQUAL = 40
    OP_GREATER_THAN = 41
    OP_GREATER_THAN_EQUAL = 42
    OP_STRING_CONCATENATION = 43
    OP_TWO_SAME_STRING = 44
    LEFT_PAREN = 45
    RIGHT_PAREN = 46
    LEFT_SQUARE_BRACKET = 47
    RIGHT_SQUARE_BRACKET = 48
    DOT = 49
    COMMA = 50
    COLON = 51
    SEMICOLON = 52
    LEFT_CURLY_BRACKET = 53
    RIGHT_CURLY_BRACKET = 54
    ESCAPE = 55
    LITERAL_INTEGER = 56
    LITERAL_FLOAT = 57
    LITERAL_BOOLEAN = 58
    LITERAL_STRING = 59
    IDENTIFER = 60
    DOLAR_IDENTIFIER = 61
    WHITE_SPACE = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'attribute'", "'statement'", "'method body'", 
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
            "DOT", "COMMA", "COLON", "SEMICOLON", "LEFT_CURLY_BRACKET", 
            "RIGHT_CURLY_BRACKET", "ESCAPE", "LITERAL_INTEGER", "LITERAL_FLOAT", 
            "LITERAL_BOOLEAN", "LITERAL_STRING", "IDENTIFER", "DOLAR_IDENTIFIER", 
            "WHITE_SPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "COMMENT", "K_BREAK", 
                  "K_CONTINUE", "K_IF", "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", 
                  "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", 
                  "K_RETURN", "K_NULL", "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", 
                  "K_DESTRUCTOR", "K_NEW", "K_BY", "K_MAIN", "OP_ASSIGN", 
                  "OP_LOGICAL_NOT", "OP_LOGICAL_OR", "OP_LOGICAL_AND", "OP_IS_EQUAL_TO", 
                  "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", "OP_SUBTRACTION", 
                  "OP_MULTIPLICATION", "OP_DIVISION", "OP_LESS_THAN", "OP_LESS_THAN_EQUAL", 
                  "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", "OP_STRING_CONCATENATION", 
                  "OP_TWO_SAME_STRING", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", 
                  "RIGHT_SQUARE_BRACKET", "DOT", "COMMA", "COLON", "SEMICOLON", 
                  "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "SINGLE_QUOTE", 
                  "DOUBLE_QUOTE", "ESCAPE", "OCTAL_NOTATION", "HEXA_NOTATION", 
                  "BINARY_NOTATION", "HEXA_DIGIT", "OCTAL_DIGIT", "BINARY_DIGIT", 
                  "DECIMAL_DIGIT", "EXPONENT", "DECIMAL", "OCTAL", "HEXA", 
                  "BINARY", "LITERAL_INTEGER", "LITERAL_FLOAT", "LITERAL_BOOLEAN", 
                  "LITERAL_STRING", "IDENTIFER", "DOLAR_IDENTIFIER", "WHITE_SPACE" ]

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
            actions[69] = self.LITERAL_INTEGER_action 
            actions[70] = self.LITERAL_FLOAT_action 
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
     


