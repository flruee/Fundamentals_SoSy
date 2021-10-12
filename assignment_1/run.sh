#!/bin/bash

FOLDER=results


if [ -d "$FOLDER" ]; then #check if file exists
    echo "$FOLDER exists." #delete all previous results in folder
    rm $FOLDER/*
fi

counter=10 
ipfs pin ls --type recursive | cut -d' ' -f1 | xargs -n1 ipfs pin rm
ipfs repo gc

while [ "$counter" -gt 0 ]; do
    python main.py -s pickle -m store --filepath test_files/100mb.txt #this is a test call
    #delete ipfs cache
    sleep 10
    ipfs pin ls --type recursive | cut -d' ' -f1 | xargs -n1 ipfs pin rm
    ipfs repo gc
    python main.py -s pickle -m retrieve --filepath 100mb.txt     

    counter=$(( counter - 1 ))
    #python .test/plot.py
done

# all txt files in result folder will be plotted
# !!! it will work when times will be written in results/*txt files !!!
# TODO: change file path ... 
#python test/export_plots.py