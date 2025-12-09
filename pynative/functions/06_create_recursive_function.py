# Exercise 6: Create a recursive function
# Write a program to create a recursive function
# that calculates the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself repeatedly.

def summer(max_num):
    if max_num:
        return max_num + summer(max_num - 1)
    else:
        return max_num

print(summer(10))
