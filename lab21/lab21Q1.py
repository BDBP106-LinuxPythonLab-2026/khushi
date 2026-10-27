# (1) Write a program to convert temperature in Celsius to Fahrenheit using map() function.
A=[90,70,80,30,60]
def celcius_to_Fahrenheit(x):
    return (x * 9/5) + 32
print(list(map(celcius_to_Fahrenheit ,A)))


