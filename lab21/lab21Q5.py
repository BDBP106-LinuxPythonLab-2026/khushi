# (5) Write a program to find the sum of all the elements in a list using lambda and reduce functions.
A=[1,2,3,4,5,6,7,8,9,10]
from functools import reduce
print(reduce(lambda x,y: x+y,A))