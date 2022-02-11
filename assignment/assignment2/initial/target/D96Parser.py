# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
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
        buf.write("\u0270\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\3\2\6\2n\n\2\r\2\16\2o\3\2\3\2\3")
        buf.write("\3\3\3\3\3\5\3w\n\3\3\3\3\3\7\3{\n\3\f\3\16\3~\13\3\3")
        buf.write("\3\3\3\3\4\3\4\5\4\u0084\n\4\3\5\3\5\3\5\3\6\3\6\3\6\5")
        buf.write("\6\u008c\n\6\3\6\3\6\3\6\3\6\5\6\u0092\n\6\3\7\3\7\3\7")
        buf.write("\5\7\u0097\n\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\6\t\u00a5\n\t\r\t\16\t\u00a6\5\t\u00a9\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\5\13\u00b2\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00c0\n\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00cc\n\r")
        buf.write("\3\16\3\16\3\16\3\16\6\16\u00d2\n\16\r\16\16\16\u00d3")
        buf.write("\5\16\u00d6\n\16\3\17\3\17\3\17\3\17\6\17\u00dc\n\17\r")
        buf.write("\17\16\17\u00dd\5\17\u00e0\n\17\3\20\3\20\3\20\3\20\6")
        buf.write("\20\u00e6\n\20\r\20\16\20\u00e7\5\20\u00ea\n\20\3\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\22\7\22\u00f3\n\22\f\22\16\22")
        buf.write("\u00f6\13\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u00ff")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u0106\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\7\26\u010e\n\26\f\26\16\26\u0111")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0119\n\27\f")
        buf.write("\27\16\27\u011c\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7")
        buf.write("\30\u0124\n\30\f\30\16\30\u0127\13\30\3\31\3\31\3\31\5")
        buf.write("\31\u012c\n\31\3\32\3\32\3\32\5\32\u0131\n\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\7\33\u0138\n\33\f\33\16\33\u013b\13\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0145\n")
        buf.write("\34\3\34\5\34\u0148\n\34\7\34\u014a\n\34\f\34\16\34\u014d")
        buf.write("\13\34\3\35\3\35\3\35\3\35\3\35\5\35\u0154\n\35\3\35\5")
        buf.write("\35\u0157\n\35\3\35\5\35\u015a\n\35\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u0160\n\36\3\36\3\36\5\36\u0164\n\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\5\37\u016d\n\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \5 \u017b\n \3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\5!\u0187\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\5\"\u0192\n\"\3#\3#\3#\3#\3#\3$\3$\7$\u019b\n$\f")
        buf.write("$\16$\u019e\13$\3$\5$\u01a1\n$\3%\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\5)\u01bf\n)\3*\3*\3*\3+\3+\3+\3,\3,\5,\u01c9")
        buf.write("\n,\3,\3,\3-\3-\3-\5-\u01d0\n-\3-\3-\3-\3-\3-\5-\u01d7")
        buf.write("\n-\3-\5-\u01da\n-\7-\u01dc\n-\f-\16-\u01df\13-\3.\3.")
        buf.write("\3.\3.\3.\3.\5.\u01e7\n.\3.\5.\u01ea\n.\3/\3/\3/\3/\3")
        buf.write("/\5/\u01f1\n/\3/\3/\3/\3/\3/\3/\3/\5/\u01fa\n/\3/\5/\u01fd")
        buf.write("\n/\3/\3/\3\60\3\60\7\60\u0203\n\60\f\60\16\60\u0206\13")
        buf.write("\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u0213\n\61\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\5\62\u021c\n\62\3\63\3\63\3\63\3\63\3\63\7\63\u0223")
        buf.write("\n\63\f\63\16\63\u0226\13\63\5\63\u0228\n\63\3\63\3\63")
        buf.write("\3\63\7\63\u022d\n\63\f\63\16\63\u0230\13\63\3\63\3\63")
        buf.write("\3\63\7\63\u0235\n\63\f\63\16\63\u0238\13\63\3\63\3\63")
        buf.write("\3\63\7\63\u023d\n\63\f\63\16\63\u0240\13\63\3\63\3\63")
        buf.write("\3\63\7\63\u0245\n\63\f\63\16\63\u0248\13\63\3\63\3\63")
        buf.write("\3\63\7\63\u024d\n\63\f\63\16\63\u0250\13\63\5\63\u0252")
        buf.write("\n\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\7\64\u025b\n")
        buf.write("\64\f\64\16\64\u025e\13\64\5\64\u0260\n\64\3\64\3\64\3")
        buf.write("\65\3\65\3\66\3\66\3\66\3\66\5\66\u026a\n\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\2\b*,.\64\66X\67\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhj\2\n\3\2;<\3\2\23\24\4\2\35\36$\'\3\2()\3")
        buf.write("\2\33\34\3\2 !\4\2\37\37\"#\3\2\f\17\2\u0293\2m\3\2\2")
        buf.write("\2\4s\3\2\2\2\6\u0083\3\2\2\2\b\u0085\3\2\2\2\n\u0091")
        buf.write("\3\2\2\2\f\u0093\3\2\2\2\16\u009b\3\2\2\2\20\u00a8\3\2")
        buf.write("\2\2\22\u00aa\3\2\2\2\24\u00b1\3\2\2\2\26\u00bf\3\2\2")
        buf.write("\2\30\u00cb\3\2\2\2\32\u00d5\3\2\2\2\34\u00df\3\2\2\2")
        buf.write("\36\u00e9\3\2\2\2 \u00eb\3\2\2\2\"\u00ee\3\2\2\2$\u00f7")
        buf.write("\3\2\2\2&\u00fe\3\2\2\2(\u0105\3\2\2\2*\u0107\3\2\2\2")
        buf.write(",\u0112\3\2\2\2.\u011d\3\2\2\2\60\u012b\3\2\2\2\62\u0130")
        buf.write("\3\2\2\2\64\u0132\3\2\2\2\66\u013c\3\2\2\28\u0159\3\2")
        buf.write("\2\2:\u0163\3\2\2\2<\u016c\3\2\2\2>\u017a\3\2\2\2@\u0186")
        buf.write("\3\2\2\2B\u0191\3\2\2\2D\u0193\3\2\2\2F\u0198\3\2\2\2")
        buf.write("H\u01a2\3\2\2\2J\u01a8\3\2\2\2L\u01ae\3\2\2\2N\u01b1\3")
        buf.write("\2\2\2P\u01b7\3\2\2\2R\u01c0\3\2\2\2T\u01c3\3\2\2\2V\u01c6")
        buf.write("\3\2\2\2X\u01cf\3\2\2\2Z\u01e0\3\2\2\2\\\u01fc\3\2\2\2")
        buf.write("^\u0200\3\2\2\2`\u0212\3\2\2\2b\u021b\3\2\2\2d\u021d\3")
        buf.write("\2\2\2f\u0255\3\2\2\2h\u0263\3\2\2\2j\u0265\3\2\2\2ln")
        buf.write("\5\4\3\2ml\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2pq\3\2")
        buf.write("\2\2qr\7\2\2\3r\3\3\2\2\2st\7\22\2\2tv\7;\2\2uw\5\b\5")
        buf.write("\2vu\3\2\2\2vw\3\2\2\2wx\3\2\2\2x|\7\64\2\2y{\5\6\4\2")
        buf.write("zy\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\177\3\2\2\2")
        buf.write("~|\3\2\2\2\177\u0080\7\65\2\2\u0080\5\3\2\2\2\u0081\u0084")
        buf.write("\5\26\f\2\u0082\u0084\5\n\6\2\u0083\u0081\3\2\2\2\u0083")
        buf.write("\u0082\3\2\2\2\u0084\7\3\2\2\2\u0085\u0086\7\61\2\2\u0086")
        buf.write("\u0087\7;\2\2\u0087\t\3\2\2\2\u0088\u0089\t\2\2\2\u0089")
        buf.write("\u008b\7*\2\2\u008a\u008c\5\20\t\2\u008b\u008a\3\2\2\2")
        buf.write("\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\7")
        buf.write("+\2\2\u008e\u0092\5^\60\2\u008f\u0092\5\f\7\2\u0090\u0092")
        buf.write("\5\16\b\2\u0091\u0088\3\2\2\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\13\3\2\2\2\u0093\u0094\7\25\2\2\u0094")
        buf.write("\u0096\7*\2\2\u0095\u0097\5\20\t\2\u0096\u0095\3\2\2\2")
        buf.write("\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\7")
        buf.write("+\2\2\u0099\u009a\5^\60\2\u009a\r\3\2\2\2\u009b\u009c")
        buf.write("\7\26\2\2\u009c\u009d\7*\2\2\u009d\u009e\7+\2\2\u009e")
        buf.write("\u009f\5^\60\2\u009f\17\3\2\2\2\u00a0\u00a9\5\22\n\2\u00a1")
        buf.write("\u00a4\5\22\n\2\u00a2\u00a3\7\63\2\2\u00a3\u00a5\5\22")
        buf.write("\n\2\u00a4\u00a2\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9\3\2\2\2\u00a8")
        buf.write("\u00a0\3\2\2\2\u00a8\u00a1\3\2\2\2\u00a9\21\3\2\2\2\u00aa")
        buf.write("\u00ab\5\32\16\2\u00ab\u00ac\7\61\2\2\u00ac\u00ad\5\24")
        buf.write("\13\2\u00ad\23\3\2\2\2\u00ae\u00b2\5h\65\2\u00af\u00b2")
        buf.write("\7;\2\2\u00b0\u00b2\5j\66\2\u00b1\u00ae\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\25\3\2\2\2\u00b3")
        buf.write("\u00b4\t\3\2\2\u00b4\u00b5\5\34\17\2\u00b5\u00b6\7\61")
        buf.write("\2\2\u00b6\u00b7\5\24\13\2\u00b7\u00b8\7\63\2\2\u00b8")
        buf.write("\u00c0\3\2\2\2\u00b9\u00ba\t\3\2\2\u00ba\u00bb\t\2\2\2")
        buf.write("\u00bb\u00bc\5\30\r\2\u00bc\u00bd\5&\24\2\u00bd\u00be")
        buf.write("\7\63\2\2\u00be\u00c0\3\2\2\2\u00bf\u00b3\3\2\2\2\u00bf")
        buf.write("\u00b9\3\2\2\2\u00c0\27\3\2\2\2\u00c1\u00c2\7\61\2\2\u00c2")
        buf.write("\u00c3\5\24\13\2\u00c3\u00c4\7\31\2\2\u00c4\u00cc\3\2")
        buf.write("\2\2\u00c5\u00c6\7\60\2\2\u00c6\u00c7\t\2\2\2\u00c7\u00c8")
        buf.write("\5\30\r\2\u00c8\u00c9\5&\24\2\u00c9\u00ca\7\60\2\2\u00ca")
        buf.write("\u00cc\3\2\2\2\u00cb\u00c1\3\2\2\2\u00cb\u00c5\3\2\2\2")
        buf.write("\u00cc\31\3\2\2\2\u00cd\u00d6\7;\2\2\u00ce\u00d1\7;\2")
        buf.write("\2\u00cf\u00d0\7\60\2\2\u00d0\u00d2\7;\2\2\u00d1\u00cf")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00cd\3\2\2\2")
        buf.write("\u00d5\u00ce\3\2\2\2\u00d6\33\3\2\2\2\u00d7\u00e0\t\2")
        buf.write("\2\2\u00d8\u00db\t\2\2\2\u00d9\u00da\7\60\2\2\u00da\u00dc")
        buf.write("\t\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd")
        buf.write("\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e0\3\2\2\2")
        buf.write("\u00df\u00d7\3\2\2\2\u00df\u00d8\3\2\2\2\u00e0\35\3\2")
        buf.write("\2\2\u00e1\u00ea\5&\24\2\u00e2\u00e5\5&\24\2\u00e3\u00e4")
        buf.write("\7\60\2\2\u00e4\u00e6\5&\24\2\u00e5\u00e3\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00ea\3\2\2\2\u00e9\u00e1\3\2\2\2\u00e9\u00e2\3")
        buf.write("\2\2\2\u00ea\37\3\2\2\2\u00eb\u00ec\5&\24\2\u00ec\u00ed")
        buf.write("\5\"\22\2\u00ed!\3\2\2\2\u00ee\u00ef\7,\2\2\u00ef\u00f0")
        buf.write("\5&\24\2\u00f0\u00f4\7-\2\2\u00f1\u00f3\5\"\22\2\u00f2")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f4\u00f5\3\2\2\2\u00f5#\3\2\2\2\u00f6\u00f4\3\2\2")
        buf.write("\2\u00f7\u00f8\t\4\2\2\u00f8%\3\2\2\2\u00f9\u00fa\5(\25")
        buf.write("\2\u00fa\u00fb\t\5\2\2\u00fb\u00fc\5(\25\2\u00fc\u00ff")
        buf.write("\3\2\2\2\u00fd\u00ff\5(\25\2\u00fe\u00f9\3\2\2\2\u00fe")
        buf.write("\u00fd\3\2\2\2\u00ff\'\3\2\2\2\u0100\u0101\5*\26\2\u0101")
        buf.write("\u0102\5$\23\2\u0102\u0103\5*\26\2\u0103\u0106\3\2\2\2")
        buf.write("\u0104\u0106\5*\26\2\u0105\u0100\3\2\2\2\u0105\u0104\3")
        buf.write("\2\2\2\u0106)\3\2\2\2\u0107\u0108\b\26\1\2\u0108\u0109")
        buf.write("\5,\27\2\u0109\u010f\3\2\2\2\u010a\u010b\f\4\2\2\u010b")
        buf.write("\u010c\t\6\2\2\u010c\u010e\5,\27\2\u010d\u010a\3\2\2\2")
        buf.write("\u010e\u0111\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3")
        buf.write("\2\2\2\u0110+\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0113")
        buf.write("\b\27\1\2\u0113\u0114\5.\30\2\u0114\u011a\3\2\2\2\u0115")
        buf.write("\u0116\f\4\2\2\u0116\u0117\t\7\2\2\u0117\u0119\5.\30\2")
        buf.write("\u0118\u0115\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3")
        buf.write("\2\2\2\u011a\u011b\3\2\2\2\u011b-\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011d\u011e\b\30\1\2\u011e\u011f\5\60\31\2\u011f")
        buf.write("\u0125\3\2\2\2\u0120\u0121\f\4\2\2\u0121\u0122\t\b\2\2")
        buf.write("\u0122\u0124\5\60\31\2\u0123\u0120\3\2\2\2\u0124\u0127")
        buf.write("\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("/\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129\7\32\2\2\u0129")
        buf.write("\u012c\5\60\31\2\u012a\u012c\5\62\32\2\u012b\u0128\3\2")
        buf.write("\2\2\u012b\u012a\3\2\2\2\u012c\61\3\2\2\2\u012d\u012e")
        buf.write("\7!\2\2\u012e\u0131\5\62\32\2\u012f\u0131\5\64\33\2\u0130")
        buf.write("\u012d\3\2\2\2\u0130\u012f\3\2\2\2\u0131\63\3\2\2\2\u0132")
        buf.write("\u0133\b\33\1\2\u0133\u0134\5\66\34\2\u0134\u0139\3\2")
        buf.write("\2\2\u0135\u0136\f\4\2\2\u0136\u0138\5\"\22\2\u0137\u0135")
        buf.write("\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013a\65\3\2\2\2\u013b\u0139\3\2\2\2\u013c")
        buf.write("\u013d\b\34\1\2\u013d\u013e\58\35\2\u013e\u014b\3\2\2")
        buf.write("\2\u013f\u0140\f\4\2\2\u0140\u0141\7.\2\2\u0141\u0147")
        buf.write("\7;\2\2\u0142\u0144\7*\2\2\u0143\u0145\5\36\20\2\u0144")
        buf.write("\u0143\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\3\2\2\2")
        buf.write("\u0146\u0148\7+\2\2\u0147\u0142\3\2\2\2\u0147\u0148\3")
        buf.write("\2\2\2\u0148\u014a\3\2\2\2\u0149\u013f\3\2\2\2\u014a\u014d")
        buf.write("\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c")
        buf.write("\67\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\7;\2\2\u014f")
        buf.write("\u0150\7\62\2\2\u0150\u0156\7<\2\2\u0151\u0153\7*\2\2")
        buf.write("\u0152\u0154\5\36\20\2\u0153\u0152\3\2\2\2\u0153\u0154")
        buf.write("\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0157\7+\2\2\u0156")
        buf.write("\u0151\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u015a\3\2\2\2")
        buf.write("\u0158\u015a\5:\36\2\u0159\u014e\3\2\2\2\u0159\u0158\3")
        buf.write("\2\2\2\u015a9\3\2\2\2\u015b\u015c\7\27\2\2\u015c\u015d")
        buf.write("\7;\2\2\u015d\u015f\7*\2\2\u015e\u0160\5\36\20\2\u015f")
        buf.write("\u015e\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\3\2\2\2")
        buf.write("\u0161\u0164\7+\2\2\u0162\u0164\5<\37\2\u0163\u015b\3")
        buf.write("\2\2\2\u0163\u0162\3\2\2\2\u0164;\3\2\2\2\u0165\u016d")
        buf.write("\5b\62\2\u0166\u016d\7\21\2\2\u0167\u016d\7;\2\2\u0168")
        buf.write("\u0169\7*\2\2\u0169\u016a\5&\24\2\u016a\u016b\7+\2\2\u016b")
        buf.write("\u016d\3\2\2\2\u016c\u0165\3\2\2\2\u016c\u0166\3\2\2\2")
        buf.write("\u016c\u0167\3\2\2\2\u016c\u0168\3\2\2\2\u016d=\3\2\2")
        buf.write("\2\u016e\u016f\t\3\2\2\u016f\u0170\5\32\16\2\u0170\u0171")
        buf.write("\7\61\2\2\u0171\u0172\5\24\13\2\u0172\u0173\7\63\2\2\u0173")
        buf.write("\u017b\3\2\2\2\u0174\u0175\t\3\2\2\u0175\u0176\7;\2\2")
        buf.write("\u0176\u0177\5@!\2\u0177\u0178\5&\24\2\u0178\u0179\7\63")
        buf.write("\2\2\u0179\u017b\3\2\2\2\u017a\u016e\3\2\2\2\u017a\u0174")
        buf.write("\3\2\2\2\u017b?\3\2\2\2\u017c\u017d\7\61\2\2\u017d\u017e")
        buf.write("\5\24\13\2\u017e\u017f\7\31\2\2\u017f\u0187\3\2\2\2\u0180")
        buf.write("\u0181\7\60\2\2\u0181\u0182\7;\2\2\u0182\u0183\5@!\2\u0183")
        buf.write("\u0184\5&\24\2\u0184\u0185\7\60\2\2\u0185\u0187\3\2\2")
        buf.write("\2\u0186\u017c\3\2\2\2\u0186\u0180\3\2\2\2\u0187A\3\2")
        buf.write("\2\2\u0188\u0189\5X-\2\u0189\u018a\7.\2\2\u018a\u018b")
        buf.write("\7;\2\2\u018b\u0192\3\2\2\2\u018c\u018d\7;\2\2\u018d\u018e")
        buf.write("\7\62\2\2\u018e\u0192\7<\2\2\u018f\u0192\7;\2\2\u0190")
        buf.write("\u0192\5 \21\2\u0191\u0188\3\2\2\2\u0191\u018c\3\2\2\2")
        buf.write("\u0191\u018f\3\2\2\2\u0191\u0190\3\2\2\2\u0192C\3\2\2")
        buf.write("\2\u0193\u0194\5B\"\2\u0194\u0195\7\31\2\2\u0195\u0196")
        buf.write("\5&\24\2\u0196\u0197\7\63\2\2\u0197E\3\2\2\2\u0198\u019c")
        buf.write("\5H%\2\u0199\u019b\5J&\2\u019a\u0199\3\2\2\2\u019b\u019e")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a1\5L\'\2")
        buf.write("\u01a0\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1G\3\2\2")
        buf.write("\2\u01a2\u01a3\7\6\2\2\u01a3\u01a4\7*\2\2\u01a4\u01a5")
        buf.write("\5&\24\2\u01a5\u01a6\7+\2\2\u01a6\u01a7\5^\60\2\u01a7")
        buf.write("I\3\2\2\2\u01a8\u01a9\7\7\2\2\u01a9\u01aa\7*\2\2\u01aa")
        buf.write("\u01ab\5&\24\2\u01ab\u01ac\7+\2\2\u01ac\u01ad\5^\60\2")
        buf.write("\u01adK\3\2\2\2\u01ae\u01af\7\b\2\2\u01af\u01b0\5^\60")
        buf.write("\2\u01b0M\3\2\2\2\u01b1\u01b2\7\t\2\2\u01b2\u01b3\7*\2")
        buf.write("\2\u01b3\u01b4\5P)\2\u01b4\u01b5\7+\2\2\u01b5\u01b6\5")
        buf.write("^\60\2\u01b6O\3\2\2\2\u01b7\u01b8\5X-\2\u01b8\u01b9\7")
        buf.write("\13\2\2\u01b9\u01ba\5&\24\2\u01ba\u01bb\7/\2\2\u01bb\u01be")
        buf.write("\5&\24\2\u01bc\u01bd\7\30\2\2\u01bd\u01bf\5&\24\2\u01be")
        buf.write("\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bfQ\3\2\2\2\u01c0")
        buf.write("\u01c1\7\4\2\2\u01c1\u01c2\7\63\2\2\u01c2S\3\2\2\2\u01c3")
        buf.write("\u01c4\7\5\2\2\u01c4\u01c5\7\63\2\2\u01c5U\3\2\2\2\u01c6")
        buf.write("\u01c8\7\20\2\2\u01c7\u01c9\5&\24\2\u01c8\u01c7\3\2\2")
        buf.write("\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb")
        buf.write("\7\63\2\2\u01cbW\3\2\2\2\u01cc\u01cd\b-\1\2\u01cd\u01d0")
        buf.write("\5Z.\2\u01ce\u01d0\5:\36\2\u01cf\u01cc\3\2\2\2\u01cf\u01ce")
        buf.write("\3\2\2\2\u01d0\u01dd\3\2\2\2\u01d1\u01d2\f\5\2\2\u01d2")
        buf.write("\u01d3\7.\2\2\u01d3\u01d9\7;\2\2\u01d4\u01d6\7*\2\2\u01d5")
        buf.write("\u01d7\5\36\20\2\u01d6\u01d5\3\2\2\2\u01d6\u01d7\3\2\2")
        buf.write("\2\u01d7\u01d8\3\2\2\2\u01d8\u01da\7+\2\2\u01d9\u01d4")
        buf.write("\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2\2\2\u01db")
        buf.write("\u01d1\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01dd\u01de\3\2\2\2\u01deY\3\2\2\2\u01df\u01dd\3\2\2")
        buf.write("\2\u01e0\u01e1\7;\2\2\u01e1\u01e9\7\62\2\2\u01e2\u01ea")
        buf.write("\7<\2\2\u01e3\u01e4\7<\2\2\u01e4\u01e6\7*\2\2\u01e5\u01e7")
        buf.write("\5\36\20\2\u01e6\u01e5\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write("\u01e8\3\2\2\2\u01e8\u01ea\7+\2\2\u01e9\u01e2\3\2\2\2")
        buf.write("\u01e9\u01e3\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea[\3\2\2")
        buf.write("\2\u01eb\u01ec\5X-\2\u01ec\u01ed\7.\2\2\u01ed\u01ee\7")
        buf.write(";\2\2\u01ee\u01f0\7*\2\2\u01ef\u01f1\5\36\20\2\u01f0\u01ef")
        buf.write("\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2")
        buf.write("\u01f3\7+\2\2\u01f3\u01fd\3\2\2\2\u01f4\u01f5\7;\2\2\u01f5")
        buf.write("\u01f6\7\62\2\2\u01f6\u01f7\7<\2\2\u01f7\u01f9\7*\2\2")
        buf.write("\u01f8\u01fa\5\36\20\2\u01f9\u01f8\3\2\2\2\u01f9\u01fa")
        buf.write("\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fd\7+\2\2\u01fc")
        buf.write("\u01eb\3\2\2\2\u01fc\u01f4\3\2\2\2\u01fd\u01fe\3\2\2\2")
        buf.write("\u01fe\u01ff\7\63\2\2\u01ff]\3\2\2\2\u0200\u0204\7\64")
        buf.write("\2\2\u0201\u0203\5`\61\2\u0202\u0201\3\2\2\2\u0203\u0206")
        buf.write("\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205")
        buf.write("\u0207\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u0208\7\65\2")
        buf.write("\2\u0208_\3\2\2\2\u0209\u0213\5> \2\u020a\u0213\5D#\2")
        buf.write("\u020b\u0213\5F$\2\u020c\u0213\5N(\2\u020d\u0213\5R*\2")
        buf.write("\u020e\u0213\5T+\2\u020f\u0213\5V,\2\u0210\u0213\5\\/")
        buf.write("\2\u0211\u0213\5^\60\2\u0212\u0209\3\2\2\2\u0212\u020a")
        buf.write("\3\2\2\2\u0212\u020b\3\2\2\2\u0212\u020c\3\2\2\2\u0212")
        buf.write("\u020d\3\2\2\2\u0212\u020e\3\2\2\2\u0212\u020f\3\2\2\2")
        buf.write("\u0212\u0210\3\2\2\2\u0212\u0211\3\2\2\2\u0213a\3\2\2")
        buf.write("\2\u0214\u021c\7\67\2\2\u0215\u021c\7\66\2\2\u0216\u021c")
        buf.write("\78\2\2\u0217\u021c\79\2\2\u0218\u021c\7:\2\2\u0219\u021c")
        buf.write("\5d\63\2\u021a\u021c\5f\64\2\u021b\u0214\3\2\2\2\u021b")
        buf.write("\u0215\3\2\2\2\u021b\u0216\3\2\2\2\u021b\u0217\3\2\2\2")
        buf.write("\u021b\u0218\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021a\3")
        buf.write("\2\2\2\u021cc\3\2\2\2\u021d\u021e\7\n\2\2\u021e\u0251")
        buf.write("\7*\2\2\u021f\u0224\7\67\2\2\u0220\u0221\7\60\2\2\u0221")
        buf.write("\u0223\7\67\2\2\u0222\u0220\3\2\2\2\u0223\u0226\3\2\2")
        buf.write("\2\u0224\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0228")
        buf.write("\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u021f\3\2\2\2\u0227")
        buf.write("\u0228\3\2\2\2\u0228\u0252\3\2\2\2\u0229\u022e\7\66\2")
        buf.write("\2\u022a\u022b\7\60\2\2\u022b\u022d\7\66\2\2\u022c\u022a")
        buf.write("\3\2\2\2\u022d\u0230\3\2\2\2\u022e\u022c\3\2\2\2\u022e")
        buf.write("\u022f\3\2\2\2\u022f\u0252\3\2\2\2\u0230\u022e\3\2\2\2")
        buf.write("\u0231\u0236\78\2\2\u0232\u0233\7\60\2\2\u0233\u0235\7")
        buf.write("8\2\2\u0234\u0232\3\2\2\2\u0235\u0238\3\2\2\2\u0236\u0234")
        buf.write("\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u0252\3\2\2\2\u0238")
        buf.write("\u0236\3\2\2\2\u0239\u023e\79\2\2\u023a\u023b\7\60\2\2")
        buf.write("\u023b\u023d\79\2\2\u023c\u023a\3\2\2\2\u023d\u0240\3")
        buf.write("\2\2\2\u023e\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0252")
        buf.write("\3\2\2\2\u0240\u023e\3\2\2\2\u0241\u0246\7:\2\2\u0242")
        buf.write("\u0243\7\60\2\2\u0243\u0245\7:\2\2\u0244\u0242\3\2\2\2")
        buf.write("\u0245\u0248\3\2\2\2\u0246\u0244\3\2\2\2\u0246\u0247\3")
        buf.write("\2\2\2\u0247\u0252\3\2\2\2\u0248\u0246\3\2\2\2\u0249\u024e")
        buf.write("\5d\63\2\u024a\u024b\7\60\2\2\u024b\u024d\5d\63\2\u024c")
        buf.write("\u024a\3\2\2\2\u024d\u0250\3\2\2\2\u024e\u024c\3\2\2\2")
        buf.write("\u024e\u024f\3\2\2\2\u024f\u0252\3\2\2\2\u0250\u024e\3")
        buf.write("\2\2\2\u0251\u0227\3\2\2\2\u0251\u0229\3\2\2\2\u0251\u0231")
        buf.write("\3\2\2\2\u0251\u0239\3\2\2\2\u0251\u0241\3\2\2\2\u0251")
        buf.write("\u0249\3\2\2\2\u0252\u0253\3\2\2\2\u0253\u0254\7+\2\2")
        buf.write("\u0254e\3\2\2\2\u0255\u0256\7\n\2\2\u0256\u025f\7*\2\2")
        buf.write("\u0257\u025c\5d\63\2\u0258\u0259\7\60\2\2\u0259\u025b")
        buf.write("\5d\63\2\u025a\u0258\3\2\2\2\u025b\u025e\3\2\2\2\u025c")
        buf.write("\u025a\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u0260\3\2\2\2")
        buf.write("\u025e\u025c\3\2\2\2\u025f\u0257\3\2\2\2\u025f\u0260\3")
        buf.write("\2\2\2\u0260\u0261\3\2\2\2\u0261\u0262\7+\2\2\u0262g\3")
        buf.write("\2\2\2\u0263\u0264\t\t\2\2\u0264i\3\2\2\2\u0265\u0266")
        buf.write("\7\n\2\2\u0266\u0269\7,\2\2\u0267\u026a\5h\65\2\u0268")
        buf.write("\u026a\5j\66\2\u0269\u0267\3\2\2\2\u0269\u0268\3\2\2\2")
        buf.write("\u026a\u026b\3\2\2\2\u026b\u026c\7\60\2\2\u026c\u026d")
        buf.write("\7\66\2\2\u026d\u026e\7-\2\2\u026ek\3\2\2\2Dov|\u0083")
        buf.write("\u008b\u0091\u0096\u00a6\u00a8\u00b1\u00bf\u00cb\u00d3")
        buf.write("\u00d5\u00dd\u00df\u00e7\u00e9\u00f4\u00fe\u0105\u010f")
        buf.write("\u011a\u0125\u012b\u0130\u0139\u0144\u0147\u014b\u0153")
        buf.write("\u0156\u0159\u015f\u0163\u016c\u017a\u0186\u0191\u019c")
        buf.write("\u01a0\u01be\u01c8\u01cf\u01d6\u01d9\u01dd\u01e6\u01e9")
        buf.write("\u01f0\u01f9\u01fc\u0204\u0212\u021b\u0224\u0227\u022e")
        buf.write("\u0236\u023e\u0246\u024e\u0251\u025c\u025f\u0269")
        return buf.getvalue()


class D96Parser(Parser):
    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "<INVALID>", "'Break'", "'Continue'",
                    "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Array'",
                    "'In'", "'Int'", "'Float'", "'Boolean'", "'String'",
                    "'Return'", "'Null'", "'Class'", "'Val'", "'Var'",
                    "'Constructor'", "'Destructor'", "'New'", "'By'", "'='",
                    "'!'", "'||'", "'&&'", "'=='", "'!='", "'%'", "'+'",
                    "'-'", "'*'", "'/'", "'<'", "'<='", "'>'", "'>='",
                    "'+.'", "'==.'", "'('", "')'", "'['", "']'", "'.'",
                    "'..'", "','", "':'", "'::'", "';'", "'{'", "'}'"]

    symbolicNames = ["<INVALID>", "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF",
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
                     "ERROR_CHAR"]

    RULE_program = 0
    RULE_classDeclaration = 1
    RULE_classBodyUnit = 2
    RULE_superClassGroup = 3
    RULE_methodDeclaration = 4
    RULE_constructor = 5
    RULE_destructor = 6
    RULE_parameterList = 7
    RULE_parameter = 8
    RULE_d96Type = 9
    RULE_attributeDeclaration = 10
    RULE_attributeValueList = 11
    RULE_identifierList = 12
    RULE_mixedIdentifierList = 13
    RULE_expressionList = 14
    RULE_elementExpression = 15
    RULE_indexOperator = 16
    RULE_relationalOperator = 17
    RULE_expression = 18
    RULE_relationalExpr = 19
    RULE_andOrExpr = 20
    RULE_addSubExpr = 21
    RULE_mulAddMolExpr = 22
    RULE_notExpr = 23
    RULE_signExpr = 24
    RULE_indexOperatorExpr = 25
    RULE_instanceAccess = 26
    RULE_staticAccess = 27
    RULE_objectCreation = 28
    RULE_atomExpr = 29
    RULE_varValStatement = 30
    RULE_varValValueList = 31
    RULE_lhs = 32
    RULE_assignStatement = 33
    RULE_ifStatement = 34
    RULE_ifPart = 35
    RULE_elseIfPart = 36
    RULE_elsePart = 37
    RULE_forInStatement = 38
    RULE_loopPart = 39
    RULE_breakStatement = 40
    RULE_continueStatement = 41
    RULE_returnStatement = 42
    RULE_memberAccessInstance = 43
    RULE_memberAccessStatic = 44
    RULE_methodInvocationStatement = 45
    RULE_blockStatement = 46
    RULE_statement = 47
    RULE_literal = 48
    RULE_indexedArray = 49
    RULE_multiDimentionalArray = 50
    RULE_primitiveType = 51
    RULE_arrayType = 52

    ruleNames = ["program", "classDeclaration", "classBodyUnit", "superClassGroup",
                 "methodDeclaration", "constructor", "destructor", "parameterList",
                 "parameter", "d96Type", "attributeDeclaration", "attributeValueList",
                 "identifierList", "mixedIdentifierList", "expressionList",
                 "elementExpression", "indexOperator", "relationalOperator",
                 "expression", "relationalExpr", "andOrExpr", "addSubExpr",
                 "mulAddMolExpr", "notExpr", "signExpr", "indexOperatorExpr",
                 "instanceAccess", "staticAccess", "objectCreation", "atomExpr",
                 "varValStatement", "varValValueList", "lhs", "assignStatement",
                 "ifStatement", "ifPart", "elseIfPart", "elsePart", "forInStatement",
                 "loopPart", "breakStatement", "continueStatement", "returnStatement",
                 "memberAccessInstance", "memberAccessStatic", "methodInvocationStatement",
                 "blockStatement", "statement", "literal", "indexedArray",
                 "multiDimentionalArray", "primitiveType", "arrayType"]

    EOF = Token.EOF
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

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def classDeclaration(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ClassDeclarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.ClassDeclarationContext, i)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitProgram"):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)

    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.classDeclaration()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == D96Parser.K_CLASS):
                    break

            self.state = 111
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
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

        def superClassGroup(self):
            return self.getTypedRuleContext(D96Parser.SuperClassGroupContext, 0)

        def classBodyUnit(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ClassBodyUnitContext)
            else:
                return self.getTypedRuleContext(D96Parser.ClassBodyUnitContext, i)

        def getRuleIndex(self):
            return D96Parser.RULE_classDeclaration

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitClassDeclaration"):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)

    def classDeclaration(self):

        localctx = D96Parser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDeclaration)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(D96Parser.K_CLASS)
            self.state = 114
            self.match(D96Parser.IDENTIFIER)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == D96Parser.COLON:
                self.state = 115
                self.superClassGroup()

            self.state = 118
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (
                    1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.IDENTIFIER) | (
                            1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 119
                self.classBodyUnit()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassBodyUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeDeclaration(self):
            return self.getTypedRuleContext(D96Parser.AttributeDeclarationContext, 0)

        def methodDeclaration(self):
            return self.getTypedRuleContext(D96Parser.MethodDeclarationContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classBodyUnit

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitClassBodyUnit"):
                return visitor.visitClassBodyUnit(self)
            else:
                return visitor.visitChildren(self)

    def classBodyUnit(self):

        localctx = D96Parser.ClassBodyUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classBodyUnit)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_VAL, D96Parser.K_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.attributeDeclaration()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR, D96Parser.K_DESTRUCTOR, D96Parser.IDENTIFIER,
                           D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.methodDeclaration()
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

    class SuperClassGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_superClassGroup

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSuperClassGroup"):
                return visitor.visitSuperClassGroup(self)
            else:
                return visitor.visitChildren(self)

    def superClassGroup(self):

        localctx = D96Parser.SuperClassGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_superClassGroup)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(D96Parser.COLON)
            self.state = 132
            self.match(D96Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def parameterList(self):
            return self.getTypedRuleContext(D96Parser.ParameterListContext, 0)

        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext, 0)

        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_methodDeclaration

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMethodDeclaration"):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)

    def methodDeclaration(self):

        localctx = D96Parser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_methodDeclaration)
        self._la = 0  # Token type
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                _la = self._input.LA(1)
                if not (_la == D96Parser.IDENTIFIER or _la == D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 135
                self.match(D96Parser.LEFT_PAREN)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == D96Parser.IDENTIFIER:
                    self.state = 136
                    self.parameterList()

                self.state = 139
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 140
                self.blockStatement()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.constructor()
                pass
            elif token in [D96Parser.K_DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_CONSTRUCTOR(self):
            return self.getToken(D96Parser.K_CONSTRUCTOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext, 0)

        def parameterList(self):
            return self.getTypedRuleContext(D96Parser.ParameterListContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitConstructor"):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)

    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constructor)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(D96Parser.K_CONSTRUCTOR)
            self.state = 146
            self.match(D96Parser.LEFT_PAREN)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == D96Parser.IDENTIFIER:
                self.state = 147
                self.parameterList()

            self.state = 150
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 151
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_DESTRUCTOR(self):
            return self.getToken(D96Parser.K_DESTRUCTOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitDestructor"):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)

    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(D96Parser.K_DESTRUCTOR)
            self.state = 154
            self.match(D96Parser.LEFT_PAREN)
            self.state = 155
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 156
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ParameterContext)
            else:
                return self.getTypedRuleContext(D96Parser.ParameterContext, i)

        def SEMI_COLON(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.SEMI_COLON)
            else:
                return self.getToken(D96Parser.SEMI_COLON, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameterList

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParameterList"):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)

    def parameterList(self):

        localctx = D96Parser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameterList)
        self._la = 0  # Token type
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 8, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.parameter()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 160
                    self.match(D96Parser.SEMI_COLON)
                    self.state = 161
                    self.parameter()
                    self.state = 164
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la == D96Parser.SEMI_COLON):
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(D96Parser.IdentifierListContext, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96Type(self):
            return self.getTypedRuleContext(D96Parser.D96TypeContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParameter"):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)

    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.identifierList()
            self.state = 169
            self.match(D96Parser.COLON)
            self.state = 170
            self.d96Type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class D96TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(D96Parser.PrimitiveTypeContext, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_d96Type

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitD96Type"):
                return visitor.visitD96Type(self)
            else:
                return visitor.visitChildren(self)

    def d96Type(self):

        localctx = D96Parser.D96TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_d96Type)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_INT, D96Parser.K_FLOAT, D96Parser.K_BOOLEAN, D96Parser.K_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.primitiveType()
                pass
            elif token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.arrayType()
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

    class AttributeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mixedIdentifierList(self):
            return self.getTypedRuleContext(D96Parser.MixedIdentifierListContext, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96Type(self):
            return self.getTypedRuleContext(D96Parser.D96TypeContext, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

        def attributeValueList(self):
            return self.getTypedRuleContext(D96Parser.AttributeValueListContext, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attributeDeclaration

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAttributeDeclaration"):
                return visitor.visitAttributeDeclaration(self)
            else:
                return visitor.visitChildren(self)

    def attributeDeclaration(self):

        localctx = D96Parser.AttributeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attributeDeclaration)
        self._la = 0  # Token type
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 10, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                _la = self._input.LA(1)
                if not (_la == D96Parser.K_VAL or _la == D96Parser.K_VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 178
                self.mixedIdentifierList()
                self.state = 179
                self.match(D96Parser.COLON)
                self.state = 180
                self.d96Type()
                self.state = 181
                self.match(D96Parser.SEMI_COLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                _la = self._input.LA(1)
                if not (_la == D96Parser.K_VAL or _la == D96Parser.K_VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 184
                _la = self._input.LA(1)
                if not (_la == D96Parser.IDENTIFIER or _la == D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 185
                self.attributeValueList()
                self.state = 186
                self.expression()
                self.state = 187
                self.match(D96Parser.SEMI_COLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeValueListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96Type(self):
            return self.getTypedRuleContext(D96Parser.D96TypeContext, 0)

        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def attributeValueList(self):
            return self.getTypedRuleContext(D96Parser.AttributeValueListContext, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attributeValueList

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAttributeValueList"):
                return visitor.visitAttributeValueList(self)
            else:
                return visitor.visitChildren(self)

    def attributeValueList(self):

        localctx = D96Parser.AttributeValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attributeValueList)
        self._la = 0  # Token type
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(D96Parser.COLON)
                self.state = 192
                self.d96Type()
                self.state = 193
                self.match(D96Parser.OP_ASSIGN)
                pass
            elif token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.match(D96Parser.COMMA)
                self.state = 196
                _la = self._input.LA(1)
                if not (_la == D96Parser.IDENTIFIER or _la == D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 197
                self.attributeValueList()
                self.state = 198
                self.expression()
                self.state = 199
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

    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_identifierList

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIdentifierList"):
                return visitor.visitIdentifierList(self)
            else:
                return visitor.visitChildren(self)

    def identifierList(self):

        localctx = D96Parser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_identifierList)
        self._la = 0  # Token type
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 13, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(D96Parser.IDENTIFIER)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 205
                    self.match(D96Parser.COMMA)
                    self.state = 206
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 209
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la == D96Parser.COMMA):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MixedIdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

        def DOLAR_IDENTIFIER(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.DOLAR_IDENTIFIER)
            else:
                return self.getToken(D96Parser.DOLAR_IDENTIFIER, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_mixedIdentifierList

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMixedIdentifierList"):
                return visitor.visitMixedIdentifierList(self)
            else:
                return visitor.visitChildren(self)

    def mixedIdentifierList(self):

        localctx = D96Parser.MixedIdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_mixedIdentifierList)
        self._la = 0  # Token type
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 15, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                _la = self._input.LA(1)
                if not (_la == D96Parser.IDENTIFIER or _la == D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                _la = self._input.LA(1)
                if not (_la == D96Parser.IDENTIFIER or _la == D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 215
                    self.match(D96Parser.COMMA)
                    self.state = 216
                    _la = self._input.LA(1)
                    if not (_la == D96Parser.IDENTIFIER or _la == D96Parser.DOLAR_IDENTIFIER):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 219
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la == D96Parser.COMMA):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expressionList

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpressionList"):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)

    def expressionList(self):

        localctx = D96Parser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expressionList)
        self._la = 0  # Token type
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 17, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.expression()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 225
                    self.match(D96Parser.COMMA)
                    self.state = 226
                    self.expression()
                    self.state = 229
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la == D96Parser.COMMA):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def indexOperator(self):
            return self.getTypedRuleContext(D96Parser.IndexOperatorContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_elementExpression

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitElementExpression"):
                return visitor.visitElementExpression(self)
            else:
                return visitor.visitChildren(self)

    def elementExpression(self):

        localctx = D96Parser.ElementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elementExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.expression()
            self.state = 234
            self.indexOperator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IndexOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.LEFT_SQUARE_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_SQUARE_BRACKET, 0)

        def indexOperator(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IndexOperatorContext)
            else:
                return self.getTypedRuleContext(D96Parser.IndexOperatorContext, i)

        def getRuleIndex(self):
            return D96Parser.RULE_indexOperator

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIndexOperator"):
                return visitor.visitIndexOperator(self)
            else:
                return visitor.visitChildren(self)

    def indexOperator(self):

        localctx = D96Parser.IndexOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_indexOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 237
            self.expression()
            self.state = 238
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 18, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 239
                    self.indexOperator()
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 18, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RelationalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
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
            return D96Parser.RULE_relationalOperator

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRelationalOperator"):
                return visitor.visitRelationalOperator(self)
            else:
                return visitor.visitChildren(self)

    def relationalOperator(self):

        localctx = D96Parser.RelationalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_relationalOperator)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << D96Parser.OP_IS_EQUAL_TO) | (1 << D96Parser.OP_NOT_EQUAL_TO) | (
                    1 << D96Parser.OP_LESS_THAN) | (1 << D96Parser.OP_LESS_THAN_EQUAL) | (
                            1 << D96Parser.OP_GREATER_THAN) | (1 << D96Parser.OP_GREATER_THAN_EQUAL))) != 0)):
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.RelationalExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.RelationalExprContext, i)

        def OP_STRING_CONCATENATION(self):
            return self.getToken(D96Parser.OP_STRING_CONCATENATION, 0)

        def OP_TWO_SAME_STRING(self):
            return self.getToken(D96Parser.OP_TWO_SAME_STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpression"):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)

    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression)
        self._la = 0  # Token type
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 19, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.relationalExpr()
                self.state = 248
                _la = self._input.LA(1)
                if not (_la == D96Parser.OP_STRING_CONCATENATION or _la == D96Parser.OP_TWO_SAME_STRING):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 249
                self.relationalExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.relationalExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andOrExpr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.AndOrExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.AndOrExprContext, i)

        def relationalOperator(self):
            return self.getTypedRuleContext(D96Parser.RelationalOperatorContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relationalExpr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRelationalExpr"):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)

    def relationalExpr(self):

        localctx = D96Parser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relationalExpr)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 20, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.andOrExpr(0)
                self.state = 255
                self.relationalOperator()
                self.state = 256
                self.andOrExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.andOrExpr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AndOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addSubExpr(self):
            return self.getTypedRuleContext(D96Parser.AddSubExprContext, 0)

        def andOrExpr(self):
            return self.getTypedRuleContext(D96Parser.AndOrExprContext, 0)

        def OP_LOGICAL_AND(self):
            return self.getToken(D96Parser.OP_LOGICAL_AND, 0)

        def OP_LOGICAL_OR(self):
            return self.getToken(D96Parser.OP_LOGICAL_OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_andOrExpr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAndOrExpr"):
                return visitor.visitAndOrExpr(self)
            else:
                return visitor.visitChildren(self)

    def andOrExpr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.AndOrExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_andOrExpr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.addSubExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 21, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.AndOrExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andOrExpr)
                    self.state = 264
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 265
                    _la = self._input.LA(1)
                    if not (_la == D96Parser.OP_LOGICAL_OR or _la == D96Parser.OP_LOGICAL_AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 266
                    self.addSubExpr(0)
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 21, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AddSubExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulAddMolExpr(self):
            return self.getTypedRuleContext(D96Parser.MulAddMolExprContext, 0)

        def addSubExpr(self):
            return self.getTypedRuleContext(D96Parser.AddSubExprContext, 0)

        def OP_ADDTION(self):
            return self.getToken(D96Parser.OP_ADDTION, 0)

        def OP_SUBTRACTION(self):
            return self.getToken(D96Parser.OP_SUBTRACTION, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_addSubExpr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAddSubExpr"):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)

    def addSubExpr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.AddSubExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_addSubExpr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.mulAddMolExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 22, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.AddSubExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addSubExpr)
                    self.state = 275
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 276
                    _la = self._input.LA(1)
                    if not (_la == D96Parser.OP_ADDTION or _la == D96Parser.OP_SUBTRACTION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 277
                    self.mulAddMolExpr(0)
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 22, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MulAddMolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notExpr(self):
            return self.getTypedRuleContext(D96Parser.NotExprContext, 0)

        def mulAddMolExpr(self):
            return self.getTypedRuleContext(D96Parser.MulAddMolExprContext, 0)

        def OP_MULTIPLICATION(self):
            return self.getToken(D96Parser.OP_MULTIPLICATION, 0)

        def OP_DIVISION(self):
            return self.getToken(D96Parser.OP_DIVISION, 0)

        def OP_MODULO(self):
            return self.getToken(D96Parser.OP_MODULO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mulAddMolExpr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMulAddMolExpr"):
                return visitor.visitMulAddMolExpr(self)
            else:
                return visitor.visitChildren(self)

    def mulAddMolExpr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.MulAddMolExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_mulAddMolExpr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.notExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 23, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.MulAddMolExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mulAddMolExpr)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                            (1 << D96Parser.OP_MODULO) | (1 << D96Parser.OP_MULTIPLICATION) | (
                            1 << D96Parser.OP_DIVISION))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 288
                    self.notExpr()
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 23, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class NotExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_LOGICAL_NOT(self):
            return self.getToken(D96Parser.OP_LOGICAL_NOT, 0)

        def notExpr(self):
            return self.getTypedRuleContext(D96Parser.NotExprContext, 0)

        def signExpr(self):
            return self.getTypedRuleContext(D96Parser.SignExprContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_notExpr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNotExpr"):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)

    def notExpr(self):

        localctx = D96Parser.NotExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_notExpr)
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(D96Parser.OP_LOGICAL_NOT)
                self.state = 295
                self.notExpr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_NEW, D96Parser.OP_SUBTRACTION,
                           D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL,
                           D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL,
                           D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.signExpr()
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

    class SignExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signExpr(self):
            return self.getTypedRuleContext(D96Parser.SignExprContext, 0)

        def OP_SUBTRACTION(self):
            return self.getToken(D96Parser.OP_SUBTRACTION, 0)

        def indexOperatorExpr(self):
            return self.getTypedRuleContext(D96Parser.IndexOperatorExprContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_signExpr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSignExpr"):
                return visitor.visitSignExpr(self)
            else:
                return visitor.visitChildren(self)

    def signExpr(self):

        localctx = D96Parser.SignExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_signExpr)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUBTRACTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(D96Parser.OP_SUBTRACTION)
                self.state = 300
                self.signExpr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_NEW, D96Parser.LEFT_PAREN,
                           D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL,
                           D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.indexOperatorExpr(0)
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

    class IndexOperatorExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instanceAccess(self):
            return self.getTypedRuleContext(D96Parser.InstanceAccessContext, 0)

        def indexOperatorExpr(self):
            return self.getTypedRuleContext(D96Parser.IndexOperatorExprContext, 0)

        def indexOperator(self):
            return self.getTypedRuleContext(D96Parser.IndexOperatorContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_indexOperatorExpr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIndexOperatorExpr"):
                return visitor.visitIndexOperatorExpr(self)
            else:
                return visitor.visitChildren(self)

    def indexOperatorExpr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.IndexOperatorExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_indexOperatorExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.instanceAccess(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 26, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.IndexOperatorExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indexOperatorExpr)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    self.indexOperator()
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 26, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class InstanceAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def staticAccess(self):
            return self.getTypedRuleContext(D96Parser.StaticAccessContext, 0)

        def instanceAccess(self):
            return self.getTypedRuleContext(D96Parser.InstanceAccessContext, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(D96Parser.ExpressionListContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instanceAccess

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitInstanceAccess"):
                return visitor.visitInstanceAccess(self)
            else:
                return visitor.visitChildren(self)

    def instanceAccess(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.InstanceAccessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_instanceAccess, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.staticAccess()
            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 29, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.InstanceAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instanceAccess)
                    self.state = 317
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 318
                    self.match(D96Parser.DOT)
                    self.state = 319
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 325
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 28, self._ctx)
                    if la_ == 1:
                        self.state = 320
                        self.match(D96Parser.LEFT_PAREN)
                        self.state = 322
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                                (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (
                                1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (
                                        1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (
                                        1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (
                                        1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (
                                        1 << D96Parser.IDENTIFIER))) != 0):
                            self.state = 321
                            self.expressionList()

                        self.state = 324
                        self.match(D96Parser.RIGHT_PAREN)

                self.state = 331
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 29, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class StaticAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
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

        def expressionList(self):
            return self.getTypedRuleContext(D96Parser.ExpressionListContext, 0)

        def objectCreation(self):
            return self.getTypedRuleContext(D96Parser.ObjectCreationContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_staticAccess

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStaticAccess"):
                return visitor.visitStaticAccess(self)
            else:
                return visitor.visitChildren(self)

    def staticAccess(self):

        localctx = D96Parser.StaticAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_staticAccess)
        self._la = 0  # Token type
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 32, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(D96Parser.IDENTIFIER)
                self.state = 333
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 334
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 340
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 31, self._ctx)
                if la_ == 1:
                    self.state = 335
                    self.match(D96Parser.LEFT_PAREN)
                    self.state = 337
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                            (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (
                            1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (
                                    1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (
                                    1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (
                                    1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (
                                    1 << D96Parser.IDENTIFIER))) != 0):
                        self.state = 336
                        self.expressionList()

                    self.state = 339
                    self.match(D96Parser.RIGHT_PAREN)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.objectCreation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjectCreationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
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

        def expressionList(self):
            return self.getTypedRuleContext(D96Parser.ExpressionListContext, 0)

        def atomExpr(self):
            return self.getTypedRuleContext(D96Parser.AtomExprContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_objectCreation

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitObjectCreation"):
                return visitor.visitObjectCreation(self)
            else:
                return visitor.visitChildren(self)

    def objectCreation(self):

        localctx = D96Parser.ObjectCreationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_objectCreation)
        self._la = 0  # Token type
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(D96Parser.K_NEW)
                self.state = 346
                self.match(D96Parser.IDENTIFIER)
                self.state = 347
                self.match(D96Parser.LEFT_PAREN)
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                        (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (
                        1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (
                                1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (
                                1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (
                                1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (
                                1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 348
                    self.expressionList()

                self.state = 351
                self.match(D96Parser.RIGHT_PAREN)
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2,
                           D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL,
                           D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.atomExpr()
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

    class AtomExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext, 0)

        def K_NULL(self):
            return self.getToken(D96Parser.K_NULL, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_atomExpr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAtomExpr"):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)

    def atomExpr(self):

        localctx = D96Parser.AtomExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_atomExpr)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_ARRAY, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL,
                         D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.literal()
                pass
            elif token in [D96Parser.K_NULL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.match(D96Parser.K_NULL)
                pass
            elif token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 357
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 358
                self.match(D96Parser.LEFT_PAREN)
                self.state = 359
                self.expression()
                self.state = 360
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

    class VarValStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(D96Parser.IdentifierListContext, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96Type(self):
            return self.getTypedRuleContext(D96Parser.D96TypeContext, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def varValValueList(self):
            return self.getTypedRuleContext(D96Parser.VarValValueListContext, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_varValStatement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVarValStatement"):
                return visitor.visitVarValStatement(self)
            else:
                return visitor.visitChildren(self)

    def varValStatement(self):

        localctx = D96Parser.VarValStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_varValStatement)
        self._la = 0  # Token type
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 36, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                _la = self._input.LA(1)
                if not (_la == D96Parser.K_VAL or _la == D96Parser.K_VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 365
                self.identifierList()
                self.state = 366
                self.match(D96Parser.COLON)
                self.state = 367
                self.d96Type()
                self.state = 368
                self.match(D96Parser.SEMI_COLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                _la = self._input.LA(1)
                if not (_la == D96Parser.K_VAL or _la == D96Parser.K_VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 371
                self.match(D96Parser.IDENTIFIER)
                self.state = 372
                self.varValValueList()
                self.state = 373
                self.expression()
                self.state = 374
                self.match(D96Parser.SEMI_COLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarValValueListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96Type(self):
            return self.getTypedRuleContext(D96Parser.D96TypeContext, 0)

        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def varValValueList(self):
            return self.getTypedRuleContext(D96Parser.VarValValueListContext, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_varValValueList

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVarValValueList"):
                return visitor.visitVarValValueList(self)
            else:
                return visitor.visitChildren(self)

    def varValValueList(self):

        localctx = D96Parser.VarValValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_varValValueList)
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.match(D96Parser.COLON)
                self.state = 379
                self.d96Type()
                self.state = 380
                self.match(D96Parser.OP_ASSIGN)
                pass
            elif token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.match(D96Parser.COMMA)
                self.state = 383
                self.match(D96Parser.IDENTIFIER)
                self.state = 384
                self.varValValueList()
                self.state = 385
                self.expression()
                self.state = 386
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberAccessInstance(self):
            return self.getTypedRuleContext(D96Parser.MemberAccessInstanceContext, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def elementExpression(self):
            return self.getTypedRuleContext(D96Parser.ElementExpressionContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLhs"):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)

    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_lhs)
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 38, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.memberAccessInstance(0)
                self.state = 391
                self.match(D96Parser.DOT)
                self.state = 392
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.match(D96Parser.IDENTIFIER)
                self.state = 395
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 396
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 397
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 398
                self.elementExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext, 0)

        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignStatement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAssignStatement"):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)

    def assignStatement(self):

        localctx = D96Parser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.lhs()
            self.state = 402
            self.match(D96Parser.OP_ASSIGN)
            self.state = 403
            self.expression()
            self.state = 404
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifPart(self):
            return self.getTypedRuleContext(D96Parser.IfPartContext, 0)

        def elseIfPart(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ElseIfPartContext)
            else:
                return self.getTypedRuleContext(D96Parser.ElseIfPartContext, i)

        def elsePart(self):
            return self.getTypedRuleContext(D96Parser.ElsePartContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_ifStatement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIfStatement"):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)

    def ifStatement(self):

        localctx = D96Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_ifStatement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.ifPart()
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == D96Parser.K_ELSE_IF:
                self.state = 407
                self.elseIfPart()
                self.state = 412
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == D96Parser.K_ELSE:
                self.state = 413
                self.elsePart()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_IF(self):
            return self.getToken(D96Parser.K_IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_ifPart

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIfPart"):
                return visitor.visitIfPart(self)
            else:
                return visitor.visitChildren(self)

    def ifPart(self):

        localctx = D96Parser.IfPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifPart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(D96Parser.K_IF)
            self.state = 417
            self.match(D96Parser.LEFT_PAREN)
            self.state = 418
            self.expression()
            self.state = 419
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 420
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElseIfPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ELSE_IF(self):
            return self.getToken(D96Parser.K_ELSE_IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_elseIfPart

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitElseIfPart"):
                return visitor.visitElseIfPart(self)
            else:
                return visitor.visitChildren(self)

    def elseIfPart(self):

        localctx = D96Parser.ElseIfPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_elseIfPart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(D96Parser.K_ELSE_IF)
            self.state = 423
            self.match(D96Parser.LEFT_PAREN)
            self.state = 424
            self.expression()
            self.state = 425
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 426
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElsePartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ELSE(self):
            return self.getToken(D96Parser.K_ELSE, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_elsePart

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitElsePart"):
                return visitor.visitElsePart(self)
            else:
                return visitor.visitChildren(self)

    def elsePart(self):

        localctx = D96Parser.ElsePartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_elsePart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(D96Parser.K_ELSE)
            self.state = 429
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForInStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_FOR_EACH(self):
            return self.getToken(D96Parser.K_FOR_EACH, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def loopPart(self):
            return self.getTypedRuleContext(D96Parser.LoopPartContext, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forInStatement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitForInStatement"):
                return visitor.visitForInStatement(self)
            else:
                return visitor.visitChildren(self)

    def forInStatement(self):

        localctx = D96Parser.ForInStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_forInStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(D96Parser.K_FOR_EACH)
            self.state = 432
            self.match(D96Parser.LEFT_PAREN)
            self.state = 433
            self.loopPart()
            self.state = 434
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 435
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LoopPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberAccessInstance(self):
            return self.getTypedRuleContext(D96Parser.MemberAccessInstanceContext, 0)

        def K_IN(self):
            return self.getToken(D96Parser.K_IN, 0)

        def expression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext, i)

        def DOUBLE_DOT(self):
            return self.getToken(D96Parser.DOUBLE_DOT, 0)

        def K_BY(self):
            return self.getToken(D96Parser.K_BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_loopPart

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLoopPart"):
                return visitor.visitLoopPart(self)
            else:
                return visitor.visitChildren(self)

    def loopPart(self):

        localctx = D96Parser.LoopPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_loopPart)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.memberAccessInstance(0)
            self.state = 438
            self.match(D96Parser.K_IN)
            self.state = 439
            self.expression()
            self.state = 440
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 441
            self.expression()
            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == D96Parser.K_BY:
                self.state = 442
                self.match(D96Parser.K_BY)
                self.state = 443
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_BREAK(self):
            return self.getToken(D96Parser.K_BREAK, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_breakStatement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBreakStatement"):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)

    def breakStatement(self):

        localctx = D96Parser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(D96Parser.K_BREAK)
            self.state = 447
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_CONTINUE(self):
            return self.getToken(D96Parser.K_CONTINUE, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continueStatement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitContinueStatement"):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)

    def continueStatement(self):

        localctx = D96Parser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(D96Parser.K_CONTINUE)
            self.state = 450
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_RETURN(self):
            return self.getToken(D96Parser.K_RETURN, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_returnStatement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitReturnStatement"):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)

    def returnStatement(self):

        localctx = D96Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_returnStatement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(D96Parser.K_RETURN)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (
                    1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (
                            1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (
                            1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (
                            1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 453
                self.expression()

            self.state = 456
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MemberAccessInstanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberAccessStatic(self):
            return self.getTypedRuleContext(D96Parser.MemberAccessStaticContext, 0)

        def objectCreation(self):
            return self.getTypedRuleContext(D96Parser.ObjectCreationContext, 0)

        def memberAccessInstance(self):
            return self.getTypedRuleContext(D96Parser.MemberAccessInstanceContext, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(D96Parser.ExpressionListContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_memberAccessInstance

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMemberAccessInstance"):
                return visitor.visitMemberAccessInstance(self)
            else:
                return visitor.visitChildren(self)

    def memberAccessInstance(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.MemberAccessInstanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_memberAccessInstance, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 43, self._ctx)
            if la_ == 1:
                self.state = 459
                self.memberAccessStatic()
                pass

            elif la_ == 2:
                self.state = 460
                self.objectCreation()
                pass

            self._ctx.stop = self._input.LT(-1)
            self.state = 475
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 46, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.MemberAccessInstanceContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_memberAccessInstance)
                    self.state = 463
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 464
                    self.match(D96Parser.DOT)
                    self.state = 465
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 471
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 45, self._ctx)
                    if la_ == 1:
                        self.state = 466
                        self.match(D96Parser.LEFT_PAREN)
                        self.state = 468
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                                (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (
                                1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (
                                        1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (
                                        1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (
                                        1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (
                                        1 << D96Parser.IDENTIFIER))) != 0):
                            self.state = 467
                            self.expressionList()

                        self.state = 470
                        self.match(D96Parser.RIGHT_PAREN)

                self.state = 477
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 46, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MemberAccessStaticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
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

        def expressionList(self):
            return self.getTypedRuleContext(D96Parser.ExpressionListContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_memberAccessStatic

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMemberAccessStatic"):
                return visitor.visitMemberAccessStatic(self)
            else:
                return visitor.visitChildren(self)

    def memberAccessStatic(self):

        localctx = D96Parser.MemberAccessStaticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_memberAccessStatic)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(D96Parser.IDENTIFIER)
            self.state = 479
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 48, self._ctx)
            if la_ == 1:
                self.state = 480
                self.match(D96Parser.DOLAR_IDENTIFIER)

            elif la_ == 2:
                self.state = 481
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 482
                self.match(D96Parser.LEFT_PAREN)
                self.state = 484
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                        (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (
                        1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (
                                1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (
                                1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (
                                1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (
                                1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 483
                    self.expressionList()

                self.state = 486
                self.match(D96Parser.RIGHT_PAREN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MethodInvocationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def memberAccessInstance(self):
            return self.getTypedRuleContext(D96Parser.MemberAccessInstanceContext, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def expressionList(self):
            return self.getTypedRuleContext(D96Parser.ExpressionListContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_methodInvocationStatement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMethodInvocationStatement"):
                return visitor.visitMethodInvocationStatement(self)
            else:
                return visitor.visitChildren(self)

    def methodInvocationStatement(self):

        localctx = D96Parser.MethodInvocationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_methodInvocationStatement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 51, self._ctx)
            if la_ == 1:
                self.state = 489
                self.memberAccessInstance(0)
                self.state = 490
                self.match(D96Parser.DOT)
                self.state = 491
                self.match(D96Parser.IDENTIFIER)
                self.state = 492
                self.match(D96Parser.LEFT_PAREN)
                self.state = 494
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                        (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (
                        1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (
                                1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (
                                1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (
                                1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (
                                1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 493
                    self.expressionList()

                self.state = 496
                self.match(D96Parser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.state = 498
                self.match(D96Parser.IDENTIFIER)
                self.state = 499
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 500
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 501
                self.match(D96Parser.LEFT_PAREN)
                self.state = 503
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                        (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_NEW) | (
                        1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (
                                1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (
                                1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (
                                1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (
                                1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 502
                    self.expressionList()

                self.state = 505
                self.match(D96Parser.RIGHT_PAREN)
                pass

            self.state = 508
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StatementContext)
            else:
                return self.getTypedRuleContext(D96Parser.StatementContext, i)

        def getRuleIndex(self):
            return D96Parser.RULE_blockStatement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBlockStatement"):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)

    def blockStatement(self):

        localctx = D96Parser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_blockStatement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << D96Parser.K_BREAK) | (1 << D96Parser.K_CONTINUE) | (1 << D96Parser.K_IF) | (
                    1 << D96Parser.K_FOR_EACH) | (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_RETURN) | (
                            1 << D96Parser.K_NULL) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (
                            1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (
                            1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (
                            1 << D96Parser.LEFT_CURLY_BRACKET) | (1 << D96Parser.INTEGER_LITERAL2) | (
                            1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (
                            1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (
                            1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 511
                self.statement()
                self.state = 516
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 517
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varValStatement(self):
            return self.getTypedRuleContext(D96Parser.VarValStatementContext, 0)

        def assignStatement(self):
            return self.getTypedRuleContext(D96Parser.AssignStatementContext, 0)

        def ifStatement(self):
            return self.getTypedRuleContext(D96Parser.IfStatementContext, 0)

        def forInStatement(self):
            return self.getTypedRuleContext(D96Parser.ForInStatementContext, 0)

        def breakStatement(self):
            return self.getTypedRuleContext(D96Parser.BreakStatementContext, 0)

        def continueStatement(self):
            return self.getTypedRuleContext(D96Parser.ContinueStatementContext, 0)

        def returnStatement(self):
            return self.getTypedRuleContext(D96Parser.ReturnStatementContext, 0)

        def methodInvocationStatement(self):
            return self.getTypedRuleContext(D96Parser.MethodInvocationStatementContext, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStatement"):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)

    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_statement)
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 53, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.varValStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.assignStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 521
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 522
                self.forInStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 523
                self.breakStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 524
                self.continueStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 525
                self.returnStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 526
                self.methodInvocationStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 527
                self.blockStatement()
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
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

        def indexedArray(self):
            return self.getTypedRuleContext(D96Parser.IndexedArrayContext, 0)

        def multiDimentionalArray(self):
            return self.getTypedRuleContext(D96Parser.MultiDimentionalArrayContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLiteral"):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)

    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_literal)
        try:
            self.state = 537
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 54, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(D96Parser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self.match(D96Parser.INTEGER_LITERAL2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 532
                self.match(D96Parser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 533
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 534
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 535
                self.indexedArray()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 536
                self.multiDimentionalArray()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IndexedArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ARRAY(self):
            return self.getToken(D96Parser.K_ARRAY, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def INTEGER_LITERAL2(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.INTEGER_LITERAL2)
            else:
                return self.getToken(D96Parser.INTEGER_LITERAL2, i)

        def FLOAT_LITERAL(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.FLOAT_LITERAL)
            else:
                return self.getToken(D96Parser.FLOAT_LITERAL, i)

        def BOOLEAN_LITERAL(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.BOOLEAN_LITERAL)
            else:
                return self.getToken(D96Parser.BOOLEAN_LITERAL, i)

        def STRING_LITERAL(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.STRING_LITERAL)
            else:
                return self.getToken(D96Parser.STRING_LITERAL, i)

        def INTEGER_LITERAL(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.INTEGER_LITERAL)
            else:
                return self.getToken(D96Parser.INTEGER_LITERAL, i)

        def indexedArray(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IndexedArrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.IndexedArrayContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_indexedArray

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIndexedArray"):
                return visitor.visitIndexedArray(self)
            else:
                return visitor.visitChildren(self)

    def indexedArray(self):

        localctx = D96Parser.IndexedArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_indexedArray)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.match(D96Parser.K_ARRAY)
            self.state = 540
            self.match(D96Parser.LEFT_PAREN)
            self.state = 591
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RIGHT_PAREN, D96Parser.INTEGER_LITERAL]:
                self.state = 549
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == D96Parser.INTEGER_LITERAL:
                    self.state = 541
                    self.match(D96Parser.INTEGER_LITERAL)
                    self.state = 546
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la == D96Parser.COMMA:
                        self.state = 542
                        self.match(D96Parser.COMMA)
                        self.state = 543
                        self.match(D96Parser.INTEGER_LITERAL)
                        self.state = 548
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                pass
            elif token in [D96Parser.INTEGER_LITERAL2]:
                self.state = 551
                self.match(D96Parser.INTEGER_LITERAL2)
                self.state = 556
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == D96Parser.COMMA:
                    self.state = 552
                    self.match(D96Parser.COMMA)
                    self.state = 553
                    self.match(D96Parser.INTEGER_LITERAL2)
                    self.state = 558
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.state = 559
                self.match(D96Parser.FLOAT_LITERAL)
                self.state = 564
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == D96Parser.COMMA:
                    self.state = 560
                    self.match(D96Parser.COMMA)
                    self.state = 561
                    self.match(D96Parser.FLOAT_LITERAL)
                    self.state = 566
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.state = 567
                self.match(D96Parser.BOOLEAN_LITERAL)
                self.state = 572
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == D96Parser.COMMA:
                    self.state = 568
                    self.match(D96Parser.COMMA)
                    self.state = 569
                    self.match(D96Parser.BOOLEAN_LITERAL)
                    self.state = 574
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.state = 575
                self.match(D96Parser.STRING_LITERAL)
                self.state = 580
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == D96Parser.COMMA:
                    self.state = 576
                    self.match(D96Parser.COMMA)
                    self.state = 577
                    self.match(D96Parser.STRING_LITERAL)
                    self.state = 582
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 583
                self.indexedArray()
                self.state = 588
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == D96Parser.COMMA:
                    self.state = 584
                    self.match(D96Parser.COMMA)
                    self.state = 585
                    self.indexedArray()
                    self.state = 590
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 593
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiDimentionalArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ARRAY(self):
            return self.getToken(D96Parser.K_ARRAY, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def indexedArray(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IndexedArrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.IndexedArrayContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_multiDimentionalArray

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMultiDimentionalArray"):
                return visitor.visitMultiDimentionalArray(self)
            else:
                return visitor.visitChildren(self)

    def multiDimentionalArray(self):

        localctx = D96Parser.MultiDimentionalArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_multiDimentionalArray)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.match(D96Parser.K_ARRAY)
            self.state = 596
            self.match(D96Parser.LEFT_PAREN)

            self.state = 605
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == D96Parser.K_ARRAY:
                self.state = 597
                self.indexedArray()
                self.state = 602
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == D96Parser.COMMA:
                    self.state = 598
                    self.match(D96Parser.COMMA)
                    self.state = 599
                    self.indexedArray()
                    self.state = 604
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 607
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
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
            return D96Parser.RULE_primitiveType

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPrimitiveType"):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)

    def primitiveType(self):

        localctx = D96Parser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_primitiveType)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << D96Parser.K_INT) | (1 << D96Parser.K_FLOAT) | (1 << D96Parser.K_BOOLEAN) | (
                    1 << D96Parser.K_STRING))) != 0)):
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

    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
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

        def primitiveType(self):
            return self.getTypedRuleContext(D96Parser.PrimitiveTypeContext, 0)

        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayType

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitArrayType"):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)

    def arrayType(self):

        localctx = D96Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.match(D96Parser.K_ARRAY)
            self.state = 612
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 615
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_INT, D96Parser.K_FLOAT, D96Parser.K_BOOLEAN, D96Parser.K_STRING]:
                self.state = 613
                self.primitiveType()
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 614
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 617
            self.match(D96Parser.COMMA)
            self.state = 618
            self.match(D96Parser.INTEGER_LITERAL2)
            self.state = 619
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
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
        self._predicates[20] = self.andOrExpr_sempred
        self._predicates[21] = self.addSubExpr_sempred
        self._predicates[22] = self.mulAddMolExpr_sempred
        self._predicates[25] = self.indexOperatorExpr_sempred
        self._predicates[26] = self.instanceAccess_sempred
        self._predicates[43] = self.memberAccessInstance_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def andOrExpr_sempred(self, localctx: AndOrExprContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 2)

    def addSubExpr_sempred(self, localctx: AddSubExprContext, predIndex: int):
        if predIndex == 1:
            return self.precpred(self._ctx, 2)

    def mulAddMolExpr_sempred(self, localctx: MulAddMolExprContext, predIndex: int):
        if predIndex == 2:
            return self.precpred(self._ctx, 2)

    def indexOperatorExpr_sempred(self, localctx: IndexOperatorExprContext, predIndex: int):
        if predIndex == 3:
            return self.precpred(self._ctx, 2)

    def instanceAccess_sempred(self, localctx: InstanceAccessContext, predIndex: int):
        if predIndex == 4:
            return self.precpred(self._ctx, 2)

    def memberAccessInstance_sempred(self, localctx: MemberAccessInstanceContext, predIndex: int):
        if predIndex == 5:
            return self.precpred(self._ctx, 3)
