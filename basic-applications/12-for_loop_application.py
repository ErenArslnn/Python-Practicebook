numbers = [3,5,7,2,12,32,45]

# 1- print each item in 'numbers' list.

# 2- which items in list 'numbers' are multiplier of '3'?

# 3- print sum of each items in 'numbers'.

products = ["samsung s24", "samsung s23","iphone 15","iphone 16"]

# 4- print apple products only.

# 5- how many samsung product in the 'products' list?

# Solution 1:
print("Solution 1:")
for items in numbers:
    print(items)

# Solution 2:
print("Solution 2:")
for items in numbers:
    if(items % 3 == 0):
        print(f"{items} is a multiplier of '3'")

# Solution 3:
print("Solution 3:")

# sum() function would do the job here but we should use for loop for this application.

number = 0
for items in numbers:
    number += items

print(f"Sum = {number}")

sum = sum(numbers)
print(f"Sum() function check: {sum}")

# If terminal output is equal with sum and sum() our code works fine. For this list it should be 106.

# Solution 4:
print("Solution 4:")
for items in products:
    if(items in "iphone 15" and items in "iphone 16"):
        print(items)

# Solution 5:
print("Solution 5:")
samsung = []
for items in products:
    if(items not in "iphone 15" and items not in "iphone 16"):
        samsung.append(items)
print(f"{len(samsung)} products of samsung in products list.")
    