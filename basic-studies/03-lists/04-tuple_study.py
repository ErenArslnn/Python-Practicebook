# tuple syntax is a little bit different

thisIsATuple = (1,2,3,4,5,6)

print(thisIsATuple.count(1))
print(thisIsATuple.index(1))

# tuple only has these two methods and it cannot be updated like list.
# but funny enough a tuple can be casted into a list and a list can be casted into a tuple.

listMaker = list(thisIsATuple)
print(listMaker)
