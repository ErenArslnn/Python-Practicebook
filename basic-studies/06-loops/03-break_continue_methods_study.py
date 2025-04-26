# Print the only repeating number in the list:
numbers = [1,2,3,4,5,6,7,8,9,2]

for number in numbers:
    if numbers.count(number) == 1:
        continue
    else:
        print(number)
        break

# Sum numbers from 0 to 100 except the multipliers of 2 and print the sum:

i = 0
sum = 0

while i <= 100:
    i += 1
    if i % 2 == 0:
        continue
    sum = i + sum
print(sum)
    