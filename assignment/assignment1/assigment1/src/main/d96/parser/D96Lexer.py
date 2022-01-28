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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u02b9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\3\2\3\2\3\2\3\2\7\2\u00b0\n\2\f\2\16\2\u00b3\13\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\3\67\5\67\u0187")
        buf.write("\n\67\38\38\38\38\58\u018d\n8\39\39\3:\3:\3;\3;\3<\3<")
        buf.write("\3=\3=\3=\7=\u019a\n=\f=\16=\u019d\13=\3=\3=\6=\u01a1")
        buf.write("\n=\r=\16=\u01a2\7=\u01a5\n=\f=\16=\u01a8\13=\5=\u01aa")
        buf.write("\n=\3>\3>\3>\3>\7>\u01b0\n>\f>\16>\u01b3\13>\3>\3>\6>")
        buf.write("\u01b7\n>\r>\16>\u01b8\7>\u01bb\n>\f>\16>\u01be\13>\5")
        buf.write(">\u01c0\n>\3?\3?\3?\3?\7?\u01c6\n?\f?\16?\u01c9\13?\3")
        buf.write("?\3?\6?\u01cd\n?\r?\16?\u01ce\7?\u01d1\n?\f?\16?\u01d4")
        buf.write("\13?\5?\u01d6\n?\3@\3@\3@\3@\7@\u01dc\n@\f@\16@\u01df")
        buf.write("\13@\3@\3@\6@\u01e3\n@\r@\16@\u01e4\7@\u01e7\n@\f@\16")
        buf.write("@\u01ea\13@\5@\u01ec\n@\3A\3A\7A\u01f0\nA\fA\16A\u01f3")
        buf.write("\13A\3A\3A\6A\u01f7\nA\rA\16A\u01f8\7A\u01fb\nA\fA\16")
        buf.write("A\u01fe\13A\5A\u0200\nA\3B\3B\3B\7B\u0205\nB\fB\16B\u0208")
        buf.write("\13B\3B\3B\6B\u020c\nB\rB\16B\u020d\7B\u0210\nB\fB\16")
        buf.write("B\u0213\13B\3C\3C\3C\7C\u0218\nC\fC\16C\u021b\13C\3C\3")
        buf.write("C\6C\u021f\nC\rC\16C\u0220\7C\u0223\nC\fC\16C\u0226\13")
        buf.write("C\3D\3D\3D\7D\u022b\nD\fD\16D\u022e\13D\3D\3D\6D\u0232")
        buf.write("\nD\rD\16D\u0233\7D\u0236\nD\fD\16D\u0239\13D\3E\3E\3")
        buf.write("E\3E\5E\u023f\nE\3E\3E\3F\3F\3F\3F\5F\u0247\nF\3F\3F\3")
        buf.write("G\3G\3H\3H\7H\u024f\nH\fH\16H\u0252\13H\3I\3I\5I\u0256")
        buf.write("\nI\3I\6I\u0259\nI\rI\16I\u025a\3J\3J\3J\5J\u0260\nJ\3")
        buf.write("J\3J\3J\3J\3J\3J\5J\u0268\nJ\3J\3J\3K\3K\3K\3K\3K\3K\3")
        buf.write("K\3K\3K\5K\u0275\nK\3L\3L\7L\u0279\nL\fL\16L\u027c\13")
        buf.write("L\3L\3L\3L\3M\3M\7M\u0283\nM\fM\16M\u0286\13M\3N\3N\6")
        buf.write("N\u028a\nN\rN\16N\u028b\3O\6O\u028f\nO\rO\16O\u0290\3")
        buf.write("O\3O\3P\3P\7P\u0297\nP\fP\16P\u029a\13P\3P\5P\u029d\n")
        buf.write("P\3P\3P\3Q\3Q\7Q\u02a3\nQ\fQ\16Q\u02a6\13Q\3Q\3Q\3Q\3")
        buf.write("R\3R\3R\3R\5R\u02af\nR\3S\3S\3S\3T\3T\3T\3U\3U\3U\3\u00b1")
        buf.write("\2V\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\2k\2m\2o\2q")
        buf.write("\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087")
        buf.write("\2\u0089\66\u008b\67\u008d\2\u008f\2\u0091\2\u00938\u0095")
        buf.write("9\u0097:\u0099;\u009b<\u009d=\u009f>\u00a1?\u00a3\2\u00a5")
        buf.write("\2\u00a7\2\u00a9@\3\2\21\4\2\62;CH\3\2\629\3\2\62\63\3")
        buf.write("\2\62;\3\2\63;\3\2\639\4\2\63;CH\4\2GGgg\4\2--//\5\2C")
        buf.write("\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\7\3\n\f\16\17")
        buf.write("$$))^^\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\2\u02d7\2\3")
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
        buf.write("\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u0093\3\2\2\2")
        buf.write("\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\3\u00ab\3\2\2\2\5\u00b9\3\2\2\2\7\u00bf")
        buf.write("\3\2\2\2\t\u00c8\3\2\2\2\13\u00cb\3\2\2\2\r\u00d2\3\2")
        buf.write("\2\2\17\u00d7\3\2\2\2\21\u00df\3\2\2\2\23\u00e5\3\2\2")
        buf.write("\2\25\u00e8\3\2\2\2\27\u00ec\3\2\2\2\31\u00f2\3\2\2\2")
        buf.write("\33\u00fa\3\2\2\2\35\u0101\3\2\2\2\37\u0108\3\2\2\2!\u010d")
        buf.write("\3\2\2\2#\u0113\3\2\2\2%\u0117\3\2\2\2\'\u011b\3\2\2\2")
        buf.write(")\u0127\3\2\2\2+\u0132\3\2\2\2-\u0136\3\2\2\2/\u0139\3")
        buf.write("\2\2\2\61\u013b\3\2\2\2\63\u013d\3\2\2\2\65\u0140\3\2")
        buf.write("\2\2\67\u0143\3\2\2\29\u0146\3\2\2\2;\u0149\3\2\2\2=\u014b")
        buf.write("\3\2\2\2?\u014d\3\2\2\2A\u014f\3\2\2\2C\u0151\3\2\2\2")
        buf.write("E\u0153\3\2\2\2G\u0155\3\2\2\2I\u0158\3\2\2\2K\u015a\3")
        buf.write("\2\2\2M\u015d\3\2\2\2O\u0160\3\2\2\2Q\u0164\3\2\2\2S\u0166")
        buf.write("\3\2\2\2U\u0168\3\2\2\2W\u016a\3\2\2\2Y\u016c\3\2\2\2")
        buf.write("[\u016e\3\2\2\2]\u0171\3\2\2\2_\u0173\3\2\2\2a\u0175\3")
        buf.write("\2\2\2c\u0178\3\2\2\2e\u017a\3\2\2\2g\u017c\3\2\2\2i\u017e")
        buf.write("\3\2\2\2k\u0180\3\2\2\2m\u0186\3\2\2\2o\u018c\3\2\2\2")
        buf.write("q\u018e\3\2\2\2s\u0190\3\2\2\2u\u0192\3\2\2\2w\u0194\3")
        buf.write("\2\2\2y\u01a9\3\2\2\2{\u01ab\3\2\2\2}\u01c1\3\2\2\2\177")
        buf.write("\u01d7\3\2\2\2\u0081\u01ed\3\2\2\2\u0083\u0201\3\2\2\2")
        buf.write("\u0085\u0214\3\2\2\2\u0087\u0227\3\2\2\2\u0089\u023e\3")
        buf.write("\2\2\2\u008b\u0246\3\2\2\2\u008d\u024a\3\2\2\2\u008f\u024c")
        buf.write("\3\2\2\2\u0091\u0253\3\2\2\2\u0093\u0267\3\2\2\2\u0095")
        buf.write("\u0274\3\2\2\2\u0097\u0276\3\2\2\2\u0099\u0280\3\2\2\2")
        buf.write("\u009b\u0287\3\2\2\2\u009d\u028e\3\2\2\2\u009f\u0294\3")
        buf.write("\2\2\2\u00a1\u02a0\3\2\2\2\u00a3\u02ae\3\2\2\2\u00a5\u02b0")
        buf.write("\3\2\2\2\u00a7\u02b3\3\2\2\2\u00a9\u02b6\3\2\2\2\u00ab")
        buf.write("\u00ac\7%\2\2\u00ac\u00ad\7%\2\2\u00ad\u00b1\3\2\2\2\u00ae")
        buf.write("\u00b0\13\2\2\2\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2")
        buf.write("\2\u00b1\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b4")
        buf.write("\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\7%\2\2\u00b5")
        buf.write("\u00b6\7%\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\b\2\2\2")
        buf.write("\u00b8\4\3\2\2\2\u00b9\u00ba\7D\2\2\u00ba\u00bb\7t\2\2")
        buf.write("\u00bb\u00bc\7g\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be\7m")
        buf.write("\2\2\u00be\6\3\2\2\2\u00bf\u00c0\7E\2\2\u00c0\u00c1\7")
        buf.write("q\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4")
        buf.write("\7k\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7\b\3\2\2\2\u00c8\u00c9\7K\2\2\u00c9\u00ca")
        buf.write("\7h\2\2\u00ca\n\3\2\2\2\u00cb\u00cc\7G\2\2\u00cc\u00cd")
        buf.write("\7n\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0")
        buf.write("\7k\2\2\u00d0\u00d1\7h\2\2\u00d1\f\3\2\2\2\u00d2\u00d3")
        buf.write("\7G\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5\7u\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\16\3\2\2\2\u00d7\u00d8\7H\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7g\2\2\u00db\u00dc")
        buf.write("\7c\2\2\u00dc\u00dd\7e\2\2\u00dd\u00de\7j\2\2\u00de\20")
        buf.write("\3\2\2\2\u00df\u00e0\7C\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7{\2\2\u00e4\22")
        buf.write("\3\2\2\2\u00e5\u00e6\7K\2\2\u00e6\u00e7\7p\2\2\u00e7\24")
        buf.write("\3\2\2\2\u00e8\u00e9\7K\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb")
        buf.write("\7v\2\2\u00eb\26\3\2\2\2\u00ec\u00ed\7H\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1")
        buf.write("\7v\2\2\u00f1\30\3\2\2\2\u00f2\u00f3\7D\2\2\u00f3\u00f4")
        buf.write("\7q\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7")
        buf.write("\7g\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7p\2\2\u00f9\32")
        buf.write("\3\2\2\2\u00fa\u00fb\7U\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7t\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100")
        buf.write("\7i\2\2\u0100\34\3\2\2\2\u0101\u0102\7T\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\u0104\7v\2\2\u0104\u0105\7w\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106\u0107\7p\2\2\u0107\36\3\2\2\2\u0108\u0109")
        buf.write("\7P\2\2\u0109\u010a\7w\2\2\u010a\u010b\7n\2\2\u010b\u010c")
        buf.write("\7n\2\2\u010c \3\2\2\2\u010d\u010e\7E\2\2\u010e\u010f")
        buf.write("\7n\2\2\u010f\u0110\7c\2\2\u0110\u0111\7u\2\2\u0111\u0112")
        buf.write("\7u\2\2\u0112\"\3\2\2\2\u0113\u0114\7X\2\2\u0114\u0115")
        buf.write("\7c\2\2\u0115\u0116\7n\2\2\u0116$\3\2\2\2\u0117\u0118")
        buf.write("\7X\2\2\u0118\u0119\7c\2\2\u0119\u011a\7t\2\2\u011a&\3")
        buf.write("\2\2\2\u011b\u011c\7E\2\2\u011c\u011d\7q\2\2\u011d\u011e")
        buf.write("\7p\2\2\u011e\u011f\7u\2\2\u011f\u0120\7v\2\2\u0120\u0121")
        buf.write("\7t\2\2\u0121\u0122\7w\2\2\u0122\u0123\7e\2\2\u0123\u0124")
        buf.write("\7v\2\2\u0124\u0125\7q\2\2\u0125\u0126\7t\2\2\u0126(\3")
        buf.write("\2\2\2\u0127\u0128\7F\2\2\u0128\u0129\7g\2\2\u0129\u012a")
        buf.write("\7u\2\2\u012a\u012b\7v\2\2\u012b\u012c\7t\2\2\u012c\u012d")
        buf.write("\7w\2\2\u012d\u012e\7e\2\2\u012e\u012f\7v\2\2\u012f\u0130")
        buf.write("\7q\2\2\u0130\u0131\7t\2\2\u0131*\3\2\2\2\u0132\u0133")
        buf.write("\7P\2\2\u0133\u0134\7g\2\2\u0134\u0135\7y\2\2\u0135,\3")
        buf.write("\2\2\2\u0136\u0137\7D\2\2\u0137\u0138\7{\2\2\u0138.\3")
        buf.write("\2\2\2\u0139\u013a\7?\2\2\u013a\60\3\2\2\2\u013b\u013c")
        buf.write("\7#\2\2\u013c\62\3\2\2\2\u013d\u013e\7~\2\2\u013e\u013f")
        buf.write("\7~\2\2\u013f\64\3\2\2\2\u0140\u0141\7(\2\2\u0141\u0142")
        buf.write("\7(\2\2\u0142\66\3\2\2\2\u0143\u0144\7?\2\2\u0144\u0145")
        buf.write("\7?\2\2\u01458\3\2\2\2\u0146\u0147\7#\2\2\u0147\u0148")
        buf.write("\7?\2\2\u0148:\3\2\2\2\u0149\u014a\7\'\2\2\u014a<\3\2")
        buf.write("\2\2\u014b\u014c\7-\2\2\u014c>\3\2\2\2\u014d\u014e\7/")
        buf.write("\2\2\u014e@\3\2\2\2\u014f\u0150\7,\2\2\u0150B\3\2\2\2")
        buf.write("\u0151\u0152\7\61\2\2\u0152D\3\2\2\2\u0153\u0154\7>\2")
        buf.write("\2\u0154F\3\2\2\2\u0155\u0156\7>\2\2\u0156\u0157\7?\2")
        buf.write("\2\u0157H\3\2\2\2\u0158\u0159\7@\2\2\u0159J\3\2\2\2\u015a")
        buf.write("\u015b\7@\2\2\u015b\u015c\7?\2\2\u015cL\3\2\2\2\u015d")
        buf.write("\u015e\7-\2\2\u015e\u015f\7\60\2\2\u015fN\3\2\2\2\u0160")
        buf.write("\u0161\7?\2\2\u0161\u0162\7?\2\2\u0162\u0163\7\60\2\2")
        buf.write("\u0163P\3\2\2\2\u0164\u0165\7*\2\2\u0165R\3\2\2\2\u0166")
        buf.write("\u0167\7+\2\2\u0167T\3\2\2\2\u0168\u0169\7]\2\2\u0169")
        buf.write("V\3\2\2\2\u016a\u016b\7_\2\2\u016bX\3\2\2\2\u016c\u016d")
        buf.write("\7\60\2\2\u016dZ\3\2\2\2\u016e\u016f\7\60\2\2\u016f\u0170")
        buf.write("\7\60\2\2\u0170\\\3\2\2\2\u0171\u0172\7.\2\2\u0172^\3")
        buf.write("\2\2\2\u0173\u0174\7<\2\2\u0174`\3\2\2\2\u0175\u0176\7")
        buf.write("<\2\2\u0176\u0177\7<\2\2\u0177b\3\2\2\2\u0178\u0179\7")
        buf.write("=\2\2\u0179d\3\2\2\2\u017a\u017b\7}\2\2\u017bf\3\2\2\2")
        buf.write("\u017c\u017d\7\177\2\2\u017dh\3\2\2\2\u017e\u017f\7$\2")
        buf.write("\2\u017fj\3\2\2\2\u0180\u0181\7\62\2\2\u0181l\3\2\2\2")
        buf.write("\u0182\u0183\7\62\2\2\u0183\u0187\7z\2\2\u0184\u0185\7")
        buf.write("\62\2\2\u0185\u0187\7Z\2\2\u0186\u0182\3\2\2\2\u0186\u0184")
        buf.write("\3\2\2\2\u0187n\3\2\2\2\u0188\u0189\7\62\2\2\u0189\u018d")
        buf.write("\7d\2\2\u018a\u018b\7\62\2\2\u018b\u018d\7D\2\2\u018c")
        buf.write("\u0188\3\2\2\2\u018c\u018a\3\2\2\2\u018dp\3\2\2\2\u018e")
        buf.write("\u018f\t\2\2\2\u018fr\3\2\2\2\u0190\u0191\t\3\2\2\u0191")
        buf.write("t\3\2\2\2\u0192\u0193\t\4\2\2\u0193v\3\2\2\2\u0194\u0195")
        buf.write("\t\5\2\2\u0195x\3\2\2\2\u0196\u01aa\5w<\2\u0197\u019b")
        buf.write("\t\6\2\2\u0198\u019a\5w<\2\u0199\u0198\3\2\2\2\u019a\u019d")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u01a6\3\2\2\2\u019d\u019b\3\2\2\2\u019e\u01a0\7a\2\2")
        buf.write("\u019f\u01a1\5w<\2\u01a0\u019f\3\2\2\2\u01a1\u01a2\3\2")
        buf.write("\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a5")
        buf.write("\3\2\2\2\u01a4\u019e\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01aa\3\2\2\2")
        buf.write("\u01a8\u01a6\3\2\2\2\u01a9\u0196\3\2\2\2\u01a9\u0197\3")
        buf.write("\2\2\2\u01aaz\3\2\2\2\u01ab\u01bf\5k\66\2\u01ac\u01c0")
        buf.write("\7\62\2\2\u01ad\u01b1\t\7\2\2\u01ae\u01b0\5s:\2\u01af")
        buf.write("\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2")
        buf.write("\u01b1\u01b2\3\2\2\2\u01b2\u01bc\3\2\2\2\u01b3\u01b1\3")
        buf.write("\2\2\2\u01b4\u01b6\7a\2\2\u01b5\u01b7\5s:\2\u01b6\u01b5")
        buf.write("\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b4\3\2\2\2")
        buf.write("\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3")
        buf.write("\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01ac")
        buf.write("\3\2\2\2\u01bf\u01ad\3\2\2\2\u01c0|\3\2\2\2\u01c1\u01d5")
        buf.write("\5m\67\2\u01c2\u01d6\7\62\2\2\u01c3\u01c7\t\b\2\2\u01c4")
        buf.write("\u01c6\5q9\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7")
        buf.write("\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01d2\3\2\2\2")
        buf.write("\u01c9\u01c7\3\2\2\2\u01ca\u01cc\7a\2\2\u01cb\u01cd\5")
        buf.write("q9\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cc")
        buf.write("\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d1\3\2\2\2\u01d0")
        buf.write("\u01ca\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2")
        buf.write("\u01d2\u01d3\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3")
        buf.write("\2\2\2\u01d5\u01c2\3\2\2\2\u01d5\u01c3\3\2\2\2\u01d6~")
        buf.write("\3\2\2\2\u01d7\u01eb\5o8\2\u01d8\u01ec\7\62\2\2\u01d9")
        buf.write("\u01dd\7\63\2\2\u01da\u01dc\5u;\2\u01db\u01da\3\2\2\2")
        buf.write("\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3")
        buf.write("\2\2\2\u01de\u01e8\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e2")
        buf.write("\7a\2\2\u01e1\u01e3\5u;\2\u01e2\u01e1\3\2\2\2\u01e3\u01e4")
        buf.write("\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5")
        buf.write("\u01e7\3\2\2\2\u01e6\u01e0\3\2\2\2\u01e7\u01ea\3\2\2\2")
        buf.write("\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ec\3")
        buf.write("\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01d8\3\2\2\2\u01eb\u01d9")
        buf.write("\3\2\2\2\u01ec\u0080\3\2\2\2\u01ed\u01ff\t\6\2\2\u01ee")
        buf.write("\u01f0\5w<\2\u01ef\u01ee\3\2\2\2\u01f0\u01f3\3\2\2\2\u01f1")
        buf.write("\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01fc\3\2\2\2")
        buf.write("\u01f3\u01f1\3\2\2\2\u01f4\u01f6\7a\2\2\u01f5\u01f7\5")
        buf.write("w<\2\u01f6\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f6")
        buf.write("\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb\3\2\2\2\u01fa")
        buf.write("\u01f4\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2")
        buf.write("\u01fc\u01fd\3\2\2\2\u01fd\u0200\3\2\2\2\u01fe\u01fc\3")
        buf.write("\2\2\2\u01ff\u01f1\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0082")
        buf.write("\3\2\2\2\u0201\u0202\5k\66\2\u0202\u0206\t\7\2\2\u0203")
        buf.write("\u0205\5s:\2\u0204\u0203\3\2\2\2\u0205\u0208\3\2\2\2\u0206")
        buf.write("\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0211\3\2\2\2")
        buf.write("\u0208\u0206\3\2\2\2\u0209\u020b\7a\2\2\u020a\u020c\5")
        buf.write("s:\2\u020b\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020b")
        buf.write("\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u0210\3\2\2\2\u020f")
        buf.write("\u0209\3\2\2\2\u0210\u0213\3\2\2\2\u0211\u020f\3\2\2\2")
        buf.write("\u0211\u0212\3\2\2\2\u0212\u0084\3\2\2\2\u0213\u0211\3")
        buf.write("\2\2\2\u0214\u0215\5m\67\2\u0215\u0219\t\b\2\2\u0216\u0218")
        buf.write("\5q9\2\u0217\u0216\3\2\2\2\u0218\u021b\3\2\2\2\u0219\u0217")
        buf.write("\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u0224\3\2\2\2\u021b")
        buf.write("\u0219\3\2\2\2\u021c\u021e\7a\2\2\u021d\u021f\5q9\2\u021e")
        buf.write("\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u021e\3\2\2\2")
        buf.write("\u0220\u0221\3\2\2\2\u0221\u0223\3\2\2\2\u0222\u021c\3")
        buf.write("\2\2\2\u0223\u0226\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225")
        buf.write("\3\2\2\2\u0225\u0086\3\2\2\2\u0226\u0224\3\2\2\2\u0227")
        buf.write("\u0228\5o8\2\u0228\u022c\7\63\2\2\u0229\u022b\5u;\2\u022a")
        buf.write("\u0229\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022a\3\2\2\2")
        buf.write("\u022c\u022d\3\2\2\2\u022d\u0237\3\2\2\2\u022e\u022c\3")
        buf.write("\2\2\2\u022f\u0231\7a\2\2\u0230\u0232\5u;\2\u0231\u0230")
        buf.write("\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0231\3\2\2\2\u0233")
        buf.write("\u0234\3\2\2\2\u0234\u0236\3\2\2\2\u0235\u022f\3\2\2\2")
        buf.write("\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238\3")
        buf.write("\2\2\2\u0238\u0088\3\2\2\2\u0239\u0237\3\2\2\2\u023a\u023f")
        buf.write("\5\u0081A\2\u023b\u023f\5\u0083B\2\u023c\u023f\5\u0085")
        buf.write("C\2\u023d\u023f\5\u0087D\2\u023e\u023a\3\2\2\2\u023e\u023b")
        buf.write("\3\2\2\2\u023e\u023c\3\2\2\2\u023e\u023d\3\2\2\2\u023f")
        buf.write("\u0240\3\2\2\2\u0240\u0241\bE\3\2\u0241\u008a\3\2\2\2")
        buf.write("\u0242\u0247\5y=\2\u0243\u0247\5{>\2\u0244\u0247\5}?\2")
        buf.write("\u0245\u0247\5\177@\2\u0246\u0242\3\2\2\2\u0246\u0243")
        buf.write("\3\2\2\2\u0246\u0244\3\2\2\2\u0246\u0245\3\2\2\2\u0247")
        buf.write("\u0248\3\2\2\2\u0248\u0249\bF\4\2\u0249\u008c\3\2\2\2")
        buf.write("\u024a\u024b\5y=\2\u024b\u008e\3\2\2\2\u024c\u0250\5Y")
        buf.write("-\2\u024d\u024f\5w<\2\u024e\u024d\3\2\2\2\u024f\u0252")
        buf.write("\3\2\2\2\u0250\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251")
        buf.write("\u0090\3\2\2\2\u0252\u0250\3\2\2\2\u0253\u0255\t\t\2\2")
        buf.write("\u0254\u0256\t\n\2\2\u0255\u0254\3\2\2\2\u0255\u0256\3")
        buf.write("\2\2\2\u0256\u0258\3\2\2\2\u0257\u0259\5w<\2\u0258\u0257")
        buf.write("\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u0258\3\2\2\2\u025a")
        buf.write("\u025b\3\2\2\2\u025b\u0092\3\2\2\2\u025c\u025d\5\u008d")
        buf.write("G\2\u025d\u025f\5\u008fH\2\u025e\u0260\5\u0091I\2\u025f")
        buf.write("\u025e\3\2\2\2\u025f\u0260\3\2\2\2\u0260\u0268\3\2\2\2")
        buf.write("\u0261\u0262\5\u008dG\2\u0262\u0263\5\u0091I\2\u0263\u0268")
        buf.write("\3\2\2\2\u0264\u0265\5\u008fH\2\u0265\u0266\5\u0091I\2")
        buf.write("\u0266\u0268\3\2\2\2\u0267\u025c\3\2\2\2\u0267\u0261\3")
        buf.write("\2\2\2\u0267\u0264\3\2\2\2\u0268\u0269\3\2\2\2\u0269\u026a")
        buf.write("\bJ\5\2\u026a\u0094\3\2\2\2\u026b\u026c\7V\2\2\u026c\u026d")
        buf.write("\7t\2\2\u026d\u026e\7w\2\2\u026e\u0275\7g\2\2\u026f\u0270")
        buf.write("\7H\2\2\u0270\u0271\7c\2\2\u0271\u0272\7n\2\2\u0272\u0273")
        buf.write("\7u\2\2\u0273\u0275\7g\2\2\u0274\u026b\3\2\2\2\u0274\u026f")
        buf.write("\3\2\2\2\u0275\u0096\3\2\2\2\u0276\u027a\5i\65\2\u0277")
        buf.write("\u0279\5\u00a3R\2\u0278\u0277\3\2\2\2\u0279\u027c\3\2")
        buf.write("\2\2\u027a\u0278\3\2\2\2\u027a\u027b\3\2\2\2\u027b\u027d")
        buf.write("\3\2\2\2\u027c\u027a\3\2\2\2\u027d\u027e\5i\65\2\u027e")
        buf.write("\u027f\bL\6\2\u027f\u0098\3\2\2\2\u0280\u0284\t\13\2\2")
        buf.write("\u0281\u0283\t\f\2\2\u0282\u0281\3\2\2\2\u0283\u0286\3")
        buf.write("\2\2\2\u0284\u0282\3\2\2\2\u0284\u0285\3\2\2\2\u0285\u009a")
        buf.write("\3\2\2\2\u0286\u0284\3\2\2\2\u0287\u0289\7&\2\2\u0288")
        buf.write("\u028a\t\f\2\2\u0289\u0288\3\2\2\2\u028a\u028b\3\2\2\2")
        buf.write("\u028b\u0289\3\2\2\2\u028b\u028c\3\2\2\2\u028c\u009c\3")
        buf.write("\2\2\2\u028d\u028f\t\r\2\2\u028e\u028d\3\2\2\2\u028f\u0290")
        buf.write("\3\2\2\2\u0290\u028e\3\2\2\2\u0290\u0291\3\2\2\2\u0291")
        buf.write("\u0292\3\2\2\2\u0292\u0293\bO\2\2\u0293\u009e\3\2\2\2")
        buf.write("\u0294\u0298\5i\65\2\u0295\u0297\5\u00a3R\2\u0296\u0295")
        buf.write("\3\2\2\2\u0297\u029a\3\2\2\2\u0298\u0296\3\2\2\2\u0298")
        buf.write("\u0299\3\2\2\2\u0299\u029c\3\2\2\2\u029a\u0298\3\2\2\2")
        buf.write("\u029b\u029d\t\16\2\2\u029c\u029b\3\2\2\2\u029d\u029e")
        buf.write("\3\2\2\2\u029e\u029f\bP\7\2\u029f\u00a0\3\2\2\2\u02a0")
        buf.write("\u02a4\5i\65\2\u02a1\u02a3\5\u00a3R\2\u02a2\u02a1\3\2")
        buf.write("\2\2\u02a3\u02a6\3\2\2\2\u02a4\u02a2\3\2\2\2\u02a4\u02a5")
        buf.write("\3\2\2\2\u02a5\u02a7\3\2\2\2\u02a6\u02a4\3\2\2\2\u02a7")
        buf.write("\u02a8\5\u00a7T\2\u02a8\u02a9\bQ\b\2\u02a9\u00a2\3\2\2")
        buf.write("\2\u02aa\u02af\n\17\2\2\u02ab\u02af\5\u00a5S\2\u02ac\u02ad")
        buf.write("\7)\2\2\u02ad\u02af\5i\65\2\u02ae\u02aa\3\2\2\2\u02ae")
        buf.write("\u02ab\3\2\2\2\u02ae\u02ac\3\2\2\2\u02af\u00a4\3\2\2\2")
        buf.write("\u02b0\u02b1\7^\2\2\u02b1\u02b2\t\20\2\2\u02b2\u00a6\3")
        buf.write("\2\2\2\u02b3\u02b4\7^\2\2\u02b4\u02b5\n\20\2\2\u02b5\u00a8")
        buf.write("\3\2\2\2\u02b6\u02b7\13\2\2\2\u02b7\u02b8\bU\t\2\u02b8")
        buf.write("\u00aa\3\2\2\2\63\2\u00b1\u0186\u018c\u019b\u01a2\u01a6")
        buf.write("\u01a9\u01b1\u01b8\u01bc\u01bf\u01c7\u01ce\u01d2\u01d5")
        buf.write("\u01dd\u01e4\u01e8\u01eb\u01f1\u01f8\u01fc\u01ff\u0206")
        buf.write("\u020d\u0211\u0219\u0220\u0224\u022c\u0233\u0237\u023e")
        buf.write("\u0246\u0250\u0255\u025a\u025f\u0267\u0274\u027a\u0284")
        buf.write("\u028b\u0290\u0298\u029c\u02a4\u02ae\n\b\2\2\3E\2\3F\3")
        buf.write("\3J\4\3L\5\3P\6\3Q\7\3U\b")
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
    DOUBLE_DOT = 45
    COMMA = 46
    COLON = 47
    DOUBLE_COLON = 48
    SEMI_COLON = 49
    LEFT_CURLY_BRACKET = 50
    RIGHT_CURLY_BRACKET = 51
    INTEGER_LITERAL2 = 52
    INTEGER_LITERAL = 53
    FLOAT_LITERAL = 54
    BOOLEAN_LITERAL = 55
    STRING_LITERAL = 56
    IDENTIFIER = 57
    DOLAR_IDENTIFIER = 58
    WS = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
            "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'='", "'!'", "'||'", "'&&'", 
            "'=='", "'!='", "'%'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", 
            "'>'", "'>='", "'+.'", "'==.'", "'('", "')'", "'['", "']'", 
            "'.'", "'..'", "','", "':'", "'::'", "';'", "'{'", "'}'" ]

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
            "RIGHT_SQUARE_BRACKET", "DOT", "DOUBLE_DOT", "COMMA", "COLON", 
            "DOUBLE_COLON", "SEMI_COLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
            "INTEGER_LITERAL2", "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", 
            "STRING_LITERAL", "IDENTIFIER", "DOLAR_IDENTIFIER", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
                  "DOT", "DOUBLE_DOT", "COMMA", "COLON", "DOUBLE_COLON", 
                  "SEMI_COLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                  "DOUBLE_QUOTE", "OCTAL_NOTATION", "HEXA_NOTATION", "BINARY_NOTATION", 
                  "HEXA_DIGIT", "OCTAL_DIGIT", "BINARY_DIGIT", "DECIMAL_DIGIT", 
                  "DECIMAL", "OCTAL", "HEXA", "BINARY", "DECIMAL2", "OCTAL2", 
                  "HEXA2", "BINARY2", "INTEGER_LITERAL2", "INTEGER_LITERAL", 
                  "INTEGER_PART", "DECIMAL_PART", "EXPONENT", "FLOAT_LITERAL", 
                  "BOOLEAN_LITERAL", "STRING_LITERAL", "IDENTIFIER", "DOLAR_IDENTIFIER", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STR_CHAR", 
                  "ESC_ACCEPT", "ESC_ILLEGAL", "ERROR_CHAR" ]

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
            actions[67] = self.INTEGER_LITERAL2_action 
            actions[68] = self.INTEGER_LITERAL_action 
            actions[72] = self.FLOAT_LITERAL_action 
            actions[74] = self.STRING_LITERAL_action 
            actions[78] = self.UNCLOSE_STRING_action 
            actions[79] = self.ILLEGAL_ESCAPE_action 
            actions[83] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_LITERAL2_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def INTEGER_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def FLOAT_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace("_", "")
     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             self.text = self.text[1:-1] 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                                    y = str(self.text)
                                    possible = ['b','\t','\n','\f','\r',"'",'\\']
                                    if y[-1] in possible:
                                        raise UncloseString(y[1:-1])
                                    else:
                                        raise UncloseString(y[1:])
                                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                                    y = str(self.text)
                                    raise IllegalEscape(y[1:])
                                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                                    raise ErrorToken(self.text)
                                
     


