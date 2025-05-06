#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Run pattern is: $0 <path_to_your_file> <word>"
    exit 1
fi

file=$1
word=$2

if [ ! -f "$file" ]; then
    echo "Attention! File '$file' wasn't found. Check the path or create new file and try again!"
    exit 1
fi

grep --color=always "$word" "$file"
