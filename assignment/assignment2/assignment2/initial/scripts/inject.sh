#!/bin/bash

cd $(dirname $0)
cd ../src
mkdir -p test/{solutions,testcases}

if [ "$2" == "fill" ]; then
    export PPL_OPTION=f1ll
    export PPL_COUNT="$3"
fi

if [ "$1" == "LexerSuite" ]; then
    export PPL_MAGIC_STRING=l3x3r5u173
    PPL_TARGET=LexerSuite
elif [ "$1" == "ParserSuite" ]; then
    export PPL_MAGIC_STRING=p4r53r5u173
    PPL_TARGET=ParserSuite
else
    echo "./inject.sh LexerSuite|ParserSuite [fill]"
    exit -1
fi

python3 run.py gen
python3 run.py test "${PPL_TARGET}"

if [ "$?" != 0 ]; then
    echo "Failed."
    exit -1
fi
echo "Success"
