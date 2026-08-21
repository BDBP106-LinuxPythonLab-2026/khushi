#!/bin/bash

read -ra numbers < nums.txt

echo "element of array= "

for number in "${numbers[*]}"
do
  echo $number
done

echo "doubled value="

for number in "${numbers[@]}"
do
  echo $((number * 2))
done
