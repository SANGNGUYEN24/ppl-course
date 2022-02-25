// Nguyen Dinh Sang - 1952955
grammar D96;

@lexer::header {
from lexererr import *
}

options {
language = Python3;
}
//==================== Program struture start ====================
program:  			classDeclaration+ EOF;
//-----------------------------------------------------------------
classDeclaration:	normalClassDecl
                    | programClassDecl
					;// Class declaration
normalClassDecl:    K_CLASS (K_MAIN | IDENTIFIER) (COLON IDENTIFIER)?
					LEFT_CURLY_BRACKET memberDeclaration* RIGHT_CURLY_BRACKET
                    ;
programClassDecl:   K_CLASS K_PROGRAM (COLON IDENTIFIER)?
					LEFT_CURLY_BRACKET programClassMemDecl* RIGHT_CURLY_BRACKET
                    ;
programClassMemDecl:
                    attributeDeclaration
					| mainMethodDecl
                    | methodDeclaration
                    ;
mainMethodDecl:     K_MAIN
                    LEFT_PAREN RIGHT_PAREN blockStatement
                    ;// No prameter in static main

memberDeclaration   :attributeDeclaration
                    | methodDeclaration
					;
//-----------------------------------------------------------------
methodDeclaration:	(K_MAIN | IDENTIFIER | DOLAR_IDENTIFIER)
                    LEFT_PAREN parameterList? RIGHT_PAREN blockStatement
					| constructor
					| destructor
					;// getSomeThing(){...}
constructor:		K_CONSTRUCTOR LEFT_PAREN parameterList? RIGHT_PAREN  blockStatement
					;
destructor:			K_DESTRUCTOR LEFT_PAREN RIGHT_PAREN  blockStatement
					;
parameterList: 	    parameter (SEMI_COLON parameter)*
					;//; a, b, c: Int
parameter:    		identifierList COLON d96Type
					;//a, b, c: String
d96Type:            PRIMITIVE_TYPE | IDENTIFIER | arrayType
                    ;// ID for class type
//----------------------------------------------------------------
attributeDeclaration:
                    (K_VAL | K_VAR)
                    mixedIdentifier (COMMA mixedIdentifier)*
                    COLON d96Type (OP_ASSIGN expression (COMMA expression)*)? SEMI_COLON
                    ;
identifierList: 	IDENTIFIER (COMMA IDENTIFIER)*
					;// My1stCons, My2ndCons
mixedIdentifier:    IDENTIFIER | DOLAR_IDENTIFIER
                    ;
//==================== Program struture end ====================


//==================== Expression start ====================
expressionList: 	expression | expression (COMMA expression)+
					;// 1+2, 1+2, 2*5
//----------------------------------------------------------------
// Index operator
elementExpression:	expression indexOperator
					;
indexOperator:		(LEFT_SQUARE_BRACKET expression RIGHT_SQUARE_BRACKET)+
					;// a[1] or b[1][2] or A[1+2]
//-----------------------------------------------------------------
// All expression
relationalOperator:
					OP_IS_EQUAL_TO
					| OP_NOT_EQUAL_TO
					| OP_LESS_THAN
					| OP_LESS_THAN_EQUAL
					| OP_GREATER_THAN
					| OP_GREATER_THAN_EQUAL
					;

expression:			relationalExpr (OP_STRING_CONCATENATION | OP_TWO_SAME_STRING) relationalExpr
					| relationalExpr
					;// +. ==

relationalExpr:	    andOrExpr relationalOperator andOrExpr
                    | andOrExpr
					;// == != < > <= >=
andOrExpr:		    andOrExpr (OP_LOGICAL_AND | OP_LOGICAL_OR) addSubExpr
					| addSubExpr
					;// && ||
addSubExpr:		    addSubExpr (OP_ADDTION | OP_SUBTRACTION) mulAddMolExpr
					| mulAddMolExpr
					;
mulAddMolExpr:	    mulAddMolExpr (OP_MULTIPLICATION | OP_DIVISION| OP_MODULO) notExpr
					| notExpr
					;
notExpr:			OP_LOGICAL_NOT notExpr | signExpr
					;
signExpr:			(OP_SUBTRACTION | OP_ADDTION) signExpr | indexOperatorExpr
					;
indexOperatorExpr:
					instanceAccess indexOperator
					| instanceAccess
					;
// Member access
instanceAccess:
					instanceAccess DOT IDENTIFIER
					(LEFT_PAREN expressionList? RIGHT_PAREN)?
					| staticAccess
					;
staticAccess:
					staticAccess DOUBLE_COLON DOLAR_IDENTIFIER
					(LEFT_PAREN expressionList? RIGHT_PAREN)?
					| objectCreation
					;
// Object creation
objectCreation:	    K_NEW IDENTIFIER
					LEFT_PAREN expressionList? RIGHT_PAREN
					| atomExpr
					;

atomExpr:			literal
                    | K_NULL
                    | K_SELF
					| IDENTIFIER
					| LEFT_PAREN expression RIGHT_PAREN
					;
//------------------------------------------------------------------------
//==================== Expression end ====================

//==================== Statement start ====================
// Variable and Constant Declaration Statement
varValStatement:	(K_VAL | K_VAR)
                    IDENTIFIER (COMMA IDENTIFIER)*
                    COLON d96Type (OP_ASSIGN expression (COMMA expression)*)? SEMI_COLON
                    ;
// Assign statement
lhs:                instanceAccess DOT IDENTIFIER
                    | instanceAccess DOUBLE_COLON DOLAR_IDENTIFIER
                    | IDENTIFIER
                    | elementExpression
                    ;
assignStatement: 	lhs OP_ASSIGN expression SEMI_COLON
					;
// If statement
// ---------------------------------------------------------------------------
ifStatement:        K_IF LEFT_PAREN expression RIGHT_PAREN blockStatement
                    | K_ELSE_IF LEFT_PAREN expression RIGHT_PAREN blockStatement
                    | K_ELSE blockStatement
                    ;
//-----------------------------------------------------------------------------
// For in statement
//-----------------------------------------------------------------------------
forInStatement:	    K_FOR_EACH
                    LEFT_PAREN
                    IDENTIFIER K_IN expression DOUBLE_DOT expression (K_BY expression)?
                    RIGHT_PAREN
					blockStatement
					;
//-----------------------------------------------------------------------------
// Break statement
breakStatement:	    K_BREAK SEMI_COLON
					;// Break;
// Continue statement
continueStatement:	K_CONTINUE SEMI_COLON
					;// Continue;
// Return statements
returnStatement:    K_RETURN expression? SEMI_COLON
					;
// Method invocation statement
methodInvocationStatement:
                    instanceAccess SEMI_COLON
					;// Shape::$getNumOfShape();
blockStatement:	    LEFT_CURLY_BRACKET
					statement*
					RIGHT_CURLY_BRACKET
					;//The <block statement> includes zero or many statements
statement: 			varValStatement
					| assignStatement
					| ifStatement
					| forInStatement
					| breakStatement
					| continueStatement
					| returnStatement
					| methodInvocationStatement
					| blockStatement
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
K_RETURN:			'Return';
K_NULL: 			'Null';
K_SELF: 			'Self';
K_MAIN:             'main';
K_PROGRAM:          'Program';
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

literal:            INTEGER_LITERAL
                    | INTEGER_LITERAL2
                    | FLOAT_LITERAL
                    | BOOLEAN_LITERAL
                    | STRING_LITERAL
                    | indexedArray;
// 5. Indexed array and Multi-dimensional array
indexedArray:  		K_ARRAY
						LEFT_PAREN(
							(INTEGER_LITERAL (COMMA INTEGER_LITERAL)*)?
							|(INTEGER_LITERAL2 (COMMA INTEGER_LITERAL2)*)
							|(FLOAT_LITERAL (COMMA FLOAT_LITERAL)*)
							|(BOOLEAN_LITERAL (COMMA BOOLEAN_LITERAL)*)
							|(STRING_LITERAL (COMMA STRING_LITERAL)*)
							|((indexedArray) (COMMA indexedArray)*)
						)
						RIGHT_PAREN
						;	// Array() Array(1) Array(1,2,3)
// Primitive type
PRIMITIVE_TYPE: 	'Int'
                    | 'Float'
                    | 'Boolean'
                    | 'String'
                    ;
// 3.3 Identifier, Dolar identifer
IDENTIFIER:			[_a-zA-Z][_a-zA-Z0-9]*;
DOLAR_IDENTIFIER: 	'$'[_a-zA-Z0-9]+;
//==================== 3. Lexical rules end ====================

//==================== 4. Type and Value start ====================
// Array type
// An array type declaration is in the form of: Array[<element_type>, <size>].
arrayType: 		K_ARRAY
						LEFT_SQUARE_BRACKET
							(PRIMITIVE_TYPE | arrayType) COMMA INTEGER_LITERAL2
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
