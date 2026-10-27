# (4) Write a program to filter out the odd elements of the Fibonacci series for the first n terms.
n = int(input("Enter the number of terms: "))

a, b = 0, 1
print("Odd elements in the Fibonacci series:")

for i in range(n):
    if a % 2 != 0:
        print(a, end=" ")
    a, b = b, a + b