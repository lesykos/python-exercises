# Exercise 13: Print multiplication table from 1 to 10
# The multiplication table from 1 to 10 is a table that shows
# the products of numbers from 1 to 10.

def num_to_pretty_str(num):
    match len(str(num)):
        case 1:
            return f"{num}  "
        case 2:
            return f"{num} "
        case _:
            return f"{num}"

print("\n", end=' ')

for i in range(1, 11):
    for j in range(1, 11):
        print(num_to_pretty_str(i * j), end=' ')
    print("\n", end=' ')
