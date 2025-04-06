# 1- If a candidate is over 18 or has any parent consent. They can work at a job.
candidateAge = int(input("Candidate age: "))
parentConsent = input("Parent consent present (yes or no): ").strip().lower()

if candidateAge >= 18:
    print("Candidate is allowed to work.")

elif candidateAge < 18 and parentConsent == "yes":
    print("Candidate is allowed to work with parental consent.")

else:
    print("Candidate is not allowed to work.")

# 2- If exam mark is between 50 and 100 print success. Else, print failed.

examNote = int(input("Please enter your exam mark: "))

if examNote < 50:
    print("Exam failed.")

else:
    print("Success!")

# 3- If student exam mark avg is higher than 70 and they have no FFs print Highly successful student certificate granted.

exam1 = int(input("Exam mark 1: "))
exam2 = int(input("Exam mark 2: "))
exam3 = int(input("Exam mark 3: "))
avgMark = (exam1 + exam2 + exam3) / 3
if avgMark >= 70 and exam1 >= 50 and exam2 >= 50 and exam3 >= 50:
    print("Highly successful student certificate granted")
else:
    print("No certificate granted.")

# 4- A candidate needs to have an associate or bachelor degree to get the job but only if they are not smoking.

candidateDegree = input("Please enter your degree level: ").strip().lower()
smokingCheck = input("Do you smoke: ").strip().lower()
if candidateDegree in ["bachelor","associate"] and smokingCheck == "no":
    print("Candidate is suitable for the job.")
else:
    print("Candidate is not suitable for the job.")

# 5- Make a credentials check getting the input of username or email and password.

username = "adminadmin"
email = "admin@info.com"
password = "admin123"

credential1 = input("Username or email: ").strip()
credential2 = input("Password: ").strip()

if credential1 in [username,email] and credential2 == password:
    print("Login successful")
else:
    print("Credentials are not correct. Please try again.")




