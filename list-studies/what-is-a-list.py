item = "I am a list".split()
print(type(item))
print(item)
print(item[0])
print(item[1])
print(item[2])
print(item[3])

numbers = [1,2,3,4,5,6,7,8,9]

print(type(numbers))
print(type(numbers[0]))

student = ["Alex","Jones",20,60,75]
print(student[0] + " " + student[1])

averageMark = (student[2] + student[3] + student[4]) / 3
print("Mark average is: " + str(averageMark))

students = [["Alex","Jones",20,60,75],["Fred","Jones",30,60,75]]
print(students[0][1])
print(students[0][2])
print(students[0][3])
print(students[0][4])
print(students[1][0])
print(students[1][1])
print(students[1][2])
print(students[1][3])
print(students[1][4])

averageMarks = [(students[0][2] + students[0][3] + students[0][4]) / 3], [(students[1][2] + students[1][3] + students[1][4]) / 3]
print(f"Average Mark for Alex is: {averageMarks[0]} while average Mark for Fred is: {averageMarks[1]}")