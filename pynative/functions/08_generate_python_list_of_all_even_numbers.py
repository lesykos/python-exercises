# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
# Expected Output:
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

def is_even(num):
    return num % 2 == 0

new_list = []

for i in range(4, 30):
    new_list.append(i) if is_even(i) else 0

print(new_list)
