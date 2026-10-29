
# Write a script to check if a number is palindrome or not.
num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
