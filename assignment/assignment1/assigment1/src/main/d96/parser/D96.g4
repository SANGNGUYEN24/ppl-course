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

//==================== Parser rules start ====================
literal:
					SIGN*
					(LITERAL_INTEGER
                    |LITERAL_FLOAT
                    |LITERAL_BOOLEAN
                    |LITERAL_STRING)*
                    ;

identifer:			IDENTIFER 
					|DOLAR_IDENTIFIER
					;

// 5. Indexed array
// TODO Array(1,) or Array(1) how about Array()
indexedArray:  		K_ARRAY
						LEFT_PAREN(
							(LITERAL_INTEGER		// Only 1 element
							|((LITERAL_INTEGER',')+ LITERAL_INTEGER))
							|
							(LITERAL_FLOAT		
							|((LITERAL_FLOAT',')+ LITERAL_FLOAT))
							|
							(LITERAL_BOOLEAN		
							|((LITERAL_BOOLEAN',')+ LITERAL_BOOLEAN))
							|
							(LITERAL_STRING	
							|((LITERAL_STRING',')+ LITERAL_STRING))
						)
						RIGHT_PAREN
					;

multiDimentionalArray: 	K_ARRAY
                            LEFT_PAREN(
                            indexedArray
                            |(indexedArray',')+indexedArray
                            )
                            RIGHT_PAREN
					    ;

// all: literal | identifer | indexedArray | multiDimentionalArray;
					
//==================== Parser rules end ====================


//==================== 3. Lexical rules start ====================
// TODO: 3.1 Character set
// 3.2 Program comment
COMMENT: 			'##' .*? '##' -> skip; 	// ## This is a comment ##
// 3.4 Keywords, define the keywords on top
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
SIGN: 					[-+];
// 3.7 Literals
fragment OCTAL_NOTATION: 	'0';
fragment HEXA_NOTATION: 	'0x' | '0X';
fragment BINARY_NOTATION: 	'0b' | '0B';
fragment HEXA_DIGIT: 		[0-9a-fA-F]; 		// base 16
fragment OCTAL_DIGIT: 		[0-7]; 				// base 8
fragment BINARY_DIGIT: 		[01]; 				// base 2

fragment DECIMAL_DIGIT:		[0-9];
fragment EXPONENT: 			[eE][-+]? DECIMAL+;

// 1. Integer
// TODO About the underscores (_), they only appear BETWEEN DIGITS, 
// which means they cannot appear at the beginning or at the end of literals or be duplicated.

fragment DECIMAL: 	DECIMAL_DIGIT | [1-9]'_'?(DECIMAL_DIGIT+'_')*DECIMAL_DIGIT+
					;

fragment OCTAL:		OCTAL_NOTATION (OCTAL_DIGIT+'_')*OCTAL_DIGIT+
					;// '0'([0-7]+'_')*[0-7]+

fragment HEXA: 		HEXA_NOTATION (HEXA_DIGIT+'_')*HEXA_DIGIT+
					;

fragment BINARY: 	BINARY_NOTATION (BINARY_DIGIT+'_')*BINARY_DIGIT+
					;

LITERAL_INTEGER:	(DECIMAL | OCTAL | HEXA | BINARY)
                    {self.text = self.text.replace("_", "")}
					;
// 2. Float
// TODO xem lại
LITERAL_FLOAT       :(DECIMAL DOT DECIMAL EXPONENT?		
					|DECIMAL EXPONENT						
					|DOT DECIMAL EXPONENT)				
					{self.text = self.text.replace("_", "")}
					;
// 3. Boolean
LITERAL_BOOLEAN:	'True' | 'False';
// 4. String
LITERAL_STRING: 	DOUBLE_QUOTE 
					(ESCAPE |~('"'| '\\'))*?
					DOUBLE_QUOTE
					;

// TODO: 3.3 Identifier, Dolar identifer
IDENTIFER:			([a-z] | [A-Z] | '_') ([a-z] | [A-Z] | '_' | [0-9])*;
DOLAR_IDENTIFIER: 	'$'([a-z] | [A-Z] | '_' | [0-9])+;


test: LITERAL_FLOAT;


WHITE_SPACE: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
//==================== 3. Lexical rules end ====================











						











