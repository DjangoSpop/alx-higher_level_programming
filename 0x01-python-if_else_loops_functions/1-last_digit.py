import random

# You mentioned not to touch the line below.
number = random.randint(-10000, 10000)

# To get the last digit, you can simply take the modulus by 10. If the number is negative, you'll need to handle that case separately.
last_digit = abs(number) % 10

# Printing the required output
print("Last digit of", number, "is", last_digit, end=' ')

# Checking conditions for last digit and printing the corresponding message
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

print()
