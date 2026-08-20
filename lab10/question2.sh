#!/bin/bash

echo "Enter the file name:"
read file

if [ -e "$file" ]
then
   echo "The file exists."
     if [ -x "$file" ]
     then
	    echo "The file is not executable."
     else
      echo "The file is not executable."
     fi
else
   echo "The file does not exist."
fi   
	    
