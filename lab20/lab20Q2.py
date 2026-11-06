# 2. Vowel and Consonant Counter
# Concepts: for loop over a string, lower(), isalpha(), membership with in
# Read a sentence. Count the vowels, consonants, digits and spaces. Ignore case and
# punctuation.
# Enter text: Hello World 2026!
# Vowels: 3 Consonants: 7 Digits: 4 Spaces: 2


text = input("Enter text: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in text.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
