/* Nguyen Tien Thanh _ 1852740 */

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
        return result
}

options{
	language=Python3;
}

// Tokens Set
// Keywords
BODY : 'Body' ;
BREAK : 'Break' ;
CONTINUE : 'Continue' ;
DO : 'Do' ;
ELSE : 'Else' ;
ELSEIF : 'ElseIf' ;
ENDBODY : 'EndBody' ;
ENDIF : 'EndIf' ;
ENDFOR : 'EndFor' ;
ENDWHILE : 'EndWhile' ;
FOR : 'For' ;
FUNCTION : 'Function' ;
IF : 'If' ;
PARAMETER : 'Parameter' ;
RETURN : 'Return' ;
THEN : 'Then' ;
VAR : 'Var' ;
WHILE : 'While' ;
ENDDO : 'EndDo' ;


WS : [ \f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines
CMT : '**' .*? '**' -> skip ; // skip comment

EQ : '=' ;
LP : '(' ;
RP : ')' ;
LS : '[' ;
RS : ']' ;
LB : '{' ;
RB : '}' ;
COLON : ':' ;
DOT : '.' ;
COMMA: ',' ;
SEMI: ';' ;
RELOP : '=='
      | '!='
      | '<'
      | '>'
      | '<='
      | '>='
      | '=/='
      | '<.'
      | '>.'
      | '<=.'
      | '>=.'
      ;

fragment LETTER : [a-zA-Z] ;
fragment DIGIT : [0-9] ;
fragment HEX : [0-9A-F] ;
fragment OCT : [0-7] ;
fragment CHAR : ~[\n'"\\] | '\\'[bfrnt'\\] | '\'' '"' ;

// Identifier
ID : [a-z] (LETTER | DIGIT | '_')* ;

// Literal
INTLIT : [1-9] DIGIT* 
       | ('0x' | '0X') [1-9A-F] HEX*
       | ('0o' | '0O') [1-7] OCT*
       | '0'
       ;
FLOATLIT : DIGIT+ DOT DIGIT* ([eE][+-]? DIGIT+)?
         | DIGIT+ DOT? DIGIT* [eE][+-]? DIGIT+
         ;
BOOLLIT : 'True' | 'False' ;

STRINGLIT : '"' CHAR*? '"'
        { 
            self.text = self.text[1:-1] 
        } 
        ;

arraylit : LB litlist? RB ;
litlist : literal (COMMA literal)* ;
literal : INTLIT
        | FLOATLIT
        | BOOLLIT
        | STRINGLIT
        | arraylit
        ;

/*--------------------- Main program structure--------------------------- */
program  : vardecl* funcdecl* EOF ;

/*-------------------------Statement structure--------------------------- */
// Variable declaration statement
vardecl : VAR COLON varlist SEMI ;
varlist : variable (COMMA variable)* ;
// Variable definition
variable : ID dim* (EQ init)? ;
dim : LS INTLIT RS ;
init : literal ;

// Assignment statement
assignstmt : expr EQ expr SEMI ;

// If statement
ifstmt : IF condblock (ELSEIF condblock)* (ELSE stmtlist)? ENDIF DOT;
condblock : expr THEN stmtlist ;

// For statement
forstmt : FOR LP iterblock RP DO stmtlist ENDFOR DOT ;
iterblock : iterinit COMMA itercond COMMA iterupdate ;
iterinit : ID EQ expr ;
itercond : expr ;
iterupdate : expr ;

// While statement
whilestmt : WHILE expr DO stmtlist ENDWHILE DOT ;

// Do-while statement
dowhilestmt : DO stmtlist WHILE expr ENDDO DOT ;

// Break statement
breakstmt : BREAK SEMI ;

// Continue statement
continuestmt : CONTINUE SEMI ;

// Function call statement
callstmt : call SEMI ;

// Return statement
returnstmt : RETURN expr? SEMI ;

// Statment list always begins with variable declarations
stmtlist : vardecl* stmt* ;
stmt : assignstmt
     | ifstmt 
     | forstmt
     | whilestmt
     | dowhilestmt
     | breakstmt
     | continuestmt
     | callstmt
     | returnstmt
     ;
/*----------------------------------------------------------------------- */

// Function declaration
funcdecl : FUNCTION COLON ID paramdecl? bodydecl ;
paramdecl : PARAMETER COLON varlist ;
bodydecl : BODY COLON stmtlist ENDBODY DOT ;

// Function call
call : ID LP exprlist? RP ;

// Expression
expr : relexpr RELOP relexpr | relexpr ;
relexpr : relexpr (LS expr RS)+
        | <assoc=right> ('-' | '-.')  relexpr
        | <assoc=right> '!' relexpr
        | relexpr ('*' | '*.' | '\\' | '\\.' | '%') relexpr
        | relexpr ('+' | '+.' | '-' | '-.') relexpr
        | relexpr ('&&' | '||') relexpr
        | operand
        ;
operand : LP expr RP
        | call
        | ID
        | literal
        ;
// List of expressions
exprlist : expr (COMMA expr)* ;


UNCLOSE_STRING: '"' (~'"')* ( '\n' | EOF )
        { 
            self.text = self.text[1:]
        } 
        ;
ILLEGAL_ESCAPE: '"' CHAR* ( '\\' ~[bfrnt'\\] | '\'' ~'"' )
        { 
            self.text = self.text[1:]
        }
        ;
UNTERMINATED_COMMENT: '**' (~'*' | '*' ~'*')* EOF ;
ERROR_CHAR: . ;