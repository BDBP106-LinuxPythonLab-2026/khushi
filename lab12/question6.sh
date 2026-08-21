#/bin/bash
function maximum {
	num1=$1
	num2=$2
	if [ $num1 -gt $num2 ] 
	  then
             echo "$num1 is greater"
	  else
             echo "$num2 is greater"
        fi
}
maximum 7 9
	
