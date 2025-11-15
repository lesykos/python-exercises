# Exercise 12: Calculate income tax
# Calculate income tax for the given income by adhering to the rules below
#
# Taxable Income    Rate (in %)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20

# Expected Output:
# For example, suppose the income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000

income = 45000
tax = 0

if income > 20000:
    tax = 1000 + (income - 20000) * 0.2
elif income > 10000:
    tax = (income - 10000) * 0.1
else:
    pass

print(f"With an income of {income}, the income tax will be {tax}.")
