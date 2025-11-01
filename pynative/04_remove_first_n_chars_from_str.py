# Exercise 4: Remove first n characters from a string
# Write a Python code to remove characters
# from a string from 0 to n and return a new string.

def remove_chars(word, n):
    return word[n:]

print("Removing characters from a string")
print(remove_chars("pynative", 4))
# output 'tive' first four characters are removed

print(remove_chars("pynative", 2))
# output 'native'