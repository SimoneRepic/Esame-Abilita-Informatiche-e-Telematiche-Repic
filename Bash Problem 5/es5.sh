#!/bin/bash 

# Create an empty text file
touch emptynum.txt

# Loop over first 10 integer numbers
for i in $(seq 1 10); do

# Write the number on file, starting a new line
    printf "$i\n" >> emptynum.txt
done

# Add all the numbers up and print the result
awk '{res += $1}; END{print res}' emptynum.txt
