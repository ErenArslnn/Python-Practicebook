numbers = [40,50,35,89,14,35,26]
names = ['alex','berthold','charlie','david','elliot','frank','geralt']
minNumber = min(numbers)
minName = min(names)
maxNumber = max(numbers)
maxName = max(names)

numbers.append(12)
names.append('eren')
newResultNumber = numbers
newResultName = names
numbers.insert(0,31)
numbers.insert(-1,100)
numbers.insert(len(numbers),101)
numbers.pop(0)
newResultNumber = numbers
names.remove("eren")
newResultName = names
numbers.sort()
names.sort()
print(numbers)
print(names)
numbers.append(4)
numbers.append(4)
numbers.append(4)
print(numbers.count(4))
print(f"[{numbers.index(4)}]")