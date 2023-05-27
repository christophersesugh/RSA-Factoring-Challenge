#!/bin/bash

# Check if source and destination file names are provided as command-line arguments
if [ $# -ne 2 ]; then
    echo "Usage: cp.sh <source_file> <destination_file>"
    exit 1
fi

source_file="$1"
destination_file="$2"

# Check if the source file exists
if [ ! -f "$source_file" ]; then
    echo "Source file does not exist: $source_file"
    exit 1
fi

# Copy the file
cp "$source_file" "$destination_file"

# Check if the move operation was successful
if [ $? -eq 0 ]; then
    echo "File copied successfully from $source_file to $destination_file"
else
    echo "Failed to copy file"
fi

