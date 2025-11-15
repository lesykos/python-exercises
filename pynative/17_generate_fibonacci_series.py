# Exercise 17: Generate Fibonacci series up to 15 terms
# It’s a series of numbers in which the next number is found
# by adding up the two numbers before it. The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21.
# The next number in this series is 13 + 21 = 34.
#
# Expected output:
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34  55  89  144  233  377

times = 13
series = [0, 1]

while times > 0:
    one = series[-1]
    two = series[-2]
    next = one + two
    series.append(next)
    times -= 1

print("Fibonacci sequence:")
for i in series:
    print(i, end=" ")