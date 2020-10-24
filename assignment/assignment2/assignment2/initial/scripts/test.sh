#!/bin/bash

cd ../$(dirname $0)
mkdir -p log
cd src
mkdir -p test/{solutions,testcases}

echo "START TESTING"
python3 run.py gen
python3 run.py test LexerSuite > ../log/1-lexer.txt
python3 run.py test ParserSuite > ../log/2-parser.txt
echo "DONE"
