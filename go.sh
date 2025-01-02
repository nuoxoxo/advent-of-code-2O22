#!/bin/bash

if [ $1 -gt 0 ] && [ $1 -lt 10 ]; then
    #FILENAME="0$1.0"
    FILENAME="$1.0"
elif [ $1 -ge 10 ] && [ $1 -lt 26 ]; then
    FILENAME="$1.0"
else
    echo "arg no good"
    return
fi

URL="https://adventofcode.com/2022/day/$1/input"

if [[ -z "$AOC_SESSION" ]]; then
    if [[ -f .env && -s .env ]]; then
        source .env
    else
        read -p "Enter aoc session: " TEMP
        export "AOC_SESSION=${TEMP}"
    fi
fi

curl -H "Cookie: session=$AOC_SESSION" -o ${FILENAME} ${URL}
