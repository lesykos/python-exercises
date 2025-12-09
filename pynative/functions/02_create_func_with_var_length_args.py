# Exercise 2: Create a function with variable length of arguments
# Write a program to create a function func1() that accepts a variable number
# of arguments and prints each of their values.
#
# Note: Create this function so that it can receive any number of arguments,
# process them, and display the value of each individual argument.

def func1(*someargs):
    for i in someargs:
        print(i)


func1(2,3,4,5,3,4,6,7)