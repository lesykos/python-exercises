# Exercise 9: Check Palindrome Number
# Write a Python code to check if the given number is a palindrome.
# A palindrome number reads the same forwards and backward.
# For example, 545 is a palindrome number.

number_str = input("Enter a number: ")
reversed_num_str = number_str[::-1]

if number_str == reversed_num_str:
    print(f"Yes, given number ({number_str}) is palindrome number")
else:
    print(f"No, {number_str} is not palindrome number")
