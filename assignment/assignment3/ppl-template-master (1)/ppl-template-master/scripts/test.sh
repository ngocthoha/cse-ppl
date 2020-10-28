#!/bin/bash

cd $(dirname $0)
cd ..
mkdir -p log
cd src

if [ "$1" == "all" ]; then
    python run.py gen
    python run.py test LexerSuite > ../log/1-lexer.txt
    python run.py test ParserSuite > ../log/2-parser.txt
    python run.py test ASTGenSuite > ../log/3-astgen.txt
elif [ "$1" == "LexerSuite" ]; then
    python run.py gen
    python run.py test $1
elif [ "$1" == "ParserSuite" ]; then
    python run.py gen
    python run.py test $1
elif [ "$1" == "ASTGenSuite" ]; then
    python run.py gen
    python run.py test $1
elif [ "$1" == "CheckSuite" ]; then
    python3 run.py gen
    python3 run.py test $1
else
    echo "./test.sh all|LexerSuite|ParserSuite|ASTGenSuite|CheckSuite"
fi
