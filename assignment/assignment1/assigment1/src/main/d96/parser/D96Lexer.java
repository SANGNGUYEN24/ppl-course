// Generated from D96.g4 by ANTLR 4.9.3
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
		WHITE_SPACE=1, COMMENT=2, BREAK=3, CONTINUE=4, IF=5, ELSE_IF=6, ELSE=7, 
		FOR_EACH=8, TRUE=9, FALSE=10, ARRAY=11, IN=12, INT=13, FLOAT=14, BOOLEAN=15, 
		STRING=16, RETURN=17, NULL=18, CLASS=19, VAL=20, VAR=21, CONSTRUCTOR=22, 
		DESTRUCTOR=23, NEW=24, BY=25, LEFT_PAREN=26, RIGHT_PAREN=27, LEFT_SQUARE_BRACKET=28, 
		RIGHT_SQUARE_BRACKET=29, DOT=30, COMMA=31, SEMICOLON=32, LEFT_CURLY_BRACKET=33, 
		RIGHT_CURLY_BRACKET=34, ESCAPE=35, INTEGER=36, OCTAL_LITERALNESS=37, HEXA_LITERALNESS=38, 
		BINARY_LITERALNESS=39, FLOAT_LITERALNESS=40, BOOLEAN_LITERALNESS=41, STRING_LITERALNESS=42;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"WHITE_SPACE", "COMMENT", "BREAK", "CONTINUE", "IF", "ELSE_IF", "ELSE", 
			"FOR_EACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
			"STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
			"NEW", "BY", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
			"DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
			"SINGLE_QUOTE", "DOUBLE_QUOTE", "ESCAPE", "OCTAL_NOTATION", "HEXA_NOTATION", 
			"BINARY_NOTATION", "OCTAL_DIGIT", "HEXA_DIGIT", "BINARY_DIGIT", "DECIMAL_DIGIT", 
			"EXPONENT", "INTEGER", "OCTAL_LITERALNESS", "HEXA_LITERALNESS", "BINARY_LITERALNESS", 
			"FLOAT_LITERALNESS", "BOOLEAN_LITERALNESS", "STRING_LITERALNESS"
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
			null, "WHITE_SPACE", "COMMENT", "BREAK", "CONTINUE", "IF", "ELSE_IF", 
			"ELSE", "FOR_EACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
			"STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
			"NEW", "BY", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
			"DOT", "COMMA", "SEMICOLON", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
			"ESCAPE", "INTEGER", "OCTAL_LITERALNESS", "HEXA_LITERALNESS", "BINARY_LITERALNESS", 
			"FLOAT_LITERALNESS", "BOOLEAN_LITERALNESS", "STRING_LITERALNESS"
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,\u0197\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\3\2\6\2m\n\2\r\2\16\2n\3\2\3\2\3\3\3\3\3\3\3\3\7\3w\n\3"+
		"\f\3\16\3z\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b"+
		"\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3"+
		"\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16"+
		"\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30"+
		"\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34"+
		"\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3"+
		"&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u0130\n&\3\'\3\'\3(\3(\3("+
		"\3(\5(\u0138\n(\3)\3)\3)\3)\5)\u013e\n)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3."+
		"\5.\u014a\n.\3.\6.\u014d\n.\r.\16.\u014e\3/\5/\u0152\n/\3/\3/\3/\3/\7"+
		"/\u0158\n/\f/\16/\u015b\13/\5/\u015d\n/\3\60\3\60\3\60\3\61\3\61\3\61"+
		"\3\62\3\62\3\62\3\63\6\63\u0169\n\63\r\63\16\63\u016a\3\63\3\63\7\63\u016f"+
		"\n\63\f\63\16\63\u0172\13\63\3\63\5\63\u0175\n\63\3\63\6\63\u0178\n\63"+
		"\r\63\16\63\u0179\3\63\5\63\u017d\n\63\3\63\3\63\6\63\u0181\n\63\r\63"+
		"\16\63\u0182\3\63\5\63\u0186\n\63\5\63\u0188\n\63\3\64\3\64\5\64\u018c"+
		"\n\64\3\65\3\65\3\65\7\65\u0191\n\65\f\65\16\65\u0194\13\65\3\65\3\65"+
		"\4x\u0192\2\66\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16"+
		"\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34"+
		"\67\359\36;\37= ?!A\"C#E$G\2I\2K%M\2O\2Q\2S\2U\2W\2Y\2[\2]&_\'a(c)e*g"+
		"+i,\3\2\13\5\2\13\f\17\17\"\"\5\2\62;CHch\3\2\629\3\2\62\63\3\2\62;\4"+
		"\2GGgg\4\2--//\3\2\63;\3\2$$\2\u01a8\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2"+
		"\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23"+
		"\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2"+
		"\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2"+
		"\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3"+
		"\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2"+
		"\2\2\2C\3\2\2\2\2E\3\2\2\2\2K\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2"+
		"\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3l\3\2\2\2\5r\3\2\2\2\7\u0080"+
		"\3\2\2\2\t\u0086\3\2\2\2\13\u008f\3\2\2\2\r\u0092\3\2\2\2\17\u0099\3\2"+
		"\2\2\21\u009e\3\2\2\2\23\u00a6\3\2\2\2\25\u00ab\3\2\2\2\27\u00b1\3\2\2"+
		"\2\31\u00b7\3\2\2\2\33\u00ba\3\2\2\2\35\u00be\3\2\2\2\37\u00c4\3\2\2\2"+
		"!\u00cc\3\2\2\2#\u00d3\3\2\2\2%\u00da\3\2\2\2\'\u00df\3\2\2\2)\u00e5\3"+
		"\2\2\2+\u00e9\3\2\2\2-\u00ed\3\2\2\2/\u00f9\3\2\2\2\61\u0104\3\2\2\2\63"+
		"\u0108\3\2\2\2\65\u010b\3\2\2\2\67\u010d\3\2\2\29\u010f\3\2\2\2;\u0111"+
		"\3\2\2\2=\u0113\3\2\2\2?\u0115\3\2\2\2A\u0117\3\2\2\2C\u0119\3\2\2\2E"+
		"\u011b\3\2\2\2G\u011d\3\2\2\2I\u011f\3\2\2\2K\u012f\3\2\2\2M\u0131\3\2"+
		"\2\2O\u0137\3\2\2\2Q\u013d\3\2\2\2S\u013f\3\2\2\2U\u0141\3\2\2\2W\u0143"+
		"\3\2\2\2Y\u0145\3\2\2\2[\u0147\3\2\2\2]\u0151\3\2\2\2_\u015e\3\2\2\2a"+
		"\u0161\3\2\2\2c\u0164\3\2\2\2e\u0187\3\2\2\2g\u018b\3\2\2\2i\u018d\3\2"+
		"\2\2km\t\2\2\2lk\3\2\2\2mn\3\2\2\2nl\3\2\2\2no\3\2\2\2op\3\2\2\2pq\b\2"+
		"\2\2q\4\3\2\2\2rs\7%\2\2st\7%\2\2tx\3\2\2\2uw\13\2\2\2vu\3\2\2\2wz\3\2"+
		"\2\2xy\3\2\2\2xv\3\2\2\2y{\3\2\2\2zx\3\2\2\2{|\7%\2\2|}\7%\2\2}~\3\2\2"+
		"\2~\177\b\3\2\2\177\6\3\2\2\2\u0080\u0081\7D\2\2\u0081\u0082\7t\2\2\u0082"+
		"\u0083\7g\2\2\u0083\u0084\7c\2\2\u0084\u0085\7m\2\2\u0085\b\3\2\2\2\u0086"+
		"\u0087\7E\2\2\u0087\u0088\7q\2\2\u0088\u0089\7p\2\2\u0089\u008a\7v\2\2"+
		"\u008a\u008b\7k\2\2\u008b\u008c\7p\2\2\u008c\u008d\7w\2\2\u008d\u008e"+
		"\7g\2\2\u008e\n\3\2\2\2\u008f\u0090\7K\2\2\u0090\u0091\7h\2\2\u0091\f"+
		"\3\2\2\2\u0092\u0093\7G\2\2\u0093\u0094\7n\2\2\u0094\u0095\7u\2\2\u0095"+
		"\u0096\7g\2\2\u0096\u0097\7k\2\2\u0097\u0098\7h\2\2\u0098\16\3\2\2\2\u0099"+
		"\u009a\7G\2\2\u009a\u009b\7n\2\2\u009b\u009c\7u\2\2\u009c\u009d\7g\2\2"+
		"\u009d\20\3\2\2\2\u009e\u009f\7H\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1\7"+
		"t\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4\7e\2\2\u00a4\u00a5"+
		"\7j\2\2\u00a5\22\3\2\2\2\u00a6\u00a7\7V\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9"+
		"\7w\2\2\u00a9\u00aa\7g\2\2\u00aa\24\3\2\2\2\u00ab\u00ac\7H\2\2\u00ac\u00ad"+
		"\7c\2\2\u00ad\u00ae\7n\2\2\u00ae\u00af\7u\2\2\u00af\u00b0\7g\2\2\u00b0"+
		"\26\3\2\2\2\u00b1\u00b2\7C\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4\7t\2\2\u00b4"+
		"\u00b5\7c\2\2\u00b5\u00b6\7{\2\2\u00b6\30\3\2\2\2\u00b7\u00b8\7K\2\2\u00b8"+
		"\u00b9\7p\2\2\u00b9\32\3\2\2\2\u00ba\u00bb\7K\2\2\u00bb\u00bc\7p\2\2\u00bc"+
		"\u00bd\7v\2\2\u00bd\34\3\2\2\2\u00be\u00bf\7H\2\2\u00bf\u00c0\7n\2\2\u00c0"+
		"\u00c1\7q\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7v\2\2\u00c3\36\3\2\2\2\u00c4"+
		"\u00c5\7D\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7n\2\2"+
		"\u00c8\u00c9\7g\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7p\2\2\u00cb \3\2\2"+
		"\2\u00cc\u00cd\7U\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0"+
		"\7k\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7i\2\2\u00d2\"\3\2\2\2\u00d3\u00d4"+
		"\7T\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7v\2\2\u00d6\u00d7\7w\2\2\u00d7"+
		"\u00d8\7t\2\2\u00d8\u00d9\7p\2\2\u00d9$\3\2\2\2\u00da\u00db\7P\2\2\u00db"+
		"\u00dc\7w\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7n\2\2\u00de&\3\2\2\2\u00df"+
		"\u00e0\7E\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3\7u\2\2"+
		"\u00e3\u00e4\7u\2\2\u00e4(\3\2\2\2\u00e5\u00e6\7X\2\2\u00e6\u00e7\7c\2"+
		"\2\u00e7\u00e8\7n\2\2\u00e8*\3\2\2\2\u00e9\u00ea\7X\2\2\u00ea\u00eb\7"+
		"c\2\2\u00eb\u00ec\7t\2\2\u00ec,\3\2\2\2\u00ed\u00ee\7E\2\2\u00ee\u00ef"+
		"\7q\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f2\7v\2\2\u00f2"+
		"\u00f3\7t\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5\7e\2\2\u00f5\u00f6\7v\2\2"+
		"\u00f6\u00f7\7q\2\2\u00f7\u00f8\7t\2\2\u00f8.\3\2\2\2\u00f9\u00fa\7F\2"+
		"\2\u00fa\u00fb\7g\2\2\u00fb\u00fc\7u\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe"+
		"\7t\2\2\u00fe\u00ff\7w\2\2\u00ff\u0100\7e\2\2\u0100\u0101\7v\2\2\u0101"+
		"\u0102\7q\2\2\u0102\u0103\7t\2\2\u0103\60\3\2\2\2\u0104\u0105\7P\2\2\u0105"+
		"\u0106\7g\2\2\u0106\u0107\7y\2\2\u0107\62\3\2\2\2\u0108\u0109\7D\2\2\u0109"+
		"\u010a\7{\2\2\u010a\64\3\2\2\2\u010b\u010c\7*\2\2\u010c\66\3\2\2\2\u010d"+
		"\u010e\7+\2\2\u010e8\3\2\2\2\u010f\u0110\7]\2\2\u0110:\3\2\2\2\u0111\u0112"+
		"\7_\2\2\u0112<\3\2\2\2\u0113\u0114\7\60\2\2\u0114>\3\2\2\2\u0115\u0116"+
		"\7.\2\2\u0116@\3\2\2\2\u0117\u0118\7=\2\2\u0118B\3\2\2\2\u0119\u011a\7"+
		"}\2\2\u011aD\3\2\2\2\u011b\u011c\7\177\2\2\u011cF\3\2\2\2\u011d\u011e"+
		"\7)\2\2\u011eH\3\2\2\2\u011f\u0120\7$\2\2\u0120J\3\2\2\2\u0121\u0122\7"+
		")\2\2\u0122\u0130\7$\2\2\u0123\u0124\7^\2\2\u0124\u0130\7d\2\2\u0125\u0126"+
		"\7^\2\2\u0126\u0130\7h\2\2\u0127\u0128\7^\2\2\u0128\u0130\7t\2\2\u0129"+
		"\u012a\7^\2\2\u012a\u0130\7p\2\2\u012b\u012c\7^\2\2\u012c\u0130\7v\2\2"+
		"\u012d\u012e\7^\2\2\u012e\u0130\7^\2\2\u012f\u0121\3\2\2\2\u012f\u0123"+
		"\3\2\2\2\u012f\u0125\3\2\2\2\u012f\u0127\3\2\2\2\u012f\u0129\3\2\2\2\u012f"+
		"\u012b\3\2\2\2\u012f\u012d\3\2\2\2\u0130L\3\2\2\2\u0131\u0132\7\62\2\2"+
		"\u0132N\3\2\2\2\u0133\u0134\7\62\2\2\u0134\u0138\7z\2\2\u0135\u0136\7"+
		"\62\2\2\u0136\u0138\7Z\2\2\u0137\u0133\3\2\2\2\u0137\u0135\3\2\2\2\u0138"+
		"P\3\2\2\2\u0139\u013a\7\62\2\2\u013a\u013e\7d\2\2\u013b\u013c\7\62\2\2"+
		"\u013c\u013e\7D\2\2\u013d\u0139\3\2\2\2\u013d\u013b\3\2\2\2\u013eR\3\2"+
		"\2\2\u013f\u0140\t\3\2\2\u0140T\3\2\2\2\u0141\u0142\t\4\2\2\u0142V\3\2"+
		"\2\2\u0143\u0144\t\5\2\2\u0144X\3\2\2\2\u0145\u0146\t\6\2\2\u0146Z\3\2"+
		"\2\2\u0147\u0149\t\7\2\2\u0148\u014a\t\b\2\2\u0149\u0148\3\2\2\2\u0149"+
		"\u014a\3\2\2\2\u014a\u014c\3\2\2\2\u014b\u014d\5Y-\2\u014c\u014b\3\2\2"+
		"\2\u014d\u014e\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\\"+
		"\3\2\2\2\u0150\u0152\t\b\2\2\u0151\u0150\3\2\2\2\u0151\u0152\3\2\2\2\u0152"+
		"\u015c\3\2\2\2\u0153\u015d\7\62\2\2\u0154\u0159\t\t\2\2\u0155\u0158\5"+
		"Y-\2\u0156\u0158\7a\2\2\u0157\u0155\3\2\2\2\u0157\u0156\3\2\2\2\u0158"+
		"\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015d\3\2"+
		"\2\2\u015b\u0159\3\2\2\2\u015c\u0153\3\2\2\2\u015c\u0154\3\2\2\2\u015d"+
		"^\3\2\2\2\u015e\u015f\5M\'\2\u015f\u0160\5S*\2\u0160`\3\2\2\2\u0161\u0162"+
		"\5O(\2\u0162\u0163\5U+\2\u0163b\3\2\2\2\u0164\u0165\5Q)\2\u0165\u0166"+
		"\5W,\2\u0166d\3\2\2\2\u0167\u0169\5]/\2\u0168\u0167\3\2\2\2\u0169\u016a"+
		"\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\3\2\2\2\u016c"+
		"\u0170\5=\37\2\u016d\u016f\5Y-\2\u016e\u016d\3\2\2\2\u016f\u0172\3\2\2"+
		"\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170"+
		"\3\2\2\2\u0173\u0175\5[.\2\u0174\u0173\3\2\2\2\u0174\u0175\3\2\2\2\u0175"+
		"\u0188\3\2\2\2\u0176\u0178\5]/\2\u0177\u0176\3\2\2\2\u0178\u0179\3\2\2"+
		"\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017c\3\2\2\2\u017b\u017d"+
		"\5[.\2\u017c\u017b\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u0188\3\2\2\2\u017e"+
		"\u0180\5=\37\2\u017f\u0181\5Y-\2\u0180\u017f\3\2\2\2\u0181\u0182\3\2\2"+
		"\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184\u0186"+
		"\5[.\2\u0185\u0184\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0188\3\2\2\2\u0187"+
		"\u0168\3\2\2\2\u0187\u0177\3\2\2\2\u0187\u017e\3\2\2\2\u0188f\3\2\2\2"+
		"\u0189\u018c\5\23\n\2\u018a\u018c\5\25\13\2\u018b\u0189\3\2\2\2\u018b"+
		"\u018a\3\2\2\2\u018ch\3\2\2\2\u018d\u0192\5I%\2\u018e\u0191\5K&\2\u018f"+
		"\u0191\n\n\2\2\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191\u0194\3\2"+
		"\2\2\u0192\u0193\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0195\3\2\2\2\u0194"+
		"\u0192\3\2\2\2\u0195\u0196\5I%\2\u0196j\3\2\2\2\31\2nx\u012f\u0137\u013d"+
		"\u0149\u014e\u0151\u0157\u0159\u015c\u016a\u0170\u0174\u0179\u017c\u0182"+
		"\u0185\u0187\u018b\u0190\u0192\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}