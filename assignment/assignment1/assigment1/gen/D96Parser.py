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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0266\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\6\2l\n\2\r\2\16\2m\3\2\3\2\3\3\3\3\3\3")
        buf.write("\5\3u\n\3\3\3\3\3\7\3y\n\3\f\3\16\3|\13\3\3\3\3\3\3\4")
        buf.write("\3\4\5\4\u0082\n\4\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u008a\n")
        buf.write("\6\3\6\3\6\3\6\3\6\5\6\u0090\n\6\3\7\3\7\3\7\5\7\u0095")
        buf.write("\n\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\6")
        buf.write("\t\u00a3\n\t\r\t\16\t\u00a4\5\t\u00a7\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\5\13\u00b0\n\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00be\n\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ca\n\r\3\16\3\16")
        buf.write("\3\16\3\16\6\16\u00d0\n\16\r\16\16\16\u00d1\5\16\u00d4")
        buf.write("\n\16\3\17\3\17\3\17\3\17\6\17\u00da\n\17\r\17\16\17\u00db")
        buf.write("\5\17\u00de\n\17\3\20\3\20\3\20\3\20\6\20\u00e4\n\20\r")
        buf.write("\20\16\20\u00e5\5\20\u00e8\n\20\3\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\22\7\22\u00f1\n\22\f\22\16\22\u00f4\13\22\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u00fd\n\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0104\n\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\7\26\u010c\n\26\f\26\16\26\u010f\13\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\7\27\u0117\n\27\f\27\16\27")
        buf.write("\u011a\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0122")
        buf.write("\n\30\f\30\16\30\u0125\13\30\3\31\3\31\3\31\5\31\u012a")
        buf.write("\n\31\3\32\3\32\3\32\5\32\u012f\n\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\7\33\u0136\n\33\f\33\16\33\u0139\13\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0143\n\34\3\34")
        buf.write("\5\34\u0146\n\34\7\34\u0148\n\34\f\34\16\34\u014b\13\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\5\35\u0152\n\35\3\35\5\35\u0155")
        buf.write("\n\35\3\35\5\35\u0158\n\35\3\36\3\36\3\36\3\36\5\36\u015e")
        buf.write("\n\36\3\36\3\36\5\36\u0162\n\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u016b\n\37\3 \3 \3 \3 \3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \5 \u0179\n \3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\5!\u0185\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\5\"\u0191\n\"\3#\3#\3#\3#\3#\3$\3$\7$\u019a\n$\f$\16")
        buf.write("$\u019d\13$\3$\5$\u01a0\n$\3%\3%\3%\3%\3%\3%\3&\3&\3&")
        buf.write("\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\5)\u01be\n)\3*\3*\3*\3+\3+\3+\3,\3,\5,\u01c8\n")
        buf.write(",\3,\3,\3-\3-\3-\3-\3-\3-\5-\u01d2\n-\3-\5-\u01d5\n-\3")
        buf.write("-\5-\u01d8\n-\3-\3-\3-\3-\3-\5-\u01df\n-\3-\5-\u01e2\n")
        buf.write("-\7-\u01e4\n-\f-\16-\u01e7\13-\3.\3.\3.\3.\3.\5.\u01ee")
        buf.write("\n.\3.\3.\5.\u01f2\n.\3.\3.\3.\3/\3/\7/\u01f9\n/\f/\16")
        buf.write("/\u01fc\13/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\5\60\u0209\n\60\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u0212\n\61\3\62\3\62\3\62\3\62\3\62\7\62\u0219")
        buf.write("\n\62\f\62\16\62\u021c\13\62\5\62\u021e\n\62\3\62\3\62")
        buf.write("\3\62\7\62\u0223\n\62\f\62\16\62\u0226\13\62\3\62\3\62")
        buf.write("\3\62\7\62\u022b\n\62\f\62\16\62\u022e\13\62\3\62\3\62")
        buf.write("\3\62\7\62\u0233\n\62\f\62\16\62\u0236\13\62\3\62\3\62")
        buf.write("\3\62\7\62\u023b\n\62\f\62\16\62\u023e\13\62\3\62\3\62")
        buf.write("\3\62\7\62\u0243\n\62\f\62\16\62\u0246\13\62\5\62\u0248")
        buf.write("\n\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\7\63\u0251\n")
        buf.write("\63\f\63\16\63\u0254\13\63\5\63\u0256\n\63\3\63\3\63\3")
        buf.write("\64\3\64\3\65\3\65\3\65\3\65\5\65\u0260\n\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\2\b*,.\64\66X\66\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfh\2\n\3\2;<\3\2\23\24\4\2\35\36$\'\3\2()\3")
        buf.write("\2\33\34\3\2 !\4\2\37\37\"#\3\2\f\17\2\u0289\2k\3\2\2")
        buf.write("\2\4q\3\2\2\2\6\u0081\3\2\2\2\b\u0083\3\2\2\2\n\u008f")
        buf.write("\3\2\2\2\f\u0091\3\2\2\2\16\u0099\3\2\2\2\20\u00a6\3\2")
        buf.write("\2\2\22\u00a8\3\2\2\2\24\u00af\3\2\2\2\26\u00bd\3\2\2")
        buf.write("\2\30\u00c9\3\2\2\2\32\u00d3\3\2\2\2\34\u00dd\3\2\2\2")
        buf.write("\36\u00e7\3\2\2\2 \u00e9\3\2\2\2\"\u00ec\3\2\2\2$\u00f5")
        buf.write("\3\2\2\2&\u00fc\3\2\2\2(\u0103\3\2\2\2*\u0105\3\2\2\2")
        buf.write(",\u0110\3\2\2\2.\u011b\3\2\2\2\60\u0129\3\2\2\2\62\u012e")
        buf.write("\3\2\2\2\64\u0130\3\2\2\2\66\u013a\3\2\2\28\u0157\3\2")
        buf.write("\2\2:\u0161\3\2\2\2<\u016a\3\2\2\2>\u0178\3\2\2\2@\u0184")
        buf.write("\3\2\2\2B\u0190\3\2\2\2D\u0192\3\2\2\2F\u0197\3\2\2\2")
        buf.write("H\u01a1\3\2\2\2J\u01a7\3\2\2\2L\u01ad\3\2\2\2N\u01b0\3")
        buf.write("\2\2\2P\u01b6\3\2\2\2R\u01bf\3\2\2\2T\u01c2\3\2\2\2V\u01c5")
        buf.write("\3\2\2\2X\u01d7\3\2\2\2Z\u01e8\3\2\2\2\\\u01f6\3\2\2\2")
        buf.write("^\u0208\3\2\2\2`\u0211\3\2\2\2b\u0213\3\2\2\2d\u024b\3")
        buf.write("\2\2\2f\u0259\3\2\2\2h\u025b\3\2\2\2jl\5\4\3\2kj\3\2\2")
        buf.write("\2lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2no\3\2\2\2op\7\2\2\3p")
        buf.write("\3\3\2\2\2qr\7\22\2\2rt\7;\2\2su\5\b\5\2ts\3\2\2\2tu\3")
        buf.write("\2\2\2uv\3\2\2\2vz\7\64\2\2wy\5\6\4\2xw\3\2\2\2y|\3\2")
        buf.write("\2\2zx\3\2\2\2z{\3\2\2\2{}\3\2\2\2|z\3\2\2\2}~\7\65\2")
        buf.write("\2~\5\3\2\2\2\177\u0082\5\26\f\2\u0080\u0082\5\n\6\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082\7\3\2\2\2\u0083")
        buf.write("\u0084\7\61\2\2\u0084\u0085\7;\2\2\u0085\t\3\2\2\2\u0086")
        buf.write("\u0087\t\2\2\2\u0087\u0089\7*\2\2\u0088\u008a\5\20\t\2")
        buf.write("\u0089\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\3")
        buf.write("\2\2\2\u008b\u008c\7+\2\2\u008c\u0090\5\\/\2\u008d\u0090")
        buf.write("\5\f\7\2\u008e\u0090\5\16\b\2\u008f\u0086\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090\13\3\2\2\2\u0091")
        buf.write("\u0092\7\25\2\2\u0092\u0094\7*\2\2\u0093\u0095\5\20\t")
        buf.write("\2\u0094\u0093\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096")
        buf.write("\3\2\2\2\u0096\u0097\7+\2\2\u0097\u0098\5\\/\2\u0098\r")
        buf.write("\3\2\2\2\u0099\u009a\7\26\2\2\u009a\u009b\7*\2\2\u009b")
        buf.write("\u009c\7+\2\2\u009c\u009d\5\\/\2\u009d\17\3\2\2\2\u009e")
        buf.write("\u00a7\5\22\n\2\u009f\u00a2\5\22\n\2\u00a0\u00a1\7\63")
        buf.write("\2\2\u00a1\u00a3\5\22\n\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\u00a7\3\2\2\2\u00a6\u009e\3\2\2\2\u00a6\u009f\3\2\2\2")
        buf.write("\u00a7\21\3\2\2\2\u00a8\u00a9\5\32\16\2\u00a9\u00aa\7")
        buf.write("\61\2\2\u00aa\u00ab\5\24\13\2\u00ab\23\3\2\2\2\u00ac\u00b0")
        buf.write("\5f\64\2\u00ad\u00b0\7;\2\2\u00ae\u00b0\5h\65\2\u00af")
        buf.write("\u00ac\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00b0\25\3\2\2\2\u00b1\u00b2\t\3\2\2\u00b2\u00b3\5\34")
        buf.write("\17\2\u00b3\u00b4\7\61\2\2\u00b4\u00b5\5\24\13\2\u00b5")
        buf.write("\u00b6\7\63\2\2\u00b6\u00be\3\2\2\2\u00b7\u00b8\t\3\2")
        buf.write("\2\u00b8\u00b9\t\2\2\2\u00b9\u00ba\5\30\r\2\u00ba\u00bb")
        buf.write("\5&\24\2\u00bb\u00bc\7\63\2\2\u00bc\u00be\3\2\2\2\u00bd")
        buf.write("\u00b1\3\2\2\2\u00bd\u00b7\3\2\2\2\u00be\27\3\2\2\2\u00bf")
        buf.write("\u00c0\7\61\2\2\u00c0\u00c1\5\24\13\2\u00c1\u00c2\7\31")
        buf.write("\2\2\u00c2\u00ca\3\2\2\2\u00c3\u00c4\7\60\2\2\u00c4\u00c5")
        buf.write("\t\2\2\2\u00c5\u00c6\5\30\r\2\u00c6\u00c7\5&\24\2\u00c7")
        buf.write("\u00c8\7\60\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00bf\3\2\2")
        buf.write("\2\u00c9\u00c3\3\2\2\2\u00ca\31\3\2\2\2\u00cb\u00d4\7")
        buf.write(";\2\2\u00cc\u00cf\7;\2\2\u00cd\u00ce\7\60\2\2\u00ce\u00d0")
        buf.write("\7;\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d4\3\2\2\2")
        buf.write("\u00d3\u00cb\3\2\2\2\u00d3\u00cc\3\2\2\2\u00d4\33\3\2")
        buf.write("\2\2\u00d5\u00de\t\2\2\2\u00d6\u00d9\t\2\2\2\u00d7\u00d8")
        buf.write("\7\60\2\2\u00d8\u00da\t\2\2\2\u00d9\u00d7\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2")
        buf.write("\u00dc\u00de\3\2\2\2\u00dd\u00d5\3\2\2\2\u00dd\u00d6\3")
        buf.write("\2\2\2\u00de\35\3\2\2\2\u00df\u00e8\5&\24\2\u00e0\u00e3")
        buf.write("\5&\24\2\u00e1\u00e2\7\60\2\2\u00e2\u00e4\5&\24\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e3\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00df\3")
        buf.write("\2\2\2\u00e7\u00e0\3\2\2\2\u00e8\37\3\2\2\2\u00e9\u00ea")
        buf.write("\5&\24\2\u00ea\u00eb\5\"\22\2\u00eb!\3\2\2\2\u00ec\u00ed")
        buf.write("\7,\2\2\u00ed\u00ee\5&\24\2\u00ee\u00f2\7-\2\2\u00ef\u00f1")
        buf.write("\5\"\22\2\u00f0\u00ef\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3#\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f5\u00f6\t\4\2\2\u00f6%\3\2\2\2\u00f7")
        buf.write("\u00f8\5(\25\2\u00f8\u00f9\t\5\2\2\u00f9\u00fa\5(\25\2")
        buf.write("\u00fa\u00fd\3\2\2\2\u00fb\u00fd\5(\25\2\u00fc\u00f7\3")
        buf.write("\2\2\2\u00fc\u00fb\3\2\2\2\u00fd\'\3\2\2\2\u00fe\u00ff")
        buf.write("\5*\26\2\u00ff\u0100\5$\23\2\u0100\u0101\5*\26\2\u0101")
        buf.write("\u0104\3\2\2\2\u0102\u0104\5*\26\2\u0103\u00fe\3\2\2\2")
        buf.write("\u0103\u0102\3\2\2\2\u0104)\3\2\2\2\u0105\u0106\b\26\1")
        buf.write("\2\u0106\u0107\5,\27\2\u0107\u010d\3\2\2\2\u0108\u0109")
        buf.write("\f\4\2\2\u0109\u010a\t\6\2\2\u010a\u010c\5,\27\2\u010b")
        buf.write("\u0108\3\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2")
        buf.write("\u010d\u010e\3\2\2\2\u010e+\3\2\2\2\u010f\u010d\3\2\2")
        buf.write("\2\u0110\u0111\b\27\1\2\u0111\u0112\5.\30\2\u0112\u0118")
        buf.write("\3\2\2\2\u0113\u0114\f\4\2\2\u0114\u0115\t\7\2\2\u0115")
        buf.write("\u0117\5.\30\2\u0116\u0113\3\2\2\2\u0117\u011a\3\2\2\2")
        buf.write("\u0118\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119-\3\2\2")
        buf.write("\2\u011a\u0118\3\2\2\2\u011b\u011c\b\30\1\2\u011c\u011d")
        buf.write("\5\60\31\2\u011d\u0123\3\2\2\2\u011e\u011f\f\4\2\2\u011f")
        buf.write("\u0120\t\b\2\2\u0120\u0122\5\60\31\2\u0121\u011e\3\2\2")
        buf.write("\2\u0122\u0125\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124")
        buf.write("\3\2\2\2\u0124/\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0127")
        buf.write("\7\32\2\2\u0127\u012a\5\60\31\2\u0128\u012a\5\62\32\2")
        buf.write("\u0129\u0126\3\2\2\2\u0129\u0128\3\2\2\2\u012a\61\3\2")
        buf.write("\2\2\u012b\u012c\7!\2\2\u012c\u012f\5\62\32\2\u012d\u012f")
        buf.write("\5\64\33\2\u012e\u012b\3\2\2\2\u012e\u012d\3\2\2\2\u012f")
        buf.write("\63\3\2\2\2\u0130\u0131\b\33\1\2\u0131\u0132\5\66\34\2")
        buf.write("\u0132\u0137\3\2\2\2\u0133\u0134\f\4\2\2\u0134\u0136\5")
        buf.write("\"\22\2\u0135\u0133\3\2\2\2\u0136\u0139\3\2\2\2\u0137")
        buf.write("\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\65\3\2\2\2\u0139")
        buf.write("\u0137\3\2\2\2\u013a\u013b\b\34\1\2\u013b\u013c\58\35")
        buf.write("\2\u013c\u0149\3\2\2\2\u013d\u013e\f\4\2\2\u013e\u013f")
        buf.write("\7.\2\2\u013f\u0145\7;\2\2\u0140\u0142\7*\2\2\u0141\u0143")
        buf.write("\5\36\20\2\u0142\u0141\3\2\2\2\u0142\u0143\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\u0146\7+\2\2\u0145\u0140\3\2\2\2")
        buf.write("\u0145\u0146\3\2\2\2\u0146\u0148\3\2\2\2\u0147\u013d\3")
        buf.write("\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a")
        buf.write("\3\2\2\2\u014a\67\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u014d")
        buf.write("\7;\2\2\u014d\u014e\7\62\2\2\u014e\u0154\7<\2\2\u014f")
        buf.write("\u0151\7*\2\2\u0150\u0152\5\36\20\2\u0151\u0150\3\2\2")
        buf.write("\2\u0151\u0152\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0155")
        buf.write("\7+\2\2\u0154\u014f\3\2\2\2\u0154\u0155\3\2\2\2\u0155")
        buf.write("\u0158\3\2\2\2\u0156\u0158\5:\36\2\u0157\u014c\3\2\2\2")
        buf.write("\u0157\u0156\3\2\2\2\u01589\3\2\2\2\u0159\u015a\7\27\2")
        buf.write("\2\u015a\u015b\7;\2\2\u015b\u015d\7*\2\2\u015c\u015e\5")
        buf.write("\36\20\2\u015d\u015c\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\u0162\7+\2\2\u0160\u0162\5<\37\2")
        buf.write("\u0161\u0159\3\2\2\2\u0161\u0160\3\2\2\2\u0162;\3\2\2")
        buf.write("\2\u0163\u016b\5`\61\2\u0164\u016b\7\21\2\2\u0165\u016b")
        buf.write("\7;\2\2\u0166\u0167\7*\2\2\u0167\u0168\5&\24\2\u0168\u0169")
        buf.write("\7+\2\2\u0169\u016b\3\2\2\2\u016a\u0163\3\2\2\2\u016a")
        buf.write("\u0164\3\2\2\2\u016a\u0165\3\2\2\2\u016a\u0166\3\2\2\2")
        buf.write("\u016b=\3\2\2\2\u016c\u016d\t\3\2\2\u016d\u016e\5\32\16")
        buf.write("\2\u016e\u016f\7\61\2\2\u016f\u0170\5\24\13\2\u0170\u0171")
        buf.write("\7\63\2\2\u0171\u0179\3\2\2\2\u0172\u0173\t\3\2\2\u0173")
        buf.write("\u0174\7;\2\2\u0174\u0175\5@!\2\u0175\u0176\5&\24\2\u0176")
        buf.write("\u0177\7\63\2\2\u0177\u0179\3\2\2\2\u0178\u016c\3\2\2")
        buf.write("\2\u0178\u0172\3\2\2\2\u0179?\3\2\2\2\u017a\u017b\7\61")
        buf.write("\2\2\u017b\u017c\5\24\13\2\u017c\u017d\7\31\2\2\u017d")
        buf.write("\u0185\3\2\2\2\u017e\u017f\7\60\2\2\u017f\u0180\7;\2\2")
        buf.write("\u0180\u0181\5@!\2\u0181\u0182\5&\24\2\u0182\u0183\7\60")
        buf.write("\2\2\u0183\u0185\3\2\2\2\u0184\u017a\3\2\2\2\u0184\u017e")
        buf.write("\3\2\2\2\u0185A\3\2\2\2\u0186\u0191\3\2\2\2\u0187\u0188")
        buf.write("\5X-\2\u0188\u0189\7.\2\2\u0189\u018a\7;\2\2\u018a\u0191")
        buf.write("\3\2\2\2\u018b\u018c\7;\2\2\u018c\u018d\7\62\2\2\u018d")
        buf.write("\u0191\7<\2\2\u018e\u0191\7;\2\2\u018f\u0191\5 \21\2\u0190")
        buf.write("\u0186\3\2\2\2\u0190\u0187\3\2\2\2\u0190\u018b\3\2\2\2")
        buf.write("\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191C\3\2\2")
        buf.write("\2\u0192\u0193\5B\"\2\u0193\u0194\7\31\2\2\u0194\u0195")
        buf.write("\5&\24\2\u0195\u0196\7\63\2\2\u0196E\3\2\2\2\u0197\u019b")
        buf.write("\5H%\2\u0198\u019a\5J&\2\u0199\u0198\3\2\2\2\u019a\u019d")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019e\u01a0\5L\'\2")
        buf.write("\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0G\3\2\2")
        buf.write("\2\u01a1\u01a2\7\6\2\2\u01a2\u01a3\7*\2\2\u01a3\u01a4")
        buf.write("\5&\24\2\u01a4\u01a5\7+\2\2\u01a5\u01a6\5\\/\2\u01a6I")
        buf.write("\3\2\2\2\u01a7\u01a8\7\7\2\2\u01a8\u01a9\7*\2\2\u01a9")
        buf.write("\u01aa\5&\24\2\u01aa\u01ab\7+\2\2\u01ab\u01ac\5\\/\2\u01ac")
        buf.write("K\3\2\2\2\u01ad\u01ae\7\b\2\2\u01ae\u01af\5\\/\2\u01af")
        buf.write("M\3\2\2\2\u01b0\u01b1\7\t\2\2\u01b1\u01b2\7*\2\2\u01b2")
        buf.write("\u01b3\5P)\2\u01b3\u01b4\7+\2\2\u01b4\u01b5\5\\/\2\u01b5")
        buf.write("O\3\2\2\2\u01b6\u01b7\5X-\2\u01b7\u01b8\7\13\2\2\u01b8")
        buf.write("\u01b9\5&\24\2\u01b9\u01ba\7/\2\2\u01ba\u01bd\5&\24\2")
        buf.write("\u01bb\u01bc\7\30\2\2\u01bc\u01be\5&\24\2\u01bd\u01bb")
        buf.write("\3\2\2\2\u01bd\u01be\3\2\2\2\u01beQ\3\2\2\2\u01bf\u01c0")
        buf.write("\7\4\2\2\u01c0\u01c1\7\63\2\2\u01c1S\3\2\2\2\u01c2\u01c3")
        buf.write("\7\5\2\2\u01c3\u01c4\7\63\2\2\u01c4U\3\2\2\2\u01c5\u01c7")
        buf.write("\7\20\2\2\u01c6\u01c8\5&\24\2\u01c7\u01c6\3\2\2\2\u01c7")
        buf.write("\u01c8\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\7\63\2")
        buf.write("\2\u01caW\3\2\2\2\u01cb\u01cc\b-\1\2\u01cc\u01cd\7;\2")
        buf.write("\2\u01cd\u01ce\7\62\2\2\u01ce\u01d4\7<\2\2\u01cf\u01d1")
        buf.write("\7*\2\2\u01d0\u01d2\5\36\20\2\u01d1\u01d0\3\2\2\2\u01d1")
        buf.write("\u01d2\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d5\7+\2\2")
        buf.write("\u01d4\u01cf\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d8\3")
        buf.write("\2\2\2\u01d6\u01d8\5:\36\2\u01d7\u01cb\3\2\2\2\u01d7\u01d6")
        buf.write("\3\2\2\2\u01d8\u01e5\3\2\2\2\u01d9\u01da\f\5\2\2\u01da")
        buf.write("\u01db\7.\2\2\u01db\u01e1\7;\2\2\u01dc\u01de\7*\2\2\u01dd")
        buf.write("\u01df\5\36\20\2\u01de\u01dd\3\2\2\2\u01de\u01df\3\2\2")
        buf.write("\2\u01df\u01e0\3\2\2\2\u01e0\u01e2\7+\2\2\u01e1\u01dc")
        buf.write("\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3")
        buf.write("\u01d9\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e6Y\3\2\2\2\u01e7\u01e5\3\2\2")
        buf.write("\2\u01e8\u01ed\5X-\2\u01e9\u01ea\7.\2\2\u01ea\u01ee\7")
        buf.write(";\2\2\u01eb\u01ec\7\62\2\2\u01ec\u01ee\7<\2\2\u01ed\u01e9")
        buf.write("\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef")
        buf.write("\u01f1\7*\2\2\u01f0\u01f2\5\36\20\2\u01f1\u01f0\3\2\2")
        buf.write("\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4")
        buf.write("\7+\2\2\u01f4\u01f5\7\63\2\2\u01f5[\3\2\2\2\u01f6\u01fa")
        buf.write("\7\64\2\2\u01f7\u01f9\5^\60\2\u01f8\u01f7\3\2\2\2\u01f9")
        buf.write("\u01fc\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2")
        buf.write("\u01fb\u01fd\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd\u01fe\7")
        buf.write("\65\2\2\u01fe]\3\2\2\2\u01ff\u0209\5> \2\u0200\u0209\5")
        buf.write("D#\2\u0201\u0209\5F$\2\u0202\u0209\5N(\2\u0203\u0209\5")
        buf.write("R*\2\u0204\u0209\5T+\2\u0205\u0209\5V,\2\u0206\u0209\5")
        buf.write("Z.\2\u0207\u0209\5\\/\2\u0208\u01ff\3\2\2\2\u0208\u0200")
        buf.write("\3\2\2\2\u0208\u0201\3\2\2\2\u0208\u0202\3\2\2\2\u0208")
        buf.write("\u0203\3\2\2\2\u0208\u0204\3\2\2\2\u0208\u0205\3\2\2\2")
        buf.write("\u0208\u0206\3\2\2\2\u0208\u0207\3\2\2\2\u0209_\3\2\2")
        buf.write("\2\u020a\u0212\7\67\2\2\u020b\u0212\7\66\2\2\u020c\u0212")
        buf.write("\78\2\2\u020d\u0212\79\2\2\u020e\u0212\7:\2\2\u020f\u0212")
        buf.write("\5b\62\2\u0210\u0212\5d\63\2\u0211\u020a\3\2\2\2\u0211")
        buf.write("\u020b\3\2\2\2\u0211\u020c\3\2\2\2\u0211\u020d\3\2\2\2")
        buf.write("\u0211\u020e\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0210\3")
        buf.write("\2\2\2\u0212a\3\2\2\2\u0213\u0214\7\n\2\2\u0214\u0247")
        buf.write("\7*\2\2\u0215\u021a\7\67\2\2\u0216\u0217\7\60\2\2\u0217")
        buf.write("\u0219\7\67\2\2\u0218\u0216\3\2\2\2\u0219\u021c\3\2\2")
        buf.write("\2\u021a\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021e")
        buf.write("\3\2\2\2\u021c\u021a\3\2\2\2\u021d\u0215\3\2\2\2\u021d")
        buf.write("\u021e\3\2\2\2\u021e\u0248\3\2\2\2\u021f\u0224\7\66\2")
        buf.write("\2\u0220\u0221\7\60\2\2\u0221\u0223\7\66\2\2\u0222\u0220")
        buf.write("\3\2\2\2\u0223\u0226\3\2\2\2\u0224\u0222\3\2\2\2\u0224")
        buf.write("\u0225\3\2\2\2\u0225\u0248\3\2\2\2\u0226\u0224\3\2\2\2")
        buf.write("\u0227\u022c\78\2\2\u0228\u0229\7\60\2\2\u0229\u022b\7")
        buf.write("8\2\2\u022a\u0228\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022a")
        buf.write("\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u0248\3\2\2\2\u022e")
        buf.write("\u022c\3\2\2\2\u022f\u0234\79\2\2\u0230\u0231\7\60\2\2")
        buf.write("\u0231\u0233\79\2\2\u0232\u0230\3\2\2\2\u0233\u0236\3")
        buf.write("\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0248")
        buf.write("\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u023c\7:\2\2\u0238")
        buf.write("\u0239\7\60\2\2\u0239\u023b\7:\2\2\u023a\u0238\3\2\2\2")
        buf.write("\u023b\u023e\3\2\2\2\u023c\u023a\3\2\2\2\u023c\u023d\3")
        buf.write("\2\2\2\u023d\u0248\3\2\2\2\u023e\u023c\3\2\2\2\u023f\u0244")
        buf.write("\5b\62\2\u0240\u0241\7\60\2\2\u0241\u0243\5b\62\2\u0242")
        buf.write("\u0240\3\2\2\2\u0243\u0246\3\2\2\2\u0244\u0242\3\2\2\2")
        buf.write("\u0244\u0245\3\2\2\2\u0245\u0248\3\2\2\2\u0246\u0244\3")
        buf.write("\2\2\2\u0247\u021d\3\2\2\2\u0247\u021f\3\2\2\2\u0247\u0227")
        buf.write("\3\2\2\2\u0247\u022f\3\2\2\2\u0247\u0237\3\2\2\2\u0247")
        buf.write("\u023f\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024a\7+\2\2")
        buf.write("\u024ac\3\2\2\2\u024b\u024c\7\n\2\2\u024c\u0255\7*\2\2")
        buf.write("\u024d\u0252\5b\62\2\u024e\u024f\7\60\2\2\u024f\u0251")
        buf.write("\5b\62\2\u0250\u024e\3\2\2\2\u0251\u0254\3\2\2\2\u0252")
        buf.write("\u0250\3\2\2\2\u0252\u0253\3\2\2\2\u0253\u0256\3\2\2\2")
        buf.write("\u0254\u0252\3\2\2\2\u0255\u024d\3\2\2\2\u0255\u0256\3")
        buf.write("\2\2\2\u0256\u0257\3\2\2\2\u0257\u0258\7+\2\2\u0258e\3")
        buf.write("\2\2\2\u0259\u025a\t\t\2\2\u025ag\3\2\2\2\u025b\u025c")
        buf.write("\7\n\2\2\u025c\u025f\7,\2\2\u025d\u0260\5f\64\2\u025e")
        buf.write("\u0260\5h\65\2\u025f\u025d\3\2\2\2\u025f\u025e\3\2\2\2")
        buf.write("\u0260\u0261\3\2\2\2\u0261\u0262\7\60\2\2\u0262\u0263")
        buf.write("\7\66\2\2\u0263\u0264\7-\2\2\u0264i\3\2\2\2Cmtz\u0081")
        buf.write("\u0089\u008f\u0094\u00a4\u00a6\u00af\u00bd\u00c9\u00d1")
        buf.write("\u00d3\u00db\u00dd\u00e5\u00e7\u00f2\u00fc\u0103\u010d")
        buf.write("\u0118\u0123\u0129\u012e\u0137\u0142\u0145\u0149\u0151")
        buf.write("\u0154\u0157\u015d\u0161\u016a\u0178\u0184\u0190\u019b")
        buf.write("\u019f\u01bd\u01c7\u01d1\u01d4\u01d7\u01de\u01e1\u01e5")
        buf.write("\u01ed\u01f1\u01fa\u0208\u0211\u021a\u021d\u0224\u022c")
        buf.write("\u0234\u023c\u0244\u0247\u0252\u0255\u025f")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
                     "'Constructor'", "'Destructor'", "'New'", "'By'", "'='", 
                     "'!'", "'||'", "'&&'", "'=='", "'!='", "'%'", "'+'", 
                     "'-'", "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", 
                     "'+.'", "'==.'", "'('", "')'", "'['", "']'", "'.'", 
                     "'..'", "','", "':'", "'::'", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", 
                      "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", 
                      "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", "K_RETURN", 
                      "K_NULL", "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", 
                      "K_DESTRUCTOR", "K_NEW", "K_BY", "OP_ASSIGN", "OP_LOGICAL_NOT", 
                      "OP_LOGICAL_OR", "OP_LOGICAL_AND", "OP_IS_EQUAL_TO", 
                      "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", "OP_SUBTRACTION", 
                      "OP_MULTIPLICATION", "OP_DIVISION", "OP_LESS_THAN", 
                      "OP_LESS_THAN_EQUAL", "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", 
                      "OP_STRING_CONCATENATION", "OP_TWO_SAME_STRING", "LEFT_PAREN", 
                      "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                      "DOT", "DOUBLE_DOT", "COMMA", "COLON", "DOUBLE_COLON", 
                      "SEMI_COLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                      "INTEGER_LITERAL2", "INTEGER_LITERAL", "FLOAT_LITERAL", 
                      "BOOLEAN_LITERAL", "STRING_LITERAL", "IDENTIFIER", 
                      "DOLAR_IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declaration = 1
    RULE_class_body_unit = 2
    RULE_super_class_group = 3
    RULE_method_declaration = 4
    RULE_constructor = 5
    RULE_destructor = 6
    RULE_parameter_list = 7
    RULE_parameter = 8
    RULE_d96_type = 9
    RULE_attribute_declaration = 10
    RULE_attribute_value_list = 11
    RULE_identifier_list = 12
    RULE_mixed_identifier_list = 13
    RULE_expression_list = 14
    RULE_element_expression = 15
    RULE_index_operator = 16
    RULE_relational_operator = 17
    RULE_expression = 18
    RULE_relational_expr = 19
    RULE_and_or_expr = 20
    RULE_add_sub_expr = 21
    RULE_mul_add_mol_expr = 22
    RULE_not_expr = 23
    RULE_sign_expr = 24
    RULE_index_operator_expr = 25
    RULE_instance_access = 26
    RULE_static_access = 27
    RULE_object_creation = 28
    RULE_atom_expr = 29
    RULE_var_val_statement = 30
    RULE_var_val_value_list = 31
    RULE_lhs = 32
    RULE_assign_statement = 33
    RULE_if_statement = 34
    RULE_if_part = 35
    RULE_else_if_part = 36
    RULE_else_part = 37
    RULE_for_in_statement = 38
    RULE_loop_part = 39
    RULE_break_statement = 40
    RULE_continue_statement = 41
    RULE_return_statement = 42
    RULE_member_access = 43
    RULE_method_invocation_statement = 44
    RULE_block_statement = 45
    RULE_statement = 46
    RULE_literal = 47
    RULE_indexed_array = 48
    RULE_multi_dimentional_array = 49
    RULE_primitive_type = 50
    RULE_array_type = 51

    ruleNames =  [ "program", "class_declaration", "class_body_unit", "super_class_group", 
                   "method_declaration", "constructor", "destructor", "parameter_list", 
                   "parameter", "d96_type", "attribute_declaration", "attribute_value_list", 
                   "identifier_list", "mixed_identifier_list", "expression_list", 
                   "element_expression", "index_operator", "relational_operator", 
                   "expression", "relational_expr", "and_or_expr", "add_sub_expr", 
                   "mul_add_mol_expr", "not_expr", "sign_expr", "index_operator_expr", 
                   "instance_access", "static_access", "object_creation", 
                   "atom_expr", "var_val_statement", "var_val_value_list", 
                   "lhs", "assign_statement", "if_statement", "if_part", 
                   "else_if_part", "else_part", "for_in_statement", "loop_part", 
                   "break_statement", "continue_statement", "return_statement", 
                   "member_access", "method_invocation_statement", "block_statement", 
                   "statement", "literal", "indexed_array", "multi_dimentional_array", 
                   "primitive_type", "array_type" ]

    EOF = Token.EOF
    COMMENT=1
    K_BREAK=2
    K_CONTINUE=3
    K_IF=4
    K_ELSE_IF=5
    K_ELSE=6
    K_FOR_EACH=7
    K_ARRAY=8
    K_IN=9
    K_INT=10
    K_FLOAT=11
    K_BOOLEAN=12
    K_STRING=13
    K_RETURN=14
    K_NULL=15
    K_CLASS=16
    K_VAL=17
    K_VAR=18
    K_CONSTRUCTOR=19
    K_DESTRUCTOR=20
    K_NEW=21
    K_BY=22
    OP_ASSIGN=23
    OP_LOGICAL_NOT=24
    OP_LOGICAL_OR=25
    OP_LOGICAL_AND=26
    OP_IS_EQUAL_TO=27
    OP_NOT_EQUAL_TO=28
    OP_MODULO=29
    OP_ADDTION=30
    OP_SUBTRACTION=31
    OP_MULTIPLICATION=32
    OP_DIVISION=33
    OP_LESS_THAN=34
    OP_LESS_THAN_EQUAL=35
    OP_GREATER_THAN=36
    OP_GREATER_THAN_EQUAL=37
    OP_STRING_CONCATENATION=38
    OP_TWO_SAME_STRING=39
    LEFT_PAREN=40
    RIGHT_PAREN=41
    LEFT_SQUARE_BRACKET=42
    RIGHT_SQUARE_BRACKET=43
    DOT=44
    DOUBLE_DOT=45
    COMMA=46
    COLON=47
    DOUBLE_COLON=48
    SEMI_COLON=49
    LEFT_CURLY_BRACKET=50
    RIGHT_CURLY_BRACKET=51
    INTEGER_LITERAL2=52
    INTEGER_LITERAL=53
    FLOAT_LITERAL=54
    BOOLEAN_LITERAL=55
    STRING_LITERAL=56
    IDENTIFIER=57
    DOLAR_IDENTIFIER=58
    WS=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_CHAR=62

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

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declarationContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.class_declaration()
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.K_CLASS):
                    break

            self.state = 109
            self.match(D96Parser.EOF)
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

        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def super_class_group(self):
            return self.getTypedRuleContext(D96Parser.Super_class_groupContext,0)


        def class_body_unit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_body_unitContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_body_unitContext,i)


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
        self.enterRule(localctx, 2, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(D96Parser.K_CLASS)
            self.state = 112
            self.match(D96Parser.IDENTIFIER)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 113
                self.super_class_group()


            self.state = 116
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 117
                self.class_body_unit()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
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
        self.enterRule(localctx, 4, self.RULE_class_body_unit)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_VAL, D96Parser.K_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.attribute_declaration()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR, D96Parser.K_DESTRUCTOR, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
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
        self.enterRule(localctx, 6, self.RULE_super_class_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(D96Parser.COLON)
            self.state = 130
            self.match(D96Parser.IDENTIFIER)
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

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

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
        self.enterRule(localctx, 8, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                _la = self._input.LA(1)
                if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self.match(D96Parser.LEFT_PAREN)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 134
                    self.parameter_list()


                self.state = 137
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 138
                self.block_statement()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.constructor()
                pass
            elif token in [D96Parser.K_DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
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
        self.enterRule(localctx, 10, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(D96Parser.K_CONSTRUCTOR)
            self.state = 144
            self.match(D96Parser.LEFT_PAREN)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDENTIFIER:
                self.state = 145
                self.parameter_list()


            self.state = 148
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 149
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
        self.enterRule(localctx, 12, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(D96Parser.K_DESTRUCTOR)
            self.state = 152
            self.match(D96Parser.LEFT_PAREN)
            self.state = 153
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 154
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
        self.enterRule(localctx, 14, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.parameter()
                self.state = 160 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 158
                    self.match(D96Parser.SEMI_COLON)
                    self.state = 159
                    self.parameter()
                    self.state = 162 
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

        def d96_type(self):
            return self.getTypedRuleContext(D96Parser.D96_typeContext,0)


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
        self.enterRule(localctx, 16, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.identifier_list()
            self.state = 167
            self.match(D96Parser.COLON)
            self.state = 168
            self.d96_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class D96_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_d96_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterD96_type" ):
                listener.enterD96_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitD96_type" ):
                listener.exitD96_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitD96_type" ):
                return visitor.visitD96_type(self)
            else:
                return visitor.visitChildren(self)




    def d96_type(self):

        localctx = D96Parser.D96_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_d96_type)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_INT, D96Parser.K_FLOAT, D96Parser.K_BOOLEAN, D96Parser.K_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.primitive_type()
                pass
            elif token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.array_type()
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


    class Attribute_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mixed_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Mixed_identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96_type(self):
            return self.getTypedRuleContext(D96Parser.D96_typeContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

        def attribute_value_list(self):
            return self.getTypedRuleContext(D96Parser.Attribute_value_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

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
        self.enterRule(localctx, 20, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                _la = self._input.LA(1)
                if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 176
                self.mixed_identifier_list()
                self.state = 177
                self.match(D96Parser.COLON)
                self.state = 178
                self.d96_type()
                self.state = 179
                self.match(D96Parser.SEMI_COLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                _la = self._input.LA(1)
                if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 182
                _la = self._input.LA(1)
                if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 183
                self.attribute_value_list()
                self.state = 184
                self.expression()
                self.state = 185
                self.match(D96Parser.SEMI_COLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_value_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96_type(self):
            return self.getTypedRuleContext(D96Parser.D96_typeContext,0)


        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def attribute_value_list(self):
            return self.getTypedRuleContext(D96Parser.Attribute_value_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_value_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_value_list" ):
                listener.enterAttribute_value_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_value_list" ):
                listener.exitAttribute_value_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_value_list" ):
                return visitor.visitAttribute_value_list(self)
            else:
                return visitor.visitChildren(self)




    def attribute_value_list(self):

        localctx = D96Parser.Attribute_value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attribute_value_list)
        self._la = 0 # Token type
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(D96Parser.COLON)
                self.state = 190
                self.d96_type()
                self.state = 191
                self.match(D96Parser.OP_ASSIGN)
                pass
            elif token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(D96Parser.COMMA)
                self.state = 194
                _la = self._input.LA(1)
                if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 195
                self.attribute_value_list()
                self.state = 196
                self.expression()
                self.state = 197
                self.match(D96Parser.COMMA)
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
        self.enterRule(localctx, 24, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(D96Parser.IDENTIFIER)
                self.state = 205 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 203
                    self.match(D96Parser.COMMA)
                    self.state = 204
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 207 
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


    class Mixed_identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

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
            return D96Parser.RULE_mixed_identifier_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMixed_identifier_list" ):
                listener.enterMixed_identifier_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMixed_identifier_list" ):
                listener.exitMixed_identifier_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMixed_identifier_list" ):
                return visitor.visitMixed_identifier_list(self)
            else:
                return visitor.visitChildren(self)




    def mixed_identifier_list(self):

        localctx = D96Parser.Mixed_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_mixed_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                _la = self._input.LA(1)
                if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                _la = self._input.LA(1)
                if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 215 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 213
                    self.match(D96Parser.COMMA)
                    self.state = 214
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 217 
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
        self.enterRule(localctx, 28, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.expression()
                self.state = 225 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 223
                    self.match(D96Parser.COMMA)
                    self.state = 224
                    self.expression()
                    self.state = 227 
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
        self.enterRule(localctx, 30, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.expression()
            self.state = 232
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
        self.enterRule(localctx, 32, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 235
            self.expression()
            self.state = 236
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
            self.state = 240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 237
                    self.index_operator() 
                self.state = 242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
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

        def relational_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Relational_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.Relational_exprContext,i)


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




    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.relational_expr()
                self.state = 246
                _la = self._input.LA(1)
                if not(_la==D96Parser.OP_STRING_CONCATENATION or _la==D96Parser.OP_TWO_SAME_STRING):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 247
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.relational_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_or_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.And_or_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.And_or_exprContext,i)


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




    def relational_expr(self):

        localctx = D96Parser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relational_expr)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.and_or_expr(0)
                self.state = 253
                self.relational_operator()
                self.state = 254
                self.and_or_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.and_or_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_and_or_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.add_sub_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.And_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_or_expr)
                    self.state = 262
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 263
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_LOGICAL_OR or _la==D96Parser.OP_LOGICAL_AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 264
                    self.add_sub_expr(0) 
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_add_sub_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.mul_add_mol_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Add_sub_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expr)
                    self.state = 273
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 274
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_ADDTION or _la==D96Parser.OP_SUBTRACTION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 275
                    self.mul_add_mol_expr(0) 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_mul_add_mol_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 289
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Mul_add_mol_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_add_mol_expr)
                    self.state = 284
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 285
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MODULO) | (1 << D96Parser.OP_MULTIPLICATION) | (1 << D96Parser.OP_DIVISION))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 286
                    self.not_expr() 
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
        self.enterRule(localctx, 46, self.RULE_not_expr)
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(D96Parser.OP_LOGICAL_NOT)
                self.state = 293
                self.not_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_NEW, D96Parser.OP_SUBTRACTION, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
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
        self.enterRule(localctx, 48, self.RULE_sign_expr)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUBTRACTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(D96Parser.OP_SUBTRACTION)
                self.state = 298
                self.sign_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_NEW, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
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

        def instance_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_accessContext,0)


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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_index_operator_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.instance_access(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operator_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operator_expr)
                    self.state = 305
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 306
                    self.index_operator() 
                self.state = 311
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Instance_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_access(self):
            return self.getTypedRuleContext(D96Parser.Static_accessContext,0)


        def instance_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_accessContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstance_access" ):
                listener.enterInstance_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstance_access" ):
                listener.exitInstance_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_access" ):
                return visitor.visitInstance_access(self)
            else:
                return visitor.visitChildren(self)



    def instance_access(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Instance_accessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_instance_access, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.static_access()
            self._ctx.stop = self._input.LT(-1)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Instance_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_access)
                    self.state = 315
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 316
                    self.match(D96Parser.DOT)
                    self.state = 317
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 323
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        self.state = 318
                        self.match(D96Parser.LEFT_PAREN)
                        self.state = 320
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                            self.state = 319
                            self.expression_list()


                        self.state = 322
                        self.match(D96Parser.RIGHT_PAREN)

             
                self.state = 329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Static_accessContext(ParserRuleContext):
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

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def object_creation(self):
            return self.getTypedRuleContext(D96Parser.Object_creationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatic_access" ):
                listener.enterStatic_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatic_access" ):
                listener.exitStatic_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_access" ):
                return visitor.visitStatic_access(self)
            else:
                return visitor.visitChildren(self)




    def static_access(self):

        localctx = D96Parser.Static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_static_access)
        self._la = 0 # Token type
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.match(D96Parser.IDENTIFIER)
                self.state = 331
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 332
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 338
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 333
                    self.match(D96Parser.LEFT_PAREN)
                    self.state = 335
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                        self.state = 334
                        self.expression_list()


                    self.state = 337
                    self.match(D96Parser.RIGHT_PAREN)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.object_creation()
                pass


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
        self.enterRule(localctx, 56, self.RULE_object_creation)
        self._la = 0 # Token type
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(D96Parser.K_NEW)
                self.state = 344
                self.match(D96Parser.IDENTIFIER)
                self.state = 345
                self.match(D96Parser.LEFT_PAREN)
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 346
                    self.expression_list()


                self.state = 349
                self.match(D96Parser.RIGHT_PAREN)
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
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


        def K_NULL(self):
            return self.getToken(D96Parser.K_NULL, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

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
        self.enterRule(localctx, 58, self.RULE_atom_expr)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_ARRAY, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.literal()
                pass
            elif token in [D96Parser.K_NULL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.match(D96Parser.K_NULL)
                pass
            elif token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 355
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 356
                self.match(D96Parser.LEFT_PAREN)
                self.state = 357
                self.expression()
                self.state = 358
                self.match(D96Parser.RIGHT_PAREN)
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


    class Var_val_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96_type(self):
            return self.getTypedRuleContext(D96Parser.D96_typeContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def var_val_value_list(self):
            return self.getTypedRuleContext(D96Parser.Var_val_value_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


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
        self.enterRule(localctx, 60, self.RULE_var_val_statement)
        self._la = 0 # Token type
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                _la = self._input.LA(1)
                if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 363
                self.identifier_list()
                self.state = 364
                self.match(D96Parser.COLON)
                self.state = 365
                self.d96_type()
                self.state = 366
                self.match(D96Parser.SEMI_COLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                _la = self._input.LA(1)
                if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 369
                self.match(D96Parser.IDENTIFIER)
                self.state = 370
                self.var_val_value_list()
                self.state = 371
                self.expression()
                self.state = 372
                self.match(D96Parser.SEMI_COLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_val_value_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96_type(self):
            return self.getTypedRuleContext(D96Parser.D96_typeContext,0)


        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def var_val_value_list(self):
            return self.getTypedRuleContext(D96Parser.Var_val_value_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_val_value_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_val_value_list" ):
                listener.enterVar_val_value_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_val_value_list" ):
                listener.exitVar_val_value_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_val_value_list" ):
                return visitor.visitVar_val_value_list(self)
            else:
                return visitor.visitChildren(self)




    def var_val_value_list(self):

        localctx = D96Parser.Var_val_value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_var_val_value_list)
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.match(D96Parser.COLON)
                self.state = 377
                self.d96_type()
                self.state = 378
                self.match(D96Parser.OP_ASSIGN)
                pass
            elif token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.match(D96Parser.COMMA)
                self.state = 381
                self.match(D96Parser.IDENTIFIER)
                self.state = 382
                self.var_val_value_list()
                self.state = 383
                self.expression()
                self.state = 384
                self.match(D96Parser.COMMA)
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


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access(self):
            return self.getTypedRuleContext(D96Parser.Member_accessContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def element_expression(self):
            return self.getTypedRuleContext(D96Parser.Element_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhs" ):
                listener.enterLhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhs" ):
                listener.exitLhs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_lhs)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.member_access(0)
                self.state = 390
                self.match(D96Parser.DOT)
                self.state = 391
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 393
                self.match(D96Parser.IDENTIFIER)
                self.state = 394
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 395
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 396
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 397
                self.element_expression()
                pass


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

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

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
        self.enterRule(localctx, 66, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.lhs()
            self.state = 401
            self.match(D96Parser.OP_ASSIGN)
            self.state = 402
            self.expression()
            self.state = 403
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
        self.enterRule(localctx, 68, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.if_part()
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.K_ELSE_IF:
                self.state = 406
                self.else_if_part()
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ELSE:
                self.state = 412
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
        self.enterRule(localctx, 70, self.RULE_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(D96Parser.K_IF)
            self.state = 416
            self.match(D96Parser.LEFT_PAREN)
            self.state = 417
            self.expression()
            self.state = 418
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 419
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
        self.enterRule(localctx, 72, self.RULE_else_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(D96Parser.K_ELSE_IF)
            self.state = 422
            self.match(D96Parser.LEFT_PAREN)
            self.state = 423
            self.expression()
            self.state = 424
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 425
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
        self.enterRule(localctx, 74, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(D96Parser.K_ELSE)
            self.state = 428
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
        self.enterRule(localctx, 76, self.RULE_for_in_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(D96Parser.K_FOR_EACH)
            self.state = 431
            self.match(D96Parser.LEFT_PAREN)
            self.state = 432
            self.loop_part()
            self.state = 433
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 434
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

        def member_access(self):
            return self.getTypedRuleContext(D96Parser.Member_accessContext,0)


        def K_IN(self):
            return self.getToken(D96Parser.K_IN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


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
        self.enterRule(localctx, 78, self.RULE_loop_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.member_access(0)
            self.state = 437
            self.match(D96Parser.K_IN)
            self.state = 438
            self.expression()
            self.state = 439
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 440
            self.expression()
            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_BY:
                self.state = 441
                self.match(D96Parser.K_BY)
                self.state = 442
                self.expression()


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
        self.enterRule(localctx, 80, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(D96Parser.K_BREAK)
            self.state = 446
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
        self.enterRule(localctx, 82, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(D96Parser.K_CONTINUE)
            self.state = 449
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

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


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
        self.enterRule(localctx, 84, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(D96Parser.K_RETURN)
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 452
                self.expression()


            self.state = 455
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_accessContext(ParserRuleContext):
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

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def object_creation(self):
            return self.getTypedRuleContext(D96Parser.Object_creationContext,0)


        def member_access(self):
            return self.getTypedRuleContext(D96Parser.Member_accessContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_member_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_access" ):
                listener.enterMember_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_access" ):
                listener.exitMember_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access" ):
                return visitor.visitMember_access(self)
            else:
                return visitor.visitChildren(self)



    def member_access(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Member_accessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_member_access, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 458
                self.match(D96Parser.IDENTIFIER)
                self.state = 459
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 460
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 466
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 461
                    self.match(D96Parser.LEFT_PAREN)
                    self.state = 463
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                        self.state = 462
                        self.expression_list()


                    self.state = 465
                    self.match(D96Parser.RIGHT_PAREN)


                pass

            elif la_ == 2:
                self.state = 468
                self.object_creation()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 483
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Member_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access)
                    self.state = 471
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 472
                    self.match(D96Parser.DOT)
                    self.state = 473
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 479
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        self.state = 474
                        self.match(D96Parser.LEFT_PAREN)
                        self.state = 476
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                            self.state = 475
                            self.expression_list()


                        self.state = 478
                        self.match(D96Parser.RIGHT_PAREN)

             
                self.state = 485
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Method_invocation_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access(self):
            return self.getTypedRuleContext(D96Parser.Member_accessContext,0)


        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


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
        self.enterRule(localctx, 88, self.RULE_method_invocation_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.member_access(0)
            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOT]:
                self.state = 487
                self.match(D96Parser.DOT)
                self.state = 488
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.DOUBLE_COLON]:
                self.state = 489
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 490
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 493
            self.match(D96Parser.LEFT_PAREN)
            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 494
                self.expression_list()


            self.state = 497
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 498
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
        self.enterRule(localctx, 90, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 504
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_BREAK) | (1 << D96Parser.K_CONTINUE) | (1 << D96Parser.K_IF) | (1 << D96Parser.K_FOR_EACH) | (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_RETURN) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_ASSIGN) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.LEFT_CURLY_BRACKET) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 501
                self.statement()
                self.state = 506
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 507
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


        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


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
        self.enterRule(localctx, 92, self.RULE_statement)
        try:
            self.state = 518
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.var_val_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 511
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 512
                self.for_in_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 513
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 514
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 515
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 516
                self.method_invocation_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 517
                self.block_statement()
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

        def INTEGER_LITERAL2(self):
            return self.getToken(D96Parser.INTEGER_LITERAL2, 0)

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
        self.enterRule(localctx, 94, self.RULE_literal)
        try:
            self.state = 527
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.match(D96Parser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 521
                self.match(D96Parser.INTEGER_LITERAL2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 522
                self.match(D96Parser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 523
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 524
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 525
                self.indexed_array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
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

        def INTEGER_LITERAL2(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.INTEGER_LITERAL2)
            else:
                return self.getToken(D96Parser.INTEGER_LITERAL2, i)

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
        self.enterRule(localctx, 96, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(D96Parser.K_ARRAY)
            self.state = 530
            self.match(D96Parser.LEFT_PAREN)
            self.state = 581
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
            elif token in [D96Parser.INTEGER_LITERAL2]:
                self.state = 541
                self.match(D96Parser.INTEGER_LITERAL2)
                self.state = 546
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 542
                    self.match(D96Parser.COMMA)
                    self.state = 543
                    self.match(D96Parser.INTEGER_LITERAL2)
                    self.state = 548
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.state = 549
                self.match(D96Parser.FLOAT_LITERAL)
                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 550
                    self.match(D96Parser.COMMA)
                    self.state = 551
                    self.match(D96Parser.FLOAT_LITERAL)
                    self.state = 556
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.state = 557
                self.match(D96Parser.BOOLEAN_LITERAL)
                self.state = 562
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 558
                    self.match(D96Parser.COMMA)
                    self.state = 559
                    self.match(D96Parser.BOOLEAN_LITERAL)
                    self.state = 564
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.state = 565
                self.match(D96Parser.STRING_LITERAL)
                self.state = 570
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 566
                    self.match(D96Parser.COMMA)
                    self.state = 567
                    self.match(D96Parser.STRING_LITERAL)
                    self.state = 572
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 573
                self.indexed_array()
                self.state = 578
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 574
                    self.match(D96Parser.COMMA)
                    self.state = 575
                    self.indexed_array()
                    self.state = 580
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 583
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
        self.enterRule(localctx, 98, self.RULE_multi_dimentional_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.match(D96Parser.K_ARRAY)
            self.state = 586
            self.match(D96Parser.LEFT_PAREN)

            self.state = 595
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ARRAY:
                self.state = 587
                self.indexed_array()
                self.state = 592
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 588
                    self.match(D96Parser.COMMA)
                    self.state = 589
                    self.indexed_array()
                    self.state = 594
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 597
            self.match(D96Parser.RIGHT_PAREN)
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
        self.enterRule(localctx, 100, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_INT) | (1 << D96Parser.K_FLOAT) | (1 << D96Parser.K_BOOLEAN) | (1 << D96Parser.K_STRING))) != 0)):
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

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTEGER_LITERAL2(self):
            return self.getToken(D96Parser.INTEGER_LITERAL2, 0)

        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_SQUARE_BRACKET, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


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
        self.enterRule(localctx, 102, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self.match(D96Parser.K_ARRAY)
            self.state = 602
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 605
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_INT, D96Parser.K_FLOAT, D96Parser.K_BOOLEAN, D96Parser.K_STRING]:
                self.state = 603
                self.primitive_type()
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 604
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 607
            self.match(D96Parser.COMMA)
            self.state = 608
            self.match(D96Parser.INTEGER_LITERAL2)
            self.state = 609
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
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
        self._predicates[20] = self.and_or_expr_sempred
        self._predicates[21] = self.add_sub_expr_sempred
        self._predicates[22] = self.mul_add_mol_expr_sempred
        self._predicates[25] = self.index_operator_expr_sempred
        self._predicates[26] = self.instance_access_sempred
        self._predicates[43] = self.member_access_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def and_or_expr_sempred(self, localctx:And_or_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def add_sub_expr_sempred(self, localctx:Add_sub_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def mul_add_mol_expr_sempred(self, localctx:Mul_add_mol_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def index_operator_expr_sempred(self, localctx:Index_operator_exprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def instance_access_sempred(self, localctx:Instance_accessContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def member_access_sempred(self, localctx:Member_accessContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         




