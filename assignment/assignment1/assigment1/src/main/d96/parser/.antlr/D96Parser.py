# Generated from d:\Study2\HCMUT\semester212\PPL\code\assignment\assignment1\assigment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u021f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\6")
        buf.write("\2v\n\2\r\2\16\2w\3\3\3\3\3\3\3\3\3\3\7\3\177\n\3\f\3")
        buf.write("\16\3\u0082\13\3\5\3\u0084\n\3\3\3\3\3\3\3\7\3\u0089\n")
        buf.write("\3\f\3\16\3\u008c\13\3\3\3\3\3\3\3\7\3\u0091\n\3\f\3\16")
        buf.write("\3\u0094\13\3\3\3\3\3\3\3\7\3\u0099\n\3\f\3\16\3\u009c")
        buf.write("\13\3\5\3\u009e\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\7\4\u00a7")
        buf.write("\n\4\f\4\16\4\u00aa\13\4\5\4\u00ac\n\4\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\6\16\u00cc\n\16\r\16\16\16\u00cd\3\16\7\16\u00d1\n")
        buf.write("\16\f\16\16\16\u00d4\13\16\3\16\3\16\3\16\7\16\u00d9\n")
        buf.write("\16\f\16\16\16\u00dc\13\16\3\16\5\16\u00df\n\16\3\17\3")
        buf.write("\17\3\17\5\17\u00e4\n\17\3\17\3\17\3\17\3\17\3\20\7\20")
        buf.write("\u00eb\n\20\f\20\16\20\u00ee\13\20\3\21\3\21\3\21\5\21")
        buf.write("\u00f3\n\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0104\n\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u0110")
        buf.write("\n\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0119\n")
        buf.write("\26\3\27\3\27\3\27\5\27\u011e\n\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u0130\n\31\3\32\3\32\3\32\3\32\7\32\u0136\n")
        buf.write("\32\f\32\16\32\u0139\13\32\3\33\3\33\3\33\3\33\3\34\3")
        buf.write("\34\3\35\3\35\3\35\5\35\u0144\n\35\3\35\3\35\3\35\5\35")
        buf.write("\u0149\n\35\3\35\3\35\5\35\u014d\n\35\3\35\3\35\3\36\3")
        buf.write("\36\3\36\5\36\u0154\n\36\3\37\3\37\3\37\5\37\u0159\n\37")
        buf.write("\3 \3 \7 \u015d\n \f \16 \u0160\13 \3!\3!\7!\u0164\n!")
        buf.write("\f!\16!\u0167\13!\3\"\3\"\3\"\3\"\5\"\u016d\n\"\3#\3#")
        buf.write("\3#\3#\7#\u0173\n#\f#\16#\u0176\13#\3$\3$\3%\3%\3%\3&")
        buf.write("\3&\3&\3&\7&\u0181\n&\f&\16&\u0184\13&\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\5+\u019f\n+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\5+\u01ac\n+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\7+\u01bc\n+\f+\16+\u01bf\13+\3,\3,\3,\7,\u01c4\n,\f")
        buf.write(",\16,\u01c7\13,\3-\3-\3-\3-\3-\5-\u01ce\n-\3-\3-\5-\u01d2")
        buf.write("\n-\3-\3-\3.\3.\5.\u01d8\n.\3.\3.\3.\3/\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\7\61\u01ee\n\61\f\61\16\61\u01f1\13\61\3\62\3\62")
        buf.write("\5\62\u01f5\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\5\64\u0204\n\64\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\38\3")
        buf.write("8\38\38\39\39\59\u0219\n9\39\39\3:\3:\3:\2\3T;\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bdfhjlnpr\2\13\3\2=@\3\2AB\3\2 $")
        buf.write("\3\2#-\3\2&-\3\2./\4\2\16\16\20\23\3\2\27\30\3\2&\'\2")
        buf.write("\u021d\2u\3\2\2\2\4y\3\2\2\2\6\u00a1\3\2\2\2\b\u00af\3")
        buf.write("\2\2\2\n\u00b1\3\2\2\2\f\u00b3\3\2\2\2\16\u00b5\3\2\2")
        buf.write("\2\20\u00b7\3\2\2\2\22\u00b9\3\2\2\2\24\u00bb\3\2\2\2")
        buf.write("\26\u00c2\3\2\2\2\30\u00c7\3\2\2\2\32\u00de\3\2\2\2\34")
        buf.write("\u00e0\3\2\2\2\36\u00ec\3\2\2\2 \u00f2\3\2\2\2\"\u00f4")
        buf.write("\3\2\2\2$\u00f7\3\2\2\2&\u0103\3\2\2\2(\u0105\3\2\2\2")
        buf.write("*\u0118\3\2\2\2,\u011a\3\2\2\2.\u0124\3\2\2\2\60\u012f")
        buf.write("\3\2\2\2\62\u0137\3\2\2\2\64\u013a\3\2\2\2\66\u013e\3")
        buf.write("\2\2\28\u0140\3\2\2\2:\u0153\3\2\2\2<\u0158\3\2\2\2>\u015e")
        buf.write("\3\2\2\2@\u0165\3\2\2\2B\u016c\3\2\2\2D\u0174\3\2\2\2")
        buf.write("F\u0177\3\2\2\2H\u0179\3\2\2\2J\u017c\3\2\2\2L\u0185\3")
        buf.write("\2\2\2N\u0189\3\2\2\2P\u018d\3\2\2\2R\u0194\3\2\2\2T\u01ab")
        buf.write("\3\2\2\2V\u01c0\3\2\2\2X\u01c8\3\2\2\2Z\u01d7\3\2\2\2")
        buf.write("\\\u01dc\3\2\2\2^\u01e0\3\2\2\2`\u01e6\3\2\2\2b\u01f4")
        buf.write("\3\2\2\2d\u01f6\3\2\2\2f\u01fc\3\2\2\2h\u0205\3\2\2\2")
        buf.write("j\u0208\3\2\2\2l\u020b\3\2\2\2n\u020f\3\2\2\2p\u0216\3")
        buf.write("\2\2\2r\u021c\3\2\2\2tv\t\2\2\2ut\3\2\2\2vw\3\2\2\2wu")
        buf.write("\3\2\2\2wx\3\2\2\2x\3\3\2\2\2yz\7\16\2\2z\u009d\7\60\2")
        buf.write("\2{\u0080\7=\2\2|}\7\66\2\2}\177\7=\2\2~|\3\2\2\2\177")
        buf.write("\u0082\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081")
        buf.write("\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0083{\3\2\2\2\u0083")
        buf.write("\u0084\3\2\2\2\u0084\u009e\3\2\2\2\u0085\u008a\7>\2\2")
        buf.write("\u0086\u0087\7\66\2\2\u0087\u0089\7>\2\2\u0088\u0086\3")
        buf.write("\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\u009e\3\2\2\2\u008c\u008a\3\2\2\2\u008d")
        buf.write("\u0092\7?\2\2\u008e\u008f\7\66\2\2\u008f\u0091\7?\2\2")
        buf.write("\u0090\u008e\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3")
        buf.write("\2\2\2\u0092\u0093\3\2\2\2\u0093\u009e\3\2\2\2\u0094\u0092")
        buf.write("\3\2\2\2\u0095\u009a\7@\2\2\u0096\u0097\7\66\2\2\u0097")
        buf.write("\u0099\7@\2\2\u0098\u0096\3\2\2\2\u0099\u009c\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009e\3")
        buf.write("\2\2\2\u009c\u009a\3\2\2\2\u009d\u0083\3\2\2\2\u009d\u0085")
        buf.write("\3\2\2\2\u009d\u008d\3\2\2\2\u009d\u0095\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a0\7\61\2\2\u00a0\5\3\2\2\2\u00a1")
        buf.write("\u00a2\7\16\2\2\u00a2\u00ab\7\60\2\2\u00a3\u00a8\5\4\3")
        buf.write("\2\u00a4\u00a5\7\66\2\2\u00a5\u00a7\5\4\3\2\u00a6\u00a4")
        buf.write("\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2")
        buf.write("\u00ab\u00a3\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\3")
        buf.write("\2\2\2\u00ad\u00ae\7\61\2\2\u00ae\7\3\2\2\2\u00af\u00b0")
        buf.write("\t\3\2\2\u00b0\t\3\2\2\2\u00b1\u00b2\t\4\2\2\u00b2\13")
        buf.write("\3\2\2\2\u00b3\u00b4\t\5\2\2\u00b4\r\3\2\2\2\u00b5\u00b6")
        buf.write("\t\6\2\2\u00b6\17\3\2\2\2\u00b7\u00b8\t\7\2\2\u00b8\21")
        buf.write("\3\2\2\2\u00b9\u00ba\t\b\2\2\u00ba\23\3\2\2\2\u00bb\u00bc")
        buf.write("\7\16\2\2\u00bc\u00bd\7\62\2\2\u00bd\u00be\5\22\n\2\u00be")
        buf.write("\u00bf\7\66\2\2\u00bf\u00c0\7=\2\2\u00c0\u00c1\7\63\2")
        buf.write("\2\u00c1\25\3\2\2\2\u00c2\u00c3\7\33\2\2\u00c3\u00c4\7")
        buf.write("A\2\2\u00c4\u00c5\7\60\2\2\u00c5\u00c6\7\61\2\2\u00c6")
        buf.write("\27\3\2\2\2\u00c7\u00c8\5\32\16\2\u00c8\u00c9\7\2\2\3")
        buf.write("\u00c9\31\3\2\2\2\u00ca\u00cc\5\34\17\2\u00cb\u00ca\3")
        buf.write("\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce")
        buf.write("\3\2\2\2\u00ce\u00df\3\2\2\2\u00cf\u00d1\5\34\17\2\u00d0")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d2\u00d3\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d2\3")
        buf.write("\2\2\2\u00d5\u00df\5$\23\2\u00d6\u00da\5$\23\2\u00d7\u00d9")
        buf.write("\5\34\17\2\u00d8\u00d7\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da")
        buf.write("\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00df\3\2\2\2")
        buf.write("\u00dc\u00da\3\2\2\2\u00dd\u00df\5$\23\2\u00de\u00cb\3")
        buf.write("\2\2\2\u00de\u00d2\3\2\2\2\u00de\u00d6\3\2\2\2\u00de\u00dd")
        buf.write("\3\2\2\2\u00df\33\3\2\2\2\u00e0\u00e1\7\26\2\2\u00e1\u00e3")
        buf.write("\7A\2\2\u00e2\u00e4\5\"\22\2\u00e3\u00e2\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\7:\2\2")
        buf.write("\u00e6\u00e7\5\36\20\2\u00e7\u00e8\7;\2\2\u00e8\35\3\2")
        buf.write("\2\2\u00e9\u00eb\5 \21\2\u00ea\u00e9\3\2\2\2\u00eb\u00ee")
        buf.write("\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed")
        buf.write("\37\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f3\58\35\2\u00f0")
        buf.write("\u00f3\5*\26\2\u00f1\u00f3\5r:\2\u00f2\u00ef\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3!\3\2\2\2\u00f4")
        buf.write("\u00f5\7\67\2\2\u00f5\u00f6\7A\2\2\u00f6#\3\2\2\2\u00f7")
        buf.write("\u00f8\7\26\2\2\u00f8\u00f9\7\3\2\2\u00f9\u00fa\7:\2\2")
        buf.write("\u00fa\u00fb\5&\24\2\u00fb\u00fc\7;\2\2\u00fc%\3\2\2\2")
        buf.write("\u00fd\u00fe\5(\25\2\u00fe\u00ff\5\36\20\2\u00ff\u0104")
        buf.write("\3\2\2\2\u0100\u0101\5\36\20\2\u0101\u0102\5(\25\2\u0102")
        buf.write("\u0104\3\2\2\2\u0103\u00fd\3\2\2\2\u0103\u0100\3\2\2\2")
        buf.write("\u0104\'\3\2\2\2\u0105\u0106\7\35\2\2\u0106\u0107\7\60")
        buf.write("\2\2\u0107\u0108\7\61\2\2\u0108\u0109\7:\2\2\u0109\u010a")
        buf.write("\5\66\34\2\u010a\u010b\7;\2\2\u010b)\3\2\2\2\u010c\u010d")
        buf.write("\7A\2\2\u010d\u010f\7\60\2\2\u010e\u0110\5\60\31\2\u010f")
        buf.write("\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111\u0112\7\61\2\2\u0112\u0113\7:\2\2\u0113\u0114\5")
        buf.write("\66\34\2\u0114\u0115\7;\2\2\u0115\u0119\3\2\2\2\u0116")
        buf.write("\u0119\5,\27\2\u0117\u0119\5.\30\2\u0118\u010c\3\2\2\2")
        buf.write("\u0118\u0116\3\2\2\2\u0118\u0117\3\2\2\2\u0119+\3\2\2")
        buf.write("\2\u011a\u011b\7\31\2\2\u011b\u011d\7\60\2\2\u011c\u011e")
        buf.write("\5\60\31\2\u011d\u011c\3\2\2\2\u011d\u011e\3\2\2\2\u011e")
        buf.write("\u011f\3\2\2\2\u011f\u0120\7\61\2\2\u0120\u0121\7:\2\2")
        buf.write("\u0121\u0122\5\66\34\2\u0122\u0123\7;\2\2\u0123-\3\2\2")
        buf.write("\2\u0124\u0125\7\32\2\2\u0125\u0126\7\60\2\2\u0126\u0127")
        buf.write("\7\61\2\2\u0127\u0128\7:\2\2\u0128\u0129\5\66\34\2\u0129")
        buf.write("\u012a\7;\2\2\u012a/\3\2\2\2\u012b\u0130\5\64\33\2\u012c")
        buf.write("\u012d\5\64\33\2\u012d\u012e\5\62\32\2\u012e\u0130\3\2")
        buf.write("\2\2\u012f\u012b\3\2\2\2\u012f\u012c\3\2\2\2\u0130\61")
        buf.write("\3\2\2\2\u0131\u0132\79\2\2\u0132\u0133\5\64\33\2\u0133")
        buf.write("\u0134\5\62\32\2\u0134\u0136\3\2\2\2\u0135\u0131\3\2\2")
        buf.write("\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\63\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u013b")
        buf.write("\5:\36\2\u013b\u013c\7\67\2\2\u013c\u013d\5\22\n\2\u013d")
        buf.write("\65\3\2\2\2\u013e\u013f\7\4\2\2\u013f\67\3\2\2\2\u0140")
        buf.write("\u0143\t\t\2\2\u0141\u0144\5:\36\2\u0142\u0144\5<\37\2")
        buf.write("\u0143\u0141\3\2\2\2\u0143\u0142\3\2\2\2\u0144\u0145\3")
        buf.write("\2\2\2\u0145\u0148\7\67\2\2\u0146\u0149\5\24\13\2\u0147")
        buf.write("\u0149\5\22\n\2\u0148\u0146\3\2\2\2\u0148\u0147\3\2\2")
        buf.write("\2\u0149\u014c\3\2\2\2\u014a\u014b\7\37\2\2\u014b\u014d")
        buf.write("\5B\"\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014e\u014f\79\2\2\u014f9\3\2\2\2\u0150")
        buf.write("\u0154\7A\2\2\u0151\u0152\7A\2\2\u0152\u0154\5> \2\u0153")
        buf.write("\u0150\3\2\2\2\u0153\u0151\3\2\2\2\u0154;\3\2\2\2\u0155")
        buf.write("\u0159\7B\2\2\u0156\u0157\7B\2\2\u0157\u0159\5@!\2\u0158")
        buf.write("\u0155\3\2\2\2\u0158\u0156\3\2\2\2\u0159=\3\2\2\2\u015a")
        buf.write("\u015b\7\66\2\2\u015b\u015d\7A\2\2\u015c\u015a\3\2\2\2")
        buf.write("\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3")
        buf.write("\2\2\2\u015f?\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162")
        buf.write("\7\66\2\2\u0162\u0164\7B\2\2\u0163\u0161\3\2\2\2\u0164")
        buf.write("\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2")
        buf.write("\u0166A\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u016d\5F$\2")
        buf.write("\u0169\u016a\5F$\2\u016a\u016b\5D#\2\u016b\u016d\3\2\2")
        buf.write("\2\u016c\u0168\3\2\2\2\u016c\u0169\3\2\2\2\u016dC\3\2")
        buf.write("\2\2\u016e\u016f\7\66\2\2\u016f\u0170\5F$\2\u0170\u0171")
        buf.write("\5D#\2\u0171\u0173\3\2\2\2\u0172\u016e\3\2\2\2\u0173\u0176")
        buf.write("\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write("E\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\7\5\2\2\u0178")
        buf.write("G\3\2\2\2\u0179\u017a\5F$\2\u017a\u017b\5J&\2\u017bI\3")
        buf.write("\2\2\2\u017c\u017d\7\62\2\2\u017d\u017e\5F$\2\u017e\u0182")
        buf.write("\7\63\2\2\u017f\u0181\5J&\2\u0180\u017f\3\2\2\2\u0181")
        buf.write("\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183K\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\7A\2\2")
        buf.write("\u0186\u0187\7\64\2\2\u0187\u0188\7A\2\2\u0188M\3\2\2")
        buf.write("\2\u0189\u018a\7A\2\2\u018a\u018b\78\2\2\u018b\u018c\7")
        buf.write("A\2\2\u018cO\3\2\2\2\u018d\u018e\7A\2\2\u018e\u018f\7")
        buf.write("8\2\2\u018f\u0190\7A\2\2\u0190\u0191\7\60\2\2\u0191\u0192")
        buf.write("\5B\"\2\u0192\u0193\7\61\2\2\u0193Q\3\2\2\2\u0194\u0195")
        buf.write("\7\33\2\2\u0195\u0196\7A\2\2\u0196\u0197\7\60\2\2\u0197")
        buf.write("\u0198\5B\"\2\u0198\u0199\7\61\2\2\u0199S\3\2\2\2\u019a")
        buf.write("\u019b\b+\1\2\u019b\u019c\7A\2\2\u019c\u019e\7\60\2\2")
        buf.write("\u019d\u019f\5V,\2\u019e\u019d\3\2\2\2\u019e\u019f\3\2")
        buf.write("\2\2\u019f\u01a0\3\2\2\2\u01a0\u01ac\7\61\2\2\u01a1\u01a2")
        buf.write("\7\'\2\2\u01a2\u01ac\5T+\n\u01a3\u01a4\7 \2\2\u01a4\u01ac")
        buf.write("\5T+\t\u01a5\u01ac\7A\2\2\u01a6\u01ac\7=\2\2\u01a7\u01a8")
        buf.write("\7\60\2\2\u01a8\u01a9\5T+\2\u01a9\u01aa\7\61\2\2\u01aa")
        buf.write("\u01ac\3\2\2\2\u01ab\u019a\3\2\2\2\u01ab\u01a1\3\2\2\2")
        buf.write("\u01ab\u01a3\3\2\2\2\u01ab\u01a5\3\2\2\2\u01ab\u01a6\3")
        buf.write("\2\2\2\u01ab\u01a7\3\2\2\2\u01ac\u01bd\3\2\2\2\u01ad\u01ae")
        buf.write("\f\b\2\2\u01ae\u01af\7(\2\2\u01af\u01bc\5T+\t\u01b0\u01b1")
        buf.write("\f\7\2\2\u01b1\u01b2\t\n\2\2\u01b2\u01bc\5T+\b\u01b3\u01b4")
        buf.write("\f\6\2\2\u01b4\u01b5\7#\2\2\u01b5\u01bc\5T+\7\u01b6\u01b7")
        buf.write("\f\13\2\2\u01b7\u01b8\7\62\2\2\u01b8\u01b9\5T+\2\u01b9")
        buf.write("\u01ba\7\63\2\2\u01ba\u01bc\3\2\2\2\u01bb\u01ad\3\2\2")
        buf.write("\2\u01bb\u01b0\3\2\2\2\u01bb\u01b3\3\2\2\2\u01bb\u01b6")
        buf.write("\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd")
        buf.write("\u01be\3\2\2\2\u01beU\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0")
        buf.write("\u01c5\5T+\2\u01c1\u01c2\7\66\2\2\u01c2\u01c4\5T+\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2")
        buf.write("\u01c5\u01c6\3\2\2\2\u01c6W\3\2\2\2\u01c7\u01c5\3\2\2")
        buf.write("\2\u01c8\u01c9\t\t\2\2\u01c9\u01ca\5:\36\2\u01ca\u01cd")
        buf.write("\7\67\2\2\u01cb\u01ce\5\24\13\2\u01cc\u01ce\5\22\n\2\u01cd")
        buf.write("\u01cb\3\2\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01d1\3\2\2\2")
        buf.write("\u01cf\u01d0\7\37\2\2\u01d0\u01d2\5B\"\2\u01d1\u01cf\3")
        buf.write("\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d4")
        buf.write("\79\2\2\u01d4Y\3\2\2\2\u01d5\u01d8\5\b\5\2\u01d6\u01d8")
        buf.write("\5H%\2\u01d7\u01d5\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01d9")
        buf.write("\3\2\2\2\u01d9\u01da\7\37\2\2\u01da\u01db\5F$\2\u01db")
        buf.write("[\3\2\2\2\u01dc\u01dd\5^\60\2\u01dd\u01de\5`\61\2\u01de")
        buf.write("\u01df\5b\62\2\u01df]\3\2\2\2\u01e0\u01e1\7\n\2\2\u01e1")
        buf.write("\u01e2\7\60\2\2\u01e2\u01e3\5F$\2\u01e3\u01e4\7\61\2\2")
        buf.write("\u01e4\u01e5\5p9\2\u01e5_\3\2\2\2\u01e6\u01e7\7\13\2\2")
        buf.write("\u01e7\u01e8\7\60\2\2\u01e8\u01e9\5F$\2\u01e9\u01ea\7")
        buf.write("\61\2\2\u01ea\u01eb\5p9\2\u01eb\u01ef\3\2\2\2\u01ec\u01ee")
        buf.write("\5`\61\2\u01ed\u01ec\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0a\3\2\2\2\u01f1")
        buf.write("\u01ef\3\2\2\2\u01f2\u01f3\7\f\2\2\u01f3\u01f5\5p9\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5c\3\2\2\2\u01f6")
        buf.write("\u01f7\7\r\2\2\u01f7\u01f8\7\60\2\2\u01f8\u01f9\5f\64")
        buf.write("\2\u01f9\u01fa\7\61\2\2\u01fa\u01fb\5p9\2\u01fbe\3\2\2")
        buf.write("\2\u01fc\u01fd\7A\2\2\u01fd\u01fe\7\17\2\2\u01fe\u01ff")
        buf.write("\7=\2\2\u01ff\u0200\7\65\2\2\u0200\u0203\7=\2\2\u0201")
        buf.write("\u0202\7\34\2\2\u0202\u0204\7=\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204g\3\2\2\2\u0205\u0206\7\b\2")
        buf.write("\2\u0206\u0207\79\2\2\u0207i\3\2\2\2\u0208\u0209\7\t\2")
        buf.write("\2\u0209\u020a\79\2\2\u020ak\3\2\2\2\u020b\u020c\7\24")
        buf.write("\2\2\u020c\u020d\5F$\2\u020d\u020e\79\2\2\u020em\3\2\2")
        buf.write("\2\u020f\u0210\7A\2\2\u0210\u0211\78\2\2\u0211\u0212\7")
        buf.write("B\2\2\u0212\u0213\7\60\2\2\u0213\u0214\7\61\2\2\u0214")
        buf.write("\u0215\79\2\2\u0215o\3\2\2\2\u0216\u0218\7:\2\2\u0217")
        buf.write("\u0219\5r:\2\u0218\u0217\3\2\2\2\u0218\u0219\3\2\2\2\u0219")
        buf.write("\u021a\3\2\2\2\u021a\u021b\7;\2\2\u021bq\3\2\2\2\u021c")
        buf.write("\u021d\7\6\2\2\u021ds\3\2\2\2.w\u0080\u0083\u008a\u0092")
        buf.write("\u009a\u009d\u00a8\u00ab\u00cd\u00d2\u00da\u00de\u00e3")
        buf.write("\u00ec\u00f2\u0103\u010f\u0118\u011d\u012f\u0137\u0143")
        buf.write("\u0148\u014c\u0153\u0158\u015e\u0165\u016c\u0174\u0182")
        buf.write("\u019e\u01ab\u01bb\u01bd\u01c5\u01cd\u01d1\u01d7\u01ef")
        buf.write("\u01f4\u0203\u0218")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Program'", "'method body'", "'expr'", 
                     "'statement'", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
                     "'Constructor'", "'Destructor'", "'New'", "'By'", "'main'", 
                     "'self'", "'='", "'!'", "'||'", "'&&'", "'=='", "'!='", 
                     "'%'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", "'>'", 
                     "'>='", "'+.'", "'==.'", "'('", "')'", "'['", "']'", 
                     "'.'", "'..'", "','", "':'", "'::'", "';'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", 
                      "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", 
                      "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", "K_RETURN", 
                      "K_NULL", "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", 
                      "K_DESTRUCTOR", "K_NEW", "K_BY", "K_MAIN", "K_SELF", 
                      "OP_ASSIGN", "OP_LOGICAL_NOT", "OP_LOGICAL_OR", "OP_LOGICAL_AND", 
                      "OP_IS_EQUAL_TO", "OP_NOT_EQUAL_TO", "OP_MODULO", 
                      "OP_ADDTION", "OP_SUBTRACTION", "OP_MULTIPLICATION", 
                      "OP_DIVISION", "OP_LESS_THAN", "OP_LESS_THAN_EQUAL", 
                      "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", "OP_STRING_CONCATENATION", 
                      "OP_TWO_SAME_STRING", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "DOT", 
                      "DOUBLE_DOT", "COMMA", "COLON", "DOUBLE_COLON", "SEMI_COLON", 
                      "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "ESCAPE", 
                      "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", 
                      "STRING_LITERAL", "IDENTIFIER", "DOLAR_IDENTIFIER", 
                      "WHITE_SPACE", "ERROR_TOKEN" ]

    RULE_literal = 0
    RULE_indexed_array = 1
    RULE_multi_dimentional_array = 2
    RULE_identifier = 3
    RULE_operator_boolean = 4
    RULE_operator_integer = 5
    RULE_operator_float = 6
    RULE_operator_string = 7
    RULE_primitive_type = 8
    RULE_array_type = 9
    RULE_class_type = 10
    RULE_program = 11
    RULE_many_class = 12
    RULE_class_declaration = 13
    RULE_class_body = 14
    RULE_class_body_unit = 15
    RULE_super_class_group = 16
    RULE_program_class_declaration = 17
    RULE_program_class_body = 18
    RULE_main_method_declaration = 19
    RULE_method_declaration = 20
    RULE_constructor = 21
    RULE_destructor = 22
    RULE_parameter_list = 23
    RULE_parameter_list_tail = 24
    RULE_parameter = 25
    RULE_method_body = 26
    RULE_attribute_declaration = 27
    RULE_identifier_list = 28
    RULE_dolar_identifier_list = 29
    RULE_identifier_list_tail = 30
    RULE_dolar_identifier_list_tail = 31
    RULE_expression_list = 32
    RULE_expression_list_tail = 33
    RULE_expression = 34
    RULE_element_expression = 35
    RULE_index_operator = 36
    RULE_instance_attribute_access = 37
    RULE_static_attribute_access = 38
    RULE_instace_method_invocation = 39
    RULE_object_creation = 40
    RULE_expr = 41
    RULE_exprList = 42
    RULE_var_val_statement = 43
    RULE_assign_statement = 44
    RULE_if_statement = 45
    RULE_if_part = 46
    RULE_else_if_part = 47
    RULE_else_part = 48
    RULE_for_in_statement = 49
    RULE_loop_part = 50
    RULE_break_statement = 51
    RULE_continue_statement = 52
    RULE_return_statement = 53
    RULE_method_invocation_statement = 54
    RULE_block_statement = 55
    RULE_statement = 56

    ruleNames =  [ "literal", "indexed_array", "multi_dimentional_array", 
                   "identifier", "operator_boolean", "operator_integer", 
                   "operator_float", "operator_string", "primitive_type", 
                   "array_type", "class_type", "program", "many_class", 
                   "class_declaration", "class_body", "class_body_unit", 
                   "super_class_group", "program_class_declaration", "program_class_body", 
                   "main_method_declaration", "method_declaration", "constructor", 
                   "destructor", "parameter_list", "parameter_list_tail", 
                   "parameter", "method_body", "attribute_declaration", 
                   "identifier_list", "dolar_identifier_list", "identifier_list_tail", 
                   "dolar_identifier_list_tail", "expression_list", "expression_list_tail", 
                   "expression", "element_expression", "index_operator", 
                   "instance_attribute_access", "static_attribute_access", 
                   "instace_method_invocation", "object_creation", "expr", 
                   "exprList", "var_val_statement", "assign_statement", 
                   "if_statement", "if_part", "else_if_part", "else_part", 
                   "for_in_statement", "loop_part", "break_statement", "continue_statement", 
                   "return_statement", "method_invocation_statement", "block_statement", 
                   "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    COMMENT=5
    K_BREAK=6
    K_CONTINUE=7
    K_IF=8
    K_ELSE_IF=9
    K_ELSE=10
    K_FOR_EACH=11
    K_ARRAY=12
    K_IN=13
    K_INT=14
    K_FLOAT=15
    K_BOOLEAN=16
    K_STRING=17
    K_RETURN=18
    K_NULL=19
    K_CLASS=20
    K_VAL=21
    K_VAR=22
    K_CONSTRUCTOR=23
    K_DESTRUCTOR=24
    K_NEW=25
    K_BY=26
    K_MAIN=27
    K_SELF=28
    OP_ASSIGN=29
    OP_LOGICAL_NOT=30
    OP_LOGICAL_OR=31
    OP_LOGICAL_AND=32
    OP_IS_EQUAL_TO=33
    OP_NOT_EQUAL_TO=34
    OP_MODULO=35
    OP_ADDTION=36
    OP_SUBTRACTION=37
    OP_MULTIPLICATION=38
    OP_DIVISION=39
    OP_LESS_THAN=40
    OP_LESS_THAN_EQUAL=41
    OP_GREATER_THAN=42
    OP_GREATER_THAN_EQUAL=43
    OP_STRING_CONCATENATION=44
    OP_TWO_SAME_STRING=45
    LEFT_PAREN=46
    RIGHT_PAREN=47
    LEFT_SQUARE_BRACKET=48
    RIGHT_SQUARE_BRACKET=49
    DOT=50
    DOUBLE_DOT=51
    COMMA=52
    COLON=53
    DOUBLE_COLON=54
    SEMI_COLON=55
    LEFT_CURLY_BRACKET=56
    RIGHT_CURLY_BRACKET=57
    ESCAPE=58
    INTEGER_LITERAL=59
    FLOAT_LITERAL=60
    BOOLEAN_LITERAL=61
    STRING_LITERAL=62
    IDENTIFIER=63
    DOLAR_IDENTIFIER=64
    WHITE_SPACE=65
    ERROR_TOKEN=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.INTEGER_LITERAL)
            else:
                return self.getToken(D96Parser.INTEGER_LITERAL, i)

        def FLOAT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.FLOAT_LITERAL)
            else:
                return self.getToken(D96Parser.FLOAT_LITERAL, i)

        def BOOLEAN_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.BOOLEAN_LITERAL)
            else:
                return self.getToken(D96Parser.BOOLEAN_LITERAL, i)

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.STRING_LITERAL)
            else:
                return self.getToken(D96Parser.STRING_LITERAL, i)

        def getRuleIndex(self):
            return D96Parser.RULE_literal




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ARRAY(self):
            return self.getToken(D96Parser.K_ARRAY, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def FLOAT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.FLOAT_LITERAL)
            else:
                return self.getToken(D96Parser.FLOAT_LITERAL, i)

        def BOOLEAN_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.BOOLEAN_LITERAL)
            else:
                return self.getToken(D96Parser.BOOLEAN_LITERAL, i)

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.STRING_LITERAL)
            else:
                return self.getToken(D96Parser.STRING_LITERAL, i)

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.INTEGER_LITERAL)
            else:
                return self.getToken(D96Parser.INTEGER_LITERAL, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_indexed_array




    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(D96Parser.K_ARRAY)
            self.state = 120
            self.match(D96Parser.LEFT_PAREN)
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RIGHT_PAREN, D96Parser.INTEGER_LITERAL]:
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.INTEGER_LITERAL:
                    self.state = 121
                    self.match(D96Parser.INTEGER_LITERAL)
                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.COMMA:
                        self.state = 122
                        self.match(D96Parser.COMMA)
                        self.state = 123
                        self.match(D96Parser.INTEGER_LITERAL)
                        self.state = 128
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.state = 131
                self.match(D96Parser.FLOAT_LITERAL)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 132
                    self.match(D96Parser.COMMA)
                    self.state = 133
                    self.match(D96Parser.FLOAT_LITERAL)
                    self.state = 138
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.state = 139
                self.match(D96Parser.BOOLEAN_LITERAL)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 140
                    self.match(D96Parser.COMMA)
                    self.state = 141
                    self.match(D96Parser.BOOLEAN_LITERAL)
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.state = 147
                self.match(D96Parser.STRING_LITERAL)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 148
                    self.match(D96Parser.COMMA)
                    self.state = 149
                    self.match(D96Parser.STRING_LITERAL)
                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 157
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_dimentional_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ARRAY(self):
            return self.getToken(D96Parser.K_ARRAY, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def indexed_array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Indexed_arrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_multi_dimentional_array




    def multi_dimentional_array(self):

        localctx = D96Parser.Multi_dimentional_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_multi_dimentional_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(D96Parser.K_ARRAY)
            self.state = 160
            self.match(D96Parser.LEFT_PAREN)

            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ARRAY:
                self.state = 161
                self.indexed_array()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 162
                    self.match(D96Parser.COMMA)
                    self.state = 163
                    self.indexed_array()
                    self.state = 168
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 171
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_identifier




    def identifier(self):

        localctx = D96Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            _la = self._input.LA(1)
            if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
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


    class Operator_booleanContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_LOGICAL_NOT(self):
            return self.getToken(D96Parser.OP_LOGICAL_NOT, 0)

        def OP_LOGICAL_AND(self):
            return self.getToken(D96Parser.OP_LOGICAL_AND, 0)

        def OP_LOGICAL_OR(self):
            return self.getToken(D96Parser.OP_LOGICAL_OR, 0)

        def OP_IS_EQUAL_TO(self):
            return self.getToken(D96Parser.OP_IS_EQUAL_TO, 0)

        def OP_NOT_EQUAL_TO(self):
            return self.getToken(D96Parser.OP_NOT_EQUAL_TO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operator_boolean




    def operator_boolean(self):

        localctx = D96Parser.Operator_booleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operator_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_LOGICAL_OR) | (1 << D96Parser.OP_LOGICAL_AND) | (1 << D96Parser.OP_IS_EQUAL_TO) | (1 << D96Parser.OP_NOT_EQUAL_TO))) != 0)):
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


    class Operator_integerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_IS_EQUAL_TO(self):
            return self.getToken(D96Parser.OP_IS_EQUAL_TO, 0)

        def OP_NOT_EQUAL_TO(self):
            return self.getToken(D96Parser.OP_NOT_EQUAL_TO, 0)

        def OP_MODULO(self):
            return self.getToken(D96Parser.OP_MODULO, 0)

        def OP_ADDTION(self):
            return self.getToken(D96Parser.OP_ADDTION, 0)

        def OP_SUBTRACTION(self):
            return self.getToken(D96Parser.OP_SUBTRACTION, 0)

        def OP_MULTIPLICATION(self):
            return self.getToken(D96Parser.OP_MULTIPLICATION, 0)

        def OP_DIVISION(self):
            return self.getToken(D96Parser.OP_DIVISION, 0)

        def OP_LESS_THAN(self):
            return self.getToken(D96Parser.OP_LESS_THAN, 0)

        def OP_LESS_THAN_EQUAL(self):
            return self.getToken(D96Parser.OP_LESS_THAN_EQUAL, 0)

        def OP_GREATER_THAN(self):
            return self.getToken(D96Parser.OP_GREATER_THAN, 0)

        def OP_GREATER_THAN_EQUAL(self):
            return self.getToken(D96Parser.OP_GREATER_THAN_EQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operator_integer




    def operator_integer(self):

        localctx = D96Parser.Operator_integerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operator_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_IS_EQUAL_TO) | (1 << D96Parser.OP_NOT_EQUAL_TO) | (1 << D96Parser.OP_MODULO) | (1 << D96Parser.OP_ADDTION) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.OP_MULTIPLICATION) | (1 << D96Parser.OP_DIVISION) | (1 << D96Parser.OP_LESS_THAN) | (1 << D96Parser.OP_LESS_THAN_EQUAL) | (1 << D96Parser.OP_GREATER_THAN) | (1 << D96Parser.OP_GREATER_THAN_EQUAL))) != 0)):
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


    class Operator_floatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ADDTION(self):
            return self.getToken(D96Parser.OP_ADDTION, 0)

        def OP_SUBTRACTION(self):
            return self.getToken(D96Parser.OP_SUBTRACTION, 0)

        def OP_MULTIPLICATION(self):
            return self.getToken(D96Parser.OP_MULTIPLICATION, 0)

        def OP_DIVISION(self):
            return self.getToken(D96Parser.OP_DIVISION, 0)

        def OP_LESS_THAN(self):
            return self.getToken(D96Parser.OP_LESS_THAN, 0)

        def OP_LESS_THAN_EQUAL(self):
            return self.getToken(D96Parser.OP_LESS_THAN_EQUAL, 0)

        def OP_GREATER_THAN(self):
            return self.getToken(D96Parser.OP_GREATER_THAN, 0)

        def OP_GREATER_THAN_EQUAL(self):
            return self.getToken(D96Parser.OP_GREATER_THAN_EQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operator_float




    def operator_float(self):

        localctx = D96Parser.Operator_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operator_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_ADDTION) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.OP_MULTIPLICATION) | (1 << D96Parser.OP_DIVISION) | (1 << D96Parser.OP_LESS_THAN) | (1 << D96Parser.OP_LESS_THAN_EQUAL) | (1 << D96Parser.OP_GREATER_THAN) | (1 << D96Parser.OP_GREATER_THAN_EQUAL))) != 0)):
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


    class Operator_stringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_TWO_SAME_STRING(self):
            return self.getToken(D96Parser.OP_TWO_SAME_STRING, 0)

        def OP_STRING_CONCATENATION(self):
            return self.getToken(D96Parser.OP_STRING_CONCATENATION, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operator_string




    def operator_string(self):

        localctx = D96Parser.Operator_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operator_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            _la = self._input.LA(1)
            if not(_la==D96Parser.OP_STRING_CONCATENATION or _la==D96Parser.OP_TWO_SAME_STRING):
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


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_BOOLEAN(self):
            return self.getToken(D96Parser.K_BOOLEAN, 0)

        def K_INT(self):
            return self.getToken(D96Parser.K_INT, 0)

        def K_FLOAT(self):
            return self.getToken(D96Parser.K_FLOAT, 0)

        def K_STRING(self):
            return self.getToken(D96Parser.K_STRING, 0)

        def K_ARRAY(self):
            return self.getToken(D96Parser.K_ARRAY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_INT) | (1 << D96Parser.K_FLOAT) | (1 << D96Parser.K_BOOLEAN) | (1 << D96Parser.K_STRING))) != 0)):
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


    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ARRAY(self):
            return self.getToken(D96Parser.K_ARRAY, 0)

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.LEFT_SQUARE_BRACKET, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(D96Parser.K_ARRAY)
            self.state = 186
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 187
            self.primitive_type()
            self.state = 188
            self.match(D96Parser.COMMA)
            self.state = 189
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 190
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_NEW(self):
            return self.getToken(D96Parser.K_NEW, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_type




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(D96Parser.K_NEW)
            self.state = 193
            self.match(D96Parser.IDENTIFIER)
            self.state = 194
            self.match(D96Parser.LEFT_PAREN)
            self.state = 195
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def many_class(self):
            return self.getTypedRuleContext(D96Parser.Many_classContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.many_class()
            self.state = 198
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_classContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declarationContext,i)


        def program_class_declaration(self):
            return self.getTypedRuleContext(D96Parser.Program_class_declarationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_many_class




    def many_class(self):

        localctx = D96Parser.Many_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_many_class)
        self._la = 0 # Token type
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 200
                    self.class_declaration()
                    self.state = 203 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.K_CLASS):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 205
                        self.class_declaration() 
                    self.state = 210
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                self.state = 211
                self.program_class_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                self.program_class_declaration()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.K_CLASS:
                    self.state = 213
                    self.class_declaration()
                    self.state = 218
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                self.program_class_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_CLASS(self):
            return self.getToken(D96Parser.K_CLASS, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def super_class_group(self):
            return self.getTypedRuleContext(D96Parser.Super_class_groupContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(D96Parser.K_CLASS)
            self.state = 223
            self.match(D96Parser.IDENTIFIER)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 224
                self.super_class_group()


            self.state = 227
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 228
            self.class_body()
            self.state = 229
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_body_unit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_body_unitContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_body_unitContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.T__3) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 231
                self.class_body_unit()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_body_unitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(D96Parser.Method_declarationContext,0)


        def statement(self):
            return self.getTypedRuleContext(D96Parser.StatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body_unit




    def class_body_unit(self):

        localctx = D96Parser.Class_body_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_class_body_unit)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_VAL, D96Parser.K_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.attribute_declaration()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR, D96Parser.K_DESTRUCTOR, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.method_declaration()
                pass
            elif token in [D96Parser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.statement()
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


    class Super_class_groupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_super_class_group




    def super_class_group(self):

        localctx = D96Parser.Super_class_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_super_class_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(D96Parser.COLON)
            self.state = 243
            self.match(D96Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_class_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_CLASS(self):
            return self.getToken(D96Parser.K_CLASS, 0)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def program_class_body(self):
            return self.getTypedRuleContext(D96Parser.Program_class_bodyContext,0)


        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program_class_declaration




    def program_class_declaration(self):

        localctx = D96Parser.Program_class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_program_class_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(D96Parser.K_CLASS)
            self.state = 246
            self.match(D96Parser.T__0)
            self.state = 247
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 248
            self.program_class_body()
            self.state = 249
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_class_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_method_declaration(self):
            return self.getTypedRuleContext(D96Parser.Main_method_declarationContext,0)


        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_program_class_body




    def program_class_body(self):

        localctx = D96Parser.Program_class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_program_class_body)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.main_method_declaration()
                self.state = 252
                self.class_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.class_body()
                self.state = 255
                self.main_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_MAIN(self):
            return self.getToken(D96Parser.K_MAIN, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def method_body(self):
            return self.getTypedRuleContext(D96Parser.Method_bodyContext,0)


        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_main_method_declaration




    def main_method_declaration(self):

        localctx = D96Parser.Main_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_main_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(D96Parser.K_MAIN)
            self.state = 260
            self.match(D96Parser.LEFT_PAREN)
            self.state = 261
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 262
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 263
            self.method_body()
            self.state = 264
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def method_body(self):
            return self.getTypedRuleContext(D96Parser.Method_bodyContext,0)


        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_listContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_declaration




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(D96Parser.IDENTIFIER)
                self.state = 267
                self.match(D96Parser.LEFT_PAREN)
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 268
                    self.parameter_list()


                self.state = 271
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 272
                self.match(D96Parser.LEFT_CURLY_BRACKET)
                self.state = 273
                self.method_body()
                self.state = 274
                self.match(D96Parser.RIGHT_CURLY_BRACKET)
                pass
            elif token in [D96Parser.K_CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.constructor()
                pass
            elif token in [D96Parser.K_DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.destructor()
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


    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_CONSTRUCTOR(self):
            return self.getToken(D96Parser.K_CONSTRUCTOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def method_body(self):
            return self.getTypedRuleContext(D96Parser.Method_bodyContext,0)


        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(D96Parser.K_CONSTRUCTOR)
            self.state = 281
            self.match(D96Parser.LEFT_PAREN)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDENTIFIER:
                self.state = 282
                self.parameter_list()


            self.state = 285
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 286
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 287
            self.method_body()
            self.state = 288
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_DESTRUCTOR(self):
            return self.getToken(D96Parser.K_DESTRUCTOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def method_body(self):
            return self.getTypedRuleContext(D96Parser.Method_bodyContext,0)


        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_destructor




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(D96Parser.K_DESTRUCTOR)
            self.state = 291
            self.match(D96Parser.LEFT_PAREN)
            self.state = 292
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 293
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 294
            self.method_body()
            self.state = 295
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(D96Parser.ParameterContext,0)


        def parameter_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Parameter_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameter_list




    def parameter_list(self):

        localctx = D96Parser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_parameter_list)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.parameter()
                self.state = 299
                self.parameter_list_tail()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_list_tailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI_COLON)
            else:
                return self.getToken(D96Parser.SEMI_COLON, i)

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ParameterContext)
            else:
                return self.getTypedRuleContext(D96Parser.ParameterContext,i)


        def parameter_list_tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Parameter_list_tailContext)
            else:
                return self.getTypedRuleContext(D96Parser.Parameter_list_tailContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_parameter_list_tail




    def parameter_list_tail(self):

        localctx = D96Parser.Parameter_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_parameter_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 303
                    self.match(D96Parser.SEMI_COLON)
                    self.state = 304
                    self.parameter()
                    self.state = 305
                    self.parameter_list_tail() 
                self.state = 311
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameter




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.identifier_list()
            self.state = 313
            self.match(D96Parser.COLON)
            self.state = 314
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_method_body




    def method_body(self):

        localctx = D96Parser.Method_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_method_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(D96Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def dolar_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Dolar_identifier_listContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declaration




    def attribute_declaration(self):

        localctx = D96Parser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER]:
                self.state = 319
                self.identifier_list()
                pass
            elif token in [D96Parser.DOLAR_IDENTIFIER]:
                self.state = 320
                self.dolar_identifier_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 323
            self.match(D96Parser.COLON)
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 324
                self.array_type()
                pass

            elif la_ == 2:
                self.state = 325
                self.primitive_type()
                pass


            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 328
                self.match(D96Parser.OP_ASSIGN)
                self.state = 329
                self.expression_list()


            self.state = 332
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def identifier_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Identifier_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_identifier_list




    def identifier_list(self):

        localctx = D96Parser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_identifier_list)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(D96Parser.IDENTIFIER)
                self.state = 336
                self.identifier_list_tail()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dolar_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def dolar_identifier_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Dolar_identifier_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_dolar_identifier_list




    def dolar_identifier_list(self):

        localctx = D96Parser.Dolar_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_dolar_identifier_list)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 341
                self.dolar_identifier_list_tail()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_list_tailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

        def getRuleIndex(self):
            return D96Parser.RULE_identifier_list_tail




    def identifier_list_tail(self):

        localctx = D96Parser.Identifier_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_identifier_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 344
                self.match(D96Parser.COMMA)
                self.state = 345
                self.match(D96Parser.IDENTIFIER)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dolar_identifier_list_tailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def DOLAR_IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLAR_IDENTIFIER)
            else:
                return self.getToken(D96Parser.DOLAR_IDENTIFIER, i)

        def getRuleIndex(self):
            return D96Parser.RULE_dolar_identifier_list_tail




    def dolar_identifier_list_tail(self):

        localctx = D96Parser.Dolar_identifier_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_dolar_identifier_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 351
                self.match(D96Parser.COMMA)
                self.state = 352
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def expression_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Expression_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression_list




    def expression_list(self):

        localctx = D96Parser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression_list)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.expression()
                self.state = 360
                self.expression_list_tail()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_list_tailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def expression_list_tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expression_list_tailContext)
            else:
                return self.getTypedRuleContext(D96Parser.Expression_list_tailContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_expression_list_tail




    def expression_list_tail(self):

        localctx = D96Parser.Expression_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expression_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 364
                    self.match(D96Parser.COMMA)
                    self.state = 365
                    self.expression()
                    self.state = 366
                    self.expression_list_tail() 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_expression




    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(D96Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_expression




    def element_expression(self):

        localctx = D96Parser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.expression()
            self.state = 376
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.LEFT_SQUARE_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_SQUARE_BRACKET, 0)

        def index_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Index_operatorContext)
            else:
                return self.getTypedRuleContext(D96Parser.Index_operatorContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operator




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 379
            self.expression()
            self.state = 380
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 381
                    self.index_operator() 
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_attribute_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attribute_access




    def instance_attribute_access(self):

        localctx = D96Parser.Instance_attribute_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_instance_attribute_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(D96Parser.IDENTIFIER)
            self.state = 388
            self.match(D96Parser.DOT)
            self.state = 389
            self.match(D96Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_attribute_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attribute_access




    def static_attribute_access(self):

        localctx = D96Parser.Static_attribute_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_static_attribute_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(D96Parser.IDENTIFIER)
            self.state = 392
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 393
            self.match(D96Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instace_method_invocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instace_method_invocation




    def instace_method_invocation(self):

        localctx = D96Parser.Instace_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_instace_method_invocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(D96Parser.IDENTIFIER)
            self.state = 396
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 397
            self.match(D96Parser.IDENTIFIER)
            self.state = 398
            self.match(D96Parser.LEFT_PAREN)
            self.state = 399
            self.expression_list()
            self.state = 400
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_creationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_NEW(self):
            return self.getToken(D96Parser.K_NEW, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_object_creation




    def object_creation(self):

        localctx = D96Parser.Object_creationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_object_creation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(D96Parser.K_NEW)
            self.state = 403
            self.match(D96Parser.IDENTIFIER)
            self.state = 404
            self.match(D96Parser.LEFT_PAREN)
            self.state = 405
            self.expression_list()
            self.state = 406
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def exprList(self):
            return self.getTypedRuleContext(D96Parser.ExprListContext,0)


        def OP_SUBTRACTION(self):
            return self.getToken(D96Parser.OP_SUBTRACTION, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def OP_LOGICAL_NOT(self):
            return self.getToken(D96Parser.OP_LOGICAL_NOT, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def OP_MULTIPLICATION(self):
            return self.getToken(D96Parser.OP_MULTIPLICATION, 0)

        def OP_ADDTION(self):
            return self.getToken(D96Parser.OP_ADDTION, 0)

        def OP_IS_EQUAL_TO(self):
            return self.getToken(D96Parser.OP_IS_EQUAL_TO, 0)

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.LEFT_SQUARE_BRACKET, 0)

        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 409
                self.match(D96Parser.IDENTIFIER)
                self.state = 410
                self.match(D96Parser.LEFT_PAREN)
                self.state = 412
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 411
                    self.exprList()


                self.state = 414
                self.match(D96Parser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.state = 415
                self.match(D96Parser.OP_SUBTRACTION)
                self.state = 416
                self.expr(8)
                pass

            elif la_ == 3:
                self.state = 417
                self.match(D96Parser.OP_LOGICAL_NOT)
                self.state = 418
                self.expr(7)
                pass

            elif la_ == 4:
                self.state = 419
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.state = 420
                self.match(D96Parser.INTEGER_LITERAL)
                pass

            elif la_ == 6:
                self.state = 421
                self.match(D96Parser.LEFT_PAREN)
                self.state = 422
                self.expr(0)
                self.state = 423
                self.match(D96Parser.RIGHT_PAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 443
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 441
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 427
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 428
                        self.match(D96Parser.OP_MULTIPLICATION)
                        self.state = 429
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 430
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 431
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.OP_ADDTION or _la==D96Parser.OP_SUBTRACTION):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 432
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 433
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 434
                        self.match(D96Parser.OP_IS_EQUAL_TO)
                        self.state = 435
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 436
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 437
                        self.match(D96Parser.LEFT_SQUARE_BRACKET)
                        self.state = 438
                        self.expr(0)
                        self.state = 439
                        self.match(D96Parser.RIGHT_SQUARE_BRACKET)
                        pass

             
                self.state = 445
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_exprList




    def exprList(self):

        localctx = D96Parser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.expr(0)
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 447
                self.match(D96Parser.COMMA)
                self.state = 448
                self.expr(0)
                self.state = 453
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_val_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_val_statement




    def var_val_statement(self):

        localctx = D96Parser.Var_val_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_var_val_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 455
            self.identifier_list()
            self.state = 456
            self.match(D96Parser.COLON)
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 457
                self.array_type()
                pass

            elif la_ == 2:
                self.state = 458
                self.primitive_type()
                pass


            self.state = 463
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 461
                self.match(D96Parser.OP_ASSIGN)
                self.state = 462
                self.expression_list()


            self.state = 465
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def element_expression(self):
            return self.getTypedRuleContext(D96Parser.Element_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_statement




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.state = 467
                self.identifier()
                pass
            elif token in [D96Parser.T__2]:
                self.state = 468
                self.element_expression()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 471
            self.match(D96Parser.OP_ASSIGN)
            self.state = 472
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_part(self):
            return self.getTypedRuleContext(D96Parser.If_partContext,0)


        def else_if_part(self):
            return self.getTypedRuleContext(D96Parser.Else_if_partContext,0)


        def else_part(self):
            return self.getTypedRuleContext(D96Parser.Else_partContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statement




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.if_part()
            self.state = 475
            self.else_if_part()
            self.state = 476
            self.else_part()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_IF(self):
            return self.getToken(D96Parser.K_IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_part




    def if_part(self):

        localctx = D96Parser.If_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(D96Parser.K_IF)
            self.state = 479
            self.match(D96Parser.LEFT_PAREN)
            self.state = 480
            self.expression()
            self.state = 481
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 482
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ELSE_IF(self):
            return self.getToken(D96Parser.K_ELSE_IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def else_if_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Else_if_partContext)
            else:
                return self.getTypedRuleContext(D96Parser.Else_if_partContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_else_if_part




    def else_if_part(self):

        localctx = D96Parser.Else_if_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_else_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(D96Parser.K_ELSE_IF)
            self.state = 485
            self.match(D96Parser.LEFT_PAREN)
            self.state = 486
            self.expression()
            self.state = 487
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 488
            self.block_statement()
            self.state = 493
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 490
                    self.else_if_part() 
                self.state = 495
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ELSE(self):
            return self.getToken(D96Parser.K_ELSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_part




    def else_part(self):

        localctx = D96Parser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_else_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ELSE:
                self.state = 496
                self.match(D96Parser.K_ELSE)
                self.state = 497
                self.block_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_FOR_EACH(self):
            return self.getToken(D96Parser.K_FOR_EACH, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def loop_part(self):
            return self.getTypedRuleContext(D96Parser.Loop_partContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_for_in_statement




    def for_in_statement(self):

        localctx = D96Parser.For_in_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_for_in_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(D96Parser.K_FOR_EACH)
            self.state = 501
            self.match(D96Parser.LEFT_PAREN)
            self.state = 502
            self.loop_part()
            self.state = 503
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 504
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def K_IN(self):
            return self.getToken(D96Parser.K_IN, 0)

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.INTEGER_LITERAL)
            else:
                return self.getToken(D96Parser.INTEGER_LITERAL, i)

        def DOUBLE_DOT(self):
            return self.getToken(D96Parser.DOUBLE_DOT, 0)

        def K_BY(self):
            return self.getToken(D96Parser.K_BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_loop_part




    def loop_part(self):

        localctx = D96Parser.Loop_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_loop_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(D96Parser.IDENTIFIER)
            self.state = 507
            self.match(D96Parser.K_IN)
            self.state = 508
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 509
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 510
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_BY:
                self.state = 511
                self.match(D96Parser.K_BY)
                self.state = 512
                self.match(D96Parser.INTEGER_LITERAL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_BREAK(self):
            return self.getToken(D96Parser.K_BREAK, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(D96Parser.K_BREAK)
            self.state = 516
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_CONTINUE(self):
            return self.getToken(D96Parser.K_CONTINUE, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(D96Parser.K_CONTINUE)
            self.state = 519
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_RETURN(self):
            return self.getToken(D96Parser.K_RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_return_statement




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(D96Parser.K_RETURN)
            self.state = 522
            self.expression()
            self.state = 523
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_statement




    def method_invocation_statement(self):

        localctx = D96Parser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.match(D96Parser.IDENTIFIER)
            self.state = 526
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 527
            self.match(D96Parser.DOLAR_IDENTIFIER)
            self.state = 528
            self.match(D96Parser.LEFT_PAREN)
            self.state = 529
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 530
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def statement(self):
            return self.getTypedRuleContext(D96Parser.StatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_block_statement




    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__3:
                self.state = 533
                self.statement()


            self.state = 536
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_statement




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(D96Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[41] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         




