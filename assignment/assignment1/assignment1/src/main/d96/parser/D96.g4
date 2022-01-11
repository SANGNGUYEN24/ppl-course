// 1952955
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program:  EOF;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

//=======================3.Lexical Structure=======================
// TODO: 3.1 Character set


// 3.2 Program comment
COMMENT: '##' .*? '##' -> skip; // ## This is a comment ##
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
LEFT_PAREN: 		  	'(';
RIGHT_PAREN: 		  	')';
LEFT_SQUARE_BRACKET: 	'[';
RIGHT_SQUARE_BRACKET: 	']';
DOT: 					'.';
COMMA: 					',';
SEMICOLON: 				';';
LEFT_CURLY_BRACKET:  	'{';
RIGHT_CURLY_BRACKET: 	'{';
// 3.7 Literals
fragment NUMBER: [0-9];










ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;