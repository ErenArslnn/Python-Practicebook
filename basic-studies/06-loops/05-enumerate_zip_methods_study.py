# Enumerate method can be used to numerate indexes in a list.

# Without enumerate method, this can be achieved like this:

brands = ["BMW","Toyota","Ford"]
index = 1
for brand in brands:
    print(f"{index}-{brand}")
    index += 1

# Usage would be like this with enumerate method:

for index,brand in enumerate(brands,1):
    print(f"{index}-{brand}")


# Zip method is useful when we need to merge two lists:

numbers = [100,200,300]

# Additional indexes ment to be ignored.
students = ["John","Alice","Emily","Marcus"]

for number,student in zip(numbers,students):
    print(f"{number}-{student}")