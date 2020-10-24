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
else
    echo "./gen.sh LexerSuite|ParserSuite"
fi
