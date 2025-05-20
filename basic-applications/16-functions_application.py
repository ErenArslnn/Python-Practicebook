# Question 1: 
# Write a function that print the value on the console for the given number of times from parameter.

# Question 2:
# Write a function that calculates the area and perimeter of a rectangle. The function should take the length and width as parameters and return the area and perimeter.

# Question 3:
# Make a tails and heads function using random module.

# Question 4:
# Write a function that finds all prime numbers in a given range.

# Question 5:
# Write a function that return all deviders of a number given in parameter in a list. 


# Solution 1:
def printValue(value, times: int):
    for i in range(times):
        print(value)

printValue('value',10)

# Solution 2:
def areaAndPerimeterCalculate(sideCount: int):
        print("Welcome to area andperimeter calculator")
        start = 'start'
        while (start == 'start'):
            side = []
            stringCount = 0
            for i in range(sideCount):
                stringCount += 1
                side.append(float(input(f"{stringCount}. Side lenght (integer or float only): ")))
            print(f"Perimeter for {sideCount} sided shape is {sum(side)}")
            if sideCount == 4:
                 start = input("Do you want to calculate area of this shape? y/n: ")
                 if (start == 'n'):
                    print("bye.")
                    break
            else:
                 print("Area calculation is not available for this shape yet!")
                 break
        while (start == 'y'):
            longSide = int(input("What is the long side: "))
            shortSide = int(input("What is the short side: "))
            area = longSide*shortSide
            print(f"Area of this rectangle is: {area}")
            break

areaAndPerimeterCalculate(1)
        
# Solution 3:
def coinFlip(value: str):
    import random
    myList = ["Head","Tails"]
    if random.choice(myList) == value:
        return "You won!"
    else:
        return "You lose."
print(coinFlip("Head"))

# Solution 4:
def primeNumbers(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def printPrimeRange(end):
    for i in range(end + 1):
        if primeNumbers(i):
            print(i,end=' ')

printPrimeRange(50)

# Solution 5:
def dividerCheck(number: int):
    myNumbers = []
    for i in range(1, number + 1):
        if number % i == 0:
            myNumbers.append(i)
    print(f"\n{myNumbers}")
            
dividerCheck(50)
        
         
     