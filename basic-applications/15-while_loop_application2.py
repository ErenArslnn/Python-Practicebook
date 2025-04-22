#   Add 'n' student information taken from input inside a dictionary.
#   ** Dictionary format should be like this: (studentNumber, studentName, studentSurname).
#   ** When adding process is over, print studentNames.

n = int(input("Enter the count of students you will add: "))
i = 0
students = []
while i < n:
    studentNumber = int(input("Enter student number: "))
    studentName = input("Enter student name: ") 
    studentSurname = input("Enter student surname: ")
    students.append({"studentNumber":studentNumber,"studentName":studentName,"studentSurname":studentSurname})
    i += 1
for student in students:
    print(student["studentName"]) 
