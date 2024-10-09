#!/bin/bash

DATASET="titanic.csv"
# Build the pipeline
# 1. Extract passengers from 2nd class who embarked at Southampton
# 2. Replace male/female labels with M/F
# 3. Calculate the average age

gawk -F',' 'NR > 1 {
    if ($3==2 && substr($13, 1, 1) == "S") {
        print $0
    }
}' $DATASET | \
sed 's/,male/,M/g; s/,female/,F/g' | \
gawk -F',' '$7 != "" { total += $7; count++ } END { print total/count; }' >output_task3.txt