# 1- Define the greater integer from input.

greatherCheck = int(input("Provide an integer: "))
greatherCheck2 = int(input("Provide another integer: "))

if greatherCheck > greatherCheck2:
    print(f"{greatherCheck} is greater.")
else:
    print(f"{greatherCheck2} is greater.")

# 2- Check if the integer from input is even or not.

evenCheck = int(input("Please provide an integer: "))

result = (evenCheck % 2) == 0

print(result)

# 3- Check the success status of a student from input of 3 exam marks. Avg of 50 and greater is successful.

grade1,grade2,grade3 =  int(input("Grade 1: ")), int(input("Grade 2: ")), int(input("Grade 3: "))

avgMark = (grade1 + grade2 + grade3) / 3

successResult = (avgMark >= 50)

if successResult == True:
    print("Successful!")
else:
    print("Failed.")