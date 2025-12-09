# Exercise 2: Print the Sum of a Current Number and a Previous number
# Write Python code to iterate through
# the first 10 numbers and, in each iteration,
# print the sum of the current and previous number.

print("Printing current and previous number sum in a range(10)")

for i in range(10):
    prev_num = i - 1 if i > 0 else 0
    print(f"Current Number: {i}, Previous Number: {prev_num}, Sum: {i + prev_num}")

