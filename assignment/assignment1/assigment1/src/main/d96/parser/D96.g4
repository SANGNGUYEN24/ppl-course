// Nguyen Dinh Sang - 1952955
grammar D96;

@lexer::header {
from lexererr import *
}

options {
language = Python3;
}
//==================== Program struture start ====================
program:  			class_declaration+ EOF;
//-----------------------------------------------------------------
class_declaration:	K_CLASS IDENTIFIER super_class_group?
					LEFT_CURLY_BRACKET class_body_unit* RIGHT_CURLY_BRACKET
					;// Class declaration
class_body_unit:	attribute_declaration | method_declaration
					;
// BUG Program class has super class???
super_class_group: 	COLON IDENTIFIER;
//-----------------------------------------------------------------
method_declaration:	(IDENTIFIER | DOLAR_IDENTIFIER)
                    LEFT_PAREN parameter_list? RIGHT_PAREN block_statement
					| constructor
					| destructor
					;// getSomeThing(){...}
constructor:		K_CONSTRUCTOR LEFT_PAREN parameter_list? RIGHT_PAREN  block_statement
					;
destructor:			K_DESTRUCTOR LEFT_PAREN RIGHT_PAREN  block_statement 
					;
parameter_list: 	parameter | parameter (SEMI_COLON parameter)+
					;//; a, b, c: Int
parameter:    		identifier_list COLON d96_type
					;//a, b, c: String
d96_type:           primitive_type | IDENTIFIER | array_type
                    ;// ID for class type
//----------------------------------------------------------------
attribute_declaration:
                    (K_VAL | K_VAR) mixed_identifier_list COLON d96_type SEMI_COLON // not assigned
                    | (K_VAL | K_VAR) (IDENTIFIER | DOLAR_IDENTIFIER) attribute_value_list expression SEMI_COLON// assigned
                    ;
attribute_value_list:
                    COLON d96_type OP_ASSIGN
                    | COMMA (IDENTIFIER | DOLAR_IDENTIFIER) attribute_value_list expression COMMA
                    ;
identifier_list: 	IDENTIFIER | IDENTIFIER (COMMA IDENTIFIER)+
					;// My1stCons, My2ndCons
mixed_identifier_list:
                    (IDENTIFIER | DOLAR_IDENTIFIER)
                    | (IDENTIFIER | DOLAR_IDENTIFIER)(COMMA (IDENTIFIER | DOLAR_IDENTIFIER))+
                    ;
//==================== Program struture end ====================


//==================== Expression start ====================
expression_list:	expression | expression (COMMA expression)+
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

expression:			relational_expr (OP_STRING_CONCATENATION | OP_TWO_SAME_STRING) relational_expr
					| relational_expr
					;// +. ==

relational_expr:	and_or_expr relational_operator and_or_expr
                    | and_or_expr
					;// == != < > <= >=
and_or_expr:		and_or_expr (OP_LOGICAL_AND | OP_LOGICAL_OR) add_sub_expr
					| add_sub_expr
					;// && ||
add_sub_expr:		add_sub_expr (OP_ADDTION | OP_SUBTRACTION) mul_add_mol_expr
					| mul_add_mol_expr
					;
mul_add_mol_expr:	mul_add_mol_expr (OP_MULTIPLICATION | OP_DIVISION| OP_MODULO) not_expr 
					| not_expr
					;
not_expr:			OP_LOGICAL_NOT not_expr | sign_expr
					;
sign_expr:			(OP_SUBTRACTION) sign_expr | index_operator_expr
					;
index_operator_expr:
					index_operator_expr index_operator | instance_access
					;
// Member access
instance_access:
					instance_access DOT IDENTIFIER
					(LEFT_PAREN expression_list? RIGHT_PAREN)?
					| static_access
					;
static_access:
					IDENTIFIER DOUBLE_COLON DOLAR_IDENTIFIER
					(LEFT_PAREN expression_list? RIGHT_PAREN)?
					| object_creation
					;
// Object creation
object_creation:	K_NEW IDENTIFIER 
					LEFT_PAREN expression_list? RIGHT_PAREN
					| atom_expr
					;

atom_expr:			literal
                    | 'Null'
					| IDENTIFIER
					| LEFT_PAREN expression RIGHT_PAREN
					;
//------------------------------------------------------------------------
//==================== Expression end ====================

//==================== Statement start ====================
// Variable and Constant Declaration Statement
var_val_statement:	(K_VAL | K_VAR) identifier_list COLON d96_type SEMI_COLON // not assigned
                    | (K_VAL | K_VAR) IDENTIFIER var_val_value_list expression SEMI_COLON// assigned
                    ;

var_val_value_list :
                    COLON d96_type OP_ASSIGN
                    | COMMA IDENTIFIER var_val_value_list expression COMMA;
// Assign statement
lhs:                member_access_instance DOT IDENTIFIER
                    | IDENTIFIER DOUBLE_COLON DOLAR_IDENTIFIER
                    | IDENTIFIER
                    | element_expression
                    ;
assign_statement: 	lhs OP_ASSIGN expression SEMI_COLON
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
loop_part:			member_access_instance K_IN expression DOUBLE_DOT expression
					(K_BY expression)?
					;// i In 1 .. 100 [By 2]?
//-----------------------------------------------------------------------------
// Break statement
break_statement:	K_BREAK SEMI_COLON
					;// Break;
// Continue statement
continue_statement:	K_CONTINUE SEMI_COLON
					;// Continue;
// Return statements 
return_statement:   K_RETURN expression? SEMI_COLON
					;
// Method invocation statement
member_access_instance:
                    member_access_instance DOT IDENTIFIER (LEFT_PAREN expression_list? RIGHT_PAREN)?
                    | member_access_static
                    | object_creation
                    ;
member_access_static:
                    IDENTIFIER DOUBLE_COLON
                    (DOLAR_IDENTIFIER | DOLAR_IDENTIFIER LEFT_PAREN expression_list? RIGHT_PAREN)?
                    ;
method_invocation_statement:
                    (member_access_instance DOT IDENTIFIER LEFT_PAREN expression_list? RIGHT_PAREN
                    | IDENTIFIER DOUBLE_COLON DOLAR_IDENTIFIER LEFT_PAREN expression_list? RIGHT_PAREN)
                    SEMI_COLON
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
					| block_statement
					;
//==================== Statement end ====================

//==================== Lexical rules start ====================
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
fragment DOUBLE_QUOTE:	'"';
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
					;
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
// For Array
fragment DECIMAL2: 	[1-9] (DECIMAL_DIGIT*('_'DECIMAL_DIGIT+)*)?
					;
fragment OCTAL2:	OCTAL_NOTATION [1-7]OCTAL_DIGIT*('_'OCTAL_DIGIT+)*
                    ;
fragment HEXA2: 	HEXA_NOTATION [1-9A-F]HEXA_DIGIT*('_' HEXA_DIGIT+)*
					;
fragment BINARY2: 	BINARY_NOTATION '1' BINARY_DIGIT*('_'BINARY_DIGIT+)*
					;
INTEGER_LITERAL2:	(DECIMAL2 | OCTAL2 | HEXA2 | BINARY2)
                    {self.text = self.text.replace("_", "")}
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
// 4. String
STRING_LITERAL		: DOUBLE_QUOTE STR_CHAR* DOUBLE_QUOTE { self.text = self.text[1:-1] };

literal:            INTEGER_LITERAL | INTEGER_LITERAL2 | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL
                    | indexed_array | multi_dimentional_array;
// 5. Indexed array
indexed_array:  		K_ARRAY
						LEFT_PAREN(
							(INTEGER_LITERAL (COMMA INTEGER_LITERAL)*)?
							|(INTEGER_LITERAL2 (COMMA INTEGER_LITERAL2)*)
							|(FLOAT_LITERAL (COMMA FLOAT_LITERAL)*)
							|(BOOLEAN_LITERAL (COMMA BOOLEAN_LITERAL)*)
							|(STRING_LITERAL (COMMA STRING_LITERAL)*)
							|((indexed_array) (COMMA indexed_array)*)
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
IDENTIFIER:			[_a-zA-Z][_a-zA-Z0-9]*;
DOLAR_IDENTIFIER: 	'$'[_a-zA-Z0-9]+;
//==================== 3. Lexical rules end ====================

//==================== 4. Type and Value start ====================

// Primitive type
primitive_type: 	K_BOOLEAN | K_INT | K_FLOAT | K_STRING;

// Array type
// An array type declaration is in the form of: Array[<element_type>, <size>].
array_type: 		K_ARRAY
						LEFT_SQUARE_BRACKET
							(primitive_type | array_type) COMMA INTEGER_LITERAL2
						RIGHT_SQUARE_BRACKET
					;
//==================== Type and Value end ====================
WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING:     DOUBLE_QUOTE STR_CHAR*
                    {
                        y = str(self.text)
                        possible = ['b','\t','\n','\f','\r',"'",'\\']
                        if y[-1] in possible:
                            raise UncloseString(y[1:-1])
                        else:
                            raise UncloseString(y[1:])
                    }
                    ;
ILLEGAL_ESCAPE:     DOUBLE_QUOTE STR_CHAR* ESC_ILLEGAL
                    {
                        y = str(self.text)
                        raise IllegalEscape(y[1:])
                    }
                    ;
fragment STR_CHAR: ~[\b\t\n\f\r"\\] | ESC_ACCEPT | '\'' DOUBLE_QUOTE;

fragment ESC_ACCEPT: '\\' [btnfr"\\] ;

fragment ESC_ILLEGAL: '\\' ~[btnfr"\\] ;

ERROR_CHAR:         .
                    {
                        raise ErrorToken(self.text)
                    }
                    ;








						











