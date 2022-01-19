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

//==================== Lexical rules start ====================
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
K_MAIN:				'main';

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
SEMI_COLON:				';';
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

INTEGER_LITERAL:	(DECIMAL | OCTAL | HEXA | BINARY)
                    {self.text = self.text.replace("_", "")}
					;
// 2. Float
FLOAT_LITERAL       :(DECIMAL DOT DECIMAL? EXPONENT?		
					|DECIMAL EXPONENT						
					|DOT DECIMAL? EXPONENT)				
					{self.text = self.text.replace("_", "")}
					;
// 3. Boolean
BOOLEAN_LITERAL:	'True' | 'False';
// 4. String
STRING_LITERAL: 	DOUBLE_QUOTE 
					(ESCAPE |~('"'| '\\'))*?
					DOUBLE_QUOTE
					;
// 5. Indexed array
indexed_array:  		K_ARRAY
						LEFT_PAREN(
							(INTEGER_LITERAL (COMMA INTEGER_LITERAL)*)?
							|(FLOAT_LITERAL (COMMA FLOAT_LITERAL)*)
							|(BOOLEAN_LITERAL (COMMA BOOLEAN_LITERAL)*)
							|(STRING_LITERAL (COMMA STRING_LITERAL)*)						
						)
						RIGHT_PAREN
					;	// Array() Array(1) Array(1,2,3)
// 6. Multi-dimensional array
multi_dimentional_array: 	K_ARRAY
                            LEFT_PAREN(
                            (indexed_array (COMMA indexed_array)*)?
                            )
                            RIGHT_PAREN
					    ;


// 3.3 Identifier, Dolar identifer
IDENTIFIER:			([a-z] | [A-Z] | '_') ([a-z] | [A-Z] | '_' | [0-9])*;
DOLAR_IDENTIFIER: 	'$'([a-z] | [A-Z] | '_' | [0-9])+;

//==================== 3. Lexical rules end ====================

//==================== 4. Type and Value start ====================

// Primitive type
operator_boolean:	OP_LOGICAL_NOT 		| OP_LOGICAL_AND 	| OP_LOGICAL_OR 
					| OP_IS_EQUAL_TO 	| OP_NOT_EQUAL_TO
					;
operator_integer: 	OP_IS_EQUAL_TO 		| OP_NOT_EQUAL_TO 	| OP_MODULO 		| OP_ADDTION
					| OP_SUBTRACTION 	| OP_MULTIPLICATION | OP_DIVISION 		| OP_LESS_THAN
					| OP_LESS_THAN_EQUAL| OP_GREATER_THAN 	| OP_GREATER_THAN_EQUAL	 
					;
operator_float: 		OP_ADDTION 			| OP_SUBTRACTION 	| OP_MULTIPLICATION | OP_DIVISION 
					| OP_LESS_THAN 		| OP_LESS_THAN_EQUAL| OP_GREATER_THAN 	
					| OP_GREATER_THAN_EQUAL
					;
operator_string: 	OP_TWO_SAME_STRING 	| OP_STRING_CONCATENATION
					;

primitive_type: 	K_BOOLEAN | K_INT | K_FLOAT | K_STRING | K_ARRAY;

// Array type
// An array type declaration is in the form of: Array[<element_type>, <size>].
array_type: 		K_ARRAY
						LEFT_SQUARE_BRACKET
							primitive_type COMMA INTEGER_LITERAL
						RIGHT_SQUARE_BRACKET
					; 

class_type:			K_NEW IDENTIFIER LEFT_PAREN RIGHT_PAREN
					;// New X()
//==================== Type and Value end ====================

//==================== Program struture start ====================

program:  			many_class EOF;
					
many_class: 		class_declaration+
					| class_declaration* program_class_declaration 
					| program_class_declaration class_declaration*
					| program_class_declaration
					;
//-----------------------------------------------------------------
// BUG How about dolar identifer in class name
class_declaration:	K_CLASS IDENTIFIER super_class_group?
					LEFT_CURLY_BRACKET class_body? RIGHT_CURLY_BRACKET
					;// Class declaration
class_body:			class_body_unit*
					;
class_body_unit:	attribute_declaration | method_declaration | statement
					;
// BUG Program class has super class???
super_class_group: 	COLON IDENTIFIER;
//-----------------------------------------------------------------
program_class_declaration:
					K_CLASS 'Program' LEFT_CURLY_BRACKET program_class_body RIGHT_CURLY_BRACKET
					;// Special class which is the entry of the program
program_class_body:	main_method_declaration class_body 
					| class_body main_method_declaration
					;
//-----------------------------------------------------------------
main_method_declaration:
					K_MAIN LEFT_PAREN RIGHT_PAREN
					LEFT_CURLY_BRACKET method_body RIGHT_CURLY_BRACKET
					;// main(){...}

method_declaration:	IDENTIFIER LEFT_PAREN parameter_list? RIGHT_PAREN
                    LEFT_CURLY_BRACKET method_body RIGHT_CURLY_BRACKET
					| constructor
					| destructor
					;// getSomeThing(){...}
constructor:		K_CONSTRUCTOR LEFT_PAREN parameter_list? RIGHT_PAREN 
					LEFT_CURLY_BRACKET method_body RIGHT_CURLY_BRACKET
					;
destructor:			K_DESTRUCTOR LEFT_PAREN RIGHT_PAREN 
					LEFT_CURLY_BRACKET method_body RIGHT_CURLY_BRACKET
					;
parameter_list: 	parameter | parameter parameter_list_tail
					;
parameter_list_tail:
					(SEMI_COLON parameter parameter_list_tail)*
					;//; a, b, c: Int
parameter:    		identifier_list COLON primitive_type
					;//a, b, c: String
method_body:		'method body';
//----------------------------------------------------------------
// BUG how to know how many identifier in the identifier list
// BUG xem lai neu khai bao Array thi phai assign voi Array ex: Var Array a: Array[Int, 2] = Array(1,2)
attribute_declaration: 	
					(K_VAL | K_VAR) 
					identifier_list COLON (array_type | primitive_type) (OP_ASSIGN expression_list)? SEMI_COLON
					;// Val My1stCons, My2ndCons: Int = 1 + 5, 2;
identifier_list: 	IDENTIFIER | IDENTIFIER identifier_list_tail
					| DOLAR_IDENTIFIER (COMMA DOLAR_IDENTIFIER)*
					;// My1stCons, My2ndCons
identifier_list_tail: (COMMA IDENTIFIER)*;

statement: 			'statement';
//==================== Program struture end ====================


//==================== Expression start ====================
expression_list:	expression | expression expression_list_tail
					;// 1+2, 1+2, 2*5

expression_list_tail:	
					(COMMA expression expression_list_tail)*
					;// , 1+2, 1+2, 2*5

return_statement:   K_RETURN expression
					;
expression:			'expr'
					;

operation: unary_operation | binary_operation;
unary_operation: 
;
binary_operation: 	int_operation | float_operation
;

// Arithmetic operations
int_operation:		int_operation (OP_ADDTION | OP_SUBTRACTION) int_operand // Left
					| int_operation (OP_MULTIPLICATION | OP_DIVISION | OP_MODULO) int_operand // Left
					| int_operand
					;

float_operation:	float_operation (OP_ADDTION | OP_SUBTRACTION) float_operand // Left
					| float_operation (OP_MULTIPLICATION | OP_DIVISION) float_operand // Left
					| float_operand
					;
int_operand: 		INTEGER_LITERAL
					| int_float_operand	
					;
float_operand: 		FLOAT_LITERAL
					|int_float_operand
					;

int_float_operand: 	function_call
					;// Common operand for both int and float operations
function_call:;
// Boolean operations
boolean_operation:	OP_LOGICAL_NOT boolean_operand

;
boolean_operand:	BOOLEAN_LITERAL;

//==================== 5. Expression end ====================


WHITE_SPACE: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines











						











