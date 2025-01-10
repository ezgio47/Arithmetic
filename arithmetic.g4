grammar arithmetic;

// Parser rules
expr:   term ((PLUS | MINUS) term)* ;
term:   factor ((MUL | DIV) factor)* ;
factor: INT | LPAREN expr RPAREN ;

// Lexer rules
PLUS:   '+' ;
MINUS:  '-' ;
MUL:    '*' ;
DIV:    '/' ;
LPAREN: '(' ;
RPAREN: ')' ;
INT:    [0-9]+ ;
WS:     [ \t\r\n]+ -> skip ;





