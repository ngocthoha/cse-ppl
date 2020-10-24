#!/bin/bash

cd ../$(dirname $0)

echo "INPUT:"
cat "src/test/testcases/$1.txt"
echo
echo

echo "OUTPUT:"
cat "src/test/solutions/$1.txt"
echo
