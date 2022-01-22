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
        buf.write("\u026a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\3\6\3\u0081\n\3\r\3")
        buf.write("\16\3\u0082\3\3\7\3\u0086\n\3\f\3\16\3\u0089\13\3\3\3")
        buf.write("\3\3\3\3\7\3\u008e\n\3\f\3\16\3\u0091\13\3\3\3\5\3\u0094")
        buf.write("\n\3\3\4\3\4\3\4\5\4\u0099\n\4\3\4\3\4\3\4\3\4\3\5\7\5")
        buf.write("\u00a0\n\5\f\5\16\5\u00a3\13\5\3\6\3\6\3\6\5\6\u00a8\n")
        buf.write("\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\5\t\u00b9\n\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\5\13\u00c3\n\13\3\13\3\13\3\13\3\13\5\13\u00c9\n\13")
        buf.write("\3\f\3\f\3\f\5\f\u00ce\n\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\5\16\u00dc\n\16\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u00e2\n\17\f\17\16\17\u00e5\13\17\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\5\21\u00ee\n\21\3\21\3\21\3")
        buf.write("\21\5\21\u00f3\n\21\3\21\3\21\5\21\u00f7\n\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\5\22\u00fe\n\22\3\23\3\23\3\23\5\23\u0103")
        buf.write("\n\23\3\24\3\24\7\24\u0107\n\24\f\24\16\24\u010a\13\24")
        buf.write("\3\25\3\25\7\25\u010e\n\25\f\25\16\25\u0111\13\25\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u0117\n\26\3\27\3\27\3\27\3\27\7")
        buf.write("\27\u011d\n\27\f\27\16\27\u0120\13\27\3\30\3\30\3\30\3")
        buf.write("\31\3\31\3\31\3\31\7\31\u0129\n\31\f\31\16\31\u012c\13")
        buf.write("\31\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0136")
        buf.write("\n\33\f\33\16\33\u0139\13\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\7\34\u0142\n\34\f\34\16\34\u0145\13\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\7\35\u014d\n\35\f\35\16\35\u0150")
        buf.write("\13\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0158\n\36\f")
        buf.write("\36\16\36\u015b\13\36\3\37\3\37\3\37\3\37\3\37\3\37\7")
        buf.write("\37\u0163\n\37\f\37\16\37\u0166\13\37\3 \3 \3 \5 \u016b")
        buf.write("\n \3!\3!\3!\5!\u0170\n!\3\"\3\"\3\"\3\"\3\"\7\"\u0177")
        buf.write("\n\"\f\"\16\"\u017a\13\"\3#\3#\3#\3#\3#\3#\7#\u0182\n")
        buf.write("#\f#\16#\u0185\13#\3$\3$\3$\3$\3$\3$\3$\3$\5$\u018f\n")
        buf.write("$\3$\7$\u0192\n$\f$\16$\u0195\13$\3%\3%\3%\3%\5%\u019b")
        buf.write("\n%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\5\'\u01a7\n\'\3")
        buf.write("\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01b4\n(\3)\3)\3")
        buf.write(")\5)\u01b9\n)\3)\3)\3*\3*\3*\3*\3*\5*\u01c2\n*\3*\3*\5")
        buf.write("*\u01c6\n*\3*\3*\3+\3+\5+\u01cc\n+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\7.\u01e2\n.\f")
        buf.write(".\16.\u01e5\13.\3/\3/\5/\u01e9\n/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01f8")
        buf.write("\n\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\5\66\u020d")
        buf.write("\n\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\5\67\u021a\n\67\38\38\38\38\38\38\58\u0222\n8\3")
        buf.write("9\39\39\39\39\79\u0229\n9\f9\169\u022c\139\59\u022e\n")
        buf.write("9\39\39\39\79\u0233\n9\f9\169\u0236\139\39\39\39\79\u023b")
        buf.write("\n9\f9\169\u023e\139\39\39\39\79\u0243\n9\f9\169\u0246")
        buf.write("\139\59\u0248\n9\39\39\3:\3:\3:\3:\3:\7:\u0251\n:\f:\16")
        buf.write(":\u0254\13:\5:\u0256\n:\3:\3:\3;\3;\3<\3<\3=\3=\3=\3=")
        buf.write("\3=\3=\3=\3>\3>\3>\3>\3>\3>\2\n\64\668:<BDF?\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2\n\3\2\24\25\4\2 !\'")
        buf.write("*\3\2+,\3\2\36\37\3\2#$\4\2\"\"%&\3\2>?\4\2\13\13\r\20")
        buf.write("\2\u0278\2|\3\2\2\2\4\u0093\3\2\2\2\6\u0095\3\2\2\2\b")
        buf.write("\u00a1\3\2\2\2\n\u00a7\3\2\2\2\f\u00a9\3\2\2\2\16\u00ac")
        buf.write("\3\2\2\2\20\u00b8\3\2\2\2\22\u00ba\3\2\2\2\24\u00c8\3")
        buf.write("\2\2\2\26\u00ca\3\2\2\2\30\u00d2\3\2\2\2\32\u00db\3\2")
        buf.write("\2\2\34\u00e3\3\2\2\2\36\u00e6\3\2\2\2 \u00ea\3\2\2\2")
        buf.write("\"\u00fd\3\2\2\2$\u0102\3\2\2\2&\u0108\3\2\2\2(\u010f")
        buf.write("\3\2\2\2*\u0116\3\2\2\2,\u011e\3\2\2\2.\u0121\3\2\2\2")
        buf.write("\60\u0124\3\2\2\2\62\u012d\3\2\2\2\64\u012f\3\2\2\2\66")
        buf.write("\u013a\3\2\2\28\u0146\3\2\2\2:\u0151\3\2\2\2<\u015c\3")
        buf.write("\2\2\2>\u016a\3\2\2\2@\u016f\3\2\2\2B\u0171\3\2\2\2D\u017b")
        buf.write("\3\2\2\2F\u0186\3\2\2\2H\u0196\3\2\2\2J\u019e\3\2\2\2")
        buf.write("L\u01a2\3\2\2\2N\u01b3\3\2\2\2P\u01b5\3\2\2\2R\u01bc\3")
        buf.write("\2\2\2T\u01cb\3\2\2\2V\u01d0\3\2\2\2X\u01d4\3\2\2\2Z\u01da")
        buf.write("\3\2\2\2\\\u01e8\3\2\2\2^\u01ea\3\2\2\2`\u01f0\3\2\2\2")
        buf.write("b\u01f9\3\2\2\2d\u01fc\3\2\2\2f\u01ff\3\2\2\2h\u0203\3")
        buf.write("\2\2\2j\u020a\3\2\2\2l\u0219\3\2\2\2n\u0221\3\2\2\2p\u0223")
        buf.write("\3\2\2\2r\u024b\3\2\2\2t\u0259\3\2\2\2v\u025b\3\2\2\2")
        buf.write("x\u025d\3\2\2\2z\u0264\3\2\2\2|}\5\4\3\2}~\7\2\2\3~\3")
        buf.write("\3\2\2\2\177\u0081\5\6\4\2\u0080\177\3\2\2\2\u0081\u0082")
        buf.write("\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0094\3\2\2\2\u0084\u0086\5\6\4\2\u0085\u0084\3\2\2\2")
        buf.write("\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3")
        buf.write("\2\2\2\u0088\u008a\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u0094")
        buf.write("\5\16\b\2\u008b\u008f\5\16\b\2\u008c\u008e\5\6\4\2\u008d")
        buf.write("\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u008f\u0090\3\2\2\2\u0090\u0094\3\2\2\2\u0091\u008f\3")
        buf.write("\2\2\2\u0092\u0094\5\16\b\2\u0093\u0080\3\2\2\2\u0093")
        buf.write("\u0087\3\2\2\2\u0093\u008b\3\2\2\2\u0093\u0092\3\2\2\2")
        buf.write("\u0094\5\3\2\2\2\u0095\u0096\7\23\2\2\u0096\u0098\7>\2")
        buf.write("\2\u0097\u0099\5\f\7\2\u0098\u0097\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\7\67\2\2\u009b")
        buf.write("\u009c\5\b\5\2\u009c\u009d\78\2\2\u009d\7\3\2\2\2\u009e")
        buf.write("\u00a0\5\n\6\2\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2")
        buf.write("\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\t\3\2\2")
        buf.write("\2\u00a3\u00a1\3\2\2\2\u00a4\u00a8\5 \21\2\u00a5\u00a8")
        buf.write("\5\24\13\2\u00a6\u00a8\5l\67\2\u00a7\u00a4\3\2\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\13\3\2\2\2\u00a9")
        buf.write("\u00aa\7\64\2\2\u00aa\u00ab\7>\2\2\u00ab\r\3\2\2\2\u00ac")
        buf.write("\u00ad\7\23\2\2\u00ad\u00ae\7\3\2\2\u00ae\u00af\7\67\2")
        buf.write("\2\u00af\u00b0\5\20\t\2\u00b0\u00b1\78\2\2\u00b1\17\3")
        buf.write("\2\2\2\u00b2\u00b3\5\22\n\2\u00b3\u00b4\5\b\5\2\u00b4")
        buf.write("\u00b9\3\2\2\2\u00b5\u00b6\5\b\5\2\u00b6\u00b7\5\22\n")
        buf.write("\2\u00b7\u00b9\3\2\2\2\u00b8\u00b2\3\2\2\2\u00b8\u00b5")
        buf.write("\3\2\2\2\u00b9\21\3\2\2\2\u00ba\u00bb\7\32\2\2\u00bb\u00bc")
        buf.write("\7-\2\2\u00bc\u00bd\7.\2\2\u00bd\u00be\5j\66\2\u00be\23")
        buf.write("\3\2\2\2\u00bf\u00c0\7>\2\2\u00c0\u00c2\7-\2\2\u00c1\u00c3")
        buf.write("\5\32\16\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00c4\3\2\2\2\u00c4\u00c5\7.\2\2\u00c5\u00c9\5j\66\2")
        buf.write("\u00c6\u00c9\5\26\f\2\u00c7\u00c9\5\30\r\2\u00c8\u00bf")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9")
        buf.write("\25\3\2\2\2\u00ca\u00cb\7\26\2\2\u00cb\u00cd\7-\2\2\u00cc")
        buf.write("\u00ce\5\32\16\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2")
        buf.write("\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\7.\2\2\u00d0\u00d1")
        buf.write("\5j\66\2\u00d1\27\3\2\2\2\u00d2\u00d3\7\27\2\2\u00d3\u00d4")
        buf.write("\7-\2\2\u00d4\u00d5\7.\2\2\u00d5\u00d6\5j\66\2\u00d6\31")
        buf.write("\3\2\2\2\u00d7\u00dc\5\36\20\2\u00d8\u00d9\5\36\20\2\u00d9")
        buf.write("\u00da\5\34\17\2\u00da\u00dc\3\2\2\2\u00db\u00d7\3\2\2")
        buf.write("\2\u00db\u00d8\3\2\2\2\u00dc\33\3\2\2\2\u00dd\u00de\7")
        buf.write("\66\2\2\u00de\u00df\5\36\20\2\u00df\u00e0\5\34\17\2\u00e0")
        buf.write("\u00e2\3\2\2\2\u00e1\u00dd\3\2\2\2\u00e2\u00e5\3\2\2\2")
        buf.write("\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\35\3\2")
        buf.write("\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e7\5\"\22\2\u00e7\u00e8")
        buf.write("\7\64\2\2\u00e8\u00e9\5v<\2\u00e9\37\3\2\2\2\u00ea\u00ed")
        buf.write("\t\2\2\2\u00eb\u00ee\5\"\22\2\u00ec\u00ee\5$\23\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2")
        buf.write("\u00ef\u00f2\7\64\2\2\u00f0\u00f3\5x=\2\u00f1\u00f3\5")
        buf.write("v<\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\u00f6")
        buf.write("\3\2\2\2\u00f4\u00f5\7\34\2\2\u00f5\u00f7\5*\26\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\u00f9\7\66\2\2\u00f9!\3\2\2\2\u00fa\u00fe\7>\2")
        buf.write("\2\u00fb\u00fc\7>\2\2\u00fc\u00fe\5&\24\2\u00fd\u00fa")
        buf.write("\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe#\3\2\2\2\u00ff\u0103")
        buf.write("\7?\2\2\u0100\u0101\7?\2\2\u0101\u0103\5(\25\2\u0102\u00ff")
        buf.write("\3\2\2\2\u0102\u0100\3\2\2\2\u0103%\3\2\2\2\u0104\u0105")
        buf.write("\7\63\2\2\u0105\u0107\7>\2\2\u0106\u0104\3\2\2\2\u0107")
        buf.write("\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2")
        buf.write("\u0109\'\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c\7\63")
        buf.write("\2\2\u010c\u010e\7?\2\2\u010d\u010b\3\2\2\2\u010e\u0111")
        buf.write("\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write(")\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0117\5\64\33\2\u0113")
        buf.write("\u0114\5\64\33\2\u0114\u0115\5,\27\2\u0115\u0117\3\2\2")
        buf.write("\2\u0116\u0112\3\2\2\2\u0116\u0113\3\2\2\2\u0117+\3\2")
        buf.write("\2\2\u0118\u0119\7\63\2\2\u0119\u011a\5\64\33\2\u011a")
        buf.write("\u011b\5,\27\2\u011b\u011d\3\2\2\2\u011c\u0118\3\2\2\2")
        buf.write("\u011d\u0120\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3")
        buf.write("\2\2\2\u011f-\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0122")
        buf.write("\5\64\33\2\u0122\u0123\5\60\31\2\u0123/\3\2\2\2\u0124")
        buf.write("\u0125\7/\2\2\u0125\u0126\5\64\33\2\u0126\u012a\7\60\2")
        buf.write("\2\u0127\u0129\5\60\31\2\u0128\u0127\3\2\2\2\u0129\u012c")
        buf.write("\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b")
        buf.write("\61\3\2\2\2\u012c\u012a\3\2\2\2\u012d\u012e\t\3\2\2\u012e")
        buf.write("\63\3\2\2\2\u012f\u0130\b\33\1\2\u0130\u0131\5\66\34\2")
        buf.write("\u0131\u0137\3\2\2\2\u0132\u0133\f\4\2\2\u0133\u0134\t")
        buf.write("\4\2\2\u0134\u0136\5\66\34\2\u0135\u0132\3\2\2\2\u0136")
        buf.write("\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\65\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u013b\b\34")
        buf.write("\1\2\u013b\u013c\58\35\2\u013c\u0143\3\2\2\2\u013d\u013e")
        buf.write("\f\4\2\2\u013e\u013f\5\62\32\2\u013f\u0140\58\35\2\u0140")
        buf.write("\u0142\3\2\2\2\u0141\u013d\3\2\2\2\u0142\u0145\3\2\2\2")
        buf.write("\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\67\3\2")
        buf.write("\2\2\u0145\u0143\3\2\2\2\u0146\u0147\b\35\1\2\u0147\u0148")
        buf.write("\5:\36\2\u0148\u014e\3\2\2\2\u0149\u014a\f\4\2\2\u014a")
        buf.write("\u014b\t\5\2\2\u014b\u014d\5:\36\2\u014c\u0149\3\2\2\2")
        buf.write("\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f\3")
        buf.write("\2\2\2\u014f9\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0152")
        buf.write("\b\36\1\2\u0152\u0153\5<\37\2\u0153\u0159\3\2\2\2\u0154")
        buf.write("\u0155\f\4\2\2\u0155\u0156\t\6\2\2\u0156\u0158\5<\37\2")
        buf.write("\u0157\u0154\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3")
        buf.write("\2\2\2\u0159\u015a\3\2\2\2\u015a;\3\2\2\2\u015b\u0159")
        buf.write("\3\2\2\2\u015c\u015d\b\37\1\2\u015d\u015e\5> \2\u015e")
        buf.write("\u0164\3\2\2\2\u015f\u0160\f\4\2\2\u0160\u0161\t\7\2\2")
        buf.write("\u0161\u0163\5> \2\u0162\u015f\3\2\2\2\u0163\u0166\3\2")
        buf.write("\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165=\3")
        buf.write("\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168\7\35\2\2\u0168")
        buf.write("\u016b\5> \2\u0169\u016b\5@!\2\u016a\u0167\3\2\2\2\u016a")
        buf.write("\u0169\3\2\2\2\u016b?\3\2\2\2\u016c\u016d\7$\2\2\u016d")
        buf.write("\u0170\5@!\2\u016e\u0170\5B\"\2\u016f\u016c\3\2\2\2\u016f")
        buf.write("\u016e\3\2\2\2\u0170A\3\2\2\2\u0171\u0172\b\"\1\2\u0172")
        buf.write("\u0173\5D#\2\u0173\u0178\3\2\2\2\u0174\u0175\f\4\2\2\u0175")
        buf.write("\u0177\5\60\31\2\u0176\u0174\3\2\2\2\u0177\u017a\3\2\2")
        buf.write("\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179C\3\2")
        buf.write("\2\2\u017a\u0178\3\2\2\2\u017b\u017c\b#\1\2\u017c\u017d")
        buf.write("\5F$\2\u017d\u0183\3\2\2\2\u017e\u017f\f\4\2\2\u017f\u0180")
        buf.write("\7\61\2\2\u0180\u0182\7>\2\2\u0181\u017e\3\2\2\2\u0182")
        buf.write("\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184E\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0187\b$\1\2")
        buf.write("\u0187\u0188\5N(\2\u0188\u0193\3\2\2\2\u0189\u018a\f\4")
        buf.write("\2\2\u018a\u018b\7\65\2\2\u018b\u018c\7>\2\2\u018c\u018e")
        buf.write("\7-\2\2\u018d\u018f\5*\26\2\u018e\u018d\3\2\2\2\u018e")
        buf.write("\u018f\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0192\7.\2\2")
        buf.write("\u0191\u0189\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3")
        buf.write("\2\2\2\u0193\u0194\3\2\2\2\u0194G\3\2\2\2\u0195\u0193")
        buf.write("\3\2\2\2\u0196\u0197\7>\2\2\u0197\u0198\7\65\2\2\u0198")
        buf.write("\u019a\7-\2\2\u0199\u019b\5*\26\2\u019a\u0199\3\2\2\2")
        buf.write("\u019a\u019b\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d\7")
        buf.write(".\2\2\u019dI\3\2\2\2\u019e\u019f\7>\2\2\u019f\u01a0\7")
        buf.write("\65\2\2\u01a0\u01a1\7>\2\2\u01a1K\3\2\2\2\u01a2\u01a3")
        buf.write("\7\30\2\2\u01a3\u01a4\7>\2\2\u01a4\u01a6\7-\2\2\u01a5")
        buf.write("\u01a7\5*\26\2\u01a6\u01a5\3\2\2\2\u01a6\u01a7\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8\u01a9\7.\2\2\u01a9M\3\2\2\2")
        buf.write("\u01aa\u01b4\5n8\2\u01ab\u01b4\7>\2\2\u01ac\u01ad\7-\2")
        buf.write("\2\u01ad\u01ae\5\64\33\2\u01ae\u01af\7.\2\2\u01af\u01b4")
        buf.write("\3\2\2\2\u01b0\u01b4\5P)\2\u01b1\u01b4\5H%\2\u01b2\u01b4")
        buf.write("\5J&\2\u01b3\u01aa\3\2\2\2\u01b3\u01ab\3\2\2\2\u01b3\u01ac")
        buf.write("\3\2\2\2\u01b3\u01b0\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b4O\3\2\2\2\u01b5\u01b6\7>\2\2\u01b6")
        buf.write("\u01b8\7-\2\2\u01b7\u01b9\5*\26\2\u01b8\u01b7\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb\7")
        buf.write(".\2\2\u01bbQ\3\2\2\2\u01bc\u01bd\t\2\2\2\u01bd\u01be\5")
        buf.write("\"\22\2\u01be\u01c1\7\64\2\2\u01bf\u01c2\5x=\2\u01c0\u01c2")
        buf.write("\5v<\2\u01c1\u01bf\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5")
        buf.write("\3\2\2\2\u01c3\u01c4\7\34\2\2\u01c4\u01c6\5*\26\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\3\2\2\2")
        buf.write("\u01c7\u01c8\7\66\2\2\u01c8S\3\2\2\2\u01c9\u01cc\5t;\2")
        buf.write("\u01ca\u01cc\5.\30\2\u01cb\u01c9\3\2\2\2\u01cb\u01ca\3")
        buf.write("\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\7\34\2\2\u01ce")
        buf.write("\u01cf\5\64\33\2\u01cfU\3\2\2\2\u01d0\u01d1\5X-\2\u01d1")
        buf.write("\u01d2\5Z.\2\u01d2\u01d3\5\\/\2\u01d3W\3\2\2\2\u01d4\u01d5")
        buf.write("\7\7\2\2\u01d5\u01d6\7-\2\2\u01d6\u01d7\5\64\33\2\u01d7")
        buf.write("\u01d8\7.\2\2\u01d8\u01d9\5j\66\2\u01d9Y\3\2\2\2\u01da")
        buf.write("\u01db\7\b\2\2\u01db\u01dc\7-\2\2\u01dc\u01dd\5\64\33")
        buf.write("\2\u01dd\u01de\7.\2\2\u01de\u01df\5j\66\2\u01df\u01e3")
        buf.write("\3\2\2\2\u01e0\u01e2\5Z.\2\u01e1\u01e0\3\2\2\2\u01e2\u01e5")
        buf.write("\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4")
        buf.write("[\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e7\7\t\2\2\u01e7")
        buf.write("\u01e9\5j\66\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2")
        buf.write("\u01e9]\3\2\2\2\u01ea\u01eb\7\n\2\2\u01eb\u01ec\7-\2\2")
        buf.write("\u01ec\u01ed\5`\61\2\u01ed\u01ee\7.\2\2\u01ee\u01ef\5")
        buf.write("j\66\2\u01ef_\3\2\2\2\u01f0\u01f1\7>\2\2\u01f1\u01f2\7")
        buf.write("\f\2\2\u01f2\u01f3\7:\2\2\u01f3\u01f4\7\62\2\2\u01f4\u01f7")
        buf.write("\7:\2\2\u01f5\u01f6\7\31\2\2\u01f6\u01f8\7:\2\2\u01f7")
        buf.write("\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8a\3\2\2\2\u01f9")
        buf.write("\u01fa\7\5\2\2\u01fa\u01fb\7\66\2\2\u01fbc\3\2\2\2\u01fc")
        buf.write("\u01fd\7\6\2\2\u01fd\u01fe\7\66\2\2\u01fee\3\2\2\2\u01ff")
        buf.write("\u0200\7\21\2\2\u0200\u0201\5\64\33\2\u0201\u0202\7\66")
        buf.write("\2\2\u0202g\3\2\2\2\u0203\u0204\7>\2\2\u0204\u0205\7\65")
        buf.write("\2\2\u0205\u0206\7?\2\2\u0206\u0207\7-\2\2\u0207\u0208")
        buf.write("\7.\2\2\u0208\u0209\7\66\2\2\u0209i\3\2\2\2\u020a\u020c")
        buf.write("\7\67\2\2\u020b\u020d\5l\67\2\u020c\u020b\3\2\2\2\u020c")
        buf.write("\u020d\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f\78\2\2")
        buf.write("\u020fk\3\2\2\2\u0210\u021a\5R*\2\u0211\u021a\5T+\2\u0212")
        buf.write("\u021a\5V,\2\u0213\u021a\5^\60\2\u0214\u021a\5b\62\2\u0215")
        buf.write("\u021a\5d\63\2\u0216\u021a\5f\64\2\u0217\u021a\5h\65\2")
        buf.write("\u0218\u021a\5j\66\2\u0219\u0210\3\2\2\2\u0219\u0211\3")
        buf.write("\2\2\2\u0219\u0212\3\2\2\2\u0219\u0213\3\2\2\2\u0219\u0214")
        buf.write("\3\2\2\2\u0219\u0215\3\2\2\2\u0219\u0216\3\2\2\2\u0219")
        buf.write("\u0217\3\2\2\2\u0219\u0218\3\2\2\2\u021am\3\2\2\2\u021b")
        buf.write("\u0222\7:\2\2\u021c\u0222\7;\2\2\u021d\u0222\7<\2\2\u021e")
        buf.write("\u0222\7=\2\2\u021f\u0222\5p9\2\u0220\u0222\5r:\2\u0221")
        buf.write("\u021b\3\2\2\2\u0221\u021c\3\2\2\2\u0221\u021d\3\2\2\2")
        buf.write("\u0221\u021e\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0220\3")
        buf.write("\2\2\2\u0222o\3\2\2\2\u0223\u0224\7\13\2\2\u0224\u0247")
        buf.write("\7-\2\2\u0225\u022a\7:\2\2\u0226\u0227\7\63\2\2\u0227")
        buf.write("\u0229\7:\2\2\u0228\u0226\3\2\2\2\u0229\u022c\3\2\2\2")
        buf.write("\u022a\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022e\3")
        buf.write("\2\2\2\u022c\u022a\3\2\2\2\u022d\u0225\3\2\2\2\u022d\u022e")
        buf.write("\3\2\2\2\u022e\u0248\3\2\2\2\u022f\u0234\7;\2\2\u0230")
        buf.write("\u0231\7\63\2\2\u0231\u0233\7;\2\2\u0232\u0230\3\2\2\2")
        buf.write("\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3")
        buf.write("\2\2\2\u0235\u0248\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u023c")
        buf.write("\7<\2\2\u0238\u0239\7\63\2\2\u0239\u023b\7<\2\2\u023a")
        buf.write("\u0238\3\2\2\2\u023b\u023e\3\2\2\2\u023c\u023a\3\2\2\2")
        buf.write("\u023c\u023d\3\2\2\2\u023d\u0248\3\2\2\2\u023e\u023c\3")
        buf.write("\2\2\2\u023f\u0244\7=\2\2\u0240\u0241\7\63\2\2\u0241\u0243")
        buf.write("\7=\2\2\u0242\u0240\3\2\2\2\u0243\u0246\3\2\2\2\u0244")
        buf.write("\u0242\3\2\2\2\u0244\u0245\3\2\2\2\u0245\u0248\3\2\2\2")
        buf.write("\u0246\u0244\3\2\2\2\u0247\u022d\3\2\2\2\u0247\u022f\3")
        buf.write("\2\2\2\u0247\u0237\3\2\2\2\u0247\u023f\3\2\2\2\u0248\u0249")
        buf.write("\3\2\2\2\u0249\u024a\7.\2\2\u024aq\3\2\2\2\u024b\u024c")
        buf.write("\7\13\2\2\u024c\u0255\7-\2\2\u024d\u0252\5p9\2\u024e\u024f")
        buf.write("\7\63\2\2\u024f\u0251\5p9\2\u0250\u024e\3\2\2\2\u0251")
        buf.write("\u0254\3\2\2\2\u0252\u0250\3\2\2\2\u0252\u0253\3\2\2\2")
        buf.write("\u0253\u0256\3\2\2\2\u0254\u0252\3\2\2\2\u0255\u024d\3")
        buf.write("\2\2\2\u0255\u0256\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0258")
        buf.write("\7.\2\2\u0258s\3\2\2\2\u0259\u025a\t\b\2\2\u025au\3\2")
        buf.write("\2\2\u025b\u025c\t\t\2\2\u025cw\3\2\2\2\u025d\u025e\7")
        buf.write("\13\2\2\u025e\u025f\7/\2\2\u025f\u0260\5v<\2\u0260\u0261")
        buf.write("\7\63\2\2\u0261\u0262\7:\2\2\u0262\u0263\7\60\2\2\u0263")
        buf.write("y\3\2\2\2\u0264\u0265\7\30\2\2\u0265\u0266\7>\2\2\u0266")
        buf.write("\u0267\7-\2\2\u0267\u0268\7.\2\2\u0268{\3\2\2\29\u0082")
        buf.write("\u0087\u008f\u0093\u0098\u00a1\u00a7\u00b8\u00c2\u00c8")
        buf.write("\u00cd\u00db\u00e3\u00ed\u00f2\u00f6\u00fd\u0102\u0108")
        buf.write("\u010f\u0116\u011e\u012a\u0137\u0143\u014e\u0159\u0164")
        buf.write("\u016a\u016f\u0178\u0183\u018e\u0193\u019a\u01a6\u01b3")
        buf.write("\u01b8\u01c1\u01c5\u01cb\u01e3\u01e8\u01f7\u020c\u0219")
        buf.write("\u0221\u022a\u022d\u0234\u023c\u0244\u0247\u0252\u0255")
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
    RULE_parameter_list_tail = 13
    RULE_parameter = 14
    RULE_attribute_declaration = 15
    RULE_identifier_list = 16
    RULE_dolar_identifier_list = 17
    RULE_identifier_list_tail = 18
    RULE_dolar_identifier_list_tail = 19
    RULE_expression_list = 20
    RULE_expression_list_tail = 21
    RULE_element_expression = 22
    RULE_index_operator = 23
    RULE_relational_operator = 24
    RULE_expression = 25
    RULE_relational_expr = 26
    RULE_and_or_expr = 27
    RULE_add_sub_expr = 28
    RULE_mul_add_mol_expr = 29
    RULE_not_expr = 30
    RULE_sign_expr = 31
    RULE_index_operator_expr = 32
    RULE_instance_attribute_access = 33
    RULE_instace_method_invocation = 34
    RULE_static_method_invocation = 35
    RULE_static_attribute_access = 36
    RULE_object_creation = 37
    RULE_atom_expr = 38
    RULE_function_call = 39
    RULE_var_val_statement = 40
    RULE_assign_statement = 41
    RULE_if_statement = 42
    RULE_if_part = 43
    RULE_else_if_part = 44
    RULE_else_part = 45
    RULE_for_in_statement = 46
    RULE_loop_part = 47
    RULE_break_statement = 48
    RULE_continue_statement = 49
    RULE_return_statement = 50
    RULE_method_invocation_statement = 51
    RULE_block_statement = 52
    RULE_statement = 53
    RULE_literal = 54
    RULE_indexed_array = 55
    RULE_multi_dimentional_array = 56
    RULE_identifier = 57
    RULE_primitive_type = 58
    RULE_array_type = 59
    RULE_class_type = 60

    ruleNames =  [ "program", "many_class", "class_declaration", "class_body", 
                   "class_body_unit", "super_class_group", "program_class_declaration", 
                   "program_class_body", "main_method_declaration", "method_declaration", 
                   "constructor", "destructor", "parameter_list", "parameter_list_tail", 
                   "parameter", "attribute_declaration", "identifier_list", 
                   "dolar_identifier_list", "identifier_list_tail", "dolar_identifier_list_tail", 
                   "expression_list", "expression_list_tail", "element_expression", 
                   "index_operator", "relational_operator", "expression", 
                   "relational_expr", "and_or_expr", "add_sub_expr", "mul_add_mol_expr", 
                   "not_expr", "sign_expr", "index_operator_expr", "instance_attribute_access", 
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
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.many_class()
            self.state = 123
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
        self.enterRule(localctx, 2, self.RULE_many_class)
        self._la = 0 # Token type
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 125
                    self.class_declaration()
                    self.state = 128 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.K_CLASS):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 130
                        self.class_declaration() 
                    self.state = 135
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 136
                self.program_class_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.program_class_declaration()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.K_CLASS:
                    self.state = 138
                    self.class_declaration()
                    self.state = 143
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
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
        self.enterRule(localctx, 4, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(D96Parser.K_CLASS)
            self.state = 148
            self.match(D96Parser.IDENTIFIER)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 149
                self.super_class_group()


            self.state = 152
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 153
            self.class_body()
            self.state = 154
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
        self.enterRule(localctx, 6, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_BREAK) | (1 << D96Parser.K_CONTINUE) | (1 << D96Parser.K_IF) | (1 << D96Parser.K_FOR_EACH) | (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_RETURN) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.LEFT_CURLY_BRACKET) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 156
                self.class_body_unit()
                self.state = 161
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
        self.enterRule(localctx, 8, self.RULE_class_body_unit)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
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
        self.enterRule(localctx, 10, self.RULE_super_class_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(D96Parser.COLON)
            self.state = 168
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
        self.enterRule(localctx, 12, self.RULE_program_class_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(D96Parser.K_CLASS)
            self.state = 171
            self.match(D96Parser.T__0)
            self.state = 172
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 173
            self.program_class_body()
            self.state = 174
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
        self.enterRule(localctx, 14, self.RULE_program_class_body)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.main_method_declaration()
                self.state = 177
                self.class_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.class_body()
                self.state = 180
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
        self.enterRule(localctx, 16, self.RULE_main_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(D96Parser.K_MAIN)
            self.state = 185
            self.match(D96Parser.LEFT_PAREN)
            self.state = 186
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 187
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
        self.enterRule(localctx, 18, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(D96Parser.IDENTIFIER)
                self.state = 190
                self.match(D96Parser.LEFT_PAREN)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 191
                    self.parameter_list()


                self.state = 194
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 195
                self.block_statement()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.constructor()
                pass
            elif token in [D96Parser.K_DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
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
        self.enterRule(localctx, 20, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(D96Parser.K_CONSTRUCTOR)
            self.state = 201
            self.match(D96Parser.LEFT_PAREN)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDENTIFIER:
                self.state = 202
                self.parameter_list()


            self.state = 205
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 206
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
        self.enterRule(localctx, 22, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(D96Parser.K_DESTRUCTOR)
            self.state = 209
            self.match(D96Parser.LEFT_PAREN)
            self.state = 210
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 211
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
        self.enterRule(localctx, 24, self.RULE_parameter_list)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.parameter()
                self.state = 215
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
        self.enterRule(localctx, 26, self.RULE_parameter_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 219
                    self.match(D96Parser.SEMI_COLON)
                    self.state = 220
                    self.parameter()
                    self.state = 221
                    self.parameter_list_tail() 
                self.state = 227
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.identifier_list()
            self.state = 229
            self.match(D96Parser.COLON)
            self.state = 230
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
        self.enterRule(localctx, 30, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER]:
                self.state = 233
                self.identifier_list()
                pass
            elif token in [D96Parser.DOLAR_IDENTIFIER]:
                self.state = 234
                self.dolar_identifier_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 237
            self.match(D96Parser.COLON)
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 238
                self.array_type()
                pass

            elif la_ == 2:
                self.state = 239
                self.primitive_type()
                pass


            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 242
                self.match(D96Parser.OP_ASSIGN)
                self.state = 243
                self.expression_list()


            self.state = 246
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
        self.enterRule(localctx, 32, self.RULE_identifier_list)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(D96Parser.IDENTIFIER)
                self.state = 250
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
        self.enterRule(localctx, 34, self.RULE_dolar_identifier_list)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 255
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
        self.enterRule(localctx, 36, self.RULE_identifier_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 258
                self.match(D96Parser.COMMA)
                self.state = 259
                self.match(D96Parser.IDENTIFIER)
                self.state = 264
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
        self.enterRule(localctx, 38, self.RULE_dolar_identifier_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 265
                self.match(D96Parser.COMMA)
                self.state = 266
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 271
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
        self.enterRule(localctx, 40, self.RULE_expression_list)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.expression(0)
                self.state = 274
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
        self.enterRule(localctx, 42, self.RULE_expression_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 278
                    self.match(D96Parser.COMMA)
                    self.state = 279
                    self.expression(0)
                    self.state = 280
                    self.expression_list_tail() 
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 44, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.expression(0)
            self.state = 288
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
        self.enterRule(localctx, 46, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 291
            self.expression(0)
            self.state = 292
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 293
                    self.index_operator() 
                self.state = 298
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
        self.enterRule(localctx, 48, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
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



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.relational_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 304
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 305
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_STRING_CONCATENATION or _la==D96Parser.OP_TWO_SAME_STRING):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 306
                    self.relational_expr(0) 
                self.state = 311
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



    def relational_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Relational_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_relational_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.and_or_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Relational_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr)
                    self.state = 315
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 316
                    self.relational_operator()
                    self.state = 317
                    self.and_or_expr(0) 
                self.state = 323
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_and_or_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.add_sub_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 332
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.And_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_or_expr)
                    self.state = 327
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 328
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_LOGICAL_OR or _la==D96Parser.OP_LOGICAL_AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 329
                    self.add_sub_expr(0) 
                self.state = 334
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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_add_sub_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.mul_add_mol_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 343
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Add_sub_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expr)
                    self.state = 338
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 339
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_ADDTION or _la==D96Parser.OP_SUBTRACTION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 340
                    self.mul_add_mol_expr(0) 
                self.state = 345
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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_mul_add_mol_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Mul_add_mol_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_add_mol_expr)
                    self.state = 349
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 350
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MODULO) | (1 << D96Parser.OP_MULTIPLICATION) | (1 << D96Parser.OP_DIVISION))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 351
                    self.not_expr() 
                self.state = 356
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
        self.enterRule(localctx, 60, self.RULE_not_expr)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(D96Parser.OP_LOGICAL_NOT)
                self.state = 358
                self.not_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.OP_SUBTRACTION, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
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
        self.enterRule(localctx, 62, self.RULE_sign_expr)
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUBTRACTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(D96Parser.OP_SUBTRACTION)
                self.state = 363
                self.sign_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
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

        def instance_attribute_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_attribute_accessContext,0)


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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_index_operator_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.instance_attribute_access(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operator_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operator_expr)
                    self.state = 370
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 371
                    self.index_operator() 
                self.state = 376
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



    def instance_attribute_access(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Instance_attribute_accessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_instance_attribute_access, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.instace_method_invocation(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 385
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Instance_attribute_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_attribute_access)
                    self.state = 380
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 381
                    self.match(D96Parser.DOT)
                    self.state = 382
                    self.match(D96Parser.IDENTIFIER) 
                self.state = 387
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_expr(self):
            return self.getTypedRuleContext(D96Parser.Atom_exprContext,0)


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



    def instace_method_invocation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Instace_method_invocationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_instace_method_invocation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.atom_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Instace_method_invocationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instace_method_invocation)
                    self.state = 391
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 392
                    self.match(D96Parser.DOUBLE_COLON)
                    self.state = 393
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 394
                    self.match(D96Parser.LEFT_PAREN)
                    self.state = 396
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                        self.state = 395
                        self.expression_list()


                    self.state = 398
                    self.match(D96Parser.RIGHT_PAREN) 
                self.state = 403
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




    def static_method_invocation(self):

        localctx = D96Parser.Static_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_static_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(D96Parser.IDENTIFIER)
            self.state = 405
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 406
            self.match(D96Parser.LEFT_PAREN)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 407
                self.expression_list()


            self.state = 410
            self.match(D96Parser.RIGHT_PAREN)
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
        self.enterRule(localctx, 72, self.RULE_static_attribute_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(D96Parser.IDENTIFIER)
            self.state = 413
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 414
            self.match(D96Parser.IDENTIFIER)
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

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_object_creation




    def object_creation(self):

        localctx = D96Parser.Object_creationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_object_creation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(D96Parser.K_NEW)
            self.state = 417
            self.match(D96Parser.IDENTIFIER)
            self.state = 418
            self.match(D96Parser.LEFT_PAREN)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
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


        def static_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocationContext,0)


        def static_attribute_access(self):
            return self.getTypedRuleContext(D96Parser.Static_attribute_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_atom_expr




    def atom_expr(self):

        localctx = D96Parser.Atom_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_atom_expr)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 426
                self.match(D96Parser.LEFT_PAREN)
                self.state = 427
                self.expression(0)
                self.state = 428
                self.match(D96Parser.RIGHT_PAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 430
                self.function_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 431
                self.static_method_invocation()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 432
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




    def function_call(self):

        localctx = D96Parser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(D96Parser.IDENTIFIER)
            self.state = 436
            self.match(D96Parser.LEFT_PAREN)
            self.state = 438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 437
                self.expression_list()


            self.state = 440
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
        self.enterRule(localctx, 80, self.RULE_var_val_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 443
            self.identifier_list()
            self.state = 444
            self.match(D96Parser.COLON)
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 445
                self.array_type()
                pass

            elif la_ == 2:
                self.state = 446
                self.primitive_type()
                pass


            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 449
                self.match(D96Parser.OP_ASSIGN)
                self.state = 450
                self.expression_list()


            self.state = 453
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
        self.enterRule(localctx, 82, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 455
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 456
                self.element_expression()
                pass


            self.state = 459
            self.match(D96Parser.OP_ASSIGN)
            self.state = 460
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
        self.enterRule(localctx, 84, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.if_part()
            self.state = 463
            self.else_if_part()
            self.state = 464
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
        self.enterRule(localctx, 86, self.RULE_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(D96Parser.K_IF)
            self.state = 467
            self.match(D96Parser.LEFT_PAREN)
            self.state = 468
            self.expression(0)
            self.state = 469
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 470
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
        self.enterRule(localctx, 88, self.RULE_else_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(D96Parser.K_ELSE_IF)
            self.state = 473
            self.match(D96Parser.LEFT_PAREN)
            self.state = 474
            self.expression(0)
            self.state = 475
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 476
            self.block_statement()
            self.state = 481
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 478
                    self.else_if_part() 
                self.state = 483
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        self.enterRule(localctx, 90, self.RULE_else_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ELSE:
                self.state = 484
                self.match(D96Parser.K_ELSE)
                self.state = 485
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
        self.enterRule(localctx, 92, self.RULE_for_in_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(D96Parser.K_FOR_EACH)
            self.state = 489
            self.match(D96Parser.LEFT_PAREN)
            self.state = 490
            self.loop_part()
            self.state = 491
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 492
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
        self.enterRule(localctx, 94, self.RULE_loop_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(D96Parser.IDENTIFIER)
            self.state = 495
            self.match(D96Parser.K_IN)
            self.state = 496
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 497
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 498
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_BY:
                self.state = 499
                self.match(D96Parser.K_BY)
                self.state = 500
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
        self.enterRule(localctx, 96, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(D96Parser.K_BREAK)
            self.state = 504
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
        self.enterRule(localctx, 98, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(D96Parser.K_CONTINUE)
            self.state = 507
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
        self.enterRule(localctx, 100, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.match(D96Parser.K_RETURN)
            self.state = 510
            self.expression(0)
            self.state = 511
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
        self.enterRule(localctx, 102, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(D96Parser.IDENTIFIER)
            self.state = 514
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 515
            self.match(D96Parser.DOLAR_IDENTIFIER)
            self.state = 516
            self.match(D96Parser.LEFT_PAREN)
            self.state = 517
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 518
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
        self.enterRule(localctx, 104, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 522
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_BREAK) | (1 << D96Parser.K_CONTINUE) | (1 << D96Parser.K_IF) | (1 << D96Parser.K_FOR_EACH) | (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_RETURN) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.LEFT_CURLY_BRACKET) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 521
                self.statement()


            self.state = 524
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
        self.enterRule(localctx, 106, self.RULE_statement)
        try:
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.var_val_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 528
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 529
                self.for_in_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 530
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 531
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 532
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 533
                self.method_invocation_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 534
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
        self.enterRule(localctx, 108, self.RULE_literal)
        try:
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.match(D96Parser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 538
                self.match(D96Parser.FLOAT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 539
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 540
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 541
                self.indexed_array()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 542
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
        self.enterRule(localctx, 110, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(D96Parser.K_ARRAY)
            self.state = 546
            self.match(D96Parser.LEFT_PAREN)
            self.state = 581
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RIGHT_PAREN, D96Parser.INTEGER_LITERAL]:
                self.state = 555
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.INTEGER_LITERAL:
                    self.state = 547
                    self.match(D96Parser.INTEGER_LITERAL)
                    self.state = 552
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.COMMA:
                        self.state = 548
                        self.match(D96Parser.COMMA)
                        self.state = 549
                        self.match(D96Parser.INTEGER_LITERAL)
                        self.state = 554
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.state = 557
                self.match(D96Parser.FLOAT_LITERAL)
                self.state = 562
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 558
                    self.match(D96Parser.COMMA)
                    self.state = 559
                    self.match(D96Parser.FLOAT_LITERAL)
                    self.state = 564
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.state = 565
                self.match(D96Parser.BOOLEAN_LITERAL)
                self.state = 570
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 566
                    self.match(D96Parser.COMMA)
                    self.state = 567
                    self.match(D96Parser.BOOLEAN_LITERAL)
                    self.state = 572
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.state = 573
                self.match(D96Parser.STRING_LITERAL)
                self.state = 578
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 574
                    self.match(D96Parser.COMMA)
                    self.state = 575
                    self.match(D96Parser.STRING_LITERAL)
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
        self.enterRule(localctx, 112, self.RULE_multi_dimentional_array)
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
        self.enterRule(localctx, 114, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
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
        self.enterRule(localctx, 116, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
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
        self.enterRule(localctx, 118, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.match(D96Parser.K_ARRAY)
            self.state = 604
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 605
            self.primitive_type()
            self.state = 606
            self.match(D96Parser.COMMA)
            self.state = 607
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 608
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
        self.enterRule(localctx, 120, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 610
            self.match(D96Parser.K_NEW)
            self.state = 611
            self.match(D96Parser.IDENTIFIER)
            self.state = 612
            self.match(D96Parser.LEFT_PAREN)
            self.state = 613
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
        self._predicates[25] = self.expression_sempred
        self._predicates[26] = self.relational_expr_sempred
        self._predicates[27] = self.and_or_expr_sempred
        self._predicates[28] = self.add_sub_expr_sempred
        self._predicates[29] = self.mul_add_mol_expr_sempred
        self._predicates[32] = self.index_operator_expr_sempred
        self._predicates[33] = self.instance_attribute_access_sempred
        self._predicates[34] = self.instace_method_invocation_sempred
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
         




