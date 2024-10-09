#!/bin/bash

# Define the directory containing the files
DATASET_DIR="dataset1"

# Start building the pipeline
find "$DATASET_DIR" -type f -exec grep -l "sample" {} \; | while read -r file; do
    # Count occurrences of "CSC510"
    count=$(grep -o "CSC510" "$file" | wc -l)
    if [ "$count" -ge 3 ]; then
        # Get file size
        size=$(stat -c%s "$file")
        # Output the filename, count of CSC510, and file size
        echo "$file $count $size"
    fi
done | sort -k2,2nr -k3,3n | gawk '{sub(/file_/, "filtered_", $1); print $1, $2, $3}' > output_task2.txt


