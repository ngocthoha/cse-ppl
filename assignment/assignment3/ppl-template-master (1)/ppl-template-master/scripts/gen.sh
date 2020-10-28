#!/bin/bash

cd $(dirname $0)
cd ../src

if [ "$1" == "LexerSuite" ]; then
    {
        echo "import unittest"
        echo "from TestUtils import TestLexer"
        echo
        echo
        echo "class LexerSuite(unittest.TestCase):"
    } > test/LexerSuite.template.py

    {
        for i in $(seq 101 200); do
            echo
            echo "    def test_${i}(self):"
            echo "        input = r\"\"\"  \"\"\""
            echo "        expect = r\"\"\"<EOF>\"\"\""
            echo "        self.assertTrue(TestLexer.checkLexeme(input, expect, ${i}))"
        done
    } >> test/LexerSuite.template.py

elif [ "$1" == "ParserSuite" ]; then
    {
        echo "import unittest"
        echo "from TestUtils import TestParser"
        echo
        echo
        echo "class ParserSuite(unittest.TestCase):"
    } > test/ParserSuite.template.py

    {
        for i in $(seq 201 300); do
            echo
            echo "    def test_${i}(self):"
            echo "        input = r\"\"\""
            echo
            echo "\"\"\""
            echo "        expect = r\"\"\"successful\"\"\""
            echo "        self.assertTrue(TestParser.checkParser(input, expect, ${i}))"
        done
    } >> test/ParserSuite.template.py

elif [ "$1" == "ASTGenSuite" ]; then
    {
        echo "import unittest"
        echo "from TestUtils import TestAST"
        echo "from AST import *"
        echo
        echo
        echo "class ASTGenSuite(unittest.TestCase):"
    } > test/ASTGenSuite.template.py

    {
        for i in $(seq 301 400); do
            echo
            echo "    def test_${i}(self):"
            echo "        input = r\"\"\""
            echo
            echo "\"\"\""
            echo "        expect = Program([])"
            echo "        self.assertTrue(TestAST.checkASTGen(input, expect, ${i}))"
        done
    } >> test/ASTGenSuite.template.py

elif [ "$1" == "CheckSuite" ]; then
    {
        echo "import unittest"
        echo "from TestUtils import TestChecker"
        echo
        echo
        echo "class CheckSuite(unittest.TestCase):"
    } > test/CheckSuite.template.py

    {
        for i in $(seq 401 500); do
            echo
            echo "    def test_${i}(self):"
            echo "        input = r\"\"\""
            echo
            echo "\"\"\""
            echo "        expect = \"\""
            echo "        self.assertTrue(TestChecker.test(input, expect, ${i}))"
        done
    } >> test/CheckSuite.template.py

else
    echo "./gen.sh LexerSuite|ParserSuite|ASTGenSuite|CheckSuite"
fi
