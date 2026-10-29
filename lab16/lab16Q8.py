
# (8)Write a program to tell which quadrat a given point lies in the first, second, third or
#fourth quadrant

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("First Quadrant")
elif x < 0 and y > 0:
    print("Second Quadrant")
elif x < 0 and y < 0:
    print("Third Quadrant")
elif x > 0 and y < 0:
    print("Fourth Quadrant")
else:
    print("The point lies on an axis or at the origin")