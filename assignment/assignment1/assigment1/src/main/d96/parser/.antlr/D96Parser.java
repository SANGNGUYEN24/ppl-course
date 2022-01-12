// Generated from d:\Study2\HCMUT\semester212\PPL\code\assignment\assignment1\assigment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class D96Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

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
	public static final int
		RULE_init = 0;
	private static String[] makeRuleNames() {
		return new String[] {
			"init"
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

	@Override
	public String getGrammarFileName() { return "D96.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public D96Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class InitContext extends ParserRuleContext {
		public TerminalNode STRING_LITERALNESS() { return getToken(D96Parser.STRING_LITERALNESS, 0); }
		public InitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init; }
	}

	public final InitContext init() throws RecognitionException {
		InitContext _localctx = new InitContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2);
			match(STRING_LITERALNESS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,\7\4\2\t\2\3\2\3"+
		"\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5\7,\2\2\5\3\3\2\2\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}