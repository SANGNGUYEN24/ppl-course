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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u022b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\3\2\6\2p\n\2\r\2\16\2q")
        buf.write("\3\2\3\2\3\3\3\3\3\3\5\3y\n\3\3\3\3\3\7\3}\n\3\f\3\16")
        buf.write("\3\u0080\13\3\3\3\3\3\3\4\3\4\5\4\u0086\n\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\5\6\u008e\n\6\3\6\3\6\3\6\3\6\3\6\5\6\u0095")
        buf.write("\n\6\3\7\3\7\3\7\5\7\u009a\n\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\6\t\u00a8\n\t\r\t\16\t\u00a9")
        buf.write("\5\t\u00ac\n\t\3\n\3\n\3\n\3\n\3\13\3\13\5\13\u00b4\n")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\6")
        buf.write("\r\u00c2\n\r\r\r\16\r\u00c3\5\r\u00c6\n\r\3\16\3\16\3")
        buf.write("\16\3\16\6\16\u00cc\n\16\r\16\16\16\u00cd\5\16\u00d0\n")
        buf.write("\16\3\17\3\17\3\17\3\17\6\17\u00d6\n\17\r\17\16\17\u00d7")
        buf.write("\5\17\u00da\n\17\3\20\3\20\3\20\3\20\6\20\u00e0\n\20\r")
        buf.write("\20\16\20\u00e1\5\20\u00e4\n\20\3\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\22\7\22\u00ed\n\22\f\22\16\22\u00f0\13\22\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u00f9\n\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0100\n\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\7\26\u0108\n\26\f\26\16\26\u010b\13\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\7\27\u0113\n\27\f\27\16\27")
        buf.write("\u0116\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u011e")
        buf.write("\n\30\f\30\16\30\u0121\13\30\3\31\3\31\3\31\5\31\u0126")
        buf.write("\n\31\3\32\3\32\3\32\5\32\u012b\n\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\7\33\u0132\n\33\f\33\16\33\u0135\13\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\7\34\u013d\n\34\f\34\16\34\u0140")
        buf.write("\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u014a")
        buf.write("\n\35\3\35\3\35\7\35\u014e\n\35\f\35\16\35\u0151\13\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\5\36\u0158\n\36\3\36\3\36\3")
        buf.write("\37\3\37\3\37\3\37\3 \3 \3 \3 \5 \u0164\n \3 \3 \5 \u0168")
        buf.write("\n \3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u0173\n!\3\"\3\"\3\"")
        buf.write("\5\"\u0178\n\"\3\"\3\"\3#\3#\3#\3#\3#\5#\u0181\n#\3#\3")
        buf.write("#\5#\u0185\n#\3$\3$\5$\u0189\n$\3$\3$\3$\3%\3%\7%\u0190")
        buf.write("\n%\f%\16%\u0193\13%\3%\5%\u0196\n%\3&\3&\3&\3&\3&\3&")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\5*\u01b4\n*\3+\3+\3,\3,\3-\3-\3-\3")
        buf.write(".\3.\5.\u01bf\n.\3/\3/\3/\3/\7/\u01c5\n/\f/\16/\u01c8")
        buf.write("\13/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60")
        buf.write("\u01d4\n\60\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01dc\n")
        buf.write("\61\3\62\3\62\3\62\3\62\3\62\7\62\u01e3\n\62\f\62\16\62")
        buf.write("\u01e6\13\62\3\62\3\62\3\62\7\62\u01eb\n\62\f\62\16\62")
        buf.write("\u01ee\13\62\3\62\3\62\3\62\7\62\u01f3\n\62\f\62\16\62")
        buf.write("\u01f6\13\62\3\62\3\62\3\62\7\62\u01fb\n\62\f\62\16\62")
        buf.write("\u01fe\13\62\3\62\3\62\3\62\7\62\u0203\n\62\f\62\16\62")
        buf.write("\u0206\13\62\3\62\5\62\u0209\n\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\7\63\u0212\n\63\f\63\16\63\u0215\13\63")
        buf.write("\5\63\u0217\n\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\2\b*,.\64\6688\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("jl\2\n\3\2\23\24\3\2:;\4\2\35\36$\'\3\2()\3\2\33\34\3")
        buf.write("\2 !\4\2\37\37\"#\4\2\n\n\f\17\2\u023c\2o\3\2\2\2\4u\3")
        buf.write("\2\2\2\6\u0085\3\2\2\2\b\u0087\3\2\2\2\n\u0094\3\2\2\2")
        buf.write("\f\u0096\3\2\2\2\16\u009e\3\2\2\2\20\u00ab\3\2\2\2\22")
        buf.write("\u00ad\3\2\2\2\24\u00b3\3\2\2\2\26\u00b5\3\2\2\2\30\u00c5")
        buf.write("\3\2\2\2\32\u00cf\3\2\2\2\34\u00d9\3\2\2\2\36\u00e3\3")
        buf.write("\2\2\2 \u00e5\3\2\2\2\"\u00e8\3\2\2\2$\u00f1\3\2\2\2&")
        buf.write("\u00f8\3\2\2\2(\u00ff\3\2\2\2*\u0101\3\2\2\2,\u010c\3")
        buf.write("\2\2\2.\u0117\3\2\2\2\60\u0125\3\2\2\2\62\u012a\3\2\2")
        buf.write("\2\64\u012c\3\2\2\2\66\u0136\3\2\2\28\u0141\3\2\2\2:\u0152")
        buf.write("\3\2\2\2<\u015b\3\2\2\2>\u0167\3\2\2\2@\u0172\3\2\2\2")
        buf.write("B\u0174\3\2\2\2D\u017b\3\2\2\2F\u0188\3\2\2\2H\u018d\3")
        buf.write("\2\2\2J\u0197\3\2\2\2L\u019d\3\2\2\2N\u01a3\3\2\2\2P\u01a6")
        buf.write("\3\2\2\2R\u01ac\3\2\2\2T\u01b5\3\2\2\2V\u01b7\3\2\2\2")
        buf.write("X\u01b9\3\2\2\2Z\u01be\3\2\2\2\\\u01c0\3\2\2\2^\u01d3")
        buf.write("\3\2\2\2`\u01db\3\2\2\2b\u01dd\3\2\2\2d\u020c\3\2\2\2")
        buf.write("f\u021a\3\2\2\2h\u021c\3\2\2\2j\u021e\3\2\2\2l\u0225\3")
        buf.write("\2\2\2np\5\4\3\2on\3\2\2\2pq\3\2\2\2qo\3\2\2\2qr\3\2\2")
        buf.write("\2rs\3\2\2\2st\7\2\2\3t\3\3\2\2\2uv\7\22\2\2vx\7:\2\2")
        buf.write("wy\5\b\5\2xw\3\2\2\2xy\3\2\2\2yz\3\2\2\2z~\7\64\2\2{}")
        buf.write("\5\6\4\2|{\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2")
        buf.write("\2\177\u0081\3\2\2\2\u0080~\3\2\2\2\u0081\u0082\7\65\2")
        buf.write("\2\u0082\5\3\2\2\2\u0083\u0086\5\26\f\2\u0084\u0086\5")
        buf.write("\n\6\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086\7")
        buf.write("\3\2\2\2\u0087\u0088\7\61\2\2\u0088\u0089\7:\2\2\u0089")
        buf.write("\t\3\2\2\2\u008a\u008b\5f\64\2\u008b\u008d\7*\2\2\u008c")
        buf.write("\u008e\5\20\t\2\u008d\u008c\3\2\2\2\u008d\u008e\3\2\2")
        buf.write("\2\u008e\u008f\3\2\2\2\u008f\u0090\7+\2\2\u0090\u0091")
        buf.write("\5\\/\2\u0091\u0095\3\2\2\2\u0092\u0095\5\f\7\2\u0093")
        buf.write("\u0095\5\16\b\2\u0094\u008a\3\2\2\2\u0094\u0092\3\2\2")
        buf.write("\2\u0094\u0093\3\2\2\2\u0095\13\3\2\2\2\u0096\u0097\7")
        buf.write("\25\2\2\u0097\u0099\7*\2\2\u0098\u009a\5\20\t\2\u0099")
        buf.write("\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\u009c\7+\2\2\u009c\u009d\5\\/\2\u009d\r\3\2\2\2")
        buf.write("\u009e\u009f\7\26\2\2\u009f\u00a0\7*\2\2\u00a0\u00a1\7")
        buf.write("+\2\2\u00a1\u00a2\5\\/\2\u00a2\17\3\2\2\2\u00a3\u00ac")
        buf.write("\5\22\n\2\u00a4\u00a7\5\22\n\2\u00a5\u00a6\7\63\2\2\u00a6")
        buf.write("\u00a8\5\22\n\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\3\2\2")
        buf.write("\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac")
        buf.write("\3\2\2\2\u00ab\u00a3\3\2\2\2\u00ab\u00a4\3\2\2\2\u00ac")
        buf.write("\21\3\2\2\2\u00ad\u00ae\5\30\r\2\u00ae\u00af\7\61\2\2")
        buf.write("\u00af\u00b0\5\24\13\2\u00b0\23\3\2\2\2\u00b1\u00b4\5")
        buf.write("h\65\2\u00b2\u00b4\5f\64\2\u00b3\u00b1\3\2\2\2\u00b3\u00b2")
        buf.write("\3\2\2\2\u00b4\25\3\2\2\2\u00b5\u00b6\t\2\2\2\u00b6\u00b7")
        buf.write("\5\34\17\2\u00b7\u00b8\7\61\2\2\u00b8\u00b9\5\24\13\2")
        buf.write("\u00b9\u00ba\7\31\2\2\u00ba\u00bb\5\36\20\2\u00bb\u00bc")
        buf.write("\7\63\2\2\u00bc\27\3\2\2\2\u00bd\u00c6\7:\2\2\u00be\u00c1")
        buf.write("\7:\2\2\u00bf\u00c0\7\60\2\2\u00c0\u00c2\7:\2\2\u00c1")
        buf.write("\u00bf\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c1\3\2\2\2")
        buf.write("\u00c3\u00c4\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00bd\3")
        buf.write("\2\2\2\u00c5\u00be\3\2\2\2\u00c6\31\3\2\2\2\u00c7\u00d0")
        buf.write("\7;\2\2\u00c8\u00cb\7;\2\2\u00c9\u00ca\7\60\2\2\u00ca")
        buf.write("\u00cc\7;\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3")
        buf.write("\2\2\2\u00cf\u00c7\3\2\2\2\u00cf\u00c8\3\2\2\2\u00d0\33")
        buf.write("\3\2\2\2\u00d1\u00da\t\3\2\2\u00d2\u00d5\t\3\2\2\u00d3")
        buf.write("\u00d4\7\60\2\2\u00d4\u00d6\t\3\2\2\u00d5\u00d3\3\2\2")
        buf.write("\2\u00d6\u00d7\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8")
        buf.write("\3\2\2\2\u00d8\u00da\3\2\2\2\u00d9\u00d1\3\2\2\2\u00d9")
        buf.write("\u00d2\3\2\2\2\u00da\35\3\2\2\2\u00db\u00e4\5&\24\2\u00dc")
        buf.write("\u00df\5&\24\2\u00dd\u00de\7\60\2\2\u00de\u00e0\5&\24")
        buf.write("\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e4\3\2\2\2\u00e3")
        buf.write("\u00db\3\2\2\2\u00e3\u00dc\3\2\2\2\u00e4\37\3\2\2\2\u00e5")
        buf.write("\u00e6\5&\24\2\u00e6\u00e7\5\"\22\2\u00e7!\3\2\2\2\u00e8")
        buf.write("\u00e9\7,\2\2\u00e9\u00ea\5&\24\2\u00ea\u00ee\7-\2\2\u00eb")
        buf.write("\u00ed\5\"\22\2\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2")
        buf.write("\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef#\3\2")
        buf.write("\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f2\t\4\2\2\u00f2%\3")
        buf.write("\2\2\2\u00f3\u00f4\5(\25\2\u00f4\u00f5\t\5\2\2\u00f5\u00f6")
        buf.write("\5(\25\2\u00f6\u00f9\3\2\2\2\u00f7\u00f9\5(\25\2\u00f8")
        buf.write("\u00f3\3\2\2\2\u00f8\u00f7\3\2\2\2\u00f9\'\3\2\2\2\u00fa")
        buf.write("\u00fb\5*\26\2\u00fb\u00fc\5$\23\2\u00fc\u00fd\5*\26\2")
        buf.write("\u00fd\u0100\3\2\2\2\u00fe\u0100\5*\26\2\u00ff\u00fa\3")
        buf.write("\2\2\2\u00ff\u00fe\3\2\2\2\u0100)\3\2\2\2\u0101\u0102")
        buf.write("\b\26\1\2\u0102\u0103\5,\27\2\u0103\u0109\3\2\2\2\u0104")
        buf.write("\u0105\f\4\2\2\u0105\u0106\t\6\2\2\u0106\u0108\5,\27\2")
        buf.write("\u0107\u0104\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3")
        buf.write("\2\2\2\u0109\u010a\3\2\2\2\u010a+\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010c\u010d\b\27\1\2\u010d\u010e\5.\30\2\u010e")
        buf.write("\u0114\3\2\2\2\u010f\u0110\f\4\2\2\u0110\u0111\t\7\2\2")
        buf.write("\u0111\u0113\5.\30\2\u0112\u010f\3\2\2\2\u0113\u0116\3")
        buf.write("\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115-")
        buf.write("\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118\b\30\1\2\u0118")
        buf.write("\u0119\5\60\31\2\u0119\u011f\3\2\2\2\u011a\u011b\f\4\2")
        buf.write("\2\u011b\u011c\t\b\2\2\u011c\u011e\5\60\31\2\u011d\u011a")
        buf.write("\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120/\3\2\2\2\u0121\u011f\3\2\2\2\u0122")
        buf.write("\u0123\7\32\2\2\u0123\u0126\5\60\31\2\u0124\u0126\5\62")
        buf.write("\32\2\u0125\u0122\3\2\2\2\u0125\u0124\3\2\2\2\u0126\61")
        buf.write("\3\2\2\2\u0127\u0128\7!\2\2\u0128\u012b\5\62\32\2\u0129")
        buf.write("\u012b\5\64\33\2\u012a\u0127\3\2\2\2\u012a\u0129\3\2\2")
        buf.write("\2\u012b\63\3\2\2\2\u012c\u012d\b\33\1\2\u012d\u012e\5")
        buf.write("\66\34\2\u012e\u0133\3\2\2\2\u012f\u0130\f\4\2\2\u0130")
        buf.write("\u0132\5\"\22\2\u0131\u012f\3\2\2\2\u0132\u0135\3\2\2")
        buf.write("\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134\65\3")
        buf.write("\2\2\2\u0135\u0133\3\2\2\2\u0136\u0137\b\34\1\2\u0137")
        buf.write("\u0138\58\35\2\u0138\u013e\3\2\2\2\u0139\u013a\f\4\2\2")
        buf.write("\u013a\u013b\7.\2\2\u013b\u013d\5f\64\2\u013c\u0139\3")
        buf.write("\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f")
        buf.write("\3\2\2\2\u013f\67\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0142")
        buf.write("\b\35\1\2\u0142\u0143\5> \2\u0143\u014f\3\2\2\2\u0144")
        buf.write("\u0145\f\4\2\2\u0145\u0146\7.\2\2\u0146\u0147\5f\64\2")
        buf.write("\u0147\u0149\7*\2\2\u0148\u014a\5\36\20\2\u0149\u0148")
        buf.write("\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\3\2\2\2\u014b")
        buf.write("\u014c\7+\2\2\u014c\u014e\3\2\2\2\u014d\u0144\3\2\2\2")
        buf.write("\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3")
        buf.write("\2\2\2\u01509\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0153")
        buf.write("\7:\2\2\u0153\u0154\7\62\2\2\u0154\u0155\7;\2\2\u0155")
        buf.write("\u0157\7*\2\2\u0156\u0158\5\36\20\2\u0157\u0156\3\2\2")
        buf.write("\2\u0157\u0158\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a")
        buf.write("\7+\2\2\u015a;\3\2\2\2\u015b\u015c\7:\2\2\u015c\u015d")
        buf.write("\7\62\2\2\u015d\u015e\7;\2\2\u015e=\3\2\2\2\u015f\u0160")
        buf.write("\7\27\2\2\u0160\u0161\7:\2\2\u0161\u0163\7*\2\2\u0162")
        buf.write("\u0164\5\36\20\2\u0163\u0162\3\2\2\2\u0163\u0164\3\2\2")
        buf.write("\2\u0164\u0165\3\2\2\2\u0165\u0168\7+\2\2\u0166\u0168")
        buf.write("\5@!\2\u0167\u015f\3\2\2\2\u0167\u0166\3\2\2\2\u0168?")
        buf.write("\3\2\2\2\u0169\u0173\5`\61\2\u016a\u0173\5f\64\2\u016b")
        buf.write("\u016c\7*\2\2\u016c\u016d\5&\24\2\u016d\u016e\7+\2\2\u016e")
        buf.write("\u0173\3\2\2\2\u016f\u0173\5B\"\2\u0170\u0173\5<\37\2")
        buf.write("\u0171\u0173\5:\36\2\u0172\u0169\3\2\2\2\u0172\u016a\3")
        buf.write("\2\2\2\u0172\u016b\3\2\2\2\u0172\u016f\3\2\2\2\u0172\u0170")
        buf.write("\3\2\2\2\u0172\u0171\3\2\2\2\u0173A\3\2\2\2\u0174\u0175")
        buf.write("\7:\2\2\u0175\u0177\7*\2\2\u0176\u0178\5\36\20\2\u0177")
        buf.write("\u0176\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179\u017a\7+\2\2\u017aC\3\2\2\2\u017b\u017c\t\2\2\2")
        buf.write("\u017c\u017d\5\30\r\2\u017d\u0180\7\61\2\2\u017e\u0181")
        buf.write("\5j\66\2\u017f\u0181\5h\65\2\u0180\u017e\3\2\2\2\u0180")
        buf.write("\u017f\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0183\7\31\2")
        buf.write("\2\u0183\u0185\5\36\20\2\u0184\u0182\3\2\2\2\u0184\u0185")
        buf.write("\3\2\2\2\u0185E\3\2\2\2\u0186\u0189\5f\64\2\u0187\u0189")
        buf.write("\5 \21\2\u0188\u0186\3\2\2\2\u0188\u0187\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u018b\7\31\2\2\u018b\u018c\5&\24")
        buf.write("\2\u018cG\3\2\2\2\u018d\u0191\5J&\2\u018e\u0190\5L\'\2")
        buf.write("\u018f\u018e\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3")
        buf.write("\2\2\2\u0191\u0192\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191")
        buf.write("\3\2\2\2\u0194\u0196\5N(\2\u0195\u0194\3\2\2\2\u0195\u0196")
        buf.write("\3\2\2\2\u0196I\3\2\2\2\u0197\u0198\7\6\2\2\u0198\u0199")
        buf.write("\7*\2\2\u0199\u019a\5&\24\2\u019a\u019b\7+\2\2\u019b\u019c")
        buf.write("\5\\/\2\u019cK\3\2\2\2\u019d\u019e\7\7\2\2\u019e\u019f")
        buf.write("\7*\2\2\u019f\u01a0\5&\24\2\u01a0\u01a1\7+\2\2\u01a1\u01a2")
        buf.write("\5\\/\2\u01a2M\3\2\2\2\u01a3\u01a4\7\b\2\2\u01a4\u01a5")
        buf.write("\5\\/\2\u01a5O\3\2\2\2\u01a6\u01a7\7\t\2\2\u01a7\u01a8")
        buf.write("\7*\2\2\u01a8\u01a9\5R*\2\u01a9\u01aa\7+\2\2\u01aa\u01ab")
        buf.write("\5\\/\2\u01abQ\3\2\2\2\u01ac\u01ad\7:\2\2\u01ad\u01ae")
        buf.write("\7\13\2\2\u01ae\u01af\7\66\2\2\u01af\u01b0\7/\2\2\u01b0")
        buf.write("\u01b3\7\66\2\2\u01b1\u01b2\7\30\2\2\u01b2\u01b4\7\66")
        buf.write("\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4S\3")
        buf.write("\2\2\2\u01b5\u01b6\7\4\2\2\u01b6U\3\2\2\2\u01b7\u01b8")
        buf.write("\7\5\2\2\u01b8W\3\2\2\2\u01b9\u01ba\7\20\2\2\u01ba\u01bb")
        buf.write("\5&\24\2\u01bbY\3\2\2\2\u01bc\u01bf\58\35\2\u01bd\u01bf")
        buf.write("\5:\36\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write("[\3\2\2\2\u01c0\u01c6\7\64\2\2\u01c1\u01c2\5^\60\2\u01c2")
        buf.write("\u01c3\7\63\2\2\u01c3\u01c5\3\2\2\2\u01c4\u01c1\3\2\2")
        buf.write("\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7")
        buf.write("\3\2\2\2\u01c7\u01c9\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9")
        buf.write("\u01ca\7\65\2\2\u01ca]\3\2\2\2\u01cb\u01d4\5D#\2\u01cc")
        buf.write("\u01d4\5F$\2\u01cd\u01d4\5H%\2\u01ce\u01d4\5P)\2\u01cf")
        buf.write("\u01d4\5T+\2\u01d0\u01d4\5V,\2\u01d1\u01d4\5X-\2\u01d2")
        buf.write("\u01d4\5Z.\2\u01d3\u01cb\3\2\2\2\u01d3\u01cc\3\2\2\2\u01d3")
        buf.write("\u01cd\3\2\2\2\u01d3\u01ce\3\2\2\2\u01d3\u01cf\3\2\2\2")
        buf.write("\u01d3\u01d0\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d2\3")
        buf.write("\2\2\2\u01d4_\3\2\2\2\u01d5\u01dc\7\66\2\2\u01d6\u01dc")
        buf.write("\7\67\2\2\u01d7\u01dc\78\2\2\u01d8\u01dc\79\2\2\u01d9")
        buf.write("\u01dc\5b\62\2\u01da\u01dc\5d\63\2\u01db\u01d5\3\2\2\2")
        buf.write("\u01db\u01d6\3\2\2\2\u01db\u01d7\3\2\2\2\u01db\u01d8\3")
        buf.write("\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01da\3\2\2\2\u01dca")
        buf.write("\3\2\2\2\u01dd\u01de\7\n\2\2\u01de\u0208\7*\2\2\u01df")
        buf.write("\u01e4\7\66\2\2\u01e0\u01e1\7\60\2\2\u01e1\u01e3\7\66")
        buf.write("\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2")
        buf.write("\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u0209\3\2\2\2\u01e6")
        buf.write("\u01e4\3\2\2\2\u01e7\u01ec\7\67\2\2\u01e8\u01e9\7\60\2")
        buf.write("\2\u01e9\u01eb\7\67\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ee")
        buf.write("\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write("\u0209\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01f4\78\2\2")
        buf.write("\u01f0\u01f1\7\60\2\2\u01f1\u01f3\78\2\2\u01f2\u01f0\3")
        buf.write("\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\u0209\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7")
        buf.write("\u01fc\79\2\2\u01f8\u01f9\7\60\2\2\u01f9\u01fb\79\2\2")
        buf.write("\u01fa\u01f8\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3")
        buf.write("\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u0209\3\2\2\2\u01fe\u01fc")
        buf.write("\3\2\2\2\u01ff\u0204\5b\62\2\u0200\u0201\7\60\2\2\u0201")
        buf.write("\u0203\5b\62\2\u0202\u0200\3\2\2\2\u0203\u0206\3\2\2\2")
        buf.write("\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0209\3")
        buf.write("\2\2\2\u0206\u0204\3\2\2\2\u0207\u0209\3\2\2\2\u0208\u01df")
        buf.write("\3\2\2\2\u0208\u01e7\3\2\2\2\u0208\u01ef\3\2\2\2\u0208")
        buf.write("\u01f7\3\2\2\2\u0208\u01ff\3\2\2\2\u0208\u0207\3\2\2\2")
        buf.write("\u0209\u020a\3\2\2\2\u020a\u020b\7+\2\2\u020bc\3\2\2\2")
        buf.write("\u020c\u020d\7\n\2\2\u020d\u0216\7*\2\2\u020e\u0213\5")
        buf.write("b\62\2\u020f\u0210\7\60\2\2\u0210\u0212\5b\62\2\u0211")
        buf.write("\u020f\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2")
        buf.write("\u0213\u0214\3\2\2\2\u0214\u0217\3\2\2\2\u0215\u0213\3")
        buf.write("\2\2\2\u0216\u020e\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0218")
        buf.write("\3\2\2\2\u0218\u0219\7+\2\2\u0219e\3\2\2\2\u021a\u021b")
        buf.write("\t\3\2\2\u021bg\3\2\2\2\u021c\u021d\t\t\2\2\u021di\3\2")
        buf.write("\2\2\u021e\u021f\7\n\2\2\u021f\u0220\7,\2\2\u0220\u0221")
        buf.write("\5h\65\2\u0221\u0222\7\60\2\2\u0222\u0223\7\66\2\2\u0223")
        buf.write("\u0224\7-\2\2\u0224k\3\2\2\2\u0225\u0226\7\27\2\2\u0226")
        buf.write("\u0227\7:\2\2\u0227\u0228\7*\2\2\u0228\u0229\7+\2\2\u0229")
        buf.write("m\3\2\2\2\67qx~\u0085\u008d\u0094\u0099\u00a9\u00ab\u00b3")
        buf.write("\u00c3\u00c5\u00cd\u00cf\u00d7\u00d9\u00e1\u00e3\u00ee")
        buf.write("\u00f8\u00ff\u0109\u0114\u011f\u0125\u012a\u0133\u013e")
        buf.write("\u0149\u014f\u0157\u0163\u0167\u0172\u0177\u0180\u0184")
        buf.write("\u0188\u0191\u0195\u01b3\u01be\u01c6\u01d3\u01db\u01e4")
        buf.write("\u01ec\u01f4\u01fc\u0204\u0208\u0213\u0216")
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
                      "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", 
                      "STRING_LITERAL", "IDENTIFIER", "DOLAR_IDENTIFIER", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
    RULE_instance_attribute_access = 26
    RULE_instace_method_invocation = 27
    RULE_static_method_invocation = 28
    RULE_static_attribute_access = 29
    RULE_object_creation = 30
    RULE_atom_expr = 31
    RULE_function_call = 32
    RULE_var_val_statement = 33
    RULE_assign_statement = 34
    RULE_if_statement = 35
    RULE_if_part = 36
    RULE_else_if_part = 37
    RULE_else_part = 38
    RULE_for_in_statement = 39
    RULE_loop_part = 40
    RULE_break_statement = 41
    RULE_continue_statement = 42
    RULE_return_statement = 43
    RULE_method_invocation_statement = 44
    RULE_block_statement = 45
    RULE_statement = 46
    RULE_literal = 47
    RULE_indexed_array = 48
    RULE_multi_dimentional_array = 49
    RULE_identifier = 50
    RULE_primitive_type = 51
    RULE_array_type = 52
    RULE_class_type = 53

    ruleNames =  [ "program", "class_declaration", "class_body_unit", "super_class_group", 
                   "method_declaration", "constructor", "destructor", "parameter_list", 
                   "parameter", "type_name", "attribute_declaration", "identifier_list", 
                   "dolar_identifier_list", "mixed_identifier_list", "expression_list", 
                   "element_expression", "index_operator", "relational_operator", 
                   "expression", "relational_expr", "and_or_expr", "add_sub_expr", 
                   "mul_add_mol_expr", "not_expr", "sign_expr", "index_operator_expr", 
                   "instance_attribute_access", "instace_method_invocation", 
                   "static_method_invocation", "static_attribute_access", 
                   "object_creation", "atom_expr", "function_call", "var_val_statement", 
                   "assign_statement", "if_statement", "if_part", "else_if_part", 
                   "else_part", "for_in_statement", "loop_part", "break_statement", 
                   "continue_statement", "return_statement", "method_invocation_statement", 
                   "block_statement", "statement", "literal", "indexed_array", 
                   "multi_dimentional_array", "identifier", "primitive_type", 
                   "array_type", "class_type" ]

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
    INTEGER_LITERAL=52
    FLOAT_LITERAL=53
    BOOLEAN_LITERAL=54
    STRING_LITERAL=55
    IDENTIFIER=56
    DOLAR_IDENTIFIER=57
    WS=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60
    ERROR_CHAR=61

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

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declarationContext,i)


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
            self.state = 109 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 108
                self.class_declaration()
                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.K_CLASS):
                    break

            self.state = 113
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
            self.state = 115
            self.match(D96Parser.K_CLASS)
            self.state = 116
            self.match(D96Parser.IDENTIFIER)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 117
                self.super_class_group()


            self.state = 120
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 121
                self.class_body_unit()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body_unit" ):
                return visitor.visitClass_body_unit(self)
            else:
                return visitor.visitChildren(self)




    def class_body_unit(self):

        localctx = D96Parser.Class_body_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body_unit)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_VAL, D96Parser.K_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.attribute_declaration()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR, D96Parser.K_DESTRUCTOR, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
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
            self.state = 133
            self.match(D96Parser.COLON)
            self.state = 134
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
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.identifier()
                self.state = 137
                self.match(D96Parser.LEFT_PAREN)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 138
                    self.parameter_list()


                self.state = 141
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 142
                self.block_statement()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.constructor()
                pass
            elif token in [D96Parser.K_DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
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
            self.state = 148
            self.match(D96Parser.K_CONSTRUCTOR)
            self.state = 149
            self.match(D96Parser.LEFT_PAREN)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDENTIFIER:
                self.state = 150
                self.parameter_list()


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
            self.state = 156
            self.match(D96Parser.K_DESTRUCTOR)
            self.state = 157
            self.match(D96Parser.LEFT_PAREN)
            self.state = 158
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 159
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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.parameter()
                self.state = 165 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 163
                    self.match(D96Parser.SEMI_COLON)
                    self.state = 164
                    self.parameter()
                    self.state = 167 
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
            self.state = 171
            self.identifier_list()
            self.state = 172
            self.match(D96Parser.COLON)
            self.state = 173
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


        def getRuleIndex(self):
            return D96Parser.RULE_type_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = D96Parser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_name)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_ARRAY, D96Parser.K_INT, D96Parser.K_FLOAT, D96Parser.K_BOOLEAN, D96Parser.K_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.primitive_type()
                pass
            elif token in [D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.identifier()
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


        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def K_VAL(self):
            return self.getToken(D96Parser.K_VAL, 0)

        def K_VAR(self):
            return self.getToken(D96Parser.K_VAR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declaration

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
            self.state = 179
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 180
            self.mixed_identifier_list()
            self.state = 181
            self.match(D96Parser.COLON)
            self.state = 182
            self.type_name()
            self.state = 183
            self.match(D96Parser.OP_ASSIGN)
            self.state = 184
            self.expression_list()
            self.state = 185
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
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(D96Parser.IDENTIFIER)
                self.state = 191 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 189
                    self.match(D96Parser.COMMA)
                    self.state = 190
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 193 
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
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 201 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 199
                    self.match(D96Parser.COMMA)
                    self.state = 200
                    self.match(D96Parser.DOLAR_IDENTIFIER)
                    self.state = 203 
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
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                _la = self._input.LA(1)
                if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                _la = self._input.LA(1)
                if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 211 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 209
                    self.match(D96Parser.COMMA)
                    self.state = 210
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 213 
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
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.expression()
                self.state = 221 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 219
                    self.match(D96Parser.COMMA)
                    self.state = 220
                    self.expression()
                    self.state = 223 
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
            self.state = 227
            self.expression()
            self.state = 228
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
            self.state = 230
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 231
            self.expression()
            self.state = 232
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 233
                    self.index_operator() 
                self.state = 238
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
            self.state = 239
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
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.relational_expr()
                self.state = 242
                _la = self._input.LA(1)
                if not(_la==D96Parser.OP_STRING_CONCATENATION or _la==D96Parser.OP_TWO_SAME_STRING):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 243
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = D96Parser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relational_expr)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.and_or_expr(0)
                self.state = 249
                self.relational_operator()
                self.state = 250
                self.and_or_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
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
            self.state = 256
            self.add_sub_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.And_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_or_expr)
                    self.state = 258
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 259
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_LOGICAL_OR or _la==D96Parser.OP_LOGICAL_AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 260
                    self.add_sub_expr(0) 
                self.state = 265
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
            self.state = 267
            self.mul_add_mol_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Add_sub_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expr)
                    self.state = 269
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 270
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_ADDTION or _la==D96Parser.OP_SUBTRACTION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 271
                    self.mul_add_mol_expr(0) 
                self.state = 276
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
            self.state = 278
            self.not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Mul_add_mol_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_add_mol_expr)
                    self.state = 280
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 281
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MODULO) | (1 << D96Parser.OP_MULTIPLICATION) | (1 << D96Parser.OP_DIVISION))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 282
                    self.not_expr() 
                self.state = 287
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_expr" ):
                return visitor.visitNot_expr(self)
            else:
                return visitor.visitChildren(self)




    def not_expr(self):

        localctx = D96Parser.Not_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_not_expr)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(D96Parser.OP_LOGICAL_NOT)
                self.state = 289
                self.not_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NEW, D96Parser.OP_SUBTRACTION, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = D96Parser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_sign_expr)
        try:
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUBTRACTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(D96Parser.OP_SUBTRACTION)
                self.state = 294
                self.sign_expr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NEW, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
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
            self.state = 299
            self.instance_attribute_access(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operator_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operator_expr)
                    self.state = 301
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 302
                    self.index_operator() 
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_attribute_access

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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_instance_attribute_access, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.instace_method_invocation(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Instance_attribute_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_attribute_access)
                    self.state = 311
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    self.match(D96Parser.DOT)
                    self.state = 313
                    self.identifier() 
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
            return D96Parser.RULE_instace_method_invocation

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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_instace_method_invocation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.object_creation()
            self._ctx.stop = self._input.LT(-1)
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Instace_method_invocationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instace_method_invocation)
                    self.state = 322
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 323
                    self.match(D96Parser.DOT)
                    self.state = 324
                    self.identifier()
                    self.state = 325
                    self.match(D96Parser.LEFT_PAREN)
                    self.state = 327
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                        self.state = 326
                        self.expression_list()


                    self.state = 329
                    self.match(D96Parser.RIGHT_PAREN) 
                self.state = 335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(D96Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_invocation" ):
                return visitor.visitStatic_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def static_method_invocation(self):

        localctx = D96Parser.Static_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_static_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(D96Parser.IDENTIFIER)
            self.state = 337
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 338
            self.match(D96Parser.DOLAR_IDENTIFIER)
            self.state = 339
            self.match(D96Parser.LEFT_PAREN)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 340
                self.expression_list()


            self.state = 343
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

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLAR_IDENTIFIER(self):
            return self.getToken(D96Parser.DOLAR_IDENTIFIER, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attribute_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_attribute_access" ):
                return visitor.visitStatic_attribute_access(self)
            else:
                return visitor.visitChildren(self)




    def static_attribute_access(self):

        localctx = D96Parser.Static_attribute_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_static_attribute_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(D96Parser.IDENTIFIER)
            self.state = 346
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 347
            self.match(D96Parser.DOLAR_IDENTIFIER)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_creation" ):
                return visitor.visitObject_creation(self)
            else:
                return visitor.visitChildren(self)




    def object_creation(self):

        localctx = D96Parser.Object_creationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_object_creation)
        self._la = 0 # Token type
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.match(D96Parser.K_NEW)
                self.state = 350
                self.match(D96Parser.IDENTIFIER)
                self.state = 351
                self.match(D96Parser.LEFT_PAREN)
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                    self.state = 352
                    self.expression_list()


                self.state = 355
                self.match(D96Parser.RIGHT_PAREN)
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
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

        def function_call(self):
            return self.getTypedRuleContext(D96Parser.Function_callContext,0)


        def static_attribute_access(self):
            return self.getTypedRuleContext(D96Parser.Static_attribute_accessContext,0)


        def static_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_atom_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom_expr" ):
                return visitor.visitAtom_expr(self)
            else:
                return visitor.visitChildren(self)




    def atom_expr(self):

        localctx = D96Parser.Atom_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_atom_expr)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 361
                self.match(D96Parser.LEFT_PAREN)
                self.state = 362
                self.expression()
                self.state = 363
                self.match(D96Parser.RIGHT_PAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 365
                self.function_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 366
                self.static_attribute_access()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 367
                self.static_method_invocation()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = D96Parser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(D96Parser.IDENTIFIER)
            self.state = 371
            self.match(D96Parser.LEFT_PAREN)
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 372
                self.expression_list()


            self.state = 375
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_val_statement" ):
                return visitor.visitVar_val_statement(self)
            else:
                return visitor.visitChildren(self)




    def var_val_statement(self):

        localctx = D96Parser.Var_val_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_var_val_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 378
            self.identifier_list()
            self.state = 379
            self.match(D96Parser.COLON)
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 380
                self.array_type()
                pass

            elif la_ == 2:
                self.state = 381
                self.primitive_type()
                pass


            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 384
                self.match(D96Parser.OP_ASSIGN)
                self.state = 385
                self.expression_list()


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


        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def element_expression(self):
            return self.getTypedRuleContext(D96Parser.Element_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 388
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 389
                self.element_expression()
                pass


            self.state = 392
            self.match(D96Parser.OP_ASSIGN)
            self.state = 393
            self.expression()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.if_part()
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.K_ELSE_IF:
                self.state = 396
                self.else_if_part()
                self.state = 401
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ELSE:
                self.state = 402
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_part" ):
                return visitor.visitIf_part(self)
            else:
                return visitor.visitChildren(self)




    def if_part(self):

        localctx = D96Parser.If_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(D96Parser.K_IF)
            self.state = 406
            self.match(D96Parser.LEFT_PAREN)
            self.state = 407
            self.expression()
            self.state = 408
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 409
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_part" ):
                return visitor.visitElse_if_part(self)
            else:
                return visitor.visitChildren(self)




    def else_if_part(self):

        localctx = D96Parser.Else_if_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_else_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(D96Parser.K_ELSE_IF)
            self.state = 412
            self.match(D96Parser.LEFT_PAREN)
            self.state = 413
            self.expression()
            self.state = 414
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 415
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = D96Parser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(D96Parser.K_ELSE)
            self.state = 418
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_statement" ):
                return visitor.visitFor_in_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_in_statement(self):

        localctx = D96Parser.For_in_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_for_in_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(D96Parser.K_FOR_EACH)
            self.state = 421
            self.match(D96Parser.LEFT_PAREN)
            self.state = 422
            self.loop_part()
            self.state = 423
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 424
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_part" ):
                return visitor.visitLoop_part(self)
            else:
                return visitor.visitChildren(self)




    def loop_part(self):

        localctx = D96Parser.Loop_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_loop_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(D96Parser.IDENTIFIER)
            self.state = 427
            self.match(D96Parser.K_IN)
            self.state = 428
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 429
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 430
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_BY:
                self.state = 431
                self.match(D96Parser.K_BY)
                self.state = 432
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

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(D96Parser.K_BREAK)
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

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(D96Parser.K_CONTINUE)
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


        def getRuleIndex(self):
            return D96Parser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(D96Parser.K_RETURN)
            self.state = 440
            self.expression()
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

        def instace_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Instace_method_invocationContext,0)


        def static_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_statement" ):
                return visitor.visitMethod_invocation_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_statement(self):

        localctx = D96Parser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_method_invocation_statement)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.instace_method_invocation(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.static_method_invocation()
                pass


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


        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI_COLON)
            else:
                return self.getToken(D96Parser.SEMI_COLON, i)

        def getRuleIndex(self):
            return D96Parser.RULE_block_statement

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
            self.state = 446
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_BREAK) | (1 << D96Parser.K_CONTINUE) | (1 << D96Parser.K_IF) | (1 << D96Parser.K_FOR_EACH) | (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_RETURN) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 447
                self.statement()
                self.state = 448
                self.match(D96Parser.SEMI_COLON)
                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 455
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_statement)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.var_val_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 459
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 460
                self.for_in_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 461
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 462
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 463
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 464
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_literal)
        try:
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.match(D96Parser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.match(D96Parser.FLOAT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 469
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 470
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 471
                self.indexed_array()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 472
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
            self.state = 475
            self.match(D96Parser.K_ARRAY)
            self.state = 476
            self.match(D96Parser.LEFT_PAREN)
            self.state = 518
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL]:
                self.state = 477
                self.match(D96Parser.INTEGER_LITERAL)
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 478
                    self.match(D96Parser.COMMA)
                    self.state = 479
                    self.match(D96Parser.INTEGER_LITERAL)
                    self.state = 484
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.state = 485
                self.match(D96Parser.FLOAT_LITERAL)
                self.state = 490
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 486
                    self.match(D96Parser.COMMA)
                    self.state = 487
                    self.match(D96Parser.FLOAT_LITERAL)
                    self.state = 492
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.state = 493
                self.match(D96Parser.BOOLEAN_LITERAL)
                self.state = 498
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 494
                    self.match(D96Parser.COMMA)
                    self.state = 495
                    self.match(D96Parser.BOOLEAN_LITERAL)
                    self.state = 500
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.state = 501
                self.match(D96Parser.STRING_LITERAL)
                self.state = 506
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 502
                    self.match(D96Parser.COMMA)
                    self.state = 503
                    self.match(D96Parser.STRING_LITERAL)
                    self.state = 508
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 509
                self.indexed_array()
                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 510
                    self.match(D96Parser.COMMA)
                    self.state = 511
                    self.indexed_array()
                    self.state = 516
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.RIGHT_PAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 520
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
            self.state = 522
            self.match(D96Parser.K_ARRAY)
            self.state = 523
            self.match(D96Parser.LEFT_PAREN)

            self.state = 532
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ARRAY:
                self.state = 524
                self.indexed_array()
                self.state = 529
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 525
                    self.match(D96Parser.COMMA)
                    self.state = 526
                    self.indexed_array()
                    self.state = 531
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 534
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
            self.state = 536
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
            self.state = 538
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
            self.state = 540
            self.match(D96Parser.K_ARRAY)
            self.state = 541
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 542
            self.primitive_type()
            self.state = 543
            self.match(D96Parser.COMMA)
            self.state = 544
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 545
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(D96Parser.K_NEW)
            self.state = 548
            self.match(D96Parser.IDENTIFIER)
            self.state = 549
            self.match(D96Parser.LEFT_PAREN)
            self.state = 550
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
        self._predicates[20] = self.and_or_expr_sempred
        self._predicates[21] = self.add_sub_expr_sempred
        self._predicates[22] = self.mul_add_mol_expr_sempred
        self._predicates[25] = self.index_operator_expr_sempred
        self._predicates[26] = self.instance_attribute_access_sempred
        self._predicates[27] = self.instace_method_invocation_sempred
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
         

    def instance_attribute_access_sempred(self, localctx:Instance_attribute_accessContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def instace_method_invocation_sempred(self, localctx:Instace_method_invocationContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




