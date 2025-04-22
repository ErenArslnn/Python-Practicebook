# 1- Take the starting and ending range from user and print each even integer within the range.

# 2- Print the numbers taken from user descending order.

# 3- Print 5 numbers from input in ascending order.

# 4- Request a username information from user. If the input includes any space char, request the username again.


# Solution 1:
print("Solution 1:")
start = int(input("Enter starting number: "))
stop = int(input("Enter ending number: "))
while start <= stop:
    if start % 2 == 0:
        print(start)
    start += 1


# Solution 2:
start = int(input("Enter starting number: "))
stop = int(input("Enter ending number: "))
print("Solution 2:")
while start <= stop:
    print(stop)
    stop -= 1


# Solution 3:
print("Solution 3:")
numberList = []
while len(numberList) < 5:
    number = int(input("Please enter a number: "))
    numberList.append(number)
numberList.sort()
for numbers in numberList:
    print(numbers)


# Solution 4:
print("Solution 4:")
userName = input("Please enter a username: ").lower()
while userName.find(' ') > -1:
    userName = input("Please enter a valid username: ").lower()
