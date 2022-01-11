/* Trieu Minh Sang - 1852717 */

grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

// Program
program  : globdeclpart funcdeclspart EOF ;

globdeclpart    :       vardecls globdeclpart 
                |       
                ;

funcdeclspart   :       funcdecls funcdeclspart
                |
                ;
        
// Global variable declaration
vardecls: VAR COLON varlist SEMI ;

varlist :   variableinit tailvar
        |   variableinit
        ;

tailvar :   COMMA variableinit tailvar
        |
        ;

variableinit    :       ID
                |       ID ASSIGN literals
                |       ID dimlist
                |       ID dimlist ASSIGN literals
                ;

literals        :       INTLIT
                |       FLOATLIT
                |       FALSE
                |       TRUE 
                |       STRINGLIT
                |       arraydecls
                ;

arraydecls      :       LB arraylit RB ;

arraylit        :       literals arraylit_
                |       
                ;

arraylit_       :       COMMA literals arraylit_
                |
                ;

dimlist :   dim taildim
        |   dim
        ;

taildim :   dim taildim
        |  
        ;

dim: LA INTLIT RA ;

// Function declaration
funcdecls       :       FUNCTION COLON ID BODY COLON (statement)* ENDBODY DOT 
                |       FUNCTION COLON ID PARAMETER COLON parameterlist BODY COLON (statement)* ENDBODY DOT
                ;

parameterlist   :       parameter parameterlist_
                |       parameter
                ;

parameterlist_  :       COMMA parameter parameterlist_
                |       
                ;

parameter       :       ID
                |       ID dimlist
                ;

// Expression
relop   :       LESS
        |       LESSFLOAT
        |       GREATER
        |       GREATERFLOAT
        |       LESSEQUAL
        |       LESSEQUALFLOAT
        |       GREATEREQUAL
        |       GREATEREQUALFLOAT
        |       EQUAL
        |       EQUALFLOAT
        |       NOTEQUAL
        ;       

expr    :       expr1 relop expr1 | expr1 ;

expr1   :       expr1 (AND | OR) expr2 | expr2 ;

expr2   :       expr2 (ADD | ADDFLOAT | SUB | SUBFLOAT) expr3 | expr3 ;

expr3   :       expr3 (MUL | MULFLOAT | DIV | DIVFLOAT | MOD) expr4 | expr4 ;

expr4   :       NOT expr4 | expr5 ;

expr5   :       (SUB | SUBFLOAT) expr5 | expr6 ;

expr6   :       expr6 (LA expr RA)+ | expr7 ;

expr7   :       literals 
        |       ID
        |       LP expr RP
        |       functioncall
        ;

functioncall: ID LP argumentslist RP;

argumentslist   :       expr argumentslist_
                |
                ;

argumentslist_  :       COMMA expr argumentslist_
                |
                ;

// Statement
statement       :       vardecls
                |       assignmentstmt
                |       ifstmt
                |       forstmt
                |       whilestmt
                |       dowhilestmt
                |       breakstmt
                |       continuestmt
                |       callstmt
                |       returnstmt
                ;

// Assignment statement
assignmentstmt  :       expr ASSIGN expr SEMI ;

// If statement
ifstmt: IF expr THEN if_statement (ELSEIF expr THEN elif_statement)* (ELSE else_statement)? ENDIF DOT ;

if_statement: (statement)*;

elif_statement: (statement)*;

else_statement: (statement)*;

// For statement
forstmt: FOR LP ID ASSIGN expr COMMA expr COMMA expr RP DO (statement)* ENDFOR DOT ;       

// While statement
whilestmt: WHILE expr DO (statement)* ENDWHILE DOT ;

// Do-While statement
dowhilestmt: DO (statement)* WHILE expr ENDDO DOT ;

// Break statement
breakstmt: BREAK SEMI ;

// Continue statement
continuestmt: CONTINUE SEMI ;

// Call statement
callstmt: ID LP argumentslist RP SEMI ;

// Return statement
returnstmt: RETURN expr? SEMI ;

//------------------
// Tokens
//------------------
// Key words
VAR: 'Var' ;
BODY: 'Body' ;
ELSE: 'Else' ;
ENDFOR: 'EndFor' ;
IF: 'If' ;
ENDDO: 'EndDo' ;
BREAK: 'Break' ;
ELSEIF: 'ElseIf' ;
ENDWHILE: 'EndWhile' ;
PARAMETER: 'Parameter' ;
WHILE: 'While' ;
CONTINUE: 'Continue' ;
ENDBODY: 'EndBody' ;
FOR: 'For' ;
RETURN: 'Return' ;
TRUE: 'True' ;
DO: 'Do' ;
ENDIF: 'EndIf' ;
FUNCTION: 'Function' ;
THEN: 'Then' ;
FALSE: 'False' ;

// Skip
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
COMMENT: '**' .*? '**' -> skip ; // skip comments

// Operators
ASSIGN: '=' ;
ADD: '+' ;
ADDFLOAT: '+.' ;
SUB: '-' ;
SUBFLOAT: '-.';
MUL: '*' ;
MULFLOAT: '*.' ;
DIV: '\\' ;
DIVFLOAT: '\\.' ;
MOD: '%' ;
NOT: '!' ;
AND: '&&' ;
OR: '||' ;
EQUAL: '==' ;
NOTEQUAL: '!=' ;
LESS: '<' ;
GREATER: '>' ;
LESSEQUAL: '<=' ;
GREATEREQUAL: '>=' ;
EQUALFLOAT: '=/=' ;
LESSFLOAT: '<.' ;
GREATERFLOAT: '>.' ;
LESSEQUALFLOAT: '<=.' ;
GREATEREQUALFLOAT: '>=.' ;

fragment ESCAPE :       '\\b'
                |       '\\f'
                |       '\\r'
                |       '\\n'
                |       '\\t'
                |       '\\\''
                |       '\\\\'
                ;

// Separators
LP: '(' ;
RP: ')' ;
LA: '[' ;
RA: ']' ;
COLON: ':' ;
DOT: '.' ;
COMMA: ',' ;
SEMI: ';' ;
LB: '{' ;
RB: '}' ;

// Identifiers
ID: [a-z] ([a-zA-Z] | [0-9] | '_')* ;

// Literals
INTLIT  :   [1-9] [0-9]*
        |   ('0x' | '0X') [1-9A-F] [0-9A-F]*
        |   ('0o' | '0O') [1-7] [0-7]*
        |   '0'
        ;

FLOATLIT    :   [0-9]+ DOT [0-9]* ([eE] [+-]? [0-9]+)?
            |   [0-9]+ (DOT [0-9]*)? [eE] [+-]? [0-9]+
            ;

STRINGLIT: '"' STRINGTYPE*? '"' {
        y = str(self.text)
        self.text = y[1:-1]
};

fragment STRINGTYPE     :       ESCAPE
                        |       '\'' '"'
                        |        ~('\n' | '\'' | '"' | '\\')     
                        ;   

ILLEGAL_ESCAPE: '"' STRINGTYPE* '\\' ~('b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\') {
    self.text = str(self.text)[1:]
};
UNCLOSE_STRING: '"' (~'"' | '\'"')* (EOF | '\n') {
    self.text = str(self.text)[1:]
};
UNTERMINATED_COMMENT: '**' (~'*')* ('*' (~'*')+)* '*'? EOF ;
ERROR_CHAR: .;
