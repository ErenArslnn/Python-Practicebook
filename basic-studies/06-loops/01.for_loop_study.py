# for loop => list

numbers = [1,2,5,3,8,2,8,3,9]
names = ["Eren", "Alex", "Zeynep"]
id = "AIRTK10"

for items in numbers:
    print(f"{items} printed.")

for name in names:
    print(name)

for i in id:
    print(i)

tuple = [(1,2),(3,4),(5,6),(7,8),(9,0)]

for n in tuple:
        print(n)

for n in tuple:
    for n in n:
        print(n)

for x,y in tuple:
     print(x,y)

dictionary = {"cat":"animal","car":"vehicle","tree":"plant"}

for x in dictionary.keys():
     print(x)

for x in dictionary.values():
     print(x)

for x,y in dictionary.items():
     print(x,y)