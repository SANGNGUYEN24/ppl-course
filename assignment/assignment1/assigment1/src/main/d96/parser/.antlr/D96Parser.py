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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u026f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u0083")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\3\7\3\u008a\n\3\f\3\16\3\u008d")
        buf.write("\13\3\5\3\u008f\n\3\3\3\3\3\3\3\7\3\u0094\n\3\f\3\16\3")
        buf.write("\u0097\13\3\3\3\3\3\3\3\7\3\u009c\n\3\f\3\16\3\u009f\13")
        buf.write("\3\3\3\3\3\3\3\7\3\u00a4\n\3\f\3\16\3\u00a7\13\3\5\3\u00a9")
        buf.write("\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\7\4\u00b2\n\4\f\4\16")
        buf.write("\4\u00b5\13\4\5\4\u00b7\n\4\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\n\6\n\u00cf\n\n\r\n\16\n\u00d0\3\n\7\n\u00d4\n")
        buf.write("\n\f\n\16\n\u00d7\13\n\3\n\3\n\3\n\7\n\u00dc\n\n\f\n\16")
        buf.write("\n\u00df\13\n\3\n\5\n\u00e2\n\n\3\13\3\13\3\13\5\13\u00e7")
        buf.write("\n\13\3\13\3\13\3\13\3\13\3\f\7\f\u00ee\n\f\f\f\16\f\u00f1")
        buf.write("\13\f\3\r\3\r\3\r\5\r\u00f6\n\r\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u0107\n\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3")
        buf.write("\22\5\22\u0111\n\22\3\22\3\22\3\22\3\22\5\22\u0117\n\22")
        buf.write("\3\23\3\23\3\23\5\23\u011c\n\23\3\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\5\25\u012a\n\25")
        buf.write("\3\26\3\26\3\26\3\26\7\26\u0130\n\26\f\26\16\26\u0133")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\5\30\u013c\n")
        buf.write("\30\3\30\3\30\3\30\5\30\u0141\n\30\3\30\3\30\5\30\u0145")
        buf.write("\n\30\3\30\3\30\3\31\3\31\3\31\5\31\u014c\n\31\3\32\3")
        buf.write("\32\3\32\5\32\u0151\n\32\3\33\3\33\7\33\u0155\n\33\f\33")
        buf.write("\16\33\u0158\13\33\3\34\3\34\7\34\u015c\n\34\f\34\16\34")
        buf.write("\u015f\13\34\3\35\3\35\3\35\3\35\5\35\u0165\n\35\3\36")
        buf.write("\3\36\3\36\3\36\7\36\u016b\n\36\f\36\16\36\u016e\13\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \7 \u0177\n \f \16 \u017a\13")
        buf.write(" \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$")
        buf.write("\3$\3$\3$\3$\3$\3%\3%\3%\3%\5%\u0195\n%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\5%\u01a2\n%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\7%\u01b2\n%\f%\16%\u01b5\13%\3&\3")
        buf.write("&\3&\7&\u01ba\n&\f&\16&\u01bd\13&\3\'\3\'\3(\3(\3(\3(")
        buf.write("\3(\3(\3(\7(\u01c8\n(\f(\16(\u01cb\13(\3)\3)\3)\3)\3)")
        buf.write("\3)\7)\u01d3\n)\f)\16)\u01d6\13)\3*\3*\3*\3*\3*\3*\7*")
        buf.write("\u01de\n*\f*\16*\u01e1\13*\3+\3+\3+\3+\3+\3+\7+\u01e9")
        buf.write("\n+\f+\16+\u01ec\13+\3,\3,\3,\5,\u01f1\n,\3-\3-\3-\5-")
        buf.write("\u01f6\n-\3.\3.\3.\3.\3.\7.\u01fd\n.\f.\16.\u0200\13.")
        buf.write("\3/\3/\3/\3/\3/\3/\3/\5/\u0209\n/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\61\5\61\u0215\n\61\3\61\3")
        buf.write("\61\5\61\u0219\n\61\3\61\3\61\3\62\3\62\5\62\u021f\n\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u0235")
        buf.write("\n\65\f\65\16\65\u0238\13\65\3\66\3\66\5\66\u023c\n\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\5")
        buf.write("8\u024b\n8\39\39\39\3:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3=\3=\5=\u0260\n=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\3>\5>\u026d\n>\3>\2\bHNPRTZ?\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnprtvxz\2\t\3\2>?\4\2\13\13\r\20\3\2\24\25")
        buf.write("\3\2#$\4\2 !\'*\3\2\36\37\4\2\"\"%&\2\u027f\2\u0082\3")
        buf.write("\2\2\2\4\u0084\3\2\2\2\6\u00ac\3\2\2\2\b\u00ba\3\2\2\2")
        buf.write("\n\u00bc\3\2\2\2\f\u00be\3\2\2\2\16\u00c5\3\2\2\2\20\u00ca")
        buf.write("\3\2\2\2\22\u00e1\3\2\2\2\24\u00e3\3\2\2\2\26\u00ef\3")
        buf.write("\2\2\2\30\u00f5\3\2\2\2\32\u00f7\3\2\2\2\34\u00fa\3\2")
        buf.write("\2\2\36\u0106\3\2\2\2 \u0108\3\2\2\2\"\u0116\3\2\2\2$")
        buf.write("\u0118\3\2\2\2&\u0120\3\2\2\2(\u0129\3\2\2\2*\u0131\3")
        buf.write("\2\2\2,\u0134\3\2\2\2.\u0138\3\2\2\2\60\u014b\3\2\2\2")
        buf.write("\62\u0150\3\2\2\2\64\u0156\3\2\2\2\66\u015d\3\2\2\28\u0164")
        buf.write("\3\2\2\2:\u016c\3\2\2\2<\u016f\3\2\2\2>\u0172\3\2\2\2")
        buf.write("@\u017b\3\2\2\2B\u017f\3\2\2\2D\u0183\3\2\2\2F\u018a\3")
        buf.write("\2\2\2H\u01a1\3\2\2\2J\u01b6\3\2\2\2L\u01be\3\2\2\2N\u01c0")
        buf.write("\3\2\2\2P\u01cc\3\2\2\2R\u01d7\3\2\2\2T\u01e2\3\2\2\2")
        buf.write("V\u01f0\3\2\2\2X\u01f5\3\2\2\2Z\u01f7\3\2\2\2\\\u0208")
        buf.write("\3\2\2\2^\u020a\3\2\2\2`\u020f\3\2\2\2b\u021e\3\2\2\2")
        buf.write("d\u0223\3\2\2\2f\u0227\3\2\2\2h\u022d\3\2\2\2j\u023b\3")
        buf.write("\2\2\2l\u023d\3\2\2\2n\u0243\3\2\2\2p\u024c\3\2\2\2r\u024f")
        buf.write("\3\2\2\2t\u0252\3\2\2\2v\u0256\3\2\2\2x\u025d\3\2\2\2")
        buf.write("z\u026c\3\2\2\2|\u0083\7:\2\2}\u0083\7;\2\2~\u0083\7<")
        buf.write("\2\2\177\u0083\7=\2\2\u0080\u0083\5\4\3\2\u0081\u0083")
        buf.write("\5\6\4\2\u0082|\3\2\2\2\u0082}\3\2\2\2\u0082~\3\2\2\2")
        buf.write("\u0082\177\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2")
        buf.write("\2\2\u0083\3\3\2\2\2\u0084\u0085\7\13\2\2\u0085\u00a8")
        buf.write("\7-\2\2\u0086\u008b\7:\2\2\u0087\u0088\7\63\2\2\u0088")
        buf.write("\u008a\7:\2\2\u0089\u0087\3\2\2\2\u008a\u008d\3\2\2\2")
        buf.write("\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008f\3")
        buf.write("\2\2\2\u008d\u008b\3\2\2\2\u008e\u0086\3\2\2\2\u008e\u008f")
        buf.write("\3\2\2\2\u008f\u00a9\3\2\2\2\u0090\u0095\7;\2\2\u0091")
        buf.write("\u0092\7\63\2\2\u0092\u0094\7;\2\2\u0093\u0091\3\2\2\2")
        buf.write("\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3")
        buf.write("\2\2\2\u0096\u00a9\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u009d")
        buf.write("\7<\2\2\u0099\u009a\7\63\2\2\u009a\u009c\7<\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e\u00a9\3\2\2\2\u009f\u009d\3")
        buf.write("\2\2\2\u00a0\u00a5\7=\2\2\u00a1\u00a2\7\63\2\2\u00a2\u00a4")
        buf.write("\7=\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a9\3\2\2\2")
        buf.write("\u00a7\u00a5\3\2\2\2\u00a8\u008e\3\2\2\2\u00a8\u0090\3")
        buf.write("\2\2\2\u00a8\u0098\3\2\2\2\u00a8\u00a0\3\2\2\2\u00a9\u00aa")
        buf.write("\3\2\2\2\u00aa\u00ab\7.\2\2\u00ab\5\3\2\2\2\u00ac\u00ad")
        buf.write("\7\13\2\2\u00ad\u00b6\7-\2\2\u00ae\u00b3\5\4\3\2\u00af")
        buf.write("\u00b0\7\63\2\2\u00b0\u00b2\5\4\3\2\u00b1\u00af\3\2\2")
        buf.write("\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4")
        buf.write("\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6")
        buf.write("\u00ae\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2")
        buf.write("\u00b8\u00b9\7.\2\2\u00b9\7\3\2\2\2\u00ba\u00bb\t\2\2")
        buf.write("\2\u00bb\t\3\2\2\2\u00bc\u00bd\t\3\2\2\u00bd\13\3\2\2")
        buf.write("\2\u00be\u00bf\7\13\2\2\u00bf\u00c0\7/\2\2\u00c0\u00c1")
        buf.write("\5\n\6\2\u00c1\u00c2\7\63\2\2\u00c2\u00c3\7:\2\2\u00c3")
        buf.write("\u00c4\7\60\2\2\u00c4\r\3\2\2\2\u00c5\u00c6\7\30\2\2\u00c6")
        buf.write("\u00c7\7>\2\2\u00c7\u00c8\7-\2\2\u00c8\u00c9\7.\2\2\u00c9")
        buf.write("\17\3\2\2\2\u00ca\u00cb\5\22\n\2\u00cb\u00cc\7\2\2\3\u00cc")
        buf.write("\21\3\2\2\2\u00cd\u00cf\5\24\13\2\u00ce\u00cd\3\2\2\2")
        buf.write("\u00cf\u00d0\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3")
        buf.write("\2\2\2\u00d1\u00e2\3\2\2\2\u00d2\u00d4\5\24\13\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2")
        buf.write("\u00d5\u00d6\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00d5\3")
        buf.write("\2\2\2\u00d8\u00e2\5\34\17\2\u00d9\u00dd\5\34\17\2\u00da")
        buf.write("\u00dc\5\24\13\2\u00db\u00da\3\2\2\2\u00dc\u00df\3\2\2")
        buf.write("\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e2")
        buf.write("\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e2\5\34\17\2\u00e1")
        buf.write("\u00ce\3\2\2\2\u00e1\u00d5\3\2\2\2\u00e1\u00d9\3\2\2\2")
        buf.write("\u00e1\u00e0\3\2\2\2\u00e2\23\3\2\2\2\u00e3\u00e4\7\23")
        buf.write("\2\2\u00e4\u00e6\7>\2\2\u00e5\u00e7\5\32\16\2\u00e6\u00e5")
        buf.write("\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\u00e9\7\67\2\2\u00e9\u00ea\5\26\f\2\u00ea\u00eb\78\2")
        buf.write("\2\u00eb\25\3\2\2\2\u00ec\u00ee\5\30\r\2\u00ed\u00ec\3")
        buf.write("\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0")
        buf.write("\3\2\2\2\u00f0\27\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f6")
        buf.write("\5.\30\2\u00f3\u00f6\5\"\22\2\u00f4\u00f6\5z>\2\u00f5")
        buf.write("\u00f2\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4\3\2\2\2")
        buf.write("\u00f6\31\3\2\2\2\u00f7\u00f8\7\64\2\2\u00f8\u00f9\7>")
        buf.write("\2\2\u00f9\33\3\2\2\2\u00fa\u00fb\7\23\2\2\u00fb\u00fc")
        buf.write("\7\3\2\2\u00fc\u00fd\7\67\2\2\u00fd\u00fe\5\36\20\2\u00fe")
        buf.write("\u00ff\78\2\2\u00ff\35\3\2\2\2\u0100\u0101\5 \21\2\u0101")
        buf.write("\u0102\5\26\f\2\u0102\u0107\3\2\2\2\u0103\u0104\5\26\f")
        buf.write("\2\u0104\u0105\5 \21\2\u0105\u0107\3\2\2\2\u0106\u0100")
        buf.write("\3\2\2\2\u0106\u0103\3\2\2\2\u0107\37\3\2\2\2\u0108\u0109")
        buf.write("\7\32\2\2\u0109\u010a\7-\2\2\u010a\u010b\7.\2\2\u010b")
        buf.write("\u010c\5x=\2\u010c!\3\2\2\2\u010d\u010e\7>\2\2\u010e\u0110")
        buf.write("\7-\2\2\u010f\u0111\5(\25\2\u0110\u010f\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\7.\2\2")
        buf.write("\u0113\u0117\5x=\2\u0114\u0117\5$\23\2\u0115\u0117\5&")
        buf.write("\24\2\u0116\u010d\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0115")
        buf.write("\3\2\2\2\u0117#\3\2\2\2\u0118\u0119\7\26\2\2\u0119\u011b")
        buf.write("\7-\2\2\u011a\u011c\5(\25\2\u011b\u011a\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e\7.\2\2")
        buf.write("\u011e\u011f\5x=\2\u011f%\3\2\2\2\u0120\u0121\7\27\2\2")
        buf.write("\u0121\u0122\7-\2\2\u0122\u0123\7.\2\2\u0123\u0124\5x")
        buf.write("=\2\u0124\'\3\2\2\2\u0125\u012a\5,\27\2\u0126\u0127\5")
        buf.write(",\27\2\u0127\u0128\5*\26\2\u0128\u012a\3\2\2\2\u0129\u0125")
        buf.write("\3\2\2\2\u0129\u0126\3\2\2\2\u012a)\3\2\2\2\u012b\u012c")
        buf.write("\7\66\2\2\u012c\u012d\5,\27\2\u012d\u012e\5*\26\2\u012e")
        buf.write("\u0130\3\2\2\2\u012f\u012b\3\2\2\2\u0130\u0133\3\2\2\2")
        buf.write("\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132+\3\2\2")
        buf.write("\2\u0133\u0131\3\2\2\2\u0134\u0135\5\60\31\2\u0135\u0136")
        buf.write("\7\64\2\2\u0136\u0137\5\n\6\2\u0137-\3\2\2\2\u0138\u013b")
        buf.write("\t\4\2\2\u0139\u013c\5\60\31\2\u013a\u013c\5\62\32\2\u013b")
        buf.write("\u0139\3\2\2\2\u013b\u013a\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u0140\7\64\2\2\u013e\u0141\5\f\7\2\u013f\u0141")
        buf.write("\5\n\6\2\u0140\u013e\3\2\2\2\u0140\u013f\3\2\2\2\u0141")
        buf.write("\u0144\3\2\2\2\u0142\u0143\7\34\2\2\u0143\u0145\58\35")
        buf.write("\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\u0147\7\66\2\2\u0147/\3\2\2\2\u0148\u014c")
        buf.write("\7>\2\2\u0149\u014a\7>\2\2\u014a\u014c\5\64\33\2\u014b")
        buf.write("\u0148\3\2\2\2\u014b\u0149\3\2\2\2\u014c\61\3\2\2\2\u014d")
        buf.write("\u0151\7?\2\2\u014e\u014f\7?\2\2\u014f\u0151\5\66\34\2")
        buf.write("\u0150\u014d\3\2\2\2\u0150\u014e\3\2\2\2\u0151\63\3\2")
        buf.write("\2\2\u0152\u0153\7\63\2\2\u0153\u0155\7>\2\2\u0154\u0152")
        buf.write("\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157\65\3\2\2\2\u0158\u0156\3\2\2\2\u0159")
        buf.write("\u015a\7\63\2\2\u015a\u015c\7?\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3")
        buf.write("\2\2\2\u015e\67\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0165")
        buf.write("\5N(\2\u0161\u0162\5N(\2\u0162\u0163\5:\36\2\u0163\u0165")
        buf.write("\3\2\2\2\u0164\u0160\3\2\2\2\u0164\u0161\3\2\2\2\u0165")
        buf.write("9\3\2\2\2\u0166\u0167\7\63\2\2\u0167\u0168\5N(\2\u0168")
        buf.write("\u0169\5:\36\2\u0169\u016b\3\2\2\2\u016a\u0166\3\2\2\2")
        buf.write("\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3")
        buf.write("\2\2\2\u016d;\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0170")
        buf.write("\5N(\2\u0170\u0171\5> \2\u0171=\3\2\2\2\u0172\u0173\7")
        buf.write("/\2\2\u0173\u0174\5N(\2\u0174\u0178\7\60\2\2\u0175\u0177")
        buf.write("\5> \2\u0176\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179?\3\2\2\2\u017a\u0178")
        buf.write("\3\2\2\2\u017b\u017c\7>\2\2\u017c\u017d\7\61\2\2\u017d")
        buf.write("\u017e\7>\2\2\u017eA\3\2\2\2\u017f\u0180\7>\2\2\u0180")
        buf.write("\u0181\7\65\2\2\u0181\u0182\7>\2\2\u0182C\3\2\2\2\u0183")
        buf.write("\u0184\7>\2\2\u0184\u0185\7\65\2\2\u0185\u0186\7>\2\2")
        buf.write("\u0186\u0187\7-\2\2\u0187\u0188\58\35\2\u0188\u0189\7")
        buf.write(".\2\2\u0189E\3\2\2\2\u018a\u018b\7\30\2\2\u018b\u018c")
        buf.write("\7>\2\2\u018c\u018d\7-\2\2\u018d\u018e\58\35\2\u018e\u018f")
        buf.write("\7.\2\2\u018fG\3\2\2\2\u0190\u0191\b%\1\2\u0191\u0192")
        buf.write("\7>\2\2\u0192\u0194\7-\2\2\u0193\u0195\5J&\2\u0194\u0193")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u01a2\7.\2\2\u0197\u0198\7$\2\2\u0198\u01a2\5H%\n\u0199")
        buf.write("\u019a\7\35\2\2\u019a\u01a2\5H%\t\u019b\u01a2\7>\2\2\u019c")
        buf.write("\u01a2\7:\2\2\u019d\u019e\7-\2\2\u019e\u019f\5H%\2\u019f")
        buf.write("\u01a0\7.\2\2\u01a0\u01a2\3\2\2\2\u01a1\u0190\3\2\2\2")
        buf.write("\u01a1\u0197\3\2\2\2\u01a1\u0199\3\2\2\2\u01a1\u019b\3")
        buf.write("\2\2\2\u01a1\u019c\3\2\2\2\u01a1\u019d\3\2\2\2\u01a2\u01b3")
        buf.write("\3\2\2\2\u01a3\u01a4\f\b\2\2\u01a4\u01a5\7%\2\2\u01a5")
        buf.write("\u01b2\5H%\t\u01a6\u01a7\f\7\2\2\u01a7\u01a8\t\5\2\2\u01a8")
        buf.write("\u01b2\5H%\b\u01a9\u01aa\f\6\2\2\u01aa\u01ab\7 \2\2\u01ab")
        buf.write("\u01b2\5H%\7\u01ac\u01ad\f\13\2\2\u01ad\u01ae\7/\2\2\u01ae")
        buf.write("\u01af\5H%\2\u01af\u01b0\7\60\2\2\u01b0\u01b2\3\2\2\2")
        buf.write("\u01b1\u01a3\3\2\2\2\u01b1\u01a6\3\2\2\2\u01b1\u01a9\3")
        buf.write("\2\2\2\u01b1\u01ac\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4I\3\2\2\2\u01b5\u01b3")
        buf.write("\3\2\2\2\u01b6\u01bb\5H%\2\u01b7\u01b8\7\63\2\2\u01b8")
        buf.write("\u01ba\5H%\2\u01b9\u01b7\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bcK\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01be\u01bf\t\6\2\2\u01bfM\3\2\2\2\u01c0")
        buf.write("\u01c1\b(\1\2\u01c1\u01c2\5P)\2\u01c2\u01c9\3\2\2\2\u01c3")
        buf.write("\u01c4\f\4\2\2\u01c4\u01c5\5L\'\2\u01c5\u01c6\5N(\5\u01c6")
        buf.write("\u01c8\3\2\2\2\u01c7\u01c3\3\2\2\2\u01c8\u01cb\3\2\2\2")
        buf.write("\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01caO\3\2\2")
        buf.write("\2\u01cb\u01c9\3\2\2\2\u01cc\u01cd\b)\1\2\u01cd\u01ce")
        buf.write("\5R*\2\u01ce\u01d4\3\2\2\2\u01cf\u01d0\f\4\2\2\u01d0\u01d1")
        buf.write("\t\7\2\2\u01d1\u01d3\5R*\2\u01d2\u01cf\3\2\2\2\u01d3\u01d6")
        buf.write("\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5")
        buf.write("Q\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d8\b*\1\2\u01d8")
        buf.write("\u01d9\5T+\2\u01d9\u01df\3\2\2\2\u01da\u01db\f\4\2\2\u01db")
        buf.write("\u01dc\t\5\2\2\u01dc\u01de\5T+\2\u01dd\u01da\3\2\2\2\u01de")
        buf.write("\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2")
        buf.write("\u01e0S\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e3\b+\1\2")
        buf.write("\u01e3\u01e4\5V,\2\u01e4\u01ea\3\2\2\2\u01e5\u01e6\f\4")
        buf.write("\2\2\u01e6\u01e7\t\b\2\2\u01e7\u01e9\5V,\2\u01e8\u01e5")
        buf.write("\3\2\2\2\u01e9\u01ec\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea")
        buf.write("\u01eb\3\2\2\2\u01ebU\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed")
        buf.write("\u01ee\7\35\2\2\u01ee\u01f1\5V,\2\u01ef\u01f1\5X-\2\u01f0")
        buf.write("\u01ed\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1W\3\2\2\2\u01f2")
        buf.write("\u01f3\7$\2\2\u01f3\u01f6\5X-\2\u01f4\u01f6\5Z.\2\u01f5")
        buf.write("\u01f2\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6Y\3\2\2\2\u01f7")
        buf.write("\u01f8\b.\1\2\u01f8\u01f9\5\\/\2\u01f9\u01fe\3\2\2\2\u01fa")
        buf.write("\u01fb\f\4\2\2\u01fb\u01fd\5> \2\u01fc\u01fa\3\2\2\2\u01fd")
        buf.write("\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2")
        buf.write("\u01ff[\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0209\5\2\2")
        buf.write("\2\u0202\u0209\7>\2\2\u0203\u0204\7-\2\2\u0204\u0205\5")
        buf.write("N(\2\u0205\u0206\7.\2\2\u0206\u0209\3\2\2\2\u0207\u0209")
        buf.write("\5^\60\2\u0208\u0201\3\2\2\2\u0208\u0202\3\2\2\2\u0208")
        buf.write("\u0203\3\2\2\2\u0208\u0207\3\2\2\2\u0209]\3\2\2\2\u020a")
        buf.write("\u020b\7>\2\2\u020b\u020c\7-\2\2\u020c\u020d\58\35\2\u020d")
        buf.write("\u020e\7.\2\2\u020e_\3\2\2\2\u020f\u0210\t\4\2\2\u0210")
        buf.write("\u0211\5\60\31\2\u0211\u0214\7\64\2\2\u0212\u0215\5\f")
        buf.write("\7\2\u0213\u0215\5\n\6\2\u0214\u0212\3\2\2\2\u0214\u0213")
        buf.write("\3\2\2\2\u0215\u0218\3\2\2\2\u0216\u0217\7\34\2\2\u0217")
        buf.write("\u0219\58\35\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2")
        buf.write("\u0219\u021a\3\2\2\2\u021a\u021b\7\66\2\2\u021ba\3\2\2")
        buf.write("\2\u021c\u021f\5\b\5\2\u021d\u021f\5<\37\2\u021e\u021c")
        buf.write("\3\2\2\2\u021e\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220")
        buf.write("\u0221\7\34\2\2\u0221\u0222\5N(\2\u0222c\3\2\2\2\u0223")
        buf.write("\u0224\5f\64\2\u0224\u0225\5h\65\2\u0225\u0226\5j\66\2")
        buf.write("\u0226e\3\2\2\2\u0227\u0228\7\7\2\2\u0228\u0229\7-\2\2")
        buf.write("\u0229\u022a\5N(\2\u022a\u022b\7.\2\2\u022b\u022c\5x=")
        buf.write("\2\u022cg\3\2\2\2\u022d\u022e\7\b\2\2\u022e\u022f\7-\2")
        buf.write("\2\u022f\u0230\5N(\2\u0230\u0231\7.\2\2\u0231\u0232\5")
        buf.write("x=\2\u0232\u0236\3\2\2\2\u0233\u0235\5h\65\2\u0234\u0233")
        buf.write("\3\2\2\2\u0235\u0238\3\2\2\2\u0236\u0234\3\2\2\2\u0236")
        buf.write("\u0237\3\2\2\2\u0237i\3\2\2\2\u0238\u0236\3\2\2\2\u0239")
        buf.write("\u023a\7\t\2\2\u023a\u023c\5x=\2\u023b\u0239\3\2\2\2\u023b")
        buf.write("\u023c\3\2\2\2\u023ck\3\2\2\2\u023d\u023e\7\n\2\2\u023e")
        buf.write("\u023f\7-\2\2\u023f\u0240\5n8\2\u0240\u0241\7.\2\2\u0241")
        buf.write("\u0242\5x=\2\u0242m\3\2\2\2\u0243\u0244\7>\2\2\u0244\u0245")
        buf.write("\7\f\2\2\u0245\u0246\7:\2\2\u0246\u0247\7\62\2\2\u0247")
        buf.write("\u024a\7:\2\2\u0248\u0249\7\31\2\2\u0249\u024b\7:\2\2")
        buf.write("\u024a\u0248\3\2\2\2\u024a\u024b\3\2\2\2\u024bo\3\2\2")
        buf.write("\2\u024c\u024d\7\5\2\2\u024d\u024e\7\66\2\2\u024eq\3\2")
        buf.write("\2\2\u024f\u0250\7\6\2\2\u0250\u0251\7\66\2\2\u0251s\3")
        buf.write("\2\2\2\u0252\u0253\7\21\2\2\u0253\u0254\5N(\2\u0254\u0255")
        buf.write("\7\66\2\2\u0255u\3\2\2\2\u0256\u0257\7>\2\2\u0257\u0258")
        buf.write("\7\65\2\2\u0258\u0259\7?\2\2\u0259\u025a\7-\2\2\u025a")
        buf.write("\u025b\7.\2\2\u025b\u025c\7\66\2\2\u025cw\3\2\2\2\u025d")
        buf.write("\u025f\7\67\2\2\u025e\u0260\5z>\2\u025f\u025e\3\2\2\2")
        buf.write("\u025f\u0260\3\2\2\2\u0260\u0261\3\2\2\2\u0261\u0262\7")
        buf.write("8\2\2\u0262y\3\2\2\2\u0263\u026d\5`\61\2\u0264\u026d\5")
        buf.write("b\62\2\u0265\u026d\5d\63\2\u0266\u026d\5l\67\2\u0267\u026d")
        buf.write("\5p9\2\u0268\u026d\5r:\2\u0269\u026d\5t;\2\u026a\u026d")
        buf.write("\5v<\2\u026b\u026d\5x=\2\u026c\u0263\3\2\2\2\u026c\u0264")
        buf.write("\3\2\2\2\u026c\u0265\3\2\2\2\u026c\u0266\3\2\2\2\u026c")
        buf.write("\u0267\3\2\2\2\u026c\u0268\3\2\2\2\u026c\u0269\3\2\2\2")
        buf.write("\u026c\u026a\3\2\2\2\u026c\u026b\3\2\2\2\u026d{\3\2\2")
        buf.write("\2\67\u0082\u008b\u008e\u0095\u009d\u00a5\u00a8\u00b3")
        buf.write("\u00b6\u00d0\u00d5\u00dd\u00e1\u00e6\u00ef\u00f5\u0106")
        buf.write("\u0110\u0116\u011b\u0129\u0131\u013b\u0140\u0144\u014b")
        buf.write("\u0150\u0156\u015d\u0164\u016c\u0178\u0194\u01a1\u01b1")
        buf.write("\u01b3\u01bb\u01c9\u01d4\u01df\u01ea\u01f0\u01f5\u01fe")
        buf.write("\u0208\u0214\u0218\u021e\u0236\u023b\u024a\u025f\u026c")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Program'", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
                     "'Constructor'", "'Destructor'", "'New'", "'By'", "'main'", 
                     "'self'", "'='", "'!'", "'||'", "'&&'", "'=='", "'!='", 
                     "'%'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", "'>'", 
                     "'>='", "'+.'", "'==.'", "'('", "')'", "'['", "']'", 
                     "'.'", "'..'", "','", "':'", "'::'", "';'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COMMENT", "K_BREAK", "K_CONTINUE", 
                      "K_IF", "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", "K_ARRAY", 
                      "K_IN", "K_INT", "K_FLOAT", "K_BOOLEAN", "K_STRING", 
                      "K_RETURN", "K_NULL", "K_CLASS", "K_VAL", "K_VAR", 
                      "K_CONSTRUCTOR", "K_DESTRUCTOR", "K_NEW", "K_BY", 
                      "K_MAIN", "K_SELF", "OP_ASSIGN", "OP_LOGICAL_NOT", 
                      "OP_LOGICAL_OR", "OP_LOGICAL_AND", "OP_IS_EQUAL_TO", 
                      "OP_NOT_EQUAL_TO", "OP_MODULO", "OP_ADDTION", "OP_SUBTRACTION", 
                      "OP_MULTIPLICATION", "OP_DIVISION", "OP_LESS_THAN", 
                      "OP_LESS_THAN_EQUAL", "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", 
                      "OP_STRING_CONCATENATION", "OP_TWO_SAME_STRING", "LEFT_PAREN", 
                      "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                      "DOT", "DOUBLE_DOT", "COMMA", "COLON", "DOUBLE_COLON", 
                      "SEMI_COLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                      "ESCAPE", "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", 
                      "STRING_LITERAL", "IDENTIFIER", "DOLAR_IDENTIFIER", 
                      "WHITE_SPACE", "ERROR_TOKEN" ]

    RULE_literal = 0
    RULE_indexed_array = 1
    RULE_multi_dimentional_array = 2
    RULE_identifier = 3
    RULE_primitive_type = 4
    RULE_array_type = 5
    RULE_class_type = 6
    RULE_program = 7
    RULE_many_class = 8
    RULE_class_declaration = 9
    RULE_class_body = 10
    RULE_class_body_unit = 11
    RULE_super_class_group = 12
    RULE_program_class_declaration = 13
    RULE_program_class_body = 14
    RULE_main_method_declaration = 15
    RULE_method_declaration = 16
    RULE_constructor = 17
    RULE_destructor = 18
    RULE_parameter_list = 19
    RULE_parameter_list_tail = 20
    RULE_parameter = 21
    RULE_attribute_declaration = 22
    RULE_identifier_list = 23
    RULE_dolar_identifier_list = 24
    RULE_identifier_list_tail = 25
    RULE_dolar_identifier_list_tail = 26
    RULE_expression_list = 27
    RULE_expression_list_tail = 28
    RULE_element_expression = 29
    RULE_index_operator = 30
    RULE_instance_attribute_access = 31
    RULE_static_attribute_access = 32
    RULE_instace_method_invocation = 33
    RULE_object_creation = 34
    RULE_expr = 35
    RULE_exprList = 36
    RULE_relational_operator = 37
    RULE_expression = 38
    RULE_and_or_expr = 39
    RULE_add_sub_expr = 40
    RULE_mul_add_mol_expr = 41
    RULE_not_expr = 42
    RULE_sign_expr = 43
    RULE_index_operator_expr = 44
    RULE_atom_expr = 45
    RULE_function_call = 46
    RULE_var_val_statement = 47
    RULE_assign_statement = 48
    RULE_if_statement = 49
    RULE_if_part = 50
    RULE_else_if_part = 51
    RULE_else_part = 52
    RULE_for_in_statement = 53
    RULE_loop_part = 54
    RULE_break_statement = 55
    RULE_continue_statement = 56
    RULE_return_statement = 57
    RULE_method_invocation_statement = 58
    RULE_block_statement = 59
    RULE_statement = 60

    ruleNames =  [ "literal", "indexed_array", "multi_dimentional_array", 
                   "identifier", "primitive_type", "array_type", "class_type", 
                   "program", "many_class", "class_declaration", "class_body", 
                   "class_body_unit", "super_class_group", "program_class_declaration", 
                   "program_class_body", "main_method_declaration", "method_declaration", 
                   "constructor", "destructor", "parameter_list", "parameter_list_tail", 
                   "parameter", "attribute_declaration", "identifier_list", 
                   "dolar_identifier_list", "identifier_list_tail", "dolar_identifier_list_tail", 
                   "expression_list", "expression_list_tail", "element_expression", 
                   "index_operator", "instance_attribute_access", "static_attribute_access", 
                   "instace_method_invocation", "object_creation", "expr", 
                   "exprList", "relational_operator", "expression", "and_or_expr", 
                   "add_sub_expr", "mul_add_mol_expr", "not_expr", "sign_expr", 
                   "index_operator_expr", "atom_expr", "function_call", 
                   "var_val_statement", "assign_statement", "if_statement", 
                   "if_part", "else_if_part", "else_part", "for_in_statement", 
                   "loop_part", "break_statement", "continue_statement", 
                   "return_statement", "method_invocation_statement", "block_statement", 
                   "statement" ]

    EOF = Token.EOF
    T__0=1
    COMMENT=2
    K_BREAK=3
    K_CONTINUE=4
    K_IF=5
    K_ELSE_IF=6
    K_ELSE=7
    K_FOR_EACH=8
    K_ARRAY=9
    K_IN=10
    K_INT=11
    K_FLOAT=12
    K_BOOLEAN=13
    K_STRING=14
    K_RETURN=15
    K_NULL=16
    K_CLASS=17
    K_VAL=18
    K_VAR=19
    K_CONSTRUCTOR=20
    K_DESTRUCTOR=21
    K_NEW=22
    K_BY=23
    K_MAIN=24
    K_SELF=25
    OP_ASSIGN=26
    OP_LOGICAL_NOT=27
    OP_LOGICAL_OR=28
    OP_LOGICAL_AND=29
    OP_IS_EQUAL_TO=30
    OP_NOT_EQUAL_TO=31
    OP_MODULO=32
    OP_ADDTION=33
    OP_SUBTRACTION=34
    OP_MULTIPLICATION=35
    OP_DIVISION=36
    OP_LESS_THAN=37
    OP_LESS_THAN_EQUAL=38
    OP_GREATER_THAN=39
    OP_GREATER_THAN_EQUAL=40
    OP_STRING_CONCATENATION=41
    OP_TWO_SAME_STRING=42
    LEFT_PAREN=43
    RIGHT_PAREN=44
    LEFT_SQUARE_BRACKET=45
    RIGHT_SQUARE_BRACKET=46
    DOT=47
    DOUBLE_DOT=48
    COMMA=49
    COLON=50
    DOUBLE_COLON=51
    SEMI_COLON=52
    LEFT_CURLY_BRACKET=53
    RIGHT_CURLY_BRACKET=54
    ESCAPE=55
    INTEGER_LITERAL=56
    FLOAT_LITERAL=57
    BOOLEAN_LITERAL=58
    STRING_LITERAL=59
    IDENTIFIER=60
    DOLAR_IDENTIFIER=61
    WHITE_SPACE=62
    ERROR_TOKEN=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LiteralContext(ParserRuleContext):

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




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_literal)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(D96Parser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(D96Parser.FLOAT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 126
                self.indexed_array()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 127
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
            self.state = 130
            self.match(D96Parser.K_ARRAY)
            self.state = 131
            self.match(D96Parser.LEFT_PAREN)
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RIGHT_PAREN, D96Parser.INTEGER_LITERAL]:
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.INTEGER_LITERAL:
                    self.state = 132
                    self.match(D96Parser.INTEGER_LITERAL)
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.COMMA:
                        self.state = 133
                        self.match(D96Parser.COMMA)
                        self.state = 134
                        self.match(D96Parser.INTEGER_LITERAL)
                        self.state = 139
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.state = 142
                self.match(D96Parser.FLOAT_LITERAL)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 143
                    self.match(D96Parser.COMMA)
                    self.state = 144
                    self.match(D96Parser.FLOAT_LITERAL)
                    self.state = 149
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.state = 150
                self.match(D96Parser.BOOLEAN_LITERAL)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 151
                    self.match(D96Parser.COMMA)
                    self.state = 152
                    self.match(D96Parser.BOOLEAN_LITERAL)
                    self.state = 157
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.state = 158
                self.match(D96Parser.STRING_LITERAL)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 159
                    self.match(D96Parser.COMMA)
                    self.state = 160
                    self.match(D96Parser.STRING_LITERAL)
                    self.state = 165
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 168
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
            self.state = 170
            self.match(D96Parser.K_ARRAY)
            self.state = 171
            self.match(D96Parser.LEFT_PAREN)

            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ARRAY:
                self.state = 172
                self.indexed_array()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 173
                    self.match(D96Parser.COMMA)
                    self.state = 174
                    self.indexed_array()
                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 182
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
            self.state = 184
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
        self.enterRule(localctx, 8, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
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
        self.enterRule(localctx, 10, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(D96Parser.K_ARRAY)
            self.state = 189
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 190
            self.primitive_type()
            self.state = 191
            self.match(D96Parser.COMMA)
            self.state = 192
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 193
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
        self.enterRule(localctx, 12, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(D96Parser.K_NEW)
            self.state = 196
            self.match(D96Parser.IDENTIFIER)
            self.state = 197
            self.match(D96Parser.LEFT_PAREN)
            self.state = 198
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
        self.enterRule(localctx, 14, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.many_class()
            self.state = 201
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
        self.enterRule(localctx, 16, self.RULE_many_class)
        self._la = 0 # Token type
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 203
                    self.class_declaration()
                    self.state = 206 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.K_CLASS):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 208
                        self.class_declaration() 
                    self.state = 213
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                self.state = 214
                self.program_class_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self.program_class_declaration()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.K_CLASS:
                    self.state = 216
                    self.class_declaration()
                    self.state = 221
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
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
        self.enterRule(localctx, 18, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(D96Parser.K_CLASS)
            self.state = 226
            self.match(D96Parser.IDENTIFIER)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 227
                self.super_class_group()


            self.state = 230
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 231
            self.class_body()
            self.state = 232
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
        self.enterRule(localctx, 20, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_BREAK) | (1 << D96Parser.K_CONTINUE) | (1 << D96Parser.K_IF) | (1 << D96Parser.K_FOR_EACH) | (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_RETURN) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.LEFT_CURLY_BRACKET) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 234
                self.class_body_unit()
                self.state = 239
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
        self.enterRule(localctx, 22, self.RULE_class_body_unit)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.statement()
                pass


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
        self.enterRule(localctx, 24, self.RULE_super_class_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(D96Parser.COLON)
            self.state = 246
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
        self.enterRule(localctx, 26, self.RULE_program_class_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(D96Parser.K_CLASS)
            self.state = 249
            self.match(D96Parser.T__0)
            self.state = 250
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 251
            self.program_class_body()
            self.state = 252
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
        self.enterRule(localctx, 28, self.RULE_program_class_body)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.main_method_declaration()
                self.state = 255
                self.class_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.class_body()
                self.state = 258
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

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_main_method_declaration




    def main_method_declaration(self):

        localctx = D96Parser.Main_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_main_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(D96Parser.K_MAIN)
            self.state = 263
            self.match(D96Parser.LEFT_PAREN)
            self.state = 264
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 265
            self.block_statement()
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




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(D96Parser.IDENTIFIER)
                self.state = 268
                self.match(D96Parser.LEFT_PAREN)
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 269
                    self.parameter_list()


                self.state = 272
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 273
                self.block_statement()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.constructor()
                pass
            elif token in [D96Parser.K_DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
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

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(D96Parser.K_CONSTRUCTOR)
            self.state = 279
            self.match(D96Parser.LEFT_PAREN)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDENTIFIER:
                self.state = 280
                self.parameter_list()


            self.state = 283
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 284
            self.block_statement()
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

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(D96Parser.K_DESTRUCTOR)
            self.state = 287
            self.match(D96Parser.LEFT_PAREN)
            self.state = 288
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 289
            self.block_statement()
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
        self.enterRule(localctx, 38, self.RULE_parameter_list)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.parameter()
                self.state = 293
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
        self.enterRule(localctx, 40, self.RULE_parameter_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 297
                    self.match(D96Parser.SEMI_COLON)
                    self.state = 298
                    self.parameter()
                    self.state = 299
                    self.parameter_list_tail() 
                self.state = 305
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
        self.enterRule(localctx, 42, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.identifier_list()
            self.state = 307
            self.match(D96Parser.COLON)
            self.state = 308
            self.primitive_type()
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
        self.enterRule(localctx, 44, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER]:
                self.state = 311
                self.identifier_list()
                pass
            elif token in [D96Parser.DOLAR_IDENTIFIER]:
                self.state = 312
                self.dolar_identifier_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 315
            self.match(D96Parser.COLON)
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 316
                self.array_type()
                pass

            elif la_ == 2:
                self.state = 317
                self.primitive_type()
                pass


            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 320
                self.match(D96Parser.OP_ASSIGN)
                self.state = 321
                self.expression_list()


            self.state = 324
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
        self.enterRule(localctx, 46, self.RULE_identifier_list)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.match(D96Parser.IDENTIFIER)
                self.state = 328
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
        self.enterRule(localctx, 48, self.RULE_dolar_identifier_list)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 333
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
        self.enterRule(localctx, 50, self.RULE_identifier_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 336
                self.match(D96Parser.COMMA)
                self.state = 337
                self.match(D96Parser.IDENTIFIER)
                self.state = 342
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
        self.enterRule(localctx, 52, self.RULE_dolar_identifier_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 343
                self.match(D96Parser.COMMA)
                self.state = 344
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 349
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
        self.enterRule(localctx, 54, self.RULE_expression_list)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.expression(0)
                self.state = 352
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
        self.enterRule(localctx, 56, self.RULE_expression_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 356
                    self.match(D96Parser.COMMA)
                    self.state = 357
                    self.expression(0)
                    self.state = 358
                    self.expression_list_tail() 
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 58, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.expression(0)
            self.state = 366
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
        self.enterRule(localctx, 60, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 369
            self.expression(0)
            self.state = 370
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 371
                    self.index_operator() 
                self.state = 376
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
        self.enterRule(localctx, 62, self.RULE_instance_attribute_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(D96Parser.IDENTIFIER)
            self.state = 378
            self.match(D96Parser.DOT)
            self.state = 379
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
        self.enterRule(localctx, 64, self.RULE_static_attribute_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(D96Parser.IDENTIFIER)
            self.state = 382
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 383
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
        self.enterRule(localctx, 66, self.RULE_instace_method_invocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(D96Parser.IDENTIFIER)
            self.state = 386
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 387
            self.match(D96Parser.IDENTIFIER)
            self.state = 388
            self.match(D96Parser.LEFT_PAREN)
            self.state = 389
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
        self.enterRule(localctx, 68, self.RULE_object_creation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(D96Parser.K_NEW)
            self.state = 393
            self.match(D96Parser.IDENTIFIER)
            self.state = 394
            self.match(D96Parser.LEFT_PAREN)
            self.state = 395
            self.expression_list()
            self.state = 396
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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 399
                self.match(D96Parser.IDENTIFIER)
                self.state = 400
                self.match(D96Parser.LEFT_PAREN)
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 401
                    self.exprList()


                self.state = 404
                self.match(D96Parser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.state = 405
                self.match(D96Parser.OP_SUBTRACTION)
                self.state = 406
                self.expr(8)
                pass

            elif la_ == 3:
                self.state = 407
                self.match(D96Parser.OP_LOGICAL_NOT)
                self.state = 408
                self.expr(7)
                pass

            elif la_ == 4:
                self.state = 409
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.state = 410
                self.match(D96Parser.INTEGER_LITERAL)
                pass

            elif la_ == 6:
                self.state = 411
                self.match(D96Parser.LEFT_PAREN)
                self.state = 412
                self.expr(0)
                self.state = 413
                self.match(D96Parser.RIGHT_PAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 433
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 431
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 417
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 418
                        self.match(D96Parser.OP_MULTIPLICATION)
                        self.state = 419
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 420
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 421
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.OP_ADDTION or _la==D96Parser.OP_SUBTRACTION):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 422
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 423
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 424
                        self.match(D96Parser.OP_IS_EQUAL_TO)
                        self.state = 425
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 426
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 427
                        self.match(D96Parser.LEFT_SQUARE_BRACKET)
                        self.state = 428
                        self.expr(0)
                        self.state = 429
                        self.match(D96Parser.RIGHT_SQUARE_BRACKET)
                        pass

             
                self.state = 435
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
        self.enterRule(localctx, 72, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.expr(0)
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 437
                self.match(D96Parser.COMMA)
                self.state = 438
                self.expr(0)
                self.state = 443
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operatorContext(ParserRuleContext):

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




    def relational_operator(self):

        localctx = D96Parser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_or_expr(self):
            return self.getTypedRuleContext(D96Parser.And_or_exprContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def relational_operator(self):
            return self.getTypedRuleContext(D96Parser.Relational_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.and_or_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 455
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 449
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 450
                    self.relational_operator()
                    self.state = 451
                    self.expression(3) 
                self.state = 457
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class And_or_exprContext(ParserRuleContext):

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



    def and_or_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.And_or_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_and_or_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.add_sub_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 466
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.And_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_or_expr)
                    self.state = 461
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 462
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_LOGICAL_OR or _la==D96Parser.OP_LOGICAL_AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 463
                    self.add_sub_expr(0) 
                self.state = 468
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_sub_exprContext(ParserRuleContext):

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



    def add_sub_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Add_sub_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_add_sub_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.mul_add_mol_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 477
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Add_sub_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expr)
                    self.state = 472
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 473
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_ADDTION or _la==D96Parser.OP_SUBTRACTION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 474
                    self.mul_add_mol_expr(0) 
                self.state = 479
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_add_mol_exprContext(ParserRuleContext):

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



    def mul_add_mol_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Mul_add_mol_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_mul_add_mol_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 488
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Mul_add_mol_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_add_mol_expr)
                    self.state = 483
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 484
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MODULO) | (1 << D96Parser.OP_MULTIPLICATION) | (1 << D96Parser.OP_DIVISION))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 485
                    self.not_expr() 
                self.state = 490
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Not_exprContext(ParserRuleContext):

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




    def not_expr(self):

        localctx = D96Parser.Not_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_not_expr)
        try:
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.match(D96Parser.OP_LOGICAL_NOT)
                self.state = 492
                self.not_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.OP_SUBTRACTION, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
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




    def sign_expr(self):

        localctx = D96Parser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_sign_expr)
        try:
            self.state = 499
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUBTRACTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.match(D96Parser.OP_SUBTRACTION)
                self.state = 497
                self.sign_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_expr(self):
            return self.getTypedRuleContext(D96Parser.Atom_exprContext,0)


        def index_operator_expr(self):
            return self.getTypedRuleContext(D96Parser.Index_operator_exprContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operator_expr



    def index_operator_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_operator_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_index_operator_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.atom_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 508
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operator_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operator_expr)
                    self.state = 504
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 505
                    self.index_operator() 
                self.state = 510
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Atom_exprContext(ParserRuleContext):

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


        def getRuleIndex(self):
            return D96Parser.RULE_atom_expr




    def atom_expr(self):

        localctx = D96Parser.Atom_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_atom_expr)
        try:
            self.state = 518
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 513
                self.match(D96Parser.LEFT_PAREN)
                self.state = 514
                self.expression(0)
                self.state = 515
                self.match(D96Parser.RIGHT_PAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 517
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_function_call




    def function_call(self):

        localctx = D96Parser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(D96Parser.IDENTIFIER)
            self.state = 521
            self.match(D96Parser.LEFT_PAREN)
            self.state = 522
            self.expression_list()
            self.state = 523
            self.match(D96Parser.RIGHT_PAREN)
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
        self.enterRule(localctx, 94, self.RULE_var_val_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 526
            self.identifier_list()
            self.state = 527
            self.match(D96Parser.COLON)
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 528
                self.array_type()
                pass

            elif la_ == 2:
                self.state = 529
                self.primitive_type()
                pass


            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 532
                self.match(D96Parser.OP_ASSIGN)
                self.state = 533
                self.expression_list()


            self.state = 536
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
        self.enterRule(localctx, 96, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 538
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 539
                self.element_expression()
                pass


            self.state = 542
            self.match(D96Parser.OP_ASSIGN)
            self.state = 543
            self.expression(0)
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
        self.enterRule(localctx, 98, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.if_part()
            self.state = 546
            self.else_if_part()
            self.state = 547
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
        self.enterRule(localctx, 100, self.RULE_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(D96Parser.K_IF)
            self.state = 550
            self.match(D96Parser.LEFT_PAREN)
            self.state = 551
            self.expression(0)
            self.state = 552
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 553
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
        self.enterRule(localctx, 102, self.RULE_else_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(D96Parser.K_ELSE_IF)
            self.state = 556
            self.match(D96Parser.LEFT_PAREN)
            self.state = 557
            self.expression(0)
            self.state = 558
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 559
            self.block_statement()
            self.state = 564
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 561
                    self.else_if_part() 
                self.state = 566
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
        self.enterRule(localctx, 104, self.RULE_else_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ELSE:
                self.state = 567
                self.match(D96Parser.K_ELSE)
                self.state = 568
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
        self.enterRule(localctx, 106, self.RULE_for_in_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.match(D96Parser.K_FOR_EACH)
            self.state = 572
            self.match(D96Parser.LEFT_PAREN)
            self.state = 573
            self.loop_part()
            self.state = 574
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 575
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
        self.enterRule(localctx, 108, self.RULE_loop_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self.match(D96Parser.IDENTIFIER)
            self.state = 578
            self.match(D96Parser.K_IN)
            self.state = 579
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 580
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 581
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 584
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_BY:
                self.state = 582
                self.match(D96Parser.K_BY)
                self.state = 583
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
        self.enterRule(localctx, 110, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(D96Parser.K_BREAK)
            self.state = 587
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
        self.enterRule(localctx, 112, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.match(D96Parser.K_CONTINUE)
            self.state = 590
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
        self.enterRule(localctx, 114, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(D96Parser.K_RETURN)
            self.state = 593
            self.expression(0)
            self.state = 594
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
        self.enterRule(localctx, 116, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.match(D96Parser.IDENTIFIER)
            self.state = 597
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 598
            self.match(D96Parser.DOLAR_IDENTIFIER)
            self.state = 599
            self.match(D96Parser.LEFT_PAREN)
            self.state = 600
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 601
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
        self.enterRule(localctx, 118, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 605
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_BREAK) | (1 << D96Parser.K_CONTINUE) | (1 << D96Parser.K_IF) | (1 << D96Parser.K_FOR_EACH) | (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_RETURN) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.LEFT_CURLY_BRACKET) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 604
                self.statement()


            self.state = 607
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




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_statement)
        try:
            self.state = 618
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 609
                self.var_val_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 610
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 611
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 612
                self.for_in_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 613
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 614
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 615
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 616
                self.method_invocation_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 617
                self.block_statement()
                pass


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
        self._predicates[35] = self.expr_sempred
        self._predicates[38] = self.expression_sempred
        self._predicates[39] = self.and_or_expr_sempred
        self._predicates[40] = self.add_sub_expr_sempred
        self._predicates[41] = self.mul_add_mol_expr_sempred
        self._predicates[44] = self.index_operator_expr_sempred
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
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def and_or_expr_sempred(self, localctx:And_or_exprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def add_sub_expr_sempred(self, localctx:Add_sub_exprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def mul_add_mol_expr_sempred(self, localctx:Mul_add_mol_exprContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def index_operator_expr_sempred(self, localctx:Index_operator_exprContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




