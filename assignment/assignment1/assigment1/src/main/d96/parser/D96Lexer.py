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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\6\4\u00b6")
        buf.write("\n\4\r\4\16\4\u00b7\3\4\3\4\3\5\3\5\3\5\3\5\7\5\u00c0")
        buf.write("\n\5\f\5\16\5\u00c3\13\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3;\3<\3<\3=\3=\3=\3=\5=")
        buf.write("\u01a1\n=\3>\3>\3>\3>\5>\u01a7\n>\3?\3?\3@\3@\3A\3A\3")
        buf.write("B\3B\3C\3C\3C\7C\u01b4\nC\fC\16C\u01b7\13C\3C\3C\6C\u01bb")
        buf.write("\nC\rC\16C\u01bc\7C\u01bf\nC\fC\16C\u01c2\13C\5C\u01c4")
        buf.write("\nC\3D\3D\3D\3D\7D\u01ca\nD\fD\16D\u01cd\13D\3D\3D\6D")
        buf.write("\u01d1\nD\rD\16D\u01d2\7D\u01d5\nD\fD\16D\u01d8\13D\5")
        buf.write("D\u01da\nD\3E\3E\3E\3E\7E\u01e0\nE\fE\16E\u01e3\13E\3")
        buf.write("E\3E\6E\u01e7\nE\rE\16E\u01e8\7E\u01eb\nE\fE\16E\u01ee")
        buf.write("\13E\5E\u01f0\nE\3F\3F\3F\3F\7F\u01f6\nF\fF\16F\u01f9")
        buf.write("\13F\3F\3F\6F\u01fd\nF\rF\16F\u01fe\7F\u0201\nF\fF\16")
        buf.write("F\u0204\13F\5F\u0206\nF\3G\3G\3G\3G\5G\u020c\nG\3G\3G")
        buf.write("\3H\3H\3I\3I\7I\u0214\nI\fI\16I\u0217\13I\3J\3J\5J\u021b")
        buf.write("\nJ\3J\6J\u021e\nJ\rJ\16J\u021f\3K\3K\3K\5K\u0225\nK\3")
        buf.write("K\3K\3K\3K\3K\3K\5K\u022d\nK\3K\3K\3L\3L\3L\3L\3L\3L\3")
        buf.write("L\3L\3L\5L\u023a\nL\3M\3M\3M\3M\5M\u0240\nM\3N\3N\7N\u0244")
        buf.write("\nN\fN\16N\u0247\13N\3N\3N\3O\5O\u024c\nO\3O\7O\u024f")
        buf.write("\nO\fO\16O\u0252\13O\3P\3P\6P\u0256\nP\rP\16P\u0257\3")
        buf.write("Q\3Q\7Q\u025c\nQ\fQ\16Q\u025f\13Q\3Q\3Q\7Q\u0263\nQ\f")
        buf.write("Q\16Q\u0266\13Q\3Q\3Q\3R\3R\3R\3R\7R\u026e\nR\fR\16R\u0271")
        buf.write("\13R\3R\5R\u0274\nR\3R\3R\3S\3S\3S\3\u00c1\2T\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q\2s\2u\2w\2y")
        buf.write("\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2")
        buf.write("\u008b\2\u008d:\u008f\2\u0091\2\u0093\2\u0095;\u0097<")
        buf.write("\u0099\2\u009b=\u009d>\u009f?\u00a1@\u00a3A\u00a5B\3\2")
        buf.write("\22\5\2\13\f\17\17\"\"\t\2))^^ddhhppttvv\4\2\62;CH\3\2")
        buf.write("\629\3\2\62\63\3\2\62;\3\2\63;\3\2\639\4\2\63;CH\4\2G")
        buf.write("Ggg\4\2--//\4\2$$^^\5\2C\\aac|\6\2\62;C\\aac|\3\2$$\3")
        buf.write("\3\f\f\2\u028e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2\u008d\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2")
        buf.write("\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2")
        buf.write("\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\3\u00a7")
        buf.write("\3\2\2\2\5\u00af\3\2\2\2\7\u00b5\3\2\2\2\t\u00bb\3\2\2")
        buf.write("\2\13\u00c9\3\2\2\2\r\u00cf\3\2\2\2\17\u00d8\3\2\2\2\21")
        buf.write("\u00db\3\2\2\2\23\u00e2\3\2\2\2\25\u00e7\3\2\2\2\27\u00ef")
        buf.write("\3\2\2\2\31\u00f5\3\2\2\2\33\u00f8\3\2\2\2\35\u00fc\3")
        buf.write("\2\2\2\37\u0102\3\2\2\2!\u010a\3\2\2\2#\u0111\3\2\2\2")
        buf.write("%\u0118\3\2\2\2\'\u011d\3\2\2\2)\u0123\3\2\2\2+\u0127")
        buf.write("\3\2\2\2-\u012b\3\2\2\2/\u0137\3\2\2\2\61\u0142\3\2\2")
        buf.write("\2\63\u0146\3\2\2\2\65\u0149\3\2\2\2\67\u014e\3\2\2\2")
        buf.write("9\u0150\3\2\2\2;\u0152\3\2\2\2=\u0155\3\2\2\2?\u0158\3")
        buf.write("\2\2\2A\u015b\3\2\2\2C\u015e\3\2\2\2E\u0160\3\2\2\2G\u0162")
        buf.write("\3\2\2\2I\u0164\3\2\2\2K\u0166\3\2\2\2M\u0168\3\2\2\2")
        buf.write("O\u016a\3\2\2\2Q\u016d\3\2\2\2S\u016f\3\2\2\2U\u0172\3")
        buf.write("\2\2\2W\u0175\3\2\2\2Y\u0179\3\2\2\2[\u017b\3\2\2\2]\u017d")
        buf.write("\3\2\2\2_\u017f\3\2\2\2a\u0181\3\2\2\2c\u0183\3\2\2\2")
        buf.write("e\u0186\3\2\2\2g\u0188\3\2\2\2i\u018a\3\2\2\2k\u018d\3")
        buf.write("\2\2\2m\u018f\3\2\2\2o\u0191\3\2\2\2q\u0193\3\2\2\2s\u0195")
        buf.write("\3\2\2\2u\u0197\3\2\2\2w\u019a\3\2\2\2y\u01a0\3\2\2\2")
        buf.write("{\u01a6\3\2\2\2}\u01a8\3\2\2\2\177\u01aa\3\2\2\2\u0081")
        buf.write("\u01ac\3\2\2\2\u0083\u01ae\3\2\2\2\u0085\u01c3\3\2\2\2")
        buf.write("\u0087\u01c5\3\2\2\2\u0089\u01db\3\2\2\2\u008b\u01f1\3")
        buf.write("\2\2\2\u008d\u020b\3\2\2\2\u008f\u020f\3\2\2\2\u0091\u0211")
        buf.write("\3\2\2\2\u0093\u0218\3\2\2\2\u0095\u022c\3\2\2\2\u0097")
        buf.write("\u0239\3\2\2\2\u0099\u023f\3\2\2\2\u009b\u0241\3\2\2\2")
        buf.write("\u009d\u024b\3\2\2\2\u009f\u0253\3\2\2\2\u00a1\u0259\3")
        buf.write("\2\2\2\u00a3\u0269\3\2\2\2\u00a5\u0277\3\2\2\2\u00a7\u00a8")
        buf.write("\7R\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab")
        buf.write("\7i\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7o\2\2\u00ae\4\3\2\2\2\u00af\u00b0\7o\2\2\u00b0\u00b1")
        buf.write("\7c\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7p\2\2\u00b3\6")
        buf.write("\3\2\2\2\u00b4\u00b6\t\2\2\2\u00b5\u00b4\3\2\2\2\u00b6")
        buf.write("\u00b7\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2")
        buf.write("\u00b8\u00b9\3\2\2\2\u00b9\u00ba\b\4\2\2\u00ba\b\3\2\2")
        buf.write("\2\u00bb\u00bc\7%\2\2\u00bc\u00bd\7%\2\2\u00bd\u00c1\3")
        buf.write("\2\2\2\u00be\u00c0\13\2\2\2\u00bf\u00be\3\2\2\2\u00c0")
        buf.write("\u00c3\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c1\u00bf\3\2\2\2")
        buf.write("\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5\7")
        buf.write("%\2\2\u00c5\u00c6\7%\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8")
        buf.write("\b\5\2\2\u00c8\n\3\2\2\2\u00c9\u00ca\7D\2\2\u00ca\u00cb")
        buf.write("\7t\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce")
        buf.write("\7m\2\2\u00ce\f\3\2\2\2\u00cf\u00d0\7E\2\2\u00d0\u00d1")
        buf.write("\7q\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4")
        buf.write("\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\16\3\2\2\2\u00d8\u00d9\7K\2\2\u00d9\u00da")
        buf.write("\7h\2\2\u00da\20\3\2\2\2\u00db\u00dc\7G\2\2\u00dc\u00dd")
        buf.write("\7n\2\2\u00dd\u00de\7u\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7k\2\2\u00e0\u00e1\7h\2\2\u00e1\22\3\2\2\2\u00e2\u00e3")
        buf.write("\7G\2\2\u00e3\u00e4\7n\2\2\u00e4\u00e5\7u\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6\24\3\2\2\2\u00e7\u00e8\7H\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec")
        buf.write("\7c\2\2\u00ec\u00ed\7e\2\2\u00ed\u00ee\7j\2\2\u00ee\26")
        buf.write("\3\2\2\2\u00ef\u00f0\7C\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2")
        buf.write("\7t\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4\7{\2\2\u00f4\30")
        buf.write("\3\2\2\2\u00f5\u00f6\7K\2\2\u00f6\u00f7\7p\2\2\u00f7\32")
        buf.write("\3\2\2\2\u00f8\u00f9\7K\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb")
        buf.write("\7v\2\2\u00fb\34\3\2\2\2\u00fc\u00fd\7H\2\2\u00fd\u00fe")
        buf.write("\7n\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100\7c\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\36\3\2\2\2\u0102\u0103\7D\2\2\u0103\u0104")
        buf.write("\7q\2\2\u0104\u0105\7q\2\2\u0105\u0106\7n\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107\u0108\7c\2\2\u0108\u0109\7p\2\2\u0109 \3")
        buf.write("\2\2\2\u010a\u010b\7U\2\2\u010b\u010c\7v\2\2\u010c\u010d")
        buf.write("\7t\2\2\u010d\u010e\7k\2\2\u010e\u010f\7p\2\2\u010f\u0110")
        buf.write("\7i\2\2\u0110\"\3\2\2\2\u0111\u0112\7T\2\2\u0112\u0113")
        buf.write("\7g\2\2\u0113\u0114\7v\2\2\u0114\u0115\7w\2\2\u0115\u0116")
        buf.write("\7t\2\2\u0116\u0117\7p\2\2\u0117$\3\2\2\2\u0118\u0119")
        buf.write("\7P\2\2\u0119\u011a\7w\2\2\u011a\u011b\7n\2\2\u011b\u011c")
        buf.write("\7n\2\2\u011c&\3\2\2\2\u011d\u011e\7E\2\2\u011e\u011f")
        buf.write("\7n\2\2\u011f\u0120\7c\2\2\u0120\u0121\7u\2\2\u0121\u0122")
        buf.write("\7u\2\2\u0122(\3\2\2\2\u0123\u0124\7X\2\2\u0124\u0125")
        buf.write("\7c\2\2\u0125\u0126\7n\2\2\u0126*\3\2\2\2\u0127\u0128")
        buf.write("\7X\2\2\u0128\u0129\7c\2\2\u0129\u012a\7t\2\2\u012a,\3")
        buf.write("\2\2\2\u012b\u012c\7E\2\2\u012c\u012d\7q\2\2\u012d\u012e")
        buf.write("\7p\2\2\u012e\u012f\7u\2\2\u012f\u0130\7v\2\2\u0130\u0131")
        buf.write("\7t\2\2\u0131\u0132\7w\2\2\u0132\u0133\7e\2\2\u0133\u0134")
        buf.write("\7v\2\2\u0134\u0135\7q\2\2\u0135\u0136\7t\2\2\u0136.\3")
        buf.write("\2\2\2\u0137\u0138\7F\2\2\u0138\u0139\7g\2\2\u0139\u013a")
        buf.write("\7u\2\2\u013a\u013b\7v\2\2\u013b\u013c\7t\2\2\u013c\u013d")
        buf.write("\7w\2\2\u013d\u013e\7e\2\2\u013e\u013f\7v\2\2\u013f\u0140")
        buf.write("\7q\2\2\u0140\u0141\7t\2\2\u0141\60\3\2\2\2\u0142\u0143")
        buf.write("\7P\2\2\u0143\u0144\7g\2\2\u0144\u0145\7y\2\2\u0145\62")
        buf.write("\3\2\2\2\u0146\u0147\7D\2\2\u0147\u0148\7{\2\2\u0148\64")
        buf.write("\3\2\2\2\u0149\u014a\7U\2\2\u014a\u014b\7g\2\2\u014b\u014c")
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
        buf.write("\u0196\7$\2\2\u0196t\3\2\2\2\u0197\u0198\7^\2\2\u0198")
        buf.write("\u0199\t\3\2\2\u0199v\3\2\2\2\u019a\u019b\7\62\2\2\u019b")
        buf.write("x\3\2\2\2\u019c\u019d\7\62\2\2\u019d\u01a1\7z\2\2\u019e")
        buf.write("\u019f\7\62\2\2\u019f\u01a1\7Z\2\2\u01a0\u019c\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a1z\3\2\2\2\u01a2\u01a3\7\62\2")
        buf.write("\2\u01a3\u01a7\7d\2\2\u01a4\u01a5\7\62\2\2\u01a5\u01a7")
        buf.write("\7D\2\2\u01a6\u01a2\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7")
        buf.write("|\3\2\2\2\u01a8\u01a9\t\4\2\2\u01a9~\3\2\2\2\u01aa\u01ab")
        buf.write("\t\5\2\2\u01ab\u0080\3\2\2\2\u01ac\u01ad\t\6\2\2\u01ad")
        buf.write("\u0082\3\2\2\2\u01ae\u01af\t\7\2\2\u01af\u0084\3\2\2\2")
        buf.write("\u01b0\u01c4\5\u0083B\2\u01b1\u01b5\t\b\2\2\u01b2\u01b4")
        buf.write("\5\u0083B\2\u01b3\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01c0\3\2\2\2")
        buf.write("\u01b7\u01b5\3\2\2\2\u01b8\u01ba\7a\2\2\u01b9\u01bb\5")
        buf.write("\u0083B\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01bf\3\2\2\2")
        buf.write("\u01be\u01b8\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3")
        buf.write("\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c3\u01b0\3\2\2\2\u01c3\u01b1\3\2\2\2\u01c4")
        buf.write("\u0086\3\2\2\2\u01c5\u01d9\5w<\2\u01c6\u01da\7\62\2\2")
        buf.write("\u01c7\u01cb\t\t\2\2\u01c8\u01ca\5\177@\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb")
        buf.write("\u01cc\3\2\2\2\u01cc\u01d6\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01ce\u01d0\7a\2\2\u01cf\u01d1\5\177@\2\u01d0\u01cf\3")
        buf.write("\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3")
        buf.write("\3\2\2\2\u01d3\u01d5\3\2\2\2\u01d4\u01ce\3\2\2\2\u01d5")
        buf.write("\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2")
        buf.write("\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01c6\3")
        buf.write("\2\2\2\u01d9\u01c7\3\2\2\2\u01da\u0088\3\2\2\2\u01db\u01ef")
        buf.write("\5y=\2\u01dc\u01f0\7\62\2\2\u01dd\u01e1\t\n\2\2\u01de")
        buf.write("\u01e0\5}?\2\u01df\u01de\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1")
        buf.write("\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01ec\3\2\2\2")
        buf.write("\u01e3\u01e1\3\2\2\2\u01e4\u01e6\7a\2\2\u01e5\u01e7\5")
        buf.write("}?\2\u01e6\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e6")
        buf.write("\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01eb\3\2\2\2\u01ea")
        buf.write("\u01e4\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2")
        buf.write("\u01ec\u01ed\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3")
        buf.write("\2\2\2\u01ef\u01dc\3\2\2\2\u01ef\u01dd\3\2\2\2\u01f0\u008a")
        buf.write("\3\2\2\2\u01f1\u0205\5{>\2\u01f2\u0206\7\62\2\2\u01f3")
        buf.write("\u01f7\7\63\2\2\u01f4\u01f6\5\u0081A\2\u01f5\u01f4\3\2")
        buf.write("\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8")
        buf.write("\3\2\2\2\u01f8\u0202\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa")
        buf.write("\u01fc\7a\2\2\u01fb\u01fd\5\u0081A\2\u01fc\u01fb\3\2\2")
        buf.write("\2\u01fd\u01fe\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff")
        buf.write("\3\2\2\2\u01ff\u0201\3\2\2\2\u0200\u01fa\3\2\2\2\u0201")
        buf.write("\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203\3\2\2\2")
        buf.write("\u0203\u0206\3\2\2\2\u0204\u0202\3\2\2\2\u0205\u01f2\3")
        buf.write("\2\2\2\u0205\u01f3\3\2\2\2\u0206\u008c\3\2\2\2\u0207\u020c")
        buf.write("\5\u0085C\2\u0208\u020c\5\u0087D\2\u0209\u020c\5\u0089")
        buf.write("E\2\u020a\u020c\5\u008bF\2\u020b\u0207\3\2\2\2\u020b\u0208")
        buf.write("\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020a\3\2\2\2\u020c")
        buf.write("\u020d\3\2\2\2\u020d\u020e\bG\3\2\u020e\u008e\3\2\2\2")
        buf.write("\u020f\u0210\5\u0085C\2\u0210\u0090\3\2\2\2\u0211\u0215")
        buf.write("\5a\61\2\u0212\u0214\5\u0083B\2\u0213\u0212\3\2\2\2\u0214")
        buf.write("\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3\2\2\2")
        buf.write("\u0216\u0092\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u021a\t")
        buf.write("\13\2\2\u0219\u021b\t\f\2\2\u021a\u0219\3\2\2\2\u021a")
        buf.write("\u021b\3\2\2\2\u021b\u021d\3\2\2\2\u021c\u021e\5\u0083")
        buf.write("B\2\u021d\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u021d")
        buf.write("\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0094\3\2\2\2\u0221")
        buf.write("\u0222\5\u008fH\2\u0222\u0224\5\u0091I\2\u0223\u0225\5")
        buf.write("\u0093J\2\u0224\u0223\3\2\2\2\u0224\u0225\3\2\2\2\u0225")
        buf.write("\u022d\3\2\2\2\u0226\u0227\5\u008fH\2\u0227\u0228\5\u0093")
        buf.write("J\2\u0228\u022d\3\2\2\2\u0229\u022a\5\u0091I\2\u022a\u022b")
        buf.write("\5\u0093J\2\u022b\u022d\3\2\2\2\u022c\u0221\3\2\2\2\u022c")
        buf.write("\u0226\3\2\2\2\u022c\u0229\3\2\2\2\u022d\u022e\3\2\2\2")
        buf.write("\u022e\u022f\bK\4\2\u022f\u0096\3\2\2\2\u0230\u0231\7")
        buf.write("V\2\2\u0231\u0232\7t\2\2\u0232\u0233\7w\2\2\u0233\u023a")
        buf.write("\7g\2\2\u0234\u0235\7H\2\2\u0235\u0236\7c\2\2\u0236\u0237")
        buf.write("\7n\2\2\u0237\u0238\7u\2\2\u0238\u023a\7g\2\2\u0239\u0230")
        buf.write("\3\2\2\2\u0239\u0234\3\2\2\2\u023a\u0098\3\2\2\2\u023b")
        buf.write("\u0240\5u;\2\u023c\u0240\n\r\2\2\u023d\u023e\7)\2\2\u023e")
        buf.write("\u0240\7$\2\2\u023f\u023b\3\2\2\2\u023f\u023c\3\2\2\2")
        buf.write("\u023f\u023d\3\2\2\2\u0240\u009a\3\2\2\2\u0241\u0245\5")
        buf.write("s:\2\u0242\u0244\5\u0099M\2\u0243\u0242\3\2\2\2\u0244")
        buf.write("\u0247\3\2\2\2\u0245\u0243\3\2\2\2\u0245\u0246\3\2\2\2")
        buf.write("\u0246\u0248\3\2\2\2\u0247\u0245\3\2\2\2\u0248\u0249\5")
        buf.write("s:\2\u0249\u009c\3\2\2\2\u024a\u024c\t\16\2\2\u024b\u024a")
        buf.write("\3\2\2\2\u024c\u0250\3\2\2\2\u024d\u024f\t\17\2\2\u024e")
        buf.write("\u024d\3\2\2\2\u024f\u0252\3\2\2\2\u0250\u024e\3\2\2\2")
        buf.write("\u0250\u0251\3\2\2\2\u0251\u009e\3\2\2\2\u0252\u0250\3")
        buf.write("\2\2\2\u0253\u0255\7&\2\2\u0254\u0256\t\17\2\2\u0255\u0254")
        buf.write("\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0255\3\2\2\2\u0257")
        buf.write("\u0258\3\2\2\2\u0258\u00a0\3\2\2\2\u0259\u025d\5s:\2\u025a")
        buf.write("\u025c\5\u0099M\2\u025b\u025a\3\2\2\2\u025c\u025f\3\2")
        buf.write("\2\2\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u0260")
        buf.write("\3\2\2\2\u025f\u025d\3\2\2\2\u0260\u0264\7^\2\2\u0261")
        buf.write("\u0263\n\3\2\2\u0262\u0261\3\2\2\2\u0263\u0266\3\2\2\2")
        buf.write("\u0264\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0267\3")
        buf.write("\2\2\2\u0266\u0264\3\2\2\2\u0267\u0268\bQ\5\2\u0268\u00a2")
        buf.write("\3\2\2\2\u0269\u026f\5s:\2\u026a\u026e\n\20\2\2\u026b")
        buf.write("\u026c\7)\2\2\u026c\u026e\7$\2\2\u026d\u026a\3\2\2\2\u026d")
        buf.write("\u026b\3\2\2\2\u026e\u0271\3\2\2\2\u026f\u026d\3\2\2\2")
        buf.write("\u026f\u0270\3\2\2\2\u0270\u0273\3\2\2\2\u0271\u026f\3")
        buf.write("\2\2\2\u0272\u0274\t\21\2\2\u0273\u0272\3\2\2\2\u0274")
        buf.write("\u0275\3\2\2\2\u0275\u0276\bR\6\2\u0276\u00a4\3\2\2\2")
        buf.write("\u0277\u0278\13\2\2\2\u0278\u0279\bS\7\2\u0279\u00a6\3")
        buf.write("\2\2\2*\2\u00b7\u00c1\u01a0\u01a6\u01b5\u01bc\u01c0\u01c3")
        buf.write("\u01cb\u01d2\u01d6\u01d9\u01e1\u01e8\u01ec\u01ef\u01f7")
        buf.write("\u01fe\u0202\u0205\u020b\u0215\u021a\u021f\u0224\u022c")
        buf.write("\u0239\u023f\u0245\u024b\u024e\u0250\u0255\u0257\u025d")
        buf.write("\u0264\u026d\u026f\u0273\b\b\2\2\3G\2\3K\3\3Q\4\3R\5\3")
        buf.write("S\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    WHITE_SPACE = 3
    COMMENT = 4
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
    ILLEGAL_ESCAPE = 62
    UNCLOSE_STRING = 63
    ERROR_TOKEN = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'main'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
            "'Else'", "'Foreach'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
            "'='", "'!'", "'||'", "'&&'", "'=='", "'!='", "'%'", "'+'", 
            "'-'", "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", "'+.'", "'==.'", 
            "'('", "')'", "'['", "']'", "'.'", "'..'", "','", "':'", "'::'", 
            "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "WHITE_SPACE", "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", 
            "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", 
            "K_BOOLEAN", "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", "K_VAL", 
            "K_VAR", "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", "K_BY", "K_SELF", 
            "OP_ASSIGN", "OP_LOGICAL_NOT", "OP_LOGICAL_OR", "OP_LOGICAL_AND", 
            "OP_IS_EQUAL_TO", "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", 
            "OP_SUBTRACTION", "OP_MULTIPLICATION", "OP_DIVISION", "OP_LESS_THAN", 
            "OP_LESS_THAN_EQUAL", "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", 
            "OP_STRING_CONCATENATION", "OP_TWO_SAME_STRING", "LEFT_PAREN", 
            "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
            "DOT", "DOUBLE_DOT", "COMMA", "COLON", "DOUBLE_COLON", "SEMI_COLON", 
            "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "INTEGER_LITERAL", 
            "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", "IDENTIFIER", 
            "DOLAR_IDENTIFIER", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_TOKEN" ]

    ruleNames = [ "T__0", "T__1", "WHITE_SPACE", "COMMENT", "K_BREAK", "K_CONTINUE", 
                  "K_IF", "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", "K_ARRAY", 
                  "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", "K_RETURN", 
                  "K_NULL", "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", 
                  "K_DESTRUCTOR", "K_NEW", "K_BY", "K_SELF", "OP_ASSIGN", 
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
                  "DOLAR_IDENTIFIER", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
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
            actions[79] = self.ILLEGAL_ESCAPE_action 
            actions[80] = self.UNCLOSE_STRING_action 
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
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:])
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


