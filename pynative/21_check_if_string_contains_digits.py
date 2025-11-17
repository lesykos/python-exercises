# Exercise 21: Check if a user-entered string contains any digits using a for loop
# Expected Output:
#
# Enter a string: Pynative123Python
# The string contains at least one digit.
#
# Enter a string: PYnative
# The string does not contain any digits.

test_str = input("Enter a string: ")

def check_digits_in_string(string):
    for char in string:
        if char.isdigit():
            return True

    return False

if check_digits_in_string(test_str):
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digit.")
