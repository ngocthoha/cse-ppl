#!/bin/bash

cd $(dirname $0)
cd ../src

cp main/bkit/parser/BKIT.g4 ../submit
cp main/bkit/astgen/ASTGeneration.py ../submit

cp test/{Lexer,Parser,ASTGen}Suite.py ../submit
