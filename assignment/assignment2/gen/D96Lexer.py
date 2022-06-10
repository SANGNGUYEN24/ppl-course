# Generated from C:/development-area/ppl/ppl-course/assignment/assignment2/initial/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
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
        buf.write("\u02d8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\3\2\3\2\3\2\3\2\5\2\u00b4\n\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00c2\n\4\f")
        buf.write("\4\16\4\u00c5\13\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\38\38\58\u0192\n8\39\39\39")
        buf.write("\39\59\u0198\n9\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\7>\u01a5")
        buf.write("\n>\f>\16>\u01a8\13>\3>\3>\6>\u01ac\n>\r>\16>\u01ad\7")
        buf.write(">\u01b0\n>\f>\16>\u01b3\13>\5>\u01b5\n>\3?\3?\3?\3?\7")
        buf.write("?\u01bb\n?\f?\16?\u01be\13?\3?\3?\6?\u01c2\n?\r?\16?\u01c3")
        buf.write("\7?\u01c6\n?\f?\16?\u01c9\13?\5?\u01cb\n?\3@\3@\3@\3@")
        buf.write("\7@\u01d1\n@\f@\16@\u01d4\13@\3@\3@\6@\u01d8\n@\r@\16")
        buf.write("@\u01d9\7@\u01dc\n@\f@\16@\u01df\13@\5@\u01e1\n@\3A\3")
        buf.write("A\3A\3A\7A\u01e7\nA\fA\16A\u01ea\13A\3A\3A\6A\u01ee\n")
        buf.write("A\rA\16A\u01ef\7A\u01f2\nA\fA\16A\u01f5\13A\5A\u01f7\n")
        buf.write("A\3B\3B\7B\u01fb\nB\fB\16B\u01fe\13B\3B\3B\6B\u0202\n")
        buf.write("B\rB\16B\u0203\7B\u0206\nB\fB\16B\u0209\13B\5B\u020b\n")
        buf.write("B\3C\3C\3C\7C\u0210\nC\fC\16C\u0213\13C\3C\3C\6C\u0217")
        buf.write("\nC\rC\16C\u0218\7C\u021b\nC\fC\16C\u021e\13C\3D\3D\3")
        buf.write("D\7D\u0223\nD\fD\16D\u0226\13D\3D\3D\6D\u022a\nD\rD\16")
        buf.write("D\u022b\7D\u022e\nD\fD\16D\u0231\13D\3E\3E\3E\7E\u0236")
        buf.write("\nE\fE\16E\u0239\13E\3E\3E\6E\u023d\nE\rE\16E\u023e\7")
        buf.write("E\u0241\nE\fE\16E\u0244\13E\3F\3F\3F\3F\5F\u024a\nF\3")
        buf.write("F\3F\3G\3G\3G\3G\5G\u0252\nG\3G\3G\3H\3H\3I\3I\7I\u025a")
        buf.write("\nI\fI\16I\u025d\13I\3J\3J\5J\u0261\nJ\3J\6J\u0264\nJ")
        buf.write("\rJ\16J\u0265\3K\3K\3K\5K\u026b\nK\3K\3K\3K\3K\3K\3K\5")
        buf.write("K\u0273\nK\3K\3K\3L\3L\3L\3L\3L\3L\3L\3L\3L\5L\u0280\n")
        buf.write("L\3M\3M\7M\u0284\nM\fM\16M\u0287\13M\3M\3M\3M\3N\3N\3")
        buf.write("N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\3")
        buf.write("N\5N\u02a1\nN\3O\3O\7O\u02a5\nO\fO\16O\u02a8\13O\3P\3")
        buf.write("P\6P\u02ac\nP\rP\16P\u02ad\3Q\6Q\u02b1\nQ\rQ\16Q\u02b2")
        buf.write("\3Q\3Q\3R\3R\7R\u02b9\nR\fR\16R\u02bc\13R\3R\3R\3S\3S")
        buf.write("\7S\u02c2\nS\fS\16S\u02c5\13S\3S\3S\3S\3T\3T\3T\3T\5T")
        buf.write("\u02ce\nT\3U\3U\3U\3V\3V\3V\3W\3W\3W\3\u00c3\2X\3\2\5")
        buf.write("\3\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33")
        buf.write("\16\35\17\37\20!\21#\22%\23\'\24)\25+\26-\27/\30\61\31")
        buf.write("\63\32\65\33\67\349\35;\36=\37? A!C\"E#G$I%K&M\'O(Q)S")
        buf.write("*U+W,Y-[.]/_\60a\61c\62e\63g\64i\65k\2m\2o\2q\2s\2u\2")
        buf.write("w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\66\u008d\67\u008f\2\u0091\2\u0093\2\u00958\u0097")
        buf.write("9\u0099:\u009b;\u009d<\u009f=\u00a1>\u00a3?\u00a5@\u00a7")
        buf.write("\2\u00a9\2\u00ab\2\u00adA\3\2\20\3\2\63;\3\2\62;\4\2\62")
        buf.write(";CH\3\2\629\3\2\62\63\3\2\639\4\2\63;CH\4\2GGgg\4\2--")
        buf.write("//\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\6\2\n")
        buf.write("\f\16\17$$^^\t\2$$^^ddhhppttvv\2\u02f9\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2\u008b\3\2")
        buf.write("\2\2\2\u008d\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2")
        buf.write("\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00ad\3\2\2\2\3\u00b3\3\2\2\2\5\u00b5\3\2\2\2\7\u00bd")
        buf.write("\3\2\2\2\t\u00cb\3\2\2\2\13\u00d1\3\2\2\2\r\u00da\3\2")
        buf.write("\2\2\17\u00dd\3\2\2\2\21\u00e4\3\2\2\2\23\u00e9\3\2\2")
        buf.write("\2\25\u00f1\3\2\2\2\27\u00f7\3\2\2\2\31\u00fa\3\2\2\2")
        buf.write("\33\u0101\3\2\2\2\35\u0106\3\2\2\2\37\u010b\3\2\2\2!\u0110")
        buf.write("\3\2\2\2#\u0118\3\2\2\2%\u011e\3\2\2\2\'\u0122\3\2\2\2")
        buf.write(")\u0126\3\2\2\2+\u0132\3\2\2\2-\u013d\3\2\2\2/\u0141\3")
        buf.write("\2\2\2\61\u0144\3\2\2\2\63\u0146\3\2\2\2\65\u0148\3\2")
        buf.write("\2\2\67\u014b\3\2\2\29\u014e\3\2\2\2;\u0151\3\2\2\2=\u0154")
        buf.write("\3\2\2\2?\u0156\3\2\2\2A\u0158\3\2\2\2C\u015a\3\2\2\2")
        buf.write("E\u015c\3\2\2\2G\u015e\3\2\2\2I\u0160\3\2\2\2K\u0163\3")
        buf.write("\2\2\2M\u0165\3\2\2\2O\u0168\3\2\2\2Q\u016b\3\2\2\2S\u016f")
        buf.write("\3\2\2\2U\u0171\3\2\2\2W\u0173\3\2\2\2Y\u0175\3\2\2\2")
        buf.write("[\u0177\3\2\2\2]\u0179\3\2\2\2_\u017c\3\2\2\2a\u017e\3")
        buf.write("\2\2\2c\u0180\3\2\2\2e\u0183\3\2\2\2g\u0185\3\2\2\2i\u0187")
        buf.write("\3\2\2\2k\u0189\3\2\2\2m\u018b\3\2\2\2o\u0191\3\2\2\2")
        buf.write("q\u0197\3\2\2\2s\u0199\3\2\2\2u\u019b\3\2\2\2w\u019d\3")
        buf.write("\2\2\2y\u019f\3\2\2\2{\u01b4\3\2\2\2}\u01b6\3\2\2\2\177")
        buf.write("\u01cc\3\2\2\2\u0081\u01e2\3\2\2\2\u0083\u01f8\3\2\2\2")
        buf.write("\u0085\u020c\3\2\2\2\u0087\u021f\3\2\2\2\u0089\u0232\3")
        buf.write("\2\2\2\u008b\u0249\3\2\2\2\u008d\u0251\3\2\2\2\u008f\u0255")
        buf.write("\3\2\2\2\u0091\u0257\3\2\2\2\u0093\u025e\3\2\2\2\u0095")
        buf.write("\u0272\3\2\2\2\u0097\u027f\3\2\2\2\u0099\u0281\3\2\2\2")
        buf.write("\u009b\u02a0\3\2\2\2\u009d\u02a2\3\2\2\2\u009f\u02a9\3")
        buf.write("\2\2\2\u00a1\u02b0\3\2\2\2\u00a3\u02b6\3\2\2\2\u00a5\u02bf")
        buf.write("\3\2\2\2\u00a7\u02cd\3\2\2\2\u00a9\u02cf\3\2\2\2\u00ab")
        buf.write("\u02d2\3\2\2\2\u00ad\u02d5\3\2\2\2\u00af\u00b4\7\62\2")
        buf.write("\2\u00b0\u00b1\t\2\2\2\u00b1\u00b2\t\3\2\2\u00b2\u00b4")
        buf.write("\t\3\2\2\u00b3\u00af\3\2\2\2\u00b3\u00b0\3\2\2\2\u00b4")
        buf.write("\4\3\2\2\2\u00b5\u00b6\5\3\2\2\u00b6\u00b7\5[.\2\u00b7")
        buf.write("\u00b8\5\3\2\2\u00b8\u00b9\5[.\2\u00b9\u00ba\5\3\2\2\u00ba")
        buf.write("\u00bb\5[.\2\u00bb\u00bc\5\3\2\2\u00bc\6\3\2\2\2\u00bd")
        buf.write("\u00be\7%\2\2\u00be\u00bf\7%\2\2\u00bf\u00c3\3\2\2\2\u00c0")
        buf.write("\u00c2\13\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c5\3\2\2")
        buf.write("\2\u00c3\u00c4\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c6")
        buf.write("\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7\7%\2\2\u00c7")
        buf.write("\u00c8\7%\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\b\4\2\2")
        buf.write("\u00ca\b\3\2\2\2\u00cb\u00cc\7D\2\2\u00cc\u00cd\7t\2\2")
        buf.write("\u00cd\u00ce\7g\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0\7m")
        buf.write("\2\2\u00d0\n\3\2\2\2\u00d1\u00d2\7E\2\2\u00d2\u00d3\7")
        buf.write("q\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7v\2\2\u00d5\u00d6")
        buf.write("\7k\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\f\3\2\2\2\u00da\u00db\7K\2\2\u00db\u00dc")
        buf.write("\7h\2\2\u00dc\16\3\2\2\2\u00dd\u00de\7G\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7k\2\2\u00e2\u00e3\7h\2\2\u00e3\20\3\2\2\2\u00e4\u00e5")
        buf.write("\7G\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8")
        buf.write("\7g\2\2\u00e8\22\3\2\2\2\u00e9\u00ea\7H\2\2\u00ea\u00eb")
        buf.write("\7q\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee")
        buf.write("\7c\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0\7j\2\2\u00f0\24")
        buf.write("\3\2\2\2\u00f1\u00f2\7C\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7{\2\2\u00f6\26")
        buf.write("\3\2\2\2\u00f7\u00f8\7K\2\2\u00f8\u00f9\7p\2\2\u00f9\30")
        buf.write("\3\2\2\2\u00fa\u00fb\7T\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd")
        buf.write("\7v\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7p\2\2\u0100\32\3\2\2\2\u0101\u0102\7P\2\2\u0102\u0103")
        buf.write("\7w\2\2\u0103\u0104\7n\2\2\u0104\u0105\7n\2\2\u0105\34")
        buf.write("\3\2\2\2\u0106\u0107\7U\2\2\u0107\u0108\7g\2\2\u0108\u0109")
        buf.write("\7n\2\2\u0109\u010a\7h\2\2\u010a\36\3\2\2\2\u010b\u010c")
        buf.write("\7o\2\2\u010c\u010d\7c\2\2\u010d\u010e\7k\2\2\u010e\u010f")
        buf.write("\7p\2\2\u010f \3\2\2\2\u0110\u0111\7R\2\2\u0111\u0112")
        buf.write("\7t\2\2\u0112\u0113\7q\2\2\u0113\u0114\7i\2\2\u0114\u0115")
        buf.write("\7t\2\2\u0115\u0116\7c\2\2\u0116\u0117\7o\2\2\u0117\"")
        buf.write("\3\2\2\2\u0118\u0119\7E\2\2\u0119\u011a\7n\2\2\u011a\u011b")
        buf.write("\7c\2\2\u011b\u011c\7u\2\2\u011c\u011d\7u\2\2\u011d$\3")
        buf.write("\2\2\2\u011e\u011f\7X\2\2\u011f\u0120\7c\2\2\u0120\u0121")
        buf.write("\7n\2\2\u0121&\3\2\2\2\u0122\u0123\7X\2\2\u0123\u0124")
        buf.write("\7c\2\2\u0124\u0125\7t\2\2\u0125(\3\2\2\2\u0126\u0127")
        buf.write("\7E\2\2\u0127\u0128\7q\2\2\u0128\u0129\7p\2\2\u0129\u012a")
        buf.write("\7u\2\2\u012a\u012b\7v\2\2\u012b\u012c\7t\2\2\u012c\u012d")
        buf.write("\7w\2\2\u012d\u012e\7e\2\2\u012e\u012f\7v\2\2\u012f\u0130")
        buf.write("\7q\2\2\u0130\u0131\7t\2\2\u0131*\3\2\2\2\u0132\u0133")
        buf.write("\7F\2\2\u0133\u0134\7g\2\2\u0134\u0135\7u\2\2\u0135\u0136")
        buf.write("\7v\2\2\u0136\u0137\7t\2\2\u0137\u0138\7w\2\2\u0138\u0139")
        buf.write("\7e\2\2\u0139\u013a\7v\2\2\u013a\u013b\7q\2\2\u013b\u013c")
        buf.write("\7t\2\2\u013c,\3\2\2\2\u013d\u013e\7P\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f\u0140\7y\2\2\u0140.\3\2\2\2\u0141\u0142")
        buf.write("\7D\2\2\u0142\u0143\7{\2\2\u0143\60\3\2\2\2\u0144\u0145")
        buf.write("\7?\2\2\u0145\62\3\2\2\2\u0146\u0147\7#\2\2\u0147\64\3")
        buf.write("\2\2\2\u0148\u0149\7~\2\2\u0149\u014a\7~\2\2\u014a\66")
        buf.write("\3\2\2\2\u014b\u014c\7(\2\2\u014c\u014d\7(\2\2\u014d8")
        buf.write("\3\2\2\2\u014e\u014f\7?\2\2\u014f\u0150\7?\2\2\u0150:")
        buf.write("\3\2\2\2\u0151\u0152\7#\2\2\u0152\u0153\7?\2\2\u0153<")
        buf.write("\3\2\2\2\u0154\u0155\7\'\2\2\u0155>\3\2\2\2\u0156\u0157")
        buf.write("\7-\2\2\u0157@\3\2\2\2\u0158\u0159\7/\2\2\u0159B\3\2\2")
        buf.write("\2\u015a\u015b\7,\2\2\u015bD\3\2\2\2\u015c\u015d\7\61")
        buf.write("\2\2\u015dF\3\2\2\2\u015e\u015f\7>\2\2\u015fH\3\2\2\2")
        buf.write("\u0160\u0161\7>\2\2\u0161\u0162\7?\2\2\u0162J\3\2\2\2")
        buf.write("\u0163\u0164\7@\2\2\u0164L\3\2\2\2\u0165\u0166\7@\2\2")
        buf.write("\u0166\u0167\7?\2\2\u0167N\3\2\2\2\u0168\u0169\7-\2\2")
        buf.write("\u0169\u016a\7\60\2\2\u016aP\3\2\2\2\u016b\u016c\7?\2")
        buf.write("\2\u016c\u016d\7?\2\2\u016d\u016e\7\60\2\2\u016eR\3\2")
        buf.write("\2\2\u016f\u0170\7*\2\2\u0170T\3\2\2\2\u0171\u0172\7+")
        buf.write("\2\2\u0172V\3\2\2\2\u0173\u0174\7]\2\2\u0174X\3\2\2\2")
        buf.write("\u0175\u0176\7_\2\2\u0176Z\3\2\2\2\u0177\u0178\7\60\2")
        buf.write("\2\u0178\\\3\2\2\2\u0179\u017a\7\60\2\2\u017a\u017b\7")
        buf.write("\60\2\2\u017b^\3\2\2\2\u017c\u017d\7.\2\2\u017d`\3\2\2")
        buf.write("\2\u017e\u017f\7<\2\2\u017fb\3\2\2\2\u0180\u0181\7<\2")
        buf.write("\2\u0181\u0182\7<\2\2\u0182d\3\2\2\2\u0183\u0184\7=\2")
        buf.write("\2\u0184f\3\2\2\2\u0185\u0186\7}\2\2\u0186h\3\2\2\2\u0187")
        buf.write("\u0188\7\177\2\2\u0188j\3\2\2\2\u0189\u018a\7$\2\2\u018a")
        buf.write("l\3\2\2\2\u018b\u018c\7\62\2\2\u018cn\3\2\2\2\u018d\u018e")
        buf.write("\7\62\2\2\u018e\u0192\7z\2\2\u018f\u0190\7\62\2\2\u0190")
        buf.write("\u0192\7Z\2\2\u0191\u018d\3\2\2\2\u0191\u018f\3\2\2\2")
        buf.write("\u0192p\3\2\2\2\u0193\u0194\7\62\2\2\u0194\u0198\7d\2")
        buf.write("\2\u0195\u0196\7\62\2\2\u0196\u0198\7D\2\2\u0197\u0193")
        buf.write("\3\2\2\2\u0197\u0195\3\2\2\2\u0198r\3\2\2\2\u0199\u019a")
        buf.write("\t\4\2\2\u019at\3\2\2\2\u019b\u019c\t\5\2\2\u019cv\3\2")
        buf.write("\2\2\u019d\u019e\t\6\2\2\u019ex\3\2\2\2\u019f\u01a0\t")
        buf.write("\3\2\2\u01a0z\3\2\2\2\u01a1\u01b5\5y=\2\u01a2\u01a6\t")
        buf.write("\2\2\2\u01a3\u01a5\5y=\2\u01a4\u01a3\3\2\2\2\u01a5\u01a8")
        buf.write("\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("\u01b1\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01ab\7a\2\2")
        buf.write("\u01aa\u01ac\5y=\2\u01ab\u01aa\3\2\2\2\u01ac\u01ad\3\2")
        buf.write("\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b0")
        buf.write("\3\2\2\2\u01af\u01a9\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1")
        buf.write("\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b5\3\2\2\2")
        buf.write("\u01b3\u01b1\3\2\2\2\u01b4\u01a1\3\2\2\2\u01b4\u01a2\3")
        buf.write("\2\2\2\u01b5|\3\2\2\2\u01b6\u01ca\5m\67\2\u01b7\u01cb")
        buf.write("\7\62\2\2\u01b8\u01bc\t\7\2\2\u01b9\u01bb\5u;\2\u01ba")
        buf.write("\u01b9\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2")
        buf.write("\u01bc\u01bd\3\2\2\2\u01bd\u01c7\3\2\2\2\u01be\u01bc\3")
        buf.write("\2\2\2\u01bf\u01c1\7a\2\2\u01c0\u01c2\5u;\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3")
        buf.write("\u01c4\3\2\2\2\u01c4\u01c6\3\2\2\2\u01c5\u01bf\3\2\2\2")
        buf.write("\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3")
        buf.write("\2\2\2\u01c8\u01cb\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01b7")
        buf.write("\3\2\2\2\u01ca\u01b8\3\2\2\2\u01cb~\3\2\2\2\u01cc\u01e0")
        buf.write("\5o8\2\u01cd\u01e1\7\62\2\2\u01ce\u01d2\t\b\2\2\u01cf")
        buf.write("\u01d1\5s:\2\u01d0\u01cf\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01dd\3\2\2\2")
        buf.write("\u01d4\u01d2\3\2\2\2\u01d5\u01d7\7a\2\2\u01d6\u01d8\5")
        buf.write("s:\2\u01d7\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01d7")
        buf.write("\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2\2\2\u01db")
        buf.write("\u01d5\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01dd\u01de\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd\3")
        buf.write("\2\2\2\u01e0\u01cd\3\2\2\2\u01e0\u01ce\3\2\2\2\u01e1\u0080")
        buf.write("\3\2\2\2\u01e2\u01f6\5q9\2\u01e3\u01f7\7\62\2\2\u01e4")
        buf.write("\u01e8\7\63\2\2\u01e5\u01e7\5w<\2\u01e6\u01e5\3\2\2\2")
        buf.write("\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3")
        buf.write("\2\2\2\u01e9\u01f3\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ed")
        buf.write("\7a\2\2\u01ec\u01ee\5w<\2\u01ed\u01ec\3\2\2\2\u01ee\u01ef")
        buf.write("\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0")
        buf.write("\u01f2\3\2\2\2\u01f1\u01eb\3\2\2\2\u01f2\u01f5\3\2\2\2")
        buf.write("\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f7\3")
        buf.write("\2\2\2\u01f5\u01f3\3\2\2\2\u01f6\u01e3\3\2\2\2\u01f6\u01e4")
        buf.write("\3\2\2\2\u01f7\u0082\3\2\2\2\u01f8\u020a\t\2\2\2\u01f9")
        buf.write("\u01fb\5y=\2\u01fa\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc")
        buf.write("\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u0207\3\2\2\2")
        buf.write("\u01fe\u01fc\3\2\2\2\u01ff\u0201\7a\2\2\u0200\u0202\5")
        buf.write("y=\2\u0201\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0201")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205")
        buf.write("\u01ff\3\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2")
        buf.write("\u0207\u0208\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207\3")
        buf.write("\2\2\2\u020a\u01fc\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u0084")
        buf.write("\3\2\2\2\u020c\u020d\5m\67\2\u020d\u0211\t\7\2\2\u020e")
        buf.write("\u0210\5u;\2\u020f\u020e\3\2\2\2\u0210\u0213\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u021c\3\2\2\2")
        buf.write("\u0213\u0211\3\2\2\2\u0214\u0216\7a\2\2\u0215\u0217\5")
        buf.write("u;\2\u0216\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0216")
        buf.write("\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021b\3\2\2\2\u021a")
        buf.write("\u0214\3\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a\3\2\2\2")
        buf.write("\u021c\u021d\3\2\2\2\u021d\u0086\3\2\2\2\u021e\u021c\3")
        buf.write("\2\2\2\u021f\u0220\5o8\2\u0220\u0224\t\b\2\2\u0221\u0223")
        buf.write("\5s:\2\u0222\u0221\3\2\2\2\u0223\u0226\3\2\2\2\u0224\u0222")
        buf.write("\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u022f\3\2\2\2\u0226")
        buf.write("\u0224\3\2\2\2\u0227\u0229\7a\2\2\u0228\u022a\5s:\2\u0229")
        buf.write("\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u0229\3\2\2\2")
        buf.write("\u022b\u022c\3\2\2\2\u022c\u022e\3\2\2\2\u022d\u0227\3")
        buf.write("\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230")
        buf.write("\3\2\2\2\u0230\u0088\3\2\2\2\u0231\u022f\3\2\2\2\u0232")
        buf.write("\u0233\5q9\2\u0233\u0237\7\63\2\2\u0234\u0236\5w<\2\u0235")
        buf.write("\u0234\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2")
        buf.write("\u0237\u0238\3\2\2\2\u0238\u0242\3\2\2\2\u0239\u0237\3")
        buf.write("\2\2\2\u023a\u023c\7a\2\2\u023b\u023d\5w<\2\u023c\u023b")
        buf.write("\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023c\3\2\2\2\u023e")
        buf.write("\u023f\3\2\2\2\u023f\u0241\3\2\2\2\u0240\u023a\3\2\2\2")
        buf.write("\u0241\u0244\3\2\2\2\u0242\u0240\3\2\2\2\u0242\u0243\3")
        buf.write("\2\2\2\u0243\u008a\3\2\2\2\u0244\u0242\3\2\2\2\u0245\u024a")
        buf.write("\5\u0083B\2\u0246\u024a\5\u0085C\2\u0247\u024a\5\u0087")
        buf.write("D\2\u0248\u024a\5\u0089E\2\u0249\u0245\3\2\2\2\u0249\u0246")
        buf.write("\3\2\2\2\u0249\u0247\3\2\2\2\u0249\u0248\3\2\2\2\u024a")
        buf.write("\u024b\3\2\2\2\u024b\u024c\bF\3\2\u024c\u008c\3\2\2\2")
        buf.write("\u024d\u0252\5{>\2\u024e\u0252\5}?\2\u024f\u0252\5\177")
        buf.write("@\2\u0250\u0252\5\u0081A\2\u0251\u024d\3\2\2\2\u0251\u024e")
        buf.write("\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0250\3\2\2\2\u0252")
        buf.write("\u0253\3\2\2\2\u0253\u0254\bG\4\2\u0254\u008e\3\2\2\2")
        buf.write("\u0255\u0256\5{>\2\u0256\u0090\3\2\2\2\u0257\u025b\5[")
        buf.write(".\2\u0258\u025a\5y=\2\u0259\u0258\3\2\2\2\u025a\u025d")
        buf.write("\3\2\2\2\u025b\u0259\3\2\2\2\u025b\u025c\3\2\2\2\u025c")
        buf.write("\u0092\3\2\2\2\u025d\u025b\3\2\2\2\u025e\u0260\t\t\2\2")
        buf.write("\u025f\u0261\t\n\2\2\u0260\u025f\3\2\2\2\u0260\u0261\3")
        buf.write("\2\2\2\u0261\u0263\3\2\2\2\u0262\u0264\5y=\2\u0263\u0262")
        buf.write("\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0263\3\2\2\2\u0265")
        buf.write("\u0266\3\2\2\2\u0266\u0094\3\2\2\2\u0267\u0268\5\u008f")
        buf.write("H\2\u0268\u026a\5\u0091I\2\u0269\u026b\5\u0093J\2\u026a")
        buf.write("\u0269\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u0273\3\2\2\2")
        buf.write("\u026c\u026d\5\u008fH\2\u026d\u026e\5\u0093J\2\u026e\u0273")
        buf.write("\3\2\2\2\u026f\u0270\5\u0091I\2\u0270\u0271\5\u0093J\2")
        buf.write("\u0271\u0273\3\2\2\2\u0272\u0267\3\2\2\2\u0272\u026c\3")
        buf.write("\2\2\2\u0272\u026f\3\2\2\2\u0273\u0274\3\2\2\2\u0274\u0275")
        buf.write("\bK\5\2\u0275\u0096\3\2\2\2\u0276\u0277\7V\2\2\u0277\u0278")
        buf.write("\7t\2\2\u0278\u0279\7w\2\2\u0279\u0280\7g\2\2\u027a\u027b")
        buf.write("\7H\2\2\u027b\u027c\7c\2\2\u027c\u027d\7n\2\2\u027d\u027e")
        buf.write("\7u\2\2\u027e\u0280\7g\2\2\u027f\u0276\3\2\2\2\u027f\u027a")
        buf.write("\3\2\2\2\u0280\u0098\3\2\2\2\u0281\u0285\5k\66\2\u0282")
        buf.write("\u0284\5\u00a7T\2\u0283\u0282\3\2\2\2\u0284\u0287\3\2")
        buf.write("\2\2\u0285\u0283\3\2\2\2\u0285\u0286\3\2\2\2\u0286\u0288")
        buf.write("\3\2\2\2\u0287\u0285\3\2\2\2\u0288\u0289\5k\66\2\u0289")
        buf.write("\u028a\bM\6\2\u028a\u009a\3\2\2\2\u028b\u028c\7K\2\2\u028c")
        buf.write("\u028d\7p\2\2\u028d\u02a1\7v\2\2\u028e\u028f\7H\2\2\u028f")
        buf.write("\u0290\7n\2\2\u0290\u0291\7q\2\2\u0291\u0292\7c\2\2\u0292")
        buf.write("\u02a1\7v\2\2\u0293\u0294\7D\2\2\u0294\u0295\7q\2\2\u0295")
        buf.write("\u0296\7q\2\2\u0296\u0297\7n\2\2\u0297\u0298\7g\2\2\u0298")
        buf.write("\u0299\7c\2\2\u0299\u02a1\7p\2\2\u029a\u029b\7U\2\2\u029b")
        buf.write("\u029c\7v\2\2\u029c\u029d\7t\2\2\u029d\u029e\7k\2\2\u029e")
        buf.write("\u029f\7p\2\2\u029f\u02a1\7i\2\2\u02a0\u028b\3\2\2\2\u02a0")
        buf.write("\u028e\3\2\2\2\u02a0\u0293\3\2\2\2\u02a0\u029a\3\2\2\2")
        buf.write("\u02a1\u009c\3\2\2\2\u02a2\u02a6\t\13\2\2\u02a3\u02a5")
        buf.write("\t\f\2\2\u02a4\u02a3\3\2\2\2\u02a5\u02a8\3\2\2\2\u02a6")
        buf.write("\u02a4\3\2\2\2\u02a6\u02a7\3\2\2\2\u02a7\u009e\3\2\2\2")
        buf.write("\u02a8\u02a6\3\2\2\2\u02a9\u02ab\7&\2\2\u02aa\u02ac\t")
        buf.write("\f\2\2\u02ab\u02aa\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02ab")
        buf.write("\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae\u00a0\3\2\2\2\u02af")
        buf.write("\u02b1\t\r\2\2\u02b0\u02af\3\2\2\2\u02b1\u02b2\3\2\2\2")
        buf.write("\u02b2\u02b0\3\2\2\2\u02b2\u02b3\3\2\2\2\u02b3\u02b4\3")
        buf.write("\2\2\2\u02b4\u02b5\bQ\2\2\u02b5\u00a2\3\2\2\2\u02b6\u02ba")
        buf.write("\5k\66\2\u02b7\u02b9\5\u00a7T\2\u02b8\u02b7\3\2\2\2\u02b9")
        buf.write("\u02bc\3\2\2\2\u02ba\u02b8\3\2\2\2\u02ba\u02bb\3\2\2\2")
        buf.write("\u02bb\u02bd\3\2\2\2\u02bc\u02ba\3\2\2\2\u02bd\u02be\b")
        buf.write("R\7\2\u02be\u00a4\3\2\2\2\u02bf\u02c3\5k\66\2\u02c0\u02c2")
        buf.write("\5\u00a7T\2\u02c1\u02c0\3\2\2\2\u02c2\u02c5\3\2\2\2\u02c3")
        buf.write("\u02c1\3\2\2\2\u02c3\u02c4\3\2\2\2\u02c4\u02c6\3\2\2\2")
        buf.write("\u02c5\u02c3\3\2\2\2\u02c6\u02c7\5\u00abV\2\u02c7\u02c8")
        buf.write("\bS\b\2\u02c8\u00a6\3\2\2\2\u02c9\u02ce\n\16\2\2\u02ca")
        buf.write("\u02ce\5\u00a9U\2\u02cb\u02cc\7)\2\2\u02cc\u02ce\5k\66")
        buf.write("\2\u02cd\u02c9\3\2\2\2\u02cd\u02ca\3\2\2\2\u02cd\u02cb")
        buf.write("\3\2\2\2\u02ce\u00a8\3\2\2\2\u02cf\u02d0\7^\2\2\u02d0")
        buf.write("\u02d1\t\17\2\2\u02d1\u00aa\3\2\2\2\u02d2\u02d3\7^\2\2")
        buf.write("\u02d3\u02d4\n\17\2\2\u02d4\u00ac\3\2\2\2\u02d5\u02d6")
        buf.write("\13\2\2\2\u02d6\u02d7\bW\t\2\u02d7\u00ae\3\2\2\2\64\2")
        buf.write("\u00b3\u00c3\u0191\u0197\u01a6\u01ad\u01b1\u01b4\u01bc")
        buf.write("\u01c3\u01c7\u01ca\u01d2\u01d9\u01dd\u01e0\u01e8\u01ef")
        buf.write("\u01f3\u01f6\u01fc\u0203\u0207\u020a\u0211\u0218\u021c")
        buf.write("\u0224\u022b\u022f\u0237\u023e\u0242\u0249\u0251\u025b")
        buf.write("\u0260\u0265\u026a\u0272\u027f\u0285\u02a0\u02a6\u02ad")
        buf.write("\u02b2\u02ba\u02c3\u02cd\n\b\2\2\3F\2\3G\3\3K\4\3M\5\3")
        buf.write("R\6\3S\7\3W\b")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IP = 1
    COMMENT = 2
    K_BREAK = 3
    K_CONTINUE = 4
    K_IF = 5
    K_ELSE_IF = 6
    K_ELSE = 7
    K_FOR_EACH = 8
    K_ARRAY = 9
    K_IN = 10
    K_RETURN = 11
    K_NULL = 12
    K_SELF = 13
    K_MAIN = 14
    K_PROGRAM = 15
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
    PRIMITIVE_TYPE = 57
    IDENTIFIER = 58
    DOLAR_IDENTIFIER = 59
    WS = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'Array'", "'In'", "'Return'", "'Null'", "'Self'", "'main'", 
            "'Program'", "'Class'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'='", "'!'", "'||'", "'&&'", "'=='", "'!='", 
            "'%'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", 
            "'+.'", "'==.'", "'('", "')'", "'['", "']'", "'.'", "'..'", 
            "','", "':'", "'::'", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "IP", "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", 
            "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", "K_RETURN", "K_NULL", 
            "K_SELF", "K_MAIN", "K_PROGRAM", "K_CLASS", "K_VAL", "K_VAR", 
            "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", "K_BY", "OP_ASSIGN", 
            "OP_LOGICAL_NOT", "OP_LOGICAL_OR", "OP_LOGICAL_AND", "OP_IS_EQUAL_TO", 
            "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", "OP_SUBTRACTION", 
            "OP_MULTIPLICATION", "OP_DIVISION", "OP_LESS_THAN", "OP_LESS_THAN_EQUAL", 
            "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", "OP_STRING_CONCATENATION", 
            "OP_TWO_SAME_STRING", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", 
            "RIGHT_SQUARE_BRACKET", "DOT", "DOUBLE_DOT", "COMMA", "COLON", 
            "DOUBLE_COLON", "SEMI_COLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
            "INTEGER_LITERAL2", "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", 
            "STRING_LITERAL", "PRIMITIVE_TYPE", "IDENTIFIER", "DOLAR_IDENTIFIER", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "CHILD", "IP", "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", 
                  "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", 
                  "K_RETURN", "K_NULL", "K_SELF", "K_MAIN", "K_PROGRAM", 
                  "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", "K_DESTRUCTOR", 
                  "K_NEW", "K_BY", "OP_ASSIGN", "OP_LOGICAL_NOT", "OP_LOGICAL_OR", 
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
                  "BOOLEAN_LITERAL", "STRING_LITERAL", "PRIMITIVE_TYPE", 
                  "IDENTIFIER", "DOLAR_IDENTIFIER", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "STR_CHAR", "ESC_ACCEPT", "ESC_ILLEGAL", 
                  "ERROR_CHAR" ]

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
            actions[68] = self.INTEGER_LITERAL2_action 
            actions[69] = self.INTEGER_LITERAL_action 
            actions[73] = self.FLOAT_LITERAL_action 
            actions[75] = self.STRING_LITERAL_action 
            actions[80] = self.UNCLOSE_STRING_action 
            actions[81] = self.ILLEGAL_ESCAPE_action 
            actions[85] = self.ERROR_CHAR_action 
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
                                
     


