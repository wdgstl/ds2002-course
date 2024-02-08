#!/bin/bash

if [ -z "$1" ]; then
	echo "This script converts a TSV into a CSV";
	echo "Append the input file name and then the output file name";
fi

/usr/bin/tr '\t', ',' < $1 > $2



#tr command = translate/convert 
# look for the tab character, replace with ,
# input file is 1, put the output into 2

# fi closes the if statement

