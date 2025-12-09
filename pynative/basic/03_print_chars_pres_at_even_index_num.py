# Exercise 3: Print characters present at an even index number
# Write a Python code to accept a string from the user
# and display characters present at an even index number.
# For example, str = "PYnative",
#   so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

user_str = input("Enter a string: ")
str_len = len(user_str)

print("Characters present at an even index numbers:")

for i in range(0, str_len, 2):
    print(f"{i}: {user_str[i]}")
