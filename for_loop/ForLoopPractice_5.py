

# For loop with If and Else. Break the execution on encountering a number which less than zero.

numbers = [10, 4, 3, 4, 5, 0, 1, -1]

total = 0
for number in numbers:
    if number < 0:
        print("The number is less than 0 and it is, ", number)
        break
    else:
        print("The number is greater than 0 and it is, ", number)
    total = total + number
print("The value of total is ", total)


# The number is greater than 0 and it is,  10
# The number is greater than 0 and it is,  4
# The number is greater than 0 and it is,  3
# The number is greater than 0 and it is,  4
# The number is greater than 0 and it is,  5
# The number is greater than 0 and it is,  0
# The number is greater than 0 and it is,  1
# The number is less than 0 and it is,  -1
# The value of total is  27