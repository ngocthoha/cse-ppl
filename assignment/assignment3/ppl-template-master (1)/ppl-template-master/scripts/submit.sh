#!/bin/bash

cd $(dirname $0)
cd ../src

cp main/bkit/parser/BKIT.g4 ../submit
cp main/bkit/astgen/ASTGeneration.py ../submit
cp main/bkit/checker/StaticCheck.py ../submit

cp test/{Lexer,Parser,ASTGen,Check}Suite.py ../submit
