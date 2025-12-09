# Exercise 9: Find the largest item from list
# Given:
# x = [4, 6, 8, 24, 12, 2]
# Expected Output:
# 24

def get_max(list):
    max = 0
    for i in list:
        if i > max:
            max = i

    return max

xxx = [4, 6, 8, 24, 12, 2]

print(get_max(xxx))