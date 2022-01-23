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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0260\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\7\3\u00ae\n\3\f\3\16\3\u00b1\13\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\5:\u019b\n:\3;\3;\3<\3<\3<\3<\5<\u01a3")
        buf.write("\n<\3=\3=\3=\3=\5=\u01a9\n=\3>\3>\3?\3?\3@\3@\3A\3A\3")
        buf.write("B\3B\3B\7B\u01b6\nB\fB\16B\u01b9\13B\3B\3B\6B\u01bd\n")
        buf.write("B\rB\16B\u01be\7B\u01c1\nB\fB\16B\u01c4\13B\5B\u01c6\n")
        buf.write("B\3C\3C\3C\3C\7C\u01cc\nC\fC\16C\u01cf\13C\3C\3C\6C\u01d3")
        buf.write("\nC\rC\16C\u01d4\7C\u01d7\nC\fC\16C\u01da\13C\5C\u01dc")
        buf.write("\nC\3D\3D\3D\3D\7D\u01e2\nD\fD\16D\u01e5\13D\3D\3D\6D")
        buf.write("\u01e9\nD\rD\16D\u01ea\7D\u01ed\nD\fD\16D\u01f0\13D\5")
        buf.write("D\u01f2\nD\3E\3E\3E\3E\7E\u01f8\nE\fE\16E\u01fb\13E\3")
        buf.write("E\3E\6E\u01ff\nE\rE\16E\u0200\7E\u0203\nE\fE\16E\u0206")
        buf.write("\13E\5E\u0208\nE\3F\3F\3F\3F\3F\3F\5F\u0210\nF\3G\3G\3")
        buf.write("H\3H\7H\u0216\nH\fH\16H\u0219\13H\3I\3I\5I\u021d\nI\3")
        buf.write("I\6I\u0220\nI\rI\16I\u0221\3J\3J\3J\5J\u0227\nJ\3J\3J")
        buf.write("\3J\3J\3J\3J\5J\u022f\nJ\3J\3J\3K\3K\3K\3K\3K\3K\3K\3")
        buf.write("K\3K\5K\u023c\nK\3L\3L\3L\7L\u0241\nL\fL\16L\u0244\13")
        buf.write("L\3L\3L\3M\5M\u0249\nM\3M\7M\u024c\nM\fM\16M\u024f\13")
        buf.write("M\3N\3N\6N\u0253\nN\rN\16N\u0254\3O\6O\u0258\nO\rO\16")
        buf.write("O\u0259\3O\3O\3P\3P\3P\4\u00af\u0242\2Q\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o\2q\2s9u\2w\2y\2{\2}\2")
        buf.write("\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b:")
        buf.write("\u008d\2\u008f\2\u0091\2\u0093;\u0095<\u0097=\u0099>\u009b")
        buf.write("?\u009d@\u009fA\3\2\17\4\2\62;CH\3\2\629\3\2\62\63\3\2")
        buf.write("\62;\3\2\63;\3\2\639\4\2\63;CH\4\2GGgg\4\2--//\5\2$$)")
        buf.write(")^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u0278")
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
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2s\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\3\u00a1\3\2\2\2\5\u00a9\3\2\2\2\7\u00b7\3\2\2")
        buf.write("\2\t\u00bd\3\2\2\2\13\u00c6\3\2\2\2\r\u00c9\3\2\2\2\17")
        buf.write("\u00d0\3\2\2\2\21\u00d5\3\2\2\2\23\u00dd\3\2\2\2\25\u00e3")
        buf.write("\3\2\2\2\27\u00e6\3\2\2\2\31\u00ea\3\2\2\2\33\u00f0\3")
        buf.write("\2\2\2\35\u00f8\3\2\2\2\37\u00ff\3\2\2\2!\u0106\3\2\2")
        buf.write("\2#\u010b\3\2\2\2%\u0111\3\2\2\2\'\u0115\3\2\2\2)\u0119")
        buf.write("\3\2\2\2+\u0125\3\2\2\2-\u0130\3\2\2\2/\u0134\3\2\2\2")
        buf.write("\61\u0137\3\2\2\2\63\u013c\3\2\2\2\65\u0141\3\2\2\2\67")
        buf.write("\u0143\3\2\2\29\u0145\3\2\2\2;\u0148\3\2\2\2=\u014b\3")
        buf.write("\2\2\2?\u014e\3\2\2\2A\u0151\3\2\2\2C\u0153\3\2\2\2E\u0155")
        buf.write("\3\2\2\2G\u0157\3\2\2\2I\u0159\3\2\2\2K\u015b\3\2\2\2")
        buf.write("M\u015d\3\2\2\2O\u0160\3\2\2\2Q\u0162\3\2\2\2S\u0165\3")
        buf.write("\2\2\2U\u0168\3\2\2\2W\u016c\3\2\2\2Y\u016e\3\2\2\2[\u0170")
        buf.write("\3\2\2\2]\u0172\3\2\2\2_\u0174\3\2\2\2a\u0176\3\2\2\2")
        buf.write("c\u0179\3\2\2\2e\u017b\3\2\2\2g\u017d\3\2\2\2i\u0180\3")
        buf.write("\2\2\2k\u0182\3\2\2\2m\u0184\3\2\2\2o\u0186\3\2\2\2q\u0188")
        buf.write("\3\2\2\2s\u019a\3\2\2\2u\u019c\3\2\2\2w\u01a2\3\2\2\2")
        buf.write("y\u01a8\3\2\2\2{\u01aa\3\2\2\2}\u01ac\3\2\2\2\177\u01ae")
        buf.write("\3\2\2\2\u0081\u01b0\3\2\2\2\u0083\u01c5\3\2\2\2\u0085")
        buf.write("\u01c7\3\2\2\2\u0087\u01dd\3\2\2\2\u0089\u01f3\3\2\2\2")
        buf.write("\u008b\u020f\3\2\2\2\u008d\u0211\3\2\2\2\u008f\u0213\3")
        buf.write("\2\2\2\u0091\u021a\3\2\2\2\u0093\u022e\3\2\2\2\u0095\u023b")
        buf.write("\3\2\2\2\u0097\u023d\3\2\2\2\u0099\u0248\3\2\2\2\u009b")
        buf.write("\u0250\3\2\2\2\u009d\u0257\3\2\2\2\u009f\u025d\3\2\2\2")
        buf.write("\u00a1\u00a2\7R\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4\7q")
        buf.write("\2\2\u00a4\u00a5\7i\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7")
        buf.write("\7c\2\2\u00a7\u00a8\7o\2\2\u00a8\4\3\2\2\2\u00a9\u00aa")
        buf.write("\7%\2\2\u00aa\u00ab\7%\2\2\u00ab\u00af\3\2\2\2\u00ac\u00ae")
        buf.write("\13\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b2\3\2\2\2")
        buf.write("\u00b1\u00af\3\2\2\2\u00b2\u00b3\7%\2\2\u00b3\u00b4\7")
        buf.write("%\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\b\3\2\2\u00b6\6")
        buf.write("\3\2\2\2\u00b7\u00b8\7D\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7m\2\2\u00bc\b")
        buf.write("\3\2\2\2\u00bd\u00be\7E\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0")
        buf.write("\7p\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3")
        buf.write("\7p\2\2\u00c3\u00c4\7w\2\2\u00c4\u00c5\7g\2\2\u00c5\n")
        buf.write("\3\2\2\2\u00c6\u00c7\7K\2\2\u00c7\u00c8\7h\2\2\u00c8\f")
        buf.write("\3\2\2\2\u00c9\u00ca\7G\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc")
        buf.write("\7u\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf")
        buf.write("\7h\2\2\u00cf\16\3\2\2\2\u00d0\u00d1\7G\2\2\u00d1\u00d2")
        buf.write("\7n\2\2\u00d2\u00d3\7u\2\2\u00d3\u00d4\7g\2\2\u00d4\20")
        buf.write("\3\2\2\2\u00d5\u00d6\7H\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8")
        buf.write("\7t\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7c\2\2\u00da\u00db")
        buf.write("\7e\2\2\u00db\u00dc\7j\2\2\u00dc\22\3\2\2\2\u00dd\u00de")
        buf.write("\7C\2\2\u00de\u00df\7t\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1")
        buf.write("\7c\2\2\u00e1\u00e2\7{\2\2\u00e2\24\3\2\2\2\u00e3\u00e4")
        buf.write("\7K\2\2\u00e4\u00e5\7p\2\2\u00e5\26\3\2\2\2\u00e6\u00e7")
        buf.write("\7K\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7v\2\2\u00e9\30")
        buf.write("\3\2\2\2\u00ea\u00eb\7H\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed")
        buf.write("\7q\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7v\2\2\u00ef\32")
        buf.write("\3\2\2\2\u00f0\u00f1\7D\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3")
        buf.write("\7q\2\2\u00f3\u00f4\7n\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6")
        buf.write("\7c\2\2\u00f6\u00f7\7p\2\2\u00f7\34\3\2\2\2\u00f8\u00f9")
        buf.write("\7U\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7k\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7i\2\2\u00fe\36")
        buf.write("\3\2\2\2\u00ff\u0100\7T\2\2\u0100\u0101\7g\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102\u0103\7w\2\2\u0103\u0104\7t\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105 \3\2\2\2\u0106\u0107\7P\2\2\u0107\u0108")
        buf.write("\7w\2\2\u0108\u0109\7n\2\2\u0109\u010a\7n\2\2\u010a\"")
        buf.write("\3\2\2\2\u010b\u010c\7E\2\2\u010c\u010d\7n\2\2\u010d\u010e")
        buf.write("\7c\2\2\u010e\u010f\7u\2\2\u010f\u0110\7u\2\2\u0110$\3")
        buf.write("\2\2\2\u0111\u0112\7X\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7n\2\2\u0114&\3\2\2\2\u0115\u0116\7X\2\2\u0116\u0117")
        buf.write("\7c\2\2\u0117\u0118\7t\2\2\u0118(\3\2\2\2\u0119\u011a")
        buf.write("\7E\2\2\u011a\u011b\7q\2\2\u011b\u011c\7p\2\2\u011c\u011d")
        buf.write("\7u\2\2\u011d\u011e\7v\2\2\u011e\u011f\7t\2\2\u011f\u0120")
        buf.write("\7w\2\2\u0120\u0121\7e\2\2\u0121\u0122\7v\2\2\u0122\u0123")
        buf.write("\7q\2\2\u0123\u0124\7t\2\2\u0124*\3\2\2\2\u0125\u0126")
        buf.write("\7F\2\2\u0126\u0127\7g\2\2\u0127\u0128\7u\2\2\u0128\u0129")
        buf.write("\7v\2\2\u0129\u012a\7t\2\2\u012a\u012b\7w\2\2\u012b\u012c")
        buf.write("\7e\2\2\u012c\u012d\7v\2\2\u012d\u012e\7q\2\2\u012e\u012f")
        buf.write("\7t\2\2\u012f,\3\2\2\2\u0130\u0131\7P\2\2\u0131\u0132")
        buf.write("\7g\2\2\u0132\u0133\7y\2\2\u0133.\3\2\2\2\u0134\u0135")
        buf.write("\7D\2\2\u0135\u0136\7{\2\2\u0136\60\3\2\2\2\u0137\u0138")
        buf.write("\7o\2\2\u0138\u0139\7c\2\2\u0139\u013a\7k\2\2\u013a\u013b")
        buf.write("\7p\2\2\u013b\62\3\2\2\2\u013c\u013d\7u\2\2\u013d\u013e")
        buf.write("\7g\2\2\u013e\u013f\7n\2\2\u013f\u0140\7h\2\2\u0140\64")
        buf.write("\3\2\2\2\u0141\u0142\7?\2\2\u0142\66\3\2\2\2\u0143\u0144")
        buf.write("\7#\2\2\u01448\3\2\2\2\u0145\u0146\7~\2\2\u0146\u0147")
        buf.write("\7~\2\2\u0147:\3\2\2\2\u0148\u0149\7(\2\2\u0149\u014a")
        buf.write("\7(\2\2\u014a<\3\2\2\2\u014b\u014c\7?\2\2\u014c\u014d")
        buf.write("\7?\2\2\u014d>\3\2\2\2\u014e\u014f\7#\2\2\u014f\u0150")
        buf.write("\7?\2\2\u0150@\3\2\2\2\u0151\u0152\7\'\2\2\u0152B\3\2")
        buf.write("\2\2\u0153\u0154\7-\2\2\u0154D\3\2\2\2\u0155\u0156\7/")
        buf.write("\2\2\u0156F\3\2\2\2\u0157\u0158\7,\2\2\u0158H\3\2\2\2")
        buf.write("\u0159\u015a\7\61\2\2\u015aJ\3\2\2\2\u015b\u015c\7>\2")
        buf.write("\2\u015cL\3\2\2\2\u015d\u015e\7>\2\2\u015e\u015f\7?\2")
        buf.write("\2\u015fN\3\2\2\2\u0160\u0161\7@\2\2\u0161P\3\2\2\2\u0162")
        buf.write("\u0163\7@\2\2\u0163\u0164\7?\2\2\u0164R\3\2\2\2\u0165")
        buf.write("\u0166\7-\2\2\u0166\u0167\7\60\2\2\u0167T\3\2\2\2\u0168")
        buf.write("\u0169\7?\2\2\u0169\u016a\7?\2\2\u016a\u016b\7\60\2\2")
        buf.write("\u016bV\3\2\2\2\u016c\u016d\7*\2\2\u016dX\3\2\2\2\u016e")
        buf.write("\u016f\7+\2\2\u016fZ\3\2\2\2\u0170\u0171\7]\2\2\u0171")
        buf.write("\\\3\2\2\2\u0172\u0173\7_\2\2\u0173^\3\2\2\2\u0174\u0175")
        buf.write("\7\60\2\2\u0175`\3\2\2\2\u0176\u0177\7\60\2\2\u0177\u0178")
        buf.write("\7\60\2\2\u0178b\3\2\2\2\u0179\u017a\7.\2\2\u017ad\3\2")
        buf.write("\2\2\u017b\u017c\7<\2\2\u017cf\3\2\2\2\u017d\u017e\7<")
        buf.write("\2\2\u017e\u017f\7<\2\2\u017fh\3\2\2\2\u0180\u0181\7=")
        buf.write("\2\2\u0181j\3\2\2\2\u0182\u0183\7}\2\2\u0183l\3\2\2\2")
        buf.write("\u0184\u0185\7\177\2\2\u0185n\3\2\2\2\u0186\u0187\7)\2")
        buf.write("\2\u0187p\3\2\2\2\u0188\u0189\7$\2\2\u0189r\3\2\2\2\u018a")
        buf.write("\u018b\7)\2\2\u018b\u019b\7$\2\2\u018c\u018d\7^\2\2\u018d")
        buf.write("\u019b\7d\2\2\u018e\u018f\7^\2\2\u018f\u019b\7h\2\2\u0190")
        buf.write("\u0191\7^\2\2\u0191\u019b\7t\2\2\u0192\u0193\7^\2\2\u0193")
        buf.write("\u019b\7p\2\2\u0194\u0195\7^\2\2\u0195\u019b\7v\2\2\u0196")
        buf.write("\u0197\7^\2\2\u0197\u019b\7)\2\2\u0198\u0199\7^\2\2\u0199")
        buf.write("\u019b\7^\2\2\u019a\u018a\3\2\2\2\u019a\u018c\3\2\2\2")
        buf.write("\u019a\u018e\3\2\2\2\u019a\u0190\3\2\2\2\u019a\u0192\3")
        buf.write("\2\2\2\u019a\u0194\3\2\2\2\u019a\u0196\3\2\2\2\u019a\u0198")
        buf.write("\3\2\2\2\u019bt\3\2\2\2\u019c\u019d\7\62\2\2\u019dv\3")
        buf.write("\2\2\2\u019e\u019f\7\62\2\2\u019f\u01a3\7z\2\2\u01a0\u01a1")
        buf.write("\7\62\2\2\u01a1\u01a3\7Z\2\2\u01a2\u019e\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a3x\3\2\2\2\u01a4\u01a5\7\62\2\2\u01a5")
        buf.write("\u01a9\7d\2\2\u01a6\u01a7\7\62\2\2\u01a7\u01a9\7D\2\2")
        buf.write("\u01a8\u01a4\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9z\3\2\2")
        buf.write("\2\u01aa\u01ab\t\2\2\2\u01ab|\3\2\2\2\u01ac\u01ad\t\3")
        buf.write("\2\2\u01ad~\3\2\2\2\u01ae\u01af\t\4\2\2\u01af\u0080\3")
        buf.write("\2\2\2\u01b0\u01b1\t\5\2\2\u01b1\u0082\3\2\2\2\u01b2\u01c6")
        buf.write("\5\u0081A\2\u01b3\u01b7\t\6\2\2\u01b4\u01b6\5\u0081A\2")
        buf.write("\u01b5\u01b4\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3")
        buf.write("\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01c2\3\2\2\2\u01b9\u01b7")
        buf.write("\3\2\2\2\u01ba\u01bc\7a\2\2\u01bb\u01bd\5\u0081A\2\u01bc")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c1\3\2\2\2\u01c0\u01ba\3")
        buf.write("\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3")
        buf.write("\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5")
        buf.write("\u01b2\3\2\2\2\u01c5\u01b3\3\2\2\2\u01c6\u0084\3\2\2\2")
        buf.write("\u01c7\u01db\5u;\2\u01c8\u01dc\7\62\2\2\u01c9\u01cd\t")
        buf.write("\7\2\2\u01ca\u01cc\5}?\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf")
        buf.write("\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce")
        buf.write("\u01d8\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d2\7a\2\2")
        buf.write("\u01d1\u01d3\5}?\2\u01d2\u01d1\3\2\2\2\u01d3\u01d4\3\2")
        buf.write("\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7")
        buf.write("\3\2\2\2\u01d6\u01d0\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8")
        buf.write("\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01dc\3\2\2\2")
        buf.write("\u01da\u01d8\3\2\2\2\u01db\u01c8\3\2\2\2\u01db\u01c9\3")
        buf.write("\2\2\2\u01dc\u0086\3\2\2\2\u01dd\u01f1\5w<\2\u01de\u01f2")
        buf.write("\7\62\2\2\u01df\u01e3\t\b\2\2\u01e0\u01e2\5{>\2\u01e1")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e4\3\2\2\2\u01e4\u01ee\3\2\2\2\u01e5\u01e3\3")
        buf.write("\2\2\2\u01e6\u01e8\7a\2\2\u01e7\u01e9\5{>\2\u01e8\u01e7")
        buf.write("\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea")
        buf.write("\u01eb\3\2\2\2\u01eb\u01ed\3\2\2\2\u01ec\u01e6\3\2\2\2")
        buf.write("\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3")
        buf.write("\2\2\2\u01ef\u01f2\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01de")
        buf.write("\3\2\2\2\u01f1\u01df\3\2\2\2\u01f2\u0088\3\2\2\2\u01f3")
        buf.write("\u0207\5y=\2\u01f4\u0208\7\62\2\2\u01f5\u01f9\7\63\2\2")
        buf.write("\u01f6\u01f8\5\177@\2\u01f7\u01f6\3\2\2\2\u01f8\u01fb")
        buf.write("\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa")
        buf.write("\u0204\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u01fe\7a\2\2")
        buf.write("\u01fd\u01ff\5\177@\2\u01fe\u01fd\3\2\2\2\u01ff\u0200")
        buf.write("\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201")
        buf.write("\u0203\3\2\2\2\u0202\u01fc\3\2\2\2\u0203\u0206\3\2\2\2")
        buf.write("\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0208\3")
        buf.write("\2\2\2\u0206\u0204\3\2\2\2\u0207\u01f4\3\2\2\2\u0207\u01f5")
        buf.write("\3\2\2\2\u0208\u008a\3\2\2\2\u0209\u0210\5\u0083B\2\u020a")
        buf.write("\u0210\5\u0085C\2\u020b\u0210\5\u0087D\2\u020c\u020d\5")
        buf.write("\u0089E\2\u020d\u020e\bF\3\2\u020e\u0210\3\2\2\2\u020f")
        buf.write("\u0209\3\2\2\2\u020f\u020a\3\2\2\2\u020f\u020b\3\2\2\2")
        buf.write("\u020f\u020c\3\2\2\2\u0210\u008c\3\2\2\2\u0211\u0212\5")
        buf.write("\u0083B\2\u0212\u008e\3\2\2\2\u0213\u0217\5_\60\2\u0214")
        buf.write("\u0216\5\u0081A\2\u0215\u0214\3\2\2\2\u0216\u0219\3\2")
        buf.write("\2\2\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0090")
        buf.write("\3\2\2\2\u0219\u0217\3\2\2\2\u021a\u021c\t\t\2\2\u021b")
        buf.write("\u021d\t\n\2\2\u021c\u021b\3\2\2\2\u021c\u021d\3\2\2\2")
        buf.write("\u021d\u021f\3\2\2\2\u021e\u0220\5\u0081A\2\u021f\u021e")
        buf.write("\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u021f\3\2\2\2\u0221")
        buf.write("\u0222\3\2\2\2\u0222\u0092\3\2\2\2\u0223\u0224\5\u008d")
        buf.write("G\2\u0224\u0226\5\u008fH\2\u0225\u0227\5\u0091I\2\u0226")
        buf.write("\u0225\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u022f\3\2\2\2")
        buf.write("\u0228\u0229\5\u008dG\2\u0229\u022a\5\u0091I\2\u022a\u022f")
        buf.write("\3\2\2\2\u022b\u022c\5\u008fH\2\u022c\u022d\5\u0091I\2")
        buf.write("\u022d\u022f\3\2\2\2\u022e\u0223\3\2\2\2\u022e\u0228\3")
        buf.write("\2\2\2\u022e\u022b\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0231")
        buf.write("\bJ\4\2\u0231\u0094\3\2\2\2\u0232\u0233\7V\2\2\u0233\u0234")
        buf.write("\7t\2\2\u0234\u0235\7w\2\2\u0235\u023c\7g\2\2\u0236\u0237")
        buf.write("\7H\2\2\u0237\u0238\7c\2\2\u0238\u0239\7n\2\2\u0239\u023a")
        buf.write("\7u\2\2\u023a\u023c\7g\2\2\u023b\u0232\3\2\2\2\u023b\u0236")
        buf.write("\3\2\2\2\u023c\u0096\3\2\2\2\u023d\u0242\5q9\2\u023e\u0241")
        buf.write("\5s:\2\u023f\u0241\n\13\2\2\u0240\u023e\3\2\2\2\u0240")
        buf.write("\u023f\3\2\2\2\u0241\u0244\3\2\2\2\u0242\u0243\3\2\2\2")
        buf.write("\u0242\u0240\3\2\2\2\u0243\u0245\3\2\2\2\u0244\u0242\3")
        buf.write("\2\2\2\u0245\u0246\5q9\2\u0246\u0098\3\2\2\2\u0247\u0249")
        buf.write("\t\f\2\2\u0248\u0247\3\2\2\2\u0249\u024d\3\2\2\2\u024a")
        buf.write("\u024c\t\r\2\2\u024b\u024a\3\2\2\2\u024c\u024f\3\2\2\2")
        buf.write("\u024d\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u009a\3")
        buf.write("\2\2\2\u024f\u024d\3\2\2\2\u0250\u0252\7&\2\2\u0251\u0253")
        buf.write("\t\r\2\2\u0252\u0251\3\2\2\2\u0253\u0254\3\2\2\2\u0254")
        buf.write("\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u009c\3\2\2\2")
        buf.write("\u0256\u0258\t\16\2\2\u0257\u0256\3\2\2\2\u0258\u0259")
        buf.write("\3\2\2\2\u0259\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a")
        buf.write("\u025b\3\2\2\2\u025b\u025c\bO\2\2\u025c\u009e\3\2\2\2")
        buf.write("\u025d\u025e\13\2\2\2\u025e\u025f\bP\5\2\u025f\u00a0\3")
        buf.write("\2\2\2&\2\u00af\u019a\u01a2\u01a8\u01b7\u01be\u01c2\u01c5")
        buf.write("\u01cd\u01d4\u01d8\u01db\u01e3\u01ea\u01ee\u01f1\u01f9")
        buf.write("\u0200\u0204\u0207\u020f\u0217\u021c\u0221\u0226\u022e")
        buf.write("\u023b\u0240\u0242\u0248\u024b\u024d\u0252\u0254\u0259")
        buf.write("\6\b\2\2\3F\2\3J\3\3P\4")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    COMMENT = 2
    K_BREAK = 3
    K_CONTINUE = 4
    K_IF = 5
    K_ELSE_IF = 6
    K_ELSE = 7
    K_FOR_EACH = 8
    K_ARRAY = 9
    K_IN = 10
    K_INT = 11
    K_FLOAT = 12
    K_BOOLEAN = 13
    K_STRING = 14
    K_RETURN = 15
    K_NULL = 16
    K_CLASS = 17
    K_VAL = 18
    K_VAR = 19
    K_CONSTRUCTOR = 20
    K_DESTRUCTOR = 21
    K_NEW = 22
    K_BY = 23
    K_MAIN = 24
    K_SELF = 25
    OP_ASSIGN = 26
    OP_LOGICAL_NOT = 27
    OP_LOGICAL_OR = 28
    OP_LOGICAL_AND = 29
    OP_IS_EQUAL_TO = 30
    OP_NOT_EQUAL_TO = 31
    OP_MODULO = 32
    OP_ADDTION = 33
    OP_SUBTRACTION = 34
    OP_MULTIPLICATION = 35
    OP_DIVISION = 36
    OP_LESS_THAN = 37
    OP_LESS_THAN_EQUAL = 38
    OP_GREATER_THAN = 39
    OP_GREATER_THAN_EQUAL = 40
    OP_STRING_CONCATENATION = 41
    OP_TWO_SAME_STRING = 42
    LEFT_PAREN = 43
    RIGHT_PAREN = 44
    LEFT_SQUARE_BRACKET = 45
    RIGHT_SQUARE_BRACKET = 46
    DOT = 47
    DOUBLE_DOT = 48
    COMMA = 49
    COLON = 50
    DOUBLE_COLON = 51
    SEMI_COLON = 52
    LEFT_CURLY_BRACKET = 53
    RIGHT_CURLY_BRACKET = 54
    ESCAPE = 55
    INTEGER_LITERAL = 56
    FLOAT_LITERAL = 57
    BOOLEAN_LITERAL = 58
    STRING_LITERAL = 59
    IDENTIFIER = 60
    DOLAR_IDENTIFIER = 61
    WHITE_SPACE = 62
    ERROR_TOKEN = 63

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

    ruleNames = [ "T__0", "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", 
                  "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", 
                  "K_BOOLEAN", "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", 
                  "K_VAL", "K_VAR", "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", 
                  "K_BY", "K_MAIN", "K_SELF", "OP_ASSIGN", "OP_LOGICAL_NOT", 
                  "OP_LOGICAL_OR", "OP_LOGICAL_AND", "OP_IS_EQUAL_TO", "OP_NOT_EQUAL_TO", 
                  "OP_MODULO", "OP_ADDTION", "OP_SUBTRACTION", "OP_MULTIPLICATION", 
                  "OP_DIVISION", "OP_LESS_THAN", "OP_LESS_THAN_EQUAL", "OP_GREATER_THAN", 
                  "OP_GREATER_THAN_EQUAL", "OP_STRING_CONCATENATION", "OP_TWO_SAME_STRING", 
                  "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                  "DOT", "DOUBLE_DOT", "COMMA", "COLON", "DOUBLE_COLON", 
                  "SEMI_COLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                  "SINGLE_QUOTE", "DOUBLE_QUOTE", "ESCAPE", "OCTAL_NOTATION", 
                  "HEXA_NOTATION", "BINARY_NOTATION", "HEXA_DIGIT", "OCTAL_DIGIT", 
                  "BINARY_DIGIT", "DECIMAL_DIGIT", "DECIMAL", "OCTAL", "HEXA", 
                  "BINARY", "INTEGER_LITERAL", "INTEGER_PART", "DECIMAL_PART", 
                  "EXPONENT", "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                  "IDENTIFIER", "DOLAR_IDENTIFIER", "WHITE_SPACE", "ERROR_TOKEN" ]

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
            actions[68] = self.INTEGER_LITERAL_action 
            actions[72] = self.FLOAT_LITERAL_action 
            actions[78] = self.ERROR_TOKEN_action 
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
     


