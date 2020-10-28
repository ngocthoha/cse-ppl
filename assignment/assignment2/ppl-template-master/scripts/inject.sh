#!/bin/bash

cd $(dirname $0)
cd ../src

if [ "$2" == "fill" ]; then
    export PPL_OPTION=f1ll
    export PPL_COUNT="$3"
fi

if [ "$1" == "LexerSuite" ]; then
    export PPL_MAGIC_STRING=l3x3r5u173
    PPL_TARGET=LexerSuite
    python run.py gen
    python run.py test "$1"
elif [ "$1" == "ParserSuite" ]; then
    export PPL_MAGIC_STRING=p4r53r5u173
    PPL_TARGET=ParserSuite
    python run.py gen
    python run.py test "$1"
elif [ "$1" == "ASTGenSuite" ]; then
    export PPL_MAGIC_STRING=45763n5u173
    python run.py gen
    python run.py test "$1"
    yapf -i test/ASTGenSuite.py --style='{column_limit: 100}'
elif [ "$1" == "CheckSuite" ]; then
    export PPL_MAGIC_STRING=ch3ck5u173
    python run.py gen
    python run.py test "$1"
else
    echo "./inject.sh LexerSuite|ParserSuite|ASTGenSuite|CheckSuite [fill]"
    exit -1
fi


if [ "$?" != 0 ]; then
    echo "Failed."
    exit -1
fi
echo "Success"
