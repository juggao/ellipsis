grammar SimpleArithmetic;

start: expr EOF;

expr: expr '++' term
    | expr '--' term
    | term;

term: term '*' factor
    | term '/' factor
    | factor;

factor: INT
    | EINT
    | EPINT
    | NINT
    | '(' expr ')';


NINT: '-'? [0-9]+;
INT: [0-9]+;
EINT: '...'? INT;
EPINT: '~~~'? INT;
WS: [ \t\r\n]+ -> skip;
