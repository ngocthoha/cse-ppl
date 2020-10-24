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
//Variable Statement
variableStatement: VAR COLON varList SEMI;
varList: varDeclaration (COMMA varDeclaration)*;
varDeclaration: Identifier (LSB IntegerConstant RSB)* (ASSIGN literals)?;

//Function Declaraton
funcDeclaration: FUNCTION COLON Identifier (PARAMETER COLON paraList)? funcBody;
paraList: parameters (COMMA parameters)*;
parameters: Identifier (LSB IntegerConstant RSB)*;
funcBody: BODY COLON statementList ENDBODY DOT;

//===== EXPRESSIONS =====//
expression
    :logicalOrAndExpression relationalOperator logicalOrAndExpression
    |logicalOrAndExpression
    ;
relationalOperator
    :EQ | NE | NEF | LE | LEF | LT | LTF | GE | GEF | GT | GTF
    ;
logicalOrAndExpression
    :logicalOrAndExpression logicalOrAndOperator additiveExpression
    |additiveExpression
    ;
logicalOrAndOperator
    :OR | AND
    ;
additiveExpression
    :additiveExpression additiveOperator multiplicativeExpression
    |multiplicativeExpression
    ;
additiveOperator
    :SUB | SUBF | ADD | ADDF
    ;
multiplicativeExpression
    :multiplicativeExpression multiplicativeOperator logicalNotExpression
    |logicalNotExpression
    ;
multiplicativeOperator
    :MUL | MULF | DIV | DIVF | MOD
    ;
logicalNotExpression
    :NOT logicalNotExpression
    |signExpression
    ;
signExpression
    :signOperator signExpression
    |indexExpression
    ;
signOperator
    :SUB | SUBF
    ;
indexExpression
    :indexExpression indexOperator
    |funcExpression
    ;
indexOperator
    :LSB expression RSB
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
literals
    :IntegerConstant
    |FloatingConstant
    |String
    |boolean
    |array
    ;
boolean
    :TRUE | FALSE
    ;
array
    :LP literals (COMMA literals)* RP
    ;
assignmentOperator
    :ASSIGN
    ;
functionCall
    :Identifier LB argumentList? RB
    ;
argumentList
    :argumentList COMMA expression
    |expression
    ;
//===== STATEMENTS =====//
statementList
    :variableStatement* statement*
    ;
statement
    :assignmentStatement
    |iterationStatement
    |jumpStatement
    |callStatement
    |returnStatement
    |ifStatement
    ;
//AssignmentStatement
assignmentStatement: assignDeclaration ASSIGN expression SEMI;
assignDeclaration: (Identifier | functionCall) indexOperator*;
//If Statement
ifStatement
    :IF expression THEN statementList (ELSEIF expression THEN statementList)*? (ELSE statementList)?
     ENDIF DOT
    ;
//IterationStatement
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
UNDERSCORE: '_';
COMMA: ',';
SEMI: ';';
LP: '{';
RP: '}';
ASSIGN: '=';

//Literals
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
String
    : '"' Character* '"' 
    {
        temp = self.text
        self.text = temp[1:-1]
    }
    ;
COMMENT: '**' .*? '**' -> skip;
WS: [ \t\f\r\n]+ -> skip; // skip spaces, tabs, newlines

UNTERMINATED_COMMENT
    :'**' .*?
    ;
UNCLOSE_STRING
    :'"' Character* ([\n] | EOF)
    {
        esc = ['\n']
        temp = self.text
        if temp[-1] in esc:
            self.text = temp[1:-1]
        else :
            self.text = temp[1:]
    }
    ;
ILLEGAL_ESCAPE
    :'"' Character* EscapeIllegal 
    {
        temp = self.text
        raise IllegalEscape(temp[1:])
    }
    ;
ERROR_CHAR
    :.
    ;