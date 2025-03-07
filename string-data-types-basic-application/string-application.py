message = "This is a basic application for string data types studies."

# What is the char count in 'message' variable?
# Select 'application' word in 'message'.
# Select first and least 5 chars of 'message' variable.
# Print 'message' variable in reverse.
# Print example sentence below according to input from keyboard.
#   example: The first exam mark for student [input] is [input] and second exam mark is [input]. The calculated average mark for [student] is [average].

charCount = len(message)
print(charCount)

application = message[16:27]
print(application)

first5 = message[:5]
least5 = message[-5:len(message)]
print(first5)
print(least5)

print(message[::-1])

nameSurname = input("Please provide a name: ")
firstExamMark = float(input("Please provide first exam mark: "))
secondExamMark = float(input("Please provide second exam mark: "))
averageExamMark = (firstExamMark + secondExamMark) / 2

print(f"The first exam mark for student {nameSurname} is {firstExamMark} and second exam mark is {secondExamMark}. The calculated average mark for {nameSurname} is {averageExamMark}.")
