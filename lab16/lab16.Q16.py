length1=int(input("enter the first length of triangle="))
length2=int(input("enter the second length of triangle="))
length3=int(input("enter the third length of triangle="))
if length1!=length2!=length3:
    print ("the traingle is scalene triangle")
elif length1==length2==length3:
    print ("the triangle is equilateral triangle ")
elif length1==length2 or length2==length3 or length3==length1:
    print ("the traingle is isosceles triangle")