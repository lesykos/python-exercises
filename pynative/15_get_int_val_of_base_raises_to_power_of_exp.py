# Exercise 15: Get an int value of base raises to the power of exponent
# Write a function called exponent(base, exp) that returns
# an int value of base raises to the power of exp.

# base = 2
# exponent = 5
# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

def exponent(base, exp):
    return base ** exp

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = exponent(base, exp)

print(f"{base} raises to the power of {exp}: {result}")

