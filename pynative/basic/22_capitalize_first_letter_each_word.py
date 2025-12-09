# Exercise 22: Capitalize the first letter of each word in a string
# Expected Output:
#
# str1 = "pynative.com is for python lovers"
# # Output Pynative.com Is For Python Lovers

str1 = "pynative.com is for python lovers"

new_str = " ".join(map(lambda x: x.capitalize(), str1.split()))

print(new_str)
