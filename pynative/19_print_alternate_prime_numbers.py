# Exercise: 19: Print Alternate Prime Numbers till 20
# A Prime Number is a number that can only be divided
# by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).
#
# For example:
# All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19
#
# Alternate prime numbers from 1 to 20:
# 2, 5, 11, 17

def is_prime_number(number):
    if number == 2: return True

    if (number <= 1) or (number % 2 == 0 and number > 2):
        return False

    for i in range(2, number - 1):
        if number % i == 0:
            return False

    # otherwise it's a prime number
    return True

upto_number = 40
prime_numbers_list = []

for i in range(1, upto_number + 1):
    if is_prime_number(i):
        prime_numbers_list.append(i)

prime_numbers_str = ', '.join(map(str, prime_numbers_list))
print(f"All prime numbers from 1 to {upto_number}:", prime_numbers_str)
