# (3) Write a program to convert a tuple of angles into a list of tuples with each tuple containing the sine and cosine of an angle.
import math

angles = (0, 30, 45, 60, 90)

result = [(math.sin(math.radians(a)), math.cos(math.radians(a))) for a in angles]

print(result)