# Exercise 6: Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5

list_with_nums = [10, 20, 33, 46, 55]

print(f"Given list is", list_with_nums)

print("Divisible by 5:")

for i in list_with_nums:
    if i % 5 == 0:
        print(i)
