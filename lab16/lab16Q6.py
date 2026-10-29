# (6) Write a program to print the sum of the digits in a number.
num = input("Enter a number: ")
sum = 0

for digit in num:
    sum = sum + int(digit)

print("Sum of digits =", sum)