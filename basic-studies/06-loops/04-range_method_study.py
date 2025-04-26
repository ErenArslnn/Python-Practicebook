# Range method allow us to work on lists that has not been defined yet.

# Normally:

numbers = [1,2,3,4,5,6,7,8,9]
for i in numbers:
    print(i)

# Is the basic code we run to print numbers if we want to use for loop.

# With range method its much more easy and flexible:

for i in range(1,100,1):
    print(i)

# We can also define lists which has been created during range method run process to access them easily:

rng = range(0,101)
numbers = list(rng)

print(numbers)

# A very basic application example:
for i in range(0,250):
    if i % 2 == 0:
        print(i)