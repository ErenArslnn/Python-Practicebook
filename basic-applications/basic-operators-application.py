# In this study file we have some values as declared in below. Requested codes in the comment lines will be covered.

x,y,z = 4, 8, (12,2)

# what is the subtraction of multiplier of two numbers provided from input and sum of 'x,y and z'.

z = sum(z)
        
number1 = int(input("First number (int only): "))
number2 = int(input("Second number (int only): "))

multiply = number1 * number2

total = x + y + z

result = multiply - total 

print(f"Result for question 1: {result}")

# calculate the division of 'z' to 'y' without mode.

result2 = z // y 
print(f"Result for question 2: {result2}")

# what is the result for (x+y+z) % 7

result3 = (x+y+z) % 7

print(f"Result for question 3: {result3}")

# what is the result for y**x ?

result4 = y**x

print(f"Result for question 4: {result4}")

# if x,y,z = (2, 4, 6, 8, 13) then what is z** 3

z = 13

z **= 3

print(f"Result for question 5: {z}")

# if x, y, *z = (2, 4, 6, 8, 13) what is sum(z)?

x, y, *z = (2, 4, 6, 8, 13)

result6 = sum(z)

print(f"Result for question 6: {result6}")

