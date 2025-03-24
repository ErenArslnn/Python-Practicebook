# value types acts like different papers with text on it. We can copy one text from another but making a change on a paper won't affect the text on the other paper. We can break it down like this:

# Lets define two different integers.
x = 150
y = 96

# the code below will copy the value in 'y' to value in 'x'

x = y

# after making this equalization both 'x' and 'y' hold the same value of '96'

print(x,y)

# however, changing the value in 'x' or 'y' like this:

y = 100

# won't be seen on 'x' as it is not taking reference from 'y' but just its value.

print(x,y)

# While lists are working as reference types...

a = [150,96]

b = [150,96]

a = b

a[0] = 100

# if lists were working like integers we would print two different lists, 'a' holding '100' value in it while 'b' is only holding '150' and '96'.

print(a)

# 'a' holds '100' in its '[0]' index as we coded.

print(b)

# weird enough 'b' holds '100' in its '[0]' index just as 'a'. This is because lists take reference from each other, following their addresses.

# to make it work like value types, we have 'copy()' method.

listA = [10,20,30]
listB = listA.copy()

listA[0] = 50

print(listA,listB)

# now we should have the items in 'listA' copied into 'listB' just as if they are in 'x' and 'y'.

# there is another method to copy values in a list to another without copying the address of the list and its the 'list()' method.

listA = [10,20,30,40]
listB = list(listA)
print(listA,listB)

listB[0] = 50
print(listA,listB)

# we can use both 'copy()' and 'list()' method to copy values in a list to another. without taking reference.
