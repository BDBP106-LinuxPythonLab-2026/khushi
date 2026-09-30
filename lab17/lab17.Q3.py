l=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
entered_number=int(input("Enter a number: "))
if entered_number in l:
    print("The number is prime")
else:
    print("The number is not prime")