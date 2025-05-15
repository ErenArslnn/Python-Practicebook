# Values we get from functions needs to be hold in a variable to be able to print.
# To hold a value in a variable we can use 'return' command.


# An html markdown page would not acknowledge print() function, thus we need to exclude print() funtion from our defined function.

def sumCalculate():
    a = 10
    b = 20
    sum = a + b
    return sum

# In this python file I need to use print() to print the value we have returned but, on another platform with different language, print() function would be replaced with proper one and no errors would be caused.

print(sumCalculate())

# A basic age calculator with return command:

def date():
    import datetime
    return datetime.datetime.now().year

def ageCalculate():
    age = int(input("Enter your birth year: "))
    result = date() - age
    return result

print(ageCalculate()) 

# A basic greeting application (to demonstrate if else conditions with return command):

def hour():
    import datetime
    return datetime.datetime.now().hour

def greet():
    if (hour() < 12):
        return "Good Morning"
    else:
        return "Hello"
    
print(greet())