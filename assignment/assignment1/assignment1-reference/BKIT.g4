/* Le Trung Hieu _ 1852365 */

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

// Tokens Set
// Keywords
MAIN : 'main' ;
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
ESCAPE : '\\' ('b'
       | 'f'
       | 'r'
       | 'n'
       | 't'
       | '\''
       | '\\')
       ;
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


// Identifier
ID : [a-z] (LETTER | DIGIT | '_')* ;

// Literal
INT : [1-9] DIGIT* 
       | ('0x' | '0X') [1-9A-F] HEX*
       | ('0o' | '0O') [1-7] OCT*
       | '0' 
       ;
FLOAT : DIGIT+ DOT DIGIT* ([eE][+-]? DIGIT+)?
         | DIGIT+ DOT? DIGIT* [eE][+-]? DIGIT+
         ;
BOOL : 'True' | 'False' ;

fragment CHAR : ~( '\n' | '\'' | '\\' | '"' ) | ESCAPE | '\'' '"';


STRING: '"' CHAR*? '"' {
    y = str(self.text)
    self.text = y[1:-1]
};


// Array
ARRAY : LB INT (COMMA INT)* RB 
      | LB FLOAT (COMMA FLOAT)* RB 
      | LB BOOL (COMMA BOOL)* RB 
      | LB STRING (COMMA STRING)* RB 
      | LB ARRAY (COMMA ARRAY)* LB
      ;


litlist : literal (COMMA literal)* ;
literal : INT
        | FLOAT  
        | BOOL
        | STRING
        | ARRAY
        ;

/*--------------------- Main program structure--------------------------- */
program  : globdecs funcdecs EOF ;
globdecs : vardec globdecs
         | vardec
         | 
         ;
funcdecs : funcdeclist mainfunc funcdeclist ;
funcdeclist : funcdec funcdeclist
            | 
            ;

/*-------------------------Statement structure--------------------------- */


// Variable declaration statement
vardec : VAR COLON varlist EQ initlist SEMI 
       | VAR COLON varlist SEMI
       ;
varlist : variable varlist_ ;
varlist_ : COMMA variable varlist_
         |
         ;
// Variable definition
variable : ID dim ;
dim : LS INT RS dim
    | 
    ;
initlist : init initlist_;
initlist_ : COMMA init initlist_
          | 
          ;
init : expr ;



// Assignment statement
assign : ID dim_ EQ expr SEMI;
dim_ : LS expr RS dim_
     | 
     ;

// If statement
ifstmt : IF cond_block elif_block else_block ENDIF DOT;
cond_block : expr THEN stmtlist ;
elif_block : ELSEIF cond_block elif_block
          | 
          ;
else_block : ELSE stmtlist
          | 
          ;

// For statement
forstmt : FOR LP iter_block RP DO stmtlist ENDFOR DOT ;
iter_block : iter_init COMMA iter_cond COMMA iter_update ;
iter_init : ID EQ expr ;
iter_cond : expr ;
iter_update : expr ;

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
returnstmt : RETURN expr SEMI
           | RETURN SEMI
           ;

// Statment list always begins with variable declarations
stmtlist : vardeclist stamentlist;
vardeclist : vardec vardeclist
           | 
           ;
stamentlist : stmt stamentlist
         | 
         ;
stmt : assign 
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
funcdec : FUNCTION COLON ID paramdec bodydec
        | FUNCTION COLON ID bodydec 
        ;
paramdec : PARAMETER COLON varlist ;

bodydec : BODY COLON stmtlist ENDBODY DOT ;

// Main function declaration
mainfunc : FUNCTION COLON MAIN paramdec bodydec
         | FUNCTION COLON MAIN bodydec 
         |
         ;

// Function call
call : ID LP exprlist RP
     | ID LP RP ;

// Expression
expr : relexpr RELOP relexpr | relexpr ;
relexpr : <assoc=right> ('-' | '-.') relexpr
     | <assoc=right> '!' relexpr
     | relexpr ('*' | '*.' | '\\' | '\\.' | '%') relexpr
     | relexpr ('+' | '+.' | '-' | '-.') relexpr
     | relexpr ('&&' | '||') relexpr
     | operand
     ;
operand : LP expr RP
        | call
        | ID dim_
        | ID
        | literal
        ;

// List of expressions
exprlist : expr exprlist_;
exprlist_ : COMMA expr exprlist_ 
          |
          ;
ILLEGAL_ESCAPE: '"' CHAR* '\\' ~('b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\') {
    self.text = str(self.text)[1:]
};
UNCLOSE_STRING: '"' (~'"' | '\'"')* ( '\n' | EOF ){
    self.text = str(self.text)[1:]
};
UNTERMINATED_COMMENT: '**' (~'*')* '*'? EOF;
ERROR_CHAR: .;
