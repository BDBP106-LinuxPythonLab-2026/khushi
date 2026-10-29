# Write a program to find the roots of a quadratic equation. Figure out what the inputs
# should be and also have provision to deal with cases where you end up getting complex
# roots.
import math
import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("It is not a quadratic equation.")
else:
    d = b**2 - 4*a*c

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print("Two distinct real roots:", root1, "and", root2)

    elif d == 0:
        root = -b / (2*a)
        print("Two equal real roots:", root)

    else:
        root1 = (-b + cmath.sqrt(d)) / (2*a)
        root2 = (-b - cmath.sqrt(d)) / (2*a)
        print("Complex roots:", root1, "and", root2)