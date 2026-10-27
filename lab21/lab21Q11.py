# (11) Write a program to concatenate a list of strings to make a sentence using reduce function.
from functools import reduce
A=["i","am","khushi"]
print(reduce(lambda x,y:x +" "+ y,A))