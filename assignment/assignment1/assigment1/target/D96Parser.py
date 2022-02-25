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
        buf.write("\u0234\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\6\2b\n\2\r\2\16\2c\3\2\3\2\3\3\3\3")
        buf.write("\5\3j\n\3\3\4\3\4\3\4\3\4\5\4p\n\4\3\4\3\4\7\4t\n\4\f")
        buf.write("\4\16\4w\13\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\177\n\5\3\5")
        buf.write("\3\5\7\5\u0083\n\5\f\5\16\5\u0086\13\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\5\6\u008d\n\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u0096")
        buf.write("\n\b\3\t\3\t\3\t\5\t\u009b\n\t\3\t\3\t\3\t\3\t\5\t\u00a1")
        buf.write("\n\t\3\n\3\n\3\n\5\n\u00a6\n\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\7\f\u00b3\n\f\f\f\16\f\u00b6")
        buf.write("\13\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\5\16\u00bf\n\16\3")
        buf.write("\17\3\17\3\17\3\17\7\17\u00c5\n\17\f\17\16\17\u00c8\13")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00d0\n\17\f\17")
        buf.write("\16\17\u00d3\13\17\5\17\u00d5\n\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\7\20\u00dc\n\20\f\20\16\20\u00df\13\20\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\6\22\u00e7\n\22\r\22\16\22\u00e8")
        buf.write("\5\22\u00eb\n\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\6")
        buf.write("\24\u00f4\n\24\r\24\16\24\u00f5\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\5\26\u00ff\n\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u0106\n\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u010e")
        buf.write("\n\30\f\30\16\30\u0111\13\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\7\31\u0119\n\31\f\31\16\31\u011c\13\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\7\32\u0124\n\32\f\32\16\32\u0127")
        buf.write("\13\32\3\33\3\33\3\33\5\33\u012c\n\33\3\34\3\34\3\34\5")
        buf.write("\34\u0131\n\34\3\35\3\35\3\35\3\35\5\35\u0137\n\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0141\n\36\3")
        buf.write("\36\5\36\u0144\n\36\7\36\u0146\n\36\f\36\16\36\u0149\13")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0153")
        buf.write("\n\37\3\37\5\37\u0156\n\37\7\37\u0158\n\37\f\37\16\37")
        buf.write("\u015b\13\37\3 \3 \3 \3 \5 \u0161\n \3 \3 \5 \u0165\n")
        buf.write(" \3!\3!\3!\3!\3!\3!\3!\3!\5!\u016f\n!\3\"\3\"\3\"\3\"")
        buf.write("\7\"\u0175\n\"\f\"\16\"\u0178\13\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\7\"\u0180\n\"\f\"\16\"\u0183\13\"\5\"\u0185\n\"\3")
        buf.write("\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0193\n#\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5")
        buf.write("%\u01a8\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01b3\n&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\5)\u01c0\n)\3)\3)\3*\3")
        buf.write("*\3*\3+\3+\7+\u01c9\n+\f+\16+\u01cc\13+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\5,\u01d9\n,\3-\3-\3-\3-\3-\3-\3-\5")
        buf.write("-\u01e2\n-\3.\3.\3.\3.\3.\7.\u01e9\n.\f.\16.\u01ec\13")
        buf.write(".\5.\u01ee\n.\3.\3.\3.\7.\u01f3\n.\f.\16.\u01f6\13.\3")
        buf.write(".\3.\3.\7.\u01fb\n.\f.\16.\u01fe\13.\3.\3.\3.\7.\u0203")
        buf.write("\n.\f.\16.\u0206\13.\3.\3.\3.\7.\u020b\n.\f.\16.\u020e")
        buf.write("\13.\3.\3.\3.\7.\u0213\n.\f.\16.\u0216\13.\5.\u0218\n")
        buf.write(".\3.\3.\3/\3/\3/\3/\3/\7/\u0221\n/\f/\16/\u0224\13/\5")
        buf.write("/\u0226\n/\3/\3/\3\60\3\60\3\60\3\60\5\60\u022e\n\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\2\7.\60\62:<\61\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^\2\13\4\2\17\17;;\4\2\17\17;<\3\2\22\23\3")
        buf.write("\2;<\4\2\34\35#&\3\2\'(\3\2\32\33\3\2\37 \4\2\36\36!\"")
        buf.write("\2\u0257\2a\3\2\2\2\4i\3\2\2\2\6k\3\2\2\2\bz\3\2\2\2\n")
        buf.write("\u008c\3\2\2\2\f\u008e\3\2\2\2\16\u0095\3\2\2\2\20\u00a0")
        buf.write("\3\2\2\2\22\u00a2\3\2\2\2\24\u00aa\3\2\2\2\26\u00af\3")
        buf.write("\2\2\2\30\u00b7\3\2\2\2\32\u00be\3\2\2\2\34\u00c0\3\2")
        buf.write("\2\2\36\u00d8\3\2\2\2 \u00e0\3\2\2\2\"\u00ea\3\2\2\2$")
        buf.write("\u00ec\3\2\2\2&\u00f3\3\2\2\2(\u00f7\3\2\2\2*\u00fe\3")
        buf.write("\2\2\2,\u0105\3\2\2\2.\u0107\3\2\2\2\60\u0112\3\2\2\2")
        buf.write("\62\u011d\3\2\2\2\64\u012b\3\2\2\2\66\u0130\3\2\2\28\u0136")
        buf.write("\3\2\2\2:\u0138\3\2\2\2<\u014a\3\2\2\2>\u0164\3\2\2\2")
        buf.write("@\u016e\3\2\2\2B\u0170\3\2\2\2D\u0192\3\2\2\2F\u0194\3")
        buf.write("\2\2\2H\u01a7\3\2\2\2J\u01a9\3\2\2\2L\u01b7\3\2\2\2N\u01ba")
        buf.write("\3\2\2\2P\u01bd\3\2\2\2R\u01c3\3\2\2\2T\u01c6\3\2\2\2")
        buf.write("V\u01d8\3\2\2\2X\u01e1\3\2\2\2Z\u01e3\3\2\2\2\\\u021b")
        buf.write("\3\2\2\2^\u0229\3\2\2\2`b\5\4\3\2a`\3\2\2\2bc\3\2\2\2")
        buf.write("ca\3\2\2\2cd\3\2\2\2de\3\2\2\2ef\7\2\2\3f\3\3\2\2\2gj")
        buf.write("\5\6\4\2hj\5\b\5\2ig\3\2\2\2ih\3\2\2\2j\5\3\2\2\2kl\7")
        buf.write("\21\2\2lo\t\2\2\2mn\7\60\2\2np\7;\2\2om\3\2\2\2op\3\2")
        buf.write("\2\2pq\3\2\2\2qu\7\63\2\2rt\5\16\b\2sr\3\2\2\2tw\3\2\2")
        buf.write("\2us\3\2\2\2uv\3\2\2\2vx\3\2\2\2wu\3\2\2\2xy\7\64\2\2")
        buf.write("y\7\3\2\2\2z{\7\21\2\2{~\7\20\2\2|}\7\60\2\2}\177\7;\2")
        buf.write("\2~|\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2\u0080\u0084")
        buf.write("\7\63\2\2\u0081\u0083\5\n\6\2\u0082\u0081\3\2\2\2\u0083")
        buf.write("\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2")
        buf.write("\u0085\u0087\3\2\2\2\u0086\u0084\3\2\2\2\u0087\u0088\7")
        buf.write("\64\2\2\u0088\t\3\2\2\2\u0089\u008d\5\34\17\2\u008a\u008d")
        buf.write("\5\f\7\2\u008b\u008d\5\20\t\2\u008c\u0089\3\2\2\2\u008c")
        buf.write("\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d\13\3\2\2\2\u008e")
        buf.write("\u008f\7\17\2\2\u008f\u0090\7)\2\2\u0090\u0091\7*\2\2")
        buf.write("\u0091\u0092\5T+\2\u0092\r\3\2\2\2\u0093\u0096\5\34\17")
        buf.write("\2\u0094\u0096\5\20\t\2\u0095\u0093\3\2\2\2\u0095\u0094")
        buf.write("\3\2\2\2\u0096\17\3\2\2\2\u0097\u0098\t\3\2\2\u0098\u009a")
        buf.write("\7)\2\2\u0099\u009b\5\26\f\2\u009a\u0099\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\7*\2\2")
        buf.write("\u009d\u00a1\5T+\2\u009e\u00a1\5\22\n\2\u009f\u00a1\5")
        buf.write("\24\13\2\u00a0\u0097\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a1\21\3\2\2\2\u00a2\u00a3\7\24\2\2\u00a3")
        buf.write("\u00a5\7)\2\2\u00a4\u00a6\5\26\f\2\u00a5\u00a4\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\7")
        buf.write("*\2\2\u00a8\u00a9\5T+\2\u00a9\23\3\2\2\2\u00aa\u00ab\7")
        buf.write("\25\2\2\u00ab\u00ac\7)\2\2\u00ac\u00ad\7*\2\2\u00ad\u00ae")
        buf.write("\5T+\2\u00ae\25\3\2\2\2\u00af\u00b4\5\30\r\2\u00b0\u00b1")
        buf.write("\7\62\2\2\u00b1\u00b3\5\30\r\2\u00b2\u00b0\3\2\2\2\u00b3")
        buf.write("\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5\27\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b8\5\36")
        buf.write("\20\2\u00b8\u00b9\7\60\2\2\u00b9\u00ba\5\32\16\2\u00ba")
        buf.write("\31\3\2\2\2\u00bb\u00bf\7:\2\2\u00bc\u00bf\7;\2\2\u00bd")
        buf.write("\u00bf\5^\60\2\u00be\u00bb\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00be\u00bd\3\2\2\2\u00bf\33\3\2\2\2\u00c0\u00c1\t\4")
        buf.write("\2\2\u00c1\u00c6\5 \21\2\u00c2\u00c3\7/\2\2\u00c3\u00c5")
        buf.write("\5 \21\2\u00c4\u00c2\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2")
        buf.write("\u00c8\u00c6\3\2\2\2\u00c9\u00ca\7\60\2\2\u00ca\u00d4")
        buf.write("\5\32\16\2\u00cb\u00cc\7\30\2\2\u00cc\u00d1\5*\26\2\u00cd")
        buf.write("\u00ce\7/\2\2\u00ce\u00d0\5*\26\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00d0\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3")
        buf.write("\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00cb")
        buf.write("\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write("\u00d7\7\62\2\2\u00d7\35\3\2\2\2\u00d8\u00dd\7;\2\2\u00d9")
        buf.write("\u00da\7/\2\2\u00da\u00dc\7;\2\2\u00db\u00d9\3\2\2\2\u00dc")
        buf.write("\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de\37\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\t\5")
        buf.write("\2\2\u00e1!\3\2\2\2\u00e2\u00eb\5*\26\2\u00e3\u00e6\5")
        buf.write("*\26\2\u00e4\u00e5\7/\2\2\u00e5\u00e7\5*\26\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00eb\3\2\2\2\u00ea\u00e2\3\2\2\2")
        buf.write("\u00ea\u00e3\3\2\2\2\u00eb#\3\2\2\2\u00ec\u00ed\5*\26")
        buf.write("\2\u00ed\u00ee\5&\24\2\u00ee%\3\2\2\2\u00ef\u00f0\7+\2")
        buf.write("\2\u00f0\u00f1\5*\26\2\u00f1\u00f2\7,\2\2\u00f2\u00f4")
        buf.write("\3\2\2\2\u00f3\u00ef\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\'\3\2\2\2\u00f7")
        buf.write("\u00f8\t\6\2\2\u00f8)\3\2\2\2\u00f9\u00fa\5,\27\2\u00fa")
        buf.write("\u00fb\t\7\2\2\u00fb\u00fc\5,\27\2\u00fc\u00ff\3\2\2\2")
        buf.write("\u00fd\u00ff\5,\27\2\u00fe\u00f9\3\2\2\2\u00fe\u00fd\3")
        buf.write("\2\2\2\u00ff+\3\2\2\2\u0100\u0101\5.\30\2\u0101\u0102")
        buf.write("\5(\25\2\u0102\u0103\5.\30\2\u0103\u0106\3\2\2\2\u0104")
        buf.write("\u0106\5.\30\2\u0105\u0100\3\2\2\2\u0105\u0104\3\2\2\2")
        buf.write("\u0106-\3\2\2\2\u0107\u0108\b\30\1\2\u0108\u0109\5\60")
        buf.write("\31\2\u0109\u010f\3\2\2\2\u010a\u010b\f\4\2\2\u010b\u010c")
        buf.write("\t\b\2\2\u010c\u010e\5\60\31\2\u010d\u010a\3\2\2\2\u010e")
        buf.write("\u0111\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110/\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0113\b\31\1")
        buf.write("\2\u0113\u0114\5\62\32\2\u0114\u011a\3\2\2\2\u0115\u0116")
        buf.write("\f\4\2\2\u0116\u0117\t\t\2\2\u0117\u0119\5\62\32\2\u0118")
        buf.write("\u0115\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2")
        buf.write("\u011a\u011b\3\2\2\2\u011b\61\3\2\2\2\u011c\u011a\3\2")
        buf.write("\2\2\u011d\u011e\b\32\1\2\u011e\u011f\5\64\33\2\u011f")
        buf.write("\u0125\3\2\2\2\u0120\u0121\f\4\2\2\u0121\u0122\t\n\2\2")
        buf.write("\u0122\u0124\5\64\33\2\u0123\u0120\3\2\2\2\u0124\u0127")
        buf.write("\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("\63\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129\7\31\2\2\u0129")
        buf.write("\u012c\5\64\33\2\u012a\u012c\5\66\34\2\u012b\u0128\3\2")
        buf.write("\2\2\u012b\u012a\3\2\2\2\u012c\65\3\2\2\2\u012d\u012e")
        buf.write("\t\t\2\2\u012e\u0131\5\66\34\2\u012f\u0131\58\35\2\u0130")
        buf.write("\u012d\3\2\2\2\u0130\u012f\3\2\2\2\u0131\67\3\2\2\2\u0132")
        buf.write("\u0133\5:\36\2\u0133\u0134\5&\24\2\u0134\u0137\3\2\2\2")
        buf.write("\u0135\u0137\5:\36\2\u0136\u0132\3\2\2\2\u0136\u0135\3")
        buf.write("\2\2\2\u01379\3\2\2\2\u0138\u0139\b\36\1\2\u0139\u013a")
        buf.write("\5<\37\2\u013a\u0147\3\2\2\2\u013b\u013c\f\4\2\2\u013c")
        buf.write("\u013d\7-\2\2\u013d\u0143\7;\2\2\u013e\u0140\7)\2\2\u013f")
        buf.write("\u0141\5\"\22\2\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2")
        buf.write("\2\u0141\u0142\3\2\2\2\u0142\u0144\7*\2\2\u0143\u013e")
        buf.write("\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0146\3\2\2\2\u0145")
        buf.write("\u013b\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3\2\2\2")
        buf.write("\u0147\u0148\3\2\2\2\u0148;\3\2\2\2\u0149\u0147\3\2\2")
        buf.write("\2\u014a\u014b\b\37\1\2\u014b\u014c\5> \2\u014c\u0159")
        buf.write("\3\2\2\2\u014d\u014e\f\4\2\2\u014e\u014f\7\61\2\2\u014f")
        buf.write("\u0155\7<\2\2\u0150\u0152\7)\2\2\u0151\u0153\5\"\22\2")
        buf.write("\u0152\u0151\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0154\3")
        buf.write("\2\2\2\u0154\u0156\7*\2\2\u0155\u0150\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\u0158\3\2\2\2\u0157\u014d\3\2\2\2\u0158")
        buf.write("\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2")
        buf.write("\u015a=\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015d\7\26\2")
        buf.write("\2\u015d\u015e\7;\2\2\u015e\u0160\7)\2\2\u015f\u0161\5")
        buf.write("\"\22\2\u0160\u015f\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162\u0165\7*\2\2\u0163\u0165\5@!\2\u0164")
        buf.write("\u015c\3\2\2\2\u0164\u0163\3\2\2\2\u0165?\3\2\2\2\u0166")
        buf.write("\u016f\5X-\2\u0167\u016f\7\r\2\2\u0168\u016f\7\16\2\2")
        buf.write("\u0169\u016f\7;\2\2\u016a\u016b\7)\2\2\u016b\u016c\5*")
        buf.write("\26\2\u016c\u016d\7*\2\2\u016d\u016f\3\2\2\2\u016e\u0166")
        buf.write("\3\2\2\2\u016e\u0167\3\2\2\2\u016e\u0168\3\2\2\2\u016e")
        buf.write("\u0169\3\2\2\2\u016e\u016a\3\2\2\2\u016fA\3\2\2\2\u0170")
        buf.write("\u0171\t\4\2\2\u0171\u0176\7;\2\2\u0172\u0173\7/\2\2\u0173")
        buf.write("\u0175\7;\2\2\u0174\u0172\3\2\2\2\u0175\u0178\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0179\3")
        buf.write("\2\2\2\u0178\u0176\3\2\2\2\u0179\u017a\7\60\2\2\u017a")
        buf.write("\u0184\5\32\16\2\u017b\u017c\7\30\2\2\u017c\u0181\5*\26")
        buf.write("\2\u017d\u017e\7/\2\2\u017e\u0180\5*\26\2\u017f\u017d")
        buf.write("\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0181")
        buf.write("\u0182\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0184\u017b\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\3")
        buf.write("\2\2\2\u0186\u0187\7\62\2\2\u0187C\3\2\2\2\u0188\u0189")
        buf.write("\5:\36\2\u0189\u018a\7-\2\2\u018a\u018b\7;\2\2\u018b\u0193")
        buf.write("\3\2\2\2\u018c\u018d\5:\36\2\u018d\u018e\7\61\2\2\u018e")
        buf.write("\u018f\7<\2\2\u018f\u0193\3\2\2\2\u0190\u0193\7;\2\2\u0191")
        buf.write("\u0193\5$\23\2\u0192\u0188\3\2\2\2\u0192\u018c\3\2\2\2")
        buf.write("\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193E\3\2\2")
        buf.write("\2\u0194\u0195\5D#\2\u0195\u0196\7\30\2\2\u0196\u0197")
        buf.write("\5*\26\2\u0197\u0198\7\62\2\2\u0198G\3\2\2\2\u0199\u019a")
        buf.write("\7\6\2\2\u019a\u019b\7)\2\2\u019b\u019c\5*\26\2\u019c")
        buf.write("\u019d\7*\2\2\u019d\u019e\5T+\2\u019e\u01a8\3\2\2\2\u019f")
        buf.write("\u01a0\7\7\2\2\u01a0\u01a1\7)\2\2\u01a1\u01a2\5*\26\2")
        buf.write("\u01a2\u01a3\7*\2\2\u01a3\u01a4\5T+\2\u01a4\u01a8\3\2")
        buf.write("\2\2\u01a5\u01a6\7\b\2\2\u01a6\u01a8\5T+\2\u01a7\u0199")
        buf.write("\3\2\2\2\u01a7\u019f\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8")
        buf.write("I\3\2\2\2\u01a9\u01aa\7\t\2\2\u01aa\u01ab\7)\2\2\u01ab")
        buf.write("\u01ac\7;\2\2\u01ac\u01ad\7\13\2\2\u01ad\u01ae\5*\26\2")
        buf.write("\u01ae\u01af\7.\2\2\u01af\u01b2\5*\26\2\u01b0\u01b1\7")
        buf.write("\27\2\2\u01b1\u01b3\5*\26\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\7*\2\2")
        buf.write("\u01b5\u01b6\5T+\2\u01b6K\3\2\2\2\u01b7\u01b8\7\4\2\2")
        buf.write("\u01b8\u01b9\7\62\2\2\u01b9M\3\2\2\2\u01ba\u01bb\7\5\2")
        buf.write("\2\u01bb\u01bc\7\62\2\2\u01bcO\3\2\2\2\u01bd\u01bf\7\f")
        buf.write("\2\2\u01be\u01c0\5*\26\2\u01bf\u01be\3\2\2\2\u01bf\u01c0")
        buf.write("\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\7\62\2\2\u01c2")
        buf.write("Q\3\2\2\2\u01c3\u01c4\5:\36\2\u01c4\u01c5\7\62\2\2\u01c5")
        buf.write("S\3\2\2\2\u01c6\u01ca\7\63\2\2\u01c7\u01c9\5V,\2\u01c8")
        buf.write("\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01ca\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3")
        buf.write("\2\2\2\u01cd\u01ce\7\64\2\2\u01ceU\3\2\2\2\u01cf\u01d9")
        buf.write("\5B\"\2\u01d0\u01d9\5F$\2\u01d1\u01d9\5H%\2\u01d2\u01d9")
        buf.write("\5J&\2\u01d3\u01d9\5L\'\2\u01d4\u01d9\5N(\2\u01d5\u01d9")
        buf.write("\5P)\2\u01d6\u01d9\5R*\2\u01d7\u01d9\5T+\2\u01d8\u01cf")
        buf.write("\3\2\2\2\u01d8\u01d0\3\2\2\2\u01d8\u01d1\3\2\2\2\u01d8")
        buf.write("\u01d2\3\2\2\2\u01d8\u01d3\3\2\2\2\u01d8\u01d4\3\2\2\2")
        buf.write("\u01d8\u01d5\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d7\3")
        buf.write("\2\2\2\u01d9W\3\2\2\2\u01da\u01e2\7\66\2\2\u01db\u01e2")
        buf.write("\7\65\2\2\u01dc\u01e2\7\67\2\2\u01dd\u01e2\78\2\2\u01de")
        buf.write("\u01e2\79\2\2\u01df\u01e2\5Z.\2\u01e0\u01e2\5\\/\2\u01e1")
        buf.write("\u01da\3\2\2\2\u01e1\u01db\3\2\2\2\u01e1\u01dc\3\2\2\2")
        buf.write("\u01e1\u01dd\3\2\2\2\u01e1\u01de\3\2\2\2\u01e1\u01df\3")
        buf.write("\2\2\2\u01e1\u01e0\3\2\2\2\u01e2Y\3\2\2\2\u01e3\u01e4")
        buf.write("\7\n\2\2\u01e4\u0217\7)\2\2\u01e5\u01ea\7\66\2\2\u01e6")
        buf.write("\u01e7\7/\2\2\u01e7\u01e9\7\66\2\2\u01e8\u01e6\3\2\2\2")
        buf.write("\u01e9\u01ec\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3")
        buf.write("\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01e5")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u0218\3\2\2\2\u01ef")
        buf.write("\u01f4\7\65\2\2\u01f0\u01f1\7/\2\2\u01f1\u01f3\7\65\2")
        buf.write("\2\u01f2\u01f0\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2")
        buf.write("\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u0218\3\2\2\2\u01f6")
        buf.write("\u01f4\3\2\2\2\u01f7\u01fc\7\67\2\2\u01f8\u01f9\7/\2\2")
        buf.write("\u01f9\u01fb\7\67\2\2\u01fa\u01f8\3\2\2\2\u01fb\u01fe")
        buf.write("\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd")
        buf.write("\u0218\3\2\2\2\u01fe\u01fc\3\2\2\2\u01ff\u0204\78\2\2")
        buf.write("\u0200\u0201\7/\2\2\u0201\u0203\78\2\2\u0202\u0200\3\2")
        buf.write("\2\2\u0203\u0206\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205")
        buf.write("\3\2\2\2\u0205\u0218\3\2\2\2\u0206\u0204\3\2\2\2\u0207")
        buf.write("\u020c\79\2\2\u0208\u0209\7/\2\2\u0209\u020b\79\2\2\u020a")
        buf.write("\u0208\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020a\3\2\2\2")
        buf.write("\u020c\u020d\3\2\2\2\u020d\u0218\3\2\2\2\u020e\u020c\3")
        buf.write("\2\2\2\u020f\u0214\5Z.\2\u0210\u0211\7/\2\2\u0211\u0213")
        buf.write("\5Z.\2\u0212\u0210\3\2\2\2\u0213\u0216\3\2\2\2\u0214\u0212")
        buf.write("\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0218\3\2\2\2\u0216")
        buf.write("\u0214\3\2\2\2\u0217\u01ed\3\2\2\2\u0217\u01ef\3\2\2\2")
        buf.write("\u0217\u01f7\3\2\2\2\u0217\u01ff\3\2\2\2\u0217\u0207\3")
        buf.write("\2\2\2\u0217\u020f\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021a")
        buf.write("\7*\2\2\u021a[\3\2\2\2\u021b\u021c\7\n\2\2\u021c\u0225")
        buf.write("\7)\2\2\u021d\u0222\5Z.\2\u021e\u021f\7/\2\2\u021f\u0221")
        buf.write("\5Z.\2\u0220\u021e\3\2\2\2\u0221\u0224\3\2\2\2\u0222\u0220")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0226\3\2\2\2\u0224")
        buf.write("\u0222\3\2\2\2\u0225\u021d\3\2\2\2\u0225\u0226\3\2\2\2")
        buf.write("\u0226\u0227\3\2\2\2\u0227\u0228\7*\2\2\u0228]\3\2\2\2")
        buf.write("\u0229\u022a\7\n\2\2\u022a\u022d\7+\2\2\u022b\u022e\7")
        buf.write(":\2\2\u022c\u022e\5^\60\2\u022d\u022b\3\2\2\2\u022d\u022c")
        buf.write("\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\7/\2\2\u0230")
        buf.write("\u0231\7\65\2\2\u0231\u0232\7,\2\2\u0232_\3\2\2\2<cio")
        buf.write("u~\u0084\u008c\u0095\u009a\u00a0\u00a5\u00b4\u00be\u00c6")
        buf.write("\u00d1\u00d4\u00dd\u00e8\u00ea\u00f5\u00fe\u0105\u010f")
        buf.write("\u011a\u0125\u012b\u0130\u0136\u0140\u0143\u0147\u0152")
        buf.write("\u0155\u0159\u0160\u0164\u016e\u0176\u0181\u0184\u0192")
        buf.write("\u01a7\u01b2\u01bf\u01ca\u01d8\u01e1\u01ea\u01ed\u01f4")
        buf.write("\u01fc\u0204\u020c\u0214\u0217\u0222\u0225\u022d")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Array'", 
                     "'In'", "'Return'", "'Null'", "'Self'", "'main'", "'Program'", 
                     "'Class'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "'='", "'!'", "'||'", "'&&'", "'=='", 
                     "'!='", "'%'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", 
                     "'>'", "'>='", "'+.'", "'==.'", "'('", "')'", "'['", 
                     "']'", "'.'", "'..'", "','", "':'", "'::'", "';'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "K_BREAK", "K_CONTINUE", "K_IF", 
                      "K_ELSE_IF", "K_ELSE", "K_FOR_EACH", "K_ARRAY", "K_IN", 
                      "K_RETURN", "K_NULL", "K_SELF", "K_MAIN", "K_PROGRAM", 
                      "K_CLASS", "K_VAL", "K_VAR", "K_CONSTRUCTOR", "K_DESTRUCTOR", 
                      "K_NEW", "K_BY", "OP_ASSIGN", "OP_LOGICAL_NOT", "OP_LOGICAL_OR", 
                      "OP_LOGICAL_AND", "OP_IS_EQUAL_TO", "OP_NOT_EQUAL_TO", 
                      "OP_MODULO", "OP_ADDTION", "OP_SUBTRACTION", "OP_MULTIPLICATION", 
                      "OP_DIVISION", "OP_LESS_THAN", "OP_LESS_THAN_EQUAL", 
                      "OP_GREATER_THAN", "OP_GREATER_THAN_EQUAL", "OP_STRING_CONCATENATION", 
                      "OP_TWO_SAME_STRING", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "DOT", 
                      "DOUBLE_DOT", "COMMA", "COLON", "DOUBLE_COLON", "SEMI_COLON", 
                      "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "INTEGER_LITERAL2", 
                      "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", 
                      "STRING_LITERAL", "PRIMITIVE_TYPE", "IDENTIFIER", 
                      "DOLAR_IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classDeclaration = 1
    RULE_normalClassDecl = 2
    RULE_programClassDecl = 3
    RULE_programClassMemDecl = 4
    RULE_mainMethodDecl = 5
    RULE_memberDeclaration = 6
    RULE_methodDeclaration = 7
    RULE_constructor = 8
    RULE_destructor = 9
    RULE_parameterList = 10
    RULE_parameter = 11
    RULE_d96Type = 12
    RULE_attributeDeclaration = 13
    RULE_identifierList = 14
    RULE_mixedIdentifier = 15
    RULE_expressionList = 16
    RULE_elementExpression = 17
    RULE_indexOperator = 18
    RULE_relationalOperator = 19
    RULE_expression = 20
    RULE_relationalExpr = 21
    RULE_andOrExpr = 22
    RULE_addSubExpr = 23
    RULE_mulAddMolExpr = 24
    RULE_notExpr = 25
    RULE_signExpr = 26
    RULE_indexOperatorExpr = 27
    RULE_instanceAccess = 28
    RULE_staticAccess = 29
    RULE_objectCreation = 30
    RULE_atomExpr = 31
    RULE_varValStatement = 32
    RULE_lhs = 33
    RULE_assignStatement = 34
    RULE_ifStatement = 35
    RULE_forInStatement = 36
    RULE_breakStatement = 37
    RULE_continueStatement = 38
    RULE_returnStatement = 39
    RULE_methodInvocationStatement = 40
    RULE_blockStatement = 41
    RULE_statement = 42
    RULE_literal = 43
    RULE_indexedArray = 44
    RULE_multiDimentionalArray = 45
    RULE_arrayType = 46

    ruleNames =  [ "program", "classDeclaration", "normalClassDecl", "programClassDecl", 
                   "programClassMemDecl", "mainMethodDecl", "memberDeclaration", 
                   "methodDeclaration", "constructor", "destructor", "parameterList", 
                   "parameter", "d96Type", "attributeDeclaration", "identifierList", 
                   "mixedIdentifier", "expressionList", "elementExpression", 
                   "indexOperator", "relationalOperator", "expression", 
                   "relationalExpr", "andOrExpr", "addSubExpr", "mulAddMolExpr", 
                   "notExpr", "signExpr", "indexOperatorExpr", "instanceAccess", 
                   "staticAccess", "objectCreation", "atomExpr", "varValStatement", 
                   "lhs", "assignStatement", "ifStatement", "forInStatement", 
                   "breakStatement", "continueStatement", "returnStatement", 
                   "methodInvocationStatement", "blockStatement", "statement", 
                   "literal", "indexedArray", "multiDimentionalArray", "arrayType" ]

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
    K_RETURN=10
    K_NULL=11
    K_SELF=12
    K_MAIN=13
    K_PROGRAM=14
    K_CLASS=15
    K_VAL=16
    K_VAR=17
    K_CONSTRUCTOR=18
    K_DESTRUCTOR=19
    K_NEW=20
    K_BY=21
    OP_ASSIGN=22
    OP_LOGICAL_NOT=23
    OP_LOGICAL_OR=24
    OP_LOGICAL_AND=25
    OP_IS_EQUAL_TO=26
    OP_NOT_EQUAL_TO=27
    OP_MODULO=28
    OP_ADDTION=29
    OP_SUBTRACTION=30
    OP_MULTIPLICATION=31
    OP_DIVISION=32
    OP_LESS_THAN=33
    OP_LESS_THAN_EQUAL=34
    OP_GREATER_THAN=35
    OP_GREATER_THAN_EQUAL=36
    OP_STRING_CONCATENATION=37
    OP_TWO_SAME_STRING=38
    LEFT_PAREN=39
    RIGHT_PAREN=40
    LEFT_SQUARE_BRACKET=41
    RIGHT_SQUARE_BRACKET=42
    DOT=43
    DOUBLE_DOT=44
    COMMA=45
    COLON=46
    DOUBLE_COLON=47
    SEMI_COLON=48
    LEFT_CURLY_BRACKET=49
    RIGHT_CURLY_BRACKET=50
    INTEGER_LITERAL2=51
    INTEGER_LITERAL=52
    FLOAT_LITERAL=53
    BOOLEAN_LITERAL=54
    STRING_LITERAL=55
    PRIMITIVE_TYPE=56
    IDENTIFIER=57
    DOLAR_IDENTIFIER=58
    WS=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_CHAR=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def classDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ClassDeclarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.ClassDeclarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

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
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.classDeclaration()
                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.K_CLASS):
                    break

            self.state = 99
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalClassDecl(self):
            return self.getTypedRuleContext(D96Parser.NormalClassDeclContext,0)


        def programClassDecl(self):
            return self.getTypedRuleContext(D96Parser.ProgramClassDeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = D96Parser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDeclaration)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.normalClassDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.programClassDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_CLASS(self):
            return self.getToken(D96Parser.K_CLASS, 0)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def K_MAIN(self):
            return self.getToken(D96Parser.K_MAIN, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def memberDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.MemberDeclarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.MemberDeclarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_normalClassDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalClassDecl" ):
                return visitor.visitNormalClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def normalClassDecl(self):

        localctx = D96Parser.NormalClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_normalClassDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(D96Parser.K_CLASS)
            self.state = 106
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_MAIN or _la==D96Parser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 107
                self.match(D96Parser.COLON)
                self.state = 108
                self.match(D96Parser.IDENTIFIER)


            self.state = 111
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_MAIN) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 112
                self.memberDeclaration()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_CLASS(self):
            return self.getToken(D96Parser.K_CLASS, 0)

        def K_PROGRAM(self):
            return self.getToken(D96Parser.K_PROGRAM, 0)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.LEFT_CURLY_BRACKET, 0)

        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_CURLY_BRACKET, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def programClassMemDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ProgramClassMemDeclContext)
            else:
                return self.getTypedRuleContext(D96Parser.ProgramClassMemDeclContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_programClassDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramClassDecl" ):
                return visitor.visitProgramClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def programClassDecl(self):

        localctx = D96Parser.ProgramClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_programClassDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(D96Parser.K_CLASS)
            self.state = 121
            self.match(D96Parser.K_PROGRAM)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 122
                self.match(D96Parser.COLON)
                self.state = 123
                self.match(D96Parser.IDENTIFIER)


            self.state = 126
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_MAIN) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 127
                self.programClassMemDecl()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self.match(D96Parser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramClassMemDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeDeclaration(self):
            return self.getTypedRuleContext(D96Parser.AttributeDeclarationContext,0)


        def mainMethodDecl(self):
            return self.getTypedRuleContext(D96Parser.MainMethodDeclContext,0)


        def methodDeclaration(self):
            return self.getTypedRuleContext(D96Parser.MethodDeclarationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_programClassMemDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramClassMemDecl" ):
                return visitor.visitProgramClassMemDecl(self)
            else:
                return visitor.visitChildren(self)




    def programClassMemDecl(self):

        localctx = D96Parser.ProgramClassMemDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_programClassMemDecl)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.attributeDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.mainMethodDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.methodDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainMethodDeclContext(ParserRuleContext):
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

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mainMethodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainMethodDecl" ):
                return visitor.visitMainMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def mainMethodDecl(self):

        localctx = D96Parser.MainMethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mainMethodDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(D96Parser.K_MAIN)
            self.state = 141
            self.match(D96Parser.LEFT_PAREN)
            self.state = 142
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 143
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeDeclaration(self):
            return self.getTypedRuleContext(D96Parser.AttributeDeclarationContext,0)


        def methodDeclaration(self):
            return self.getTypedRuleContext(D96Parser.MethodDeclarationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_memberDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberDeclaration" ):
                return visitor.visitMemberDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def memberDeclaration(self):

        localctx = D96Parser.MemberDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_memberDeclaration)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_VAL, D96Parser.K_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.attributeDeclaration()
                pass
            elif token in [D96Parser.K_MAIN, D96Parser.K_CONSTRUCTOR, D96Parser.K_DESTRUCTOR, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
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


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def K_MAIN(self):
            return self.getToken(D96Parser.K_MAIN, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def parameterList(self):
            return self.getTypedRuleContext(D96Parser.ParameterListContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methodDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = D96Parser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_MAIN, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_MAIN) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.match(D96Parser.LEFT_PAREN)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 151
                    self.parameterList()


                self.state = 154
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 155
                self.blockStatement()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.constructor()
                pass
            elif token in [D96Parser.K_DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
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

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(D96Parser.ParameterListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(D96Parser.K_CONSTRUCTOR)
            self.state = 161
            self.match(D96Parser.LEFT_PAREN)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDENTIFIER:
                self.state = 162
                self.parameterList()


            self.state = 165
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 166
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_DESTRUCTOR(self):
            return self.getToken(D96Parser.K_DESTRUCTOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(D96Parser.K_DESTRUCTOR)
            self.state = 169
            self.match(D96Parser.LEFT_PAREN)
            self.state = 170
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 171
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
            return D96Parser.RULE_parameterList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = D96Parser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.parameter()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI_COLON:
                self.state = 174
                self.match(D96Parser.SEMI_COLON)
                self.state = 175
                self.parameter()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def identifierList(self):
            return self.getTypedRuleContext(D96Parser.IdentifierListContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96Type(self):
            return self.getTypedRuleContext(D96Parser.D96TypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.identifierList()
            self.state = 182
            self.match(D96Parser.COLON)
            self.state = 183
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMITIVE_TYPE(self):
            return self.getToken(D96Parser.PRIMITIVE_TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_d96Type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitD96Type" ):
                return visitor.visitD96Type(self)
            else:
                return visitor.visitChildren(self)




    def d96Type(self):

        localctx = D96Parser.D96TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_d96Type)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.PRIMITIVE_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(D96Parser.PRIMITIVE_TYPE)
                pass
            elif token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mixedIdentifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.MixedIdentifierContext)
            else:
                return self.getTypedRuleContext(D96Parser.MixedIdentifierContext,i)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96Type(self):
            return self.getTypedRuleContext(D96Parser.D96TypeContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_attributeDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeDeclaration" ):
                return visitor.visitAttributeDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def attributeDeclaration(self):

        localctx = D96Parser.AttributeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_attributeDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 191
            self.mixedIdentifier()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 192
                self.match(D96Parser.COMMA)
                self.state = 193
                self.mixedIdentifier()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.match(D96Parser.COLON)
            self.state = 200
            self.d96Type()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 201
                self.match(D96Parser.OP_ASSIGN)
                self.state = 202
                self.expression()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 203
                    self.match(D96Parser.COMMA)
                    self.state = 204
                    self.expression()
                    self.state = 209
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 212
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
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
            return D96Parser.RULE_identifierList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierList" ):
                return visitor.visitIdentifierList(self)
            else:
                return visitor.visitChildren(self)




    def identifierList(self):

        localctx = D96Parser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(D96Parser.IDENTIFIER)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 215
                self.match(D96Parser.COMMA)
                self.state = 216
                self.match(D96Parser.IDENTIFIER)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MixedIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mixedIdentifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMixedIdentifier" ):
                return visitor.visitMixedIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def mixedIdentifier(self):

        localctx = D96Parser.MixedIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_mixedIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
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


    class ExpressionListContext(ParserRuleContext):
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
            return D96Parser.RULE_expressionList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = D96Parser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.expression()
                self.state = 228 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 226
                    self.match(D96Parser.COMMA)
                    self.state = 227
                    self.expression()
                    self.state = 230 
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


    class ElementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def indexOperator(self):
            return self.getTypedRuleContext(D96Parser.IndexOperatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elementExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementExpression" ):
                return visitor.visitElementExpression(self)
            else:
                return visitor.visitChildren(self)




    def elementExpression(self):

        localctx = D96Parser.ElementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_elementExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expression()
            self.state = 235
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LEFT_SQUARE_BRACKET)
            else:
                return self.getToken(D96Parser.LEFT_SQUARE_BRACKET, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def RIGHT_SQUARE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RIGHT_SQUARE_BRACKET)
            else:
                return self.getToken(D96Parser.RIGHT_SQUARE_BRACKET, i)

        def getRuleIndex(self):
            return D96Parser.RULE_indexOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexOperator" ):
                return visitor.visitIndexOperator(self)
            else:
                return visitor.visitChildren(self)




    def indexOperator(self):

        localctx = D96Parser.IndexOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_indexOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 237
                    self.match(D96Parser.LEFT_SQUARE_BRACKET)
                    self.state = 238
                    self.expression()
                    self.state = 239
                    self.match(D96Parser.RIGHT_SQUARE_BRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 243 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalOperatorContext(ParserRuleContext):
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
            return D96Parser.RULE_relationalOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalOperator" ):
                return visitor.visitRelationalOperator(self)
            else:
                return visitor.visitChildren(self)




    def relationalOperator(self):

        localctx = D96Parser.RelationalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relationalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
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

        def relationalExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.RelationalExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.RelationalExprContext,i)


        def OP_STRING_CONCATENATION(self):
            return self.getToken(D96Parser.OP_STRING_CONCATENATION, 0)

        def OP_TWO_SAME_STRING(self):
            return self.getToken(D96Parser.OP_TWO_SAME_STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.relationalExpr()
                self.state = 248
                _la = self._input.LA(1)
                if not(_la==D96Parser.OP_STRING_CONCATENATION or _la==D96Parser.OP_TWO_SAME_STRING):
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andOrExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.AndOrExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.AndOrExprContext,i)


        def relationalOperator(self):
            return self.getTypedRuleContext(D96Parser.RelationalOperatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_relationalExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpr(self):

        localctx = D96Parser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_relationalExpr)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addSubExpr(self):
            return self.getTypedRuleContext(D96Parser.AddSubExprContext,0)


        def andOrExpr(self):
            return self.getTypedRuleContext(D96Parser.AndOrExprContext,0)


        def OP_LOGICAL_AND(self):
            return self.getToken(D96Parser.OP_LOGICAL_AND, 0)

        def OP_LOGICAL_OR(self):
            return self.getToken(D96Parser.OP_LOGICAL_OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_andOrExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndOrExpr" ):
                return visitor.visitAndOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def andOrExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.AndOrExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_andOrExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.addSubExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
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
                    if not(_la==D96Parser.OP_LOGICAL_OR or _la==D96Parser.OP_LOGICAL_AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 266
                    self.addSubExpr(0) 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AddSubExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulAddMolExpr(self):
            return self.getTypedRuleContext(D96Parser.MulAddMolExprContext,0)


        def addSubExpr(self):
            return self.getTypedRuleContext(D96Parser.AddSubExprContext,0)


        def OP_ADDTION(self):
            return self.getToken(D96Parser.OP_ADDTION, 0)

        def OP_SUBTRACTION(self):
            return self.getToken(D96Parser.OP_SUBTRACTION, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_addSubExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def addSubExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.AddSubExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_addSubExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.mulAddMolExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
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
                    if not(_la==D96Parser.OP_ADDTION or _la==D96Parser.OP_SUBTRACTION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 277
                    self.mulAddMolExpr(0) 
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MulAddMolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notExpr(self):
            return self.getTypedRuleContext(D96Parser.NotExprContext,0)


        def mulAddMolExpr(self):
            return self.getTypedRuleContext(D96Parser.MulAddMolExprContext,0)


        def OP_MULTIPLICATION(self):
            return self.getToken(D96Parser.OP_MULTIPLICATION, 0)

        def OP_DIVISION(self):
            return self.getToken(D96Parser.OP_DIVISION, 0)

        def OP_MODULO(self):
            return self.getToken(D96Parser.OP_MODULO, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mulAddMolExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulAddMolExpr" ):
                return visitor.visitMulAddMolExpr(self)
            else:
                return visitor.visitChildren(self)



    def mulAddMolExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.MulAddMolExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_mulAddMolExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.notExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MODULO) | (1 << D96Parser.OP_MULTIPLICATION) | (1 << D96Parser.OP_DIVISION))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 288
                    self.notExpr() 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NotExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_LOGICAL_NOT(self):
            return self.getToken(D96Parser.OP_LOGICAL_NOT, 0)

        def notExpr(self):
            return self.getTypedRuleContext(D96Parser.NotExprContext,0)


        def signExpr(self):
            return self.getTypedRuleContext(D96Parser.SignExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_notExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)




    def notExpr(self):

        localctx = D96Parser.NotExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_notExpr)
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
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_SELF, D96Parser.K_NEW, D96Parser.OP_ADDTION, D96Parser.OP_SUBTRACTION, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signExpr(self):
            return self.getTypedRuleContext(D96Parser.SignExprContext,0)


        def OP_SUBTRACTION(self):
            return self.getToken(D96Parser.OP_SUBTRACTION, 0)

        def OP_ADDTION(self):
            return self.getToken(D96Parser.OP_ADDTION, 0)

        def indexOperatorExpr(self):
            return self.getTypedRuleContext(D96Parser.IndexOperatorExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_signExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignExpr" ):
                return visitor.visitSignExpr(self)
            else:
                return visitor.visitChildren(self)




    def signExpr(self):

        localctx = D96Parser.SignExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_signExpr)
        self._la = 0 # Token type
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_ADDTION, D96Parser.OP_SUBTRACTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                _la = self._input.LA(1)
                if not(_la==D96Parser.OP_ADDTION or _la==D96Parser.OP_SUBTRACTION):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 300
                self.signExpr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_SELF, D96Parser.K_NEW, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.indexOperatorExpr()
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instanceAccess(self):
            return self.getTypedRuleContext(D96Parser.InstanceAccessContext,0)


        def indexOperator(self):
            return self.getTypedRuleContext(D96Parser.IndexOperatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexOperatorExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexOperatorExpr" ):
                return visitor.visitIndexOperatorExpr(self)
            else:
                return visitor.visitChildren(self)




    def indexOperatorExpr(self):

        localctx = D96Parser.IndexOperatorExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_indexOperatorExpr)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.instanceAccess(0)
                self.state = 305
                self.indexOperator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.instanceAccess(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def staticAccess(self):
            return self.getTypedRuleContext(D96Parser.StaticAccessContext,0)


        def instanceAccess(self):
            return self.getTypedRuleContext(D96Parser.InstanceAccessContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(D96Parser.ExpressionListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instanceAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceAccess" ):
                return visitor.visitInstanceAccess(self)
            else:
                return visitor.visitChildren(self)



    def instanceAccess(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.InstanceAccessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_instanceAccess, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.staticAccess(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.InstanceAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instanceAccess)
                    self.state = 313
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 314
                    self.match(D96Parser.DOT)
                    self.state = 315
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 321
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        self.state = 316
                        self.match(D96Parser.LEFT_PAREN)
                        self.state = 318
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_ADDTION) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                            self.state = 317
                            self.expressionList()


                        self.state = 320
                        self.match(D96Parser.RIGHT_PAREN)

             
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StaticAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objectCreation(self):
            return self.getTypedRuleContext(D96Parser.ObjectCreationContext,0)


        def staticAccess(self):
            return self.getTypedRuleContext(D96Parser.StaticAccessContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(D96Parser.ExpressionListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_staticAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticAccess" ):
                return visitor.visitStaticAccess(self)
            else:
                return visitor.visitChildren(self)



    def staticAccess(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.StaticAccessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_staticAccess, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.objectCreation()
            self._ctx.stop = self._input.LT(-1)
            self.state = 343
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.StaticAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_staticAccess)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 332
                    self.match(D96Parser.DOUBLE_COLON)
                    self.state = 333
                    self.match(D96Parser.DOLAR_IDENTIFIER)
                    self.state = 339
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        self.state = 334
                        self.match(D96Parser.LEFT_PAREN)
                        self.state = 336
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_ADDTION) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                            self.state = 335
                            self.expressionList()


                        self.state = 338
                        self.match(D96Parser.RIGHT_PAREN)

             
                self.state = 345
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ObjectCreationContext(ParserRuleContext):
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

        def expressionList(self):
            return self.getTypedRuleContext(D96Parser.ExpressionListContext,0)


        def atomExpr(self):
            return self.getTypedRuleContext(D96Parser.AtomExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_objectCreation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectCreation" ):
                return visitor.visitObjectCreation(self)
            else:
                return visitor.visitChildren(self)




    def objectCreation(self):

        localctx = D96Parser.ObjectCreationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_objectCreation)
        self._la = 0 # Token type
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(D96Parser.K_NEW)
                self.state = 347
                self.match(D96Parser.IDENTIFIER)
                self.state = 348
                self.match(D96Parser.LEFT_PAREN)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_ADDTION) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 349
                    self.expressionList()


                self.state = 352
                self.match(D96Parser.RIGHT_PAREN)
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_SELF, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def K_NULL(self):
            return self.getToken(D96Parser.K_NULL, 0)

        def K_SELF(self):
            return self.getToken(D96Parser.K_SELF, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_atomExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)




    def atomExpr(self):

        localctx = D96Parser.AtomExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_atomExpr)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_ARRAY, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.literal()
                pass
            elif token in [D96Parser.K_NULL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.match(D96Parser.K_NULL)
                pass
            elif token in [D96Parser.K_SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 358
                self.match(D96Parser.K_SELF)
                pass
            elif token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 359
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 360
                self.match(D96Parser.LEFT_PAREN)
                self.state = 361
                self.expression()
                self.state = 362
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIER)
            else:
                return self.getToken(D96Parser.IDENTIFIER, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96Type(self):
            return self.getTypedRuleContext(D96Parser.D96TypeContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_varValStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarValStatement" ):
                return visitor.visitVarValStatement(self)
            else:
                return visitor.visitChildren(self)




    def varValStatement(self):

        localctx = D96Parser.VarValStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_varValStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 367
            self.match(D96Parser.IDENTIFIER)
            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 368
                self.match(D96Parser.COMMA)
                self.state = 369
                self.match(D96Parser.IDENTIFIER)
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 375
            self.match(D96Parser.COLON)
            self.state = 376
            self.d96Type()
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 377
                self.match(D96Parser.OP_ASSIGN)
                self.state = 378
                self.expression()
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 379
                    self.match(D96Parser.COMMA)
                    self.state = 380
                    self.expression()
                    self.state = 385
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 388
            self.match(D96Parser.SEMI_COLON)
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

        def instanceAccess(self):
            return self.getTypedRuleContext(D96Parser.InstanceAccessContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def elementExpression(self):
            return self.getTypedRuleContext(D96Parser.ElementExpressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_lhs)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.instanceAccess(0)
                self.state = 391
                self.match(D96Parser.DOT)
                self.state = 392
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.instanceAccess(0)
                self.state = 395
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 396
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 398
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 399
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
            return D96Parser.RULE_assignStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = D96Parser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.lhs()
            self.state = 403
            self.match(D96Parser.OP_ASSIGN)
            self.state = 404
            self.expression()
            self.state = 405
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

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def K_ELSE_IF(self):
            return self.getToken(D96Parser.K_ELSE_IF, 0)

        def K_ELSE(self):
            return self.getToken(D96Parser.K_ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = D96Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifStatement)
        try:
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(D96Parser.K_IF)
                self.state = 408
                self.match(D96Parser.LEFT_PAREN)
                self.state = 409
                self.expression()
                self.state = 410
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 411
                self.blockStatement()
                pass
            elif token in [D96Parser.K_ELSE_IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.match(D96Parser.K_ELSE_IF)
                self.state = 414
                self.match(D96Parser.LEFT_PAREN)
                self.state = 415
                self.expression()
                self.state = 416
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 417
                self.blockStatement()
                pass
            elif token in [D96Parser.K_ELSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 419
                self.match(D96Parser.K_ELSE)
                self.state = 420
                self.blockStatement()
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


    class ForInStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_FOR_EACH(self):
            return self.getToken(D96Parser.K_FOR_EACH, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def K_IN(self):
            return self.getToken(D96Parser.K_IN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def DOUBLE_DOT(self):
            return self.getToken(D96Parser.DOUBLE_DOT, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def K_BY(self):
            return self.getToken(D96Parser.K_BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forInStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInStatement" ):
                return visitor.visitForInStatement(self)
            else:
                return visitor.visitChildren(self)




    def forInStatement(self):

        localctx = D96Parser.ForInStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_forInStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(D96Parser.K_FOR_EACH)
            self.state = 424
            self.match(D96Parser.LEFT_PAREN)
            self.state = 425
            self.match(D96Parser.IDENTIFIER)
            self.state = 426
            self.match(D96Parser.K_IN)
            self.state = 427
            self.expression()
            self.state = 428
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 429
            self.expression()
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_BY:
                self.state = 430
                self.match(D96Parser.K_BY)
                self.state = 431
                self.expression()


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


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_BREAK(self):
            return self.getToken(D96Parser.K_BREAK, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = D96Parser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(D96Parser.K_BREAK)
            self.state = 438
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_CONTINUE(self):
            return self.getToken(D96Parser.K_CONTINUE, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = D96Parser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(D96Parser.K_CONTINUE)
            self.state = 441
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
            return D96Parser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = D96Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(D96Parser.K_RETURN)
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_ADDTION) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 444
                self.expression()


            self.state = 447
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvocationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instanceAccess(self):
            return self.getTypedRuleContext(D96Parser.InstanceAccessContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_methodInvocationStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodInvocationStatement" ):
                return visitor.visitMethodInvocationStatement(self)
            else:
                return visitor.visitChildren(self)




    def methodInvocationStatement(self):

        localctx = D96Parser.MethodInvocationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_methodInvocationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.instanceAccess(0)
            self.state = 450
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
            return D96Parser.RULE_blockStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = D96Parser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 456
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_BREAK) | (1 << D96Parser.K_CONTINUE) | (1 << D96Parser.K_IF) | (1 << D96Parser.K_ELSE_IF) | (1 << D96Parser.K_ELSE) | (1 << D96Parser.K_FOR_EACH) | (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_RETURN) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_ADDTION) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.LEFT_CURLY_BRACKET) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 453
                self.statement()
                self.state = 458
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 459
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

        def varValStatement(self):
            return self.getTypedRuleContext(D96Parser.VarValStatementContext,0)


        def assignStatement(self):
            return self.getTypedRuleContext(D96Parser.AssignStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(D96Parser.IfStatementContext,0)


        def forInStatement(self):
            return self.getTypedRuleContext(D96Parser.ForInStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(D96Parser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(D96Parser.ContinueStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(D96Parser.ReturnStatementContext,0)


        def methodInvocationStatement(self):
            return self.getTypedRuleContext(D96Parser.MethodInvocationStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_statement)
        try:
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.varValStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.assignStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 463
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 464
                self.forInStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 465
                self.breakStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 466
                self.continueStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 467
                self.returnStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 468
                self.methodInvocationStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 469
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

        def indexedArray(self):
            return self.getTypedRuleContext(D96Parser.IndexedArrayContext,0)


        def multiDimentionalArray(self):
            return self.getTypedRuleContext(D96Parser.MultiDimentionalArrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literal)
        try:
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.match(D96Parser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.match(D96Parser.INTEGER_LITERAL2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 474
                self.match(D96Parser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 475
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 476
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 477
                self.indexedArray()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 478
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

        def indexedArray(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IndexedArrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.IndexedArrayContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_indexedArray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexedArray" ):
                return visitor.visitIndexedArray(self)
            else:
                return visitor.visitChildren(self)




    def indexedArray(self):

        localctx = D96Parser.IndexedArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_indexedArray)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(D96Parser.K_ARRAY)
            self.state = 482
            self.match(D96Parser.LEFT_PAREN)
            self.state = 533
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RIGHT_PAREN, D96Parser.INTEGER_LITERAL]:
                self.state = 491
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.INTEGER_LITERAL:
                    self.state = 483
                    self.match(D96Parser.INTEGER_LITERAL)
                    self.state = 488
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.COMMA:
                        self.state = 484
                        self.match(D96Parser.COMMA)
                        self.state = 485
                        self.match(D96Parser.INTEGER_LITERAL)
                        self.state = 490
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                pass
            elif token in [D96Parser.INTEGER_LITERAL2]:
                self.state = 493
                self.match(D96Parser.INTEGER_LITERAL2)
                self.state = 498
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 494
                    self.match(D96Parser.COMMA)
                    self.state = 495
                    self.match(D96Parser.INTEGER_LITERAL2)
                    self.state = 500
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.state = 501
                self.match(D96Parser.FLOAT_LITERAL)
                self.state = 506
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 502
                    self.match(D96Parser.COMMA)
                    self.state = 503
                    self.match(D96Parser.FLOAT_LITERAL)
                    self.state = 508
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.state = 509
                self.match(D96Parser.BOOLEAN_LITERAL)
                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 510
                    self.match(D96Parser.COMMA)
                    self.state = 511
                    self.match(D96Parser.BOOLEAN_LITERAL)
                    self.state = 516
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.state = 517
                self.match(D96Parser.STRING_LITERAL)
                self.state = 522
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 518
                    self.match(D96Parser.COMMA)
                    self.state = 519
                    self.match(D96Parser.STRING_LITERAL)
                    self.state = 524
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 525
                self.indexedArray()
                self.state = 530
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 526
                    self.match(D96Parser.COMMA)
                    self.state = 527
                    self.indexedArray()
                    self.state = 532
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 535
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ARRAY(self):
            return self.getToken(D96Parser.K_ARRAY, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def indexedArray(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IndexedArrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.IndexedArrayContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_multiDimentionalArray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiDimentionalArray" ):
                return visitor.visitMultiDimentionalArray(self)
            else:
                return visitor.visitChildren(self)




    def multiDimentionalArray(self):

        localctx = D96Parser.MultiDimentionalArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_multiDimentionalArray)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(D96Parser.K_ARRAY)
            self.state = 538
            self.match(D96Parser.LEFT_PAREN)

            self.state = 547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ARRAY:
                self.state = 539
                self.indexedArray()
                self.state = 544
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 540
                    self.match(D96Parser.COMMA)
                    self.state = 541
                    self.indexedArray()
                    self.state = 546
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 549
            self.match(D96Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
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

        def PRIMITIVE_TYPE(self):
            return self.getToken(D96Parser.PRIMITIVE_TYPE, 0)

        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = D96Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(D96Parser.K_ARRAY)
            self.state = 552
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.PRIMITIVE_TYPE]:
                self.state = 553
                self.match(D96Parser.PRIMITIVE_TYPE)
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 554
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 557
            self.match(D96Parser.COMMA)
            self.state = 558
            self.match(D96Parser.INTEGER_LITERAL2)
            self.state = 559
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
        self._predicates[22] = self.andOrExpr_sempred
        self._predicates[23] = self.addSubExpr_sempred
        self._predicates[24] = self.mulAddMolExpr_sempred
        self._predicates[28] = self.instanceAccess_sempred
        self._predicates[29] = self.staticAccess_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def andOrExpr_sempred(self, localctx:AndOrExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def addSubExpr_sempred(self, localctx:AddSubExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def mulAddMolExpr_sempred(self, localctx:MulAddMolExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def instanceAccess_sempred(self, localctx:InstanceAccessContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def staticAccess_sempred(self, localctx:StaticAccessContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




