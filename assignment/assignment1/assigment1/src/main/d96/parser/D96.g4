grammar D96;

// @lexer::header {
// from lexererr import *
// }

// options {
// 	language = Python3;
// }

// ERROR_CHAR: .{raise ErrorToken (self.text)};
// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;

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

init: STRING_LITERALNESS;
//-------

WHITE_SPACE: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


//=======================3.Lexical Structure=======================
// TODO: 3.1 Character set


// 3.2 Program comment
COMMENT: 	'##' .*? '##' -> skip; 	// ## This is a comment ##
// TODO: 3.3 Identifier, Dolar identifer
// 3.4 Keywords
BREAK: 		'Break'; 
CONTINUE: 	'Continue';
IF: 		'If'; 
ELSE_IF: 	'Elseif'; 
ELSE: 		'Else';
FOR_EACH: 	'Foreach'; 
TRUE: 		'True'; 
FALSE: 		'False';
ARRAY:		'Array';
IN: 		'In';
INT: 		'Int';
FLOAT: 		'Float';
BOOLEAN: 	'Boolean';
STRING:		'String';
RETURN:		'Return';
NULL: 		'Null';
CLASS: 		'Class';
VAL: 		'Val';
VAR: 		'Var';
CONSTRUCTOR:'Constructor';
DESTRUCTOR:	'Destructor';
NEW:		'New';
BY: 		'By';

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
fragment OCTAL_DIGIT: 		[0-9a-fA-F]; 		// base 16
fragment HEXA_DIGIT: 		[0-7]; 				// base 8
fragment BINARY_DIGIT: 		[0-1]; 				// base 2

fragment DECIMAL_DIGIT:		[0-9];
fragment EXPONENT: 			[eE][-+]? DECIMAL_DIGIT+;
// Integer - decimal literal
INTEGER: 				[-+]?('0' | [1-9](DECIMAL_DIGIT | '_')*) ;	// 0, 123, 12_123
						// {self.text = self.text.replace("_", "")};

OCTAL_LITERALNESS:		OCTAL_NOTATION OCTAL_DIGIT;

HEXA_LITERALNESS: 		HEXA_NOTATION HEXA_DIGIT;

BINARY_LITERALNESS: 	BINARY_NOTATION BINARY_DIGIT;

FLOAT_LITERALNESS
						:INTEGER+ DOT DECIMAL_DIGIT* EXPONENT?		// 10.20 or 10. or 10.2e10 or 10.e2
						|INTEGER+ EXPONENT?							// 10 or 10e10 
						|DOT DECIMAL_DIGIT+ EXPONENT?				// .10 or .10e10 NOT .e10
						;

BOOLEAN_LITERALNESS:	TRUE | FALSE;

STRING_LITERALNESS: 	DOUBLE_QUOTE 
						(ESCAPE |~["])*? 
						DOUBLE_QUOTE;







