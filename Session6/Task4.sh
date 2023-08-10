#!/bin/bash
echo "Input first file name"
read file1

# echo "Input relative dir"
# read dir

echo "Input second file name"
read file2

diff -y file1 file2 >> changes.txt
