# A list of strings
['Mike', 'Tom', 'Brittany', 'Shannon']

# A list of integers
[0, 1, 2, 10, 44, 232]

# Appending to a list

add = [0, 1, 2, 10, 44, 232]
add.append(20)

# Appending to a list in a certain place BEFORE
add = [0, 1, 2, 10, 44, 232]
add[:1] = [20]

print(add)

# Appending to a list in a certain place AFTER
add = [0, 1, 2, 10, 44, 232]
add[1:] = [20]

print(add)