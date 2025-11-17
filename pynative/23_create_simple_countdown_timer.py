# Exercise 23: Create a simple countdown timer using a while loop.
# Write a code to create a simple countdown timer of 5 seconds using a while loop.
#
# Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.
#
# Expected Output:
#
# Time remaining: 5 seconds
# Time remaining: 4 seconds
# Time remaining: 3 seconds
# Time remaining: 2 seconds
# Time remaining: 1 seconds
# Time's up!

import time

start = 7
end = 1

while end <= start:
    print(f"Time remaining: {start} seconds")
    time.sleep(1)
    start -= 1

print("Time's up!")