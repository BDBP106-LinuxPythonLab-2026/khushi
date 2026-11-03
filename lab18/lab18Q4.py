# Given a dictionary with a values list, extract the key whose value has the most unique
# values.
test_dict = {
    "Gfg": [5, 7, 7, 7, 7],
    "is": [6, 7, 7, 7],
    "Best": [9, 9, 6, 5, 5]
}

max_count = 0
result = ""

for key in test_dict:
    count = len(set(test_dict[key]))

    if count > max_count:
        max_count = count
        result = key

print(result)
