grammar D96;

@lexer::header {
from lexererr import *
}

options {
language = Python3;
}
//==================== Program struture start ====================

program:  			many_class EOF;
	
many_class: 		class_declaration+
					| class_declaration* program_class_declaration 
					| program_class_declaration class_declaration*
					| program_class_declaration
					;
//-----------------------------------------------------------------
class_declaration:	K_CLASS IDENTIFIER super_class_group?
					LEFT_CURLY_BRACKET class_body RIGHT_CURLY_BRACKET
					;// Class declaration
class_body:			class_body_unit*
					;
class_body_unit:	attribute_declaration | method_declaration
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
					'main' LEFT_PAREN RIGHT_PAREN block_statement
					;// main(){...}

method_declaration:	identifier LEFT_PAREN parameter_list? RIGHT_PAREN block_statement
					| constructor
					| destructor
					;// getSomeThing(){...}
constructor:		K_CONSTRUCTOR LEFT_PAREN parameter_list? RIGHT_PAREN  block_statement
					;
destructor:			K_DESTRUCTOR LEFT_PAREN RIGHT_PAREN  block_statement 
					;
parameter_list: 	parameter | parameter (SEMI_COLON parameter)+
					;//; a, b, c: Int
parameter:    		identifier_list COLON primitive_type
					;//a, b, c: String
//----------------------------------------------------------------
// BUG xem lai neu khai bao Array thi phai assign voi Array ex: Var Array a: Array[Int, 2] = Array(1,2)
// TODO Xem lai co viec them identifier vao sau COLON
attribute_declaration:
					(K_VAL | K_VAR) 
					(identifier_list | dolar_identifier_list) 
					COLON 
					(array_type | primitive_type | identifier) (OP_ASSIGN expression_list)? SEMI_COLON
					;// Val My1stCons, My2ndCons: Int = 1 + 5, 2;
identifier_list: 	IDENTIFIER | IDENTIFIER (COMMA IDENTIFIER)+
					;// My1stCons, My2ndCons
dolar_identifier_list: 	
					DOLAR_IDENTIFIER | DOLAR_IDENTIFIER (COMMA DOLAR_IDENTIFIER)+
					;// $My1stCons, $My2ndCons
//==================== Program struture end ====================


//==================== Expression start ====================
expression_list:	expression | expression (COMMA expression)*
					;// 1+2, 1+2, 2*5
//----------------------------------------------------------------
// Index operator
element_expression:	expression index_operator
					;
index_operator:		LEFT_SQUARE_BRACKET expression RIGHT_SQUARE_BRACKET index_operator*
					;// a[1] or b[1][2] or A[1+2]
//-----------------------------------------------------------------
// All expression
relational_operator:
					OP_IS_EQUAL_TO
					| OP_NOT_EQUAL_TO
					| OP_LESS_THAN
					| OP_LESS_THAN_EQUAL
					| OP_GREATER_THAN
					| OP_GREATER_THAN_EQUAL
					;

expression:			expression (OP_STRING_CONCATENATION | OP_TWO_SAME_STRING) relational_expr
					| relational_expr
					;

relational_expr:	relational_expr relational_operator and_or_expr | and_or_expr
					;
and_or_expr:		and_or_expr (OP_LOGICAL_AND | OP_LOGICAL_OR) add_sub_expr
					| add_sub_expr
					;
add_sub_expr:		add_sub_expr (OP_ADDTION | OP_SUBTRACTION) mul_add_mol_expr
					| mul_add_mol_expr
					;
mul_add_mol_expr:	mul_add_mol_expr (OP_MULTIPLICATION | OP_DIVISION| OP_MODULO) not_expr 
					| not_expr
					;
not_expr:			<assoc=right> OP_LOGICAL_NOT not_expr | sign_expr
					;
sign_expr:			<assoc=right> (OP_SUBTRACTION) sign_expr | index_operator_expr
					;

index_operator_expr:
					index_operator_expr index_operator | instance_attribute_access
					;
// Member access
instance_attribute_access:
					instance_attribute_access DOT IDENTIFIER | instace_method_invocation
					;// getClassObject.object
					// TODO review lai dieu kien co DOLAR_IDENTIFIER ko?
					// <expression> is an expression that returns an object of a class and 
					// <identifier> is an attribute of the class.	
instace_method_invocation:
					instace_method_invocation DOUBLE_COLON IDENTIFIER 
					LEFT_PAREN expression_list? RIGHT_PAREN 
					| object_creation
					;// the first <identifier> is a class name and 
					// <identifier> is a static method name of the class. 
static_method_invocation:
					IDENTIFIER DOUBLE_COLON 
					LEFT_PAREN expression_list? RIGHT_PAREN
					;
static_attribute_access:
					IDENTIFIER DOUBLE_COLON IDENTIFIER
					;// the first <identifier> is a class name, and 
					// the second <identifier> is a static attribute of the class.
// Object creation
object_creation:	K_NEW IDENTIFIER 
					LEFT_PAREN expression_list? RIGHT_PAREN
					| atom_expr
					;

atom_expr:			literal
					| IDENTIFIER
					| LEFT_PAREN expression RIGHT_PAREN
					| function_call
					| static_method_invocation
					| static_attribute_access
					;
function_call:		IDENTIFIER LEFT_PAREN expression_list? RIGHT_PAREN
					;
//------------------------------------------------------------------------
//==================== Expression end ====================

//==================== Statement start ====================
// Variable and Constant Declaration Statement
// TODO check xem co dung dolar identifier ko?
// TODO Xem lai co viec them identifier vao sau COLON
var_val_statement:	(K_VAL | K_VAR) 
					identifier_list 
					COLON 
					(array_type | primitive_type) (OP_ASSIGN expression_list)? SEMI_COLON
					;// Val My1stCons, My2ndCons: Int = 1 + 5, 2;
					// However, the static property of attribute cannot be applied to them 
					// so its name should not follow the dollar identifier rule.
// Assign statement
assign_statement: 	(identifier | element_expression) OP_ASSIGN expression SEMI_COLON
					;
// If statement
// ---------------------------------------------------------------------------
if_statement:		if_part
					else_if_part*
					else_part?
					;
if_part:			K_IF LEFT_PAREN expression RIGHT_PAREN block_statement		
					;
else_if_part:		K_ELSE_IF LEFT_PAREN expression RIGHT_PAREN block_statement
					;
else_part:			K_ELSE block_statement
					;
//-----------------------------------------------------------------------------		
// For in statement
//-----------------------------------------------------------------------------
for_in_statement:	K_FOR_EACH
					LEFT_PAREN loop_part RIGHT_PAREN
					block_statement
					;
loop_part:			IDENTIFIER K_IN INTEGER_LITERAL DOUBLE_DOT INTEGER_LITERAL
					(K_BY INTEGER_LITERAL)?
					;// i In 1 .. 100 [By 2]?
//-----------------------------------------------------------------------------
// Break statement
break_statement:	K_BREAK SEMI_COLON
					;// Break;
// Continue statement
continue_statement:	K_CONTINUE SEMI_COLON
					;// Continue;
// Return statements 
return_statement:   K_RETURN expression SEMI_COLON
					;
// Method invocation statement
method_invocation_statement: 
					IDENTIFIER DOUBLE_COLON DOLAR_IDENTIFIER LEFT_PAREN RIGHT_PAREN SEMI_COLON
					;// Shape::$getNumOfShape();
block_statement:	LEFT_CURLY_BRACKET
					statement*
					RIGHT_CURLY_BRACKET
					;//The <block statement> includes zero or many statements

statement: 			var_val_statement
					| assign_statement
					| if_statement
					| for_in_statement
					| break_statement
					| continue_statement
					| return_statement
					| method_invocation_statement
					;

//==================== Statement end ====================

//==================== Lexical rules start ====================
WHITE_SPACE: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
// 3.2 Program comment
COMMENT: 			'##' .*? '##' -> skip; 	// ## This is a comment ##
// 3.4 Keywords, define the keywords on top
K_BREAK: 			'Break';
K_CONTINUE: 		'Continue';
K_IF: 				'If'; 
K_ELSE_IF: 			'Elseif'; 
K_ELSE: 			'Else';
K_FOR_EACH: 		'Foreach';
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
K_SELF:				'Self';

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
DOUBLE_DOT:				'..';
COMMA:					',';
COLON : 				':' ;
DOUBLE_COLON:			'::';
SEMI_COLON:				';';
LEFT_CURLY_BRACKET:		'{';
RIGHT_CURLY_BRACKET:	'}';
// Quote
fragment SINGLE_QUOTE:	'\'';
fragment DOUBLE_QUOTE:	'"';
// Escape
fragment ESCAPE: 		'\\' [bfrnt'\\];
// 3.7 Literals
fragment OCTAL_NOTATION: 	'0';
fragment HEXA_NOTATION: 	'0x' | '0X';
fragment BINARY_NOTATION: 	'0b' | '0B';
fragment HEXA_DIGIT: 		[0-9A-F]; 		// base 16
fragment OCTAL_DIGIT: 		[0-7]; 				// base 8
fragment BINARY_DIGIT: 		[01]; 				// base 2

fragment DECIMAL_DIGIT:		[0-9];


// 1. Integer
fragment DECIMAL: 	DECIMAL_DIGIT | [1-9]DECIMAL_DIGIT*('_'DECIMAL_DIGIT+)*
					;
fragment OCTAL:		OCTAL_NOTATION ( 
					'0' | [1-7]OCTAL_DIGIT*('_'OCTAL_DIGIT+)*
					)
					;// '0'([0-7]+'_')*[0-7]+

fragment HEXA: 		HEXA_NOTATION(
					'0'
					| [1-9A-F]HEXA_DIGIT*('_' HEXA_DIGIT+)*
					)
					;

fragment BINARY: 	BINARY_NOTATION(
					'0'
					| '1'BINARY_DIGIT*('_'BINARY_DIGIT+)*
					)
					;

INTEGER_LITERAL:	(DECIMAL | OCTAL | HEXA | BINARY)
                    {self.text = self.text.replace("_", "")}
					;
// For Float
fragment INTEGER_PART:	DECIMAL;
fragment DECIMAL_PART:	DOT DECIMAL_DIGIT*;
fragment EXPONENT: 		[eE][-+]? DECIMAL_DIGIT+;

// 2. Float
FLOAT_LITERAL       :(INTEGER_PART DECIMAL_PART EXPONENT?	
					| INTEGER_PART EXPONENT
					| DECIMAL_PART EXPONENT)
					{self.text = self.text.replace("_", "")}
					;

// 3. Boolean
BOOLEAN_LITERAL:	'True' | 'False';

fragment CHAR: 		ESCAPE | ~["\\] | '\'"'
					;
// 4. String
STRING_LITERAL		: DOUBLE_QUOTE CHAR* DOUBLE_QUOTE;

literal:            INTEGER_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL
                    | indexed_array | multi_dimentional_array;
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

// TODO check so expr bang so bien
// var_dcl : VAL_VAR id_list CL data_type // not assigned
//         | VAL_VAR ID var_dcl_list expr; // assigned

// var_dcl_list : CL data_type ASSIGN_OP
//              | CM ID var_dcl_list expr CM;

// 3.3 Identifier, Dolar identifer
IDENTIFIER:			([a-z] | [A-Z] | '_') ([a-z] | [A-Z] | '_' | [0-9])*;
DOLAR_IDENTIFIER: 	'$'([a-z] | [A-Z] | '_' | [0-9])+;
// TODO Why main is not a ID?
identifier: 		IDENTIFIER | DOLAR_IDENTIFIER | 'main';
//==================== 3. Lexical rules end ====================

//==================== 4. Type and Value start ====================

// Primitive type
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


// TODO Xem lai may cai nay
ILLEGAL_ESCAPE:     DOUBLE_QUOTE CHAR* '\\' ~[bfrnt'\\]* {raise IllegalEscape(self.text[1:])};
UNCLOSE_STRING:     DOUBLE_QUOTE (~'"' | '\'"')* (EOF | '\n') {raise UncloseString(self.text[1:])};
ERROR_TOKEN : 		. {raise ErrorToken(self.text)};










						











