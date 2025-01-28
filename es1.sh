#! /bin/bash

# 50 steps loop
for i in {1..50}; do

# Create a dummy text file
	touch dumfile$i.txt
done

# Initialize an array
allfile=()

# Loop over all unhidden items in current directory
for item in *; do

# Check if the item is a file
	if [ -f "$item" ]; then

# Add the file to the array
		allfile+=("$item")
	fi
done

# Loop over all hidden items in current directory
for item in .*; do

# Check if the item is a file
	if [[ -f "$item" ]]; then

# Add the file to the array
		allfile+=("$item")
	fi
done

# Say if the array is empty checking its size
if [ ${#allfile[@]} -eq 0 ]; then
	echo "The array is empty"
else

# Otherwise print the array elements
	echo ${allfile[@]}
fi

# Loop over all files in the array
for item in ${allfile[@]}; do

# Get current date in YYYY-mm-dd format
	current_date=$(date +"%Y-%m-%d")

# Append date to file names
# ${file%.*} gets the file name only; ${file##*.} gets the file extension only
	new_filename="$current_date-${item%.*}.${item##*.}"

# Rename each file
	mv "$item" "$new_filename"
done
