# (5) Write a decorator measure_time to calculate how long a function takes to run. Use it
# on a function that calculates the factorial of a number. Use a test case of calculating the
# factorial of 50.

import time

def measure_time(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return result
    return wrapper

@measure_time
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of 50:", factorial(50))