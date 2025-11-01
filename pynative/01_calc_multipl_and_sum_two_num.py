# Given two integer numbers, write a Python program
# to return their product only if the product
# is equal to or lower than 1000. Otherwise, return their sum.

str_num1 = input("Enter first number: ")
str_num2 = input("Enter second number: ")

if str_num1.isnumeric() and str_num2.isnumeric():
    num1 = int(str_num1)
    num2 = int(str_num2)
    num_multipl = num1 * num2
    num_add = num1 + num2

    if num_multipl <= 1000:
        print("Multiplication of numbers:", num_multipl)
    else:
        print("Sum of numbers:", num_add)
else:
    print("Please enter a valid numbers")




