# (5) Remove all duplicate words from a given sentence using a dictionary. (Hint: Use the
# set() function might be useful here.)
sentence = input("Enter a sentence: ")

words = sentence.split()
unique_words = dict.fromkeys(words)

result = " ".join(unique_words)

print("Sentence without duplicate words:", result)