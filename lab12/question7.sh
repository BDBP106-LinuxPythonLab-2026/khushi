#!/bin/bash
function filedir {
	echo "Enter a file"
	read file
	if [ -e $file ]
	then
	  echo "file exists"
	  ls $file
	else
	   mkdir newdirectory
	   echo "new directory is created"
	fi
}
filedir
