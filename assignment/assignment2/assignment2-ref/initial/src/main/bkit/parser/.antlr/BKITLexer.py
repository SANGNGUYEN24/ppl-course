# Generated from c:\Users\ADMIN\Desktop\Study\193\Principles of Programming Language\Assignment2\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0225\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\6\27\u010d\n\27\r\27\16\27\u010e\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\7\30\u0117\n\30\f\30\16\30\u011a\13\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&")
        buf.write("\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\5\61\u0171\n\61\3\62\3\62\3\63\3\63\3")
        buf.write("\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:")
        buf.write("\3:\3;\3;\3<\3<\7<\u0189\n<\f<\16<\u018c\13<\3=\3=\7=")
        buf.write("\u0190\n=\f=\16=\u0193\13=\3=\3=\3=\3=\5=\u0199\n=\3=")
        buf.write("\3=\7=\u019d\n=\f=\16=\u01a0\13=\3=\3=\3=\3=\5=\u01a6")
        buf.write("\n=\3=\3=\7=\u01aa\n=\f=\16=\u01ad\13=\3=\5=\u01b0\n=")
        buf.write("\3>\6>\u01b3\n>\r>\16>\u01b4\3>\3>\7>\u01b9\n>\f>\16>")
        buf.write("\u01bc\13>\3>\3>\5>\u01c0\n>\3>\6>\u01c3\n>\r>\16>\u01c4")
        buf.write("\5>\u01c7\n>\3>\6>\u01ca\n>\r>\16>\u01cb\3>\3>\7>\u01d0")
        buf.write("\n>\f>\16>\u01d3\13>\5>\u01d5\n>\3>\3>\5>\u01d9\n>\3>")
        buf.write("\6>\u01dc\n>\r>\16>\u01dd\5>\u01e0\n>\3?\3?\7?\u01e4\n")
        buf.write("?\f?\16?\u01e7\13?\3?\3?\3?\3@\3@\3@\3@\5@\u01f0\n@\3")
        buf.write("A\3A\7A\u01f4\nA\fA\16A\u01f7\13A\3A\3A\3A\3A\3B\3B\3")
        buf.write("B\3B\7B\u0201\nB\fB\16B\u0204\13B\3B\5B\u0207\nB\3B\3")
        buf.write("B\3C\3C\3C\3C\7C\u020f\nC\fC\16C\u0212\13C\3C\3C\6C\u0216")
        buf.write("\nC\rC\16C\u0217\7C\u021a\nC\fC\16C\u021d\13C\3C\5C\u0220")
        buf.write("\nC\3C\3C\3D\3D\4\u0118\u01e5\2E\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\2c\62e\63g\64i\65k\66m\67o8q9s:u;w<y={>}?\177\2\u0081")
        buf.write("@\u0083A\u0085B\u0087C\3\2\22\5\2\13\f\17\17\"\"\3\2c")
        buf.write("|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2\63;CH\4\2\62;CH\3")
        buf.write("\2\639\3\2\629\4\2GGgg\4\2--//\6\2\f\f$$))^^\t\2))^^d")
        buf.write("dhhppttvv\3\2$$\3\3\f\f\3\2,,\2\u0248\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2")
        buf.write("\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2")
        buf.write("\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\3\u0089\3\2\2\2\5\u008d\3\2\2\2\7\u0092\3\2\2\2\t\u0097")
        buf.write("\3\2\2\2\13\u009e\3\2\2\2\r\u00a1\3\2\2\2\17\u00a7\3\2")
        buf.write("\2\2\21\u00ad\3\2\2\2\23\u00b4\3\2\2\2\25\u00bd\3\2\2")
        buf.write("\2\27\u00c7\3\2\2\2\31\u00cd\3\2\2\2\33\u00d6\3\2\2\2")
        buf.write("\35\u00de\3\2\2\2\37\u00e2\3\2\2\2!\u00e9\3\2\2\2#\u00ee")
        buf.write("\3\2\2\2%\u00f1\3\2\2\2\'\u00f7\3\2\2\2)\u0100\3\2\2\2")
        buf.write("+\u0105\3\2\2\2-\u010c\3\2\2\2/\u0112\3\2\2\2\61\u0120")
        buf.write("\3\2\2\2\63\u0122\3\2\2\2\65\u0124\3\2\2\2\67\u0127\3")
        buf.write("\2\2\29\u0129\3\2\2\2;\u012c\3\2\2\2=\u012e\3\2\2\2?\u0131")
        buf.write("\3\2\2\2A\u0133\3\2\2\2C\u0136\3\2\2\2E\u0138\3\2\2\2")
        buf.write("G\u013a\3\2\2\2I\u013d\3\2\2\2K\u0140\3\2\2\2M\u0143\3")
        buf.write("\2\2\2O\u0146\3\2\2\2Q\u0148\3\2\2\2S\u014a\3\2\2\2U\u014d")
        buf.write("\3\2\2\2W\u0150\3\2\2\2Y\u0154\3\2\2\2[\u0157\3\2\2\2")
        buf.write("]\u015a\3\2\2\2_\u015e\3\2\2\2a\u0170\3\2\2\2c\u0172\3")
        buf.write("\2\2\2e\u0174\3\2\2\2g\u0176\3\2\2\2i\u0178\3\2\2\2k\u017a")
        buf.write("\3\2\2\2m\u017c\3\2\2\2o\u017e\3\2\2\2q\u0180\3\2\2\2")
        buf.write("s\u0182\3\2\2\2u\u0184\3\2\2\2w\u0186\3\2\2\2y\u01af\3")
        buf.write("\2\2\2{\u01df\3\2\2\2}\u01e1\3\2\2\2\177\u01ef\3\2\2\2")
        buf.write("\u0081\u01f1\3\2\2\2\u0083\u01fc\3\2\2\2\u0085\u020a\3")
        buf.write("\2\2\2\u0087\u0223\3\2\2\2\u0089\u008a\7X\2\2\u008a\u008b")
        buf.write("\7c\2\2\u008b\u008c\7t\2\2\u008c\4\3\2\2\2\u008d\u008e")
        buf.write("\7D\2\2\u008e\u008f\7q\2\2\u008f\u0090\7f\2\2\u0090\u0091")
        buf.write("\7{\2\2\u0091\6\3\2\2\2\u0092\u0093\7G\2\2\u0093\u0094")
        buf.write("\7n\2\2\u0094\u0095\7u\2\2\u0095\u0096\7g\2\2\u0096\b")
        buf.write("\3\2\2\2\u0097\u0098\7G\2\2\u0098\u0099\7p\2\2\u0099\u009a")
        buf.write("\7f\2\2\u009a\u009b\7H\2\2\u009b\u009c\7q\2\2\u009c\u009d")
        buf.write("\7t\2\2\u009d\n\3\2\2\2\u009e\u009f\7K\2\2\u009f\u00a0")
        buf.write("\7h\2\2\u00a0\f\3\2\2\2\u00a1\u00a2\7G\2\2\u00a2\u00a3")
        buf.write("\7p\2\2\u00a3\u00a4\7f\2\2\u00a4\u00a5\7F\2\2\u00a5\u00a6")
        buf.write("\7q\2\2\u00a6\16\3\2\2\2\u00a7\u00a8\7D\2\2\u00a8\u00a9")
        buf.write("\7t\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac")
        buf.write("\7m\2\2\u00ac\20\3\2\2\2\u00ad\u00ae\7G\2\2\u00ae\u00af")
        buf.write("\7n\2\2\u00af\u00b0\7u\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2")
        buf.write("\7K\2\2\u00b2\u00b3\7h\2\2\u00b3\22\3\2\2\2\u00b4\u00b5")
        buf.write("\7G\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7\7f\2\2\u00b7\u00b8")
        buf.write("\7Y\2\2\u00b8\u00b9\7j\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb")
        buf.write("\7n\2\2\u00bb\u00bc\7g\2\2\u00bc\24\3\2\2\2\u00bd\u00be")
        buf.write("\7R\2\2\u00be\u00bf\7c\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7c\2\2\u00c1\u00c2\7o\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4")
        buf.write("\7v\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7t\2\2\u00c6\26")
        buf.write("\3\2\2\2\u00c7\u00c8\7Y\2\2\u00c8\u00c9\7j\2\2\u00c9\u00ca")
        buf.write("\7k\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7g\2\2\u00cc\30")
        buf.write("\3\2\2\2\u00cd\u00ce\7E\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5\7g\2\2\u00d5\32")
        buf.write("\3\2\2\2\u00d6\u00d7\7G\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9")
        buf.write("\7f\2\2\u00d9\u00da\7D\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7f\2\2\u00dc\u00dd\7{\2\2\u00dd\34\3\2\2\2\u00de\u00df")
        buf.write("\7H\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7t\2\2\u00e1\36")
        buf.write("\3\2\2\2\u00e2\u00e3\7T\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5\u00e6\7w\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8 \3\2\2\2\u00e9\u00ea\7V\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7g\2\2\u00ed\"")
        buf.write("\3\2\2\2\u00ee\u00ef\7F\2\2\u00ef\u00f0\7q\2\2\u00f0$")
        buf.write("\3\2\2\2\u00f1\u00f2\7G\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7f\2\2\u00f4\u00f5\7K\2\2\u00f5\u00f6\7h\2\2\u00f6&\3")
        buf.write("\2\2\2\u00f7\u00f8\7H\2\2\u00f8\u00f9\7w\2\2\u00f9\u00fa")
        buf.write("\7p\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7k\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7p\2\2\u00ff(\3")
        buf.write("\2\2\2\u0100\u0101\7V\2\2\u0101\u0102\7j\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\u0104\7p\2\2\u0104*\3\2\2\2\u0105\u0106")
        buf.write("\7H\2\2\u0106\u0107\7c\2\2\u0107\u0108\7n\2\2\u0108\u0109")
        buf.write("\7u\2\2\u0109\u010a\7g\2\2\u010a,\3\2\2\2\u010b\u010d")
        buf.write("\t\2\2\2\u010c\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e")
        buf.write("\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110\u0111\b\27\2\2\u0111.\3\2\2\2\u0112\u0113\7,\2")
        buf.write("\2\u0113\u0114\7,\2\2\u0114\u0118\3\2\2\2\u0115\u0117")
        buf.write("\13\2\2\2\u0116\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011b\3\2\2\2")
        buf.write("\u011a\u0118\3\2\2\2\u011b\u011c\7,\2\2\u011c\u011d\7")
        buf.write(",\2\2\u011d\u011e\3\2\2\2\u011e\u011f\b\30\2\2\u011f\60")
        buf.write("\3\2\2\2\u0120\u0121\7?\2\2\u0121\62\3\2\2\2\u0122\u0123")
        buf.write("\7-\2\2\u0123\64\3\2\2\2\u0124\u0125\7-\2\2\u0125\u0126")
        buf.write("\7\60\2\2\u0126\66\3\2\2\2\u0127\u0128\7/\2\2\u01288\3")
        buf.write("\2\2\2\u0129\u012a\7/\2\2\u012a\u012b\7\60\2\2\u012b:")
        buf.write("\3\2\2\2\u012c\u012d\7,\2\2\u012d<\3\2\2\2\u012e\u012f")
        buf.write("\7,\2\2\u012f\u0130\7\60\2\2\u0130>\3\2\2\2\u0131\u0132")
        buf.write("\7^\2\2\u0132@\3\2\2\2\u0133\u0134\7^\2\2\u0134\u0135")
        buf.write("\7\60\2\2\u0135B\3\2\2\2\u0136\u0137\7\'\2\2\u0137D\3")
        buf.write("\2\2\2\u0138\u0139\7#\2\2\u0139F\3\2\2\2\u013a\u013b\7")
        buf.write("(\2\2\u013b\u013c\7(\2\2\u013cH\3\2\2\2\u013d\u013e\7")
        buf.write("~\2\2\u013e\u013f\7~\2\2\u013fJ\3\2\2\2\u0140\u0141\7")
        buf.write("?\2\2\u0141\u0142\7?\2\2\u0142L\3\2\2\2\u0143\u0144\7")
        buf.write("#\2\2\u0144\u0145\7?\2\2\u0145N\3\2\2\2\u0146\u0147\7")
        buf.write(">\2\2\u0147P\3\2\2\2\u0148\u0149\7@\2\2\u0149R\3\2\2\2")
        buf.write("\u014a\u014b\7>\2\2\u014b\u014c\7?\2\2\u014cT\3\2\2\2")
        buf.write("\u014d\u014e\7@\2\2\u014e\u014f\7?\2\2\u014fV\3\2\2\2")
        buf.write("\u0150\u0151\7?\2\2\u0151\u0152\7\61\2\2\u0152\u0153\7")
        buf.write("?\2\2\u0153X\3\2\2\2\u0154\u0155\7>\2\2\u0155\u0156\7")
        buf.write("\60\2\2\u0156Z\3\2\2\2\u0157\u0158\7@\2\2\u0158\u0159")
        buf.write("\7\60\2\2\u0159\\\3\2\2\2\u015a\u015b\7>\2\2\u015b\u015c")
        buf.write("\7?\2\2\u015c\u015d\7\60\2\2\u015d^\3\2\2\2\u015e\u015f")
        buf.write("\7@\2\2\u015f\u0160\7?\2\2\u0160\u0161\7\60\2\2\u0161")
        buf.write("`\3\2\2\2\u0162\u0163\7^\2\2\u0163\u0171\7d\2\2\u0164")
        buf.write("\u0165\7^\2\2\u0165\u0171\7h\2\2\u0166\u0167\7^\2\2\u0167")
        buf.write("\u0171\7t\2\2\u0168\u0169\7^\2\2\u0169\u0171\7p\2\2\u016a")
        buf.write("\u016b\7^\2\2\u016b\u0171\7v\2\2\u016c\u016d\7^\2\2\u016d")
        buf.write("\u0171\7)\2\2\u016e\u016f\7^\2\2\u016f\u0171\7^\2\2\u0170")
        buf.write("\u0162\3\2\2\2\u0170\u0164\3\2\2\2\u0170\u0166\3\2\2\2")
        buf.write("\u0170\u0168\3\2\2\2\u0170\u016a\3\2\2\2\u0170\u016c\3")
        buf.write("\2\2\2\u0170\u016e\3\2\2\2\u0171b\3\2\2\2\u0172\u0173")
        buf.write("\7*\2\2\u0173d\3\2\2\2\u0174\u0175\7+\2\2\u0175f\3\2\2")
        buf.write("\2\u0176\u0177\7]\2\2\u0177h\3\2\2\2\u0178\u0179\7_\2")
        buf.write("\2\u0179j\3\2\2\2\u017a\u017b\7<\2\2\u017bl\3\2\2\2\u017c")
        buf.write("\u017d\7\60\2\2\u017dn\3\2\2\2\u017e\u017f\7.\2\2\u017f")
        buf.write("p\3\2\2\2\u0180\u0181\7=\2\2\u0181r\3\2\2\2\u0182\u0183")
        buf.write("\7}\2\2\u0183t\3\2\2\2\u0184\u0185\7\177\2\2\u0185v\3")
        buf.write("\2\2\2\u0186\u018a\t\3\2\2\u0187\u0189\t\4\2\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018bx\3\2\2\2\u018c\u018a\3\2\2\2\u018d")
        buf.write("\u0191\t\5\2\2\u018e\u0190\t\6\2\2\u018f\u018e\3\2\2\2")
        buf.write("\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3")
        buf.write("\2\2\2\u0192\u01b0\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0195")
        buf.write("\7\62\2\2\u0195\u0199\7z\2\2\u0196\u0197\7\62\2\2\u0197")
        buf.write("\u0199\7Z\2\2\u0198\u0194\3\2\2\2\u0198\u0196\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019a\u019e\t\7\2\2\u019b\u019d\t")
        buf.write("\b\2\2\u019c\u019b\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c")
        buf.write("\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01b0\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a1\u01a2\7\62\2\2\u01a2\u01a6\7q\2\2")
        buf.write("\u01a3\u01a4\7\62\2\2\u01a4\u01a6\7Q\2\2\u01a5\u01a1\3")
        buf.write("\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01ab")
        buf.write("\t\t\2\2\u01a8\u01aa\t\n\2\2\u01a9\u01a8\3\2\2\2\u01aa")
        buf.write("\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write("\u01ac\u01b0\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01b0\7")
        buf.write("\62\2\2\u01af\u018d\3\2\2\2\u01af\u0198\3\2\2\2\u01af")
        buf.write("\u01a5\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0z\3\2\2\2\u01b1")
        buf.write("\u01b3\t\6\2\2\u01b2\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2")
        buf.write("\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\3")
        buf.write("\2\2\2\u01b6\u01ba\5m\67\2\u01b7\u01b9\t\6\2\2\u01b8\u01b7")
        buf.write("\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba")
        buf.write("\u01bb\3\2\2\2\u01bb\u01c6\3\2\2\2\u01bc\u01ba\3\2\2\2")
        buf.write("\u01bd\u01bf\t\13\2\2\u01be\u01c0\t\f\2\2\u01bf\u01be")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c2\3\2\2\2\u01c1")
        buf.write("\u01c3\t\6\2\2\u01c2\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2")
        buf.write("\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c7\3")
        buf.write("\2\2\2\u01c6\u01bd\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01e0")
        buf.write("\3\2\2\2\u01c8\u01ca\t\6\2\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01cc\u01d4\3\2\2\2\u01cd\u01d1\5m\67\2\u01ce\u01d0\t")
        buf.write("\6\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf")
        buf.write("\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d4\u01cd\3\2\2\2\u01d4\u01d5\3\2\2\2")
        buf.write("\u01d5\u01d6\3\2\2\2\u01d6\u01d8\t\13\2\2\u01d7\u01d9")
        buf.write("\t\f\2\2\u01d8\u01d7\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9")
        buf.write("\u01db\3\2\2\2\u01da\u01dc\t\6\2\2\u01db\u01da\3\2\2\2")
        buf.write("\u01dc\u01dd\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3")
        buf.write("\2\2\2\u01de\u01e0\3\2\2\2\u01df\u01b2\3\2\2\2\u01df\u01c9")
        buf.write("\3\2\2\2\u01e0|\3\2\2\2\u01e1\u01e5\7$\2\2\u01e2\u01e4")
        buf.write("\5\177@\2\u01e3\u01e2\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e8\3\2\2\2")
        buf.write("\u01e7\u01e5\3\2\2\2\u01e8\u01e9\7$\2\2\u01e9\u01ea\b")
        buf.write("?\3\2\u01ea~\3\2\2\2\u01eb\u01f0\5a\61\2\u01ec\u01ed\7")
        buf.write(")\2\2\u01ed\u01f0\7$\2\2\u01ee\u01f0\n\r\2\2\u01ef\u01eb")
        buf.write("\3\2\2\2\u01ef\u01ec\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0")
        buf.write("\u0080\3\2\2\2\u01f1\u01f5\7$\2\2\u01f2\u01f4\5\177@\2")
        buf.write("\u01f3\u01f2\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3")
        buf.write("\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f8\3\2\2\2\u01f7\u01f5")
        buf.write("\3\2\2\2\u01f8\u01f9\7^\2\2\u01f9\u01fa\n\16\2\2\u01fa")
        buf.write("\u01fb\bA\4\2\u01fb\u0082\3\2\2\2\u01fc\u0202\7$\2\2\u01fd")
        buf.write("\u0201\n\17\2\2\u01fe\u01ff\7)\2\2\u01ff\u0201\7$\2\2")
        buf.write("\u0200\u01fd\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0204\3")
        buf.write("\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0206")
        buf.write("\3\2\2\2\u0204\u0202\3\2\2\2\u0205\u0207\t\20\2\2\u0206")
        buf.write("\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0209\bB\5\2")
        buf.write("\u0209\u0084\3\2\2\2\u020a\u020b\7,\2\2\u020b\u020c\7")
        buf.write(",\2\2\u020c\u0210\3\2\2\2\u020d\u020f\n\21\2\2\u020e\u020d")
        buf.write("\3\2\2\2\u020f\u0212\3\2\2\2\u0210\u020e\3\2\2\2\u0210")
        buf.write("\u0211\3\2\2\2\u0211\u021b\3\2\2\2\u0212\u0210\3\2\2\2")
        buf.write("\u0213\u0215\7,\2\2\u0214\u0216\n\21\2\2\u0215\u0214\3")
        buf.write("\2\2\2\u0216\u0217\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218")
        buf.write("\3\2\2\2\u0218\u021a\3\2\2\2\u0219\u0213\3\2\2\2\u021a")
        buf.write("\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2")
        buf.write("\u021c\u021f\3\2\2\2\u021d\u021b\3\2\2\2\u021e\u0220\7")
        buf.write(",\2\2\u021f\u021e\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0221")
        buf.write("\3\2\2\2\u0221\u0222\7\2\2\3\u0222\u0086\3\2\2\2\u0223")
        buf.write("\u0224\13\2\2\2\u0224\u0088\3\2\2\2#\2\u010e\u0118\u0170")
        buf.write("\u0188\u018a\u0191\u0198\u019e\u01a5\u01ab\u01af\u01b4")
        buf.write("\u01ba\u01bf\u01c4\u01c6\u01cb\u01d1\u01d4\u01d8\u01dd")
        buf.write("\u01df\u01e5\u01ef\u01f5\u0200\u0202\u0206\u0210\u0217")
        buf.write("\u021b\u021f\6\b\2\2\3?\2\3A\3\3B\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VAR = 1
    BODY = 2
    ELSE = 3
    ENDFOR = 4
    IF = 5
    ENDDO = 6
    BREAK = 7
    ELSEIF = 8
    ENDWHILE = 9
    PARAMETER = 10
    WHILE = 11
    CONTINUE = 12
    ENDBODY = 13
    FOR = 14
    RETURN = 15
    TRUE = 16
    DO = 17
    ENDIF = 18
    FUNCTION = 19
    THEN = 20
    FALSE = 21
    WS = 22
    COMMENT = 23
    ASSIGN = 24
    ADD = 25
    ADDFLOAT = 26
    SUB = 27
    SUBFLOAT = 28
    MUL = 29
    MULFLOAT = 30
    DIV = 31
    DIVFLOAT = 32
    MOD = 33
    NOT = 34
    AND = 35
    OR = 36
    EQUAL = 37
    NOTEQUAL = 38
    LESS = 39
    GREATER = 40
    LESSEQUAL = 41
    GREATEREQUAL = 42
    EQUALFLOAT = 43
    LESSFLOAT = 44
    GREATERFLOAT = 45
    LESSEQUALFLOAT = 46
    GREATEREQUALFLOAT = 47
    LP = 48
    RP = 49
    LA = 50
    RA = 51
    COLON = 52
    DOT = 53
    COMMA = 54
    SEMI = 55
    LB = 56
    RB = 57
    ID = 58
    INTLIT = 59
    FLOATLIT = 60
    STRINGLIT = 61
    ILLEGAL_ESCAPE = 62
    UNCLOSE_STRING = 63
    UNTERMINATED_COMMENT = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Var'", "'Body'", "'Else'", "'EndFor'", "'If'", "'EndDo'", 
            "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
            "'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", "'Do'", 
            "'EndIf'", "'Function'", "'Then'", "'False'", "'='", "'+'", 
            "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", 
            "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", 
            "'['", "']'", "':'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "BODY", "ELSE", "ENDFOR", "IF", "ENDDO", "BREAK", "ELSEIF", 
            "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", 
            "RETURN", "TRUE", "DO", "ENDIF", "FUNCTION", "THEN", "FALSE", 
            "WS", "COMMENT", "ASSIGN", "ADD", "ADDFLOAT", "SUB", "SUBFLOAT", 
            "MUL", "MULFLOAT", "DIV", "DIVFLOAT", "MOD", "NOT", "AND", "OR", 
            "EQUAL", "NOTEQUAL", "LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", 
            "EQUALFLOAT", "LESSFLOAT", "GREATERFLOAT", "LESSEQUALFLOAT", 
            "GREATEREQUALFLOAT", "LP", "RP", "LA", "RA", "COLON", "DOT", 
            "COMMA", "SEMI", "LB", "RB", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "VAR", "BODY", "ELSE", "ENDFOR", "IF", "ENDDO", "BREAK", 
                  "ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", 
                  "ENDBODY", "FOR", "RETURN", "TRUE", "DO", "ENDIF", "FUNCTION", 
                  "THEN", "FALSE", "WS", "COMMENT", "ASSIGN", "ADD", "ADDFLOAT", 
                  "SUB", "SUBFLOAT", "MUL", "MULFLOAT", "DIV", "DIVFLOAT", 
                  "MOD", "NOT", "AND", "OR", "EQUAL", "NOTEQUAL", "LESS", 
                  "GREATER", "LESSEQUAL", "GREATEREQUAL", "EQUALFLOAT", 
                  "LESSFLOAT", "GREATERFLOAT", "LESSEQUALFLOAT", "GREATEREQUALFLOAT", 
                  "ESCAPE", "LP", "RP", "LA", "RA", "COLON", "DOT", "COMMA", 
                  "SEMI", "LB", "RB", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", 
                  "STRINGTYPE", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[61] = self.STRINGLIT_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[64] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    y = str(self.text)
                    self.text = y[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = str(self.text)[1:]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = str(self.text)[1:]

     


