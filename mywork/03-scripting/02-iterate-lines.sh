#!/bin/bash

set -e

while read line; do
	echo line $x $line;
	sleep 1;
done < guids.list

