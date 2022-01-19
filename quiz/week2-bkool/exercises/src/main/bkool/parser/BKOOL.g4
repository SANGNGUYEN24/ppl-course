grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: many_declaration  EOF
;
many_declaration: one_declaration declaration_list
;
declaration_list: (one_declaration declaration_list)*
;
one_declaration: variable_declaration | function_declaration
;
// write for program rule here using vardecl and funcdecl
SEMI_COLON : ';';
COMMA: ',';
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_CURLY_BRACKET: '{';
RIGHT_CURLY_BRACKET: '}';
ASSIGN : '=';
ID:	[a-zA-Z_]+[a-zA-Z0-9_]*
;

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
LITERAL_FLOAT       :(DECIMAL '.' DECIMAL? EXPONENT?		
					|DECIMAL EXPONENT						
					|'.' DECIMAL? EXPONENT)				
					{self.text = self.text.replace("_", "")}
					;


variable_declaration: 	typeVar identifer_list SEMI_COLON
; // int a,b,c;
identifer_list: 		ID | ID identifer_list_tail
; // a or ,a,b
identifer_list_tail: 	(COMMA ID identifer_list_tail)*
; // empty ,b,c
function_declaration: 	typeVar ID parameter LEFT_CURLY_BRACKET body RIGHT_CURLY_BRACKET
;
parameter:				LEFT_PAREN parameter_list? RIGHT_PAREN
;
parameter_list:			one_parameter | one_parameter parameter_list_tail
;
parameter_list_tail: 	(SEMI_COLON one_parameter parameter_list_tail)*
;// ; float c,d,e,f
one_parameter:	typeVar identifer_list
;// float a,b,c

typeVar : 'int' | 'float';

body:  (variable_declaration | assignment_statement | return_statement | function_declaration|call)*
;

assignment_statement: 	ID ASSIGN expression SEMI_COLON
;// An assignment statement starts with an identifier, then an equal ’=’, then an expression
call: 					ID LEFT_PAREN expression_list? RIGHT_PAREN
;// A call starts with an identifier and then follows by a null-able 
// comma-separated list of expressions enclosed by round brackets.
expression_list:  		expression | expression expression_list_tail 
;
expression_list_tail: 	(COMMA expression expression_list_tail)*
;
return_statement: 		'return' expression SEMI_COLON
;
//A return statement starts with a symbol ’return’ and then an expression. 
expression: 	operand '+' expression
				| expression '-' expression
				| expression ('*'|'/') operand
				| operand
;

operand: sub_expression
		| LITERAL_INTEGER 
		| LITERAL_FLOAT 
		| call
		| ID
;
sub_expression: LEFT_PAREN expression RIGHT_PAREN
;



WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};