

# For loop. Breaking the loop stops the execution on encountering a number which is less than zero.
numbers = [9, 18, 3, -19, 2.3, 51]
result = 0
for num in numbers:
    if num < 0:
        print("The number is less than 0 and it is, ", num)
        break
    result = result + num
print("The value of result is ", result )

# # The number is less than 0 and it is,  -19
# # The value of result is  30
