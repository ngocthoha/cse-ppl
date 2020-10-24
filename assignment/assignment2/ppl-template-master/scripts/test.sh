#!/bin/bash

cd $(dirname $0)
cd ..
mkdir -p log
cd src

if [ "$1" == "all" ]; then
    python3 run.py gen
    python3 run.py test LexerSuite > ../log/1-lexer.txt
    python3 run.py test ParserSuite > ../log/2-parser.txt
    python3 run.py test ASTGenSuite > ../log/3-astgen.txt
elif [ "$1" == "LexerSuite" ]; then
    python3 run.py gen
    python3 run.py test LexerSuite
elif [ "$1" == "ParserSuite" ]; then
    python3 run.py gen
    python3 run.py test ParserSuite
elif [ "$1" == "ASTGenSuite" ]; then
    python3 run.py gen
    python3 run.py test ASTGenSuite
else
    echo "./test.sh all|LexerSuite|ParserSuite|ASTGenSuite"
fi
