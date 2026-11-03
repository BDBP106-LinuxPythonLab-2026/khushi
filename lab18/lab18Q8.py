# (8) Write a program to interchange the even and odd components of an input list. The list
# can contain any type of variables. Output the result for the following example:
# [23,32,33,44,’BDBH101’,’hello’,’python’, 15, 1e-10, True,’hit’]

lst = [23, 32, 33, 44, 'BDBH101', 'hello',
       'python', 15, 1e-10, True, 'hit']

for i in range(0, len(lst) - 1, 2):
    lst[i], lst[i + 1] = lst[i + 1], lst[i]

print(lst)