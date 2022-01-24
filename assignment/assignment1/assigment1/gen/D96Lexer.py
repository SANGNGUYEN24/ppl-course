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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0281\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3\u00b1\n\3\r\3\16\3\u00b2")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00bb\n\4\f\4\16\4\u00be")
        buf.write("\13\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;")
        buf.write("\3;\3;\3;\3;\3;\5;\u01a7\n;\3<\3<\3=\3=\3=\3=\5=\u01af")
        buf.write("\n=\3>\3>\3>\3>\5>\u01b5\n>\3?\3?\3@\3@\3A\3A\3B\3B\3")
        buf.write("C\3C\3C\7C\u01c2\nC\fC\16C\u01c5\13C\3C\3C\6C\u01c9\n")
        buf.write("C\rC\16C\u01ca\7C\u01cd\nC\fC\16C\u01d0\13C\5C\u01d2\n")
        buf.write("C\3D\3D\3D\3D\7D\u01d8\nD\fD\16D\u01db\13D\3D\3D\6D\u01df")
        buf.write("\nD\rD\16D\u01e0\7D\u01e3\nD\fD\16D\u01e6\13D\5D\u01e8")
        buf.write("\nD\3E\3E\3E\3E\7E\u01ee\nE\fE\16E\u01f1\13E\3E\3E\6E")
        buf.write("\u01f5\nE\rE\16E\u01f6\7E\u01f9\nE\fE\16E\u01fc\13E\5")
        buf.write("E\u01fe\nE\3F\3F\3F\3F\7F\u0204\nF\fF\16F\u0207\13F\3")
        buf.write("F\3F\6F\u020b\nF\rF\16F\u020c\7F\u020f\nF\fF\16F\u0212")
        buf.write("\13F\5F\u0214\nF\3G\3G\3G\3G\5G\u021a\nG\3G\3G\3H\3H\3")
        buf.write("I\3I\7I\u0222\nI\fI\16I\u0225\13I\3J\3J\5J\u0229\nJ\3")
        buf.write("J\6J\u022c\nJ\rJ\16J\u022d\3K\3K\3K\5K\u0233\nK\3K\3K")
        buf.write("\3K\3K\3K\3K\5K\u023b\nK\3K\3K\3L\3L\3L\3L\3L\3L\3L\3")
        buf.write("L\3L\5L\u0248\nL\3M\3M\3M\3M\5M\u024e\nM\3N\3N\7N\u0252")
        buf.write("\nN\fN\16N\u0255\13N\3N\3N\3O\5O\u025a\nO\3O\7O\u025d")
        buf.write("\nO\fO\16O\u0260\13O\3P\3P\6P\u0264\nP\rP\16P\u0265\3")
        buf.write("Q\3Q\7Q\u026a\nQ\fQ\16Q\u026d\13Q\3Q\5Q\u0270\nQ\3Q\3")
        buf.write("Q\3R\3R\7R\u0276\nR\fR\16R\u0279\13R\3R\3R\3R\3R\3S\3")
        buf.write("S\3S\3\u00bc\2T\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083")
        buf.write("\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d:\u008f\2\u0091")
        buf.write("\2\u0093\2\u0095;\u0097<\u0099\2\u009b=\u009d>\u009f?")
        buf.write("\u00a1@\u00a3A\u00a5B\3\2\21\5\2\13\f\17\17\"\"\4\2\62")
        buf.write(";CH\3\2\629\3\2\62\63\3\2\62;\3\2\63;\3\2\639\4\2\63;")
        buf.write("CH\4\2GGgg\4\2--//\6\2\f\f$$))^^\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\6\3\n\f\16\17))^^\n\2$$))^^ddhhppttvv\2\u029a\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\3\u00a7\3\2\2\2\5\u00b0\3\2\2")
        buf.write("\2\7\u00b6\3\2\2\2\t\u00c4\3\2\2\2\13\u00ca\3\2\2\2\r")
        buf.write("\u00d3\3\2\2\2\17\u00d6\3\2\2\2\21\u00dd\3\2\2\2\23\u00e2")
        buf.write("\3\2\2\2\25\u00ea\3\2\2\2\27\u00f0\3\2\2\2\31\u00f3\3")
        buf.write("\2\2\2\33\u00f7\3\2\2\2\35\u00fd\3\2\2\2\37\u0105\3\2")
        buf.write("\2\2!\u010c\3\2\2\2#\u0113\3\2\2\2%\u0118\3\2\2\2\'\u011e")
        buf.write("\3\2\2\2)\u0122\3\2\2\2+\u0126\3\2\2\2-\u0132\3\2\2\2")
        buf.write("/\u013d\3\2\2\2\61\u0141\3\2\2\2\63\u0144\3\2\2\2\65\u0149")
        buf.write("\3\2\2\2\67\u014e\3\2\2\29\u0150\3\2\2\2;\u0152\3\2\2")
        buf.write("\2=\u0155\3\2\2\2?\u0158\3\2\2\2A\u015b\3\2\2\2C\u015e")
        buf.write("\3\2\2\2E\u0160\3\2\2\2G\u0162\3\2\2\2I\u0164\3\2\2\2")
        buf.write("K\u0166\3\2\2\2M\u0168\3\2\2\2O\u016a\3\2\2\2Q\u016d\3")
        buf.write("\2\2\2S\u016f\3\2\2\2U\u0172\3\2\2\2W\u0175\3\2\2\2Y\u0179")
        buf.write("\3\2\2\2[\u017b\3\2\2\2]\u017d\3\2\2\2_\u017f\3\2\2\2")
        buf.write("a\u0181\3\2\2\2c\u0183\3\2\2\2e\u0186\3\2\2\2g\u0188\3")
        buf.write("\2\2\2i\u018a\3\2\2\2k\u018d\3\2\2\2m\u018f\3\2\2\2o\u0191")
        buf.write("\3\2\2\2q\u0193\3\2\2\2s\u0195\3\2\2\2u\u01a6\3\2\2\2")
        buf.write("w\u01a8\3\2\2\2y\u01ae\3\2\2\2{\u01b4\3\2\2\2}\u01b6\3")
        buf.write("\2\2\2\177\u01b8\3\2\2\2\u0081\u01ba\3\2\2\2\u0083\u01bc")
        buf.write("\3\2\2\2\u0085\u01d1\3\2\2\2\u0087\u01d3\3\2\2\2\u0089")
        buf.write("\u01e9\3\2\2\2\u008b\u01ff\3\2\2\2\u008d\u0219\3\2\2\2")
        buf.write("\u008f\u021d\3\2\2\2\u0091\u021f\3\2\2\2\u0093\u0226\3")
        buf.write("\2\2\2\u0095\u023a\3\2\2\2\u0097\u0247\3\2\2\2\u0099\u024d")
        buf.write("\3\2\2\2\u009b\u024f\3\2\2\2\u009d\u0259\3\2\2\2\u009f")
        buf.write("\u0261\3\2\2\2\u00a1\u0267\3\2\2\2\u00a3\u0273\3\2\2\2")
        buf.write("\u00a5\u027e\3\2\2\2\u00a7\u00a8\7R\2\2\u00a8\u00a9\7")
        buf.write("t\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7i\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7o\2\2\u00ae\4")
        buf.write("\3\2\2\2\u00af\u00b1\t\2\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\u00b2\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\u00b4\3\2\2\2\u00b4\u00b5\b\3\2\2\u00b5\6\3\2\2")
        buf.write("\2\u00b6\u00b7\7%\2\2\u00b7\u00b8\7%\2\2\u00b8\u00bc\3")
        buf.write("\2\2\2\u00b9\u00bb\13\2\2\2\u00ba\u00b9\3\2\2\2\u00bb")
        buf.write("\u00be\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bc\u00ba\3\2\2\2")
        buf.write("\u00bd\u00bf\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\7")
        buf.write("%\2\2\u00c0\u00c1\7%\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3")
        buf.write("\b\4\2\2\u00c3\b\3\2\2\2\u00c4\u00c5\7D\2\2\u00c5\u00c6")
        buf.write("\7t\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9")
        buf.write("\7m\2\2\u00c9\n\3\2\2\2\u00ca\u00cb\7E\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf")
        buf.write("\7k\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2")
        buf.write("\7g\2\2\u00d2\f\3\2\2\2\u00d3\u00d4\7K\2\2\u00d4\u00d5")
        buf.write("\7h\2\2\u00d5\16\3\2\2\2\u00d6\u00d7\7G\2\2\u00d7\u00d8")
        buf.write("\7n\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da\7g\2\2\u00da\u00db")
        buf.write("\7k\2\2\u00db\u00dc\7h\2\2\u00dc\20\3\2\2\2\u00dd\u00de")
        buf.write("\7G\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1")
        buf.write("\7g\2\2\u00e1\22\3\2\2\2\u00e2\u00e3\7H\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7")
        buf.write("\7c\2\2\u00e7\u00e8\7e\2\2\u00e8\u00e9\7j\2\2\u00e9\24")
        buf.write("\3\2\2\2\u00ea\u00eb\7C\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7{\2\2\u00ef\26")
        buf.write("\3\2\2\2\u00f0\u00f1\7K\2\2\u00f1\u00f2\7p\2\2\u00f2\30")
        buf.write("\3\2\2\2\u00f3\u00f4\7K\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6")
        buf.write("\7v\2\2\u00f6\32\3\2\2\2\u00f7\u00f8\7H\2\2\u00f8\u00f9")
        buf.write("\7n\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7v\2\2\u00fc\34\3\2\2\2\u00fd\u00fe\7D\2\2\u00fe\u00ff")
        buf.write("\7q\2\2\u00ff\u0100\7q\2\2\u0100\u0101\7n\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102\u0103\7c\2\2\u0103\u0104\7p\2\2\u0104\36")
        buf.write("\3\2\2\2\u0105\u0106\7U\2\2\u0106\u0107\7v\2\2\u0107\u0108")
        buf.write("\7t\2\2\u0108\u0109\7k\2\2\u0109\u010a\7p\2\2\u010a\u010b")
        buf.write("\7i\2\2\u010b \3\2\2\2\u010c\u010d\7T\2\2\u010d\u010e")
        buf.write("\7g\2\2\u010e\u010f\7v\2\2\u010f\u0110\7w\2\2\u0110\u0111")
        buf.write("\7t\2\2\u0111\u0112\7p\2\2\u0112\"\3\2\2\2\u0113\u0114")
        buf.write("\7P\2\2\u0114\u0115\7w\2\2\u0115\u0116\7n\2\2\u0116\u0117")
        buf.write("\7n\2\2\u0117$\3\2\2\2\u0118\u0119\7E\2\2\u0119\u011a")
        buf.write("\7n\2\2\u011a\u011b\7c\2\2\u011b\u011c\7u\2\2\u011c\u011d")
        buf.write("\7u\2\2\u011d&\3\2\2\2\u011e\u011f\7X\2\2\u011f\u0120")
        buf.write("\7c\2\2\u0120\u0121\7n\2\2\u0121(\3\2\2\2\u0122\u0123")
        buf.write("\7X\2\2\u0123\u0124\7c\2\2\u0124\u0125\7t\2\2\u0125*\3")
        buf.write("\2\2\2\u0126\u0127\7E\2\2\u0127\u0128\7q\2\2\u0128\u0129")
        buf.write("\7p\2\2\u0129\u012a\7u\2\2\u012a\u012b\7v\2\2\u012b\u012c")
        buf.write("\7t\2\2\u012c\u012d\7w\2\2\u012d\u012e\7e\2\2\u012e\u012f")
        buf.write("\7v\2\2\u012f\u0130\7q\2\2\u0130\u0131\7t\2\2\u0131,\3")
        buf.write("\2\2\2\u0132\u0133\7F\2\2\u0133\u0134\7g\2\2\u0134\u0135")
        buf.write("\7u\2\2\u0135\u0136\7v\2\2\u0136\u0137\7t\2\2\u0137\u0138")
        buf.write("\7w\2\2\u0138\u0139\7e\2\2\u0139\u013a\7v\2\2\u013a\u013b")
        buf.write("\7q\2\2\u013b\u013c\7t\2\2\u013c.\3\2\2\2\u013d\u013e")
        buf.write("\7P\2\2\u013e\u013f\7g\2\2\u013f\u0140\7y\2\2\u0140\60")
        buf.write("\3\2\2\2\u0141\u0142\7D\2\2\u0142\u0143\7{\2\2\u0143\62")
        buf.write("\3\2\2\2\u0144\u0145\7o\2\2\u0145\u0146\7c\2\2\u0146\u0147")
        buf.write("\7k\2\2\u0147\u0148\7p\2\2\u0148\64\3\2\2\2\u0149\u014a")
        buf.write("\7u\2\2\u014a\u014b\7g\2\2\u014b\u014c\7n\2\2\u014c\u014d")
        buf.write("\7h\2\2\u014d\66\3\2\2\2\u014e\u014f\7?\2\2\u014f8\3\2")
        buf.write("\2\2\u0150\u0151\7#\2\2\u0151:\3\2\2\2\u0152\u0153\7~")
        buf.write("\2\2\u0153\u0154\7~\2\2\u0154<\3\2\2\2\u0155\u0156\7(")
        buf.write("\2\2\u0156\u0157\7(\2\2\u0157>\3\2\2\2\u0158\u0159\7?")
        buf.write("\2\2\u0159\u015a\7?\2\2\u015a@\3\2\2\2\u015b\u015c\7#")
        buf.write("\2\2\u015c\u015d\7?\2\2\u015dB\3\2\2\2\u015e\u015f\7\'")
        buf.write("\2\2\u015fD\3\2\2\2\u0160\u0161\7-\2\2\u0161F\3\2\2\2")
        buf.write("\u0162\u0163\7/\2\2\u0163H\3\2\2\2\u0164\u0165\7,\2\2")
        buf.write("\u0165J\3\2\2\2\u0166\u0167\7\61\2\2\u0167L\3\2\2\2\u0168")
        buf.write("\u0169\7>\2\2\u0169N\3\2\2\2\u016a\u016b\7>\2\2\u016b")
        buf.write("\u016c\7?\2\2\u016cP\3\2\2\2\u016d\u016e\7@\2\2\u016e")
        buf.write("R\3\2\2\2\u016f\u0170\7@\2\2\u0170\u0171\7?\2\2\u0171")
        buf.write("T\3\2\2\2\u0172\u0173\7-\2\2\u0173\u0174\7\60\2\2\u0174")
        buf.write("V\3\2\2\2\u0175\u0176\7?\2\2\u0176\u0177\7?\2\2\u0177")
        buf.write("\u0178\7\60\2\2\u0178X\3\2\2\2\u0179\u017a\7*\2\2\u017a")
        buf.write("Z\3\2\2\2\u017b\u017c\7+\2\2\u017c\\\3\2\2\2\u017d\u017e")
        buf.write("\7]\2\2\u017e^\3\2\2\2\u017f\u0180\7_\2\2\u0180`\3\2\2")
        buf.write("\2\u0181\u0182\7\60\2\2\u0182b\3\2\2\2\u0183\u0184\7\60")
        buf.write("\2\2\u0184\u0185\7\60\2\2\u0185d\3\2\2\2\u0186\u0187\7")
        buf.write(".\2\2\u0187f\3\2\2\2\u0188\u0189\7<\2\2\u0189h\3\2\2\2")
        buf.write("\u018a\u018b\7<\2\2\u018b\u018c\7<\2\2\u018cj\3\2\2\2")
        buf.write("\u018d\u018e\7=\2\2\u018el\3\2\2\2\u018f\u0190\7}\2\2")
        buf.write("\u0190n\3\2\2\2\u0191\u0192\7\177\2\2\u0192p\3\2\2\2\u0193")
        buf.write("\u0194\7)\2\2\u0194r\3\2\2\2\u0195\u0196\7$\2\2\u0196")
        buf.write("t\3\2\2\2\u0197\u01a7\3\2\2\2\u0198\u0199\7^\2\2\u0199")
        buf.write("\u01a7\7d\2\2\u019a\u019b\7^\2\2\u019b\u01a7\7h\2\2\u019c")
        buf.write("\u019d\7^\2\2\u019d\u01a7\7t\2\2\u019e\u019f\7^\2\2\u019f")
        buf.write("\u01a7\7p\2\2\u01a0\u01a1\7^\2\2\u01a1\u01a7\7v\2\2\u01a2")
        buf.write("\u01a3\7^\2\2\u01a3\u01a7\7)\2\2\u01a4\u01a5\7^\2\2\u01a5")
        buf.write("\u01a7\7^\2\2\u01a6\u0197\3\2\2\2\u01a6\u0198\3\2\2\2")
        buf.write("\u01a6\u019a\3\2\2\2\u01a6\u019c\3\2\2\2\u01a6\u019e\3")
        buf.write("\2\2\2\u01a6\u01a0\3\2\2\2\u01a6\u01a2\3\2\2\2\u01a6\u01a4")
        buf.write("\3\2\2\2\u01a7v\3\2\2\2\u01a8\u01a9\7\62\2\2\u01a9x\3")
        buf.write("\2\2\2\u01aa\u01ab\7\62\2\2\u01ab\u01af\7z\2\2\u01ac\u01ad")
        buf.write("\7\62\2\2\u01ad\u01af\7Z\2\2\u01ae\u01aa\3\2\2\2\u01ae")
        buf.write("\u01ac\3\2\2\2\u01afz\3\2\2\2\u01b0\u01b1\7\62\2\2\u01b1")
        buf.write("\u01b5\7d\2\2\u01b2\u01b3\7\62\2\2\u01b3\u01b5\7D\2\2")
        buf.write("\u01b4\u01b0\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5|\3\2\2")
        buf.write("\2\u01b6\u01b7\t\3\2\2\u01b7~\3\2\2\2\u01b8\u01b9\t\4")
        buf.write("\2\2\u01b9\u0080\3\2\2\2\u01ba\u01bb\t\5\2\2\u01bb\u0082")
        buf.write("\3\2\2\2\u01bc\u01bd\t\6\2\2\u01bd\u0084\3\2\2\2\u01be")
        buf.write("\u01d2\5\u0083B\2\u01bf\u01c3\t\7\2\2\u01c0\u01c2\5\u0083")
        buf.write("B\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01ce\3\2\2\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c6\u01c8\7a\2\2\u01c7\u01c9\5\u0083")
        buf.write("B\2\u01c8\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc")
        buf.write("\u01c6\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3")
        buf.write("\2\2\2\u01d1\u01be\3\2\2\2\u01d1\u01bf\3\2\2\2\u01d2\u0086")
        buf.write("\3\2\2\2\u01d3\u01e7\5w<\2\u01d4\u01e8\7\62\2\2\u01d5")
        buf.write("\u01d9\t\b\2\2\u01d6\u01d8\5\177@\2\u01d7\u01d6\3\2\2")
        buf.write("\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da")
        buf.write("\3\2\2\2\u01da\u01e4\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc")
        buf.write("\u01de\7a\2\2\u01dd\u01df\5\177@\2\u01de\u01dd\3\2\2\2")
        buf.write("\u01df\u01e0\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3")
        buf.write("\2\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01dc\3\2\2\2\u01e3\u01e6")
        buf.write("\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5")
        buf.write("\u01e8\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01d4\3\2\2\2")
        buf.write("\u01e7\u01d5\3\2\2\2\u01e8\u0088\3\2\2\2\u01e9\u01fd\5")
        buf.write("y=\2\u01ea\u01fe\7\62\2\2\u01eb\u01ef\t\t\2\2\u01ec\u01ee")
        buf.write("\5}?\2\u01ed\u01ec\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef\u01ed")
        buf.write("\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01fa\3\2\2\2\u01f1")
        buf.write("\u01ef\3\2\2\2\u01f2\u01f4\7a\2\2\u01f3\u01f5\5}?\2\u01f4")
        buf.write("\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f4\3\2\2\2")
        buf.write("\u01f6\u01f7\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8\u01f2\3")
        buf.write("\2\2\2\u01f9\u01fc\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb")
        buf.write("\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd")
        buf.write("\u01ea\3\2\2\2\u01fd\u01eb\3\2\2\2\u01fe\u008a\3\2\2\2")
        buf.write("\u01ff\u0213\5{>\2\u0200\u0214\7\62\2\2\u0201\u0205\7")
        buf.write("\63\2\2\u0202\u0204\5\u0081A\2\u0203\u0202\3\2\2\2\u0204")
        buf.write("\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2")
        buf.write("\u0206\u0210\3\2\2\2\u0207\u0205\3\2\2\2\u0208\u020a\7")
        buf.write("a\2\2\u0209\u020b\5\u0081A\2\u020a\u0209\3\2\2\2\u020b")
        buf.write("\u020c\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2")
        buf.write("\u020d\u020f\3\2\2\2\u020e\u0208\3\2\2\2\u020f\u0212\3")
        buf.write("\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0214")
        buf.write("\3\2\2\2\u0212\u0210\3\2\2\2\u0213\u0200\3\2\2\2\u0213")
        buf.write("\u0201\3\2\2\2\u0214\u008c\3\2\2\2\u0215\u021a\5\u0085")
        buf.write("C\2\u0216\u021a\5\u0087D\2\u0217\u021a\5\u0089E\2\u0218")
        buf.write("\u021a\5\u008bF\2\u0219\u0215\3\2\2\2\u0219\u0216\3\2")
        buf.write("\2\2\u0219\u0217\3\2\2\2\u0219\u0218\3\2\2\2\u021a\u021b")
        buf.write("\3\2\2\2\u021b\u021c\bG\3\2\u021c\u008e\3\2\2\2\u021d")
        buf.write("\u021e\5\u0085C\2\u021e\u0090\3\2\2\2\u021f\u0223\5a\61")
        buf.write("\2\u0220\u0222\5\u0083B\2\u0221\u0220\3\2\2\2\u0222\u0225")
        buf.write("\3\2\2\2\u0223\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224")
        buf.write("\u0092\3\2\2\2\u0225\u0223\3\2\2\2\u0226\u0228\t\n\2\2")
        buf.write("\u0227\u0229\t\13\2\2\u0228\u0227\3\2\2\2\u0228\u0229")
        buf.write("\3\2\2\2\u0229\u022b\3\2\2\2\u022a\u022c\5\u0083B\2\u022b")
        buf.write("\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022b\3\2\2\2")
        buf.write("\u022d\u022e\3\2\2\2\u022e\u0094\3\2\2\2\u022f\u0230\5")
        buf.write("\u008fH\2\u0230\u0232\5\u0091I\2\u0231\u0233\5\u0093J")
        buf.write("\2\u0232\u0231\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u023b")
        buf.write("\3\2\2\2\u0234\u0235\5\u008fH\2\u0235\u0236\5\u0093J\2")
        buf.write("\u0236\u023b\3\2\2\2\u0237\u0238\5\u0091I\2\u0238\u0239")
        buf.write("\5\u0093J\2\u0239\u023b\3\2\2\2\u023a\u022f\3\2\2\2\u023a")
        buf.write("\u0234\3\2\2\2\u023a\u0237\3\2\2\2\u023b\u023c\3\2\2\2")
        buf.write("\u023c\u023d\bK\4\2\u023d\u0096\3\2\2\2\u023e\u023f\7")
        buf.write("V\2\2\u023f\u0240\7t\2\2\u0240\u0241\7w\2\2\u0241\u0248")
        buf.write("\7g\2\2\u0242\u0243\7H\2\2\u0243\u0244\7c\2\2\u0244\u0245")
        buf.write("\7n\2\2\u0245\u0246\7u\2\2\u0246\u0248\7g\2\2\u0247\u023e")
        buf.write("\3\2\2\2\u0247\u0242\3\2\2\2\u0248\u0098\3\2\2\2\u0249")
        buf.write("\u024e\5u;\2\u024a\u024b\7)\2\2\u024b\u024e\7$\2\2\u024c")
        buf.write("\u024e\n\f\2\2\u024d\u0249\3\2\2\2\u024d\u024a\3\2\2\2")
        buf.write("\u024d\u024c\3\2\2\2\u024e\u009a\3\2\2\2\u024f\u0253\5")
        buf.write("s:\2\u0250\u0252\5\u0099M\2\u0251\u0250\3\2\2\2\u0252")
        buf.write("\u0255\3\2\2\2\u0253\u0251\3\2\2\2\u0253\u0254\3\2\2\2")
        buf.write("\u0254\u0256\3\2\2\2\u0255\u0253\3\2\2\2\u0256\u0257\5")
        buf.write("s:\2\u0257\u009c\3\2\2\2\u0258\u025a\t\r\2\2\u0259\u0258")
        buf.write("\3\2\2\2\u025a\u025e\3\2\2\2\u025b\u025d\t\16\2\2\u025c")
        buf.write("\u025b\3\2\2\2\u025d\u0260\3\2\2\2\u025e\u025c\3\2\2\2")
        buf.write("\u025e\u025f\3\2\2\2\u025f\u009e\3\2\2\2\u0260\u025e\3")
        buf.write("\2\2\2\u0261\u0263\7&\2\2\u0262\u0264\t\16\2\2\u0263\u0262")
        buf.write("\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0263\3\2\2\2\u0265")
        buf.write("\u0266\3\2\2\2\u0266\u00a0\3\2\2\2\u0267\u026b\5s:\2\u0268")
        buf.write("\u026a\5\u0099M\2\u0269\u0268\3\2\2\2\u026a\u026d\3\2")
        buf.write("\2\2\u026b\u0269\3\2\2\2\u026b\u026c\3\2\2\2\u026c\u026f")
        buf.write("\3\2\2\2\u026d\u026b\3\2\2\2\u026e\u0270\t\17\2\2\u026f")
        buf.write("\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u0272\bQ\5\2")
        buf.write("\u0272\u00a2\3\2\2\2\u0273\u0277\5s:\2\u0274\u0276\5\u0099")
        buf.write("M\2\u0275\u0274\3\2\2\2\u0276\u0279\3\2\2\2\u0277\u0275")
        buf.write("\3\2\2\2\u0277\u0278\3\2\2\2\u0278\u027a\3\2\2\2\u0279")
        buf.write("\u0277\3\2\2\2\u027a\u027b\7^\2\2\u027b\u027c\n\20\2\2")
        buf.write("\u027c\u027d\bR\6\2\u027d\u00a4\3\2\2\2\u027e\u027f\13")
        buf.write("\2\2\2\u027f\u0280\bS\7\2\u0280\u00a6\3\2\2\2)\2\u00b2")
        buf.write("\u00bc\u01a6\u01ae\u01b4\u01c3\u01ca\u01ce\u01d1\u01d9")
        buf.write("\u01e0\u01e4\u01e7\u01ef\u01f6\u01fa\u01fd\u0205\u020c")
        buf.write("\u0210\u0213\u0219\u0223\u0228\u022d\u0232\u023a\u0247")
        buf.write("\u024d\u0253\u0259\u025c\u025e\u0263\u0265\u026b\u026f")
        buf.write("\u0277\b\b\2\2\3G\2\3K\3\3Q\4\3R\5\3S\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    WHITE_SPACE = 2
    COMMENT = 3
    K_BREAK = 4
    K_CONTINUE = 5
    K_IF = 6
    K_ELSE_IF = 7
    K_ELSE = 8
    K_FOR_EACH = 9
    K_ARRAY = 10
    K_IN = 11
    K_INT = 12
    K_FLOAT = 13
    K_BOOLEAN = 14
    K_STRING = 15
    K_RETURN = 16
    K_NULL = 17
    K_CLASS = 18
    K_VAL = 19
    K_VAR = 20
    K_CONSTRUCTOR = 21
    K_DESTRUCTOR = 22
    K_NEW = 23
    K_BY = 24
    K_MAIN = 25
    K_SELF = 26
    OP_ASSIGN = 27
    OP_LOGICAL_NOT = 28
    OP_LOGICAL_OR = 29
    OP_LOGICAL_AND = 30
    OP_IS_EQUAL_TO = 31
    OP_NOT_EQUAL_TO = 32
    OP_MODULO = 33
    OP_ADDTION = 34
    OP_SUBTRACTION = 35
    OP_MULTIPLICATION = 36
    OP_DIVISION = 37
    OP_LESS_THAN = 38
    OP_LESS_THAN_EQUAL = 39
    OP_GREATER_THAN = 40
    OP_GREATER_THAN_EQUAL = 41
    OP_STRING_CONCATENATION = 42
    OP_TWO_SAME_STRING = 43
    LEFT_PAREN = 44
    RIGHT_PAREN = 45
    LEFT_SQUARE_BRACKET = 46
    RIGHT_SQUARE_BRACKET = 47
    DOT = 48
    DOUBLE_DOT = 49
    COMMA = 50
    COLON = 51
    DOUBLE_COLON = 52
    SEMI_COLON = 53
    LEFT_CURLY_BRACKET = 54
    RIGHT_CURLY_BRACKET = 55
    INTEGER_LITERAL = 56
    FLOAT_LITERAL = 57
    BOOLEAN_LITERAL = 58
    STRING_LITERAL = 59
    IDENTIFIER = 60
    DOLAR_IDENTIFIER = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_TOKEN = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
            "'Foreach'", "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
            "'String'", "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
            "'Constructor'", "'Destructor'", "'New'", "'By'", "'main'", 
            "'self'", "'='", "'!'", "'||'", "'&&'", "'=='", "'!='", "'%'", 
            "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", "'+.'", 
            "'==.'", "'('", "')'", "'['", "']'", "'.'", "'..'", "','", "':'", 
            "'::'", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "WHITE_SPACE", "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", 
            "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", 
            "K_BOOLEAN", "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", "K_VAL", 
            "K_VAR", "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", "K_BY", "K_MAIN", 
            "K_SELF", "OP_ASSIGN", "OP_LOGICAL_NOT", "OP_LOGICAL_OR", "OP_LOGICAL_AND", 
            "OP_IS_EQUAL_TO", "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", 
            "OP_SUBTRACTION", "OP_MULTIPLICATION", "OP_DIVISION", "OP_LESS_THAN", 
            "OP_LESS_THAN_EQUAL", "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", 
            "OP_STRING_CONCATENATION", "OP_TWO_SAME_STRING", "LEFT_PAREN", 
            "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
            "DOT", "DOUBLE_DOT", "COMMA", "COLON", "DOUBLE_COLON", "SEMI_COLON", 
            "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "INTEGER_LITERAL", 
            "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", "IDENTIFIER", 
            "DOLAR_IDENTIFIER", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "T__0", "WHITE_SPACE", "COMMENT", "K_BREAK", "K_CONTINUE", 
                  "K_IF", "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", "K_ARRAY", 
                  "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", "K_RETURN", 
                  "K_NULL", "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", 
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
                  "DECIMAL", "OCTAL", "HEXA", "BINARY", "INTEGER_LITERAL", 
                  "INTEGER_PART", "DECIMAL_PART", "EXPONENT", "FLOAT_LITERAL", 
                  "BOOLEAN_LITERAL", "CHAR", "STRING_LITERAL", "IDENTIFIER", 
                  "DOLAR_IDENTIFIER", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_TOKEN" ]

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
            actions[69] = self.INTEGER_LITERAL_action 
            actions[73] = self.FLOAT_LITERAL_action 
            actions[79] = self.UNCLOSE_STRING_action 
            actions[80] = self.ILLEGAL_ESCAPE_action 
            actions[81] = self.ERROR_TOKEN_action 
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
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                                    y = str(self.text)
                                    	end_with = ['\b', '\t', '\n', '\f', '\r', "'", '\\']
                                    if y[-1] in end with:
                                    	raise UncloseString(self.text[1:-1])
            						else:
                                        raise UncloseString(self.text[1:])
                                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


