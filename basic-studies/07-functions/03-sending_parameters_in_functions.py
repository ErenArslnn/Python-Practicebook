# While definin functions, we can tell the function to wait for a parameter. Later, the parameter provided will be taken into action while calling that function to main.

# Greeting function with name parameters:

def greeting(name: str):
    return f"Hello, {name}."

print(greeting("Alex"))

# Sum calculation with parameters:

def sumCalculate(number1: int,number2: int):
    return number1 + number2

print(sumCalculate(10,15))

# Age calculation with parameters:

def ageCalculate(yearOfBirth: int):
    import datetime
    return datetime.datetime.now().year - yearOfBirth

print(ageCalculate(1973))

# Retirement remaining year calculate with parameters:

def retirementCalculator(yearOfBirth: int, name: str):
    age = ageCalculate(yearOfBirth)
    remainingTime = 60 - age

    if remainingTime >= 60:
        return f"Personal {name} is eligible for retirement."
    else:
        return f"Personal {name} will be eligible for retirement in {remainingTime} years."
    
print(retirementCalculator(2001,"Eren"))
