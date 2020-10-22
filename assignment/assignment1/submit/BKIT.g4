//1814196
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
//===== PARSER STRUCTURE =====//
program  :variableStatement* funcDeclaration* EOF;
funcDeclaration: FUNCTION COLON Identifier (PARAMETER COLON paraList)? funcBody;
paraList: parameters (COMMA parameters)*;
parameters: Identifier (LSB IntegerConstant RSB)*;
funcBody: BODY COLON statementList ENDBODY DOT;

//===== EXPRESSIONS =====//
expression
    :logicalOrAndExpression relationalOperator logicalOrAndExpression
    |logicalOrAndExpression
    ;
logicalOrAndExpression
    :logicalOrAndExpression logicalOrAndOperator additiveExpression
    |additiveExpression
    ;
additiveExpression
    :additiveExpression additiveOperator multiplicativeExpression
    |multiplicativeExpression
    ;
multiplicativeExpression
    :multiplicativeExpression multiplicativeOperator logicalNotExpression
    |logicalNotExpression
    ;
logicalNotExpression
    :logicalNotOperator logicalNotExpression
    |signExpression
    ;
signExpression
    :signOperator signExpression
    |indexExpression
    ;
indexExpression
    :indexExpression indexOperator
    |funcExpression
    ;
funcExpression
    :primaryExpression LSB expression RSB
    |primaryExpression
    ;
primaryExpression
    :Identifier
    |literals
    |functionCall
    |LB expression RB
    ;
additiveOperator
    :SUB | SUBF | ADD | ADDF
    ;
multiplicativeOperator
    :MUL | MULF | DIV | DIVF | MOD
    ;
logicalOrAndOperator
    :OR | AND
    ;
logicalNotOperator
    :NOT
    ;
relationalOperator
    :EQ | NE | NEF | LE | LEF | LT | LTF | GE | GEF | GT | GTF
    ;
signOperator
    :SUB | SUBF
    ;
assignmentOperator
    :ASSIGN
    ;
indexOperator
    :LSB expression RSB
    ;
functionCall
    :Identifier LB argumentList? RB
    ;
argumentList
    :argumentList COMMA expression
    |expression
    ;
//===== STATEMENTS =====//
statement
    :assignmentStatement
    |iterationStatement
    |jumpStatement
    |callStatement
    |returnStatement
    |ifStatement
    ;
statementList
    : variableStatement* statement*;

//ExpressionStatement
expressionStatement
    :expression? SEMI
    ;
//Variable Statement
variableStatement: VAR COLON varList SEMI; //Var: variable-list;
varList: varDeclaration (COMMA varDeclaration)*; //Var: c, d = 6, n[2], b[2] = {1, 2};
varDeclaration: Identifier (LSB IntegerConstant RSB)* (ASSIGN literals)?;
//AssignmentStatement
assignmentStatement: assignDeclaration ASSIGN expression SEMI;
assignDeclaration: (Identifier | functionCall) indexOperator*;
//If Statement
ifStatement
    :IF expression THEN statementList (ELSEIF expression THEN statementList)*? (ELSE statementList)?
     ENDIF DOT
    ;
iterationStatement
    :forStatement
    |whileStatement
    |doWhileStatement
    ;
//For Statement
forStatement
    :FOR LB forCondition RB DO
        statementList
     ENDFOR DOT
    ;
forCondition
    :forDeclaration COMMA conditionExpr? COMMA updateExpr?
    ;
forDeclaration: Identifier ASSIGN expression;
conditionExpr: expression;
updateExpr: expression;
//While Statement
whileStatement
    :WHILE expression DO statementList ENDWHILE DOT
    ;

//Do-while Statement
doWhileStatement
    :DO statementList WHILE expression ENDDO DOT
    ;
//JumpStatement
jumpStatement
    :breakStatement
    |continueStatement
    ;
//Break Statement
breakStatement
    :BREAK SEMI
    ;
//Continue Statement
continueStatement
    :CONTINUE SEMI
    ;
//Call Statement
callStatement
    :functionCall SEMI
    ;
//Return Statement
returnStatement
    :RETURN expression? SEMI
    ;
//===== LEXICAL STRUCTURE =====//
//Identifier
Identifier: Lowercase (Letters | UNDERSCORE | Digit)*;
//Fragment
fragment Lowercase: [a-z];
fragment Uppercase: [A-Z];
fragment Digit: [0-9];
fragment Letters: Lowercase | Uppercase;
fragment DecimalConstant: '0' | NonzeroDigit Digit*;
fragment OctalConstant: OctalPrefix NonzeroOctalDigit OctalDigit*;
fragment HexadecimalContant: HexPrefix NonzeroHexDigit HexDigit*;
fragment NonzeroDigit: [1-9];
fragment OctalDigit: [0-7];
fragment NonzeroOctalDigit: [1-7];
fragment OctalPrefix: '0' [oO];
fragment HexPrefix: '0' [xX];
fragment HexDigit: [0-9A-F];
fragment NonzeroHexDigit: [1-9A-F];
fragment Exponent: [eE] (SUB | ADD)? Digit+;

fragment Character: ~[\b\f\r\n\t'"\\] | EscapeSequence;
fragment EscapeSequence: '\\' [bfrnt'\\] | '\'' '"';
fragment EscapeIllegal: '\\' ~[bfrnt'\\] | '\'' ~["];

//Keywords
BODY: 'Body';
ELSE: 'Else';
ENDFOR: 'EndFor';
IF: 'If';
VAR: 'Var';
ENDDO: 'EndDo';
BREAK: 'Break';
ELSEIF: 'ElseIf';
ENDWHILE: 'EndWhile';
PARAMETER: 'Parameter';
WHILE: 'While';
CONTINUE: 'Continue';
ENDBODY: 'EndBody';
FOR: 'For';
RETURN: 'Return';
TRUE: 'True';
DO: 'Do';
ENDIF: 'EndIf';
FUNCTION: 'Function';
THEN: 'Then';
FALSE: 'False';

//Arithmetic Operators
ADD :'+';
SUB :'-';
MUL :'*';
MOD :'%';
DIV :'\\';
SUBF :'-.';
DIVF :'\\.';
ADDF :'+.';
MULF :'*.';

//Boolean Operators
NOT :'!';
OR :'||';
AND :'&&';

//Relational Operators
EQ :'==';
LE :'<=';
GTF :'>.';
NE :'!=';
GE :'>=';
LEF :'<=.';
LT :'<';
NEF :'=/=';
GEF :'>=.';
GT :'>';
LTF :'<.';

//Separators
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
COLON: ':';
DOT: '.';
fragment UNDERSCORE: '_';
COMMA: ',';
SEMI: ';';
LP: '{';
RP: '}';
ASSIGN: '=';

//Literals
literals
    :IntegerConstant
    |FloatingConstant
    |String
    |boolean
    |array
    ;
IntegerConstant
    :DecimalConstant
    |OctalConstant
    |HexadecimalContant
    ;
FloatingConstant
    : Digit+ DOT Digit+ Exponent
    | Digit+ DOT (Digit | Exponent)*
    | Digit+ Exponent
    ;
String: '"' Character* '"' {
    temp = str(self.text)
    self.text = temp[1:-1]
};
boolean: TRUE | FALSE;
array: LP literals (COMMA literals)* RP;
COMMENT: '**' .*? '**' -> skip;
WS : [ \t\f\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNTERMINATED_COMMENT
    : '**' .*?
    ;
UNCLOSE_STRING
    : '"' Character* ([\n] | EOF)
    {
        esc = ['\n']
        temp = str(self.text)
        if temp[-1] in esc:
            self.text = temp[1:-1]
        else :
            self.text = temp[1:]
    }
    ;
ILLEGAL_ESCAPE
    :'"' Character* EscapeIllegal 
    {
        temp = str(self.text)
        raise IllegalEscape(temp[1:])
    }
    ;
ERROR_CHAR
    :.
    ;