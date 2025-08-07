
# Program to define user defined function for adding two numbers.

# function to add two given numbers.
def AddTwoNumbers(numberOne, numberTwo):
    totalSum = numberOne + numberTwo
    return totalSum

# converting the string entered to type integer.
numberOne = int(input("What is the first number to be added? "))
numberTwo = int(input("What is the second number to be added? "))

# passing the two integers to above defined function -- AddTwoNumbers
sumOfTwoNumbers = AddTwoNumbers(numberOne, numberTwo)
print("The sum of given two numbers is: ", sumOfTwoNumbers)