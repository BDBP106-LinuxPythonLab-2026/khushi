# (7) Write a program with a function to find whether a given triangle with sides a, b, c is
# isosceles, scalene or equilateral triangle, also provide a test case output from the program.

def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"


a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    print(triangle_type(a, b, c))
else:
    print("Invalid triangle")