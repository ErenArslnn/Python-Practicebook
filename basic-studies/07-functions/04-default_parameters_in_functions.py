# Normally if you try to use a function with 2 parameters with none or one only, you would get an error.

# For example:

def greeting(name, message):
    return f"{message} {name}."

# To use greeting() function we need to enter 2 parameters. But its possible to use default parameters to prevent this error.

def greetingEnhanced(name, message = "Hello"):
    return f"{message} {name}."

# Call method with 'name' only:

print(greetingEnhanced("Ellie"))

# By default, "Hello" message is set, thus no error.

# Another example:

def exponentiation(number = 2, exponent = 2):
    return number ** exponent

# By default 2 ** 2 will be calculated when exponentiation() function is called.

print(exponentiation())

# But it is not possible to set first parameter as default:

#        def sumCustom(number1 = 5, number2):
#            return number1 + number2               ======>>>>  Will throw an error.

# It is also possible to use functions as parameters in other functions. 
# We can even set default function as a parameter:

def sumCustom(number1 = 1, number2 = 1):
    return number1 + number2

def subtractCustom(number1 = 1, number2 =1):
    return number1 - number2

def calculator(number1 = 1, number2 = 1, function = sumCustom):
    return function(number1, number2)

print(calculator(5,10,subtractCustom))


    
