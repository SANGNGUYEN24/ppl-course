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
        buf.write("\u025e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\6\u008c\n\6\3\6\3\6\3\6\3\6\3\6\5\6\u0093\n\6\3\7\3\7")
        buf.write("\3\7\5\7\u0098\n\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\6\t\u00a6\n\t\r\t\16\t\u00a7\5\t\u00aa\n")
        buf.write("\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\5\13\u00b3\n\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\f\u00bb\n\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\6\r\u00c3\n\r\r\r\16\r\u00c4\5\r\u00c7\n\r\3\16\3")
        buf.write("\16\3\16\3\16\6\16\u00cd\n\16\r\16\16\16\u00ce\5\16\u00d1")
        buf.write("\n\16\3\17\3\17\3\17\3\17\6\17\u00d7\n\17\r\17\16\17\u00d8")
        buf.write("\5\17\u00db\n\17\3\20\3\20\3\20\3\20\6\20\u00e1\n\20\r")
        buf.write("\20\16\20\u00e2\5\20\u00e5\n\20\3\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\22\7\22\u00ee\n\22\f\22\16\22\u00f1\13\22\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u00fa\n\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0101\n\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\7\26\u0109\n\26\f\26\16\26\u010c\13\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\7\27\u0114\n\27\f\27\16\27")
        buf.write("\u0117\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u011f")
        buf.write("\n\30\f\30\16\30\u0122\13\30\3\31\3\31\3\31\5\31\u0127")
        buf.write("\n\31\3\32\3\32\3\32\5\32\u012c\n\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\7\33\u0133\n\33\f\33\16\33\u0136\13\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0140\n\34\3\34")
        buf.write("\5\34\u0143\n\34\7\34\u0145\n\34\f\34\16\34\u0148\13\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\5\35\u014f\n\35\3\35\5\35\u0152")
        buf.write("\n\35\3\35\5\35\u0155\n\35\3\36\3\36\3\36\3\36\5\36\u015b")
        buf.write("\n\36\3\36\3\36\5\36\u015f\n\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\5\37\u0167\n\37\3 \3 \3 \3 \3 \5 \u016e\n \3")
        buf.write(" \3 \3 \3 \3 \5 \u0175\n \3!\3!\3!\5!\u017a\n!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\5!\u0184\n!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\5\"\u0191\n\"\3#\3#\3#\3#\3#\3$\3$")
        buf.write("\7$\u019a\n$\f$\16$\u019d\13$\3$\5$\u01a0\n$\3%\3%\3%")
        buf.write("\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write("(\3(\3)\3)\3)\3)\3)\3)\3)\5)\u01be\n)\3*\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\5,\u01c8\n,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01d4")
        buf.write("\n-\3-\5-\u01d7\n-\3-\3-\3-\3-\3-\5-\u01de\n-\3-\5-\u01e1")
        buf.write("\n-\7-\u01e3\n-\f-\16-\u01e6\13-\3.\3.\3.\3.\3.\5.\u01ed")
        buf.write("\n.\3.\3.\5.\u01f1\n.\3.\3.\3.\3/\3/\7/\u01f8\n/\f/\16")
        buf.write("/\u01fb\13/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\5\60\u0208\n\60\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u0211\n\61\3\62\3\62\3\62\3\62\3\62\7\62\u0218")
        buf.write("\n\62\f\62\16\62\u021b\13\62\3\62\3\62\3\62\7\62\u0220")
        buf.write("\n\62\f\62\16\62\u0223\13\62\3\62\3\62\3\62\7\62\u0228")
        buf.write("\n\62\f\62\16\62\u022b\13\62\3\62\3\62\3\62\7\62\u0230")
        buf.write("\n\62\f\62\16\62\u0233\13\62\3\62\3\62\3\62\7\62\u0238")
        buf.write("\n\62\f\62\16\62\u023b\13\62\3\62\5\62\u023e\n\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\7\63\u0247\n\63\f\63\16")
        buf.write("\63\u024a\13\63\5\63\u024c\n\63\3\63\3\63\3\64\3\64\3")
        buf.write("\65\3\65\3\66\3\66\3\66\3\66\5\66\u0258\n\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\2\b*,.\64\66X\67\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhj\2\n\3\2\23\24\3\2;<\4\2\35\36$\'\3\2()\3")
        buf.write("\2\33\34\3\2 !\4\2\37\37\"#\3\2\f\17\2\u0280\2m\3\2\2")
        buf.write("\2\4s\3\2\2\2\6\u0083\3\2\2\2\b\u0085\3\2\2\2\n\u0092")
        buf.write("\3\2\2\2\f\u0094\3\2\2\2\16\u009c\3\2\2\2\20\u00a9\3\2")
        buf.write("\2\2\22\u00ab\3\2\2\2\24\u00b2\3\2\2\2\26\u00b4\3\2\2")
        buf.write("\2\30\u00c6\3\2\2\2\32\u00d0\3\2\2\2\34\u00da\3\2\2\2")
        buf.write("\36\u00e4\3\2\2\2 \u00e6\3\2\2\2\"\u00e9\3\2\2\2$\u00f2")
        buf.write("\3\2\2\2&\u00f9\3\2\2\2(\u0100\3\2\2\2*\u0102\3\2\2\2")
        buf.write(",\u010d\3\2\2\2.\u0118\3\2\2\2\60\u0126\3\2\2\2\62\u012b")
        buf.write("\3\2\2\2\64\u012d\3\2\2\2\66\u0137\3\2\2\28\u0154\3\2")
        buf.write("\2\2:\u015e\3\2\2\2<\u0166\3\2\2\2>\u0174\3\2\2\2@\u0183")
        buf.write("\3\2\2\2B\u0190\3\2\2\2D\u0192\3\2\2\2F\u0197\3\2\2\2")
        buf.write("H\u01a1\3\2\2\2J\u01a7\3\2\2\2L\u01ad\3\2\2\2N\u01b0\3")
        buf.write("\2\2\2P\u01b6\3\2\2\2R\u01bf\3\2\2\2T\u01c2\3\2\2\2V\u01c5")
        buf.write("\3\2\2\2X\u01cb\3\2\2\2Z\u01e7\3\2\2\2\\\u01f5\3\2\2\2")
        buf.write("^\u0207\3\2\2\2`\u0210\3\2\2\2b\u0212\3\2\2\2d\u0241\3")
        buf.write("\2\2\2f\u024f\3\2\2\2h\u0251\3\2\2\2j\u0253\3\2\2\2ln")
        buf.write("\5\4\3\2ml\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2pq\3\2")
        buf.write("\2\2qr\7\2\2\3r\3\3\2\2\2st\7\22\2\2tv\7;\2\2uw\5\b\5")
        buf.write("\2vu\3\2\2\2vw\3\2\2\2wx\3\2\2\2x|\7\64\2\2y{\5\6\4\2")
        buf.write("zy\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\177\3\2\2\2")
        buf.write("~|\3\2\2\2\177\u0080\7\65\2\2\u0080\5\3\2\2\2\u0081\u0084")
        buf.write("\5\26\f\2\u0082\u0084\5\n\6\2\u0083\u0081\3\2\2\2\u0083")
        buf.write("\u0082\3\2\2\2\u0084\7\3\2\2\2\u0085\u0086\7\61\2\2\u0086")
        buf.write("\u0087\7;\2\2\u0087\t\3\2\2\2\u0088\u0089\5f\64\2\u0089")
        buf.write("\u008b\7*\2\2\u008a\u008c\5\20\t\2\u008b\u008a\3\2\2\2")
        buf.write("\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\7")
        buf.write("+\2\2\u008e\u008f\5\\/\2\u008f\u0093\3\2\2\2\u0090\u0093")
        buf.write("\5\f\7\2\u0091\u0093\5\16\b\2\u0092\u0088\3\2\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0092\u0091\3\2\2\2\u0093\13\3\2\2\2\u0094")
        buf.write("\u0095\7\25\2\2\u0095\u0097\7*\2\2\u0096\u0098\5\20\t")
        buf.write("\2\u0097\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009a\7+\2\2\u009a\u009b\5\\/\2\u009b\r")
        buf.write("\3\2\2\2\u009c\u009d\7\26\2\2\u009d\u009e\7*\2\2\u009e")
        buf.write("\u009f\7+\2\2\u009f\u00a0\5\\/\2\u00a0\17\3\2\2\2\u00a1")
        buf.write("\u00aa\5\22\n\2\u00a2\u00a5\5\22\n\2\u00a3\u00a4\7\63")
        buf.write("\2\2\u00a4\u00a6\5\22\n\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7")
        buf.write("\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00aa\3\2\2\2\u00a9\u00a1\3\2\2\2\u00a9\u00a2\3\2\2\2")
        buf.write("\u00aa\21\3\2\2\2\u00ab\u00ac\5\30\r\2\u00ac\u00ad\7\61")
        buf.write("\2\2\u00ad\u00ae\5\24\13\2\u00ae\23\3\2\2\2\u00af\u00b3")
        buf.write("\5h\65\2\u00b0\u00b3\5f\64\2\u00b1\u00b3\5j\66\2\u00b2")
        buf.write("\u00af\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1\3\2\2\2")
        buf.write("\u00b3\25\3\2\2\2\u00b4\u00b5\t\2\2\2\u00b5\u00b6\5\34")
        buf.write("\17\2\u00b6\u00b7\7\61\2\2\u00b7\u00ba\5\24\13\2\u00b8")
        buf.write("\u00b9\7\31\2\2\u00b9\u00bb\5\36\20\2\u00ba\u00b8\3\2")
        buf.write("\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd")
        buf.write("\7\63\2\2\u00bd\27\3\2\2\2\u00be\u00c7\7;\2\2\u00bf\u00c2")
        buf.write("\7;\2\2\u00c0\u00c1\7\60\2\2\u00c1\u00c3\7;\2\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c2\3\2\2\2")
        buf.write("\u00c4\u00c5\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00be\3")
        buf.write("\2\2\2\u00c6\u00bf\3\2\2\2\u00c7\31\3\2\2\2\u00c8\u00d1")
        buf.write("\7<\2\2\u00c9\u00cc\7<\2\2\u00ca\u00cb\7\60\2\2\u00cb")
        buf.write("\u00cd\7<\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1\3")
        buf.write("\2\2\2\u00d0\u00c8\3\2\2\2\u00d0\u00c9\3\2\2\2\u00d1\33")
        buf.write("\3\2\2\2\u00d2\u00db\t\3\2\2\u00d3\u00d6\t\3\2\2\u00d4")
        buf.write("\u00d5\7\60\2\2\u00d5\u00d7\t\3\2\2\u00d6\u00d4\3\2\2")
        buf.write("\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00db\3\2\2\2\u00da\u00d2\3\2\2\2\u00da")
        buf.write("\u00d3\3\2\2\2\u00db\35\3\2\2\2\u00dc\u00e5\5&\24\2\u00dd")
        buf.write("\u00e0\5&\24\2\u00de\u00df\7\60\2\2\u00df\u00e1\5&\24")
        buf.write("\2\u00e0\u00de\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e0")
        buf.write("\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4")
        buf.write("\u00dc\3\2\2\2\u00e4\u00dd\3\2\2\2\u00e5\37\3\2\2\2\u00e6")
        buf.write("\u00e7\5&\24\2\u00e7\u00e8\5\"\22\2\u00e8!\3\2\2\2\u00e9")
        buf.write("\u00ea\7,\2\2\u00ea\u00eb\5&\24\2\u00eb\u00ef\7-\2\2\u00ec")
        buf.write("\u00ee\5\"\22\2\u00ed\u00ec\3\2\2\2\u00ee\u00f1\3\2\2")
        buf.write("\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0#\3\2")
        buf.write("\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\t\4\2\2\u00f3%\3")
        buf.write("\2\2\2\u00f4\u00f5\5(\25\2\u00f5\u00f6\t\5\2\2\u00f6\u00f7")
        buf.write("\5(\25\2\u00f7\u00fa\3\2\2\2\u00f8\u00fa\5(\25\2\u00f9")
        buf.write("\u00f4\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\'\3\2\2\2\u00fb")
        buf.write("\u00fc\5*\26\2\u00fc\u00fd\5$\23\2\u00fd\u00fe\5*\26\2")
        buf.write("\u00fe\u0101\3\2\2\2\u00ff\u0101\5*\26\2\u0100\u00fb\3")
        buf.write("\2\2\2\u0100\u00ff\3\2\2\2\u0101)\3\2\2\2\u0102\u0103")
        buf.write("\b\26\1\2\u0103\u0104\5,\27\2\u0104\u010a\3\2\2\2\u0105")
        buf.write("\u0106\f\4\2\2\u0106\u0107\t\6\2\2\u0107\u0109\5,\27\2")
        buf.write("\u0108\u0105\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3")
        buf.write("\2\2\2\u010a\u010b\3\2\2\2\u010b+\3\2\2\2\u010c\u010a")
        buf.write("\3\2\2\2\u010d\u010e\b\27\1\2\u010e\u010f\5.\30\2\u010f")
        buf.write("\u0115\3\2\2\2\u0110\u0111\f\4\2\2\u0111\u0112\t\7\2\2")
        buf.write("\u0112\u0114\5.\30\2\u0113\u0110\3\2\2\2\u0114\u0117\3")
        buf.write("\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116-")
        buf.write("\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\b\30\1\2\u0119")
        buf.write("\u011a\5\60\31\2\u011a\u0120\3\2\2\2\u011b\u011c\f\4\2")
        buf.write("\2\u011c\u011d\t\b\2\2\u011d\u011f\5\60\31\2\u011e\u011b")
        buf.write("\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121/\3\2\2\2\u0122\u0120\3\2\2\2\u0123")
        buf.write("\u0124\7\32\2\2\u0124\u0127\5\60\31\2\u0125\u0127\5\62")
        buf.write("\32\2\u0126\u0123\3\2\2\2\u0126\u0125\3\2\2\2\u0127\61")
        buf.write("\3\2\2\2\u0128\u0129\7!\2\2\u0129\u012c\5\62\32\2\u012a")
        buf.write("\u012c\5\64\33\2\u012b\u0128\3\2\2\2\u012b\u012a\3\2\2")
        buf.write("\2\u012c\63\3\2\2\2\u012d\u012e\b\33\1\2\u012e\u012f\5")
        buf.write("\66\34\2\u012f\u0134\3\2\2\2\u0130\u0131\f\4\2\2\u0131")
        buf.write("\u0133\5\"\22\2\u0132\u0130\3\2\2\2\u0133\u0136\3\2\2")
        buf.write("\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\65\3")
        buf.write("\2\2\2\u0136\u0134\3\2\2\2\u0137\u0138\b\34\1\2\u0138")
        buf.write("\u0139\58\35\2\u0139\u0146\3\2\2\2\u013a\u013b\f\4\2\2")
        buf.write("\u013b\u013c\7.\2\2\u013c\u0142\5f\64\2\u013d\u013f\7")
        buf.write("*\2\2\u013e\u0140\5\36\20\2\u013f\u013e\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0143\7+\2\2")
        buf.write("\u0142\u013d\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145\3")
        buf.write("\2\2\2\u0144\u013a\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147\67\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0149\u014a\7;\2\2\u014a\u014b\7\62\2\2\u014b")
        buf.write("\u0151\7<\2\2\u014c\u014e\7*\2\2\u014d\u014f\5\36\20\2")
        buf.write("\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\3")
        buf.write("\2\2\2\u0150\u0152\7+\2\2\u0151\u014c\3\2\2\2\u0151\u0152")
        buf.write("\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0155\5:\36\2\u0154")
        buf.write("\u0149\3\2\2\2\u0154\u0153\3\2\2\2\u01559\3\2\2\2\u0156")
        buf.write("\u0157\7\27\2\2\u0157\u0158\7;\2\2\u0158\u015a\7*\2\2")
        buf.write("\u0159\u015b\5\36\20\2\u015a\u0159\3\2\2\2\u015a\u015b")
        buf.write("\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015f\7+\2\2\u015d")
        buf.write("\u015f\5<\37\2\u015e\u0156\3\2\2\2\u015e\u015d\3\2\2\2")
        buf.write("\u015f;\3\2\2\2\u0160\u0167\5`\61\2\u0161\u0167\5f\64")
        buf.write("\2\u0162\u0163\7*\2\2\u0163\u0164\5&\24\2\u0164\u0165")
        buf.write("\7+\2\2\u0165\u0167\3\2\2\2\u0166\u0160\3\2\2\2\u0166")
        buf.write("\u0161\3\2\2\2\u0166\u0162\3\2\2\2\u0167=\3\2\2\2\u0168")
        buf.write("\u0169\t\2\2\2\u0169\u016a\5\30\r\2\u016a\u016d\7\61\2")
        buf.write("\2\u016b\u016e\5h\65\2\u016c\u016e\5j\66\2\u016d\u016b")
        buf.write("\3\2\2\2\u016d\u016c\3\2\2\2\u016e\u0175\3\2\2\2\u016f")
        buf.write("\u0170\t\2\2\2\u0170\u0171\7;\2\2\u0171\u0172\5@!\2\u0172")
        buf.write("\u0173\5&\24\2\u0173\u0175\3\2\2\2\u0174\u0168\3\2\2\2")
        buf.write("\u0174\u016f\3\2\2\2\u0175?\3\2\2\2\u0176\u0179\7\61\2")
        buf.write("\2\u0177\u017a\5h\65\2\u0178\u017a\5j\66\2\u0179\u0177")
        buf.write("\3\2\2\2\u0179\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("\u017c\7\31\2\2\u017c\u0184\3\2\2\2\u017d\u017e\7\60\2")
        buf.write("\2\u017e\u017f\7;\2\2\u017f\u0180\5@!\2\u0180\u0181\5")
        buf.write("&\24\2\u0181\u0182\7\60\2\2\u0182\u0184\3\2\2\2\u0183")
        buf.write("\u0176\3\2\2\2\u0183\u017d\3\2\2\2\u0184A\3\2\2\2\u0185")
        buf.write("\u0191\3\2\2\2\u0186\u0187\5X-\2\u0187\u0188\7.\2\2\u0188")
        buf.write("\u0189\7;\2\2\u0189\u0191\3\2\2\2\u018a\u018b\5X-\2\u018b")
        buf.write("\u018c\7\62\2\2\u018c\u018d\7<\2\2\u018d\u0191\3\2\2\2")
        buf.write("\u018e\u0191\5f\64\2\u018f\u0191\5 \21\2\u0190\u0185\3")
        buf.write("\2\2\2\u0190\u0186\3\2\2\2\u0190\u018a\3\2\2\2\u0190\u018e")
        buf.write("\3\2\2\2\u0190\u018f\3\2\2\2\u0191C\3\2\2\2\u0192\u0193")
        buf.write("\5B\"\2\u0193\u0194\7\31\2\2\u0194\u0195\5&\24\2\u0195")
        buf.write("\u0196\7\63\2\2\u0196E\3\2\2\2\u0197\u019b\5H%\2\u0198")
        buf.write("\u019a\5J&\2\u0199\u0198\3\2\2\2\u019a\u019d\3\2\2\2\u019b")
        buf.write("\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019f\3\2\2\2")
        buf.write("\u019d\u019b\3\2\2\2\u019e\u01a0\5L\'\2\u019f\u019e\3")
        buf.write("\2\2\2\u019f\u01a0\3\2\2\2\u01a0G\3\2\2\2\u01a1\u01a2")
        buf.write("\7\6\2\2\u01a2\u01a3\7*\2\2\u01a3\u01a4\5&\24\2\u01a4")
        buf.write("\u01a5\7+\2\2\u01a5\u01a6\5\\/\2\u01a6I\3\2\2\2\u01a7")
        buf.write("\u01a8\7\7\2\2\u01a8\u01a9\7*\2\2\u01a9\u01aa\5&\24\2")
        buf.write("\u01aa\u01ab\7+\2\2\u01ab\u01ac\5\\/\2\u01acK\3\2\2\2")
        buf.write("\u01ad\u01ae\7\b\2\2\u01ae\u01af\5\\/\2\u01afM\3\2\2\2")
        buf.write("\u01b0\u01b1\7\t\2\2\u01b1\u01b2\7*\2\2\u01b2\u01b3\5")
        buf.write("P)\2\u01b3\u01b4\7+\2\2\u01b4\u01b5\5\\/\2\u01b5O\3\2")
        buf.write("\2\2\u01b6\u01b7\5X-\2\u01b7\u01b8\7\13\2\2\u01b8\u01b9")
        buf.write("\5&\24\2\u01b9\u01ba\7/\2\2\u01ba\u01bd\5&\24\2\u01bb")
        buf.write("\u01bc\7\30\2\2\u01bc\u01be\5&\24\2\u01bd\u01bb\3\2\2")
        buf.write("\2\u01bd\u01be\3\2\2\2\u01beQ\3\2\2\2\u01bf\u01c0\7\4")
        buf.write("\2\2\u01c0\u01c1\7\63\2\2\u01c1S\3\2\2\2\u01c2\u01c3\7")
        buf.write("\5\2\2\u01c3\u01c4\7\63\2\2\u01c4U\3\2\2\2\u01c5\u01c7")
        buf.write("\7\20\2\2\u01c6\u01c8\5&\24\2\u01c7\u01c6\3\2\2\2\u01c7")
        buf.write("\u01c8\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\7\63\2")
        buf.write("\2\u01caW\3\2\2\2\u01cb\u01cc\b-\1\2\u01cc\u01cd\5:\36")
        buf.write("\2\u01cd\u01e4\3\2\2\2\u01ce\u01cf\f\5\2\2\u01cf\u01d0")
        buf.write("\7.\2\2\u01d0\u01d6\7;\2\2\u01d1\u01d3\7*\2\2\u01d2\u01d4")
        buf.write("\5\36\20\2\u01d3\u01d2\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d7\7+\2\2\u01d6\u01d1\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d7\u01e3\3\2\2\2\u01d8\u01d9\f")
        buf.write("\4\2\2\u01d9\u01da\7\62\2\2\u01da\u01e0\7<\2\2\u01db\u01dd")
        buf.write("\7*\2\2\u01dc\u01de\5\36\20\2\u01dd\u01dc\3\2\2\2\u01dd")
        buf.write("\u01de\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e1\7+\2\2")
        buf.write("\u01e0\u01db\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e3\3")
        buf.write("\2\2\2\u01e2\u01ce\3\2\2\2\u01e2\u01d8\3\2\2\2\u01e3\u01e6")
        buf.write("\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5")
        buf.write("Y\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01ec\5X-\2\u01e8")
        buf.write("\u01e9\7.\2\2\u01e9\u01ed\7;\2\2\u01ea\u01eb\7\62\2\2")
        buf.write("\u01eb\u01ed\7<\2\2\u01ec\u01e8\3\2\2\2\u01ec\u01ea\3")
        buf.write("\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f0\7*\2\2\u01ef\u01f1")
        buf.write("\5\36\20\2\u01f0\u01ef\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1")
        buf.write("\u01f2\3\2\2\2\u01f2\u01f3\7+\2\2\u01f3\u01f4\7\63\2\2")
        buf.write("\u01f4[\3\2\2\2\u01f5\u01f9\7\64\2\2\u01f6\u01f8\5^\60")
        buf.write("\2\u01f7\u01f6\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7")
        buf.write("\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fc\3\2\2\2\u01fb")
        buf.write("\u01f9\3\2\2\2\u01fc\u01fd\7\65\2\2\u01fd]\3\2\2\2\u01fe")
        buf.write("\u0208\5> \2\u01ff\u0208\5D#\2\u0200\u0208\5F$\2\u0201")
        buf.write("\u0208\5N(\2\u0202\u0208\5R*\2\u0203\u0208\5T+\2\u0204")
        buf.write("\u0208\5V,\2\u0205\u0208\5Z.\2\u0206\u0208\5\\/\2\u0207")
        buf.write("\u01fe\3\2\2\2\u0207\u01ff\3\2\2\2\u0207\u0200\3\2\2\2")
        buf.write("\u0207\u0201\3\2\2\2\u0207\u0202\3\2\2\2\u0207\u0203\3")
        buf.write("\2\2\2\u0207\u0204\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0206")
        buf.write("\3\2\2\2\u0208_\3\2\2\2\u0209\u0211\7\67\2\2\u020a\u0211")
        buf.write("\7\66\2\2\u020b\u0211\78\2\2\u020c\u0211\79\2\2\u020d")
        buf.write("\u0211\7:\2\2\u020e\u0211\5b\62\2\u020f\u0211\5d\63\2")
        buf.write("\u0210\u0209\3\2\2\2\u0210\u020a\3\2\2\2\u0210\u020b\3")
        buf.write("\2\2\2\u0210\u020c\3\2\2\2\u0210\u020d\3\2\2\2\u0210\u020e")
        buf.write("\3\2\2\2\u0210\u020f\3\2\2\2\u0211a\3\2\2\2\u0212\u0213")
        buf.write("\7\n\2\2\u0213\u023d\7*\2\2\u0214\u0219\7\67\2\2\u0215")
        buf.write("\u0216\7\60\2\2\u0216\u0218\7\67\2\2\u0217\u0215\3\2\2")
        buf.write("\2\u0218\u021b\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u021a")
        buf.write("\3\2\2\2\u021a\u023e\3\2\2\2\u021b\u0219\3\2\2\2\u021c")
        buf.write("\u0221\78\2\2\u021d\u021e\7\60\2\2\u021e\u0220\78\2\2")
        buf.write("\u021f\u021d\3\2\2\2\u0220\u0223\3\2\2\2\u0221\u021f\3")
        buf.write("\2\2\2\u0221\u0222\3\2\2\2\u0222\u023e\3\2\2\2\u0223\u0221")
        buf.write("\3\2\2\2\u0224\u0229\79\2\2\u0225\u0226\7\60\2\2\u0226")
        buf.write("\u0228\79\2\2\u0227\u0225\3\2\2\2\u0228\u022b\3\2\2\2")
        buf.write("\u0229\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u023e\3")
        buf.write("\2\2\2\u022b\u0229\3\2\2\2\u022c\u0231\7:\2\2\u022d\u022e")
        buf.write("\7\60\2\2\u022e\u0230\7:\2\2\u022f\u022d\3\2\2\2\u0230")
        buf.write("\u0233\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0232\3\2\2\2")
        buf.write("\u0232\u023e\3\2\2\2\u0233\u0231\3\2\2\2\u0234\u0239\5")
        buf.write("b\62\2\u0235\u0236\7\60\2\2\u0236\u0238\5b\62\2\u0237")
        buf.write("\u0235\3\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237\3\2\2\2")
        buf.write("\u0239\u023a\3\2\2\2\u023a\u023e\3\2\2\2\u023b\u0239\3")
        buf.write("\2\2\2\u023c\u023e\3\2\2\2\u023d\u0214\3\2\2\2\u023d\u021c")
        buf.write("\3\2\2\2\u023d\u0224\3\2\2\2\u023d\u022c\3\2\2\2\u023d")
        buf.write("\u0234\3\2\2\2\u023d\u023c\3\2\2\2\u023e\u023f\3\2\2\2")
        buf.write("\u023f\u0240\7+\2\2\u0240c\3\2\2\2\u0241\u0242\7\n\2\2")
        buf.write("\u0242\u024b\7*\2\2\u0243\u0248\5b\62\2\u0244\u0245\7")
        buf.write("\60\2\2\u0245\u0247\5b\62\2\u0246\u0244\3\2\2\2\u0247")
        buf.write("\u024a\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249\3\2\2\2")
        buf.write("\u0249\u024c\3\2\2\2\u024a\u0248\3\2\2\2\u024b\u0243\3")
        buf.write("\2\2\2\u024b\u024c\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u024e")
        buf.write("\7+\2\2\u024ee\3\2\2\2\u024f\u0250\t\3\2\2\u0250g\3\2")
        buf.write("\2\2\u0251\u0252\t\t\2\2\u0252i\3\2\2\2\u0253\u0254\7")
        buf.write("\n\2\2\u0254\u0257\7,\2\2\u0255\u0258\5h\65\2\u0256\u0258")
        buf.write("\5j\66\2\u0257\u0255\3\2\2\2\u0257\u0256\3\2\2\2\u0258")
        buf.write("\u0259\3\2\2\2\u0259\u025a\7\60\2\2\u025a\u025b\7\66\2")
        buf.write("\2\u025b\u025c\7-\2\2\u025ck\3\2\2\2Dov|\u0083\u008b\u0092")
        buf.write("\u0097\u00a7\u00a9\u00b2\u00ba\u00c4\u00c6\u00ce\u00d0")
        buf.write("\u00d8\u00da\u00e2\u00e4\u00ef\u00f9\u0100\u010a\u0115")
        buf.write("\u0120\u0126\u012b\u0134\u013f\u0142\u0146\u014e\u0151")
        buf.write("\u0154\u015a\u015e\u0166\u016d\u0174\u0179\u0183\u0190")
        buf.write("\u019b\u019f\u01bd\u01c7\u01d3\u01d6\u01dd\u01e0\u01e2")
        buf.write("\u01e4\u01ec\u01f0\u01f9\u0207\u0210\u0219\u0221\u0229")
        buf.write("\u0231\u0239\u023d\u0248\u024b\u0257")
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
    RULE_type_name = 9
    RULE_attribute_declaration = 10
    RULE_identifier_list = 11
    RULE_dolar_identifier_list = 12
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
    RULE_var_dcl_list = 31
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
    RULE_identifier = 50
    RULE_primitive_type = 51
    RULE_array_type = 52

    ruleNames =  [ "program", "class_declaration", "class_body_unit", "super_class_group", 
                   "method_declaration", "constructor", "destructor", "parameter_list", 
                   "parameter", "type_name", "attribute_declaration", "identifier_list", 
                   "dolar_identifier_list", "mixed_identifier_list", "expression_list", 
                   "element_expression", "index_operator", "relational_operator", 
                   "expression", "relational_expr", "and_or_expr", "add_sub_expr", 
                   "mul_add_mol_expr", "not_expr", "sign_expr", "index_operator_expr", 
                   "instance_access", "static_access", "object_creation", 
                   "atom_expr", "var_val_statement", "var_dcl_list", "lhs", 
                   "assign_statement", "if_statement", "if_part", "else_if_part", 
                   "else_part", "for_in_statement", "loop_part", "break_statement", 
                   "continue_statement", "return_statement", "member_access", 
                   "method_invocation_statement", "block_statement", "statement", 
                   "literal", "indexed_array", "multi_dimentional_array", 
                   "identifier", "primitive_type", "array_type" ]

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
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.class_declaration()
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.K_CLASS):
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
            self.state = 113
            self.match(D96Parser.K_CLASS)
            self.state = 114
            self.match(D96Parser.IDENTIFIER)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 115
                self.super_class_group()


            self.state = 118
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
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
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_VAL, D96Parser.K_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.attribute_declaration()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR, D96Parser.K_DESTRUCTOR, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
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
        self.enterRule(localctx, 8, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.identifier()
                self.state = 135
                self.match(D96Parser.LEFT_PAREN)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 136
                    self.parameter_list()


                self.state = 139
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 140
                self.block_statement()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.constructor()
                pass
            elif token in [D96Parser.K_DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
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
            self.state = 146
            self.match(D96Parser.K_CONSTRUCTOR)
            self.state = 147
            self.match(D96Parser.LEFT_PAREN)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDENTIFIER:
                self.state = 148
                self.parameter_list()


            self.state = 151
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 152
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
            self.state = 154
            self.match(D96Parser.K_DESTRUCTOR)
            self.state = 155
            self.match(D96Parser.LEFT_PAREN)
            self.state = 156
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 157
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
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.parameter()
                self.state = 163 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 161
                    self.match(D96Parser.SEMI_COLON)
                    self.state = 162
                    self.parameter()
                    self.state = 165 
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

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


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
            self.state = 169
            self.identifier_list()
            self.state = 170
            self.match(D96Parser.COLON)
            self.state = 171
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_name" ):
                listener.enterType_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_name" ):
                listener.exitType_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = D96Parser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_name)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_INT, D96Parser.K_FLOAT, D96Parser.K_BOOLEAN, D96Parser.K_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.primitive_type()
                pass
            elif token in [D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.identifier()
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 175
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

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

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
        self.enterRule(localctx, 20, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 179
            self.mixed_identifier_list()
            self.state = 180
            self.match(D96Parser.COLON)
            self.state = 181
            self.type_name()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 182
                self.match(D96Parser.OP_ASSIGN)
                self.state = 183
                self.expression_list()


            self.state = 186
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
        self.enterRule(localctx, 22, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(D96Parser.IDENTIFIER)
                self.state = 192 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 190
                    self.match(D96Parser.COMMA)
                    self.state = 191
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 194 
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
        self.enterRule(localctx, 24, self.RULE_dolar_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 202 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 200
                    self.match(D96Parser.COMMA)
                    self.state = 201
                    self.match(D96Parser.DOLAR_IDENTIFIER)
                    self.state = 204 
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
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                _la = self._input.LA(1)
                if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                _la = self._input.LA(1)
                if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 212 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 210
                    self.match(D96Parser.COMMA)
                    self.state = 211
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 214 
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
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.expression()
                self.state = 222 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 220
                    self.match(D96Parser.COMMA)
                    self.state = 221
                    self.expression()
                    self.state = 224 
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
            self.state = 228
            self.expression()
            self.state = 229
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
            self.state = 231
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 232
            self.expression()
            self.state = 233
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 234
                    self.index_operator() 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.state = 240
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
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.relational_expr()
                self.state = 243
                _la = self._input.LA(1)
                if not(_la==D96Parser.OP_STRING_CONCATENATION or _la==D96Parser.OP_TWO_SAME_STRING):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 244
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
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
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.and_or_expr(0)
                self.state = 250
                self.relational_operator()
                self.state = 251
                self.and_or_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
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
            self.state = 257
            self.add_sub_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 264
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.And_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_or_expr)
                    self.state = 259
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 260
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_LOGICAL_OR or _la==D96Parser.OP_LOGICAL_AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 261
                    self.add_sub_expr(0) 
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 268
            self.mul_add_mol_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Add_sub_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expr)
                    self.state = 270
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 271
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_ADDTION or _la==D96Parser.OP_SUBTRACTION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 272
                    self.mul_add_mol_expr(0) 
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
            self.state = 279
            self.not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Mul_add_mol_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_add_mol_expr)
                    self.state = 281
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 282
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MODULO) | (1 << D96Parser.OP_MULTIPLICATION) | (1 << D96Parser.OP_DIVISION))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 283
                    self.not_expr() 
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(D96Parser.OP_LOGICAL_NOT)
                self.state = 290
                self.not_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NEW, D96Parser.OP_SUBTRACTION, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
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
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUBTRACTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(D96Parser.OP_SUBTRACTION)
                self.state = 295
                self.sign_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NEW, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
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
            self.state = 300
            self.instance_access(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 306
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operator_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operator_expr)
                    self.state = 302
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 303
                    self.index_operator() 
                self.state = 308
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


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
            self.state = 310
            self.static_access()
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Instance_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_access)
                    self.state = 312
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 313
                    self.match(D96Parser.DOT)
                    self.state = 314
                    self.identifier()
                    self.state = 320
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        self.state = 315
                        self.match(D96Parser.LEFT_PAREN)
                        self.state = 317
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                            self.state = 316
                            self.expression_list()


                        self.state = 319
                        self.match(D96Parser.RIGHT_PAREN)

             
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(D96Parser.IDENTIFIER)
                self.state = 328
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 329
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 335
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 330
                    self.match(D96Parser.LEFT_PAREN)
                    self.state = 332
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                        self.state = 331
                        self.expression_list()


                    self.state = 334
                    self.match(D96Parser.RIGHT_PAREN)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
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
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(D96Parser.K_NEW)
                self.state = 341
                self.match(D96Parser.IDENTIFIER)
                self.state = 342
                self.match(D96Parser.LEFT_PAREN)
                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                    self.state = 343
                    self.expression_list()


                self.state = 346
                self.match(D96Parser.RIGHT_PAREN)
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
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


        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


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
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_ARRAY, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.literal()
                pass
            elif token in [D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.identifier()
                pass
            elif token in [D96Parser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.match(D96Parser.LEFT_PAREN)
                self.state = 353
                self.expression()
                self.state = 354
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

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def var_dcl_list(self):
            return self.getTypedRuleContext(D96Parser.Var_dcl_listContext,0)


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
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                _la = self._input.LA(1)
                if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 359
                self.identifier_list()
                self.state = 360
                self.match(D96Parser.COLON)
                self.state = 363
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.K_INT, D96Parser.K_FLOAT, D96Parser.K_BOOLEAN, D96Parser.K_STRING]:
                    self.state = 361
                    self.primitive_type()
                    pass
                elif token in [D96Parser.K_ARRAY]:
                    self.state = 362
                    self.array_type()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                _la = self._input.LA(1)
                if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 366
                self.match(D96Parser.IDENTIFIER)
                self.state = 367
                self.var_dcl_list()
                self.state = 368
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dcl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def var_dcl_list(self):
            return self.getTypedRuleContext(D96Parser.Var_dcl_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_dcl_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_dcl_list" ):
                listener.enterVar_dcl_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_dcl_list" ):
                listener.exitVar_dcl_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dcl_list" ):
                return visitor.visitVar_dcl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_dcl_list(self):

        localctx = D96Parser.Var_dcl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_var_dcl_list)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(D96Parser.COLON)
                self.state = 375
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.K_INT, D96Parser.K_FLOAT, D96Parser.K_BOOLEAN, D96Parser.K_STRING]:
                    self.state = 373
                    self.primitive_type()
                    pass
                elif token in [D96Parser.K_ARRAY]:
                    self.state = 374
                    self.array_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 377
                self.match(D96Parser.OP_ASSIGN)
                pass
            elif token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.match(D96Parser.COMMA)
                self.state = 380
                self.match(D96Parser.IDENTIFIER)
                self.state = 381
                self.var_dcl_list()
                self.state = 382
                self.expression()
                self.state = 383
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

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


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
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.member_access(0)
                self.state = 389
                self.match(D96Parser.DOT)
                self.state = 390
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 392
                self.member_access(0)
                self.state = 393
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 394
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 396
                self.identifier()
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
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

        def object_creation(self):
            return self.getTypedRuleContext(D96Parser.Object_creationContext,0)


        def member_access(self):
            return self.getTypedRuleContext(D96Parser.Member_accessContext,0)


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


        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

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
            self.state = 458
            self.object_creation()
            self._ctx.stop = self._input.LT(-1)
            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 480
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Member_accessContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access)
                        self.state = 460
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 461
                        self.match(D96Parser.DOT)
                        self.state = 462
                        self.match(D96Parser.IDENTIFIER)
                        self.state = 468
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                        if la_ == 1:
                            self.state = 463
                            self.match(D96Parser.LEFT_PAREN)
                            self.state = 465
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                                self.state = 464
                                self.expression_list()


                            self.state = 467
                            self.match(D96Parser.RIGHT_PAREN)


                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Member_accessContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access)
                        self.state = 470
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 471
                        self.match(D96Parser.DOUBLE_COLON)
                        self.state = 472
                        self.match(D96Parser.DOLAR_IDENTIFIER)
                        self.state = 478
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                        if la_ == 1:
                            self.state = 473
                            self.match(D96Parser.LEFT_PAREN)
                            self.state = 475
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                                self.state = 474
                                self.expression_list()


                            self.state = 477
                            self.match(D96Parser.RIGHT_PAREN)


                        pass

             
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

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
            self.state = 485
            self.member_access(0)
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOT]:
                self.state = 486
                self.match(D96Parser.DOT)
                self.state = 487
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.DOUBLE_COLON]:
                self.state = 488
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 489
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 492
            self.match(D96Parser.LEFT_PAREN)
            self.state = 494
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 493
                self.expression_list()


            self.state = 496
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 497
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
            self.state = 499
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_BREAK) | (1 << D96Parser.K_CONTINUE) | (1 << D96Parser.K_IF) | (1 << D96Parser.K_FOR_EACH) | (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_RETURN) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_ASSIGN) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.LEFT_CURLY_BRACKET) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 500
                self.statement()
                self.state = 505
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 506
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
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.var_val_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 510
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 511
                self.for_in_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 512
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 513
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 514
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 515
                self.method_invocation_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 516
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
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.match(D96Parser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.match(D96Parser.INTEGER_LITERAL2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 521
                self.match(D96Parser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 522
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 523
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 524
                self.indexed_array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 525
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
            self.state = 528
            self.match(D96Parser.K_ARRAY)
            self.state = 529
            self.match(D96Parser.LEFT_PAREN)
            self.state = 571
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL]:
                self.state = 530
                self.match(D96Parser.INTEGER_LITERAL)
                self.state = 535
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 531
                    self.match(D96Parser.COMMA)
                    self.state = 532
                    self.match(D96Parser.INTEGER_LITERAL)
                    self.state = 537
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.state = 538
                self.match(D96Parser.FLOAT_LITERAL)
                self.state = 543
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 539
                    self.match(D96Parser.COMMA)
                    self.state = 540
                    self.match(D96Parser.FLOAT_LITERAL)
                    self.state = 545
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.state = 546
                self.match(D96Parser.BOOLEAN_LITERAL)
                self.state = 551
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 547
                    self.match(D96Parser.COMMA)
                    self.state = 548
                    self.match(D96Parser.BOOLEAN_LITERAL)
                    self.state = 553
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.state = 554
                self.match(D96Parser.STRING_LITERAL)
                self.state = 559
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 555
                    self.match(D96Parser.COMMA)
                    self.state = 556
                    self.match(D96Parser.STRING_LITERAL)
                    self.state = 561
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 562
                self.indexed_array()
                self.state = 567
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 563
                    self.match(D96Parser.COMMA)
                    self.state = 564
                    self.indexed_array()
                    self.state = 569
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.RIGHT_PAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 573
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
            self.state = 575
            self.match(D96Parser.K_ARRAY)
            self.state = 576
            self.match(D96Parser.LEFT_PAREN)

            self.state = 585
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ARRAY:
                self.state = 577
                self.indexed_array()
                self.state = 582
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 578
                    self.match(D96Parser.COMMA)
                    self.state = 579
                    self.indexed_array()
                    self.state = 584
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 587
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
        self.enterRule(localctx, 100, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
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
        self.enterRule(localctx, 102, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
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
        self.enterRule(localctx, 104, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.match(D96Parser.K_ARRAY)
            self.state = 594
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 597
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_INT, D96Parser.K_FLOAT, D96Parser.K_BOOLEAN, D96Parser.K_STRING]:
                self.state = 595
                self.primitive_type()
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 596
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 599
            self.match(D96Parser.COMMA)
            self.state = 600
            self.match(D96Parser.INTEGER_LITERAL2)
            self.state = 601
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
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




