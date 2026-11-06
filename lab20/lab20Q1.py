# 1. Number Classifier
# Concepts: if/elif/else
# Ask the user for an integer. Print whether it is positive, negative or zero. If it is non-zero,
# also print whether it is even or odd. If it is divisible by both 3 and 5, print "FizzBuzz
# number!".
# Enter a number: -15
# Negative, odd
# FizzBuzz number!

N= int(input("enter a number = "))
if  (N>0):
    print("the number is positive")
elif(N==0):
    print("the number is zero")
elif(N<0):
    print("the number is negative")
if (N%2==0):
     print("the number is even")
else:
     print("the number is odd")
if(N%3==0) and (N%5==0):
 print("Fizz Buzz Number")
else:
    print("Not a Fizz Buzz Number")