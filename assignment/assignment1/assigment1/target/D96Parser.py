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
        buf.write("\u027e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\3\2\6\2p\n\2\r\2\16\2q")
        buf.write("\3\2\3\2\3\3\3\3\5\3x\n\3\3\4\3\4\3\4\3\4\5\4~\n\4\3\4")
        buf.write("\3\4\7\4\u0082\n\4\f\4\16\4\u0085\13\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\5\5\u008d\n\5\3\5\3\5\7\5\u0091\n\5\f\5\16\5")
        buf.write("\u0094\13\5\3\5\3\5\3\6\3\6\3\6\5\6\u009b\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\5\b\u00a4\n\b\3\t\3\t\3\t\5\t\u00a9")
        buf.write("\n\t\3\t\3\t\3\t\3\t\5\t\u00af\n\t\3\n\3\n\3\n\5\n\u00b4")
        buf.write("\n\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\7\f\u00c1\n\f\f\f\16\f\u00c4\13\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\5\16\u00cd\n\16\3\17\3\17\3\17\3\17\7\17\u00d3")
        buf.write("\n\17\f\17\16\17\u00d6\13\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u00de\n\17\f\17\16\17\u00e1\13\17\5\17\u00e3")
        buf.write("\n\17\3\17\3\17\3\20\3\20\3\20\7\20\u00ea\n\20\f\20\16")
        buf.write("\20\u00ed\13\20\3\21\3\21\3\22\3\22\3\22\3\22\6\22\u00f5")
        buf.write("\n\22\r\22\16\22\u00f6\5\22\u00f9\n\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\7\24\u0102\n\24\f\24\16\24\u0105")
        buf.write("\13\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26\5\26\u010e\n")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\5\27\u0115\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\7\30\u011d\n\30\f\30\16\30\u0120")
        buf.write("\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0128\n\31\f")
        buf.write("\31\16\31\u012b\13\31\3\32\3\32\3\32\3\32\3\32\3\32\7")
        buf.write("\32\u0133\n\32\f\32\16\32\u0136\13\32\3\33\3\33\3\33\5")
        buf.write("\33\u013b\n\33\3\34\3\34\3\34\5\34\u0140\n\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\7\35\u0147\n\35\f\35\16\35\u014a\13\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0154\n")
        buf.write("\36\3\36\5\36\u0157\n\36\7\36\u0159\n\36\f\36\16\36\u015c")
        buf.write("\13\36\3\37\3\37\3\37\3\37\3\37\5\37\u0163\n\37\3\37\5")
        buf.write("\37\u0166\n\37\3\37\5\37\u0169\n\37\3 \3 \3 \3 \5 \u016f")
        buf.write("\n \3 \3 \5 \u0173\n \3!\3!\3!\3!\3!\3!\3!\3!\5!\u017d")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5")
        buf.write("\"\u018b\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0197\n")
        buf.write("#\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u01a2\n$\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\7&\u01ab\n&\f&\16&\u01ae\13&\3&\5&\u01b1\n&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\5+\u01cf\n+\3,\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\5.\u01d9\n.\3.\3.\3/\3/\3/\5/\u01e0\n")
        buf.write("/\3/\3/\3/\3/\3/\5/\u01e7\n/\3/\5/\u01ea\n/\7/\u01ec\n")
        buf.write("/\f/\16/\u01ef\13/\3\60\3\60\3\60\3\60\3\60\3\60\5\60")
        buf.write("\u01f7\n\60\3\60\5\60\u01fa\n\60\3\61\3\61\3\61\3\61\3")
        buf.write("\61\5\61\u0201\n\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\5\61\u020a\n\61\3\61\5\61\u020d\n\61\3\61\3\61\3\62\3")
        buf.write("\62\7\62\u0213\n\62\f\62\16\62\u0216\13\62\3\62\3\62\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u0223")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u022c\n")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\7\65\u0233\n\65\f\65\16\65")
        buf.write("\u0236\13\65\5\65\u0238\n\65\3\65\3\65\3\65\7\65\u023d")
        buf.write("\n\65\f\65\16\65\u0240\13\65\3\65\3\65\3\65\7\65\u0245")
        buf.write("\n\65\f\65\16\65\u0248\13\65\3\65\3\65\3\65\7\65\u024d")
        buf.write("\n\65\f\65\16\65\u0250\13\65\3\65\3\65\3\65\7\65\u0255")
        buf.write("\n\65\f\65\16\65\u0258\13\65\3\65\3\65\3\65\7\65\u025d")
        buf.write("\n\65\f\65\16\65\u0260\13\65\5\65\u0262\n\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\7\66\u026b\n\66\f\66\16\66\u026e")
        buf.write("\13\66\5\66\u0270\n\66\3\66\3\66\3\67\3\67\3\67\3\67\5")
        buf.write("\67\u0278\n\67\3\67\3\67\3\67\3\67\3\67\2\b.\60\628:\\")
        buf.write("8\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjl\2\n\4\2\17\17;;\3\2")
        buf.write(";<\3\2\22\23\4\2\34\35#&\3\2\'(\3\2\32\33\3\2\37 \4\2")
        buf.write("\36\36!\"\2\u02a3\2o\3\2\2\2\4w\3\2\2\2\6y\3\2\2\2\b\u0088")
        buf.write("\3\2\2\2\n\u009a\3\2\2\2\f\u009c\3\2\2\2\16\u00a3\3\2")
        buf.write("\2\2\20\u00ae\3\2\2\2\22\u00b0\3\2\2\2\24\u00b8\3\2\2")
        buf.write("\2\26\u00bd\3\2\2\2\30\u00c5\3\2\2\2\32\u00cc\3\2\2\2")
        buf.write("\34\u00ce\3\2\2\2\36\u00e6\3\2\2\2 \u00ee\3\2\2\2\"\u00f8")
        buf.write("\3\2\2\2$\u00fa\3\2\2\2&\u00fd\3\2\2\2(\u0106\3\2\2\2")
        buf.write("*\u010d\3\2\2\2,\u0114\3\2\2\2.\u0116\3\2\2\2\60\u0121")
        buf.write("\3\2\2\2\62\u012c\3\2\2\2\64\u013a\3\2\2\2\66\u013f\3")
        buf.write("\2\2\28\u0141\3\2\2\2:\u014b\3\2\2\2<\u0168\3\2\2\2>\u0172")
        buf.write("\3\2\2\2@\u017c\3\2\2\2B\u018a\3\2\2\2D\u0196\3\2\2\2")
        buf.write("F\u01a1\3\2\2\2H\u01a3\3\2\2\2J\u01a8\3\2\2\2L\u01b2\3")
        buf.write("\2\2\2N\u01b8\3\2\2\2P\u01be\3\2\2\2R\u01c1\3\2\2\2T\u01c7")
        buf.write("\3\2\2\2V\u01d0\3\2\2\2X\u01d3\3\2\2\2Z\u01d6\3\2\2\2")
        buf.write("\\\u01df\3\2\2\2^\u01f0\3\2\2\2`\u020c\3\2\2\2b\u0210")
        buf.write("\3\2\2\2d\u0222\3\2\2\2f\u022b\3\2\2\2h\u022d\3\2\2\2")
        buf.write("j\u0265\3\2\2\2l\u0273\3\2\2\2np\5\4\3\2on\3\2\2\2pq\3")
        buf.write("\2\2\2qo\3\2\2\2qr\3\2\2\2rs\3\2\2\2st\7\2\2\3t\3\3\2")
        buf.write("\2\2ux\5\6\4\2vx\5\b\5\2wu\3\2\2\2wv\3\2\2\2x\5\3\2\2")
        buf.write("\2yz\7\21\2\2z}\t\2\2\2{|\7\60\2\2|~\7;\2\2}{\3\2\2\2")
        buf.write("}~\3\2\2\2~\177\3\2\2\2\177\u0083\7\63\2\2\u0080\u0082")
        buf.write("\5\16\b\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2\2\u0083")
        buf.write("\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0086\3\2\2\2")
        buf.write("\u0085\u0083\3\2\2\2\u0086\u0087\7\64\2\2\u0087\7\3\2")
        buf.write("\2\2\u0088\u0089\7\21\2\2\u0089\u008c\7\20\2\2\u008a\u008b")
        buf.write("\7\60\2\2\u008b\u008d\7;\2\2\u008c\u008a\3\2\2\2\u008c")
        buf.write("\u008d\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0092\7\63\2")
        buf.write("\2\u008f\u0091\5\n\6\2\u0090\u008f\3\2\2\2\u0091\u0094")
        buf.write("\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\u0095\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0096\7\64\2")
        buf.write("\2\u0096\t\3\2\2\2\u0097\u009b\5\34\17\2\u0098\u009b\5")
        buf.write("\20\t\2\u0099\u009b\5\f\7\2\u009a\u0097\3\2\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\13\3\2\2\2\u009c")
        buf.write("\u009d\7\17\2\2\u009d\u009e\7)\2\2\u009e\u009f\7*\2\2")
        buf.write("\u009f\u00a0\5b\62\2\u00a0\r\3\2\2\2\u00a1\u00a4\5\34")
        buf.write("\17\2\u00a2\u00a4\5\20\t\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2")
        buf.write("\3\2\2\2\u00a4\17\3\2\2\2\u00a5\u00a6\t\3\2\2\u00a6\u00a8")
        buf.write("\7)\2\2\u00a7\u00a9\5\26\f\2\u00a8\u00a7\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\7*\2\2")
        buf.write("\u00ab\u00af\5b\62\2\u00ac\u00af\5\22\n\2\u00ad\u00af")
        buf.write("\5\24\13\2\u00ae\u00a5\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\21\3\2\2\2\u00b0\u00b1\7\24\2\2\u00b1")
        buf.write("\u00b3\7)\2\2\u00b2\u00b4\5\26\f\2\u00b3\u00b2\3\2\2\2")
        buf.write("\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\7")
        buf.write("*\2\2\u00b6\u00b7\5b\62\2\u00b7\23\3\2\2\2\u00b8\u00b9")
        buf.write("\7\25\2\2\u00b9\u00ba\7)\2\2\u00ba\u00bb\7*\2\2\u00bb")
        buf.write("\u00bc\5b\62\2\u00bc\25\3\2\2\2\u00bd\u00c2\5\30\r\2\u00be")
        buf.write("\u00bf\7\62\2\2\u00bf\u00c1\5\30\r\2\u00c0\u00be\3\2\2")
        buf.write("\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3")
        buf.write("\3\2\2\2\u00c3\27\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00c6")
        buf.write("\5\36\20\2\u00c6\u00c7\7\60\2\2\u00c7\u00c8\5\32\16\2")
        buf.write("\u00c8\31\3\2\2\2\u00c9\u00cd\7:\2\2\u00ca\u00cd\7;\2")
        buf.write("\2\u00cb\u00cd\5l\67\2\u00cc\u00c9\3\2\2\2\u00cc\u00ca")
        buf.write("\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\33\3\2\2\2\u00ce\u00cf")
        buf.write("\t\4\2\2\u00cf\u00d4\5 \21\2\u00d0\u00d1\7/\2\2\u00d1")
        buf.write("\u00d3\5 \21\2\u00d2\u00d0\3\2\2\2\u00d3\u00d6\3\2\2\2")
        buf.write("\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d7\3")
        buf.write("\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\7\60\2\2\u00d8")
        buf.write("\u00e2\5\32\16\2\u00d9\u00da\7\30\2\2\u00da\u00df\5*\26")
        buf.write("\2\u00db\u00dc\7/\2\2\u00dc\u00de\5*\26\2\u00dd\u00db")
        buf.write("\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df")
        buf.write("\u00e0\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2")
        buf.write("\u00e2\u00d9\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\3")
        buf.write("\2\2\2\u00e4\u00e5\7\62\2\2\u00e5\35\3\2\2\2\u00e6\u00eb")
        buf.write("\7;\2\2\u00e7\u00e8\7/\2\2\u00e8\u00ea\7;\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec\37\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee")
        buf.write("\u00ef\t\3\2\2\u00ef!\3\2\2\2\u00f0\u00f9\5*\26\2\u00f1")
        buf.write("\u00f4\5*\26\2\u00f2\u00f3\7/\2\2\u00f3\u00f5\5*\26\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f4\3")
        buf.write("\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9\3\2\2\2\u00f8\u00f0")
        buf.write("\3\2\2\2\u00f8\u00f1\3\2\2\2\u00f9#\3\2\2\2\u00fa\u00fb")
        buf.write("\5*\26\2\u00fb\u00fc\5&\24\2\u00fc%\3\2\2\2\u00fd\u00fe")
        buf.write("\7+\2\2\u00fe\u00ff\5*\26\2\u00ff\u0103\7,\2\2\u0100\u0102")
        buf.write("\5&\24\2\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103")
        buf.write("\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104\'\3\2\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0106\u0107\t\5\2\2\u0107)\3\2\2\2\u0108")
        buf.write("\u0109\5,\27\2\u0109\u010a\t\6\2\2\u010a\u010b\5,\27\2")
        buf.write("\u010b\u010e\3\2\2\2\u010c\u010e\5,\27\2\u010d\u0108\3")
        buf.write("\2\2\2\u010d\u010c\3\2\2\2\u010e+\3\2\2\2\u010f\u0110")
        buf.write("\5.\30\2\u0110\u0111\5(\25\2\u0111\u0112\5.\30\2\u0112")
        buf.write("\u0115\3\2\2\2\u0113\u0115\5.\30\2\u0114\u010f\3\2\2\2")
        buf.write("\u0114\u0113\3\2\2\2\u0115-\3\2\2\2\u0116\u0117\b\30\1")
        buf.write("\2\u0117\u0118\5\60\31\2\u0118\u011e\3\2\2\2\u0119\u011a")
        buf.write("\f\4\2\2\u011a\u011b\t\7\2\2\u011b\u011d\5\60\31\2\u011c")
        buf.write("\u0119\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c\3\2\2\2")
        buf.write("\u011e\u011f\3\2\2\2\u011f/\3\2\2\2\u0120\u011e\3\2\2")
        buf.write("\2\u0121\u0122\b\31\1\2\u0122\u0123\5\62\32\2\u0123\u0129")
        buf.write("\3\2\2\2\u0124\u0125\f\4\2\2\u0125\u0126\t\b\2\2\u0126")
        buf.write("\u0128\5\62\32\2\u0127\u0124\3\2\2\2\u0128\u012b\3\2\2")
        buf.write("\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\61\3")
        buf.write("\2\2\2\u012b\u0129\3\2\2\2\u012c\u012d\b\32\1\2\u012d")
        buf.write("\u012e\5\64\33\2\u012e\u0134\3\2\2\2\u012f\u0130\f\4\2")
        buf.write("\2\u0130\u0131\t\t\2\2\u0131\u0133\5\64\33\2\u0132\u012f")
        buf.write("\3\2\2\2\u0133\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0134")
        buf.write("\u0135\3\2\2\2\u0135\63\3\2\2\2\u0136\u0134\3\2\2\2\u0137")
        buf.write("\u0138\7\31\2\2\u0138\u013b\5\64\33\2\u0139\u013b\5\66")
        buf.write("\34\2\u013a\u0137\3\2\2\2\u013a\u0139\3\2\2\2\u013b\65")
        buf.write("\3\2\2\2\u013c\u013d\7 \2\2\u013d\u0140\5\66\34\2\u013e")
        buf.write("\u0140\58\35\2\u013f\u013c\3\2\2\2\u013f\u013e\3\2\2\2")
        buf.write("\u0140\67\3\2\2\2\u0141\u0142\b\35\1\2\u0142\u0143\5:")
        buf.write("\36\2\u0143\u0148\3\2\2\2\u0144\u0145\f\4\2\2\u0145\u0147")
        buf.write("\5&\24\2\u0146\u0144\3\2\2\2\u0147\u014a\3\2\2\2\u0148")
        buf.write("\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u01499\3\2\2\2\u014a")
        buf.write("\u0148\3\2\2\2\u014b\u014c\b\36\1\2\u014c\u014d\5<\37")
        buf.write("\2\u014d\u015a\3\2\2\2\u014e\u014f\f\4\2\2\u014f\u0150")
        buf.write("\7-\2\2\u0150\u0156\7;\2\2\u0151\u0153\7)\2\2\u0152\u0154")
        buf.write("\5\"\22\2\u0153\u0152\3\2\2\2\u0153\u0154\3\2\2\2\u0154")
        buf.write("\u0155\3\2\2\2\u0155\u0157\7*\2\2\u0156\u0151\3\2\2\2")
        buf.write("\u0156\u0157\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u014e\3")
        buf.write("\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b")
        buf.write("\3\2\2\2\u015b;\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e")
        buf.write("\7;\2\2\u015e\u015f\7\61\2\2\u015f\u0165\7<\2\2\u0160")
        buf.write("\u0162\7)\2\2\u0161\u0163\5\"\22\2\u0162\u0161\3\2\2\2")
        buf.write("\u0162\u0163\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0166\7")
        buf.write("*\2\2\u0165\u0160\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0169")
        buf.write("\3\2\2\2\u0167\u0169\5> \2\u0168\u015d\3\2\2\2\u0168\u0167")
        buf.write("\3\2\2\2\u0169=\3\2\2\2\u016a\u016b\7\26\2\2\u016b\u016c")
        buf.write("\7;\2\2\u016c\u016e\7)\2\2\u016d\u016f\5\"\22\2\u016e")
        buf.write("\u016d\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0173\7*\2\2\u0171\u0173\5@!\2\u0172\u016a\3\2")
        buf.write("\2\2\u0172\u0171\3\2\2\2\u0173?\3\2\2\2\u0174\u017d\5")
        buf.write("f\64\2\u0175\u017d\7\r\2\2\u0176\u017d\7\16\2\2\u0177")
        buf.write("\u017d\7;\2\2\u0178\u0179\7)\2\2\u0179\u017a\5*\26\2\u017a")
        buf.write("\u017b\7*\2\2\u017b\u017d\3\2\2\2\u017c\u0174\3\2\2\2")
        buf.write("\u017c\u0175\3\2\2\2\u017c\u0176\3\2\2\2\u017c\u0177\3")
        buf.write("\2\2\2\u017c\u0178\3\2\2\2\u017dA\3\2\2\2\u017e\u017f")
        buf.write("\t\4\2\2\u017f\u0180\5\36\20\2\u0180\u0181\7\60\2\2\u0181")
        buf.write("\u0182\5\32\16\2\u0182\u0183\7\62\2\2\u0183\u018b\3\2")
        buf.write("\2\2\u0184\u0185\t\4\2\2\u0185\u0186\7;\2\2\u0186\u0187")
        buf.write("\5D#\2\u0187\u0188\5*\26\2\u0188\u0189\7\62\2\2\u0189")
        buf.write("\u018b\3\2\2\2\u018a\u017e\3\2\2\2\u018a\u0184\3\2\2\2")
        buf.write("\u018bC\3\2\2\2\u018c\u018d\7\60\2\2\u018d\u018e\5\32")
        buf.write("\16\2\u018e\u018f\7\30\2\2\u018f\u0197\3\2\2\2\u0190\u0191")
        buf.write("\7/\2\2\u0191\u0192\7;\2\2\u0192\u0193\5D#\2\u0193\u0194")
        buf.write("\5*\26\2\u0194\u0195\7/\2\2\u0195\u0197\3\2\2\2\u0196")
        buf.write("\u018c\3\2\2\2\u0196\u0190\3\2\2\2\u0197E\3\2\2\2\u0198")
        buf.write("\u0199\5\\/\2\u0199\u019a\7-\2\2\u019a\u019b\7;\2\2\u019b")
        buf.write("\u01a2\3\2\2\2\u019c\u019d\7;\2\2\u019d\u019e\7\61\2\2")
        buf.write("\u019e\u01a2\7<\2\2\u019f\u01a2\7;\2\2\u01a0\u01a2\5$")
        buf.write("\23\2\u01a1\u0198\3\2\2\2\u01a1\u019c\3\2\2\2\u01a1\u019f")
        buf.write("\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2G\3\2\2\2\u01a3\u01a4")
        buf.write("\5F$\2\u01a4\u01a5\7\30\2\2\u01a5\u01a6\5*\26\2\u01a6")
        buf.write("\u01a7\7\62\2\2\u01a7I\3\2\2\2\u01a8\u01ac\5L\'\2\u01a9")
        buf.write("\u01ab\5N(\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01b0\3\2\2\2")
        buf.write("\u01ae\u01ac\3\2\2\2\u01af\u01b1\5P)\2\u01b0\u01af\3\2")
        buf.write("\2\2\u01b0\u01b1\3\2\2\2\u01b1K\3\2\2\2\u01b2\u01b3\7")
        buf.write("\6\2\2\u01b3\u01b4\7)\2\2\u01b4\u01b5\5*\26\2\u01b5\u01b6")
        buf.write("\7*\2\2\u01b6\u01b7\5b\62\2\u01b7M\3\2\2\2\u01b8\u01b9")
        buf.write("\7\7\2\2\u01b9\u01ba\7)\2\2\u01ba\u01bb\5*\26\2\u01bb")
        buf.write("\u01bc\7*\2\2\u01bc\u01bd\5b\62\2\u01bdO\3\2\2\2\u01be")
        buf.write("\u01bf\7\b\2\2\u01bf\u01c0\5b\62\2\u01c0Q\3\2\2\2\u01c1")
        buf.write("\u01c2\7\t\2\2\u01c2\u01c3\7)\2\2\u01c3\u01c4\5T+\2\u01c4")
        buf.write("\u01c5\7*\2\2\u01c5\u01c6\5b\62\2\u01c6S\3\2\2\2\u01c7")
        buf.write("\u01c8\5\\/\2\u01c8\u01c9\7\13\2\2\u01c9\u01ca\5*\26\2")
        buf.write("\u01ca\u01cb\7.\2\2\u01cb\u01ce\5*\26\2\u01cc\u01cd\7")
        buf.write("\27\2\2\u01cd\u01cf\5*\26\2\u01ce\u01cc\3\2\2\2\u01ce")
        buf.write("\u01cf\3\2\2\2\u01cfU\3\2\2\2\u01d0\u01d1\7\4\2\2\u01d1")
        buf.write("\u01d2\7\62\2\2\u01d2W\3\2\2\2\u01d3\u01d4\7\5\2\2\u01d4")
        buf.write("\u01d5\7\62\2\2\u01d5Y\3\2\2\2\u01d6\u01d8\7\f\2\2\u01d7")
        buf.write("\u01d9\5*\26\2\u01d8\u01d7\3\2\2\2\u01d8\u01d9\3\2\2\2")
        buf.write("\u01d9\u01da\3\2\2\2\u01da\u01db\7\62\2\2\u01db[\3\2\2")
        buf.write("\2\u01dc\u01dd\b/\1\2\u01dd\u01e0\5^\60\2\u01de\u01e0")
        buf.write("\5> \2\u01df\u01dc\3\2\2\2\u01df\u01de\3\2\2\2\u01e0\u01ed")
        buf.write("\3\2\2\2\u01e1\u01e2\f\5\2\2\u01e2\u01e3\7-\2\2\u01e3")
        buf.write("\u01e9\7;\2\2\u01e4\u01e6\7)\2\2\u01e5\u01e7\5\"\22\2")
        buf.write("\u01e6\u01e5\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\3")
        buf.write("\2\2\2\u01e8\u01ea\7*\2\2\u01e9\u01e4\3\2\2\2\u01e9\u01ea")
        buf.write("\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01e1\3\2\2\2\u01ec")
        buf.write("\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ee]\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f1\7;\2\2")
        buf.write("\u01f1\u01f9\7\61\2\2\u01f2\u01fa\7<\2\2\u01f3\u01f4\7")
        buf.write("<\2\2\u01f4\u01f6\7)\2\2\u01f5\u01f7\5\"\22\2\u01f6\u01f5")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8")
        buf.write("\u01fa\7*\2\2\u01f9\u01f2\3\2\2\2\u01f9\u01f3\3\2\2\2")
        buf.write("\u01f9\u01fa\3\2\2\2\u01fa_\3\2\2\2\u01fb\u01fc\5\\/\2")
        buf.write("\u01fc\u01fd\7-\2\2\u01fd\u01fe\7;\2\2\u01fe\u0200\7)")
        buf.write("\2\2\u01ff\u0201\5\"\22\2\u0200\u01ff\3\2\2\2\u0200\u0201")
        buf.write("\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0203\7*\2\2\u0203")
        buf.write("\u020d\3\2\2\2\u0204\u0205\7;\2\2\u0205\u0206\7\61\2\2")
        buf.write("\u0206\u0207\7<\2\2\u0207\u0209\7)\2\2\u0208\u020a\5\"")
        buf.write("\22\2\u0209\u0208\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020b")
        buf.write("\3\2\2\2\u020b\u020d\7*\2\2\u020c\u01fb\3\2\2\2\u020c")
        buf.write("\u0204\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f\7\62\2")
        buf.write("\2\u020fa\3\2\2\2\u0210\u0214\7\63\2\2\u0211\u0213\5d")
        buf.write("\63\2\u0212\u0211\3\2\2\2\u0213\u0216\3\2\2\2\u0214\u0212")
        buf.write("\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0217\3\2\2\2\u0216")
        buf.write("\u0214\3\2\2\2\u0217\u0218\7\64\2\2\u0218c\3\2\2\2\u0219")
        buf.write("\u0223\5B\"\2\u021a\u0223\5H%\2\u021b\u0223\5J&\2\u021c")
        buf.write("\u0223\5R*\2\u021d\u0223\5V,\2\u021e\u0223\5X-\2\u021f")
        buf.write("\u0223\5Z.\2\u0220\u0223\5`\61\2\u0221\u0223\5b\62\2\u0222")
        buf.write("\u0219\3\2\2\2\u0222\u021a\3\2\2\2\u0222\u021b\3\2\2\2")
        buf.write("\u0222\u021c\3\2\2\2\u0222\u021d\3\2\2\2\u0222\u021e\3")
        buf.write("\2\2\2\u0222\u021f\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0221")
        buf.write("\3\2\2\2\u0223e\3\2\2\2\u0224\u022c\7\66\2\2\u0225\u022c")
        buf.write("\7\65\2\2\u0226\u022c\7\67\2\2\u0227\u022c\78\2\2\u0228")
        buf.write("\u022c\79\2\2\u0229\u022c\5h\65\2\u022a\u022c\5j\66\2")
        buf.write("\u022b\u0224\3\2\2\2\u022b\u0225\3\2\2\2\u022b\u0226\3")
        buf.write("\2\2\2\u022b\u0227\3\2\2\2\u022b\u0228\3\2\2\2\u022b\u0229")
        buf.write("\3\2\2\2\u022b\u022a\3\2\2\2\u022cg\3\2\2\2\u022d\u022e")
        buf.write("\7\n\2\2\u022e\u0261\7)\2\2\u022f\u0234\7\66\2\2\u0230")
        buf.write("\u0231\7/\2\2\u0231\u0233\7\66\2\2\u0232\u0230\3\2\2\2")
        buf.write("\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3")
        buf.write("\2\2\2\u0235\u0238\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u022f")
        buf.write("\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u0262\3\2\2\2\u0239")
        buf.write("\u023e\7\65\2\2\u023a\u023b\7/\2\2\u023b\u023d\7\65\2")
        buf.write("\2\u023c\u023a\3\2\2\2\u023d\u0240\3\2\2\2\u023e\u023c")
        buf.write("\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0262\3\2\2\2\u0240")
        buf.write("\u023e\3\2\2\2\u0241\u0246\7\67\2\2\u0242\u0243\7/\2\2")
        buf.write("\u0243\u0245\7\67\2\2\u0244\u0242\3\2\2\2\u0245\u0248")
        buf.write("\3\2\2\2\u0246\u0244\3\2\2\2\u0246\u0247\3\2\2\2\u0247")
        buf.write("\u0262\3\2\2\2\u0248\u0246\3\2\2\2\u0249\u024e\78\2\2")
        buf.write("\u024a\u024b\7/\2\2\u024b\u024d\78\2\2\u024c\u024a\3\2")
        buf.write("\2\2\u024d\u0250\3\2\2\2\u024e\u024c\3\2\2\2\u024e\u024f")
        buf.write("\3\2\2\2\u024f\u0262\3\2\2\2\u0250\u024e\3\2\2\2\u0251")
        buf.write("\u0256\79\2\2\u0252\u0253\7/\2\2\u0253\u0255\79\2\2\u0254")
        buf.write("\u0252\3\2\2\2\u0255\u0258\3\2\2\2\u0256\u0254\3\2\2\2")
        buf.write("\u0256\u0257\3\2\2\2\u0257\u0262\3\2\2\2\u0258\u0256\3")
        buf.write("\2\2\2\u0259\u025e\5h\65\2\u025a\u025b\7/\2\2\u025b\u025d")
        buf.write("\5h\65\2\u025c\u025a\3\2\2\2\u025d\u0260\3\2\2\2\u025e")
        buf.write("\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u0262\3\2\2\2")
        buf.write("\u0260\u025e\3\2\2\2\u0261\u0237\3\2\2\2\u0261\u0239\3")
        buf.write("\2\2\2\u0261\u0241\3\2\2\2\u0261\u0249\3\2\2\2\u0261\u0251")
        buf.write("\3\2\2\2\u0261\u0259\3\2\2\2\u0262\u0263\3\2\2\2\u0263")
        buf.write("\u0264\7*\2\2\u0264i\3\2\2\2\u0265\u0266\7\n\2\2\u0266")
        buf.write("\u026f\7)\2\2\u0267\u026c\5h\65\2\u0268\u0269\7/\2\2\u0269")
        buf.write("\u026b\5h\65\2\u026a\u0268\3\2\2\2\u026b\u026e\3\2\2\2")
        buf.write("\u026c\u026a\3\2\2\2\u026c\u026d\3\2\2\2\u026d\u0270\3")
        buf.write("\2\2\2\u026e\u026c\3\2\2\2\u026f\u0267\3\2\2\2\u026f\u0270")
        buf.write("\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u0272\7*\2\2\u0272")
        buf.write("k\3\2\2\2\u0273\u0274\7\n\2\2\u0274\u0277\7+\2\2\u0275")
        buf.write("\u0278\7:\2\2\u0276\u0278\5l\67\2\u0277\u0275\3\2\2\2")
        buf.write("\u0277\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279\u027a\7")
        buf.write("/\2\2\u027a\u027b\7\65\2\2\u027b\u027c\7,\2\2\u027cm\3")
        buf.write("\2\2\2Eqw}\u0083\u008c\u0092\u009a\u00a3\u00a8\u00ae\u00b3")
        buf.write("\u00c2\u00cc\u00d4\u00df\u00e2\u00eb\u00f6\u00f8\u0103")
        buf.write("\u010d\u0114\u011e\u0129\u0134\u013a\u013f\u0148\u0153")
        buf.write("\u0156\u015a\u0162\u0165\u0168\u016e\u0172\u017c\u018a")
        buf.write("\u0196\u01a1\u01ac\u01b0\u01ce\u01d8\u01df\u01e6\u01e9")
        buf.write("\u01ed\u01f6\u01f9\u0200\u0209\u020c\u0214\u0222\u022b")
        buf.write("\u0234\u0237\u023e\u0246\u024e\u0256\u025e\u0261\u026c")
        buf.write("\u026f\u0277")
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
    RULE_varValValueList = 33
    RULE_lhs = 34
    RULE_assignStatement = 35
    RULE_ifStatement = 36
    RULE_ifPart = 37
    RULE_elseIfPart = 38
    RULE_elsePart = 39
    RULE_forInStatement = 40
    RULE_loopPart = 41
    RULE_breakStatement = 42
    RULE_continueStatement = 43
    RULE_returnStatement = 44
    RULE_memberAccessInstance = 45
    RULE_memberAccessStatic = 46
    RULE_methodInvocationStatement = 47
    RULE_blockStatement = 48
    RULE_statement = 49
    RULE_literal = 50
    RULE_indexedArray = 51
    RULE_multiDimentionalArray = 52
    RULE_arrayType = 53

    ruleNames =  [ "program", "classDeclaration", "normalClassDecl", "programClassDecl", 
                   "programClassMemDecl", "mainMethodDecl", "memberDeclaration", 
                   "methodDeclaration", "constructor", "destructor", "parameterList", 
                   "parameter", "d96Type", "attributeDeclaration", "identifierList", 
                   "mixedIdentifier", "expressionList", "elementExpression", 
                   "indexOperator", "relationalOperator", "expression", 
                   "relationalExpr", "andOrExpr", "addSubExpr", "mulAddMolExpr", 
                   "notExpr", "signExpr", "indexOperatorExpr", "instanceAccess", 
                   "staticAccess", "objectCreation", "atomExpr", "varValStatement", 
                   "varValValueList", "lhs", "assignStatement", "ifStatement", 
                   "ifPart", "elseIfPart", "elsePart", "forInStatement", 
                   "loopPart", "breakStatement", "continueStatement", "returnStatement", 
                   "memberAccessInstance", "memberAccessStatic", "methodInvocationStatement", 
                   "blockStatement", "statement", "literal", "indexedArray", 
                   "multiDimentionalArray", "arrayType" ]

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
            self.state = 109 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 108
                self.classDeclaration()
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
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.normalClassDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
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
            self.state = 119
            self.match(D96Parser.K_CLASS)
            self.state = 120
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_MAIN or _la==D96Parser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 121
                self.match(D96Parser.COLON)
                self.state = 122
                self.match(D96Parser.IDENTIFIER)


            self.state = 125
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 126
                self.memberDeclaration()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
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
            self.state = 134
            self.match(D96Parser.K_CLASS)
            self.state = 135
            self.match(D96Parser.K_PROGRAM)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 136
                self.match(D96Parser.COLON)
                self.state = 137
                self.match(D96Parser.IDENTIFIER)


            self.state = 140
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_MAIN) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 141
                self.programClassMemDecl()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
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


        def methodDeclaration(self):
            return self.getTypedRuleContext(D96Parser.MethodDeclarationContext,0)


        def mainMethodDecl(self):
            return self.getTypedRuleContext(D96Parser.MainMethodDeclContext,0)


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
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_VAL, D96Parser.K_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.attributeDeclaration()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR, D96Parser.K_DESTRUCTOR, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.methodDeclaration()
                pass
            elif token in [D96Parser.K_MAIN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.mainMethodDecl()
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
            self.state = 154
            self.match(D96Parser.K_MAIN)
            self.state = 155
            self.match(D96Parser.LEFT_PAREN)
            self.state = 156
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 157
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
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_VAL, D96Parser.K_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.attributeDeclaration()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR, D96Parser.K_DESTRUCTOR, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
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
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                _la = self._input.LA(1)
                if not(_la==D96Parser.IDENTIFIER or _la==D96Parser.DOLAR_IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 164
                self.match(D96Parser.LEFT_PAREN)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 165
                    self.parameterList()


                self.state = 168
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 169
                self.blockStatement()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.constructor()
                pass
            elif token in [D96Parser.K_DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
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
            self.state = 174
            self.match(D96Parser.K_CONSTRUCTOR)
            self.state = 175
            self.match(D96Parser.LEFT_PAREN)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDENTIFIER:
                self.state = 176
                self.parameterList()


            self.state = 179
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 180
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
            self.state = 182
            self.match(D96Parser.K_DESTRUCTOR)
            self.state = 183
            self.match(D96Parser.LEFT_PAREN)
            self.state = 184
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 185
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
            self.state = 187
            self.parameter()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI_COLON:
                self.state = 188
                self.match(D96Parser.SEMI_COLON)
                self.state = 189
                self.parameter()
                self.state = 194
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
            self.state = 195
            self.identifierList()
            self.state = 196
            self.match(D96Parser.COLON)
            self.state = 197
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
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.PRIMITIVE_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.match(D96Parser.PRIMITIVE_TYPE)
                pass
            elif token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 201
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
            self.state = 204
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 205
            self.mixedIdentifier()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 206
                self.match(D96Parser.COMMA)
                self.state = 207
                self.mixedIdentifier()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 213
            self.match(D96Parser.COLON)
            self.state = 214
            self.d96Type()
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 215
                self.match(D96Parser.OP_ASSIGN)
                self.state = 216
                self.expression()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 217
                    self.match(D96Parser.COMMA)
                    self.state = 218
                    self.expression()
                    self.state = 223
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 226
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
            self.state = 228
            self.match(D96Parser.IDENTIFIER)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 229
                self.match(D96Parser.COMMA)
                self.state = 230
                self.match(D96Parser.IDENTIFIER)
                self.state = 235
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
            self.state = 236
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
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.expression()
                self.state = 242 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 240
                    self.match(D96Parser.COMMA)
                    self.state = 241
                    self.expression()
                    self.state = 244 
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
            self.state = 248
            self.expression()
            self.state = 249
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

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.LEFT_SQUARE_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(D96Parser.RIGHT_SQUARE_BRACKET, 0)

        def indexOperator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IndexOperatorContext)
            else:
                return self.getTypedRuleContext(D96Parser.IndexOperatorContext,i)


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
            self.state = 251
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 252
            self.expression()
            self.state = 253
            self.match(D96Parser.RIGHT_SQUARE_BRACKET)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 254
                    self.indexOperator() 
                self.state = 259
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
            self.state = 260
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
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.relationalExpr()
                self.state = 263
                _la = self._input.LA(1)
                if not(_la==D96Parser.OP_STRING_CONCATENATION or _la==D96Parser.OP_TWO_SAME_STRING):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 264
                self.relationalExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
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
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.andOrExpr(0)
                self.state = 270
                self.relationalOperator()
                self.state = 271
                self.andOrExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
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
            self.state = 277
            self.addSubExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.AndOrExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andOrExpr)
                    self.state = 279
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 280
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_LOGICAL_OR or _la==D96Parser.OP_LOGICAL_AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 281
                    self.addSubExpr(0) 
                self.state = 286
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
            self.state = 288
            self.mulAddMolExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.AddSubExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addSubExpr)
                    self.state = 290
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 291
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_ADDTION or _la==D96Parser.OP_SUBTRACTION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 292
                    self.mulAddMolExpr(0) 
                self.state = 297
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
            self.state = 299
            self.notExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 306
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.MulAddMolExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mulAddMolExpr)
                    self.state = 301
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 302
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MODULO) | (1 << D96Parser.OP_MULTIPLICATION) | (1 << D96Parser.OP_DIVISION))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 303
                    self.notExpr() 
                self.state = 308
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
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(D96Parser.OP_LOGICAL_NOT)
                self.state = 310
                self.notExpr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_SELF, D96Parser.K_NEW, D96Parser.OP_SUBTRACTION, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
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
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUBTRACTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(D96Parser.OP_SUBTRACTION)
                self.state = 315
                self.signExpr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_SELF, D96Parser.K_NEW, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instanceAccess(self):
            return self.getTypedRuleContext(D96Parser.InstanceAccessContext,0)


        def indexOperatorExpr(self):
            return self.getTypedRuleContext(D96Parser.IndexOperatorExprContext,0)


        def indexOperator(self):
            return self.getTypedRuleContext(D96Parser.IndexOperatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexOperatorExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexOperatorExpr" ):
                return visitor.visitIndexOperatorExpr(self)
            else:
                return visitor.visitChildren(self)



    def indexOperatorExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.IndexOperatorExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_indexOperatorExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.instanceAccess(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.IndexOperatorExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indexOperatorExpr)
                    self.state = 322
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 323
                    self.indexOperator() 
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 330
            self.staticAccess()
            self._ctx.stop = self._input.LT(-1)
            self.state = 344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.InstanceAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instanceAccess)
                    self.state = 332
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 333
                    self.match(D96Parser.DOT)
                    self.state = 334
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 340
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        self.state = 335
                        self.match(D96Parser.LEFT_PAREN)
                        self.state = 337
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                            self.state = 336
                            self.expressionList()


                        self.state = 339
                        self.match(D96Parser.RIGHT_PAREN)

             
                self.state = 346
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
            return self.getTypedRuleContext(D96Parser.ExpressionListContext,0)


        def objectCreation(self):
            return self.getTypedRuleContext(D96Parser.ObjectCreationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_staticAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticAccess" ):
                return visitor.visitStaticAccess(self)
            else:
                return visitor.visitChildren(self)




    def staticAccess(self):

        localctx = D96Parser.StaticAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_staticAccess)
        self._la = 0 # Token type
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(D96Parser.IDENTIFIER)
                self.state = 348
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 349
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 355
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 350
                    self.match(D96Parser.LEFT_PAREN)
                    self.state = 352
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                        self.state = 351
                        self.expressionList()


                    self.state = 354
                    self.match(D96Parser.RIGHT_PAREN)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
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
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(D96Parser.K_NEW)
                self.state = 361
                self.match(D96Parser.IDENTIFIER)
                self.state = 362
                self.match(D96Parser.LEFT_PAREN)
                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 363
                    self.expressionList()


                self.state = 366
                self.match(D96Parser.RIGHT_PAREN)
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_SELF, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
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
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_ARRAY, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.literal()
                pass
            elif token in [D96Parser.K_NULL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.match(D96Parser.K_NULL)
                pass
            elif token in [D96Parser.K_SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 372
                self.match(D96Parser.K_SELF)
                pass
            elif token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 373
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 374
                self.match(D96Parser.LEFT_PAREN)
                self.state = 375
                self.expression()
                self.state = 376
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

        def identifierList(self):
            return self.getTypedRuleContext(D96Parser.IdentifierListContext,0)


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

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def varValValueList(self):
            return self.getTypedRuleContext(D96Parser.VarValValueListContext,0)


        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


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
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                _la = self._input.LA(1)
                if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 381
                self.identifierList()
                self.state = 382
                self.match(D96Parser.COLON)
                self.state = 383
                self.d96Type()
                self.state = 384
                self.match(D96Parser.SEMI_COLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                _la = self._input.LA(1)
                if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 387
                self.match(D96Parser.IDENTIFIER)
                self.state = 388
                self.varValValueList()
                self.state = 389
                self.expression()
                self.state = 390
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def d96Type(self):
            return self.getTypedRuleContext(D96Parser.D96TypeContext,0)


        def OP_ASSIGN(self):
            return self.getToken(D96Parser.OP_ASSIGN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def IDENTIFIER(self):
            return self.getToken(D96Parser.IDENTIFIER, 0)

        def varValValueList(self):
            return self.getTypedRuleContext(D96Parser.VarValValueListContext,0)


        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_varValValueList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarValValueList" ):
                return visitor.visitVarValValueList(self)
            else:
                return visitor.visitChildren(self)




    def varValValueList(self):

        localctx = D96Parser.VarValValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_varValValueList)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(D96Parser.COLON)
                self.state = 395
                self.d96Type()
                self.state = 396
                self.match(D96Parser.OP_ASSIGN)
                pass
            elif token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.match(D96Parser.COMMA)
                self.state = 399
                self.match(D96Parser.IDENTIFIER)
                self.state = 400
                self.varValValueList()
                self.state = 401
                self.expression()
                self.state = 402
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

        def memberAccessInstance(self):
            return self.getTypedRuleContext(D96Parser.MemberAccessInstanceContext,0)


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
        self.enterRule(localctx, 68, self.RULE_lhs)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.memberAccessInstance(0)
                self.state = 407
                self.match(D96Parser.DOT)
                self.state = 408
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.match(D96Parser.IDENTIFIER)
                self.state = 411
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 412
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 413
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 414
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
        self.enterRule(localctx, 70, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.lhs()
            self.state = 418
            self.match(D96Parser.OP_ASSIGN)
            self.state = 419
            self.expression()
            self.state = 420
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

        def ifPart(self):
            return self.getTypedRuleContext(D96Parser.IfPartContext,0)


        def elseIfPart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ElseIfPartContext)
            else:
                return self.getTypedRuleContext(D96Parser.ElseIfPartContext,i)


        def elsePart(self):
            return self.getTypedRuleContext(D96Parser.ElsePartContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = D96Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.ifPart()
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.K_ELSE_IF:
                self.state = 423
                self.elseIfPart()
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ELSE:
                self.state = 429
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


        def getRuleIndex(self):
            return D96Parser.RULE_ifPart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfPart" ):
                return visitor.visitIfPart(self)
            else:
                return visitor.visitChildren(self)




    def ifPart(self):

        localctx = D96Parser.IfPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ifPart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(D96Parser.K_IF)
            self.state = 433
            self.match(D96Parser.LEFT_PAREN)
            self.state = 434
            self.expression()
            self.state = 435
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 436
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

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseIfPart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfPart" ):
                return visitor.visitElseIfPart(self)
            else:
                return visitor.visitChildren(self)




    def elseIfPart(self):

        localctx = D96Parser.ElseIfPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_elseIfPart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(D96Parser.K_ELSE_IF)
            self.state = 439
            self.match(D96Parser.LEFT_PAREN)
            self.state = 440
            self.expression()
            self.state = 441
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 442
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ELSE(self):
            return self.getToken(D96Parser.K_ELSE, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elsePart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsePart" ):
                return visitor.visitElsePart(self)
            else:
                return visitor.visitChildren(self)




    def elsePart(self):

        localctx = D96Parser.ElsePartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_elsePart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(D96Parser.K_ELSE)
            self.state = 445
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_FOR_EACH(self):
            return self.getToken(D96Parser.K_FOR_EACH, 0)

        def LEFT_PAREN(self):
            return self.getToken(D96Parser.LEFT_PAREN, 0)

        def loopPart(self):
            return self.getTypedRuleContext(D96Parser.LoopPartContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(D96Parser.RIGHT_PAREN, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_forInStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInStatement" ):
                return visitor.visitForInStatement(self)
            else:
                return visitor.visitChildren(self)




    def forInStatement(self):

        localctx = D96Parser.ForInStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_forInStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(D96Parser.K_FOR_EACH)
            self.state = 448
            self.match(D96Parser.LEFT_PAREN)
            self.state = 449
            self.loopPart()
            self.state = 450
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 451
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberAccessInstance(self):
            return self.getTypedRuleContext(D96Parser.MemberAccessInstanceContext,0)


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
            return D96Parser.RULE_loopPart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopPart" ):
                return visitor.visitLoopPart(self)
            else:
                return visitor.visitChildren(self)




    def loopPart(self):

        localctx = D96Parser.LoopPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_loopPart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.memberAccessInstance(0)
            self.state = 454
            self.match(D96Parser.K_IN)
            self.state = 455
            self.expression()
            self.state = 456
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 457
            self.expression()
            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_BY:
                self.state = 458
                self.match(D96Parser.K_BY)
                self.state = 459
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
        self.enterRule(localctx, 84, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(D96Parser.K_BREAK)
            self.state = 463
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
        self.enterRule(localctx, 86, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(D96Parser.K_CONTINUE)
            self.state = 466
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
        self.enterRule(localctx, 88, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(D96Parser.K_RETURN)
            self.state = 470
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 469
                self.expression()


            self.state = 472
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberAccessStatic(self):
            return self.getTypedRuleContext(D96Parser.MemberAccessStaticContext,0)


        def objectCreation(self):
            return self.getTypedRuleContext(D96Parser.ObjectCreationContext,0)


        def memberAccessInstance(self):
            return self.getTypedRuleContext(D96Parser.MemberAccessInstanceContext,0)


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
            return D96Parser.RULE_memberAccessInstance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberAccessInstance" ):
                return visitor.visitMemberAccessInstance(self)
            else:
                return visitor.visitChildren(self)



    def memberAccessInstance(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.MemberAccessInstanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_memberAccessInstance, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 475
                self.memberAccessStatic()
                pass

            elif la_ == 2:
                self.state = 476
                self.objectCreation()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 491
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.MemberAccessInstanceContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_memberAccessInstance)
                    self.state = 479
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 480
                    self.match(D96Parser.DOT)
                    self.state = 481
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 487
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        self.state = 482
                        self.match(D96Parser.LEFT_PAREN)
                        self.state = 484
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                            self.state = 483
                            self.expressionList()


                        self.state = 486
                        self.match(D96Parser.RIGHT_PAREN)

             
                self.state = 493
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MemberAccessStaticContext(ParserRuleContext):
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

        def expressionList(self):
            return self.getTypedRuleContext(D96Parser.ExpressionListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_memberAccessStatic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberAccessStatic" ):
                return visitor.visitMemberAccessStatic(self)
            else:
                return visitor.visitChildren(self)




    def memberAccessStatic(self):

        localctx = D96Parser.MemberAccessStaticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_memberAccessStatic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(D96Parser.IDENTIFIER)
            self.state = 495
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 496
                self.match(D96Parser.DOLAR_IDENTIFIER)

            elif la_ == 2:
                self.state = 497
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 498
                self.match(D96Parser.LEFT_PAREN)
                self.state = 500
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 499
                    self.expressionList()


                self.state = 502
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def memberAccessInstance(self):
            return self.getTypedRuleContext(D96Parser.MemberAccessInstanceContext,0)


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
            return self.getTypedRuleContext(D96Parser.ExpressionListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methodInvocationStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodInvocationStatement" ):
                return visitor.visitMethodInvocationStatement(self)
            else:
                return visitor.visitChildren(self)




    def methodInvocationStatement(self):

        localctx = D96Parser.MethodInvocationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_methodInvocationStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 505
                self.memberAccessInstance(0)
                self.state = 506
                self.match(D96Parser.DOT)
                self.state = 507
                self.match(D96Parser.IDENTIFIER)
                self.state = 508
                self.match(D96Parser.LEFT_PAREN)
                self.state = 510
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 509
                    self.expressionList()


                self.state = 512
                self.match(D96Parser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.state = 514
                self.match(D96Parser.IDENTIFIER)
                self.state = 515
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 516
                self.match(D96Parser.DOLAR_IDENTIFIER)
                self.state = 517
                self.match(D96Parser.LEFT_PAREN)
                self.state = 519
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 518
                    self.expressionList()


                self.state = 521
                self.match(D96Parser.RIGHT_PAREN)
                pass


            self.state = 524
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
        self.enterRule(localctx, 96, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 530
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_BREAK) | (1 << D96Parser.K_CONTINUE) | (1 << D96Parser.K_IF) | (1 << D96Parser.K_FOR_EACH) | (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_RETURN) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.LEFT_CURLY_BRACKET) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 527
                self.statement()
                self.state = 532
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 533
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
        self.enterRule(localctx, 98, self.RULE_statement)
        try:
            self.state = 544
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.varValStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.assignStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 537
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 538
                self.forInStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 539
                self.breakStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 540
                self.continueStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 541
                self.returnStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 542
                self.methodInvocationStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 543
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
        self.enterRule(localctx, 100, self.RULE_literal)
        try:
            self.state = 553
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.match(D96Parser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 547
                self.match(D96Parser.INTEGER_LITERAL2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 548
                self.match(D96Parser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 549
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 550
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 551
                self.indexedArray()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 552
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
        self.enterRule(localctx, 102, self.RULE_indexedArray)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(D96Parser.K_ARRAY)
            self.state = 556
            self.match(D96Parser.LEFT_PAREN)
            self.state = 607
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RIGHT_PAREN, D96Parser.INTEGER_LITERAL]:
                self.state = 565
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.INTEGER_LITERAL:
                    self.state = 557
                    self.match(D96Parser.INTEGER_LITERAL)
                    self.state = 562
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.COMMA:
                        self.state = 558
                        self.match(D96Parser.COMMA)
                        self.state = 559
                        self.match(D96Parser.INTEGER_LITERAL)
                        self.state = 564
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                pass
            elif token in [D96Parser.INTEGER_LITERAL2]:
                self.state = 567
                self.match(D96Parser.INTEGER_LITERAL2)
                self.state = 572
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 568
                    self.match(D96Parser.COMMA)
                    self.state = 569
                    self.match(D96Parser.INTEGER_LITERAL2)
                    self.state = 574
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.state = 575
                self.match(D96Parser.FLOAT_LITERAL)
                self.state = 580
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 576
                    self.match(D96Parser.COMMA)
                    self.state = 577
                    self.match(D96Parser.FLOAT_LITERAL)
                    self.state = 582
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.state = 583
                self.match(D96Parser.BOOLEAN_LITERAL)
                self.state = 588
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 584
                    self.match(D96Parser.COMMA)
                    self.state = 585
                    self.match(D96Parser.BOOLEAN_LITERAL)
                    self.state = 590
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.state = 591
                self.match(D96Parser.STRING_LITERAL)
                self.state = 596
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 592
                    self.match(D96Parser.COMMA)
                    self.state = 593
                    self.match(D96Parser.STRING_LITERAL)
                    self.state = 598
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 599
                self.indexedArray()
                self.state = 604
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 600
                    self.match(D96Parser.COMMA)
                    self.state = 601
                    self.indexedArray()
                    self.state = 606
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 609
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
        self.enterRule(localctx, 104, self.RULE_multiDimentionalArray)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.match(D96Parser.K_ARRAY)
            self.state = 612
            self.match(D96Parser.LEFT_PAREN)

            self.state = 621
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_ARRAY:
                self.state = 613
                self.indexedArray()
                self.state = 618
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 614
                    self.match(D96Parser.COMMA)
                    self.state = 615
                    self.indexedArray()
                    self.state = 620
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 623
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
        self.enterRule(localctx, 106, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self.match(D96Parser.K_ARRAY)
            self.state = 626
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 629
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.PRIMITIVE_TYPE]:
                self.state = 627
                self.match(D96Parser.PRIMITIVE_TYPE)
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 628
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 631
            self.match(D96Parser.COMMA)
            self.state = 632
            self.match(D96Parser.INTEGER_LITERAL2)
            self.state = 633
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
        self._predicates[27] = self.indexOperatorExpr_sempred
        self._predicates[28] = self.instanceAccess_sempred
        self._predicates[45] = self.memberAccessInstance_sempred
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
         

    def indexOperatorExpr_sempred(self, localctx:IndexOperatorExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def instanceAccess_sempred(self, localctx:InstanceAccessContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def memberAccessInstance_sempred(self, localctx:MemberAccessInstanceContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         




