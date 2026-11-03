# (11) A magic date is a date where the date multiplied by the month is equal to the two-digit
# year. For example, June 10, 1960 is a magic date because June is the sixth month, and
# 6 times 10 is 60 which is the two-digit year. Write a function that determines whether
# or not a date is a magic date. Use your function to create a main program that finds
# and displays all of the magic dates in the 20th century.


def magic_date(d,m,y):
    if d*m==y :
        return "Magic date"
    else:
        return False
for y in range(1,100):
    for m in range(1,13):
        for d in range(1,32):
            res=magic_date(d,m,y)
            if res=="Magic date":
                print(d,m,y,"is a magic date in the 20th century.")