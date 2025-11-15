# Exercise 11: Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536,
# the output shall be “6 3 5 7“, with a space separating the digits.
# Given:
# number = 7536
# # Output 6 3 5 7

number = 7536

# First option:
result = ""

for i in str(number):
    result = i + " " + result

print(result)

# Second option:
my_list = []

for i in str(number):
    my_list.append(i)

my_list.reverse()

for i in my_list:
    print(i, end=" ")

print("\nend.")
