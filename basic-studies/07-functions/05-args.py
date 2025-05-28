# Sometimes we would want to send changing amount of parameters into our functions.

# sumCalculate function example:


def sumCalculate(numbers):
    numbers = []
    start = 'y'
    while start == 'y':
        numbers.append(float(input("Enter number: ")))
        check = input("Add? (y/n): ")
        if check == 'y':
            continue
        else:
            break
    total = 0
    for n in numbers:
        total += n
    return total

# To run =====>> print(sumCalculate([]))

# This is an example of how I would handle a custom sum function right now.

# But with args its possible to enter desired amount of parameters in a function

# Args Example:

def argsSum(*args: float):
    total = 0
    for i in args:
        total += i
    return total

# Now we can use '*args' to send custom amount of parameters in our function. 

print(argsSum(5,5,5,5,5,5,5,5,5,5,5,5,5,5))
    
    
