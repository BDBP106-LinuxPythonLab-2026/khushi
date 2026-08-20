#!/bin/bash

echo "Enter a string:"
read str

if [ -z "$str" ]
then
   echo "the string is empty"
else
   echo "the string is not empty"
fi
