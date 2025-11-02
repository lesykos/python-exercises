# Exercise 10: Merge two lists using the following condition.
# Given two lists of numbers, write Python code to create
# a new list containing odd numbers from the first list
# and even numbers from the second list.
# Given:
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# Expected Output:
# result list: [25, 35, 40, 60, 90]

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def return_only_even_numbers(some_list):
    new_list = []
    for i in some_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

def return_only_odd_numbers(some_list):
    new_list = []
    for i in some_list:
        if i % 2 != 0:
            new_list.append(i)
    return new_list

only_odd_numbers = return_only_odd_numbers(list1)
only_even_numbers = return_only_even_numbers(list2)

combined_list = only_odd_numbers + only_even_numbers
combined_list.sort()
print(combined_list)