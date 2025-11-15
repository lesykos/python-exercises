# Exercise 16: Check Palindrome Number
# A palindrome number is a number that remains the same when
# its digits are reversed. In simpler terms, it reads the same forwards and backward.
# For example 121, 5005.
# Write a code to check if given number is palindrome.

# for i in str(number):
#     result = i + " " + result

str_input = input("Enter a number: ")

if str_input.isnumeric():
    reversed_input = ""
    for i in str_input:
        reversed_input = i + reversed_input

    if reversed_input == str_input:
        print("Number is a palindrome")
    else :
        print("Number is not a palindrome")

else:
    print("Not a valid number")