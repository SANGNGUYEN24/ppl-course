# Generated from c:\Users\ADMIN\Desktop\Study\193\Principles of Programming Language\Assignment2\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u01b9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3a\n\3\3\4\3\4\3\4\3\4\5\4g\n\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6r\n\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7y\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u0086\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u008e")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u0098\n")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\5\f\u009f\n\f\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00a5\n\r\3\16\3\16\3\16\3\16\5\16\u00ab\n\16\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00b7")
        buf.write("\n\20\f\20\16\20\u00ba\13\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00c7\n\20\f\20\16")
        buf.write("\20\u00ca\13\20\3\20\3\20\3\20\5\20\u00cf\n\20\3\21\3")
        buf.write("\21\3\21\3\21\5\21\u00d5\n\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00dc\n\22\3\23\3\23\3\23\5\23\u00e1\n\23\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\5\25\u00ea\n\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\7\26\u00f2\n\26\f\26\16\26\u00f5")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00fd\n\27\f")
        buf.write("\27\16\27\u0100\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7")
        buf.write("\30\u0108\n\30\f\30\16\30\u010b\13\30\3\31\3\31\3\31\5")
        buf.write("\31\u0110\n\31\3\32\3\32\3\32\5\32\u0115\n\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\6\33\u011f\n\33\r\33\16")
        buf.write("\33\u0120\7\33\u0123\n\33\f\33\16\33\u0126\13\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u012f\n\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\5\36\u013a\n\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\5\37\u0141\n\37\3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \5 \u014d\n \3!\3!\3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u015d\n\"\f\"\16\"\u0160")
        buf.write("\13\"\3\"\3\"\5\"\u0164\n\"\3\"\3\"\3\"\3#\7#\u016a\n")
        buf.write("#\f#\16#\u016d\13#\3$\7$\u0170\n$\f$\16$\u0173\13$\3%")
        buf.write("\7%\u0176\n%\f%\16%\u0179\13%\3&\3&\3&\3&\3&\3&\3&\3&")
        buf.write("\3&\3&\3&\3&\7&\u0187\n&\f&\16&\u018a\13&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\7\'\u0193\n\'\f\'\16\'\u0196\13\'\3\'\3\'")
        buf.write("\3\'\3(\3(\7(\u019d\n(\f(\16(\u01a0\13(\3(\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\5,\u01b5\n")
        buf.write(",\3,\3,\3,\2\6*,.\64-\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV\2\7\3\2\'")
        buf.write("\61\3\2%&\3\2\33\36\3\2\37#\3\2\35\36\2\u01c2\2X\3\2\2")
        buf.write("\2\4`\3\2\2\2\6f\3\2\2\2\bh\3\2\2\2\nq\3\2\2\2\fx\3\2")
        buf.write("\2\2\16\u0085\3\2\2\2\20\u008d\3\2\2\2\22\u008f\3\2\2")
        buf.write("\2\24\u0097\3\2\2\2\26\u009e\3\2\2\2\30\u00a4\3\2\2\2")
        buf.write("\32\u00aa\3\2\2\2\34\u00ac\3\2\2\2\36\u00ce\3\2\2\2 \u00d4")
        buf.write("\3\2\2\2\"\u00db\3\2\2\2$\u00e0\3\2\2\2&\u00e2\3\2\2\2")
        buf.write("(\u00e9\3\2\2\2*\u00eb\3\2\2\2,\u00f6\3\2\2\2.\u0101\3")
        buf.write("\2\2\2\60\u010f\3\2\2\2\62\u0114\3\2\2\2\64\u0116\3\2")
        buf.write("\2\2\66\u012e\3\2\2\28\u0130\3\2\2\2:\u0139\3\2\2\2<\u0140")
        buf.write("\3\2\2\2>\u014c\3\2\2\2@\u014e\3\2\2\2B\u0153\3\2\2\2")
        buf.write("D\u016b\3\2\2\2F\u0171\3\2\2\2H\u0177\3\2\2\2J\u017a\3")
        buf.write("\2\2\2L\u018e\3\2\2\2N\u019a\3\2\2\2P\u01a6\3\2\2\2R\u01a9")
        buf.write("\3\2\2\2T\u01ac\3\2\2\2V\u01b2\3\2\2\2XY\5\4\3\2YZ\5\6")
        buf.write("\4\2Z[\7\2\2\3[\3\3\2\2\2\\]\5\b\5\2]^\5\4\3\2^a\3\2\2")
        buf.write("\2_a\3\2\2\2`\\\3\2\2\2`_\3\2\2\2a\5\3\2\2\2bc\5\36\20")
        buf.write("\2cd\5\6\4\2dg\3\2\2\2eg\3\2\2\2fb\3\2\2\2fe\3\2\2\2g")
        buf.write("\7\3\2\2\2hi\7\3\2\2ij\7\66\2\2jk\5\n\6\2kl\79\2\2l\t")
        buf.write("\3\2\2\2mn\5\16\b\2no\5\f\7\2or\3\2\2\2pr\5\16\b\2qm\3")
        buf.write("\2\2\2qp\3\2\2\2r\13\3\2\2\2st\78\2\2tu\5\16\b\2uv\5\f")
        buf.write("\7\2vy\3\2\2\2wy\3\2\2\2xs\3\2\2\2xw\3\2\2\2y\r\3\2\2")
        buf.write("\2z\u0086\7<\2\2{|\7<\2\2|}\7\32\2\2}\u0086\5\20\t\2~")
        buf.write("\177\7<\2\2\177\u0086\5\30\r\2\u0080\u0081\7<\2\2\u0081")
        buf.write("\u0082\5\30\r\2\u0082\u0083\7\32\2\2\u0083\u0084\5\20")
        buf.write("\t\2\u0084\u0086\3\2\2\2\u0085z\3\2\2\2\u0085{\3\2\2\2")
        buf.write("\u0085~\3\2\2\2\u0085\u0080\3\2\2\2\u0086\17\3\2\2\2\u0087")
        buf.write("\u008e\7=\2\2\u0088\u008e\7>\2\2\u0089\u008e\7\27\2\2")
        buf.write("\u008a\u008e\7\22\2\2\u008b\u008e\7?\2\2\u008c\u008e\5")
        buf.write("\22\n\2\u008d\u0087\3\2\2\2\u008d\u0088\3\2\2\2\u008d")
        buf.write("\u0089\3\2\2\2\u008d\u008a\3\2\2\2\u008d\u008b\3\2\2\2")
        buf.write("\u008d\u008c\3\2\2\2\u008e\21\3\2\2\2\u008f\u0090\7:\2")
        buf.write("\2\u0090\u0091\5\24\13\2\u0091\u0092\7;\2\2\u0092\23\3")
        buf.write("\2\2\2\u0093\u0094\5\20\t\2\u0094\u0095\5\26\f\2\u0095")
        buf.write("\u0098\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0093\3\2\2\2")
        buf.write("\u0097\u0096\3\2\2\2\u0098\25\3\2\2\2\u0099\u009a\78\2")
        buf.write("\2\u009a\u009b\5\20\t\2\u009b\u009c\5\26\f\2\u009c\u009f")
        buf.write("\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u0099\3\2\2\2\u009e")
        buf.write("\u009d\3\2\2\2\u009f\27\3\2\2\2\u00a0\u00a1\5\34\17\2")
        buf.write("\u00a1\u00a2\5\32\16\2\u00a2\u00a5\3\2\2\2\u00a3\u00a5")
        buf.write("\5\34\17\2\u00a4\u00a0\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5")
        buf.write("\31\3\2\2\2\u00a6\u00a7\5\34\17\2\u00a7\u00a8\5\32\16")
        buf.write("\2\u00a8\u00ab\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a6")
        buf.write("\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\33\3\2\2\2\u00ac\u00ad")
        buf.write("\7\64\2\2\u00ad\u00ae\7=\2\2\u00ae\u00af\7\65\2\2\u00af")
        buf.write("\35\3\2\2\2\u00b0\u00b1\7\25\2\2\u00b1\u00b2\7\66\2\2")
        buf.write("\u00b2\u00b3\7<\2\2\u00b3\u00b4\7\4\2\2\u00b4\u00b8\7")
        buf.write("\66\2\2\u00b5\u00b7\5> \2\u00b6\u00b5\3\2\2\2\u00b7\u00ba")
        buf.write("\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9")
        buf.write("\u00bb\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bc\7\17\2")
        buf.write("\2\u00bc\u00cf\7\67\2\2\u00bd\u00be\7\25\2\2\u00be\u00bf")
        buf.write("\7\66\2\2\u00bf\u00c0\7<\2\2\u00c0\u00c1\7\f\2\2\u00c1")
        buf.write("\u00c2\7\66\2\2\u00c2\u00c3\5 \21\2\u00c3\u00c4\7\4\2")
        buf.write("\2\u00c4\u00c8\7\66\2\2\u00c5\u00c7\5> \2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8")
        buf.write("\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00c8\3\2\2\2")
        buf.write("\u00cb\u00cc\7\17\2\2\u00cc\u00cd\7\67\2\2\u00cd\u00cf")
        buf.write("\3\2\2\2\u00ce\u00b0\3\2\2\2\u00ce\u00bd\3\2\2\2\u00cf")
        buf.write("\37\3\2\2\2\u00d0\u00d1\5$\23\2\u00d1\u00d2\5\"\22\2\u00d2")
        buf.write("\u00d5\3\2\2\2\u00d3\u00d5\5$\23\2\u00d4\u00d0\3\2\2\2")
        buf.write("\u00d4\u00d3\3\2\2\2\u00d5!\3\2\2\2\u00d6\u00d7\78\2\2")
        buf.write("\u00d7\u00d8\5$\23\2\u00d8\u00d9\5\"\22\2\u00d9\u00dc")
        buf.write("\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00d6\3\2\2\2\u00db")
        buf.write("\u00da\3\2\2\2\u00dc#\3\2\2\2\u00dd\u00e1\7<\2\2\u00de")
        buf.write("\u00df\7<\2\2\u00df\u00e1\5\30\r\2\u00e0\u00dd\3\2\2\2")
        buf.write("\u00e0\u00de\3\2\2\2\u00e1%\3\2\2\2\u00e2\u00e3\t\2\2")
        buf.write("\2\u00e3\'\3\2\2\2\u00e4\u00e5\5*\26\2\u00e5\u00e6\5&")
        buf.write("\24\2\u00e6\u00e7\5*\26\2\u00e7\u00ea\3\2\2\2\u00e8\u00ea")
        buf.write("\5*\26\2\u00e9\u00e4\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea")
        buf.write(")\3\2\2\2\u00eb\u00ec\b\26\1\2\u00ec\u00ed\5,\27\2\u00ed")
        buf.write("\u00f3\3\2\2\2\u00ee\u00ef\f\4\2\2\u00ef\u00f0\t\3\2\2")
        buf.write("\u00f0\u00f2\5,\27\2\u00f1\u00ee\3\2\2\2\u00f2\u00f5\3")
        buf.write("\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4+")
        buf.write("\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7\b\27\1\2\u00f7")
        buf.write("\u00f8\5.\30\2\u00f8\u00fe\3\2\2\2\u00f9\u00fa\f\4\2\2")
        buf.write("\u00fa\u00fb\t\4\2\2\u00fb\u00fd\5.\30\2\u00fc\u00f9\3")
        buf.write("\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff-\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102")
        buf.write("\b\30\1\2\u0102\u0103\5\60\31\2\u0103\u0109\3\2\2\2\u0104")
        buf.write("\u0105\f\4\2\2\u0105\u0106\t\5\2\2\u0106\u0108\5\60\31")
        buf.write("\2\u0107\u0104\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107")
        buf.write("\3\2\2\2\u0109\u010a\3\2\2\2\u010a/\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010c\u010d\7$\2\2\u010d\u0110\5\60\31\2\u010e")
        buf.write("\u0110\5\62\32\2\u010f\u010c\3\2\2\2\u010f\u010e\3\2\2")
        buf.write("\2\u0110\61\3\2\2\2\u0111\u0112\t\6\2\2\u0112\u0115\5")
        buf.write("\62\32\2\u0113\u0115\5\64\33\2\u0114\u0111\3\2\2\2\u0114")
        buf.write("\u0113\3\2\2\2\u0115\63\3\2\2\2\u0116\u0117\b\33\1\2\u0117")
        buf.write("\u0118\5\66\34\2\u0118\u0124\3\2\2\2\u0119\u011e\f\4\2")
        buf.write("\2\u011a\u011b\7\64\2\2\u011b\u011c\5(\25\2\u011c\u011d")
        buf.write("\7\65\2\2\u011d\u011f\3\2\2\2\u011e\u011a\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2")
        buf.write("\u0121\u0123\3\2\2\2\u0122\u0119\3\2\2\2\u0123\u0126\3")
        buf.write("\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\65")
        buf.write("\3\2\2\2\u0126\u0124\3\2\2\2\u0127\u012f\5\20\t\2\u0128")
        buf.write("\u012f\7<\2\2\u0129\u012a\7\62\2\2\u012a\u012b\5(\25\2")
        buf.write("\u012b\u012c\7\63\2\2\u012c\u012f\3\2\2\2\u012d\u012f")
        buf.write("\58\35\2\u012e\u0127\3\2\2\2\u012e\u0128\3\2\2\2\u012e")
        buf.write("\u0129\3\2\2\2\u012e\u012d\3\2\2\2\u012f\67\3\2\2\2\u0130")
        buf.write("\u0131\7<\2\2\u0131\u0132\7\62\2\2\u0132\u0133\5:\36\2")
        buf.write("\u0133\u0134\7\63\2\2\u01349\3\2\2\2\u0135\u0136\5(\25")
        buf.write("\2\u0136\u0137\5<\37\2\u0137\u013a\3\2\2\2\u0138\u013a")
        buf.write("\3\2\2\2\u0139\u0135\3\2\2\2\u0139\u0138\3\2\2\2\u013a")
        buf.write(";\3\2\2\2\u013b\u013c\78\2\2\u013c\u013d\5(\25\2\u013d")
        buf.write("\u013e\5<\37\2\u013e\u0141\3\2\2\2\u013f\u0141\3\2\2\2")
        buf.write("\u0140\u013b\3\2\2\2\u0140\u013f\3\2\2\2\u0141=\3\2\2")
        buf.write("\2\u0142\u014d\5\b\5\2\u0143\u014d\5@!\2\u0144\u014d\5")
        buf.write("B\"\2\u0145\u014d\5J&\2\u0146\u014d\5L\'\2\u0147\u014d")
        buf.write("\5N(\2\u0148\u014d\5P)\2\u0149\u014d\5R*\2\u014a\u014d")
        buf.write("\5T+\2\u014b\u014d\5V,\2\u014c\u0142\3\2\2\2\u014c\u0143")
        buf.write("\3\2\2\2\u014c\u0144\3\2\2\2\u014c\u0145\3\2\2\2\u014c")
        buf.write("\u0146\3\2\2\2\u014c\u0147\3\2\2\2\u014c\u0148\3\2\2\2")
        buf.write("\u014c\u0149\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014b\3")
        buf.write("\2\2\2\u014d?\3\2\2\2\u014e\u014f\5(\25\2\u014f\u0150")
        buf.write("\7\32\2\2\u0150\u0151\5(\25\2\u0151\u0152\79\2\2\u0152")
        buf.write("A\3\2\2\2\u0153\u0154\7\7\2\2\u0154\u0155\5(\25\2\u0155")
        buf.write("\u0156\7\26\2\2\u0156\u015e\5D#\2\u0157\u0158\7\n\2\2")
        buf.write("\u0158\u0159\5(\25\2\u0159\u015a\7\26\2\2\u015a\u015b")
        buf.write("\5F$\2\u015b\u015d\3\2\2\2\u015c\u0157\3\2\2\2\u015d\u0160")
        buf.write("\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u0163\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162\7\5\2\2")
        buf.write("\u0162\u0164\5H%\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2")
        buf.write("\2\2\u0164\u0165\3\2\2\2\u0165\u0166\7\24\2\2\u0166\u0167")
        buf.write("\7\67\2\2\u0167C\3\2\2\2\u0168\u016a\5> \2\u0169\u0168")
        buf.write("\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016cE\3\2\2\2\u016d\u016b\3\2\2\2\u016e")
        buf.write("\u0170\5> \2\u016f\u016e\3\2\2\2\u0170\u0173\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172G\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0174\u0176\5> \2\u0175\u0174\3\2\2\2\u0176")
        buf.write("\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178I\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017b\7\20\2")
        buf.write("\2\u017b\u017c\7\62\2\2\u017c\u017d\7<\2\2\u017d\u017e")
        buf.write("\7\32\2\2\u017e\u017f\5(\25\2\u017f\u0180\78\2\2\u0180")
        buf.write("\u0181\5(\25\2\u0181\u0182\78\2\2\u0182\u0183\5(\25\2")
        buf.write("\u0183\u0184\7\63\2\2\u0184\u0188\7\23\2\2\u0185\u0187")
        buf.write("\5> \2\u0186\u0185\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018b\3\2\2\2\u018a")
        buf.write("\u0188\3\2\2\2\u018b\u018c\7\6\2\2\u018c\u018d\7\67\2")
        buf.write("\2\u018dK\3\2\2\2\u018e\u018f\7\r\2\2\u018f\u0190\5(\25")
        buf.write("\2\u0190\u0194\7\23\2\2\u0191\u0193\5> \2\u0192\u0191")
        buf.write("\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0197\3\2\2\2\u0196\u0194\3\2\2\2")
        buf.write("\u0197\u0198\7\13\2\2\u0198\u0199\7\67\2\2\u0199M\3\2")
        buf.write("\2\2\u019a\u019e\7\23\2\2\u019b\u019d\5> \2\u019c\u019b")
        buf.write("\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2\2")
        buf.write("\u01a1\u01a2\7\r\2\2\u01a2\u01a3\5(\25\2\u01a3\u01a4\7")
        buf.write("\b\2\2\u01a4\u01a5\7\67\2\2\u01a5O\3\2\2\2\u01a6\u01a7")
        buf.write("\7\t\2\2\u01a7\u01a8\79\2\2\u01a8Q\3\2\2\2\u01a9\u01aa")
        buf.write("\7\16\2\2\u01aa\u01ab\79\2\2\u01abS\3\2\2\2\u01ac\u01ad")
        buf.write("\7<\2\2\u01ad\u01ae\7\62\2\2\u01ae\u01af\5:\36\2\u01af")
        buf.write("\u01b0\7\63\2\2\u01b0\u01b1\79\2\2\u01b1U\3\2\2\2\u01b2")
        buf.write("\u01b4\7\21\2\2\u01b3\u01b5\5(\25\2\u01b4\u01b3\3\2\2")
        buf.write("\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7")
        buf.write("\79\2\2\u01b7W\3\2\2\2\'`fqx\u0085\u008d\u0097\u009e\u00a4")
        buf.write("\u00aa\u00b8\u00c8\u00ce\u00d4\u00db\u00e0\u00e9\u00f3")
        buf.write("\u00fe\u0109\u010f\u0114\u0120\u0124\u012e\u0139\u0140")
        buf.write("\u014c\u015e\u0163\u016b\u0171\u0177\u0188\u0194\u019e")
        buf.write("\u01b4")
        return buf.getvalue()


class BKITParser(Parser):
    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'Var'", "'Body'", "'Else'", "'EndFor'",
                    "'If'", "'EndDo'", "'Break'", "'ElseIf'", "'EndWhile'",
                    "'Parameter'", "'While'", "'Continue'", "'EndBody'",
                    "'For'", "'Return'", "'True'", "'Do'", "'EndIf'", "'Function'",
                    "'Then'", "'False'", "<INVALID>", "<INVALID>", "'='",
                    "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'",
                    "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='",
                    "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'",
                    "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", "':'",
                    "'.'", "','", "';'", "'{'", "'}'"]

    symbolicNames = ["<INVALID>", "VAR", "BODY", "ELSE", "ENDFOR", "IF",
                     "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER",
                     "WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", "TRUE",
                     "DO", "ENDIF", "FUNCTION", "THEN", "FALSE", "WS",
                     "COMMENT", "ASSIGN", "ADD", "ADDFLOAT", "SUB", "SUBFLOAT",
                     "MUL", "MULFLOAT", "DIV", "DIVFLOAT", "MOD", "NOT",
                     "AND", "OR", "EQUAL", "NOTEQUAL", "LESS", "GREATER",
                     "LESSEQUAL", "GREATEREQUAL", "EQUALFLOAT", "LESSFLOAT",
                     "GREATERFLOAT", "LESSEQUALFLOAT", "GREATEREQUALFLOAT",
                     "LP", "RP", "LA", "RA", "COLON", "DOT", "COMMA", "SEMI",
                     "LB", "RB", "ID", "INTLIT", "FLOATLIT", "STRINGLIT",
                     "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT",
                     "ERROR_CHAR"]

    RULE_program = 0
    RULE_globdeclpart = 1
    RULE_funcdeclspart = 2
    RULE_vardecls = 3
    RULE_varlist = 4
    RULE_tailvar = 5
    RULE_variableinit = 6
    RULE_literals = 7
    RULE_arraydecls = 8
    RULE_arraylit = 9
    RULE_arraylit_ = 10
    RULE_dimlist = 11
    RULE_taildim = 12
    RULE_dim = 13
    RULE_funcdecls = 14
    RULE_parameterlist = 15
    RULE_parameterlist_ = 16
    RULE_parameter = 17
    RULE_relop = 18
    RULE_expr = 19
    RULE_expr1 = 20
    RULE_expr2 = 21
    RULE_expr3 = 22
    RULE_expr4 = 23
    RULE_expr5 = 24
    RULE_expr6 = 25
    RULE_expr7 = 26
    RULE_functioncall = 27
    RULE_argumentslist = 28
    RULE_argumentslist_ = 29
    RULE_statement = 30
    RULE_assignmentstmt = 31
    RULE_ifstmt = 32
    RULE_if_statement = 33
    RULE_elif_statement = 34
    RULE_else_statement = 35
    RULE_forstmt = 36
    RULE_whilestmt = 37
    RULE_dowhilestmt = 38
    RULE_breakstmt = 39
    RULE_continuestmt = 40
    RULE_callstmt = 41
    RULE_returnstmt = 42

    ruleNames = ["program", "globdeclpart", "funcdeclspart", "vardecls",
                 "varlist", "tailvar", "variableinit", "literals", "arraydecls",
                 "arraylit", "arraylit_", "dimlist", "taildim", "dim",
                 "funcdecls", "parameterlist", "parameterlist_", "parameter",
                 "relop", "expr", "expr1", "expr2", "expr3", "expr4",
                 "expr5", "expr6", "expr7", "functioncall", "argumentslist",
                 "argumentslist_", "statement", "assignmentstmt", "ifstmt",
                 "if_statement", "elif_statement", "else_statement", "forstmt",
                 "whilestmt", "dowhilestmt", "breakstmt", "continuestmt",
                 "callstmt", "returnstmt"]

    EOF = Token.EOF
    VAR = 1
    BODY = 2
    ELSE = 3
    ENDFOR = 4
    IF = 5
    ENDDO = 6
    BREAK = 7
    ELSEIF = 8
    ENDWHILE = 9
    PARAMETER = 10
    WHILE = 11
    CONTINUE = 12
    ENDBODY = 13
    FOR = 14
    RETURN = 15
    TRUE = 16
    DO = 17
    ENDIF = 18
    FUNCTION = 19
    THEN = 20
    FALSE = 21
    WS = 22
    COMMENT = 23
    ASSIGN = 24
    ADD = 25
    ADDFLOAT = 26
    SUB = 27
    SUBFLOAT = 28
    MUL = 29
    MULFLOAT = 30
    DIV = 31
    DIVFLOAT = 32
    MOD = 33
    NOT = 34
    AND = 35
    OR = 36
    EQUAL = 37
    NOTEQUAL = 38
    LESS = 39
    GREATER = 40
    LESSEQUAL = 41
    GREATEREQUAL = 42
    EQUALFLOAT = 43
    LESSFLOAT = 44
    GREATERFLOAT = 45
    LESSEQUALFLOAT = 46
    GREATEREQUALFLOAT = 47
    LP = 48
    RP = 49
    LA = 50
    RA = 51
    COLON = 52
    DOT = 53
    COMMA = 54
    SEMI = 55
    LB = 56
    RB = 57
    ID = 58
    INTLIT = 59
    FLOATLIT = 60
    STRINGLIT = 61
    ILLEGAL_ESCAPE = 62
    UNCLOSE_STRING = 63
    UNTERMINATED_COMMENT = 64
    ERROR_CHAR = 65

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def globdeclpart(self):
            return self.getTypedRuleContext(BKITParser.GlobdeclpartContext, 0)

        def funcdeclspart(self):
            return self.getTypedRuleContext(BKITParser.FuncdeclspartContext, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.globdeclpart()
            self.state = 87
            self.funcdeclspart()
            self.state = 88
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GlobdeclpartContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecls(self):
            return self.getTypedRuleContext(BKITParser.VardeclsContext, 0)

        def globdeclpart(self):
            return self.getTypedRuleContext(BKITParser.GlobdeclpartContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_globdeclpart

    def globdeclpart(self):

        localctx = BKITParser.GlobdeclpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_globdeclpart)
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.vardecls()
                self.state = 91
                self.globdeclpart()
                pass
            elif token in [BKITParser.EOF, BKITParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncdeclspartContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecls(self):
            return self.getTypedRuleContext(BKITParser.FuncdeclsContext, 0)

        def funcdeclspart(self):
            return self.getTypedRuleContext(BKITParser.FuncdeclspartContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_funcdeclspart

    def funcdeclspart(self):

        localctx = BKITParser.FuncdeclspartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcdeclspart)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.funcdecls()
                self.state = 97
                self.funcdeclspart()
                pass
            elif token in [BKITParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VardeclsContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def varlist(self):
            return self.getTypedRuleContext(BKITParser.VarlistContext, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_vardecls

    def vardecls(self):

        localctx = BKITParser.VardeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(BKITParser.VAR)
            self.state = 103
            self.match(BKITParser.COLON)
            self.state = 104
            self.varlist()
            self.state = 105
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarlistContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableinit(self):
            return self.getTypedRuleContext(BKITParser.VariableinitContext, 0)

        def tailvar(self):
            return self.getTypedRuleContext(BKITParser.TailvarContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_varlist

    def varlist(self):

        localctx = BKITParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varlist)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 2, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.variableinit()
                self.state = 108
                self.tailvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.variableinit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TailvarContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def variableinit(self):
            return self.getTypedRuleContext(BKITParser.VariableinitContext, 0)

        def tailvar(self):
            return self.getTypedRuleContext(BKITParser.TailvarContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_tailvar

    def tailvar(self):

        localctx = BKITParser.TailvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tailvar)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(BKITParser.COMMA)
                self.state = 114
                self.variableinit()
                self.state = 115
                self.tailvar()
                pass
            elif token in [BKITParser.SEMI]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableinitContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def literals(self):
            return self.getTypedRuleContext(BKITParser.LiteralsContext, 0)

        def dimlist(self):
            return self.getTypedRuleContext(BKITParser.DimlistContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_variableinit

    def variableinit(self):

        localctx = BKITParser.VariableinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableinit)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 4, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(BKITParser.ID)
                self.state = 122
                self.match(BKITParser.ASSIGN)
                self.state = 123
                self.literals()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.match(BKITParser.ID)
                self.state = 125
                self.dimlist()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.match(BKITParser.ID)
                self.state = 127
                self.dimlist()
                self.state = 128
                self.match(BKITParser.ASSIGN)
                self.state = 129
                self.literals()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralsContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def arraydecls(self):
            return self.getTypedRuleContext(BKITParser.ArraydeclsContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_literals

    def literals(self):

        localctx = BKITParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_literals)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(BKITParser.INTLIT)
                pass
            elif token in [BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(BKITParser.FLOATLIT)
                pass
            elif token in [BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.match(BKITParser.FALSE)
                pass
            elif token in [BKITParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.match(BKITParser.TRUE)
                pass
            elif token in [BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 137
                self.match(BKITParser.STRINGLIT)
                pass
            elif token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 138
                self.arraydecls()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArraydeclsContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def arraylit(self):
            return self.getTypedRuleContext(BKITParser.ArraylitContext, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_arraydecls

    def arraydecls(self):

        localctx = BKITParser.ArraydeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arraydecls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(BKITParser.LB)
            self.state = 142
            self.arraylit()
            self.state = 143
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArraylitContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(BKITParser.LiteralsContext, 0)

        def arraylit_(self):
            return self.getTypedRuleContext(BKITParser.Arraylit_Context, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_arraylit

    def arraylit(self):

        localctx = BKITParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arraylit)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.LB, BKITParser.INTLIT, BKITParser.FLOATLIT,
                         BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.literals()
                self.state = 146
                self.arraylit_()
                pass
            elif token in [BKITParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Arraylit_Context(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def literals(self):
            return self.getTypedRuleContext(BKITParser.LiteralsContext, 0)

        def arraylit_(self):
            return self.getTypedRuleContext(BKITParser.Arraylit_Context, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_arraylit_

    def arraylit_(self):

        localctx = BKITParser.Arraylit_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arraylit_)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(BKITParser.COMMA)
                self.state = 152
                self.literals()
                self.state = 153
                self.arraylit_()
                pass
            elif token in [BKITParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DimlistContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dim(self):
            return self.getTypedRuleContext(BKITParser.DimContext, 0)

        def taildim(self):
            return self.getTypedRuleContext(BKITParser.TaildimContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dimlist

    def dimlist(self):

        localctx = BKITParser.DimlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dimlist)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 8, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.dim()
                self.state = 159
                self.taildim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.dim()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TaildimContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dim(self):
            return self.getTypedRuleContext(BKITParser.DimContext, 0)

        def taildim(self):
            return self.getTypedRuleContext(BKITParser.TaildimContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_taildim

    def taildim(self):

        localctx = BKITParser.TaildimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_taildim)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.dim()
                self.state = 165
                self.taildim()
                pass
            elif token in [BKITParser.BODY, BKITParser.ASSIGN, BKITParser.COMMA, BKITParser.SEMI]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DimContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LA(self):
            return self.getToken(BKITParser.LA, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def RA(self):
            return self.getToken(BKITParser.RA, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dim

    def dim(self):

        localctx = BKITParser.DimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(BKITParser.LA)
            self.state = 171
            self.match(BKITParser.INTLIT)
            self.state = 172
            self.match(BKITParser.RA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncdeclsContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self, i: int = None):
            if i is None:
                return self.getTokens(BKITParser.COLON)
            else:
                return self.getToken(BKITParser.COLON, i)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext, i)

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(BKITParser.ParameterlistContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_funcdecls

    def funcdecls(self):

        localctx = BKITParser.FuncdeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funcdecls)
        self._la = 0  # Token type
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 12, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(BKITParser.FUNCTION)
                self.state = 175
                self.match(BKITParser.COLON)
                self.state = 176
                self.match(BKITParser.ID)
                self.state = 177
                self.match(BKITParser.BODY)
                self.state = 178
                self.match(BKITParser.COLON)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                        (1 << BKITParser.VAR) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (
                        1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (
                                1 << BKITParser.RETURN) | (1 << BKITParser.TRUE) | (1 << BKITParser.DO) | (
                                1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBFLOAT) | (
                                1 << BKITParser.NOT) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (
                                1 << BKITParser.ID) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (
                                1 << BKITParser.STRINGLIT))) != 0):
                    self.state = 179
                    self.statement()
                    self.state = 184
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 185
                self.match(BKITParser.ENDBODY)
                self.state = 186
                self.match(BKITParser.DOT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(BKITParser.FUNCTION)
                self.state = 188
                self.match(BKITParser.COLON)
                self.state = 189
                self.match(BKITParser.ID)
                self.state = 190
                self.match(BKITParser.PARAMETER)
                self.state = 191
                self.match(BKITParser.COLON)
                self.state = 192
                self.parameterlist()
                self.state = 193
                self.match(BKITParser.BODY)
                self.state = 194
                self.match(BKITParser.COLON)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                        (1 << BKITParser.VAR) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (
                        1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (
                                1 << BKITParser.RETURN) | (1 << BKITParser.TRUE) | (1 << BKITParser.DO) | (
                                1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBFLOAT) | (
                                1 << BKITParser.NOT) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (
                                1 << BKITParser.ID) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (
                                1 << BKITParser.STRINGLIT))) != 0):
                    self.state = 195
                    self.statement()
                    self.state = 200
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 201
                self.match(BKITParser.ENDBODY)
                self.state = 202
                self.match(BKITParser.DOT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterlistContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(BKITParser.ParameterContext, 0)

        def parameterlist_(self):
            return self.getTypedRuleContext(BKITParser.Parameterlist_Context, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_parameterlist

    def parameterlist(self):

        localctx = BKITParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameterlist)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 13, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.parameter()
                self.state = 207
                self.parameterlist_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parameterlist_Context(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def parameter(self):
            return self.getTypedRuleContext(BKITParser.ParameterContext, 0)

        def parameterlist_(self):
            return self.getTypedRuleContext(BKITParser.Parameterlist_Context, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_parameterlist_

    def parameterlist_(self):

        localctx = BKITParser.Parameterlist_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameterlist_)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(BKITParser.COMMA)
                self.state = 213
                self.parameter()
                self.state = 214
                self.parameterlist_()
                pass
            elif token in [BKITParser.BODY]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimlist(self):
            return self.getTypedRuleContext(BKITParser.DimlistContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_parameter

    def parameter(self):

        localctx = BKITParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameter)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 15, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(BKITParser.ID)
                self.state = 221
                self.dimlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RelopContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS(self):
            return self.getToken(BKITParser.LESS, 0)

        def LESSFLOAT(self):
            return self.getToken(BKITParser.LESSFLOAT, 0)

        def GREATER(self):
            return self.getToken(BKITParser.GREATER, 0)

        def GREATERFLOAT(self):
            return self.getToken(BKITParser.GREATERFLOAT, 0)

        def LESSEQUAL(self):
            return self.getToken(BKITParser.LESSEQUAL, 0)

        def LESSEQUALFLOAT(self):
            return self.getToken(BKITParser.LESSEQUALFLOAT, 0)

        def GREATEREQUAL(self):
            return self.getToken(BKITParser.GREATEREQUAL, 0)

        def GREATEREQUALFLOAT(self):
            return self.getToken(BKITParser.GREATEREQUALFLOAT, 0)

        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def EQUALFLOAT(self):
            return self.getToken(BKITParser.EQUALFLOAT, 0)

        def NOTEQUAL(self):
            return self.getToken(BKITParser.NOTEQUAL, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_relop

    def relop(self):

        localctx = BKITParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_relop)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << BKITParser.EQUAL) | (1 << BKITParser.NOTEQUAL) | (1 << BKITParser.LESS) | (
                    1 << BKITParser.GREATER) | (1 << BKITParser.LESSEQUAL) | (1 << BKITParser.GREATEREQUAL) | (
                            1 << BKITParser.EQUALFLOAT) | (1 << BKITParser.LESSFLOAT) | (
                            1 << BKITParser.GREATERFLOAT) | (1 << BKITParser.LESSEQUALFLOAT) | (
                            1 << BKITParser.GREATEREQUALFLOAT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Expr1Context, i)

        def relop(self):
            return self.getTypedRuleContext(BKITParser.RelopContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr

    def expr(self):

        localctx = BKITParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 16, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.expr1(0)
                self.state = 227
                self.relop()
                self.state = 228
                self.expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.expr1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(BKITParser.Expr2Context, 0)

        def expr1(self):
            return self.getTypedRuleContext(BKITParser.Expr1Context, 0)

        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr1

    def expr1(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr1, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 17, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 236
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 237
                    _la = self._input.LA(1)
                    if not (_la == BKITParser.AND or _la == BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 238
                    self.expr2(0)
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 17, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKITParser.Expr3Context, 0)

        def expr2(self):
            return self.getTypedRuleContext(BKITParser.Expr2Context, 0)

        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def ADDFLOAT(self):
            return self.getToken(BKITParser.ADDFLOAT, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBFLOAT(self):
            return self.getToken(BKITParser.SUBFLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr2

    def expr2(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr2, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 18, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 247
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 248
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                            (1 << BKITParser.ADD) | (1 << BKITParser.ADDFLOAT) | (1 << BKITParser.SUB) | (
                            1 << BKITParser.SUBFLOAT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 249
                    self.expr3(0)
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 18, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(BKITParser.Expr4Context, 0)

        def expr3(self):
            return self.getTypedRuleContext(BKITParser.Expr3Context, 0)

        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def MULFLOAT(self):
            return self.getToken(BKITParser.MULFLOAT, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def DIVFLOAT(self):
            return self.getToken(BKITParser.DIVFLOAT, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr3

    def expr3(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr3, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 19, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 258
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 259
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                            (1 << BKITParser.MUL) | (1 << BKITParser.MULFLOAT) | (1 << BKITParser.DIV) | (
                            1 << BKITParser.DIVFLOAT) | (1 << BKITParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 260
                    self.expr4()
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 19, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def expr4(self):
            return self.getTypedRuleContext(BKITParser.Expr4Context, 0)

        def expr5(self):
            return self.getTypedRuleContext(BKITParser.Expr5Context, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr4

    def expr4(self):

        localctx = BKITParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr4)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(BKITParser.NOT)
                self.state = 267
                self.expr4()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUBFLOAT, BKITParser.LP,
                           BKITParser.LB, BKITParser.ID, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.expr5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(BKITParser.Expr5Context, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBFLOAT(self):
            return self.getToken(BKITParser.SUBFLOAT, 0)

        def expr6(self):
            return self.getTypedRuleContext(BKITParser.Expr6Context, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr5

    def expr5(self):

        localctx = BKITParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr5)
        self._la = 0  # Token type
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUBFLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                _la = self._input.LA(1)
                if not (_la == BKITParser.SUB or _la == BKITParser.SUBFLOAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 272
                self.expr5()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.LP, BKITParser.LB, BKITParser.ID,
                           BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(BKITParser.Expr7Context, 0)

        def expr6(self):
            return self.getTypedRuleContext(BKITParser.Expr6Context, 0)

        def LA(self, i: int = None):
            if i is None:
                return self.getTokens(BKITParser.LA)
            else:
                return self.getToken(BKITParser.LA, i)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext, i)

        def RA(self, i: int = None):
            if i is None:
                return self.getTokens(BKITParser.RA)
            else:
                return self.getToken(BKITParser.RA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_expr6

    def expr6(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 23, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 279
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 284
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 280
                            self.match(BKITParser.LA)
                            self.state = 281
                            self.expr()
                            self.state = 282
                            self.match(BKITParser.RA)

                        else:
                            raise NoViableAltException(self)
                        self.state = 286
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input, 22, self._ctx)

                self.state = 292
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 23, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(BKITParser.LiteralsContext, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def functioncall(self):
            return self.getTypedRuleContext(BKITParser.FunctioncallContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr7

    def expr7(self):

        localctx = BKITParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr7)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 24, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.match(BKITParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.match(BKITParser.LP)
                self.state = 296
                self.expr()
                self.state = 297
                self.match(BKITParser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 299
                self.functioncall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctioncallContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def argumentslist(self):
            return self.getTypedRuleContext(BKITParser.ArgumentslistContext, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_functioncall

    def functioncall(self):

        localctx = BKITParser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_functioncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(BKITParser.ID)
            self.state = 303
            self.match(BKITParser.LP)
            self.state = 304
            self.argumentslist()
            self.state = 305
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentslistContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext, 0)

        def argumentslist_(self):
            return self.getTypedRuleContext(BKITParser.Argumentslist_Context, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_argumentslist

    def argumentslist(self):

        localctx = BKITParser.ArgumentslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_argumentslist)
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUBFLOAT, BKITParser.NOT,
                         BKITParser.LP, BKITParser.LB, BKITParser.ID, BKITParser.INTLIT, BKITParser.FLOATLIT,
                         BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.expr()
                self.state = 308
                self.argumentslist_()
                pass
            elif token in [BKITParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argumentslist_Context(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext, 0)

        def argumentslist_(self):
            return self.getTypedRuleContext(BKITParser.Argumentslist_Context, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_argumentslist_

    def argumentslist_(self):

        localctx = BKITParser.Argumentslist_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_argumentslist_)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(BKITParser.COMMA)
                self.state = 314
                self.expr()
                self.state = 315
                self.argumentslist_()
                pass
            elif token in [BKITParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecls(self):
            return self.getTypedRuleContext(BKITParser.VardeclsContext, 0)

        def assignmentstmt(self):
            return self.getTypedRuleContext(BKITParser.AssignmentstmtContext, 0)

        def ifstmt(self):
            return self.getTypedRuleContext(BKITParser.IfstmtContext, 0)

        def forstmt(self):
            return self.getTypedRuleContext(BKITParser.ForstmtContext, 0)

        def whilestmt(self):
            return self.getTypedRuleContext(BKITParser.WhilestmtContext, 0)

        def dowhilestmt(self):
            return self.getTypedRuleContext(BKITParser.DowhilestmtContext, 0)

        def breakstmt(self):
            return self.getTypedRuleContext(BKITParser.BreakstmtContext, 0)

        def continuestmt(self):
            return self.getTypedRuleContext(BKITParser.ContinuestmtContext, 0)

        def callstmt(self):
            return self.getTypedRuleContext(BKITParser.CallstmtContext, 0)

        def returnstmt(self):
            return self.getTypedRuleContext(BKITParser.ReturnstmtContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_statement

    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_statement)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 27, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.vardecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.assignmentstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 323
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 324
                self.whilestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 325
                self.dowhilestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 326
                self.breakstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 327
                self.continuestmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 328
                self.callstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 329
                self.returnstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentstmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext, i)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assignmentstmt

    def assignmentstmt(self):

        localctx = BKITParser.AssignmentstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assignmentstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.expr()
            self.state = 333
            self.match(BKITParser.ASSIGN)
            self.state = 334
            self.expr()
            self.state = 335
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfstmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext, i)

        def THEN(self, i: int = None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def if_statement(self):
            return self.getTypedRuleContext(BKITParser.If_statementContext, 0)

        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def ELSEIF(self, i: int = None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def elif_statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Elif_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Elif_statementContext, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def else_statement(self):
            return self.getTypedRuleContext(BKITParser.Else_statementContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_ifstmt

    def ifstmt(self):

        localctx = BKITParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ifstmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(BKITParser.IF)
            self.state = 338
            self.expr()
            self.state = 339
            self.match(BKITParser.THEN)
            self.state = 340
            self.if_statement()
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == BKITParser.ELSEIF:
                self.state = 341
                self.match(BKITParser.ELSEIF)
                self.state = 342
                self.expr()
                self.state = 343
                self.match(BKITParser.THEN)
                self.state = 344
                self.elif_statement()
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == BKITParser.ELSE:
                self.state = 351
                self.match(BKITParser.ELSE)
                self.state = 352
                self.else_statement()

            self.state = 355
            self.match(BKITParser.ENDIF)
            self.state = 356
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext, i)

        def getRuleIndex(self):
            return BKITParser.RULE_if_statement

    def if_statement(self):

        localctx = BKITParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_if_statement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << BKITParser.VAR) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (
                    1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (
                            1 << BKITParser.TRUE) | (1 << BKITParser.DO) | (1 << BKITParser.FALSE) | (
                            1 << BKITParser.SUB) | (1 << BKITParser.SUBFLOAT) | (1 << BKITParser.NOT) | (
                            1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.ID) | (
                            1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 358
                self.statement()
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Elif_statementContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext, i)

        def getRuleIndex(self):
            return BKITParser.RULE_elif_statement

    def elif_statement(self):

        localctx = BKITParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elif_statement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << BKITParser.VAR) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (
                    1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (
                            1 << BKITParser.TRUE) | (1 << BKITParser.DO) | (1 << BKITParser.FALSE) | (
                            1 << BKITParser.SUB) | (1 << BKITParser.SUBFLOAT) | (1 << BKITParser.NOT) | (
                            1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.ID) | (
                            1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 364
                self.statement()
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_statementContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext, i)

        def getRuleIndex(self):
            return BKITParser.RULE_else_statement

    def else_statement(self):

        localctx = BKITParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_else_statement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << BKITParser.VAR) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (
                    1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (
                            1 << BKITParser.TRUE) | (1 << BKITParser.DO) | (1 << BKITParser.FALSE) | (
                            1 << BKITParser.SUB) | (1 << BKITParser.SUBFLOAT) | (1 << BKITParser.NOT) | (
                            1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.ID) | (
                            1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 370
                self.statement()
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForstmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext, i)

        def getRuleIndex(self):
            return BKITParser.RULE_forstmt

    def forstmt(self):

        localctx = BKITParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_forstmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(BKITParser.FOR)
            self.state = 377
            self.match(BKITParser.LP)
            self.state = 378
            self.match(BKITParser.ID)
            self.state = 379
            self.match(BKITParser.ASSIGN)
            self.state = 380
            self.expr()
            self.state = 381
            self.match(BKITParser.COMMA)
            self.state = 382
            self.expr()
            self.state = 383
            self.match(BKITParser.COMMA)
            self.state = 384
            self.expr()
            self.state = 385
            self.match(BKITParser.RP)
            self.state = 386
            self.match(BKITParser.DO)
            self.state = 390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << BKITParser.VAR) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (
                    1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (
                            1 << BKITParser.TRUE) | (1 << BKITParser.DO) | (1 << BKITParser.FALSE) | (
                            1 << BKITParser.SUB) | (1 << BKITParser.SUBFLOAT) | (1 << BKITParser.NOT) | (
                            1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.ID) | (
                            1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 387
                self.statement()
                self.state = 392
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 393
            self.match(BKITParser.ENDFOR)
            self.state = 394
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhilestmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext, i)

        def getRuleIndex(self):
            return BKITParser.RULE_whilestmt

    def whilestmt(self):

        localctx = BKITParser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_whilestmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(BKITParser.WHILE)
            self.state = 397
            self.expr()
            self.state = 398
            self.match(BKITParser.DO)
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << BKITParser.VAR) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (
                    1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (
                            1 << BKITParser.TRUE) | (1 << BKITParser.DO) | (1 << BKITParser.FALSE) | (
                            1 << BKITParser.SUB) | (1 << BKITParser.SUBFLOAT) | (1 << BKITParser.NOT) | (
                            1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.ID) | (
                            1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 399
                self.statement()
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 405
            self.match(BKITParser.ENDWHILE)
            self.state = 406
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DowhilestmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext, 0)

        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext, i)

        def getRuleIndex(self):
            return BKITParser.RULE_dowhilestmt

    def dowhilestmt(self):

        localctx = BKITParser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_dowhilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(BKITParser.DO)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 35, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 409
                    self.statement()
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 35, self._ctx)

            self.state = 415
            self.match(BKITParser.WHILE)
            self.state = 416
            self.expr()
            self.state = 417
            self.match(BKITParser.ENDDO)
            self.state = 418
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BreakstmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_breakstmt

    def breakstmt(self):

        localctx = BKITParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(BKITParser.BREAK)
            self.state = 421
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContinuestmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continuestmt

    def continuestmt(self):

        localctx = BKITParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(BKITParser.CONTINUE)
            self.state = 424
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallstmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def argumentslist(self):
            return self.getTypedRuleContext(BKITParser.ArgumentslistContext, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_callstmt

    def callstmt(self):

        localctx = BKITParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(BKITParser.ID)
            self.state = 427
            self.match(BKITParser.LP)
            self.state = 428
            self.argumentslist()
            self.state = 429
            self.match(BKITParser.RP)
            self.state = 430
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnstmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_returnstmt

    def returnstmt(self):

        localctx = BKITParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_returnstmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(BKITParser.RETURN)
            self.state = 434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (
                    1 << BKITParser.SUBFLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (
                            1 << BKITParser.ID) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (
                            1 << BKITParser.STRINGLIT))) != 0):
                self.state = 433
                self.expr()

            self.state = 436
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.expr1_sempred
        self._predicates[21] = self.expr2_sempred
        self._predicates[22] = self.expr3_sempred
        self._predicates[25] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx: Expr1Context, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 2)

    def expr2_sempred(self, localctx: Expr2Context, predIndex: int):
        if predIndex == 1:
            return self.precpred(self._ctx, 2)

    def expr3_sempred(self, localctx: Expr3Context, predIndex: int):
        if predIndex == 2:
            return self.precpred(self._ctx, 2)

    def expr6_sempred(self, localctx: Expr6Context, predIndex: int):
        if predIndex == 3:
            return self.precpred(self._ctx, 2)
