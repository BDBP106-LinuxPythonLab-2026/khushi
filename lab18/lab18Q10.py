# (10) Write a function called nextPrime that finds and returns the first prime number larger
# than some integer, n. The value of n will be passed to the function as its only parameter.
# The main program should read an integer from the user and display the first prime
# number larger than the entered value.

def nextprime(n):
    num=n+1
    while True:
        for i in range(2,num):
                if num%i==0:
                    break
        else:
            return num
        num+=1

m=int(input("Enter an integer: "))
o=nextprime(m)
print("The next prime number is :",o)