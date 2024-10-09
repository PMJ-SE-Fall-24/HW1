#!/bin/bash

gawk -F',' 'NR > 1 && $3 == 2 && substr($13, 1, 1) == "S" { gsub(/,male/, ",M"); gsub(/,female/, ",F"); 
total += $7; count++ } END { print (count ? total / count : 0) }' titanic.csv 
