#!/bin/bash

# 10 steps loop
for i in {1..10}; do

# Create a dummy text file
	touch dum3file$i.txt
done

# Define a function
function file_count(){

# ls -a -l lists all items (both hidden and unhidden) in the current directory
# grep ^- selects files only
# wc -l counts the lines of the remaining list
	ls -a -l | grep ^- | wc -l
}

# Call the function
file_count
