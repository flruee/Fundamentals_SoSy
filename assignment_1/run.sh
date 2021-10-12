#!/bin/bash

FOLDER=results


if [ -d "$FOLDER" ]; then #check if file exists
    echo "$FOLDER exists." #delete all previous results in folder
    rm $FOLDER/*
fi

counter=10 
while [ "$counter" -gt 0 ]; do
    python main.py -s pickle -m store test_files/1mb.txt #this is a test call
    counter=$(( counter - 1 ))
    #python .test/plot.py
done

# all txt files in result folder will be plotted
# !!! it will work when times will be written in results/*txt files !!!
# TODO: change file path ... 
python test/export_plots.py