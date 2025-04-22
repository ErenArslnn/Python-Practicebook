# While loop usage 

# Print numbers from 0 to 100:

i = 0
while i <= 100:
    print(i)
    i += 1

# Print numbers in a list using while loop:

numberList = [1,2,3,4,5,6,7,8,9]
number = 0

while number < len(numberList):
    print(numberList[number])
    number += 1

# Using 'while loop' with conditional calculations is more beneficial than 'for loop' while 'for loop' is better with lists:

for numbers in numberList:
    print(numbers)