#!/bin/bash

function divide {
	local num1=$1
	local num2=$2
	local quotient
	local remainder

	if [ $num2 -eq 0 ]
	then
	   echo "Error Division by zero not allowed"
	  return
	fi
	quotient=$(echo "scale=2 ; $num1 / $num2" | bc)
	remainder=$(echo " $num1 % $num2"| bc) 
	echo "Quotient = $quotient"
	echo "Remainder = $remainder"
}

echo "Enter first number= "
read a

echo "Enter second number= "
read b

result=$(divide "$a" "$b")

echo "$result"


