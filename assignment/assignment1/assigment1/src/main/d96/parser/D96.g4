grammar D96;

@lexer::header {
from lexererr import *
}

options {
language = Python3;
}
// @lexer::members {
// def emit(self):
//     tk = self.type
//     result = super().emit()
//     if tk == self.ERROR_TOKEN:
//         raise ErrorToken(result.text)
//     elif tk == self.UNCLOSE_STRING:       
//         raise UncloseString(result.text)
//     elif tk == self.ILLEGAL_ESCAPE:
//         raise IllegalEscape(result.text)
//     elif tk == self.UNTERMINATED_COMMENT:
//         raise UnterminatedComment()
//     else:
//         return result;
// }

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
literal:			(OP_ADDTION | OP_SUBTRACTION)*
					(LITERAL_INTEGER
                    |LITERAL_FLOAT
                    |LITERAL_BOOLEAN
                    |LITERAL_STRING)+
                    ;

identifer:			IDENTIFER 
					|DOLAR_IDENTIFIER
					;

// 5. Indexed array
indexedArray:  		K_ARRAY
						LEFT_PAREN(
							(LITERAL_INTEGER (COMMA LITERAL_INTEGER)*)?
							|(LITERAL_FLOAT (COMMA LITERAL_FLOAT)*)
							|(LITERAL_BOOLEAN (COMMA LITERAL_BOOLEAN)*)
							|(LITERAL_STRING (COMMA LITERAL_STRING)*)						
						)
						RIGHT_PAREN
					;	// Array() Array(1) Array(1,2,3)

multiDimentionalArray: 	K_ARRAY
                            LEFT_PAREN(
                            (indexedArray (COMMA indexedArray)*)?
                            )
                            RIGHT_PAREN
					    ;

allTest: literal | identifer | indexedArray | multiDimentionalArray;
					
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

// 3.5 Operators
OP_ASSIGN: 					'=';
// Boolean type
OP_LOGICAL_NOT:				'!';
OP_LOGICAL_OR:				'||';
OP_LOGICAL_AND:				'&&';

// Boolean + Integer
OP_IS_EQUAL_TO:				'==';
OP_NOT_EQUAL_TO:			'!=';

// Integer
OP_MODULO:					'%';

// Integer + Float
OP_ADDTION:					'+';
OP_SUBTRACTION:				'-';
OP_MULTIPLICATION:			'*';
OP_DIVISION:				'/';
OP_LESS_THAN:				'<';
OP_LESS_THAN_EQUAL:			'<=';
OP_GREATER_THAN:			'>';
OP_GREATER_THAN_EQUAL:		'>=';

// String
OP_STRING_CONCATENATION:	'+.';
OP_TWO_SAME_STRING:			'==.';

// 3.6 Seperators
LEFT_PAREN:				'(';
RIGHT_PAREN:			')';
LEFT_SQUARE_BRACKET:	'[';
RIGHT_SQUARE_BRACKET:	']';
DOT:					'.';
COMMA:					',';
COLON : 				':' ;
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
fragment EXPONENT: 			[eE][-+]? DECIMAL+;

// 1. Integer
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
LITERAL_FLOAT       :(DECIMAL DOT DECIMAL? EXPONENT?		
					|DECIMAL EXPONENT						
					|DOT DECIMAL? EXPONENT)				
					{self.text = self.text.replace("_", "")}
					;
// 3. Boolean
LITERAL_BOOLEAN:	'True' | 'False';
// 4. String
LITERAL_STRING: 	DOUBLE_QUOTE 
					(ESCAPE |~('"'| '\\'))*?
					DOUBLE_QUOTE
					;

// 3.3 Identifier, Dolar identifer
IDENTIFER:			([a-z] | [A-Z] | '_') ([a-z] | [A-Z] | '_' | [0-9])*;
DOLAR_IDENTIFIER: 	'$'([a-z] | [A-Z] | '_' | [0-9])+;

//==================== 3. Lexical rules end ====================

//==================== 4. Type and Value start ====================

// 4.1 Primitive type
operatorBoolean:	OP_LOGICAL_NOT 		| OP_LOGICAL_AND 	| OP_LOGICAL_OR 
					| OP_IS_EQUAL_TO 	| OP_NOT_EQUAL_TO
					;
operatorInteger: 	OP_IS_EQUAL_TO 		| OP_NOT_EQUAL_TO 	| OP_MODULO 		| OP_ADDTION
					| OP_SUBTRACTION 	| OP_MULTIPLICATION | OP_DIVISION 		| OP_LESS_THAN
					| OP_LESS_THAN_EQUAL| OP_GREATER_THAN 	| OP_GREATER_THAN_EQUAL	 
					;
operatorFloat: 		OP_ADDTION 			| OP_SUBTRACTION 	| OP_MULTIPLICATION | OP_DIVISION 
					| OP_LESS_THAN 		| OP_LESS_THAN_EQUAL| OP_GREATER_THAN 	
					| OP_GREATER_THAN_EQUAL
					;
operatorString: 	OP_TWO_SAME_STRING 	| OP_STRING_CONCATENATION
					;

primitiveType: 		K_BOOLEAN | K_INT | K_FLOAT | K_STRING | K_ARRAY;

// 4.2 Array type
// An array type declaration is in the form of: Array[<element_type>, <size>].
arrayType: 			K_ARRAY
						LEFT_SQUARE_BRACKET
							primitiveType COMMA LITERAL_INTEGER
						RIGHT_SQUARE_BRACKET
					; 

// TODO 4.3 Class type
//==================== 4. Type and Value end ====================

//==================== 5. Expression start ====================
// 2.2 Attribute declaration
attributeDeclaration: 	(K_VAL | K_VAR) identiferList COLON primitiveType OP_ASSIGN expressionList
						; //Val My1stCons, My2ndCons: Int = 1 + 5, 2;

identiferList: 		IDENTIFER (COMMA IDENTIFER)*
					| DOLAR_IDENTIFIER (COMMA DOLAR_IDENTIFIER)*
					; // My1stCons, My2ndCons

// 2.1 Class declaration
classDeclaration: 	K_CLASS	
						IDENTIFER
							(COLON IDENTIFER)?
								LEFT_CURLY_BRACKET
									blockStatement?
								RIGHT_CURLY_BRACKET
					;
// 2.3 Method declaration
methodDeclaration: 	identifer listOfParameter blockStatement
					; // BUG review
constructor:		K_CONSTRUCTOR 
						LEFT_PAREN 
							listOfParameter 
						RIGHT_PAREN 
						blockStatement
					; // BUG review
destructor:			K_DESTRUCTOR (LEFT_PAREN RIGHT_PAREN) blockStatement
					;// BUG review
// TODO listOfParameter
listOfParameter:;
// TODO blockStatement
blockStatement:;
// TODO expressionList
expressionList:;

			


//==================== 5. Expression end ====================





WHITE_SPACE: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines











						











