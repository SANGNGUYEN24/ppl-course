// Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3

from lexererr import *

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class D96Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.3", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		WS=1, COMMENT=2, BREAK=3, CONTINUE=4, IF=5, ELSE_IF=6, ELSE=7, FOR_EACH=8, 
		TRUE=9, FALSE=10, ARRAY=11, IN=12, INT=13, FLOAT=14, BOOLEAN=15, STRING=16, 
		RETURN=17, NULL=18, CLASS=19, VAL=20, VAR=21, CONSTRUCTOR=22, DESTRUCTOR=23, 
		NEW=24, BY=25, LEFT_PAREN=26, RIGHT_PAREN=27, LEFT_SQUARE_BRACKET=28, 
		RIGHT_SQUARE_BRACKET=29, DOT=30, COMMA=31, SEMICOLON=32, LEFT_CURLY_BRACKET=33, 
		RIGHT_CURLY_BRACKET=34, ESCAPE=35, INTEGER=36, OCTAL_LITERALNESS=37, HEXA_LITERALNESS=38, 
		BINARY_LITERALNESS=39, FLOAT_LITERALNESS=40, BOOLEAN_LITERALNESS=41, STRING_LITERALNESS=42, 
		ERROR_CHAR=43, UNCLOSE_STRING=44, ILLEGAL_ESCAPE=45;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"WS", "COMMENT", "BREAK", "CONTINUE", "IF", "ELSE_IF", "ELSE", "FOR_EACH", 
			"TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
			"RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
			"NEW", "BY", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
			"DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
			"SINGLE_QUOTE", "DOUBLE_QUOTE", "ESCAPE", "OCTAL_NOTATION", "HEXA_NOTATION", 
			"BINARY_NOTATION", "OCTAL_DIGIT", "HEXA_DIGIT", "BINARY_DIGIT", "DECIMAL_DIGIT", 
			"EXPONENT", "INTEGER", "OCTAL_LITERALNESS", "HEXA_LITERALNESS", "BINARY_LITERALNESS", 
			"FLOAT_LITERALNESS", "BOOLEAN_LITERALNESS", "STRING_LITERALNESS", "ERROR_CHAR", 
			"UNCLOSE_STRING", "ILLEGAL_ESCAPE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
			"'Foreach'", "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
			"'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
			"'Constructor'", "'Destructor'", "'New'", "'By'", "'('", "')'", "'['", 
			"']'", "'.'", "','", "';'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WS", "COMMENT", "BREAK", "CONTINUE", "IF", "ELSE_IF", "ELSE", 
			"FOR_EACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
			"STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
			"NEW", "BY", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
			"DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
			"ESCAPE", "INTEGER", "OCTAL_LITERALNESS", "HEXA_LITERALNESS", "BINARY_LITERALNESS", 
			"FLOAT_LITERALNESS", "BOOLEAN_LITERALNESS", "STRING_LITERALNESS", "ERROR_CHAR", 
			"UNCLOSE_STRING", "ILLEGAL_ESCAPE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public D96Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "D96.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 45:
			INTEGER_action((RuleContext)_localctx, actionIndex);
			break;
		case 52:
			ERROR_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void INTEGER_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			self.text = self.text.replace("_", "")
			break;
		}
	}
	private void ERROR_CHAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:
			raise ErrorToken (self.text)
			break;
		}
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2/\u019a\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\6\2s\n\2\r\2\16\2t\3\2\3\2"+
		"\3\3\3\3\3\3\3\3\7\3}\n\3\f\3\16\3\u0080\13\3\3\3\3\3\3\3\3\3\3\3\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26"+
		"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30"+
		"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32"+
		"\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!"+
		"\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\5&\u012a\n&\3\'\3\'\3(\3(\3(\3(\5"+
		"(\u0132\n(\3)\3)\3)\3)\5)\u0138\n)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\5.\u0144"+
		"\n.\3.\6.\u0147\n.\r.\16.\u0148\3/\5/\u014c\n/\3/\3/\3/\3/\7/\u0152\n"+
		"/\f/\16/\u0155\13/\5/\u0157\n/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62"+
		"\3\62\3\62\3\63\6\63\u0165\n\63\r\63\16\63\u0166\3\63\3\63\7\63\u016b"+
		"\n\63\f\63\16\63\u016e\13\63\3\63\5\63\u0171\n\63\3\63\6\63\u0174\n\63"+
		"\r\63\16\63\u0175\3\63\5\63\u0179\n\63\3\63\3\63\6\63\u017d\n\63\r\63"+
		"\16\63\u017e\3\63\5\63\u0182\n\63\5\63\u0184\n\63\3\64\3\64\5\64\u0188"+
		"\n\64\3\65\3\65\3\65\7\65\u018d\n\65\f\65\16\65\u0190\13\65\3\65\3\65"+
		"\3\66\3\66\3\66\3\67\3\67\38\38\4~\u018e\29\3\3\5\4\7\5\t\6\13\7\r\b\17"+
		"\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+"+
		"\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G\2I\2K%M\2O\2Q"+
		"\2S\2U\2W\2Y\2[\2]&_\'a(c)e*g+i,k-m.o/\3\2\13\5\2\13\f\17\17\"\"\n\2$"+
		"$))^^ddhhppttvv\5\2\62;CHch\3\2\629\3\2\62\63\3\2\62;\4\2GGgg\4\2--//"+
		"\3\2\63;\2\u01a5\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2"+
		"\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2"+
		"!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3"+
		"\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2"+
		"\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E"+
		"\3\2\2\2\2K\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2"+
		"\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3r\3\2\2\2"+
		"\5x\3\2\2\2\7\u0086\3\2\2\2\t\u008c\3\2\2\2\13\u0095\3\2\2\2\r\u0098\3"+
		"\2\2\2\17\u009f\3\2\2\2\21\u00a4\3\2\2\2\23\u00ac\3\2\2\2\25\u00b1\3\2"+
		"\2\2\27\u00b7\3\2\2\2\31\u00bd\3\2\2\2\33\u00c0\3\2\2\2\35\u00c4\3\2\2"+
		"\2\37\u00ca\3\2\2\2!\u00d2\3\2\2\2#\u00d9\3\2\2\2%\u00e0\3\2\2\2\'\u00e5"+
		"\3\2\2\2)\u00eb\3\2\2\2+\u00ef\3\2\2\2-\u00f3\3\2\2\2/\u00ff\3\2\2\2\61"+
		"\u010a\3\2\2\2\63\u010e\3\2\2\2\65\u0111\3\2\2\2\67\u0113\3\2\2\29\u0115"+
		"\3\2\2\2;\u0117\3\2\2\2=\u0119\3\2\2\2?\u011b\3\2\2\2A\u011d\3\2\2\2C"+
		"\u011f\3\2\2\2E\u0121\3\2\2\2G\u0123\3\2\2\2I\u0125\3\2\2\2K\u0127\3\2"+
		"\2\2M\u012b\3\2\2\2O\u0131\3\2\2\2Q\u0137\3\2\2\2S\u0139\3\2\2\2U\u013b"+
		"\3\2\2\2W\u013d\3\2\2\2Y\u013f\3\2\2\2[\u0141\3\2\2\2]\u014b\3\2\2\2_"+
		"\u015a\3\2\2\2a\u015d\3\2\2\2c\u0160\3\2\2\2e\u0183\3\2\2\2g\u0187\3\2"+
		"\2\2i\u0189\3\2\2\2k\u0193\3\2\2\2m\u0196\3\2\2\2o\u0198\3\2\2\2qs\t\2"+
		"\2\2rq\3\2\2\2st\3\2\2\2tr\3\2\2\2tu\3\2\2\2uv\3\2\2\2vw\b\2\2\2w\4\3"+
		"\2\2\2xy\7%\2\2yz\7%\2\2z~\3\2\2\2{}\13\2\2\2|{\3\2\2\2}\u0080\3\2\2\2"+
		"~\177\3\2\2\2~|\3\2\2\2\177\u0081\3\2\2\2\u0080~\3\2\2\2\u0081\u0082\7"+
		"%\2\2\u0082\u0083\7%\2\2\u0083\u0084\3\2\2\2\u0084\u0085\b\3\2\2\u0085"+
		"\6\3\2\2\2\u0086\u0087\7D\2\2\u0087\u0088\7t\2\2\u0088\u0089\7g\2\2\u0089"+
		"\u008a\7c\2\2\u008a\u008b\7m\2\2\u008b\b\3\2\2\2\u008c\u008d\7E\2\2\u008d"+
		"\u008e\7q\2\2\u008e\u008f\7p\2\2\u008f\u0090\7v\2\2\u0090\u0091\7k\2\2"+
		"\u0091\u0092\7p\2\2\u0092\u0093\7w\2\2\u0093\u0094\7g\2\2\u0094\n\3\2"+
		"\2\2\u0095\u0096\7K\2\2\u0096\u0097\7h\2\2\u0097\f\3\2\2\2\u0098\u0099"+
		"\7G\2\2\u0099\u009a\7n\2\2\u009a\u009b\7u\2\2\u009b\u009c\7g\2\2\u009c"+
		"\u009d\7k\2\2\u009d\u009e\7h\2\2\u009e\16\3\2\2\2\u009f\u00a0\7G\2\2\u00a0"+
		"\u00a1\7n\2\2\u00a1\u00a2\7u\2\2\u00a2\u00a3\7g\2\2\u00a3\20\3\2\2\2\u00a4"+
		"\u00a5\7H\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g\2\2"+
		"\u00a8\u00a9\7c\2\2\u00a9\u00aa\7e\2\2\u00aa\u00ab\7j\2\2\u00ab\22\3\2"+
		"\2\2\u00ac\u00ad\7V\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7w\2\2\u00af\u00b0"+
		"\7g\2\2\u00b0\24\3\2\2\2\u00b1\u00b2\7H\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4"+
		"\7n\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6\7g\2\2\u00b6\26\3\2\2\2\u00b7\u00b8"+
		"\7C\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7c\2\2\u00bb"+
		"\u00bc\7{\2\2\u00bc\30\3\2\2\2\u00bd\u00be\7K\2\2\u00be\u00bf\7p\2\2\u00bf"+
		"\32\3\2\2\2\u00c0\u00c1\7K\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7v\2\2\u00c3"+
		"\34\3\2\2\2\u00c4\u00c5\7H\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7\7q\2\2\u00c7"+
		"\u00c8\7c\2\2\u00c8\u00c9\7v\2\2\u00c9\36\3\2\2\2\u00ca\u00cb\7D\2\2\u00cb"+
		"\u00cc\7q\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7n\2\2\u00ce\u00cf\7g\2\2"+
		"\u00cf\u00d0\7c\2\2\u00d0\u00d1\7p\2\2\u00d1 \3\2\2\2\u00d2\u00d3\7U\2"+
		"\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7"+
		"\7p\2\2\u00d7\u00d8\7i\2\2\u00d8\"\3\2\2\2\u00d9\u00da\7T\2\2\u00da\u00db"+
		"\7g\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7w\2\2\u00dd\u00de\7t\2\2\u00de"+
		"\u00df\7p\2\2\u00df$\3\2\2\2\u00e0\u00e1\7P\2\2\u00e1\u00e2\7w\2\2\u00e2"+
		"\u00e3\7n\2\2\u00e3\u00e4\7n\2\2\u00e4&\3\2\2\2\u00e5\u00e6\7E\2\2\u00e6"+
		"\u00e7\7n\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea\7u\2\2"+
		"\u00ea(\3\2\2\2\u00eb\u00ec\7X\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7n\2"+
		"\2\u00ee*\3\2\2\2\u00ef\u00f0\7X\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7"+
		"t\2\2\u00f2,\3\2\2\2\u00f3\u00f4\7E\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6"+
		"\7p\2\2\u00f6\u00f7\7u\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7t\2\2\u00f9"+
		"\u00fa\7w\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7q\2\2"+
		"\u00fd\u00fe\7t\2\2\u00fe.\3\2\2\2\u00ff\u0100\7F\2\2\u0100\u0101\7g\2"+
		"\2\u0101\u0102\7u\2\2\u0102\u0103\7v\2\2\u0103\u0104\7t\2\2\u0104\u0105"+
		"\7w\2\2\u0105\u0106\7e\2\2\u0106\u0107\7v\2\2\u0107\u0108\7q\2\2\u0108"+
		"\u0109\7t\2\2\u0109\60\3\2\2\2\u010a\u010b\7P\2\2\u010b\u010c\7g\2\2\u010c"+
		"\u010d\7y\2\2\u010d\62\3\2\2\2\u010e\u010f\7D\2\2\u010f\u0110\7{\2\2\u0110"+
		"\64\3\2\2\2\u0111\u0112\7*\2\2\u0112\66\3\2\2\2\u0113\u0114\7+\2\2\u0114"+
		"8\3\2\2\2\u0115\u0116\7]\2\2\u0116:\3\2\2\2\u0117\u0118\7_\2\2\u0118<"+
		"\3\2\2\2\u0119\u011a\7\60\2\2\u011a>\3\2\2\2\u011b\u011c\7.\2\2\u011c"+
		"@\3\2\2\2\u011d\u011e\7=\2\2\u011eB\3\2\2\2\u011f\u0120\7}\2\2\u0120D"+
		"\3\2\2\2\u0121\u0122\7\177\2\2\u0122F\3\2\2\2\u0123\u0124\7)\2\2\u0124"+
		"H\3\2\2\2\u0125\u0126\7$\2\2\u0126J\3\2\2\2\u0127\u0129\7^\2\2\u0128\u012a"+
		"\t\3\2\2\u0129\u0128\3\2\2\2\u012aL\3\2\2\2\u012b\u012c\7\62\2\2\u012c"+
		"N\3\2\2\2\u012d\u012e\7\62\2\2\u012e\u0132\7z\2\2\u012f\u0130\7\62\2\2"+
		"\u0130\u0132\7Z\2\2\u0131\u012d\3\2\2\2\u0131\u012f\3\2\2\2\u0132P\3\2"+
		"\2\2\u0133\u0134\7\62\2\2\u0134\u0138\7d\2\2\u0135\u0136\7\62\2\2\u0136"+
		"\u0138\7D\2\2\u0137\u0133\3\2\2\2\u0137\u0135\3\2\2\2\u0138R\3\2\2\2\u0139"+
		"\u013a\t\4\2\2\u013aT\3\2\2\2\u013b\u013c\t\5\2\2\u013cV\3\2\2\2\u013d"+
		"\u013e\t\6\2\2\u013eX\3\2\2\2\u013f\u0140\t\7\2\2\u0140Z\3\2\2\2\u0141"+
		"\u0143\t\b\2\2\u0142\u0144\t\t\2\2\u0143\u0142\3\2\2\2\u0143\u0144\3\2"+
		"\2\2\u0144\u0146\3\2\2\2\u0145\u0147\5Y-\2\u0146\u0145\3\2\2\2\u0147\u0148"+
		"\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149\\\3\2\2\2\u014a"+
		"\u014c\t\t\2\2\u014b\u014a\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u0156\3\2"+
		"\2\2\u014d\u0157\7\62\2\2\u014e\u0153\t\n\2\2\u014f\u0152\5Y-\2\u0150"+
		"\u0152\7a\2\2\u0151\u014f\3\2\2\2\u0151\u0150\3\2\2\2\u0152\u0155\3\2"+
		"\2\2\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0157\3\2\2\2\u0155"+
		"\u0153\3\2\2\2\u0156\u014d\3\2\2\2\u0156\u014e\3\2\2\2\u0157\u0158\3\2"+
		"\2\2\u0158\u0159\b/\3\2\u0159^\3\2\2\2\u015a\u015b\5M\'\2\u015b\u015c"+
		"\5S*\2\u015c`\3\2\2\2\u015d\u015e\5O(\2\u015e\u015f\5U+\2\u015fb\3\2\2"+
		"\2\u0160\u0161\5Q)\2\u0161\u0162\5W,\2\u0162d\3\2\2\2\u0163\u0165\5]/"+
		"\2\u0164\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167"+
		"\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u016c\5=\37\2\u0169\u016b\5Y-\2\u016a"+
		"\u0169\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2"+
		"\2\2\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0171\5[.\2\u0170\u016f"+
		"\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0184\3\2\2\2\u0172\u0174\5]/\2\u0173"+
		"\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2"+
		"\2\2\u0176\u0178\3\2\2\2\u0177\u0179\5[.\2\u0178\u0177\3\2\2\2\u0178\u0179"+
		"\3\2\2\2\u0179\u0184\3\2\2\2\u017a\u017c\5=\37\2\u017b\u017d\5Y-\2\u017c"+
		"\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2"+
		"\2\2\u017f\u0181\3\2\2\2\u0180\u0182\5[.\2\u0181\u0180\3\2\2\2\u0181\u0182"+
		"\3\2\2\2\u0182\u0184\3\2\2\2\u0183\u0164\3\2\2\2\u0183\u0173\3\2\2\2\u0183"+
		"\u017a\3\2\2\2\u0184f\3\2\2\2\u0185\u0188\5\23\n\2\u0186\u0188\5\25\13"+
		"\2\u0187\u0185\3\2\2\2\u0187\u0186\3\2\2\2\u0188h\3\2\2\2\u0189\u018e"+
		"\5I%\2\u018a\u018d\5K&\2\u018b\u018d\13\2\2\2\u018c\u018a\3\2\2\2\u018c"+
		"\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e\u018f\3\2\2\2\u018e\u018c\3\2"+
		"\2\2\u018f\u0191\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192\5I%\2\u0192j"+
		"\3\2\2\2\u0193\u0194\13\2\2\2\u0194\u0195\b\66\4\2\u0195l\3\2\2\2\u0196"+
		"\u0197\13\2\2\2\u0197n\3\2\2\2\u0198\u0199\13\2\2\2\u0199p\3\2\2\2\31"+
		"\2t~\u0129\u0131\u0137\u0143\u0148\u014b\u0151\u0153\u0156\u0166\u016c"+
		"\u0170\u0175\u0178\u017e\u0181\u0183\u0187\u018c\u018e\5\b\2\2\3/\2\3"+
		"\66\3";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}