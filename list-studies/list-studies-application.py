# Define a list of popular video games

gameList = ["GTAV","RDR2","Last of Us 2","Baldur's Gate","Valorant","League of Legends","World of Warcraft","Minecraft","Counter Strike"]

# Find the length of the list

itemNumber = len(gameList)

print(itemNumber)

# Find first and last members of the list

last = gameList[-1]
first = gameList[0]

print(f"{first} and {last}")

# Reblace first game with another unique game

gameList[0] = "GTAVI"

print(gameList)

# Is your new game in the list?

question = "GTAVI" in gameList
print(question)

# List first two games

first2 = gameList[0], gameList[1]
print(f"First two items: {first2}")

# Delete last game on the list

del gameList[-1]

print(gameList)

# Calculate average marks for each student below and then calculate ages of each student.

student1 = ["Eren Arslan", 2010, [70,80,90]]
student2 = ["Fred Becker", 2011, [70,70,80]]
student3 = ["Annie Ruler", 2013, [60,60,90]]
studentList = [student1,student2,student3]
studentAges = [(2025 - (studentList[0][1])), (2025 - (studentList[1][1])), (2025 - (studentList[2][1]))]
studentMarkSum1 = student1[2][0] + student1[2][1] + student1[2][2]
studentMarkSum2 = student2[2][0] + student2[2][1] + student2[2][2]
studentMarkSum3 = student3[2][0] + student3[2][1] + student3[2][2]
studentMarkAverage = [(studentMarkSum1 / len(student1[2])), (studentMarkSum2 / len(student2[2])), (studentMarkSum3 / len(student3[2]))]
print(f"Student's mark averages are: {studentMarkAverage}")

print(f"Studen's ages are: {studentAges}")
