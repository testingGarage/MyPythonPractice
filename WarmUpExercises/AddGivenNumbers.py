
# Program to add given 'n' numbers and print the total sum of it.


inputYourNumbers = input("Enter the numbers to add separated by whitespace.")

fetchInputedNumbers = inputYourNumbers.split()

numbersFetchedAsInt = list(map(int, fetchInputedNumbers))

totalSum = sum(numbersFetchedAsInt)

print("The total sum of given numbers is ", totalSum)