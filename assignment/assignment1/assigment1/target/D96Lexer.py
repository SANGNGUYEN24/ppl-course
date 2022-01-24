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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u027d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3;\3;\3;\3;\3;\3;\5;\u01a8\n;\3<\3<\3=\3=\3=\3=\5=\u01b0")
        buf.write("\n=\3>\3>\3>\3>\5>\u01b6\n>\3?\3?\3@\3@\3A\3A\3B\3B\3")
        buf.write("C\3C\3C\7C\u01c3\nC\fC\16C\u01c6\13C\3C\3C\6C\u01ca\n")
        buf.write("C\rC\16C\u01cb\7C\u01ce\nC\fC\16C\u01d1\13C\5C\u01d3\n")
        buf.write("C\3D\3D\3D\3D\7D\u01d9\nD\fD\16D\u01dc\13D\3D\3D\6D\u01e0")
        buf.write("\nD\rD\16D\u01e1\7D\u01e4\nD\fD\16D\u01e7\13D\5D\u01e9")
        buf.write("\nD\3E\3E\3E\3E\7E\u01ef\nE\fE\16E\u01f2\13E\3E\3E\6E")
        buf.write("\u01f6\nE\rE\16E\u01f7\7E\u01fa\nE\fE\16E\u01fd\13E\5")
        buf.write("E\u01ff\nE\3F\3F\3F\3F\7F\u0205\nF\fF\16F\u0208\13F\3")
        buf.write("F\3F\6F\u020c\nF\rF\16F\u020d\7F\u0210\nF\fF\16F\u0213")
        buf.write("\13F\5F\u0215\nF\3G\3G\3G\3G\5G\u021b\nG\3G\3G\3H\3H\3")
        buf.write("I\3I\7I\u0223\nI\fI\16I\u0226\13I\3J\3J\5J\u022a\nJ\3")
        buf.write("J\6J\u022d\nJ\rJ\16J\u022e\3K\3K\3K\5K\u0234\nK\3K\3K")
        buf.write("\3K\3K\3K\3K\5K\u023c\nK\3K\3K\3L\3L\3L\3L\3L\3L\3L\3")
        buf.write("L\3L\5L\u0249\nL\3M\3M\5M\u024d\nM\3N\3N\7N\u0251\nN\f")
        buf.write("N\16N\u0254\13N\3N\3N\3O\5O\u0259\nO\3O\7O\u025c\nO\f")
        buf.write("O\16O\u025f\13O\3P\3P\6P\u0263\nP\rP\16P\u0264\3Q\3Q\7")
        buf.write("Q\u0269\nQ\fQ\16Q\u026c\13Q\3Q\3Q\3R\3R\3R\3R\7R\u0274")
        buf.write("\nR\fR\16R\u0277\13R\3R\3R\3S\3S\3S\3\u00bc\2T\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q\2s\2u:w\2y\2")
        buf.write("{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b")
        buf.write("\2\u008d;\u008f\2\u0091\2\u0093\2\u0095<\u0097=\u0099")
        buf.write("\2\u009b>\u009d?\u009f@\u00a1A\u00a3B\u00a5C\3\2\21\5")
        buf.write("\2\13\f\17\17\"\"\4\2\62;CH\3\2\629\3\2\62\63\3\2\62;")
        buf.write("\3\2\63;\3\2\639\4\2\63;CH\4\2GGgg\4\2--//\5\2$$))^^\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\n\2$$))^^ddhhppttvv\3\2^^\2\u0297")
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
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2u")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\3\u00a7\3\2\2")
        buf.write("\2\5\u00b0\3\2\2\2\7\u00b6\3\2\2\2\t\u00c4\3\2\2\2\13")
        buf.write("\u00ca\3\2\2\2\r\u00d3\3\2\2\2\17\u00d6\3\2\2\2\21\u00dd")
        buf.write("\3\2\2\2\23\u00e2\3\2\2\2\25\u00ea\3\2\2\2\27\u00f0\3")
        buf.write("\2\2\2\31\u00f3\3\2\2\2\33\u00f7\3\2\2\2\35\u00fd\3\2")
        buf.write("\2\2\37\u0105\3\2\2\2!\u010c\3\2\2\2#\u0113\3\2\2\2%\u0118")
        buf.write("\3\2\2\2\'\u011e\3\2\2\2)\u0122\3\2\2\2+\u0126\3\2\2\2")
        buf.write("-\u0132\3\2\2\2/\u013d\3\2\2\2\61\u0141\3\2\2\2\63\u0144")
        buf.write("\3\2\2\2\65\u0149\3\2\2\2\67\u014e\3\2\2\29\u0150\3\2")
        buf.write("\2\2;\u0152\3\2\2\2=\u0155\3\2\2\2?\u0158\3\2\2\2A\u015b")
        buf.write("\3\2\2\2C\u015e\3\2\2\2E\u0160\3\2\2\2G\u0162\3\2\2\2")
        buf.write("I\u0164\3\2\2\2K\u0166\3\2\2\2M\u0168\3\2\2\2O\u016a\3")
        buf.write("\2\2\2Q\u016d\3\2\2\2S\u016f\3\2\2\2U\u0172\3\2\2\2W\u0175")
        buf.write("\3\2\2\2Y\u0179\3\2\2\2[\u017b\3\2\2\2]\u017d\3\2\2\2")
        buf.write("_\u017f\3\2\2\2a\u0181\3\2\2\2c\u0183\3\2\2\2e\u0186\3")
        buf.write("\2\2\2g\u0188\3\2\2\2i\u018a\3\2\2\2k\u018d\3\2\2\2m\u018f")
        buf.write("\3\2\2\2o\u0191\3\2\2\2q\u0193\3\2\2\2s\u0195\3\2\2\2")
        buf.write("u\u01a7\3\2\2\2w\u01a9\3\2\2\2y\u01af\3\2\2\2{\u01b5\3")
        buf.write("\2\2\2}\u01b7\3\2\2\2\177\u01b9\3\2\2\2\u0081\u01bb\3")
        buf.write("\2\2\2\u0083\u01bd\3\2\2\2\u0085\u01d2\3\2\2\2\u0087\u01d4")
        buf.write("\3\2\2\2\u0089\u01ea\3\2\2\2\u008b\u0200\3\2\2\2\u008d")
        buf.write("\u021a\3\2\2\2\u008f\u021e\3\2\2\2\u0091\u0220\3\2\2\2")
        buf.write("\u0093\u0227\3\2\2\2\u0095\u023b\3\2\2\2\u0097\u0248\3")
        buf.write("\2\2\2\u0099\u024c\3\2\2\2\u009b\u024e\3\2\2\2\u009d\u0258")
        buf.write("\3\2\2\2\u009f\u0260\3\2\2\2\u00a1\u0266\3\2\2\2\u00a3")
        buf.write("\u026f\3\2\2\2\u00a5\u027a\3\2\2\2\u00a7\u00a8\7R\2\2")
        buf.write("\u00a8\u00a9\7t\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7i")
        buf.write("\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7o\2\2\u00ae\4\3\2\2\2\u00af\u00b1\t\2\2\2\u00b0\u00af")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\b\3\2\2")
        buf.write("\u00b5\6\3\2\2\2\u00b6\u00b7\7%\2\2\u00b7\u00b8\7%\2\2")
        buf.write("\u00b8\u00bc\3\2\2\2\u00b9\u00bb\13\2\2\2\u00ba\u00b9")
        buf.write("\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bd\u00bf\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00bf\u00c0\7%\2\2\u00c0\u00c1\7%\2\2\u00c1\u00c2\3\2")
        buf.write("\2\2\u00c2\u00c3\b\4\2\2\u00c3\b\3\2\2\2\u00c4\u00c5\7")
        buf.write("D\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8")
        buf.write("\7c\2\2\u00c8\u00c9\7m\2\2\u00c9\n\3\2\2\2\u00ca\u00cb")
        buf.write("\7E\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce")
        buf.write("\7v\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1")
        buf.write("\7w\2\2\u00d1\u00d2\7g\2\2\u00d2\f\3\2\2\2\u00d3\u00d4")
        buf.write("\7K\2\2\u00d4\u00d5\7h\2\2\u00d5\16\3\2\2\2\u00d6\u00d7")
        buf.write("\7G\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da\u00db\7k\2\2\u00db\u00dc\7h\2\2\u00dc\20")
        buf.write("\3\2\2\2\u00dd\u00de\7G\2\2\u00de\u00df\7n\2\2\u00df\u00e0")
        buf.write("\7u\2\2\u00e0\u00e1\7g\2\2\u00e1\22\3\2\2\2\u00e2\u00e3")
        buf.write("\7H\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8\7e\2\2\u00e8\u00e9")
        buf.write("\7j\2\2\u00e9\24\3\2\2\2\u00ea\u00eb\7C\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef")
        buf.write("\7{\2\2\u00ef\26\3\2\2\2\u00f0\u00f1\7K\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2\30\3\2\2\2\u00f3\u00f4\7K\2\2\u00f4\u00f5")
        buf.write("\7p\2\2\u00f5\u00f6\7v\2\2\u00f6\32\3\2\2\2\u00f7\u00f8")
        buf.write("\7H\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb")
        buf.write("\7c\2\2\u00fb\u00fc\7v\2\2\u00fc\34\3\2\2\2\u00fd\u00fe")
        buf.write("\7D\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100\7q\2\2\u0100\u0101")
        buf.write("\7n\2\2\u0101\u0102\7g\2\2\u0102\u0103\7c\2\2\u0103\u0104")
        buf.write("\7p\2\2\u0104\36\3\2\2\2\u0105\u0106\7U\2\2\u0106\u0107")
        buf.write("\7v\2\2\u0107\u0108\7t\2\2\u0108\u0109\7k\2\2\u0109\u010a")
        buf.write("\7p\2\2\u010a\u010b\7i\2\2\u010b \3\2\2\2\u010c\u010d")
        buf.write("\7T\2\2\u010d\u010e\7g\2\2\u010e\u010f\7v\2\2\u010f\u0110")
        buf.write("\7w\2\2\u0110\u0111\7t\2\2\u0111\u0112\7p\2\2\u0112\"")
        buf.write("\3\2\2\2\u0113\u0114\7P\2\2\u0114\u0115\7w\2\2\u0115\u0116")
        buf.write("\7n\2\2\u0116\u0117\7n\2\2\u0117$\3\2\2\2\u0118\u0119")
        buf.write("\7E\2\2\u0119\u011a\7n\2\2\u011a\u011b\7c\2\2\u011b\u011c")
        buf.write("\7u\2\2\u011c\u011d\7u\2\2\u011d&\3\2\2\2\u011e\u011f")
        buf.write("\7X\2\2\u011f\u0120\7c\2\2\u0120\u0121\7n\2\2\u0121(\3")
        buf.write("\2\2\2\u0122\u0123\7X\2\2\u0123\u0124\7c\2\2\u0124\u0125")
        buf.write("\7t\2\2\u0125*\3\2\2\2\u0126\u0127\7E\2\2\u0127\u0128")
        buf.write("\7q\2\2\u0128\u0129\7p\2\2\u0129\u012a\7u\2\2\u012a\u012b")
        buf.write("\7v\2\2\u012b\u012c\7t\2\2\u012c\u012d\7w\2\2\u012d\u012e")
        buf.write("\7e\2\2\u012e\u012f\7v\2\2\u012f\u0130\7q\2\2\u0130\u0131")
        buf.write("\7t\2\2\u0131,\3\2\2\2\u0132\u0133\7F\2\2\u0133\u0134")
        buf.write("\7g\2\2\u0134\u0135\7u\2\2\u0135\u0136\7v\2\2\u0136\u0137")
        buf.write("\7t\2\2\u0137\u0138\7w\2\2\u0138\u0139\7e\2\2\u0139\u013a")
        buf.write("\7v\2\2\u013a\u013b\7q\2\2\u013b\u013c\7t\2\2\u013c.\3")
        buf.write("\2\2\2\u013d\u013e\7P\2\2\u013e\u013f\7g\2\2\u013f\u0140")
        buf.write("\7y\2\2\u0140\60\3\2\2\2\u0141\u0142\7D\2\2\u0142\u0143")
        buf.write("\7{\2\2\u0143\62\3\2\2\2\u0144\u0145\7o\2\2\u0145\u0146")
        buf.write("\7c\2\2\u0146\u0147\7k\2\2\u0147\u0148\7p\2\2\u0148\64")
        buf.write("\3\2\2\2\u0149\u014a\7u\2\2\u014a\u014b\7g\2\2\u014b\u014c")
        buf.write("\7n\2\2\u014c\u014d\7h\2\2\u014d\66\3\2\2\2\u014e\u014f")
        buf.write("\7?\2\2\u014f8\3\2\2\2\u0150\u0151\7#\2\2\u0151:\3\2\2")
        buf.write("\2\u0152\u0153\7~\2\2\u0153\u0154\7~\2\2\u0154<\3\2\2")
        buf.write("\2\u0155\u0156\7(\2\2\u0156\u0157\7(\2\2\u0157>\3\2\2")
        buf.write("\2\u0158\u0159\7?\2\2\u0159\u015a\7?\2\2\u015a@\3\2\2")
        buf.write("\2\u015b\u015c\7#\2\2\u015c\u015d\7?\2\2\u015dB\3\2\2")
        buf.write("\2\u015e\u015f\7\'\2\2\u015fD\3\2\2\2\u0160\u0161\7-\2")
        buf.write("\2\u0161F\3\2\2\2\u0162\u0163\7/\2\2\u0163H\3\2\2\2\u0164")
        buf.write("\u0165\7,\2\2\u0165J\3\2\2\2\u0166\u0167\7\61\2\2\u0167")
        buf.write("L\3\2\2\2\u0168\u0169\7>\2\2\u0169N\3\2\2\2\u016a\u016b")
        buf.write("\7>\2\2\u016b\u016c\7?\2\2\u016cP\3\2\2\2\u016d\u016e")
        buf.write("\7@\2\2\u016eR\3\2\2\2\u016f\u0170\7@\2\2\u0170\u0171")
        buf.write("\7?\2\2\u0171T\3\2\2\2\u0172\u0173\7-\2\2\u0173\u0174")
        buf.write("\7\60\2\2\u0174V\3\2\2\2\u0175\u0176\7?\2\2\u0176\u0177")
        buf.write("\7?\2\2\u0177\u0178\7\60\2\2\u0178X\3\2\2\2\u0179\u017a")
        buf.write("\7*\2\2\u017aZ\3\2\2\2\u017b\u017c\7+\2\2\u017c\\\3\2")
        buf.write("\2\2\u017d\u017e\7]\2\2\u017e^\3\2\2\2\u017f\u0180\7_")
        buf.write("\2\2\u0180`\3\2\2\2\u0181\u0182\7\60\2\2\u0182b\3\2\2")
        buf.write("\2\u0183\u0184\7\60\2\2\u0184\u0185\7\60\2\2\u0185d\3")
        buf.write("\2\2\2\u0186\u0187\7.\2\2\u0187f\3\2\2\2\u0188\u0189\7")
        buf.write("<\2\2\u0189h\3\2\2\2\u018a\u018b\7<\2\2\u018b\u018c\7")
        buf.write("<\2\2\u018cj\3\2\2\2\u018d\u018e\7=\2\2\u018el\3\2\2\2")
        buf.write("\u018f\u0190\7}\2\2\u0190n\3\2\2\2\u0191\u0192\7\177\2")
        buf.write("\2\u0192p\3\2\2\2\u0193\u0194\7)\2\2\u0194r\3\2\2\2\u0195")
        buf.write("\u0196\7$\2\2\u0196t\3\2\2\2\u0197\u0198\7)\2\2\u0198")
        buf.write("\u01a8\7$\2\2\u0199\u019a\7^\2\2\u019a\u01a8\7d\2\2\u019b")
        buf.write("\u019c\7^\2\2\u019c\u01a8\7h\2\2\u019d\u019e\7^\2\2\u019e")
        buf.write("\u01a8\7t\2\2\u019f\u01a0\7^\2\2\u01a0\u01a8\7p\2\2\u01a1")
        buf.write("\u01a2\7^\2\2\u01a2\u01a8\7v\2\2\u01a3\u01a4\7^\2\2\u01a4")
        buf.write("\u01a8\7)\2\2\u01a5\u01a6\7^\2\2\u01a6\u01a8\7^\2\2\u01a7")
        buf.write("\u0197\3\2\2\2\u01a7\u0199\3\2\2\2\u01a7\u019b\3\2\2\2")
        buf.write("\u01a7\u019d\3\2\2\2\u01a7\u019f\3\2\2\2\u01a7\u01a1\3")
        buf.write("\2\2\2\u01a7\u01a3\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8v")
        buf.write("\3\2\2\2\u01a9\u01aa\7\62\2\2\u01aax\3\2\2\2\u01ab\u01ac")
        buf.write("\7\62\2\2\u01ac\u01b0\7z\2\2\u01ad\u01ae\7\62\2\2\u01ae")
        buf.write("\u01b0\7Z\2\2\u01af\u01ab\3\2\2\2\u01af\u01ad\3\2\2\2")
        buf.write("\u01b0z\3\2\2\2\u01b1\u01b2\7\62\2\2\u01b2\u01b6\7d\2")
        buf.write("\2\u01b3\u01b4\7\62\2\2\u01b4\u01b6\7D\2\2\u01b5\u01b1")
        buf.write("\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6|\3\2\2\2\u01b7\u01b8")
        buf.write("\t\3\2\2\u01b8~\3\2\2\2\u01b9\u01ba\t\4\2\2\u01ba\u0080")
        buf.write("\3\2\2\2\u01bb\u01bc\t\5\2\2\u01bc\u0082\3\2\2\2\u01bd")
        buf.write("\u01be\t\6\2\2\u01be\u0084\3\2\2\2\u01bf\u01d3\5\u0083")
        buf.write("B\2\u01c0\u01c4\t\7\2\2\u01c1\u01c3\5\u0083B\2\u01c2\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c5\3\2\2\2\u01c5\u01cf\3\2\2\2\u01c6\u01c4\3\2\2\2")
        buf.write("\u01c7\u01c9\7a\2\2\u01c8\u01ca\5\u0083B\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb")
        buf.write("\u01cc\3\2\2\2\u01cc\u01ce\3\2\2\2\u01cd\u01c7\3\2\2\2")
        buf.write("\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3")
        buf.write("\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01bf")
        buf.write("\3\2\2\2\u01d2\u01c0\3\2\2\2\u01d3\u0086\3\2\2\2\u01d4")
        buf.write("\u01e8\5w<\2\u01d5\u01e9\7\62\2\2\u01d6\u01da\t\b\2\2")
        buf.write("\u01d7\u01d9\5\177@\2\u01d8\u01d7\3\2\2\2\u01d9\u01dc")
        buf.write("\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db")
        buf.write("\u01e5\3\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01df\7a\2\2")
        buf.write("\u01de\u01e0\5\177@\2\u01df\u01de\3\2\2\2\u01e0\u01e1")
        buf.write("\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2")
        buf.write("\u01e4\3\2\2\2\u01e3\u01dd\3\2\2\2\u01e4\u01e7\3\2\2\2")
        buf.write("\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e9\3")
        buf.write("\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01d5\3\2\2\2\u01e8\u01d6")
        buf.write("\3\2\2\2\u01e9\u0088\3\2\2\2\u01ea\u01fe\5y=\2\u01eb\u01ff")
        buf.write("\7\62\2\2\u01ec\u01f0\t\t\2\2\u01ed\u01ef\5}?\2\u01ee")
        buf.write("\u01ed\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0\u01ee\3\2\2\2")
        buf.write("\u01f0\u01f1\3\2\2\2\u01f1\u01fb\3\2\2\2\u01f2\u01f0\3")
        buf.write("\2\2\2\u01f3\u01f5\7a\2\2\u01f4\u01f6\5}?\2\u01f5\u01f4")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7")
        buf.write("\u01f8\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01f3\3\2\2\2")
        buf.write("\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3")
        buf.write("\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe\u01eb")
        buf.write("\3\2\2\2\u01fe\u01ec\3\2\2\2\u01ff\u008a\3\2\2\2\u0200")
        buf.write("\u0214\5{>\2\u0201\u0215\7\62\2\2\u0202\u0206\7\63\2\2")
        buf.write("\u0203\u0205\5\u0081A\2\u0204\u0203\3\2\2\2\u0205\u0208")
        buf.write("\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207")
        buf.write("\u0211\3\2\2\2\u0208\u0206\3\2\2\2\u0209\u020b\7a\2\2")
        buf.write("\u020a\u020c\5\u0081A\2\u020b\u020a\3\2\2\2\u020c\u020d")
        buf.write("\3\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e")
        buf.write("\u0210\3\2\2\2\u020f\u0209\3\2\2\2\u0210\u0213\3\2\2\2")
        buf.write("\u0211\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0215\3")
        buf.write("\2\2\2\u0213\u0211\3\2\2\2\u0214\u0201\3\2\2\2\u0214\u0202")
        buf.write("\3\2\2\2\u0215\u008c\3\2\2\2\u0216\u021b\5\u0085C\2\u0217")
        buf.write("\u021b\5\u0087D\2\u0218\u021b\5\u0089E\2\u0219\u021b\5")
        buf.write("\u008bF\2\u021a\u0216\3\2\2\2\u021a\u0217\3\2\2\2\u021a")
        buf.write("\u0218\3\2\2\2\u021a\u0219\3\2\2\2\u021b\u021c\3\2\2\2")
        buf.write("\u021c\u021d\bG\3\2\u021d\u008e\3\2\2\2\u021e\u021f\5")
        buf.write("\u0085C\2\u021f\u0090\3\2\2\2\u0220\u0224\5a\61\2\u0221")
        buf.write("\u0223\5\u0083B\2\u0222\u0221\3\2\2\2\u0223\u0226\3\2")
        buf.write("\2\2\u0224\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0092")
        buf.write("\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u0229\t\n\2\2\u0228")
        buf.write("\u022a\t\13\2\2\u0229\u0228\3\2\2\2\u0229\u022a\3\2\2")
        buf.write("\2\u022a\u022c\3\2\2\2\u022b\u022d\5\u0083B\2\u022c\u022b")
        buf.write("\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u022c\3\2\2\2\u022e")
        buf.write("\u022f\3\2\2\2\u022f\u0094\3\2\2\2\u0230\u0231\5\u008f")
        buf.write("H\2\u0231\u0233\5\u0091I\2\u0232\u0234\5\u0093J\2\u0233")
        buf.write("\u0232\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u023c\3\2\2\2")
        buf.write("\u0235\u0236\5\u008fH\2\u0236\u0237\5\u0093J\2\u0237\u023c")
        buf.write("\3\2\2\2\u0238\u0239\5\u0091I\2\u0239\u023a\5\u0093J\2")
        buf.write("\u023a\u023c\3\2\2\2\u023b\u0230\3\2\2\2\u023b\u0235\3")
        buf.write("\2\2\2\u023b\u0238\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e")
        buf.write("\bK\4\2\u023e\u0096\3\2\2\2\u023f\u0240\7V\2\2\u0240\u0241")
        buf.write("\7t\2\2\u0241\u0242\7w\2\2\u0242\u0249\7g\2\2\u0243\u0244")
        buf.write("\7H\2\2\u0244\u0245\7c\2\2\u0245\u0246\7n\2\2\u0246\u0247")
        buf.write("\7u\2\2\u0247\u0249\7g\2\2\u0248\u023f\3\2\2\2\u0248\u0243")
        buf.write("\3\2\2\2\u0249\u0098\3\2\2\2\u024a\u024d\5u;\2\u024b\u024d")
        buf.write("\n\f\2\2\u024c\u024a\3\2\2\2\u024c\u024b\3\2\2\2\u024d")
        buf.write("\u009a\3\2\2\2\u024e\u0252\5s:\2\u024f\u0251\5\u0099M")
        buf.write("\2\u0250\u024f\3\2\2\2\u0251\u0254\3\2\2\2\u0252\u0250")
        buf.write("\3\2\2\2\u0252\u0253\3\2\2\2\u0253\u0255\3\2\2\2\u0254")
        buf.write("\u0252\3\2\2\2\u0255\u0256\5s:\2\u0256\u009c\3\2\2\2\u0257")
        buf.write("\u0259\t\r\2\2\u0258\u0257\3\2\2\2\u0259\u025d\3\2\2\2")
        buf.write("\u025a\u025c\t\16\2\2\u025b\u025a\3\2\2\2\u025c\u025f")
        buf.write("\3\2\2\2\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e")
        buf.write("\u009e\3\2\2\2\u025f\u025d\3\2\2\2\u0260\u0262\7&\2\2")
        buf.write("\u0261\u0263\t\16\2\2\u0262\u0261\3\2\2\2\u0263\u0264")
        buf.write("\3\2\2\2\u0264\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265")
        buf.write("\u00a0\3\2\2\2\u0266\u026a\5s:\2\u0267\u0269\5\u0099M")
        buf.write("\2\u0268\u0267\3\2\2\2\u0269\u026c\3\2\2\2\u026a\u0268")
        buf.write("\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u026d\3\2\2\2\u026c")
        buf.write("\u026a\3\2\2\2\u026d\u026e\bQ\5\2\u026e\u00a2\3\2\2\2")
        buf.write("\u026f\u0275\5s:\2\u0270\u0271\7^\2\2\u0271\u0274\n\17")
        buf.write("\2\2\u0272\u0274\n\20\2\2\u0273\u0270\3\2\2\2\u0273\u0272")
        buf.write("\3\2\2\2\u0274\u0277\3\2\2\2\u0275\u0273\3\2\2\2\u0275")
        buf.write("\u0276\3\2\2\2\u0276\u0278\3\2\2\2\u0277\u0275\3\2\2\2")
        buf.write("\u0278\u0279\bR\6\2\u0279\u00a4\3\2\2\2\u027a\u027b\13")
        buf.write("\2\2\2\u027b\u027c\bS\7\2\u027c\u00a6\3\2\2\2)\2\u00b2")
        buf.write("\u00bc\u01a7\u01af\u01b5\u01c4\u01cb\u01cf\u01d2\u01da")
        buf.write("\u01e1\u01e5\u01e8\u01f0\u01f7\u01fb\u01fe\u0206\u020d")
        buf.write("\u0211\u0214\u021a\u0224\u0229\u022e\u0233\u023b\u0248")
        buf.write("\u024c\u0252\u0258\u025b\u025d\u0262\u0264\u026a\u0273")
        buf.write("\u0275\b\b\2\2\3G\2\3K\3\3Q\4\3R\5\3S\6")
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
    ESCAPE = 56
    INTEGER_LITERAL = 57
    FLOAT_LITERAL = 58
    BOOLEAN_LITERAL = 59
    STRING_LITERAL = 60
    IDENTIFIER = 61
    DOLAR_IDENTIFIER = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    ERROR_TOKEN = 65

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
            "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "ESCAPE", "INTEGER_LITERAL", 
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
        self.checkVersion("4.9.3")
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
            raise  UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


