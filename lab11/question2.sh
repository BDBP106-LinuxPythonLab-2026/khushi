#!/bin/bash

if [ -e test.txt ]
then
   echo "test.txt exists"
else
   echo "test.txt does not exist"
fi

if [ -f test.txt ]
then
   echo "test.txt is a regular file"
else
   echo "test.txt is not a regular file"
fi

if [ -s test.txt ]
then
   echo "test.txt is not empty"
else
   echo "test.txt is empty"
fi
