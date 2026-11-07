# (4) Write a decorator called check_positive that checks whether the argument passed to
# a function is positive. If it is positive, execute the function; otherwise, print
# "Number must be positive".

def check_positive(func):
    def wrapper(num):
        if num > 0:
            func(num)
        else:
            print("Number must be positive")
    return wrapper

@check_positive
def display_number(num):
    print("The number is:", num)

display_number(5)
display_number(-3)
display_number(0)