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
ID:	[a-zA-Z_]+[a-zA-Z0-9_]*
;

variable_declaration: 	typeVar identifer_list SEMI_COLON
; // int a,b,c;
identifer_list: 		ID | ID identifer_list_tail
; // a or ,a,b
identifer_list_tail: 	(COMMA ID identifer_list_tail)*
; // empty ,b,c
function_declaration: 	typeVar ID parameter body
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

body: 'body';

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};