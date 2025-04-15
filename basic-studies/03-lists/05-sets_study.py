# In this file sets and its rules will be studied.

mySet = {"Barcelona","Real Madrid","Manchester City","Manchester United"}

# Sets won't allow twin indexes or even searching for index making them memory friendly.

# mySet[0]                    # => This will cause an error
mySet.add("Barcelona")        # => Only one 'Barcelona' entry will be awailable 

# Updating an item in a set is also not possible. However It is allowed to push new items in a set.



result = mySet
print(result)

# Order of items in a set will change everytime you run the code.

# To find an index in a set, for loop can be used.

for x in result:
    print(x)

# Or boolean queries can be used.
result = "Barcelona" in mySet

print(result)

# Sets have methods that allows deleting, adding, poping or updating items.

myNewSet = {"Mercedes","BMW","Audi","Porshe"}

myNewSet.add("Volkswagen")      # adds 'Volkswagen' into the set.

myNewSet.discard("Volkswagen")  # Deletes 'Volkswagen' from the set.

# myNewSet.remove("Volkswagen") # Also deletes 'Volkswagen' but raises a 'key error' if not found.

myNewSet2 = {"Opel","Mercedes","Volkswagen"}

myNewSet.update(myNewSet2)      # Updates the set from the item in the parameter.

myNewSet2.pop()                 # Deletes an item from the set. Since we don't know the index precsiely at the moment it will delete randomly.

myNewSet.clear()                # Truncates the set.

print(myNewSet)
print(myNewSet2)
