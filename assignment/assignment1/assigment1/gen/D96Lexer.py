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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u0259\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\7\6\u00c3\n\6\f\6\16\6\u00c6\13\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\5:\u01a3\n:\3;\3;\3<\3<\3<\3<\5<\u01ab\n<\3=\3=\3=\3")
        buf.write("=\5=\u01b1\n=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\5B\u01bd\n")
        buf.write("B\3B\6B\u01c0\nB\rB\16B\u01c1\3C\3C\3C\5C\u01c7\nC\3C")
        buf.write("\6C\u01ca\nC\rC\16C\u01cb\3C\3C\7C\u01d0\nC\fC\16C\u01d3")
        buf.write("\13C\3C\6C\u01d6\nC\rC\16C\u01d7\5C\u01da\nC\3D\3D\6D")
        buf.write("\u01de\nD\rD\16D\u01df\3D\3D\7D\u01e4\nD\fD\16D\u01e7")
        buf.write("\13D\3D\6D\u01ea\nD\rD\16D\u01eb\3E\3E\6E\u01f0\nE\rE")
        buf.write("\16E\u01f1\3E\3E\7E\u01f6\nE\fE\16E\u01f9\13E\3E\6E\u01fc")
        buf.write("\nE\rE\16E\u01fd\3F\3F\6F\u0202\nF\rF\16F\u0203\3F\3F")
        buf.write("\7F\u0208\nF\fF\16F\u020b\13F\3F\6F\u020e\nF\rF\16F\u020f")
        buf.write("\3G\3G\3G\3G\5G\u0216\nG\3G\3G\3H\3H\3H\5H\u021d\nH\3")
        buf.write("H\5H\u0220\nH\3H\3H\3H\3H\3H\5H\u0227\nH\3H\3H\5H\u022b")
        buf.write("\nH\3H\3H\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u0238\nI\3J\3")
        buf.write("J\3J\7J\u023d\nJ\fJ\16J\u0240\13J\3J\3J\3K\5K\u0245\n")
        buf.write("K\3K\7K\u0248\nK\fK\16K\u024b\13K\3L\3L\6L\u024f\nL\r")
        buf.write("L\16L\u0250\3M\6M\u0254\nM\rM\16M\u0255\3M\3M\4\u00c4")
        buf.write("\u023e\2N\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o\2q\2s9u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085")
        buf.write("\2\u0087\2\u0089\2\u008b\2\u008d:\u008f;\u0091<\u0093")
        buf.write("=\u0095>\u0097?\u0099@\3\2\r\5\2\62;CHch\3\2\629\3\2\62")
        buf.write("\63\3\2\62;\4\2GGgg\4\2--//\3\2\63;\4\2$$^^\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u0271\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2s\3\2\2\2\2\u008d\3\2")
        buf.write("\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2")
        buf.write("\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\3\u009b")
        buf.write("\3\2\2\2\5\u00a3\3\2\2\2\7\u00af\3\2\2\2\t\u00b9\3\2\2")
        buf.write("\2\13\u00be\3\2\2\2\r\u00cc\3\2\2\2\17\u00d2\3\2\2\2\21")
        buf.write("\u00db\3\2\2\2\23\u00de\3\2\2\2\25\u00e5\3\2\2\2\27\u00ea")
        buf.write("\3\2\2\2\31\u00f2\3\2\2\2\33\u00f8\3\2\2\2\35\u00fb\3")
        buf.write("\2\2\2\37\u00ff\3\2\2\2!\u0105\3\2\2\2#\u010d\3\2\2\2")
        buf.write("%\u0114\3\2\2\2\'\u011b\3\2\2\2)\u0120\3\2\2\2+\u0126")
        buf.write("\3\2\2\2-\u012a\3\2\2\2/\u012e\3\2\2\2\61\u013a\3\2\2")
        buf.write("\2\63\u0145\3\2\2\2\65\u0149\3\2\2\2\67\u014c\3\2\2\2")
        buf.write("9\u0151\3\2\2\2;\u0153\3\2\2\2=\u0155\3\2\2\2?\u0158\3")
        buf.write("\2\2\2A\u015b\3\2\2\2C\u015e\3\2\2\2E\u0161\3\2\2\2G\u0163")
        buf.write("\3\2\2\2I\u0165\3\2\2\2K\u0167\3\2\2\2M\u0169\3\2\2\2")
        buf.write("O\u016b\3\2\2\2Q\u016d\3\2\2\2S\u0170\3\2\2\2U\u0172\3")
        buf.write("\2\2\2W\u0175\3\2\2\2Y\u0178\3\2\2\2[\u017c\3\2\2\2]\u017e")
        buf.write("\3\2\2\2_\u0180\3\2\2\2a\u0182\3\2\2\2c\u0184\3\2\2\2")
        buf.write("e\u0186\3\2\2\2g\u0188\3\2\2\2i\u018a\3\2\2\2k\u018c\3")
        buf.write("\2\2\2m\u018e\3\2\2\2o\u0190\3\2\2\2q\u0192\3\2\2\2s\u01a2")
        buf.write("\3\2\2\2u\u01a4\3\2\2\2w\u01aa\3\2\2\2y\u01b0\3\2\2\2")
        buf.write("{\u01b2\3\2\2\2}\u01b4\3\2\2\2\177\u01b6\3\2\2\2\u0081")
        buf.write("\u01b8\3\2\2\2\u0083\u01ba\3\2\2\2\u0085\u01d9\3\2\2\2")
        buf.write("\u0087\u01db\3\2\2\2\u0089\u01ed\3\2\2\2\u008b\u01ff\3")
        buf.write("\2\2\2\u008d\u0215\3\2\2\2\u008f\u022a\3\2\2\2\u0091\u0237")
        buf.write("\3\2\2\2\u0093\u0239\3\2\2\2\u0095\u0244\3\2\2\2\u0097")
        buf.write("\u024c\3\2\2\2\u0099\u0253\3\2\2\2\u009b\u009c\7R\2\2")
        buf.write("\u009c\u009d\7t\2\2\u009d\u009e\7q\2\2\u009e\u009f\7i")
        buf.write("\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2")
        buf.write("\7o\2\2\u00a2\4\3\2\2\2\u00a3\u00a4\7o\2\2\u00a4\u00a5")
        buf.write("\7g\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7j\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\u00a9\7f\2\2\u00a9\u00aa\7\"\2\2\u00aa\u00ab")
        buf.write("\7d\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad\7f\2\2\u00ad\u00ae")
        buf.write("\7{\2\2\u00ae\6\3\2\2\2\u00af\u00b0\7u\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7o\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7")
        buf.write("\7p\2\2\u00b7\u00b8\7v\2\2\u00b8\b\3\2\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7z\2\2\u00bb\u00bc\7r\2\2\u00bc\u00bd")
        buf.write("\7t\2\2\u00bd\n\3\2\2\2\u00be\u00bf\7%\2\2\u00bf\u00c0")
        buf.write("\7%\2\2\u00c0\u00c4\3\2\2\2\u00c1\u00c3\13\2\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c5\3\2\2\2")
        buf.write("\u00c4\u00c2\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3")
        buf.write("\2\2\2\u00c7\u00c8\7%\2\2\u00c8\u00c9\7%\2\2\u00c9\u00ca")
        buf.write("\3\2\2\2\u00ca\u00cb\b\6\2\2\u00cb\f\3\2\2\2\u00cc\u00cd")
        buf.write("\7D\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0")
        buf.write("\7c\2\2\u00d0\u00d1\7m\2\2\u00d1\16\3\2\2\2\u00d2\u00d3")
        buf.write("\7E\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6")
        buf.write("\7v\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9")
        buf.write("\7w\2\2\u00d9\u00da\7g\2\2\u00da\20\3\2\2\2\u00db\u00dc")
        buf.write("\7K\2\2\u00dc\u00dd\7h\2\2\u00dd\22\3\2\2\2\u00de\u00df")
        buf.write("\7G\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1\7u\2\2\u00e1\u00e2")
        buf.write("\7g\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4\7h\2\2\u00e4\24")
        buf.write("\3\2\2\2\u00e5\u00e6\7G\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8")
        buf.write("\7u\2\2\u00e8\u00e9\7g\2\2\u00e9\26\3\2\2\2\u00ea\u00eb")
        buf.write("\7H\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0\7e\2\2\u00f0\u00f1")
        buf.write("\7j\2\2\u00f1\30\3\2\2\2\u00f2\u00f3\7C\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7")
        buf.write("\7{\2\2\u00f7\32\3\2\2\2\u00f8\u00f9\7K\2\2\u00f9\u00fa")
        buf.write("\7p\2\2\u00fa\34\3\2\2\2\u00fb\u00fc\7K\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\36\3\2\2\2\u00ff\u0100")
        buf.write("\7H\2\2\u0100\u0101\7n\2\2\u0101\u0102\7q\2\2\u0102\u0103")
        buf.write("\7c\2\2\u0103\u0104\7v\2\2\u0104 \3\2\2\2\u0105\u0106")
        buf.write("\7D\2\2\u0106\u0107\7q\2\2\u0107\u0108\7q\2\2\u0108\u0109")
        buf.write("\7n\2\2\u0109\u010a\7g\2\2\u010a\u010b\7c\2\2\u010b\u010c")
        buf.write("\7p\2\2\u010c\"\3\2\2\2\u010d\u010e\7U\2\2\u010e\u010f")
        buf.write("\7v\2\2\u010f\u0110\7t\2\2\u0110\u0111\7k\2\2\u0111\u0112")
        buf.write("\7p\2\2\u0112\u0113\7i\2\2\u0113$\3\2\2\2\u0114\u0115")
        buf.write("\7T\2\2\u0115\u0116\7g\2\2\u0116\u0117\7v\2\2\u0117\u0118")
        buf.write("\7w\2\2\u0118\u0119\7t\2\2\u0119\u011a\7p\2\2\u011a&\3")
        buf.write("\2\2\2\u011b\u011c\7P\2\2\u011c\u011d\7w\2\2\u011d\u011e")
        buf.write("\7n\2\2\u011e\u011f\7n\2\2\u011f(\3\2\2\2\u0120\u0121")
        buf.write("\7E\2\2\u0121\u0122\7n\2\2\u0122\u0123\7c\2\2\u0123\u0124")
        buf.write("\7u\2\2\u0124\u0125\7u\2\2\u0125*\3\2\2\2\u0126\u0127")
        buf.write("\7X\2\2\u0127\u0128\7c\2\2\u0128\u0129\7n\2\2\u0129,\3")
        buf.write("\2\2\2\u012a\u012b\7X\2\2\u012b\u012c\7c\2\2\u012c\u012d")
        buf.write("\7t\2\2\u012d.\3\2\2\2\u012e\u012f\7E\2\2\u012f\u0130")
        buf.write("\7q\2\2\u0130\u0131\7p\2\2\u0131\u0132\7u\2\2\u0132\u0133")
        buf.write("\7v\2\2\u0133\u0134\7t\2\2\u0134\u0135\7w\2\2\u0135\u0136")
        buf.write("\7e\2\2\u0136\u0137\7v\2\2\u0137\u0138\7q\2\2\u0138\u0139")
        buf.write("\7t\2\2\u0139\60\3\2\2\2\u013a\u013b\7F\2\2\u013b\u013c")
        buf.write("\7g\2\2\u013c\u013d\7u\2\2\u013d\u013e\7v\2\2\u013e\u013f")
        buf.write("\7t\2\2\u013f\u0140\7w\2\2\u0140\u0141\7e\2\2\u0141\u0142")
        buf.write("\7v\2\2\u0142\u0143\7q\2\2\u0143\u0144\7t\2\2\u0144\62")
        buf.write("\3\2\2\2\u0145\u0146\7P\2\2\u0146\u0147\7g\2\2\u0147\u0148")
        buf.write("\7y\2\2\u0148\64\3\2\2\2\u0149\u014a\7D\2\2\u014a\u014b")
        buf.write("\7{\2\2\u014b\66\3\2\2\2\u014c\u014d\7o\2\2\u014d\u014e")
        buf.write("\7c\2\2\u014e\u014f\7k\2\2\u014f\u0150\7p\2\2\u01508\3")
        buf.write("\2\2\2\u0151\u0152\7?\2\2\u0152:\3\2\2\2\u0153\u0154\7")
        buf.write("#\2\2\u0154<\3\2\2\2\u0155\u0156\7~\2\2\u0156\u0157\7")
        buf.write("~\2\2\u0157>\3\2\2\2\u0158\u0159\7(\2\2\u0159\u015a\7")
        buf.write("(\2\2\u015a@\3\2\2\2\u015b\u015c\7?\2\2\u015c\u015d\7")
        buf.write("?\2\2\u015dB\3\2\2\2\u015e\u015f\7#\2\2\u015f\u0160\7")
        buf.write("?\2\2\u0160D\3\2\2\2\u0161\u0162\7\'\2\2\u0162F\3\2\2")
        buf.write("\2\u0163\u0164\7-\2\2\u0164H\3\2\2\2\u0165\u0166\7/\2")
        buf.write("\2\u0166J\3\2\2\2\u0167\u0168\7,\2\2\u0168L\3\2\2\2\u0169")
        buf.write("\u016a\7\61\2\2\u016aN\3\2\2\2\u016b\u016c\7>\2\2\u016c")
        buf.write("P\3\2\2\2\u016d\u016e\7>\2\2\u016e\u016f\7?\2\2\u016f")
        buf.write("R\3\2\2\2\u0170\u0171\7@\2\2\u0171T\3\2\2\2\u0172\u0173")
        buf.write("\7@\2\2\u0173\u0174\7?\2\2\u0174V\3\2\2\2\u0175\u0176")
        buf.write("\7-\2\2\u0176\u0177\7\60\2\2\u0177X\3\2\2\2\u0178\u0179")
        buf.write("\7?\2\2\u0179\u017a\7?\2\2\u017a\u017b\7\60\2\2\u017b")
        buf.write("Z\3\2\2\2\u017c\u017d\7*\2\2\u017d\\\3\2\2\2\u017e\u017f")
        buf.write("\7+\2\2\u017f^\3\2\2\2\u0180\u0181\7]\2\2\u0181`\3\2\2")
        buf.write("\2\u0182\u0183\7_\2\2\u0183b\3\2\2\2\u0184\u0185\7\60")
        buf.write("\2\2\u0185d\3\2\2\2\u0186\u0187\7.\2\2\u0187f\3\2\2\2")
        buf.write("\u0188\u0189\7<\2\2\u0189h\3\2\2\2\u018a\u018b\7=\2\2")
        buf.write("\u018bj\3\2\2\2\u018c\u018d\7}\2\2\u018dl\3\2\2\2\u018e")
        buf.write("\u018f\7\177\2\2\u018fn\3\2\2\2\u0190\u0191\7)\2\2\u0191")
        buf.write("p\3\2\2\2\u0192\u0193\7$\2\2\u0193r\3\2\2\2\u0194\u0195")
        buf.write("\7)\2\2\u0195\u01a3\7$\2\2\u0196\u0197\7^\2\2\u0197\u01a3")
        buf.write("\7d\2\2\u0198\u0199\7^\2\2\u0199\u01a3\7h\2\2\u019a\u019b")
        buf.write("\7^\2\2\u019b\u01a3\7t\2\2\u019c\u019d\7^\2\2\u019d\u01a3")
        buf.write("\7p\2\2\u019e\u019f\7^\2\2\u019f\u01a3\7v\2\2\u01a0\u01a1")
        buf.write("\7^\2\2\u01a1\u01a3\7^\2\2\u01a2\u0194\3\2\2\2\u01a2\u0196")
        buf.write("\3\2\2\2\u01a2\u0198\3\2\2\2\u01a2\u019a\3\2\2\2\u01a2")
        buf.write("\u019c\3\2\2\2\u01a2\u019e\3\2\2\2\u01a2\u01a0\3\2\2\2")
        buf.write("\u01a3t\3\2\2\2\u01a4\u01a5\7\62\2\2\u01a5v\3\2\2\2\u01a6")
        buf.write("\u01a7\7\62\2\2\u01a7\u01ab\7z\2\2\u01a8\u01a9\7\62\2")
        buf.write("\2\u01a9\u01ab\7Z\2\2\u01aa\u01a6\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01abx\3\2\2\2\u01ac\u01ad\7\62\2\2\u01ad\u01b1")
        buf.write("\7d\2\2\u01ae\u01af\7\62\2\2\u01af\u01b1\7D\2\2\u01b0")
        buf.write("\u01ac\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1z\3\2\2\2\u01b2")
        buf.write("\u01b3\t\2\2\2\u01b3|\3\2\2\2\u01b4\u01b5\t\3\2\2\u01b5")
        buf.write("~\3\2\2\2\u01b6\u01b7\t\4\2\2\u01b7\u0080\3\2\2\2\u01b8")
        buf.write("\u01b9\t\5\2\2\u01b9\u0082\3\2\2\2\u01ba\u01bc\t\6\2\2")
        buf.write("\u01bb\u01bd\t\7\2\2\u01bc\u01bb\3\2\2\2\u01bc\u01bd\3")
        buf.write("\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01c0\5\u0085C\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01bf\3\2\2\2")
        buf.write("\u01c1\u01c2\3\2\2\2\u01c2\u0084\3\2\2\2\u01c3\u01da\5")
        buf.write("\u0081A\2\u01c4\u01c6\t\b\2\2\u01c5\u01c7\7a\2\2\u01c6")
        buf.write("\u01c5\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01d1\3\2\2\2")
        buf.write("\u01c8\u01ca\5\u0081A\2\u01c9\u01c8\3\2\2\2\u01ca\u01cb")
        buf.write("\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd\u01ce\7a\2\2\u01ce\u01d0\3\2\2\2")
        buf.write("\u01cf\u01c9\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf\3")
        buf.write("\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1")
        buf.write("\3\2\2\2\u01d4\u01d6\5\u0081A\2\u01d5\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2")
        buf.write("\u01d8\u01da\3\2\2\2\u01d9\u01c3\3\2\2\2\u01d9\u01c4\3")
        buf.write("\2\2\2\u01da\u0086\3\2\2\2\u01db\u01e5\5u;\2\u01dc\u01de")
        buf.write("\5}?\2\u01dd\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01dd")
        buf.write("\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1")
        buf.write("\u01e2\7a\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01dd\3\2\2\2")
        buf.write("\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3")
        buf.write("\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01ea")
        buf.write("\5}?\2\u01e9\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01e9")
        buf.write("\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u0088\3\2\2\2\u01ed")
        buf.write("\u01f7\5w<\2\u01ee\u01f0\5{>\2\u01ef\u01ee\3\2\2\2\u01f0")
        buf.write("\u01f1\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2")
        buf.write("\u01f2\u01f3\3\2\2\2\u01f3\u01f4\7a\2\2\u01f4\u01f6\3")
        buf.write("\2\2\2\u01f5\u01ef\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5")
        buf.write("\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9")
        buf.write("\u01f7\3\2\2\2\u01fa\u01fc\5{>\2\u01fb\u01fa\3\2\2\2\u01fc")
        buf.write("\u01fd\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2")
        buf.write("\u01fe\u008a\3\2\2\2\u01ff\u0209\5y=\2\u0200\u0202\5\177")
        buf.write("@\2\u0201\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0201")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205\3\2\2\2\u0205")
        buf.write("\u0206\7a\2\2\u0206\u0208\3\2\2\2\u0207\u0201\3\2\2\2")
        buf.write("\u0208\u020b\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a\3")
        buf.write("\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209\3\2\2\2\u020c\u020e")
        buf.write("\5\177@\2\u020d\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f")
        buf.write("\u020d\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u008c\3\2\2\2")
        buf.write("\u0211\u0216\5\u0085C\2\u0212\u0216\5\u0087D\2\u0213\u0216")
        buf.write("\5\u0089E\2\u0214\u0216\5\u008bF\2\u0215\u0211\3\2\2\2")
        buf.write("\u0215\u0212\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0214\3")
        buf.write("\2\2\2\u0216\u0217\3\2\2\2\u0217\u0218\bG\3\2\u0218\u008e")
        buf.write("\3\2\2\2\u0219\u021a\5\u0085C\2\u021a\u021c\5c\62\2\u021b")
        buf.write("\u021d\5\u0085C\2\u021c\u021b\3\2\2\2\u021c\u021d\3\2")
        buf.write("\2\2\u021d\u021f\3\2\2\2\u021e\u0220\5\u0083B\2\u021f")
        buf.write("\u021e\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u022b\3\2\2\2")
        buf.write("\u0221\u0222\5\u0085C\2\u0222\u0223\5\u0083B\2\u0223\u022b")
        buf.write("\3\2\2\2\u0224\u0226\5c\62\2\u0225\u0227\5\u0085C\2\u0226")
        buf.write("\u0225\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0228\3\2\2\2")
        buf.write("\u0228\u0229\5\u0083B\2\u0229\u022b\3\2\2\2\u022a\u0219")
        buf.write("\3\2\2\2\u022a\u0221\3\2\2\2\u022a\u0224\3\2\2\2\u022b")
        buf.write("\u022c\3\2\2\2\u022c\u022d\bH\4\2\u022d\u0090\3\2\2\2")
        buf.write("\u022e\u022f\7V\2\2\u022f\u0230\7t\2\2\u0230\u0231\7w")
        buf.write("\2\2\u0231\u0238\7g\2\2\u0232\u0233\7H\2\2\u0233\u0234")
        buf.write("\7c\2\2\u0234\u0235\7n\2\2\u0235\u0236\7u\2\2\u0236\u0238")
        buf.write("\7g\2\2\u0237\u022e\3\2\2\2\u0237\u0232\3\2\2\2\u0238")
        buf.write("\u0092\3\2\2\2\u0239\u023e\5q9\2\u023a\u023d\5s:\2\u023b")
        buf.write("\u023d\n\t\2\2\u023c\u023a\3\2\2\2\u023c\u023b\3\2\2\2")
        buf.write("\u023d\u0240\3\2\2\2\u023e\u023f\3\2\2\2\u023e\u023c\3")
        buf.write("\2\2\2\u023f\u0241\3\2\2\2\u0240\u023e\3\2\2\2\u0241\u0242")
        buf.write("\5q9\2\u0242\u0094\3\2\2\2\u0243\u0245\t\n\2\2\u0244\u0243")
        buf.write("\3\2\2\2\u0245\u0249\3\2\2\2\u0246\u0248\t\13\2\2\u0247")
        buf.write("\u0246\3\2\2\2\u0248\u024b\3\2\2\2\u0249\u0247\3\2\2\2")
        buf.write("\u0249\u024a\3\2\2\2\u024a\u0096\3\2\2\2\u024b\u0249\3")
        buf.write("\2\2\2\u024c\u024e\7&\2\2\u024d\u024f\t\13\2\2\u024e\u024d")
        buf.write("\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u024e\3\2\2\2\u0250")
        buf.write("\u0251\3\2\2\2\u0251\u0098\3\2\2\2\u0252\u0254\t\f\2\2")
        buf.write("\u0253\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0253\3")
        buf.write("\2\2\2\u0255\u0256\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0258")
        buf.write("\bM\2\2\u0258\u009a\3\2\2\2%\2\u00c4\u01a2\u01aa\u01b0")
        buf.write("\u01bc\u01c1\u01c6\u01cb\u01d1\u01d7\u01d9\u01df\u01e5")
        buf.write("\u01eb\u01f1\u01f7\u01fd\u0203\u0209\u020f\u0215\u021c")
        buf.write("\u021f\u0226\u022a\u0237\u023c\u023e\u0244\u0247\u0249")
        buf.write("\u024e\u0250\u0255\5\b\2\2\3G\2\3H\3")
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

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'method body'", "'statement'", "'expr'", "'Break'", 
            "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Array'", 
            "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", 
            "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'main'", "'='", "'!'", "'||'", "'&&'", "'=='", 
            "'!='", "'%'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", "'>'", 
            "'>='", "'+.'", "'==.'", "'('", "')'", "'['", "']'", "'.'", 
            "','", "':'", "';'", "'{'", "'}'" ]

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
            actions[69] = self.INTEGER_LITERAL_action 
            actions[70] = self.FLOAT_LITERAL_action 
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
     


