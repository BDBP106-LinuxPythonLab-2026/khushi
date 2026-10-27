# (10) Write a program to extract all vowels in a given string using list comprehension.
A="sayfvywwvfysfawuqu8uw8riqai"
L=[ vow for vow in A if vow.lower() in "aeiou"]
print(L)