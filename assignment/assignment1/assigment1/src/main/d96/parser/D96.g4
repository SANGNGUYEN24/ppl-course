grammar D96;

  @lexer::header {
  from lexererr import *
  }

  options {
  	language = Python3;
  }

//  ERROR_CHAR: .{raise ErrorToken (self.text)};
//  UNCLOSE_STRING: .;
//  ILLEGAL_ESCAPE: .;

//-----
// program: mptype 'main' LEFT_PAREN RIGHT_PAREN LEFT_CURLY_BRACKET body? RIGHT_CURLY_BRACKET EOF;

// mptype: 		INTTYPE | VOIDTYPE;

// body: 			funcall SEMICOLON;

// exp: 			funcall;

// funcall: 		LEFT_PAREN exp? RIGHT_PAREN;

// INTTYPE: 		'int';

// VOIDTYPE: 		'void';

// -----
/** A rule called init that matches comma-separated values between {...}. */
// init : LEFT_CURLY_BRACKET value (COMMA value)* RIGHT_CURLY_BRACKET ;
/** A value can be either a nested array/struct or a simple integer (INT) */
// value : init | TEST;
// parser rules start with lowercase letters, lexer rules with uppercase
// TEST: DECIMAL_DIGIT+;

literalness:    
					SIGN*
					(LITERAL_INTEGER
                    |LITERAL_FLOAT
                    |LITERAL_OCTAL
                    |LITERAL_HEXA
                    |LITERAL_BINARY
                    |LITERAL_BOOLEAN
                    |LITERAL_STRING
                    |LITERAL_BOOLEAN)*
                    ;

identifer:			IDENTIFER 
					|DOLAR_IDENTIFIER
					;
indexedArray:		INDEXED_ARRAY;
					
//-------

WHITE_SPACE: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


//=======================3.Lexical Structure=======================
// TODO: 3.1 Character set


// 3.2 Program comment
COMMENT: 			'##' .*? '##' -> skip; 	// ## This is a comment ##
// TODO: 3.3 Identifier, Dolar identifer
IDENTIFER			:([a-z] | [A-Z] | '_') ([a-z] | [A-Z] | '_' | [0-9])*
					;
DOLAR_IDENTIFIER: 	'$'([a-z] | [A-Z] | '_' | [0-9])+;
// 3.4 Keywords
K_BREAK: 			'Break'; 
K_CONTINUE: 		'Continue';
K_IF: 				'If'; 
K_ELSE_IF: 			'Elseif'; 
K_ELSE: 			'Else';
K_FOR_EACH: 		'Foreach';
// TODO xem lại True False
//TRUE: 		'True';
//FALSE: 		'False';
K_ARRAY:			'Array';
K_IN: 				'In';
K_INT: 				'Int';
K_FLOAT: 			'Float';
K_BOOLEAN: 			'Boolean';
K_STRING:			'String';
K_RETURN:			'Return';
K_NULL: 			'Null';
K_CLASS: 			'Class';
K_VAL: 				'Val';
K_VAR: 				'Var';
K_CONSTRUCTOR:		'Constructor';
K_DESTRUCTOR:		'Destructor';
K_NEW:				'New';
K_BY: 				'By';

// TODO: 3.5 Operators
// 3.6 Seperators
LEFT_PAREN:				'(';
RIGHT_PAREN:			')';
LEFT_SQUARE_BRACKET:	'[';
RIGHT_SQUARE_BRACKET:	']';
DOT:					'.';
COMMA:					',';
SEMICOLON:				';';
LEFT_CURLY_BRACKET:		'{';
RIGHT_CURLY_BRACKET:	'}';
// Quote
fragment SINGLE_QUOTE:	'\'';
fragment DOUBLE_QUOTE:	'"';
// Escape
ESCAPE:				 	'\'"' 
						|'\\b'		// \b backspace
						|'\\f'		// \f form feed
						|'\\r'		// \r carriage return
						|'\\n'		// \n newline
						|'\\t'		// \t horizontal tab
						|'\\\\';	// \\ backslash
									// \' single quote
// 3.7 Literals
fragment OCTAL_NOTATION: 	'0';
fragment HEXA_NOTATION: 	'0x' | '0X';
fragment BINARY_NOTATION: 	'0b' | '0B';
fragment HEXA_DIGIT: 		[0-9a-fA-F]; 		// base 16
fragment OCTAL_DIGIT: 		[0-7]; 				// base 8
fragment BINARY_DIGIT: 		[01]; 				// base 2

fragment DECIMAL_DIGIT:		[0-9];
fragment EXPONENT: 			[eE][-+]? LITERAL_INTEGER+;

// 1. Integer
SIGN: 				[-+];
LITERAL_INTEGER:	DECIMAL_DIGIT | [1-9](DECIMAL_DIGIT | '_')*
                        {self.text = self.text.replace("_", "")};

LITERAL_OCTAL:		OCTAL_NOTATION OCTAL_DIGIT+;

LITERAL_HEXA: 		HEXA_NOTATION HEXA_DIGIT+;

LITERAL_BINARY: 	BINARY_NOTATION BINARY_DIGIT+;
// 2. Float
LITERAL_FLOAT       :LITERAL_INTEGER+ DOT LITERAL_INTEGER* EXPONENT?		// 10.20 or 10. or 10.2e10 or 10.e2
					|[1-9]+ EXPONENT?							// 10 or 10e10 NOT 08 09
					DOT LITERAL_INTEGER+ EXPONENT?				// .10 or .10e10 NOT .e10
					;
// 3. Boolean
LITERAL_BOOLEAN:	'True' | 'False';
// 4. String
LITERAL_STRING: 	DOUBLE_QUOTE 
					(ESCAPE |~('"'| '\\'))*?
					;
// 5. Indexed array
// TODO Array(1,) or Array(1)
INDEXED_ARRAY:  	K_ARRAY
						LEFT_PAREN(
							(LITERAL_INTEGER		// Only 1 element
							|((LITERAL_INTEGER',')+ LITERAL_INTEGER))
							|
							((LITERAL_OCTAL		// Only 1 element
							|((LITERAL_OCTAL',')+ LITERAL_OCTAL)))
							|
							((LITERAL_HEXA		// Only 1 element
							|((LITERAL_HEXA',')+ LITERAL_HEXA)))
						)
						RIGHT_PAREN
					;
// TODO Research about how to read tokens










						











