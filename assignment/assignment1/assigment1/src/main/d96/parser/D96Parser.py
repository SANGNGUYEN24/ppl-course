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
        buf.write("\u0223\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\6\2`\n\2\r\2\16\2a\3\2\3\2\3\3\3\3\5\3h\n\3\3")
        buf.write("\4\3\4\3\4\3\4\5\4n\n\4\3\4\3\4\7\4r\n\4\f\4\16\4u\13")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5}\n\5\3\5\3\5\7\5\u0081")
        buf.write("\n\5\f\5\16\5\u0084\13\5\3\5\3\5\3\6\3\6\3\6\5\6\u008b")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u0094\n\b\3\t\3\t")
        buf.write("\3\t\5\t\u0099\n\t\3\t\3\t\3\t\3\t\5\t\u009f\n\t\3\n\3")
        buf.write("\n\3\n\5\n\u00a4\n\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\7\f\u00b1\n\f\f\f\16\f\u00b4\13\f\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\5\16\u00bd\n\16\3\17\3\17")
        buf.write("\3\17\3\17\7\17\u00c3\n\17\f\17\16\17\u00c6\13\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\7\17\u00ce\n\17\f\17\16\17\u00d1")
        buf.write("\13\17\5\17\u00d3\n\17\3\17\3\17\3\20\3\20\3\20\7\20\u00da")
        buf.write("\n\20\f\20\16\20\u00dd\13\20\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\6\22\u00e5\n\22\r\22\16\22\u00e6\5\22\u00e9\n\22")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\6\24\u00f2\n\24\r")
        buf.write("\24\16\24\u00f3\3\25\3\25\3\26\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u00fd\n\26\3\27\3\27\3\27\3\27\3\27\5\27\u0104\n\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\7\30\u010c\n\30\f\30\16\30")
        buf.write("\u010f\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0117")
        buf.write("\n\31\f\31\16\31\u011a\13\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\7\32\u0122\n\32\f\32\16\32\u0125\13\32\3\33\3\33")
        buf.write("\3\33\5\33\u012a\n\33\3\34\3\34\3\34\5\34\u012f\n\34\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u0135\n\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u013f\n\36\3\36\5\36\u0142\n")
        buf.write("\36\7\36\u0144\n\36\f\36\16\36\u0147\13\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\5\37\u0151\n\37\3\37\5\37")
        buf.write("\u0154\n\37\7\37\u0156\n\37\f\37\16\37\u0159\13\37\3 ")
        buf.write("\3 \3 \3 \5 \u015f\n \3 \3 \5 \u0163\n \3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\5!\u016d\n!\3\"\3\"\3\"\3\"\7\"\u0173\n\"\f")
        buf.write("\"\16\"\u0176\13\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u017e\n")
        buf.write("\"\f\"\16\"\u0181\13\"\5\"\u0183\n\"\3\"\3\"\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\5#\u0191\n#\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01a6\n%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\5&\u01b1\n&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\5)\u01be\n)\3)\3)\3*\3*\3*\3+\3+\7+")
        buf.write("\u01c7\n+\f+\16+\u01ca\13+\3+\3+\3,\3,\3,\3,\3,\3,\3,")
        buf.write("\3,\3,\5,\u01d7\n,\3-\3-\3-\3-\3-\3-\5-\u01df\n-\3.\3")
        buf.write(".\3.\3.\3.\7.\u01e6\n.\f.\16.\u01e9\13.\5.\u01eb\n.\3")
        buf.write(".\3.\3.\7.\u01f0\n.\f.\16.\u01f3\13.\3.\3.\3.\7.\u01f8")
        buf.write("\n.\f.\16.\u01fb\13.\3.\3.\3.\7.\u0200\n.\f.\16.\u0203")
        buf.write("\13.\3.\3.\3.\7.\u0208\n.\f.\16.\u020b\13.\3.\3.\3.\7")
        buf.write(".\u0210\n.\f.\16.\u0213\13.\5.\u0215\n.\3.\3.\3/\3/\3")
        buf.write("/\3/\5/\u021d\n/\3/\3/\3/\3/\3/\2\7.\60\62:<\60\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\\2\13\4\2\17\17;;\4\2\17\17;<\3\2")
        buf.write("\22\23\3\2;<\4\2\34\35#&\3\2\'(\3\2\32\33\3\2\37 \4\2")
        buf.write("\36\36!\"\2\u0244\2_\3\2\2\2\4g\3\2\2\2\6i\3\2\2\2\bx")
        buf.write("\3\2\2\2\n\u008a\3\2\2\2\f\u008c\3\2\2\2\16\u0093\3\2")
        buf.write("\2\2\20\u009e\3\2\2\2\22\u00a0\3\2\2\2\24\u00a8\3\2\2")
        buf.write("\2\26\u00ad\3\2\2\2\30\u00b5\3\2\2\2\32\u00bc\3\2\2\2")
        buf.write("\34\u00be\3\2\2\2\36\u00d6\3\2\2\2 \u00de\3\2\2\2\"\u00e8")
        buf.write("\3\2\2\2$\u00ea\3\2\2\2&\u00f1\3\2\2\2(\u00f5\3\2\2\2")
        buf.write("*\u00fc\3\2\2\2,\u0103\3\2\2\2.\u0105\3\2\2\2\60\u0110")
        buf.write("\3\2\2\2\62\u011b\3\2\2\2\64\u0129\3\2\2\2\66\u012e\3")
        buf.write("\2\2\28\u0134\3\2\2\2:\u0136\3\2\2\2<\u0148\3\2\2\2>\u0162")
        buf.write("\3\2\2\2@\u016c\3\2\2\2B\u016e\3\2\2\2D\u0190\3\2\2\2")
        buf.write("F\u0192\3\2\2\2H\u01a5\3\2\2\2J\u01a7\3\2\2\2L\u01b5\3")
        buf.write("\2\2\2N\u01b8\3\2\2\2P\u01bb\3\2\2\2R\u01c1\3\2\2\2T\u01c4")
        buf.write("\3\2\2\2V\u01d6\3\2\2\2X\u01de\3\2\2\2Z\u01e0\3\2\2\2")
        buf.write("\\\u0218\3\2\2\2^`\5\4\3\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2")
        buf.write("\2ab\3\2\2\2bc\3\2\2\2cd\7\2\2\3d\3\3\2\2\2eh\5\6\4\2")
        buf.write("fh\5\b\5\2ge\3\2\2\2gf\3\2\2\2h\5\3\2\2\2ij\7\21\2\2j")
        buf.write("m\t\2\2\2kl\7\60\2\2ln\7;\2\2mk\3\2\2\2mn\3\2\2\2no\3")
        buf.write("\2\2\2os\7\63\2\2pr\5\16\b\2qp\3\2\2\2ru\3\2\2\2sq\3\2")
        buf.write("\2\2st\3\2\2\2tv\3\2\2\2us\3\2\2\2vw\7\64\2\2w\7\3\2\2")
        buf.write("\2xy\7\21\2\2y|\7\20\2\2z{\7\60\2\2{}\7;\2\2|z\3\2\2\2")
        buf.write("|}\3\2\2\2}~\3\2\2\2~\u0082\7\63\2\2\177\u0081\5\n\6\2")
        buf.write("\u0080\177\3\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2")
        buf.write("\2\2\u0082\u0083\3\2\2\2\u0083\u0085\3\2\2\2\u0084\u0082")
        buf.write("\3\2\2\2\u0085\u0086\7\64\2\2\u0086\t\3\2\2\2\u0087\u008b")
        buf.write("\5\34\17\2\u0088\u008b\5\f\7\2\u0089\u008b\5\20\t\2\u008a")
        buf.write("\u0087\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u0089\3\2\2\2")
        buf.write("\u008b\13\3\2\2\2\u008c\u008d\7\17\2\2\u008d\u008e\7)")
        buf.write("\2\2\u008e\u008f\7*\2\2\u008f\u0090\5T+\2\u0090\r\3\2")
        buf.write("\2\2\u0091\u0094\5\34\17\2\u0092\u0094\5\20\t\2\u0093")
        buf.write("\u0091\3\2\2\2\u0093\u0092\3\2\2\2\u0094\17\3\2\2\2\u0095")
        buf.write("\u0096\t\3\2\2\u0096\u0098\7)\2\2\u0097\u0099\5\26\f\2")
        buf.write("\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\3")
        buf.write("\2\2\2\u009a\u009b\7*\2\2\u009b\u009f\5T+\2\u009c\u009f")
        buf.write("\5\22\n\2\u009d\u009f\5\24\13\2\u009e\u0095\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f\21\3\2\2\2\u00a0")
        buf.write("\u00a1\7\24\2\2\u00a1\u00a3\7)\2\2\u00a2\u00a4\5\26\f")
        buf.write("\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5")
        buf.write("\3\2\2\2\u00a5\u00a6\7*\2\2\u00a6\u00a7\5T+\2\u00a7\23")
        buf.write("\3\2\2\2\u00a8\u00a9\7\25\2\2\u00a9\u00aa\7)\2\2\u00aa")
        buf.write("\u00ab\7*\2\2\u00ab\u00ac\5T+\2\u00ac\25\3\2\2\2\u00ad")
        buf.write("\u00b2\5\30\r\2\u00ae\u00af\7\62\2\2\u00af\u00b1\5\30")
        buf.write("\r\2\u00b0\u00ae\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\27\3\2\2\2\u00b4\u00b2")
        buf.write("\3\2\2\2\u00b5\u00b6\5\36\20\2\u00b6\u00b7\7\60\2\2\u00b7")
        buf.write("\u00b8\5\32\16\2\u00b8\31\3\2\2\2\u00b9\u00bd\7:\2\2\u00ba")
        buf.write("\u00bd\7;\2\2\u00bb\u00bd\5\\/\2\u00bc\u00b9\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\33\3\2\2\2\u00be")
        buf.write("\u00bf\t\4\2\2\u00bf\u00c4\5 \21\2\u00c0\u00c1\7/\2\2")
        buf.write("\u00c1\u00c3\5 \21\2\u00c2\u00c0\3\2\2\2\u00c3\u00c6\3")
        buf.write("\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c7")
        buf.write("\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8\7\60\2\2\u00c8")
        buf.write("\u00d2\5\32\16\2\u00c9\u00ca\7\30\2\2\u00ca\u00cf\5*\26")
        buf.write("\2\u00cb\u00cc\7/\2\2\u00cc\u00ce\5*\26\2\u00cd\u00cb")
        buf.write("\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d2\u00c9\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3")
        buf.write("\2\2\2\u00d4\u00d5\7\62\2\2\u00d5\35\3\2\2\2\u00d6\u00db")
        buf.write("\7;\2\2\u00d7\u00d8\7/\2\2\u00d8\u00da\7;\2\2\u00d9\u00d7")
        buf.write("\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\37\3\2\2\2\u00dd\u00db\3\2\2\2\u00de")
        buf.write("\u00df\t\5\2\2\u00df!\3\2\2\2\u00e0\u00e9\5*\26\2\u00e1")
        buf.write("\u00e4\5*\26\2\u00e2\u00e3\7/\2\2\u00e3\u00e5\5*\26\2")
        buf.write("\u00e4\u00e2\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e4\3")
        buf.write("\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e9\3\2\2\2\u00e8\u00e0")
        buf.write("\3\2\2\2\u00e8\u00e1\3\2\2\2\u00e9#\3\2\2\2\u00ea\u00eb")
        buf.write("\5*\26\2\u00eb\u00ec\5&\24\2\u00ec%\3\2\2\2\u00ed\u00ee")
        buf.write("\7+\2\2\u00ee\u00ef\5*\26\2\u00ef\u00f0\7,\2\2\u00f0\u00f2")
        buf.write("\3\2\2\2\u00f1\u00ed\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\'\3\2\2\2\u00f5")
        buf.write("\u00f6\t\6\2\2\u00f6)\3\2\2\2\u00f7\u00f8\5,\27\2\u00f8")
        buf.write("\u00f9\t\7\2\2\u00f9\u00fa\5,\27\2\u00fa\u00fd\3\2\2\2")
        buf.write("\u00fb\u00fd\5,\27\2\u00fc\u00f7\3\2\2\2\u00fc\u00fb\3")
        buf.write("\2\2\2\u00fd+\3\2\2\2\u00fe\u00ff\5.\30\2\u00ff\u0100")
        buf.write("\5(\25\2\u0100\u0101\5.\30\2\u0101\u0104\3\2\2\2\u0102")
        buf.write("\u0104\5.\30\2\u0103\u00fe\3\2\2\2\u0103\u0102\3\2\2\2")
        buf.write("\u0104-\3\2\2\2\u0105\u0106\b\30\1\2\u0106\u0107\5\60")
        buf.write("\31\2\u0107\u010d\3\2\2\2\u0108\u0109\f\4\2\2\u0109\u010a")
        buf.write("\t\b\2\2\u010a\u010c\5\60\31\2\u010b\u0108\3\2\2\2\u010c")
        buf.write("\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2")
        buf.write("\u010e/\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111\b\31\1")
        buf.write("\2\u0111\u0112\5\62\32\2\u0112\u0118\3\2\2\2\u0113\u0114")
        buf.write("\f\4\2\2\u0114\u0115\t\t\2\2\u0115\u0117\5\62\32\2\u0116")
        buf.write("\u0113\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0118\u0119\3\2\2\2\u0119\61\3\2\2\2\u011a\u0118\3\2")
        buf.write("\2\2\u011b\u011c\b\32\1\2\u011c\u011d\5\64\33\2\u011d")
        buf.write("\u0123\3\2\2\2\u011e\u011f\f\4\2\2\u011f\u0120\t\n\2\2")
        buf.write("\u0120\u0122\5\64\33\2\u0121\u011e\3\2\2\2\u0122\u0125")
        buf.write("\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124")
        buf.write("\63\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0127\7\31\2\2\u0127")
        buf.write("\u012a\5\64\33\2\u0128\u012a\5\66\34\2\u0129\u0126\3\2")
        buf.write("\2\2\u0129\u0128\3\2\2\2\u012a\65\3\2\2\2\u012b\u012c")
        buf.write("\t\t\2\2\u012c\u012f\5\66\34\2\u012d\u012f\58\35\2\u012e")
        buf.write("\u012b\3\2\2\2\u012e\u012d\3\2\2\2\u012f\67\3\2\2\2\u0130")
        buf.write("\u0131\5:\36\2\u0131\u0132\5&\24\2\u0132\u0135\3\2\2\2")
        buf.write("\u0133\u0135\5:\36\2\u0134\u0130\3\2\2\2\u0134\u0133\3")
        buf.write("\2\2\2\u01359\3\2\2\2\u0136\u0137\b\36\1\2\u0137\u0138")
        buf.write("\5<\37\2\u0138\u0145\3\2\2\2\u0139\u013a\f\4\2\2\u013a")
        buf.write("\u013b\7-\2\2\u013b\u0141\7;\2\2\u013c\u013e\7)\2\2\u013d")
        buf.write("\u013f\5\"\22\2\u013e\u013d\3\2\2\2\u013e\u013f\3\2\2")
        buf.write("\2\u013f\u0140\3\2\2\2\u0140\u0142\7*\2\2\u0141\u013c")
        buf.write("\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0144\3\2\2\2\u0143")
        buf.write("\u0139\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2")
        buf.write("\u0145\u0146\3\2\2\2\u0146;\3\2\2\2\u0147\u0145\3\2\2")
        buf.write("\2\u0148\u0149\b\37\1\2\u0149\u014a\5> \2\u014a\u0157")
        buf.write("\3\2\2\2\u014b\u014c\f\4\2\2\u014c\u014d\7\61\2\2\u014d")
        buf.write("\u0153\7<\2\2\u014e\u0150\7)\2\2\u014f\u0151\5\"\22\2")
        buf.write("\u0150\u014f\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0152\3")
        buf.write("\2\2\2\u0152\u0154\7*\2\2\u0153\u014e\3\2\2\2\u0153\u0154")
        buf.write("\3\2\2\2\u0154\u0156\3\2\2\2\u0155\u014b\3\2\2\2\u0156")
        buf.write("\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158=\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015b\7\26\2")
        buf.write("\2\u015b\u015c\7;\2\2\u015c\u015e\7)\2\2\u015d\u015f\5")
        buf.write("\"\22\2\u015e\u015d\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u0160\3\2\2\2\u0160\u0163\7*\2\2\u0161\u0163\5@!\2\u0162")
        buf.write("\u015a\3\2\2\2\u0162\u0161\3\2\2\2\u0163?\3\2\2\2\u0164")
        buf.write("\u016d\5X-\2\u0165\u016d\7\r\2\2\u0166\u016d\7\16\2\2")
        buf.write("\u0167\u016d\7;\2\2\u0168\u0169\7)\2\2\u0169\u016a\5*")
        buf.write("\26\2\u016a\u016b\7*\2\2\u016b\u016d\3\2\2\2\u016c\u0164")
        buf.write("\3\2\2\2\u016c\u0165\3\2\2\2\u016c\u0166\3\2\2\2\u016c")
        buf.write("\u0167\3\2\2\2\u016c\u0168\3\2\2\2\u016dA\3\2\2\2\u016e")
        buf.write("\u016f\t\4\2\2\u016f\u0174\7;\2\2\u0170\u0171\7/\2\2\u0171")
        buf.write("\u0173\7;\2\2\u0172\u0170\3\2\2\2\u0173\u0176\3\2\2\2")
        buf.write("\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0177\3")
        buf.write("\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\7\60\2\2\u0178")
        buf.write("\u0182\5\32\16\2\u0179\u017a\7\30\2\2\u017a\u017f\5*\26")
        buf.write("\2\u017b\u017c\7/\2\2\u017c\u017e\5*\26\2\u017d\u017b")
        buf.write("\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2")
        buf.write("\u0182\u0179\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\3")
        buf.write("\2\2\2\u0184\u0185\7\62\2\2\u0185C\3\2\2\2\u0186\u0187")
        buf.write("\5:\36\2\u0187\u0188\7-\2\2\u0188\u0189\7;\2\2\u0189\u0191")
        buf.write("\3\2\2\2\u018a\u018b\5:\36\2\u018b\u018c\7\61\2\2\u018c")
        buf.write("\u018d\7<\2\2\u018d\u0191\3\2\2\2\u018e\u0191\7;\2\2\u018f")
        buf.write("\u0191\5$\23\2\u0190\u0186\3\2\2\2\u0190\u018a\3\2\2\2")
        buf.write("\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191E\3\2\2")
        buf.write("\2\u0192\u0193\5D#\2\u0193\u0194\7\30\2\2\u0194\u0195")
        buf.write("\5*\26\2\u0195\u0196\7\62\2\2\u0196G\3\2\2\2\u0197\u0198")
        buf.write("\7\6\2\2\u0198\u0199\7)\2\2\u0199\u019a\5*\26\2\u019a")
        buf.write("\u019b\7*\2\2\u019b\u019c\5T+\2\u019c\u01a6\3\2\2\2\u019d")
        buf.write("\u019e\7\7\2\2\u019e\u019f\7)\2\2\u019f\u01a0\5*\26\2")
        buf.write("\u01a0\u01a1\7*\2\2\u01a1\u01a2\5T+\2\u01a2\u01a6\3\2")
        buf.write("\2\2\u01a3\u01a4\7\b\2\2\u01a4\u01a6\5T+\2\u01a5\u0197")
        buf.write("\3\2\2\2\u01a5\u019d\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6")
        buf.write("I\3\2\2\2\u01a7\u01a8\7\t\2\2\u01a8\u01a9\7)\2\2\u01a9")
        buf.write("\u01aa\7;\2\2\u01aa\u01ab\7\13\2\2\u01ab\u01ac\5*\26\2")
        buf.write("\u01ac\u01ad\7.\2\2\u01ad\u01b0\5*\26\2\u01ae\u01af\7")
        buf.write("\27\2\2\u01af\u01b1\5*\26\2\u01b0\u01ae\3\2\2\2\u01b0")
        buf.write("\u01b1\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\7*\2\2")
        buf.write("\u01b3\u01b4\5T+\2\u01b4K\3\2\2\2\u01b5\u01b6\7\4\2\2")
        buf.write("\u01b6\u01b7\7\62\2\2\u01b7M\3\2\2\2\u01b8\u01b9\7\5\2")
        buf.write("\2\u01b9\u01ba\7\62\2\2\u01baO\3\2\2\2\u01bb\u01bd\7\f")
        buf.write("\2\2\u01bc\u01be\5*\26\2\u01bd\u01bc\3\2\2\2\u01bd\u01be")
        buf.write("\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\7\62\2\2\u01c0")
        buf.write("Q\3\2\2\2\u01c1\u01c2\5:\36\2\u01c2\u01c3\7\62\2\2\u01c3")
        buf.write("S\3\2\2\2\u01c4\u01c8\7\63\2\2\u01c5\u01c7\5V,\2\u01c6")
        buf.write("\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2")
        buf.write("\u01c8\u01c9\3\2\2\2\u01c9\u01cb\3\2\2\2\u01ca\u01c8\3")
        buf.write("\2\2\2\u01cb\u01cc\7\64\2\2\u01ccU\3\2\2\2\u01cd\u01d7")
        buf.write("\5B\"\2\u01ce\u01d7\5F$\2\u01cf\u01d7\5H%\2\u01d0\u01d7")
        buf.write("\5J&\2\u01d1\u01d7\5L\'\2\u01d2\u01d7\5N(\2\u01d3\u01d7")
        buf.write("\5P)\2\u01d4\u01d7\5R*\2\u01d5\u01d7\5T+\2\u01d6\u01cd")
        buf.write("\3\2\2\2\u01d6\u01ce\3\2\2\2\u01d6\u01cf\3\2\2\2\u01d6")
        buf.write("\u01d0\3\2\2\2\u01d6\u01d1\3\2\2\2\u01d6\u01d2\3\2\2\2")
        buf.write("\u01d6\u01d3\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3")
        buf.write("\2\2\2\u01d7W\3\2\2\2\u01d8\u01df\7\66\2\2\u01d9\u01df")
        buf.write("\7\65\2\2\u01da\u01df\7\67\2\2\u01db\u01df\78\2\2\u01dc")
        buf.write("\u01df\79\2\2\u01dd\u01df\5Z.\2\u01de\u01d8\3\2\2\2\u01de")
        buf.write("\u01d9\3\2\2\2\u01de\u01da\3\2\2\2\u01de\u01db\3\2\2\2")
        buf.write("\u01de\u01dc\3\2\2\2\u01de\u01dd\3\2\2\2\u01dfY\3\2\2")
        buf.write("\2\u01e0\u01e1\7\n\2\2\u01e1\u0214\7)\2\2\u01e2\u01e7")
        buf.write("\7\66\2\2\u01e3\u01e4\7/\2\2\u01e4\u01e6\7\66\2\2\u01e5")
        buf.write("\u01e3\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2")
        buf.write("\u01e7\u01e8\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3")
        buf.write("\2\2\2\u01ea\u01e2\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u0215")
        buf.write("\3\2\2\2\u01ec\u01f1\7\65\2\2\u01ed\u01ee\7/\2\2\u01ee")
        buf.write("\u01f0\7\65\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f3\3\2\2")
        buf.write("\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u0215")
        buf.write("\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f9\7\67\2\2\u01f5")
        buf.write("\u01f6\7/\2\2\u01f6\u01f8\7\67\2\2\u01f7\u01f5\3\2\2\2")
        buf.write("\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3")
        buf.write("\2\2\2\u01fa\u0215\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u0201")
        buf.write("\78\2\2\u01fd\u01fe\7/\2\2\u01fe\u0200\78\2\2\u01ff\u01fd")
        buf.write("\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\u0215\3\2\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0204\u0209\79\2\2\u0205\u0206\7/\2\2\u0206\u0208\79")
        buf.write("\2\2\u0207\u0205\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207")
        buf.write("\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u0215\3\2\2\2\u020b")
        buf.write("\u0209\3\2\2\2\u020c\u0211\5Z.\2\u020d\u020e\7/\2\2\u020e")
        buf.write("\u0210\5Z.\2\u020f\u020d\3\2\2\2\u0210\u0213\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0215\3\2\2\2")
        buf.write("\u0213\u0211\3\2\2\2\u0214\u01ea\3\2\2\2\u0214\u01ec\3")
        buf.write("\2\2\2\u0214\u01f4\3\2\2\2\u0214\u01fc\3\2\2\2\u0214\u0204")
        buf.write("\3\2\2\2\u0214\u020c\3\2\2\2\u0215\u0216\3\2\2\2\u0216")
        buf.write("\u0217\7*\2\2\u0217[\3\2\2\2\u0218\u0219\7\n\2\2\u0219")
        buf.write("\u021c\7+\2\2\u021a\u021d\7:\2\2\u021b\u021d\5\\/\2\u021c")
        buf.write("\u021a\3\2\2\2\u021c\u021b\3\2\2\2\u021d\u021e\3\2\2\2")
        buf.write("\u021e\u021f\7/\2\2\u021f\u0220\7\65\2\2\u0220\u0221\7")
        buf.write(",\2\2\u0221]\3\2\2\2:agms|\u0082\u008a\u0093\u0098\u009e")
        buf.write("\u00a3\u00b2\u00bc\u00c4\u00cf\u00d2\u00db\u00e6\u00e8")
        buf.write("\u00f3\u00fc\u0103\u010d\u0118\u0123\u0129\u012e\u0134")
        buf.write("\u013e\u0141\u0145\u0150\u0153\u0157\u015e\u0162\u016c")
        buf.write("\u0174\u017f\u0182\u0190\u01a5\u01b0\u01bd\u01c8\u01d6")
        buf.write("\u01de\u01e7\u01ea\u01f1\u01f9\u0201\u0209\u0211\u0214")
        buf.write("\u021c")
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
    RULE_arrayType = 45

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
                   "literal", "indexedArray", "arrayType" ]

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
            self.state = 93 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 92
                self.classDeclaration()
                self.state = 95 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.K_CLASS):
                    break

            self.state = 97
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
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.normalClassDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
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
            self.state = 103
            self.match(D96Parser.K_CLASS)
            self.state = 104
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_MAIN or _la==D96Parser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 105
                self.match(D96Parser.COLON)
                self.state = 106
                self.match(D96Parser.IDENTIFIER)


            self.state = 109
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_MAIN) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 110
                self.memberDeclaration()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
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
            self.state = 118
            self.match(D96Parser.K_CLASS)
            self.state = 119
            self.match(D96Parser.K_PROGRAM)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 120
                self.match(D96Parser.COLON)
                self.state = 121
                self.match(D96Parser.IDENTIFIER)


            self.state = 124
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_MAIN) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_CONSTRUCTOR) | (1 << D96Parser.K_DESTRUCTOR) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0):
                self.state = 125
                self.programClassMemDecl()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
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
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.attributeDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.mainMethodDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
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
            self.state = 138
            self.match(D96Parser.K_MAIN)
            self.state = 139
            self.match(D96Parser.LEFT_PAREN)
            self.state = 140
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 141
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
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_VAL, D96Parser.K_VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.attributeDeclaration()
                pass
            elif token in [D96Parser.K_MAIN, D96Parser.K_CONSTRUCTOR, D96Parser.K_DESTRUCTOR, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
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
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_MAIN, D96Parser.IDENTIFIER, D96Parser.DOLAR_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_MAIN) | (1 << D96Parser.IDENTIFIER) | (1 << D96Parser.DOLAR_IDENTIFIER))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 148
                self.match(D96Parser.LEFT_PAREN)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDENTIFIER:
                    self.state = 149
                    self.parameterList()


                self.state = 152
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 153
                self.blockStatement()
                pass
            elif token in [D96Parser.K_CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.constructor()
                pass
            elif token in [D96Parser.K_DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
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
            self.state = 158
            self.match(D96Parser.K_CONSTRUCTOR)
            self.state = 159
            self.match(D96Parser.LEFT_PAREN)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDENTIFIER:
                self.state = 160
                self.parameterList()


            self.state = 163
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 164
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
            self.state = 166
            self.match(D96Parser.K_DESTRUCTOR)
            self.state = 167
            self.match(D96Parser.LEFT_PAREN)
            self.state = 168
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 169
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
            self.state = 171
            self.parameter()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI_COLON:
                self.state = 172
                self.match(D96Parser.SEMI_COLON)
                self.state = 173
                self.parameter()
                self.state = 178
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
            self.state = 179
            self.identifierList()
            self.state = 180
            self.match(D96Parser.COLON)
            self.state = 181
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
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.PRIMITIVE_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(D96Parser.PRIMITIVE_TYPE)
                pass
            elif token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
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
            self.state = 188
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 189
            self.mixedIdentifier()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 190
                self.match(D96Parser.COMMA)
                self.state = 191
                self.mixedIdentifier()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 197
            self.match(D96Parser.COLON)
            self.state = 198
            self.d96Type()
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 199
                self.match(D96Parser.OP_ASSIGN)
                self.state = 200
                self.expression()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 201
                    self.match(D96Parser.COMMA)
                    self.state = 202
                    self.expression()
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 210
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
            self.state = 212
            self.match(D96Parser.IDENTIFIER)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 213
                self.match(D96Parser.COMMA)
                self.state = 214
                self.match(D96Parser.IDENTIFIER)
                self.state = 219
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
            self.state = 220
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
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.expression()
                self.state = 226 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 224
                    self.match(D96Parser.COMMA)
                    self.state = 225
                    self.expression()
                    self.state = 228 
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
            self.state = 232
            self.expression()
            self.state = 233
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
            self.state = 239 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 235
                    self.match(D96Parser.LEFT_SQUARE_BRACKET)
                    self.state = 236
                    self.expression()
                    self.state = 237
                    self.match(D96Parser.RIGHT_SQUARE_BRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 241 
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
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.relationalExpr()
                self.state = 246
                _la = self._input.LA(1)
                if not(_la==D96Parser.OP_STRING_CONCATENATION or _la==D96Parser.OP_TWO_SAME_STRING):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 247
                self.relationalExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
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
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.andOrExpr(0)
                self.state = 253
                self.relationalOperator()
                self.state = 254
                self.andOrExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
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
            self.state = 260
            self.addSubExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.AndOrExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andOrExpr)
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
                    self.addSubExpr(0) 
                self.state = 269
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
            self.state = 271
            self.mulAddMolExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.AddSubExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addSubExpr)
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
                    self.mulAddMolExpr(0) 
                self.state = 280
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
            self.state = 282
            self.notExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 289
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.MulAddMolExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mulAddMolExpr)
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
                    self.notExpr() 
                self.state = 291
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
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(D96Parser.OP_LOGICAL_NOT)
                self.state = 293
                self.notExpr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_SELF, D96Parser.K_NEW, D96Parser.OP_ADDTION, D96Parser.OP_SUBTRACTION, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
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
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_ADDTION, D96Parser.OP_SUBTRACTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                _la = self._input.LA(1)
                if not(_la==D96Parser.OP_ADDTION or _la==D96Parser.OP_SUBTRACTION):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 298
                self.signExpr()
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_SELF, D96Parser.K_NEW, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
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
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.instanceAccess(0)
                self.state = 303
                self.indexOperator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
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
            self.state = 309
            self.staticAccess(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.InstanceAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instanceAccess)
                    self.state = 311
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    self.match(D96Parser.DOT)
                    self.state = 313
                    self.match(D96Parser.IDENTIFIER)
                    self.state = 319
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        self.state = 314
                        self.match(D96Parser.LEFT_PAREN)
                        self.state = 316
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_ADDTION) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                            self.state = 315
                            self.expressionList()


                        self.state = 318
                        self.match(D96Parser.RIGHT_PAREN)

             
                self.state = 325
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
            self.state = 327
            self.objectCreation()
            self._ctx.stop = self._input.LT(-1)
            self.state = 341
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.StaticAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_staticAccess)
                    self.state = 329
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 330
                    self.match(D96Parser.DOUBLE_COLON)
                    self.state = 331
                    self.match(D96Parser.DOLAR_IDENTIFIER)
                    self.state = 337
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        self.state = 332
                        self.match(D96Parser.LEFT_PAREN)
                        self.state = 334
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_ADDTION) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                            self.state = 333
                            self.expressionList()


                        self.state = 336
                        self.match(D96Parser.RIGHT_PAREN)

             
                self.state = 343
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
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.match(D96Parser.K_NEW)
                self.state = 345
                self.match(D96Parser.IDENTIFIER)
                self.state = 346
                self.match(D96Parser.LEFT_PAREN)
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_ADDTION) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                    self.state = 347
                    self.expressionList()


                self.state = 350
                self.match(D96Parser.RIGHT_PAREN)
                pass
            elif token in [D96Parser.K_ARRAY, D96Parser.K_NULL, D96Parser.K_SELF, D96Parser.LEFT_PAREN, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
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
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_ARRAY, D96Parser.INTEGER_LITERAL2, D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.literal()
                pass
            elif token in [D96Parser.K_NULL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.match(D96Parser.K_NULL)
                pass
            elif token in [D96Parser.K_SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.match(D96Parser.K_SELF)
                pass
            elif token in [D96Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 357
                self.match(D96Parser.IDENTIFIER)
                pass
            elif token in [D96Parser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 5)
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
            self.state = 364
            _la = self._input.LA(1)
            if not(_la==D96Parser.K_VAL or _la==D96Parser.K_VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 365
            self.match(D96Parser.IDENTIFIER)
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 366
                self.match(D96Parser.COMMA)
                self.state = 367
                self.match(D96Parser.IDENTIFIER)
                self.state = 372
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 373
            self.match(D96Parser.COLON)
            self.state = 374
            self.d96Type()
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.OP_ASSIGN:
                self.state = 375
                self.match(D96Parser.OP_ASSIGN)
                self.state = 376
                self.expression()
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 377
                    self.match(D96Parser.COMMA)
                    self.state = 378
                    self.expression()
                    self.state = 383
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 386
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
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.instanceAccess(0)
                self.state = 389
                self.match(D96Parser.DOT)
                self.state = 390
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.instanceAccess(0)
                self.state = 393
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 394
                self.match(D96Parser.DOLAR_IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.match(D96Parser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 397
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
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.K_IF]:
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
                self.blockStatement()
                pass
            elif token in [D96Parser.K_ELSE_IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.match(D96Parser.K_ELSE_IF)
                self.state = 412
                self.match(D96Parser.LEFT_PAREN)
                self.state = 413
                self.expression()
                self.state = 414
                self.match(D96Parser.RIGHT_PAREN)
                self.state = 415
                self.blockStatement()
                pass
            elif token in [D96Parser.K_ELSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 417
                self.match(D96Parser.K_ELSE)
                self.state = 418
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
            self.state = 421
            self.match(D96Parser.K_FOR_EACH)
            self.state = 422
            self.match(D96Parser.LEFT_PAREN)
            self.state = 423
            self.match(D96Parser.IDENTIFIER)
            self.state = 424
            self.match(D96Parser.K_IN)
            self.state = 425
            self.expression()
            self.state = 426
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 427
            self.expression()
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.K_BY:
                self.state = 428
                self.match(D96Parser.K_BY)
                self.state = 429
                self.expression()


            self.state = 432
            self.match(D96Parser.RIGHT_PAREN)
            self.state = 433
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
            self.state = 435
            self.match(D96Parser.K_BREAK)
            self.state = 436
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
            self.state = 438
            self.match(D96Parser.K_CONTINUE)
            self.state = 439
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
            self.state = 441
            self.match(D96Parser.K_RETURN)
            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_ADDTION) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 442
                self.expression()


            self.state = 445
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
            self.state = 447
            self.instanceAccess(0)
            self.state = 448
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
            self.state = 450
            self.match(D96Parser.LEFT_CURLY_BRACKET)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.K_BREAK) | (1 << D96Parser.K_CONTINUE) | (1 << D96Parser.K_IF) | (1 << D96Parser.K_ELSE_IF) | (1 << D96Parser.K_ELSE) | (1 << D96Parser.K_FOR_EACH) | (1 << D96Parser.K_ARRAY) | (1 << D96Parser.K_RETURN) | (1 << D96Parser.K_NULL) | (1 << D96Parser.K_SELF) | (1 << D96Parser.K_VAL) | (1 << D96Parser.K_VAR) | (1 << D96Parser.K_NEW) | (1 << D96Parser.OP_LOGICAL_NOT) | (1 << D96Parser.OP_ADDTION) | (1 << D96Parser.OP_SUBTRACTION) | (1 << D96Parser.LEFT_PAREN) | (1 << D96Parser.LEFT_CURLY_BRACKET) | (1 << D96Parser.INTEGER_LITERAL2) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDENTIFIER))) != 0):
                self.state = 451
                self.statement()
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 457
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
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.varValStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.assignStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 461
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 462
                self.forInStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 463
                self.breakStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 464
                self.continueStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 465
                self.returnStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 466
                self.methodInvocationStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 467
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
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.INTEGER_LITERAL2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.match(D96Parser.INTEGER_LITERAL2)
                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 472
                self.match(D96Parser.FLOAT_LITERAL)
                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 473
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 474
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 475
                self.indexedArray()
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
            self.state = 478
            self.match(D96Parser.K_ARRAY)
            self.state = 479
            self.match(D96Parser.LEFT_PAREN)
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RIGHT_PAREN, D96Parser.INTEGER_LITERAL]:
                self.state = 488
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.INTEGER_LITERAL:
                    self.state = 480
                    self.match(D96Parser.INTEGER_LITERAL)
                    self.state = 485
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.COMMA:
                        self.state = 481
                        self.match(D96Parser.COMMA)
                        self.state = 482
                        self.match(D96Parser.INTEGER_LITERAL)
                        self.state = 487
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                pass
            elif token in [D96Parser.INTEGER_LITERAL2]:
                self.state = 490
                self.match(D96Parser.INTEGER_LITERAL2)
                self.state = 495
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 491
                    self.match(D96Parser.COMMA)
                    self.state = 492
                    self.match(D96Parser.INTEGER_LITERAL2)
                    self.state = 497
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.state = 498
                self.match(D96Parser.FLOAT_LITERAL)
                self.state = 503
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 499
                    self.match(D96Parser.COMMA)
                    self.state = 500
                    self.match(D96Parser.FLOAT_LITERAL)
                    self.state = 505
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.state = 506
                self.match(D96Parser.BOOLEAN_LITERAL)
                self.state = 511
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 507
                    self.match(D96Parser.COMMA)
                    self.state = 508
                    self.match(D96Parser.BOOLEAN_LITERAL)
                    self.state = 513
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.state = 514
                self.match(D96Parser.STRING_LITERAL)
                self.state = 519
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 515
                    self.match(D96Parser.COMMA)
                    self.state = 516
                    self.match(D96Parser.STRING_LITERAL)
                    self.state = 521
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 522
                self.indexedArray()
                self.state = 527
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 523
                    self.match(D96Parser.COMMA)
                    self.state = 524
                    self.indexedArray()
                    self.state = 529
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 532
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
        self.enterRule(localctx, 90, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(D96Parser.K_ARRAY)
            self.state = 535
            self.match(D96Parser.LEFT_SQUARE_BRACKET)
            self.state = 538
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.PRIMITIVE_TYPE]:
                self.state = 536
                self.match(D96Parser.PRIMITIVE_TYPE)
                pass
            elif token in [D96Parser.K_ARRAY]:
                self.state = 537
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 540
            self.match(D96Parser.COMMA)
            self.state = 541
            self.match(D96Parser.INTEGER_LITERAL2)
            self.state = 542
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
         




