

# For loop; do not break on encountering a number which is less than 0.

numbers = [10, 4, 3, 4, -5, 0, 1]

total = 0
for number in numbers:
    if number < 0:
        print("The number is less than 0 and it is,", number)
        continue
    total = total + number
print("The value of total is ", total)


# The number is less than 0 and it is,  -5
# The value of total is  22