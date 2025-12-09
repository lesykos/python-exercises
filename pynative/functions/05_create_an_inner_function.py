# Exercise 5: Create an inner function
# Create a program with nested functions to perform an addition calculation as follows:
#
# Define an outer function that accepts two parameters, a and b.
# Inside this outer function, define an inner function that calculates the sum of a and b.
# The outer function should then add 5 to this sum.
# Finally, the outer function should return the resulting value.”

def addition(num1, num2):
    def inner_add(num1, num2):
        return num1 + num2
    return inner_add(num1, num2) + 5

print(addition(1, 2))
