# Exercise 20: Print Reverse Number Pattern
# Expected Output:
#
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

i = 1
max= 5

print("\n", end=" ")

while i <= max:
    for j in range(1, max - i + 2):
        print(i, end=" ")
    print("\n", end=" ")
    i += 1
