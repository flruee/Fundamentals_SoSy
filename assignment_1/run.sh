#!/bin/bash

FOLDER=results


if [ -d "$FOLDER" ]; then #check if file exists
    echo "$FOLDER exists."
    rm $FOLDER/*
fi

counter=10 
while [ "$counter" -gt 0 ]; do
    python main.py 
    counter=$(( counter - 1 ))
    #python .test/plot.py
done