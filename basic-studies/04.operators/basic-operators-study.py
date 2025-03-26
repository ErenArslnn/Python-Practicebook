# we have some basic operators let us do some calculations, concating, dividing and more.

x = 10
y = 20

sum = x + y
subtract = x - y
multiply = x * y
divide = x / y
mode = x % y        # ===> Useful with coding questions such as 'fizzBuzz'.  
exponential = x ** y
intDivide = x // y  # ===> only prints division value of integers without mod value. for example: 'print(5 // 2)', will print the integer '2'.

print(sum)
print(subtract)
print(multiply)
print(divide)
print(mode)
print(exponential)
print(intDivide)

# we also can assign our operators to different variables. Normally if you want to sum 'x' and '5', you would use 'x = x + 5'. To make it easier we have assign operators:

a = 10

a += 5      # ----> 'a' assigned to '15'
print(a)    # ----> '15' will be printed.

a -= 5      # a = a - 5
print(a)
a *= 5      # a = a * 5
print(a)
a /= 5      # a = a / 5
print(a)
a %= 8      # a = a % 5
print(a)
a **= 5     # a = a ** 5
print(a)
a //= 5
print(a)

