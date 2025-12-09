# Exercise 14: Print a downward half-pyramid pattern of stars
# * * * * *
# * * * *
# * * *
# * *
# *

i = 5

print("\n", end=" ")

while i > 0:
    for j in range(1, i+1):
        print("*", end=" ")
    print("\n", end=" ")
    i -= 1
