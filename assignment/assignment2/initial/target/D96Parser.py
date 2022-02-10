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
    RULE_member_access_instance = 43
    RULE_member_access_static = 44
    RULE_method_invocation_statement = 45
    RULE_block_statement = 46
    RULE_statement = 47
    RULE_literal = 48
    RULE_indexed_array = 49
    RULE_multi_dimentional_array = 50
    RULE_primitive_type = 51
    RULE_array_type = 52

    ruleNames = ["program", "class_declaration", "class_body_unit", "super_class_group",
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
                 "member_access_instance", "member_access_static", "method_invocation_statement",
                 "block_statement", "statement", "literal", "indexed_array",
                 "multi_dimentional_array", "primitive_type", "array_type"]

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

        def class_declaration(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declarationContext, i)

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
                self.class_declaration()
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

    class Class_declarationContext(ParserRuleContext):
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

        def super_class_group(self):
            return self.getTypedRuleContext(D96Parser.Super_class_groupContext, 0)

        def class_body_unit(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_body_unitContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_body_unitContext, i)

        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitClass_declaration"):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)

    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declaration)
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
                self.super_class_group()

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
                self.class_body_unit()
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

    class Class_body_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declarationContext, 0)

        def method_declaration(self):
            return self.getTypedRuleContext(D96Parser.Method_declarationContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_body_unit

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitClass_body_unit"):
                return visitor.visitClass_body_unit(self)
            else:
                return visitor.visitChildren(self)

    def class_body_unit(self):

        localctx = D96Parser.Class_body_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body_unit)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_VAL, D96Parser.K_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.attribute_declaration()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR, D96Parser.K_DESTRUCTOR, D96Parser.IDENTIFIER,
                           D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_super_class_group

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSuper_class_group"):
                return visitor.visitSuper_class_group(self)
            else:
                return visitor.visitChildren(self)

    def super_class_group(self):

        localctx = D96Parser.Super_class_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_super_class_group)
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

    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_listContext, 0)

        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext, 0)

        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_declaration

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMethod_declaration"):
                return visitor.visitMethod_declaration(self)
            else:
                return visitor.visitChildren(self)

    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_method_declaration)
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
                    self.parameter_list()

                self.state = 139
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 140
                self.block_statement()
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

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_listContext, 0)

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
                self.parameter_list()

            self.state = 150
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 151
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_DESTRUCTOR(self):
            return self.getToken(D96Parser.K_DESTRUCTOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext, 0)

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
            return D96Parser.RULE_parameter_list

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParameter_list"):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)

    def parameter_list(self):

        localctx = D96Parser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter_list)
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

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96_type(self):
            return self.getTypedRuleContext(D96Parser.D96_typeContext, 0)

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
            self.identifier_list()
            self.state = 169
            self.match(D96Parser.COLON)
            self.state = 170
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_d96_type

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitD96_type"):
                return visitor.visitD96_type(self)
            else:
                return visitor.visitChildren(self)

    def d96_type(self):

        localctx = D96Parser.D96_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_d96_type)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_INT, D96Parser.K_FLOAT, D96Parser.K_BOOLEAN, D96Parser.K_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.primitive_type()
                pass
            elif token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mixed_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Mixed_identifier_listContext, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96_type(self):
            return self.getTypedRuleContext(D96Parser.D96_typeContext, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

        def attribute_value_list(self):
            return self.getTypedRuleContext(D96Parser.Attribute_value_listContext, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declaration

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAttribute_declaration"):
                return visitor.visitAttribute_declaration(self)
            else:
                return visitor.visitChildren(self)

    def attribute_declaration(self):

        localctx = D96Parser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attribute_declaration)
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
                self.mixed_identifier_list()
                self.state = 179
                self.match(D96Parser.COLON)
                self.state = 180
                self.d96_type()
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
                self.attribute_value_list()
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

    class Attribute_value_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96_type(self):
            return self.getTypedRuleContext(D96Parser.D96_typeContext, 0)

        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def attribute_value_list(self):
            return self.getTypedRuleContext(D96Parser.Attribute_value_listContext, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_value_list

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAttribute_value_list"):
                return visitor.visitAttribute_value_list(self)
            else:
                return visitor.visitChildren(self)

    def attribute_value_list(self):

        localctx = D96Parser.Attribute_value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attribute_value_list)
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
                self.d96_type()
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
                self.attribute_value_list()
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

    class Identifier_listContext(ParserRuleContext):
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
            return D96Parser.RULE_identifier_list

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIdentifier_list"):
                return visitor.visitIdentifier_list(self)
            else:
                return visitor.visitChildren(self)

    def identifier_list(self):

        localctx = D96Parser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_identifier_list)
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

    class Mixed_identifier_listContext(ParserRuleContext):
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
            return D96Parser.RULE_mixed_identifier_list

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMixed_identifier_list"):
                return visitor.visitMixed_identifier_list(self)
            else:
                return visitor.visitChildren(self)

    def mixed_identifier_list(self):

        localctx = D96Parser.Mixed_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_mixed_identifier_list)
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

    class Expression_listContext(ParserRuleContext):
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
            return D96Parser.RULE_expression_list

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpression_list"):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)

    def expression_list(self):

        localctx = D96Parser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression_list)
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

    class Element_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_element_expression

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitElement_expression"):
                return visitor.visitElement_expression(self)
            else:
                return visitor.visitChildren(self)

    def element_expression(self):

        localctx = D96Parser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.expression()
            self.state = 234
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.LEFT_SQUARE_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_SQUARE_BRACKET, 0)

        def index_operator(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Index_operatorContext)
            else:
                return self.getTypedRuleContext(D96Parser.Index_operatorContext, i)

        def getRuleIndex(self):
            return D96Parser.RULE_index_operator

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIndex_operator"):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)

    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_index_operator)
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
                    self.index_operator()
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

    class Relational_operatorContext(ParserRuleContext):
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
            return D96Parser.RULE_relational_operator

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRelational_operator"):
                return visitor.visitRelational_operator(self)
            else:
                return visitor.visitChildren(self)

    def relational_operator(self):

        localctx = D96Parser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_relational_operator)
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

        def relational_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Relational_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.Relational_exprContext, i)

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
                self.relational_expr()
                self.state = 248
                _la = self._input.LA(1)
                if not (_la == D96Parser.OP_STRING_CONCATENATION or _la == D96Parser.OP_TWO_SAME_STRING):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 249
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_or_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.And_or_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.And_or_exprContext, i)

        def relational_operator(self):
            return self.getTypedRuleContext(D96Parser.Relational_operatorContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relational_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRelational_expr"):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)

    def relational_expr(self):

        localctx = D96Parser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relational_expr)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 20, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.and_or_expr(0)
                self.state = 255
                self.relational_operator()
                self.state = 256
                self.and_or_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_sub_expr(self):
            return self.getTypedRuleContext(D96Parser.Add_sub_exprContext, 0)

        def and_or_expr(self):
            return self.getTypedRuleContext(D96Parser.And_or_exprContext, 0)

        def OP_LOGICAL_AND(self):
            return self.getToken(D96Parser.OP_LOGICAL_AND, 0)

        def OP_LOGICAL_OR(self):
            return self.getToken(D96Parser.OP_LOGICAL_OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_and_or_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAnd_or_expr"):
                return visitor.visitAnd_or_expr(self)
            else:
                return visitor.visitChildren(self)

    def and_or_expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.And_or_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_and_or_expr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.add_sub_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 21, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.And_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_or_expr)
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
                    self.add_sub_expr(0)
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

    class Add_sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_add_mol_expr(self):
            return self.getTypedRuleContext(D96Parser.Mul_add_mol_exprContext, 0)

        def add_sub_expr(self):
            return self.getTypedRuleContext(D96Parser.Add_sub_exprContext, 0)

        def OP_ADDTION(self):
            return self.getToken(D96Parser.OP_ADDTION, 0)

        def OP_SUBTRACTION(self):
            return self.getToken(D96Parser.OP_SUBTRACTION, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_add_sub_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAdd_sub_expr"):
                return visitor.visitAdd_sub_expr(self)
            else:
                return visitor.visitChildren(self)

    def add_sub_expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Add_sub_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_add_sub_expr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.mul_add_mol_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 22, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Add_sub_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expr)
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
                    self.mul_add_mol_expr(0)
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

    class Mul_add_mol_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_expr(self):
            return self.getTypedRuleContext(D96Parser.Not_exprContext, 0)

        def mul_add_mol_expr(self):
            return self.getTypedRuleContext(D96Parser.Mul_add_mol_exprContext, 0)

        def OP_MULTIPLICATION(self):
            return self.getToken(D96Parser.OP_MULTIPLICATION, 0)

        def OP_DIVISION(self):
            return self.getToken(D96Parser.OP_DIVISION, 0)

        def OP_MODULO(self):
            return self.getToken(D96Parser.OP_MODULO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mul_add_mol_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMul_add_mol_expr"):
                return visitor.visitMul_add_mol_expr(self)
            else:
                return visitor.visitChildren(self)

    def mul_add_mol_expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Mul_add_mol_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_mul_add_mol_expr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 23, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Mul_add_mol_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_add_mol_expr)
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
                    self.not_expr()
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

    class Not_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_LOGICAL_NOT(self):
            return self.getToken(D96Parser.OP_LOGICAL_NOT, 0)

        def not_expr(self):
            return self.getTypedRuleContext(D96Parser.Not_exprContext, 0)

        def sign_expr(self):
            return self.getTypedRuleContext(D96Parser.Sign_exprContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_not_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNot_expr"):
                return visitor.visitNot_expr(self)
            else:
                return visitor.visitChildren(self)

    def not_expr(self):

        localctx = D96Parser.Not_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_not_expr)
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(D96Parser.OP_LOGICAL_NOT)
                self.state = 295
                self.not_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_NEW, D96Parser.OP_SUBTRACTION,
                           D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL,
                           D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL,
                           D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_expr(self):
            return self.getTypedRuleContext(D96Parser.Sign_exprContext, 0)

        def OP_SUBTRACTION(self):
            return self.getToken(D96Parser.OP_SUBTRACTION, 0)

        def index_operator_expr(self):
            return self.getTypedRuleContext(D96Parser.Index_operator_exprContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_sign_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSign_expr"):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)

    def sign_expr(self):

        localctx = D96Parser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_sign_expr)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUBTRACTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(D96Parser.OP_SUBTRACTION)
                self.state = 300
                self.sign_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_NEW, D96Parser.LEFT_PAREN,
                           D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL,
                           D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_accessContext, 0)

        def index_operator_expr(self):
            return self.getTypedRuleContext(D96Parser.Index_operator_exprContext, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_index_operator_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIndex_operator_expr"):
                return visitor.visitIndex_operator_expr(self)
            else:
                return visitor.visitChildren(self)

    def index_operator_expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_operator_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_index_operator_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.instance_access(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 26, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operator_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operator_expr)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    self.index_operator()
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

    class Instance_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_access(self):
            return self.getTypedRuleContext(D96Parser.Static_accessContext, 0)

        def instance_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_accessContext, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_access

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitInstance_access"):
                return visitor.visitInstance_access(self)
            else:
                return visitor.visitChildren(self)

    def instance_access(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Instance_accessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_instance_access, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.static_access()
            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 29, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Instance_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_access)
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
                            self.expression_list()

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

    class Static_accessContext(ParserRuleContext):
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

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext, 0)

        def object_creation(self):
            return self.getTypedRuleContext(D96Parser.Object_creationContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_access

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStatic_access"):
                return visitor.visitStatic_access(self)
            else:
                return visitor.visitChildren(self)

    def static_access(self):

        localctx = D96Parser.Static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_static_access)
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
                        self.expression_list()

                    self.state = 339
                    self.match(D96Parser.RIGHT_PAREN)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
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

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext, 0)

        def atom_expr(self):
            return self.getTypedRuleContext(D96Parser.Atom_exprContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_object_creation

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitObject_creation"):
                return visitor.visitObject_creation(self)
            else:
                return visitor.visitChildren(self)

    def object_creation(self):

        localctx = D96Parser.Object_creationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_object_creation)
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
                    self.expression_list()

                self.state = 351
                self.match(D96Parser.RIGHT_PAREN)
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2,
                           D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL,
                           D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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
            return D96Parser.RULE_atom_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAtom_expr"):
                return visitor.visitAtom_expr(self)
            else:
                return visitor.visitChildren(self)

    def atom_expr(self):

        localctx = D96Parser.Atom_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_atom_expr)
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

    class Var_val_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96_type(self):
            return self.getTypedRuleContext(D96Parser.D96_typeContext, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def var_val_value_list(self):
            return self.getTypedRuleContext(D96Parser.Var_val_value_listContext, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_val_statement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVar_val_statement"):
                return visitor.visitVar_val_statement(self)
            else:
                return visitor.visitChildren(self)

    def var_val_statement(self):

        localctx = D96Parser.Var_val_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_var_val_statement)
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
                self.identifier_list()
                self.state = 366
                self.match(D96Parser.COLON)
                self.state = 367
                self.d96_type()
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
                self.var_val_value_list()
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

    class Var_val_value_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96_type(self):
            return self.getTypedRuleContext(D96Parser.D96_typeContext, 0)

        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def var_val_value_list(self):
            return self.getTypedRuleContext(D96Parser.Var_val_value_listContext, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_val_value_list

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVar_val_value_list"):
                return visitor.visitVar_val_value_list(self)
            else:
                return visitor.visitChildren(self)

    def var_val_value_list(self):

        localctx = D96Parser.Var_val_value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_var_val_value_list)
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.match(D96Parser.COLON)
                self.state = 379
                self.d96_type()
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
                self.var_val_value_list()
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

        def member_access_instance(self):
            return self.getTypedRuleContext(D96Parser.Member_access_instanceContext, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def element_expression(self):
            return self.getTypedRuleContext(D96Parser.Element_expressionContext, 0)

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
                self.member_access_instance(0)
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
            return D96Parser.RULE_assign_statement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAssign_statement"):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)

    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assign_statement)
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

    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_part(self):
            return self.getTypedRuleContext(D96Parser.If_partContext, 0)

        def else_if_part(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Else_if_partContext)
            else:
                return self.getTypedRuleContext(D96Parser.Else_if_partContext, i)

        def else_part(self):
            return self.getTypedRuleContext(D96Parser.Else_partContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_statement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIf_statement"):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)

    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_if_statement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.if_part()
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == D96Parser.K_ELSE_IF:
                self.state = 407
                self.else_if_part()
                self.state = 412
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == D96Parser.K_ELSE:
                self.state = 413
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

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_part

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIf_part"):
                return visitor.visitIf_part(self)
            else:
                return visitor.visitChildren(self)

    def if_part(self):

        localctx = D96Parser.If_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_part)
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

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_else_if_part

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitElse_if_part"):
                return visitor.visitElse_if_part(self)
            else:
                return visitor.visitChildren(self)

    def else_if_part(self):

        localctx = D96Parser.Else_if_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_else_if_part)
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ELSE(self):
            return self.getToken(D96Parser.K_ELSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_else_part

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitElse_part"):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)

    def else_part(self):

        localctx = D96Parser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(D96Parser.K_ELSE)
            self.state = 429
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_FOR_EACH(self):
            return self.getToken(D96Parser.K_FOR_EACH, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def loop_part(self):
            return self.getTypedRuleContext(D96Parser.Loop_partContext, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_statement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFor_in_statement"):
                return visitor.visitFor_in_statement(self)
            else:
                return visitor.visitChildren(self)

    def for_in_statement(self):

        localctx = D96Parser.For_in_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_for_in_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(D96Parser.K_FOR_EACH)
            self.state = 432
            self.match(D96Parser.LEFT_PAREN)
            self.state = 433
            self.loop_part()
            self.state = 434
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 435
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_instance(self):
            return self.getTypedRuleContext(D96Parser.Member_access_instanceContext, 0)

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
            return D96Parser.RULE_loop_part

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLoop_part"):
                return visitor.visitLoop_part(self)
            else:
                return visitor.visitChildren(self)

    def loop_part(self):

        localctx = D96Parser.Loop_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_loop_part)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.member_access_instance(0)
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

    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_BREAK(self):
            return self.getToken(D96Parser.K_BREAK, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBreak_statement"):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)

    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_break_statement)
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

    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_CONTINUE(self):
            return self.getToken(D96Parser.K_CONTINUE, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitContinue_statement"):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)

    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_continue_statement)
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

    class Return_statementContext(ParserRuleContext):
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
            return D96Parser.RULE_return_statement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitReturn_statement"):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)

    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_return_statement)
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

    class Member_access_instanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_static(self):
            return self.getTypedRuleContext(D96Parser.Member_access_staticContext, 0)

        def object_creation(self):
            return self.getTypedRuleContext(D96Parser.Object_creationContext, 0)

        def member_access_instance(self):
            return self.getTypedRuleContext(D96Parser.Member_access_instanceContext, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_member_access_instance

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMember_access_instance"):
                return visitor.visitMember_access_instance(self)
            else:
                return visitor.visitChildren(self)

    def member_access_instance(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Member_access_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_member_access_instance, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 43, self._ctx)
            if la_ == 1:
                self.state = 459
                self.member_access_static()
                pass

            elif la_ == 2:
                self.state = 460
                self.object_creation()
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
                    localctx = D96Parser.Member_access_instanceContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_instance)
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
                            self.expression_list()

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

    class Member_access_staticContext(ParserRuleContext):
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

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_member_access_static

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMember_access_static"):
                return visitor.visitMember_access_static(self)
            else:
                return visitor.visitChildren(self)

    def member_access_static(self):

        localctx = D96Parser.Member_access_staticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_member_access_static)
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
                    self.expression_list()

                self.state = 486
                self.match(D96Parser.RIGHT_PAREN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_invocation_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def member_access_instance(self):
            return self.getTypedRuleContext(D96Parser.Member_access_instanceContext, 0)

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

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_statement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMethod_invocation_statement"):
                return visitor.visitMethod_invocation_statement(self)
            else:
                return visitor.visitChildren(self)

    def method_invocation_statement(self):

        localctx = D96Parser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_method_invocation_statement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 51, self._ctx)
            if la_ == 1:
                self.state = 489
                self.member_access_instance(0)
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
                    self.expression_list()

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
                    self.expression_list()

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

    class Block_statementContext(ParserRuleContext):
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
            return D96Parser.RULE_block_statement

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBlock_statement"):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)

    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_block_statement)
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

        def var_val_statement(self):
            return self.getTypedRuleContext(D96Parser.Var_val_statementContext, 0)

        def assign_statement(self):
            return self.getTypedRuleContext(D96Parser.Assign_statementContext, 0)

        def if_statement(self):
            return self.getTypedRuleContext(D96Parser.If_statementContext, 0)

        def for_in_statement(self):
            return self.getTypedRuleContext(D96Parser.For_in_statementContext, 0)

        def break_statement(self):
            return self.getTypedRuleContext(D96Parser.Break_statementContext, 0)

        def continue_statement(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementContext, 0)

        def return_statement(self):
            return self.getTypedRuleContext(D96Parser.Return_statementContext, 0)

        def method_invocation_statement(self):
            return self.getTypedRuleContext(D96Parser.Method_invocation_statementContext, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext, 0)

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
                self.var_val_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 521
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 522
                self.for_in_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 523
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 524
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 525
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 526
                self.method_invocation_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 527
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

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext, 0)

        def multi_dimentional_array(self):
            return self.getTypedRuleContext(D96Parser.Multi_dimentional_arrayContext, 0)

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
                self.indexed_array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 536
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

        def indexed_array(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Indexed_arrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.Indexed_arrayContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_indexed_array

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIndexed_array"):
                return visitor.visitIndexed_array(self)
            else:
                return visitor.visitChildren(self)

    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_indexed_array)
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
                self.indexed_array()
                self.state = 588
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == D96Parser.COMMA:
                    self.state = 584
                    self.match(D96Parser.COMMA)
                    self.state = 585
                    self.indexed_array()
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

    class Multi_dimentional_arrayContext(ParserRuleContext):
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

        def indexed_array(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Indexed_arrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.Indexed_arrayContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_multi_dimentional_array

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMulti_dimentional_array"):
                return visitor.visitMulti_dimentional_array(self)
            else:
                return visitor.visitChildren(self)

    def multi_dimentional_array(self):

        localctx = D96Parser.Multi_dimentional_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_multi_dimentional_array)
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
                self.indexed_array()
                self.state = 602
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == D96Parser.COMMA:
                    self.state = 598
                    self.match(D96Parser.COMMA)
                    self.state = 599
                    self.indexed_array()
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

    class Primitive_typeContext(ParserRuleContext):
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
            return D96Parser.RULE_primitive_type

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPrimitive_type"):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)

    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_primitive_type)
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

    class Array_typeContext(ParserRuleContext):
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

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitArray_type"):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)

    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_array_type)
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
                self.primitive_type()
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 614
                self.array_type()
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
        self._predicates[20] = self.and_or_expr_sempred
        self._predicates[21] = self.add_sub_expr_sempred
        self._predicates[22] = self.mul_add_mol_expr_sempred
        self._predicates[25] = self.index_operator_expr_sempred
        self._predicates[26] = self.instance_access_sempred
        self._predicates[43] = self.member_access_instance_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def and_or_expr_sempred(self, localctx: And_or_exprContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 2)

    def add_sub_expr_sempred(self, localctx: Add_sub_exprContext, predIndex: int):
        if predIndex == 1:
            return self.precpred(self._ctx, 2)

    def mul_add_mol_expr_sempred(self, localctx: Mul_add_mol_exprContext, predIndex: int):
        if predIndex == 2:
            return self.precpred(self._ctx, 2)

    def index_operator_expr_sempred(self, localctx: Index_operator_exprContext, predIndex: int):
        if predIndex == 3:
            return self.precpred(self._ctx, 2)

    def instance_access_sempred(self, localctx: Instance_accessContext, predIndex: int):
        if predIndex == 4:
            return self.precpred(self._ctx, 2)

    def member_access_instance_sempred(self, localctx: Member_access_instanceContext, predIndex: int):
        if predIndex == 5:
            return self.precpred(self._ctx, 3)
