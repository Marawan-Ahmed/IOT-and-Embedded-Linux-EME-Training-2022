#!/bin/bash
echo "Input file name"
read file

echo "Input relative dir"
read dir

find $dir -name $file
