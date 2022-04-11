# Generated from C:/development-area/ppl/ppl-course/assignment/assignment1/assigment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u025a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\3")
        buf.write("\2\3\2\3\3\6\3y\n\3\r\3\16\3z\3\3\7\3~\n\3\f\3\16\3\u0081")
        buf.write("\13\3\3\3\3\3\3\3\7\3\u0086\n\3\f\3\16\3\u0089\13\3\3")
        buf.write("\3\5\3\u008c\n\3\3\4\3\4\3\4\5\4\u0091\n\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\7\5\u0098\n\5\f\5\16\5\u009b\13\5\3\6\3\6\5\6")
        buf.write("\u009f\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\5\t\u00b0\n\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\5\13\u00ba\n\13\3\13\3\13\3\13\3\13\3\13\5")
        buf.write("\13\u00c1\n\13\3\f\3\f\3\f\5\f\u00c6\n\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\6\16\u00d4\n\16")
        buf.write("\r\16\16\16\u00d5\5\16\u00d8\n\16\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\5\20\u00e1\n\20\3\20\3\20\3\20\3\20\5")
        buf.write("\20\u00e7\n\20\3\20\3\20\5\20\u00eb\n\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\6\21\u00f3\n\21\r\21\16\21\u00f4\5\21")
        buf.write("\u00f7\n\21\3\22\3\22\3\22\3\22\6\22\u00fd\n\22\r\22\16")
        buf.write("\22\u00fe\5\22\u0101\n\22\3\23\3\23\3\23\3\23\7\23\u0107")
        buf.write("\n\23\f\23\16\23\u010a\13\23\5\23\u010c\n\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\7\25\u0115\n\25\f\25\16\25\u0118")
        buf.write("\13\25\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0122")
        buf.write("\n\27\f\27\16\27\u0125\13\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\7\30\u012e\n\30\f\30\16\30\u0131\13\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\7\31\u0139\n\31\f\31\16\31\u013c")
        buf.write("\13\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0144\n\32\f")
        buf.write("\32\16\32\u0147\13\32\3\33\3\33\3\33\3\33\3\33\3\33\7")
        buf.write("\33\u014f\n\33\f\33\16\33\u0152\13\33\3\34\3\34\3\34\5")
        buf.write("\34\u0157\n\34\3\35\3\35\3\35\5\35\u015c\n\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\7\36\u0163\n\36\f\36\16\36\u0166\13\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u016e\n\37\f\37\16")
        buf.write("\37\u0171\13\37\3 \3 \3 \3 \3 \3 \3 \3 \5 \u017b\n \3")
        buf.write(" \7 \u017e\n \f \16 \u0181\13 \3!\3!\3!\3!\5!\u0187\n")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\5#\u0193\n#\3#\3#")
        buf.write("\5#\u0197\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u01a2\n$\3")
        buf.write("%\3%\3%\5%\u01a7\n%\3%\3%\3&\3&\3&\3&\3&\5&\u01b0\n&\3")
        buf.write("&\3&\5&\u01b4\n&\3&\3&\3\'\3\'\5\'\u01ba\n\'\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\7(\u01c2\n(\f(\16(\u01c5\13(\3(\5(\u01c8")
        buf.write("\n(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\5-\u01e6\n-\3.\3.\3")
        buf.write(".\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\7\62\u01fb\n\62\f\62\16\62\u01fe")
        buf.write("\13\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\5\63\u020a\n\63\3\64\3\64\3\64\3\64\3\64\3\64\5\64")
        buf.write("\u0212\n\64\3\65\3\65\3\65\3\65\3\65\7\65\u0219\n\65\f")
        buf.write("\65\16\65\u021c\13\65\5\65\u021e\n\65\3\65\3\65\3\65\7")
        buf.write("\65\u0223\n\65\f\65\16\65\u0226\13\65\3\65\3\65\3\65\7")
        buf.write("\65\u022b\n\65\f\65\16\65\u022e\13\65\3\65\3\65\3\65\7")
        buf.write("\65\u0233\n\65\f\65\16\65\u0236\13\65\5\65\u0238\n\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\7\66\u0241\n\66\f")
        buf.write("\66\16\66\u0244\13\66\5\66\u0246\n\66\3\66\3\66\3\67\3")
        buf.write("\67\38\38\39\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\2\n,")
        buf.write(".\60\62\64:<>;\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnpr\2")
        buf.write("\n\3\2\25\26\4\2!\"(+\3\2,-\3\2\37 \3\2$%\4\2##&\'\3\2")
        buf.write(">?\4\2\f\f\16\21\2\u026c\2t\3\2\2\2\4\u008b\3\2\2\2\6")
        buf.write("\u008d\3\2\2\2\b\u0099\3\2\2\2\n\u009e\3\2\2\2\f\u00a0")
        buf.write("\3\2\2\2\16\u00a3\3\2\2\2\20\u00af\3\2\2\2\22\u00b1\3")
        buf.write("\2\2\2\24\u00c0\3\2\2\2\26\u00c2\3\2\2\2\30\u00ca\3\2")
        buf.write("\2\2\32\u00d7\3\2\2\2\34\u00d9\3\2\2\2\36\u00dd\3\2\2")
        buf.write("\2 \u00f6\3\2\2\2\"\u0100\3\2\2\2$\u010b\3\2\2\2&\u010d")
        buf.write("\3\2\2\2(\u0110\3\2\2\2*\u0119\3\2\2\2,\u011b\3\2\2\2")
        buf.write(".\u0126\3\2\2\2\60\u0132\3\2\2\2\62\u013d\3\2\2\2\64\u0148")
        buf.write("\3\2\2\2\66\u0156\3\2\2\28\u015b\3\2\2\2:\u015d\3\2\2")
        buf.write("\2<\u0167\3\2\2\2>\u0172\3\2\2\2@\u0182\3\2\2\2B\u018a")
        buf.write("\3\2\2\2D\u0196\3\2\2\2F\u01a1\3\2\2\2H\u01a3\3\2\2\2")
        buf.write("J\u01aa\3\2\2\2L\u01b9\3\2\2\2N\u01bf\3\2\2\2P\u01c9\3")
        buf.write("\2\2\2R\u01cf\3\2\2\2T\u01d5\3\2\2\2V\u01d8\3\2\2\2X\u01de")
        buf.write("\3\2\2\2Z\u01e7\3\2\2\2\\\u01ea\3\2\2\2^\u01ed\3\2\2\2")
        buf.write("`\u01f1\3\2\2\2b\u01f8\3\2\2\2d\u0209\3\2\2\2f\u0211\3")
        buf.write("\2\2\2h\u0213\3\2\2\2j\u023b\3\2\2\2l\u0249\3\2\2\2n\u024b")
        buf.write("\3\2\2\2p\u024d\3\2\2\2r\u0254\3\2\2\2tu\5\4\3\2uv\7\2")
        buf.write("\2\3v\3\3\2\2\2wy\5\6\4\2xw\3\2\2\2yz\3\2\2\2zx\3\2\2")
        buf.write("\2z{\3\2\2\2{\u008c\3\2\2\2|~\5\6\4\2}|\3\2\2\2~\u0081")
        buf.write("\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\3")
        buf.write("\2\2\2\u0081\177\3\2\2\2\u0082\u008c\5\16\b\2\u0083\u0087")
        buf.write("\5\16\b\2\u0084\u0086\5\6\4\2\u0085\u0084\3\2\2\2\u0086")
        buf.write("\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u008c\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008c\5")
        buf.write("\16\b\2\u008bx\3\2\2\2\u008b\177\3\2\2\2\u008b\u0083\3")
        buf.write("\2\2\2\u008b\u008a\3\2\2\2\u008c\5\3\2\2\2\u008d\u008e")
        buf.write("\7\24\2\2\u008e\u0090\7>\2\2\u008f\u0091\5\f\7\2\u0090")
        buf.write("\u008f\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\u0093\78\2\2\u0093\u0094\5\b\5\2\u0094\u0095\7")
        buf.write("9\2\2\u0095\7\3\2\2\2\u0096\u0098\5\n\6\2\u0097\u0096")
        buf.write("\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\t\3\2\2\2\u009b\u0099\3\2\2\2\u009c")
        buf.write("\u009f\5\36\20\2\u009d\u009f\5\24\13\2\u009e\u009c\3\2")
        buf.write("\2\2\u009e\u009d\3\2\2\2\u009f\13\3\2\2\2\u00a0\u00a1")
        buf.write("\7\65\2\2\u00a1\u00a2\7>\2\2\u00a2\r\3\2\2\2\u00a3\u00a4")
        buf.write("\7\24\2\2\u00a4\u00a5\7\3\2\2\u00a5\u00a6\78\2\2\u00a6")
        buf.write("\u00a7\5\20\t\2\u00a7\u00a8\79\2\2\u00a8\17\3\2\2\2\u00a9")
        buf.write("\u00aa\5\22\n\2\u00aa\u00ab\5\b\5\2\u00ab\u00b0\3\2\2")
        buf.write("\2\u00ac\u00ad\5\b\5\2\u00ad\u00ae\5\22\n\2\u00ae\u00b0")
        buf.write("\3\2\2\2\u00af\u00a9\3\2\2\2\u00af\u00ac\3\2\2\2\u00b0")
        buf.write("\21\3\2\2\2\u00b1\u00b2\7\33\2\2\u00b2\u00b3\7.\2\2\u00b3")
        buf.write("\u00b4\7/\2\2\u00b4\u00b5\5b\62\2\u00b5\23\3\2\2\2\u00b6")
        buf.write("\u00b7\5l\67\2\u00b7\u00b9\7.\2\2\u00b8\u00ba\5\32\16")
        buf.write("\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00bc\7/\2\2\u00bc\u00bd\5b\62\2\u00bd")
        buf.write("\u00c1\3\2\2\2\u00be\u00c1\5\26\f\2\u00bf\u00c1\5\30\r")
        buf.write("\2\u00c0\u00b6\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00bf")
        buf.write("\3\2\2\2\u00c1\25\3\2\2\2\u00c2\u00c3\7\27\2\2\u00c3\u00c5")
        buf.write("\7.\2\2\u00c4\u00c6\5\32\16\2\u00c5\u00c4\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\7/\2\2")
        buf.write("\u00c8\u00c9\5b\62\2\u00c9\27\3\2\2\2\u00ca\u00cb\7\30")
        buf.write("\2\2\u00cb\u00cc\7.\2\2\u00cc\u00cd\7/\2\2\u00cd\u00ce")
        buf.write("\5b\62\2\u00ce\31\3\2\2\2\u00cf\u00d8\5\34\17\2\u00d0")
        buf.write("\u00d3\5\34\17\2\u00d1\u00d2\7\67\2\2\u00d2\u00d4\5\34")
        buf.write("\17\2\u00d3\u00d1\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d3")
        buf.write("\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7")
        buf.write("\u00cf\3\2\2\2\u00d7\u00d0\3\2\2\2\u00d8\33\3\2\2\2\u00d9")
        buf.write("\u00da\5 \21\2\u00da\u00db\7\65\2\2\u00db\u00dc\5n8\2")
        buf.write("\u00dc\35\3\2\2\2\u00dd\u00e0\t\2\2\2\u00de\u00e1\5 \21")
        buf.write("\2\u00df\u00e1\5\"\22\2\u00e0\u00de\3\2\2\2\u00e0\u00df")
        buf.write("\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e6\7\65\2\2\u00e3")
        buf.write("\u00e7\5p9\2\u00e4\u00e7\5n8\2\u00e5\u00e7\5l\67\2\u00e6")
        buf.write("\u00e3\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2")
        buf.write("\u00e7\u00ea\3\2\2\2\u00e8\u00e9\7\35\2\2\u00e9\u00eb")
        buf.write("\5$\23\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec\u00ed\7\67\2\2\u00ed\37\3\2\2\2\u00ee")
        buf.write("\u00f7\7>\2\2\u00ef\u00f2\7>\2\2\u00f0\u00f1\7\64\2\2")
        buf.write("\u00f1\u00f3\7>\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f4\3")
        buf.write("\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7")
        buf.write("\3\2\2\2\u00f6\u00ee\3\2\2\2\u00f6\u00ef\3\2\2\2\u00f7")
        buf.write("!\3\2\2\2\u00f8\u0101\7?\2\2\u00f9\u00fc\7?\2\2\u00fa")
        buf.write("\u00fb\7\64\2\2\u00fb\u00fd\7?\2\2\u00fc\u00fa\3\2\2\2")
        buf.write("\u00fd\u00fe\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3")
        buf.write("\2\2\2\u00ff\u0101\3\2\2\2\u0100\u00f8\3\2\2\2\u0100\u00f9")
        buf.write("\3\2\2\2\u0101#\3\2\2\2\u0102\u010c\5,\27\2\u0103\u0108")
        buf.write("\5,\27\2\u0104\u0105\7\64\2\2\u0105\u0107\5,\27\2\u0106")
        buf.write("\u0104\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2")
        buf.write("\u0108\u0109\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3")
        buf.write("\2\2\2\u010b\u0102\3\2\2\2\u010b\u0103\3\2\2\2\u010c%")
        buf.write("\3\2\2\2\u010d\u010e\5,\27\2\u010e\u010f\5(\25\2\u010f")
        buf.write("\'\3\2\2\2\u0110\u0111\7\60\2\2\u0111\u0112\5,\27\2\u0112")
        buf.write("\u0116\7\61\2\2\u0113\u0115\5(\25\2\u0114\u0113\3\2\2")
        buf.write("\2\u0115\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117")
        buf.write("\3\2\2\2\u0117)\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a")
        buf.write("\t\3\2\2\u011a+\3\2\2\2\u011b\u011c\b\27\1\2\u011c\u011d")
        buf.write("\5.\30\2\u011d\u0123\3\2\2\2\u011e\u011f\f\4\2\2\u011f")
        buf.write("\u0120\t\4\2\2\u0120\u0122\5.\30\2\u0121\u011e\3\2\2\2")
        buf.write("\u0122\u0125\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3")
        buf.write("\2\2\2\u0124-\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0127")
        buf.write("\b\30\1\2\u0127\u0128\5\60\31\2\u0128\u012f\3\2\2\2\u0129")
        buf.write("\u012a\f\4\2\2\u012a\u012b\5*\26\2\u012b\u012c\5\60\31")
        buf.write("\2\u012c\u012e\3\2\2\2\u012d\u0129\3\2\2\2\u012e\u0131")
        buf.write("\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130")
        buf.write("/\3\2\2\2\u0131\u012f\3\2\2\2\u0132\u0133\b\31\1\2\u0133")
        buf.write("\u0134\5\62\32\2\u0134\u013a\3\2\2\2\u0135\u0136\f\4\2")
        buf.write("\2\u0136\u0137\t\5\2\2\u0137\u0139\5\62\32\2\u0138\u0135")
        buf.write("\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\61\3\2\2\2\u013c\u013a\3\2\2\2\u013d")
        buf.write("\u013e\b\32\1\2\u013e\u013f\5\64\33\2\u013f\u0145\3\2")
        buf.write("\2\2\u0140\u0141\f\4\2\2\u0141\u0142\t\6\2\2\u0142\u0144")
        buf.write("\5\64\33\2\u0143\u0140\3\2\2\2\u0144\u0147\3\2\2\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\63\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0148\u0149\b\33\1\2\u0149\u014a\5\66\34")
        buf.write("\2\u014a\u0150\3\2\2\2\u014b\u014c\f\4\2\2\u014c\u014d")
        buf.write("\t\7\2\2\u014d\u014f\5\66\34\2\u014e\u014b\3\2\2\2\u014f")
        buf.write("\u0152\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151\65\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0154\7\36")
        buf.write("\2\2\u0154\u0157\5\66\34\2\u0155\u0157\58\35\2\u0156\u0153")
        buf.write("\3\2\2\2\u0156\u0155\3\2\2\2\u0157\67\3\2\2\2\u0158\u0159")
        buf.write("\7%\2\2\u0159\u015c\58\35\2\u015a\u015c\5:\36\2\u015b")
        buf.write("\u0158\3\2\2\2\u015b\u015a\3\2\2\2\u015c9\3\2\2\2\u015d")
        buf.write("\u015e\b\36\1\2\u015e\u015f\5<\37\2\u015f\u0164\3\2\2")
        buf.write("\2\u0160\u0161\f\4\2\2\u0161\u0163\5(\25\2\u0162\u0160")
        buf.write("\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164")
        buf.write("\u0165\3\2\2\2\u0165;\3\2\2\2\u0166\u0164\3\2\2\2\u0167")
        buf.write("\u0168\b\37\1\2\u0168\u0169\5> \2\u0169\u016f\3\2\2\2")
        buf.write("\u016a\u016b\f\4\2\2\u016b\u016c\7\62\2\2\u016c\u016e")
        buf.write("\7>\2\2\u016d\u016a\3\2\2\2\u016e\u0171\3\2\2\2\u016f")
        buf.write("\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170=\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0172\u0173\b \1\2\u0173\u0174\5D#\2\u0174")
        buf.write("\u017f\3\2\2\2\u0175\u0176\f\4\2\2\u0176\u0177\7\66\2")
        buf.write("\2\u0177\u0178\7>\2\2\u0178\u017a\7.\2\2\u0179\u017b\5")
        buf.write("$\23\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c")
        buf.write("\3\2\2\2\u017c\u017e\7/\2\2\u017d\u0175\3\2\2\2\u017e")
        buf.write("\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180?\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0183\7>\2\2")
        buf.write("\u0183\u0184\7\66\2\2\u0184\u0186\7.\2\2\u0185\u0187\5")
        buf.write("$\23\2\u0186\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u0188\u0189\7/\2\2\u0189A\3\2\2\2\u018a\u018b")
        buf.write("\7>\2\2\u018b\u018c\7\66\2\2\u018c\u018d\7>\2\2\u018d")
        buf.write("C\3\2\2\2\u018e\u018f\7\31\2\2\u018f\u0190\7>\2\2\u0190")
        buf.write("\u0192\7.\2\2\u0191\u0193\5$\23\2\u0192\u0191\3\2\2\2")
        buf.write("\u0192\u0193\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0197\7")
        buf.write("/\2\2\u0195\u0197\5F$\2\u0196\u018e\3\2\2\2\u0196\u0195")
        buf.write("\3\2\2\2\u0197E\3\2\2\2\u0198\u01a2\5f\64\2\u0199\u01a2")
        buf.write("\7>\2\2\u019a\u019b\7.\2\2\u019b\u019c\5,\27\2\u019c\u019d")
        buf.write("\7/\2\2\u019d\u01a2\3\2\2\2\u019e\u01a2\5H%\2\u019f\u01a2")
        buf.write("\5@!\2\u01a0\u01a2\5B\"\2\u01a1\u0198\3\2\2\2\u01a1\u0199")
        buf.write("\3\2\2\2\u01a1\u019a\3\2\2\2\u01a1\u019e\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2G\3\2\2\2\u01a3")
        buf.write("\u01a4\7>\2\2\u01a4\u01a6\7.\2\2\u01a5\u01a7\5$\23\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\3\2\2\2")
        buf.write("\u01a8\u01a9\7/\2\2\u01a9I\3\2\2\2\u01aa\u01ab\t\2\2\2")
        buf.write("\u01ab\u01ac\5 \21\2\u01ac\u01af\7\65\2\2\u01ad\u01b0")
        buf.write("\5p9\2\u01ae\u01b0\5n8\2\u01af\u01ad\3\2\2\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01b2\7\35\2\2\u01b2")
        buf.write("\u01b4\5$\23\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2")
        buf.write("\u01b4\u01b5\3\2\2\2\u01b5\u01b6\7\67\2\2\u01b6K\3\2\2")
        buf.write("\2\u01b7\u01ba\5l\67\2\u01b8\u01ba\5&\24\2\u01b9\u01b7")
        buf.write("\3\2\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write("\u01bc\7\35\2\2\u01bc\u01bd\5,\27\2\u01bd\u01be\7\67\2")
        buf.write("\2\u01beM\3\2\2\2\u01bf\u01c3\5P)\2\u01c0\u01c2\5R*\2")
        buf.write("\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3")
        buf.write("\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3")
        buf.write("\3\2\2\2\u01c6\u01c8\5T+\2\u01c7\u01c6\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8O\3\2\2\2\u01c9\u01ca\7\b\2\2\u01ca\u01cb")
        buf.write("\7.\2\2\u01cb\u01cc\5,\27\2\u01cc\u01cd\7/\2\2\u01cd\u01ce")
        buf.write("\5b\62\2\u01ceQ\3\2\2\2\u01cf\u01d0\7\t\2\2\u01d0\u01d1")
        buf.write("\7.\2\2\u01d1\u01d2\5,\27\2\u01d2\u01d3\7/\2\2\u01d3\u01d4")
        buf.write("\5b\62\2\u01d4S\3\2\2\2\u01d5\u01d6\7\n\2\2\u01d6\u01d7")
        buf.write("\5b\62\2\u01d7U\3\2\2\2\u01d8\u01d9\7\13\2\2\u01d9\u01da")
        buf.write("\7.\2\2\u01da\u01db\5X-\2\u01db\u01dc\7/\2\2\u01dc\u01dd")
        buf.write("\5b\62\2\u01ddW\3\2\2\2\u01de\u01df\7>\2\2\u01df\u01e0")
        buf.write("\7\r\2\2\u01e0\u01e1\7:\2\2\u01e1\u01e2\7\63\2\2\u01e2")
        buf.write("\u01e5\7:\2\2\u01e3\u01e4\7\32\2\2\u01e4\u01e6\7:\2\2")
        buf.write("\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6Y\3\2\2")
        buf.write("\2\u01e7\u01e8\7\6\2\2\u01e8\u01e9\7\67\2\2\u01e9[\3\2")
        buf.write("\2\2\u01ea\u01eb\7\7\2\2\u01eb\u01ec\7\67\2\2\u01ec]\3")
        buf.write("\2\2\2\u01ed\u01ee\7\22\2\2\u01ee\u01ef\5,\27\2\u01ef")
        buf.write("\u01f0\7\67\2\2\u01f0_\3\2\2\2\u01f1\u01f2\7>\2\2\u01f2")
        buf.write("\u01f3\7\66\2\2\u01f3\u01f4\7?\2\2\u01f4\u01f5\7.\2\2")
        buf.write("\u01f5\u01f6\7/\2\2\u01f6\u01f7\7\67\2\2\u01f7a\3\2\2")
        buf.write("\2\u01f8\u01fc\78\2\2\u01f9\u01fb\5d\63\2\u01fa\u01f9")
        buf.write("\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc")
        buf.write("\u01fd\3\2\2\2\u01fd\u01ff\3\2\2\2\u01fe\u01fc\3\2\2\2")
        buf.write("\u01ff\u0200\79\2\2\u0200c\3\2\2\2\u0201\u020a\5J&\2\u0202")
        buf.write("\u020a\5L\'\2\u0203\u020a\5N(\2\u0204\u020a\5V,\2\u0205")
        buf.write("\u020a\5Z.\2\u0206\u020a\5\\/\2\u0207\u020a\5^\60\2\u0208")
        buf.write("\u020a\5`\61\2\u0209\u0201\3\2\2\2\u0209\u0202\3\2\2\2")
        buf.write("\u0209\u0203\3\2\2\2\u0209\u0204\3\2\2\2\u0209\u0205\3")
        buf.write("\2\2\2\u0209\u0206\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u0208")
        buf.write("\3\2\2\2\u020ae\3\2\2\2\u020b\u0212\7:\2\2\u020c\u0212")
        buf.write("\7;\2\2\u020d\u0212\7<\2\2\u020e\u0212\7=\2\2\u020f\u0212")
        buf.write("\5h\65\2\u0210\u0212\5j\66\2\u0211\u020b\3\2\2\2\u0211")
        buf.write("\u020c\3\2\2\2\u0211\u020d\3\2\2\2\u0211\u020e\3\2\2\2")
        buf.write("\u0211\u020f\3\2\2\2\u0211\u0210\3\2\2\2\u0212g\3\2\2")
        buf.write("\2\u0213\u0214\7\f\2\2\u0214\u0237\7.\2\2\u0215\u021a")
        buf.write("\7:\2\2\u0216\u0217\7\64\2\2\u0217\u0219\7:\2\2\u0218")
        buf.write("\u0216\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218\3\2\2\2")
        buf.write("\u021a\u021b\3\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a\3")
        buf.write("\2\2\2\u021d\u0215\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u0238")
        buf.write("\3\2\2\2\u021f\u0224\7;\2\2\u0220\u0221\7\64\2\2\u0221")
        buf.write("\u0223\7;\2\2\u0222\u0220\3\2\2\2\u0223\u0226\3\2\2\2")
        buf.write("\u0224\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0238\3")
        buf.write("\2\2\2\u0226\u0224\3\2\2\2\u0227\u022c\7<\2\2\u0228\u0229")
        buf.write("\7\64\2\2\u0229\u022b\7<\2\2\u022a\u0228\3\2\2\2\u022b")
        buf.write("\u022e\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2\2\2")
        buf.write("\u022d\u0238\3\2\2\2\u022e\u022c\3\2\2\2\u022f\u0234\7")
        buf.write("=\2\2\u0230\u0231\7\64\2\2\u0231\u0233\7=\2\2\u0232\u0230")
        buf.write("\3\2\2\2\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234")
        buf.write("\u0235\3\2\2\2\u0235\u0238\3\2\2\2\u0236\u0234\3\2\2\2")
        buf.write("\u0237\u021d\3\2\2\2\u0237\u021f\3\2\2\2\u0237\u0227\3")
        buf.write("\2\2\2\u0237\u022f\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u023a")
        buf.write("\7/\2\2\u023ai\3\2\2\2\u023b\u023c\7\f\2\2\u023c\u0245")
        buf.write("\7.\2\2\u023d\u0242\5h\65\2\u023e\u023f\7\64\2\2\u023f")
        buf.write("\u0241\5h\65\2\u0240\u023e\3\2\2\2\u0241\u0244\3\2\2\2")
        buf.write("\u0242\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0246\3")
        buf.write("\2\2\2\u0244\u0242\3\2\2\2\u0245\u023d\3\2\2\2\u0245\u0246")
        buf.write("\3\2\2\2\u0246\u0247\3\2\2\2\u0247\u0248\7/\2\2\u0248")
        buf.write("k\3\2\2\2\u0249\u024a\t\b\2\2\u024am\3\2\2\2\u024b\u024c")
        buf.write("\t\t\2\2\u024co\3\2\2\2\u024d\u024e\7\f\2\2\u024e\u024f")
        buf.write("\7\60\2\2\u024f\u0250\5n8\2\u0250\u0251\7\64\2\2\u0251")
        buf.write("\u0252\7:\2\2\u0252\u0253\7\61\2\2\u0253q\3\2\2\2\u0254")
        buf.write("\u0255\7\31\2\2\u0255\u0256\7>\2\2\u0256\u0257\7.\2\2")
        buf.write("\u0257\u0258\7/\2\2\u0258s\3\2\2\2:z\177\u0087\u008b\u0090")
        buf.write("\u0099\u009e\u00af\u00b9\u00c0\u00c5\u00d5\u00d7\u00e0")
        buf.write("\u00e6\u00ea\u00f4\u00f6\u00fe\u0100\u0108\u010b\u0116")
        buf.write("\u0123\u012f\u013a\u0145\u0150\u0156\u015b\u0164\u016f")
        buf.write("\u017a\u017f\u0186\u0192\u0196\u01a1\u01a6\u01af\u01b3")
        buf.write("\u01b9\u01c3\u01c7\u01e5\u01fc\u0209\u0211\u021a\u021d")
        buf.write("\u0224\u022c\u0234\u0237\u0242\u0245")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Program'", "<INVALID>", "<INVALID>", 
                     "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
                     "'Foreach'", "'Array'", "'In'", "'Int'", "'Float'", 
                     "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", 
                     "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "'main'", "'self'", "'='", "'!'", 
                     "'||'", "'&&'", "'=='", "'!='", "'%'", "'+'", "'-'", 
                     "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", "'+.'", 
                     "'==.'", "'('", "')'", "'['", "']'", "'.'", "'..'", 
                     "','", "':'", "'::'", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WHITE_SPACE", "COMMENT", 
                      "K_BREAK", "K_CONTINUE", "K_IF", "K_ELSE_IF", "K_ELSE", 
                      "K_FOR_EACH", "K_ARRAY", "K_IN", "K_INT", "K_FLOAT", 
                      "K_BOOLEAN", "K_STRING", "K_RETURN", "K_NULL", "K_CLASS", 
                      "K_VAL", "K_VAR", "K_CONSTRUCTOR", "K_DESTRUCTOR", 
                      "K_NEW", "K_BY", "K_MAIN", "K_SELF", "OP_ASSIGN", 
                      "OP_LOGICAL_NOT", "OP_LOGICAL_OR", "OP_LOGICAL_AND", 
                      "OP_IS_EQUAL_TO", "OP_NOT_EQUAL_TO", "OP_MODULO", 
                      "OP_ADDTION", "OP_SUBTRACTION", "OP_MULTIPLICATION", 
                      "OP_DIVISION", "OP_LESS_THAN", "OP_LESS_THAN_EQUAL", 
                      "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", "OP_STRING_CONCATENATION", 
                      "OP_TWO_SAME_STRING", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "DOT", 
                      "DOUBLE_DOT", "COMMA", "COLON", "DOUBLE_COLON", "SEMI_COLON", 
                      "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "INTEGER_LITERAL", 
                      "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                      "IDENTIFIER", "DOLAR_IDENTIFIER", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_many_class = 1
    RULE_class_declaration = 2
    RULE_class_body = 3
    RULE_class_body_unit = 4
    RULE_super_class_group = 5
    RULE_program_class_declaration = 6
    RULE_program_class_body = 7
    RULE_main_method_declaration = 8
    RULE_method_declaration = 9
    RULE_constructor = 10
    RULE_destructor = 11
    RULE_parameter_list = 12
    RULE_parameter = 13
    RULE_attribute_declaration = 14
    RULE_identifier_list = 15
    RULE_dolar_identifier_list = 16
    RULE_expression_list = 17
    RULE_element_expression = 18
    RULE_index_operator = 19
    RULE_relational_operator = 20
    RULE_expression = 21
    RULE_relational_expr = 22
    RULE_and_or_expr = 23
    RULE_add_sub_expr = 24
    RULE_mul_add_mol_expr = 25
    RULE_not_expr = 26
    RULE_sign_expr = 27
    RULE_index_operator_expr = 28
    RULE_instance_attribute_access = 29
    RULE_instace_method_invocation = 30
    RULE_static_method_invocation = 31
    RULE_static_attribute_access = 32
    RULE_object_creation = 33
    RULE_atom_expr = 34
    RULE_function_call = 35
    RULE_var_val_statement = 36
    RULE_assign_statement = 37
    RULE_if_statement = 38
    RULE_if_part = 39
    RULE_else_if_part = 40
    RULE_else_part = 41
    RULE_for_in_statement = 42
    RULE_loop_part = 43
    RULE_break_statement = 44
    RULE_continue_statement = 45
    RULE_return_statement = 46
    RULE_method_invocation_statement = 47
    RULE_block_statement = 48
    RULE_statement = 49
    RULE_literal = 50
    RULE_indexed_array = 51
    RULE_multi_dimentional_array = 52
    RULE_identifier = 53
    RULE_primitive_type = 54
    RULE_array_type = 55
    RULE_class_type = 56

    ruleNames =  [ "program", "many_class", "class_declaration", "class_body", 
                   "class_body_unit", "super_class_group", "program_class_declaration", 
                   "program_class_body", "main_method_declaration", "method_declaration", 
                   "constructor", "destructor", "parameter_list", "parameter", 
                   "attribute_declaration", "identifier_list", "dolar_identifier_list", 
                   "expression_list", "element_expression", "index_operator", 
                   "relational_operator", "expression", "relational_expr", 
                   "and_or_expr", "add_sub_expr", "mul_add_mol_expr", "not_expr", 
                   "sign_expr", "index_operator_expr", "instance_attribute_access", 
                   "instace_method_invocation", "static_method_invocation", 
                   "static_attribute_access", "object_creation", "atom_expr", 
                   "function_call", "var_val_statement", "assign_statement", 
                   "if_statement", "if_part", "else_if_part", "else_part", 
                   "for_in_statement", "loop_part", "break_statement", "continue_statement", 
                   "return_statement", "method_invocation_statement", "block_statement", 
                   "statement", "literal", "indexed_array", "multi_dimentional_array", 
                   "identifier", "primitive_type", "array_type", "class_type" ]

    EOF = Token.EOF
    T__0=1
    WHITE_SPACE=2
    COMMENT=3
    K_BREAK=4
    K_CONTINUE=5
    K_IF=6
    K_ELSE_IF=7
    K_ELSE=8
    K_FOR_EACH=9
    K_ARRAY=10
    K_IN=11
    K_INT=12
    K_FLOAT=13
    K_BOOLEAN=14
    K_STRING=15
    K_RETURN=16
    K_NULL=17
    K_CLASS=18
    K_VAL=19
    K_VAR=20
    K_CONSTRUCTOR=21
    K_DESTRUCTOR=22
    K_NEW=23
    K_BY=24
    K_MAIN=25
    K_SELF=26
    OP_ASSIGN=27
    OP_LOGICAL_NOT=28
    OP_LOGICAL_OR=29
    OP_LOGICAL_AND=30
    OP_IS_EQUAL_TO=31
    OP_NOT_EQUAL_TO=32
    OP_MODULO=33
    OP_ADDTION=34
    OP_SUBTRACTION=35
    OP_MULTIPLICATION=36
    OP_DIVISION=37
    OP_LESS_THAN=38
    OP_LESS_THAN_EQUAL=39
    OP_GREATER_THAN=40
    OP_GREATER_THAN_EQUAL=41
    OP_STRING_CONCATENATION=42
    OP_TWO_SAME_STRING=43
    LEFT_PAREN=44
    RIGHT_PAREN=45
    LEFT_SQUARE_BRACKET=46
    RIGHT_SQUARE_BRACKET=47
    DOT=48
    DOUBLE_DOT=49
    COMMA=50
    COLON=51
    DOUBLE_COLON=52
    SEMI_COLON=53
    LEFT_CURLY_BRACKET=54
    RIGHT_CURLY_BRACKET=55
    INTEGER_LITERAL=56
    FLOAT_LITERAL=57
    BOOLEAN_LITERAL=58
    STRING_LITERAL=59
    IDENTIFIER=60
    DOLAR_IDENTIFIER=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    ERROR_TOKEN=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def many_class(self):
            return self.getTypedRuleContext(D96Parser.Many_classContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.many_class()
            self.state = 115
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_classContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMany_class" ):
                listener.enterMany_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMany_class" ):
                listener.exitMany_class(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_class" ):
                return visitor.visitMany_class(self)
            else:
                return visitor.visitChildren(self)




    def many_class(self):

        localctx = D96Parser.Many_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_many_class)
        self._la = 0 # Token type
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 117
                    self.class_declaration()
                    self.state = 120 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.K_CLASS):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 122
                        self.class_declaration() 
                    self.state = 127
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 128
                self.program_class_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.program_class_declaration()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.K_CLASS:
                    self.state = 130
                    self.class_declaration()
                    self.state = 135
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
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
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_declaration" ):
                listener.enterClass_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_declaration" ):
                listener.exitClass_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(D96Parser.K_CLASS)
            self.state = 140
            self.match(D96Parser.IDENTIFIER)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 141
                self.super_class_group()


            self.state = 144
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 145
            self.class_body()
            self.state = 146
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_body" ):
                listener.enterClass_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_body" ):
                listener.exitClass_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 148
                self.class_body_unit()
                self.state = 153
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(D96Parser.Method_declarationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_body_unit" ):
                listener.enterClass_body_unit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_body_unit" ):
                listener.exitClass_body_unit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body_unit" ):
                return visitor.visitClass_body_unit(self)
            else:
                return visitor.visitChildren(self)




    def class_body_unit(self):

        localctx = D96Parser.Class_body_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_body_unit)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_VAL, D96Parser.K_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.attribute_declaration()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR, D96Parser.K_DESTRUCTOR, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.method_declaration()
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_super_class_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuper_class_group" ):
                listener.enterSuper_class_group(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuper_class_group" ):
                listener.exitSuper_class_group(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuper_class_group" ):
                return visitor.visitSuper_class_group(self)
            else:
                return visitor.visitChildren(self)




    def super_class_group(self):

        localctx = D96Parser.Super_class_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_super_class_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(D96Parser.COLON)
            self.state = 159
            self.match(D96Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram_class_declaration" ):
                listener.enterProgram_class_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram_class_declaration" ):
                listener.exitProgram_class_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_class_declaration" ):
                return visitor.visitProgram_class_declaration(self)
            else:
                return visitor.visitChildren(self)




    def program_class_declaration(self):

        localctx = D96Parser.Program_class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_program_class_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(D96Parser.K_CLASS)
            self.state = 162
            self.match(D96Parser.T__0)
            self.state = 163
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 164
            self.program_class_body()
            self.state = 165
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_method_declaration(self):
            return self.getTypedRuleContext(D96Parser.Main_method_declarationContext,0)


        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_program_class_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram_class_body" ):
                listener.enterProgram_class_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram_class_body" ):
                listener.exitProgram_class_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_class_body" ):
                return visitor.visitProgram_class_body(self)
            else:
                return visitor.visitChildren(self)




    def program_class_body(self):

        localctx = D96Parser.Program_class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_program_class_body)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.main_method_declaration()
                self.state = 168
                self.class_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.class_body()
                self.state = 171
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_MAIN(self):
            return self.getToken(D96Parser.K_MAIN, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_main_method_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_method_declaration" ):
                listener.enterMain_method_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_method_declaration" ):
                listener.exitMain_method_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_method_declaration" ):
                return visitor.visitMain_method_declaration(self)
            else:
                return visitor.visitChildren(self)




    def main_method_declaration(self):

        localctx = D96Parser.Main_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_main_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(D96Parser.K_MAIN)
            self.state = 176
            self.match(D96Parser.LEFT_PAREN)
            self.state = 177
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 178
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_listContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_declaration" ):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_declaration" ):
                listener.exitMethod_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declaration" ):
                return visitor.visitMethod_declaration(self)
            else:
                return visitor.visitChildren(self)




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.identifier()
                self.state = 181
                self.match(D96Parser.LEFT_PAREN)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 182
                    self.parameter_list()


                self.state = 185
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 186
                self.block_statement()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.constructor()
                pass
            elif token in [D96Parser.K_DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_CONSTRUCTOR(self):
            return self.getToken(D96Parser.K_CONSTRUCTOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructor" ):
                listener.enterConstructor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructor" ):
                listener.exitConstructor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(D96Parser.K_CONSTRUCTOR)
            self.state = 193
            self.match(D96Parser.LEFT_PAREN)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDENTIFIER:
                self.state = 194
                self.parameter_list()


            self.state = 197
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 198
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_DESTRUCTOR(self):
            return self.getToken(D96Parser.K_DESTRUCTOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDestructor" ):
                listener.enterDestructor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDestructor" ):
                listener.exitDestructor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(D96Parser.K_DESTRUCTOR)
            self.state = 201
            self.match(D96Parser.LEFT_PAREN)
            self.state = 202
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 203
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ParameterContext)
            else:
                return self.getTypedRuleContext(D96Parser.ParameterContext,i)


        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI_COLON)
            else:
                return self.getToken(D96Parser.SEMI_COLON, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_list" ):
                listener.enterParameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_list" ):
                listener.exitParameter_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = D96Parser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.parameter()
                self.state = 209 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 207
                    self.match(D96Parser.SEMI_COLON)
                    self.state = 208
                    self.parameter()
                    self.state = 211 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.SEMI_COLON):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.identifier_list()
            self.state = 216
            self.match(D96Parser.COLON)
            self.state = 217
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_declaration" ):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_declaration" ):
                listener.exitAttribute_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declaration" ):
                return visitor.visitAttribute_declaration(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declaration(self):

        localctx = D96Parser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER]:
                self.state = 220
                self.identifier_list()
                pass
            elif token in [D96Parser.DOLAR_IDENTIFIER]:
                self.state = 221
                self.dolar_identifier_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 224
            self.match(D96Parser.COLON)
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 225
                self.array_type()
                pass

            elif la_ == 2:
                self.state = 226
                self.primitive_type()
                pass

            elif la_ == 3:
                self.state = 227
                self.identifier()
                pass


            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 230
                self.match(D96Parser.OP_ASSIGN)
                self.state = 231
                self.expression_list()


            self.state = 234
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_identifier_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier_list" ):
                listener.enterIdentifier_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier_list" ):
                listener.exitIdentifier_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier_list" ):
                return visitor.visitIdentifier_list(self)
            else:
                return visitor.visitChildren(self)




    def identifier_list(self):

        localctx = D96Parser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(D96Parser.IDENTIFIER)
                self.state = 240 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 238
                    self.match(D96Parser.COMMA)
                    self.state = 239
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 242 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.COMMA):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dolar_identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLAR_IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLAR_IDENTIFIER)
            else:
                return self.getToken(D96Parser.DOLAR_IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_dolar_identifier_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDolar_identifier_list" ):
                listener.enterDolar_identifier_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDolar_identifier_list" ):
                listener.exitDolar_identifier_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDolar_identifier_list" ):
                return visitor.visitDolar_identifier_list(self)
            else:
                return visitor.visitChildren(self)




    def dolar_identifier_list(self):

        localctx = D96Parser.Dolar_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_dolar_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 250 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 248
                    self.match(D96Parser.COMMA)
                    self.state = 249
                    self.match(D96Parser.DOLAR_IDENTIFIER)
                    self.state = 252 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.COMMA):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = D96Parser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.expression(0)
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 258
                    self.match(D96Parser.COMMA)
                    self.state = 259
                    self.expression(0)
                    self.state = 264
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement_expression" ):
                listener.enterElement_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement_expression" ):
                listener.exitElement_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expression" ):
                return visitor.visitElement_expression(self)
            else:
                return visitor.visitChildren(self)




    def element_expression(self):

        localctx = D96Parser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.expression(0)
            self.state = 268
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_operator" ):
                listener.enterIndex_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_operator" ):
                listener.exitIndex_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 271
            self.expression(0)
            self.state = 272
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 273
                    self.index_operator() 
                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_IS_EQUAL_TO(self):
            return self.getToken(D96Parser.OP_IS_EQUAL_TO, 0)

        def OP_NOT_EQUAL_TO(self):
            return self.getToken(D96Parser.OP_NOT_EQUAL_TO, 0)

        def OP_LESS_THAN(self):
            return self.getToken(D96Parser.OP_LESS_THAN, 0)

        def OP_LESS_THAN_EQUAL(self):
            return self.getToken(D96Parser.OP_LESS_THAN_EQUAL, 0)

        def OP_GREATER_THAN(self):
            return self.getToken(D96Parser.OP_GREATER_THAN, 0)

        def OP_GREATER_THAN_EQUAL(self):
            return self.getToken(D96Parser.OP_GREATER_THAN_EQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relational_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_operator" ):
                listener.enterRelational_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_operator" ):
                listener.exitRelational_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operator" ):
                return visitor.visitRelational_operator(self)
            else:
                return visitor.visitChildren(self)




    def relational_operator(self):

        localctx = D96Parser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_IS_EQUAL_TO) | (1 << D96Parser.OP_NOT_EQUAL_TO) | (1 << D96Parser.OP_LESS_THAN) | (1 << D96Parser.OP_LESS_THAN_EQUAL) | (1 << D96Parser.OP_GREATER_THAN) | (1 << D96Parser.OP_GREATER_THAN_EQUAL))) != 0)):
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self):
            return self.getTypedRuleContext(D96Parser.Relational_exprContext,0)


        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def OP_STRING_CONCATENATION(self):
            return self.getToken(D96Parser.OP_STRING_CONCATENATION, 0)

        def OP_TWO_SAME_STRING(self):
            return self.getToken(D96Parser.OP_TWO_SAME_STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.relational_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 289
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 284
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 285
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_STRING_CONCATENATION or _la==D96Parser.OP_TWO_SAME_STRING):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 286
                    self.relational_expr(0) 
                self.state = 291
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_or_expr(self):
            return self.getTypedRuleContext(D96Parser.And_or_exprContext,0)


        def relational_expr(self):
            return self.getTypedRuleContext(D96Parser.Relational_exprContext,0)


        def relational_operator(self):
            return self.getTypedRuleContext(D96Parser.Relational_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_relational_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_expr" ):
                listener.enterRelational_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_expr" ):
                listener.exitRelational_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)



    def relational_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Relational_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_relational_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.and_or_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Relational_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr)
                    self.state = 295
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 296
                    self.relational_operator()
                    self.state = 297
                    self.and_or_expr(0) 
                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class And_or_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_sub_expr(self):
            return self.getTypedRuleContext(D96Parser.Add_sub_exprContext,0)


        def and_or_expr(self):
            return self.getTypedRuleContext(D96Parser.And_or_exprContext,0)


        def OP_LOGICAL_AND(self):
            return self.getToken(D96Parser.OP_LOGICAL_AND, 0)

        def OP_LOGICAL_OR(self):
            return self.getToken(D96Parser.OP_LOGICAL_OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_and_or_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_or_expr" ):
                listener.enterAnd_or_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_or_expr" ):
                listener.exitAnd_or_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_or_expr" ):
                return visitor.visitAnd_or_expr(self)
            else:
                return visitor.visitChildren(self)



    def and_or_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.And_or_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_and_or_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.add_sub_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 312
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.And_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_or_expr)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_LOGICAL_OR or _la==D96Parser.OP_LOGICAL_AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 309
                    self.add_sub_expr(0) 
                self.state = 314
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_add_mol_expr(self):
            return self.getTypedRuleContext(D96Parser.Mul_add_mol_exprContext,0)


        def add_sub_expr(self):
            return self.getTypedRuleContext(D96Parser.Add_sub_exprContext,0)


        def OP_ADDTION(self):
            return self.getToken(D96Parser.OP_ADDTION, 0)

        def OP_SUBTRACTION(self):
            return self.getToken(D96Parser.OP_SUBTRACTION, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_add_sub_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_sub_expr" ):
                listener.enterAdd_sub_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_sub_expr" ):
                listener.exitAdd_sub_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_sub_expr" ):
                return visitor.visitAdd_sub_expr(self)
            else:
                return visitor.visitChildren(self)



    def add_sub_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Add_sub_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_add_sub_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.mul_add_mol_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Add_sub_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expr)
                    self.state = 318
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 319
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_ADDTION or _la==D96Parser.OP_SUBTRACTION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 320
                    self.mul_add_mol_expr(0) 
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_add_mol_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_expr(self):
            return self.getTypedRuleContext(D96Parser.Not_exprContext,0)


        def mul_add_mol_expr(self):
            return self.getTypedRuleContext(D96Parser.Mul_add_mol_exprContext,0)


        def OP_MULTIPLICATION(self):
            return self.getToken(D96Parser.OP_MULTIPLICATION, 0)

        def OP_DIVISION(self):
            return self.getToken(D96Parser.OP_DIVISION, 0)

        def OP_MODULO(self):
            return self.getToken(D96Parser.OP_MODULO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mul_add_mol_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul_add_mol_expr" ):
                listener.enterMul_add_mol_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul_add_mol_expr" ):
                listener.exitMul_add_mol_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_add_mol_expr" ):
                return visitor.visitMul_add_mol_expr(self)
            else:
                return visitor.visitChildren(self)



    def mul_add_mol_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Mul_add_mol_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_mul_add_mol_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Mul_add_mol_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_add_mol_expr)
                    self.state = 329
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 330
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MODULO) | (1 << D96Parser.OP_MULTIPLICATION) | (1 << D96Parser.OP_DIVISION))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 331
                    self.not_expr() 
                self.state = 336
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Not_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_LOGICAL_NOT(self):
            return self.getToken(D96Parser.OP_LOGICAL_NOT, 0)

        def not_expr(self):
            return self.getTypedRuleContext(D96Parser.Not_exprContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(D96Parser.Sign_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_not_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_expr" ):
                listener.enterNot_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_expr" ):
                listener.exitNot_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_expr" ):
                return visitor.visitNot_expr(self)
            else:
                return visitor.visitChildren(self)




    def not_expr(self):

        localctx = D96Parser.Not_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_not_expr)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(D96Parser.OP_LOGICAL_NOT)
                self.state = 338
                self.not_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NEW, D96Parser.OP_SUBTRACTION, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.sign_expr()
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


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_expr(self):
            return self.getTypedRuleContext(D96Parser.Sign_exprContext,0)


        def OP_SUBTRACTION(self):
            return self.getToken(D96Parser.OP_SUBTRACTION, 0)

        def index_operator_expr(self):
            return self.getTypedRuleContext(D96Parser.Index_operator_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_sign_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign_expr" ):
                listener.enterSign_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign_expr" ):
                listener.exitSign_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = D96Parser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_sign_expr)
        try:
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUBTRACTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.match(D96Parser.OP_SUBTRACTION)
                self.state = 343
                self.sign_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NEW, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.index_operator_expr(0)
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


    class Index_operator_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_attribute_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_attribute_accessContext,0)


        def index_operator_expr(self):
            return self.getTypedRuleContext(D96Parser.Index_operator_exprContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operator_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_operator_expr" ):
                listener.enterIndex_operator_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_operator_expr" ):
                listener.exitIndex_operator_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator_expr" ):
                return visitor.visitIndex_operator_expr(self)
            else:
                return visitor.visitChildren(self)



    def index_operator_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_operator_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_index_operator_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.instance_attribute_access(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operator_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operator_expr)
                    self.state = 350
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 351
                    self.index_operator() 
                self.state = 356
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Instance_attribute_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instace_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Instace_method_invocationContext,0)


        def instance_attribute_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_attribute_accessContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attribute_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstance_attribute_access" ):
                listener.enterInstance_attribute_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstance_attribute_access" ):
                listener.exitInstance_attribute_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_attribute_access" ):
                return visitor.visitInstance_attribute_access(self)
            else:
                return visitor.visitChildren(self)



    def instance_attribute_access(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Instance_attribute_accessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_instance_attribute_access, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.instace_method_invocation(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Instance_attribute_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_attribute_access)
                    self.state = 360
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 361
                    self.match(D96Parser.DOT)
                    self.state = 362
                    self.match(D96Parser.IDENTIFIER) 
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Instace_method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_creation(self):
            return self.getTypedRuleContext(D96Parser.Object_creationContext,0)


        def instace_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Instace_method_invocationContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instace_method_invocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstace_method_invocation" ):
                listener.enterInstace_method_invocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstace_method_invocation" ):
                listener.exitInstace_method_invocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstace_method_invocation" ):
                return visitor.visitInstace_method_invocation(self)
            else:
                return visitor.visitChildren(self)



    def instace_method_invocation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Instace_method_invocationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_instace_method_invocation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.object_creation()
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Instace_method_invocationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instace_method_invocation)
                    self.state = 371
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 372
                    self.match(D96Parser.DOUBLE_COLON)
                    self.state = 373
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 374
                    self.match(D96Parser.LEFT_PAREN)
                    self.state = 376
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                        self.state = 375
                        self.expression_list()


                    self.state = 378
                    self.match(D96Parser.RIGHT_PAREN) 
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Static_method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_method_invocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatic_method_invocation" ):
                listener.enterStatic_method_invocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatic_method_invocation" ):
                listener.exitStatic_method_invocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_invocation" ):
                return visitor.visitStatic_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def static_method_invocation(self):

        localctx = D96Parser.Static_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_static_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(D96Parser.IDENTIFIER)
            self.state = 385
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 386
            self.match(D96Parser.LEFT_PAREN)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 387
                self.expression_list()


            self.state = 390
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_attribute_accessContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatic_attribute_access" ):
                listener.enterStatic_attribute_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatic_attribute_access" ):
                listener.exitStatic_attribute_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_attribute_access" ):
                return visitor.visitStatic_attribute_access(self)
            else:
                return visitor.visitChildren(self)




    def static_attribute_access(self):

        localctx = D96Parser.Static_attribute_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_static_attribute_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(D96Parser.IDENTIFIER)
            self.state = 393
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 394
            self.match(D96Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_creationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def atom_expr(self):
            return self.getTypedRuleContext(D96Parser.Atom_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_object_creation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_creation" ):
                listener.enterObject_creation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_creation" ):
                listener.exitObject_creation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_creation" ):
                return visitor.visitObject_creation(self)
            else:
                return visitor.visitChildren(self)




    def object_creation(self):

        localctx = D96Parser.Object_creationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_object_creation)
        self._la = 0 # Token type
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(D96Parser.K_NEW)
                self.state = 397
                self.match(D96Parser.IDENTIFIER)
                self.state = 398
                self.match(D96Parser.LEFT_PAREN)
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 399
                    self.expression_list()


                self.state = 402
                self.match(D96Parser.RIGHT_PAREN)
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.atom_expr()
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


    class Atom_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def function_call(self):
            return self.getTypedRuleContext(D96Parser.Function_callContext,0)


        def static_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocationContext,0)


        def static_attribute_access(self):
            return self.getTypedRuleContext(D96Parser.Static_attribute_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_atom_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom_expr" ):
                listener.enterAtom_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom_expr" ):
                listener.exitAtom_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom_expr" ):
                return visitor.visitAtom_expr(self)
            else:
                return visitor.visitChildren(self)




    def atom_expr(self):

        localctx = D96Parser.Atom_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_atom_expr)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
                self.match(D96Parser.LEFT_PAREN)
                self.state = 409
                self.expression(0)
                self.state = 410
                self.match(D96Parser.RIGHT_PAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 412
                self.function_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 413
                self.static_method_invocation()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 414
                self.static_attribute_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = D96Parser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(D96Parser.IDENTIFIER)
            self.state = 418
            self.match(D96Parser.LEFT_PAREN)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 419
                self.expression_list()


            self.state = 422
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_val_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_val_statement" ):
                listener.enterVar_val_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_val_statement" ):
                listener.exitVar_val_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_val_statement" ):
                return visitor.visitVar_val_statement(self)
            else:
                return visitor.visitChildren(self)




    def var_val_statement(self):

        localctx = D96Parser.Var_val_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_var_val_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 425
            self.identifier_list()
            self.state = 426
            self.match(D96Parser.COLON)
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 427
                self.array_type()
                pass

            elif la_ == 2:
                self.state = 428
                self.primitive_type()
                pass


            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 431
                self.match(D96Parser.OP_ASSIGN)
                self.state = 432
                self.expression_list()


            self.state = 435
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def element_expression(self):
            return self.getTypedRuleContext(D96Parser.Element_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_statement" ):
                listener.enterAssign_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_statement" ):
                listener.exitAssign_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 437
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 438
                self.element_expression()
                pass


            self.state = 441
            self.match(D96Parser.OP_ASSIGN)
            self.state = 442
            self.expression(0)
            self.state = 443
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_part(self):
            return self.getTypedRuleContext(D96Parser.If_partContext,0)


        def else_if_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Else_if_partContext)
            else:
                return self.getTypedRuleContext(D96Parser.Else_if_partContext,i)


        def else_part(self):
            return self.getTypedRuleContext(D96Parser.Else_partContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.if_part()
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.K_ELSE_IF:
                self.state = 446
                self.else_if_part()
                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ELSE:
                self.state = 452
                self.else_part()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_partContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_part" ):
                listener.enterIf_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_part" ):
                listener.exitIf_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_part" ):
                return visitor.visitIf_part(self)
            else:
                return visitor.visitChildren(self)




    def if_part(self):

        localctx = D96Parser.If_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(D96Parser.K_IF)
            self.state = 456
            self.match(D96Parser.LEFT_PAREN)
            self.state = 457
            self.expression(0)
            self.state = 458
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 459
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_partContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def getRuleIndex(self):
            return D96Parser.RULE_else_if_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_if_part" ):
                listener.enterElse_if_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_if_part" ):
                listener.exitElse_if_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_part" ):
                return visitor.visitElse_if_part(self)
            else:
                return visitor.visitChildren(self)




    def else_if_part(self):

        localctx = D96Parser.Else_if_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_else_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(D96Parser.K_ELSE_IF)
            self.state = 462
            self.match(D96Parser.LEFT_PAREN)
            self.state = 463
            self.expression(0)
            self.state = 464
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 465
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ELSE(self):
            return self.getToken(D96Parser.K_ELSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_part" ):
                listener.enterElse_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_part" ):
                listener.exitElse_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = D96Parser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(D96Parser.K_ELSE)
            self.state = 468
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_in_statement" ):
                listener.enterFor_in_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_in_statement" ):
                listener.exitFor_in_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_statement" ):
                return visitor.visitFor_in_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_in_statement(self):

        localctx = D96Parser.For_in_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_for_in_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(D96Parser.K_FOR_EACH)
            self.state = 471
            self.match(D96Parser.LEFT_PAREN)
            self.state = 472
            self.loop_part()
            self.state = 473
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 474
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_partContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_part" ):
                listener.enterLoop_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_part" ):
                listener.exitLoop_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_part" ):
                return visitor.visitLoop_part(self)
            else:
                return visitor.visitChildren(self)




    def loop_part(self):

        localctx = D96Parser.Loop_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_loop_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(D96Parser.IDENTIFIER)
            self.state = 477
            self.match(D96Parser.K_IN)
            self.state = 478
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 479
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 480
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_BY:
                self.state = 481
                self.match(D96Parser.K_BY)
                self.state = 482
                self.match(D96Parser.INTEGER_LITERAL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_BREAK(self):
            return self.getToken(D96Parser.K_BREAK, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_statement" ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_statement" ):
                listener.exitBreak_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(D96Parser.K_BREAK)
            self.state = 486
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_CONTINUE(self):
            return self.getToken(D96Parser.K_CONTINUE, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_statement" ):
                listener.enterContinue_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_statement" ):
                listener.exitContinue_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(D96Parser.K_CONTINUE)
            self.state = 489
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(D96Parser.K_RETURN)
            self.state = 492
            self.expression(0)
            self.state = 493
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_invocation_statement" ):
                listener.enterMethod_invocation_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_invocation_statement" ):
                listener.exitMethod_invocation_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_statement" ):
                return visitor.visitMethod_invocation_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_statement(self):

        localctx = D96Parser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(D96Parser.IDENTIFIER)
            self.state = 496
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 497
            self.match(D96Parser.DOLAR_IDENTIFIER)
            self.state = 498
            self.match(D96Parser.LEFT_PAREN)
            self.state = 499
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 500
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StatementContext)
            else:
                return self.getTypedRuleContext(D96Parser.StatementContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_statement" ):
                listener.enterBlock_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_statement" ):
                listener.exitBlock_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 506
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_BREAK) | (1 << D96Parser.K_CONTINUE) | (1 << D96Parser.K_IF) | (1 << D96Parser.K_FOR_EACH) | (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_RETURN) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 503
                self.statement()
                self.state = 508
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 509
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_val_statement(self):
            return self.getTypedRuleContext(D96Parser.Var_val_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(D96Parser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(D96Parser.If_statementContext,0)


        def for_in_statement(self):
            return self.getTypedRuleContext(D96Parser.For_in_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(D96Parser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(D96Parser.Return_statementContext,0)


        def method_invocation_statement(self):
            return self.getTypedRuleContext(D96Parser.Method_invocation_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_statement)
        try:
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.var_val_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 513
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 514
                self.for_in_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 515
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 516
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 517
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 518
                self.method_invocation_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(D96Parser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(D96Parser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def multi_dimentional_array(self):
            return self.getTypedRuleContext(D96Parser.Multi_dimentional_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_literal)
        try:
            self.state = 527
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.match(D96Parser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(D96Parser.FLOAT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 523
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 524
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 525
                self.indexed_array()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 526
                self.multi_dimentional_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexed_array" ):
                listener.enterIndexed_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexed_array" ):
                listener.exitIndexed_array(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array" ):
                return visitor.visitIndexed_array(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(D96Parser.K_ARRAY)
            self.state = 530
            self.match(D96Parser.LEFT_PAREN)
            self.state = 565
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RIGHT_PAREN, D96Parser.INTEGER_LITERAL]:
                self.state = 539
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.INTEGER_LITERAL:
                    self.state = 531
                    self.match(D96Parser.INTEGER_LITERAL)
                    self.state = 536
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.COMMA:
                        self.state = 532
                        self.match(D96Parser.COMMA)
                        self.state = 533
                        self.match(D96Parser.INTEGER_LITERAL)
                        self.state = 538
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.state = 541
                self.match(D96Parser.FLOAT_LITERAL)
                self.state = 546
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 542
                    self.match(D96Parser.COMMA)
                    self.state = 543
                    self.match(D96Parser.FLOAT_LITERAL)
                    self.state = 548
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.state = 549
                self.match(D96Parser.BOOLEAN_LITERAL)
                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 550
                    self.match(D96Parser.COMMA)
                    self.state = 551
                    self.match(D96Parser.BOOLEAN_LITERAL)
                    self.state = 556
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.state = 557
                self.match(D96Parser.STRING_LITERAL)
                self.state = 562
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 558
                    self.match(D96Parser.COMMA)
                    self.state = 559
                    self.match(D96Parser.STRING_LITERAL)
                    self.state = 564
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 567
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_dimentional_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulti_dimentional_array" ):
                listener.enterMulti_dimentional_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulti_dimentional_array" ):
                listener.exitMulti_dimentional_array(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_dimentional_array" ):
                return visitor.visitMulti_dimentional_array(self)
            else:
                return visitor.visitChildren(self)




    def multi_dimentional_array(self):

        localctx = D96Parser.Multi_dimentional_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_multi_dimentional_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(D96Parser.K_ARRAY)
            self.state = 570
            self.match(D96Parser.LEFT_PAREN)

            self.state = 579
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ARRAY:
                self.state = 571
                self.indexed_array()
                self.state = 576
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 572
                    self.match(D96Parser.COMMA)
                    self.state = 573
                    self.indexed_array()
                    self.state = 578
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 581
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = D96Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
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


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive_type" ):
                listener.enterPrimitive_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive_type" ):
                listener.exitPrimitive_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
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
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_type" ):
                listener.enterArray_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_type" ):
                listener.exitArray_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self.match(D96Parser.K_ARRAY)
            self.state = 588
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 589
            self.primitive_type()
            self.state = 590
            self.match(D96Parser.COMMA)
            self.state = 591
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 592
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_type" ):
                listener.enterClass_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_type" ):
                listener.exitClass_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(D96Parser.K_NEW)
            self.state = 595
            self.match(D96Parser.IDENTIFIER)
            self.state = 596
            self.match(D96Parser.LEFT_PAREN)
            self.state = 597
            self.match(D96Parser.RIGHT_PAREN)
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
        self._predicates[21] = self.expression_sempred
        self._predicates[22] = self.relational_expr_sempred
        self._predicates[23] = self.and_or_expr_sempred
        self._predicates[24] = self.add_sub_expr_sempred
        self._predicates[25] = self.mul_add_mol_expr_sempred
        self._predicates[28] = self.index_operator_expr_sempred
        self._predicates[29] = self.instance_attribute_access_sempred
        self._predicates[30] = self.instace_method_invocation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def relational_expr_sempred(self, localctx:Relational_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def and_or_expr_sempred(self, localctx:And_or_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def add_sub_expr_sempred(self, localctx:Add_sub_exprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def mul_add_mol_expr_sempred(self, localctx:Mul_add_mol_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def index_operator_expr_sempred(self, localctx:Index_operator_exprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def instance_attribute_access_sempred(self, localctx:Instance_attribute_accessContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def instace_method_invocation_sempred(self, localctx:Instace_method_invocationContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         




