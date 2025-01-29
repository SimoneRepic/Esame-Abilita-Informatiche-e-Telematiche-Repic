#!/bin/bash

# Check if the file /etc/shadow exists
if test -f /etc/shadow; then
	echo "Shadow passwords are enabled"

	# Display the content of /etc/shadow
	cat /etc/shadow
else

# Otherwise print the exit code: it is always non-zero if /etc/shadow does not exist
	echo $?
fi

# Check if /etc/shadow is writeable 
if [ -w /etc/shadow ]; then
	echo "You have permission to edit /etc/shadow"

# Return a 0 exit status 
	exit 0
else
	echo "You do NOT have permissions to edit /etc/shadow"

# Otherwise return a non-zero exit status
	exit 22
fi

# Can check the exit status with echo $? from the terminal
