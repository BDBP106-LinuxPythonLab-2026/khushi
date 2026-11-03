# (6) Write a program with a function to calculate the area of a triangle using the formula,
# where a, b, c are sides of the triangle, also providing a test case output from the program
# Area=p
# s(s − a)(s − b)(s − c) where 2s = a + b + c.

import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    print("Area of triangle =", triangle_area(a, b, c))
else:
    print("Invalid triangle")