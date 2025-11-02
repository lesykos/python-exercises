# Exercise 5: Check if the first and last numbers of a list are the same.
# Write a code to return True if the list’s first and last numbers are the same.
# If the numbers are different, return False.

# Given:
numbers_x = [10, 20, 30, 40, 10]
# output True

numbers_y = [75, 65, 35, 75, 30]
# Output False

def check_list_first_and_last_nums_are_same(list_with_nums):
    return list_with_nums[0] == list_with_nums[-1]

for i in [numbers_x, numbers_y]:
    print(check_list_first_and_last_nums_are_same(i))