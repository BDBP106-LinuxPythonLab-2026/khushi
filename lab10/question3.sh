#!/bin/bash

echo "Enter the file name:"
read file

if [ -e "$file" ]
then
   echo "The file exists."
   echo exit 200
else
   echo "The file does not exist."
   echo exit 201
fi
