# 7. Word Frequency Counter
# Concepts: dictionaries, split(), strip(), lower(), get(), items()
# Read a paragraph. Count how often each word appears, ignoring case and stripping
# surrounding punctuation (.,!?;:). Print the words alphabetically with their counts. Then
# print the most frequent word. If several words tie, print all of them.
text = input("Enter a paragraph: ")

words = text.lower().split()
frequency = {}

for word in words:
    word = word.strip(".,!?;:")

    if word:
        frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequencies:")

for word, count in sorted(frequency.items()):
    print(word, ":", count)

if frequency:
    max_count = max(frequency.values())

    print("\nMost frequent word(s):")

    for word, count in sorted(frequency.items()):
        if count == max_count:
            print(word, ":", count)
