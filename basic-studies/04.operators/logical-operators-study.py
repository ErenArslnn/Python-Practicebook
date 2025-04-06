# logical operators allow us to work on and, or questions. 
# Lets say a candidate has to be over 18 and at least high school graduate.

inputAge = int(input("Age of the candidate: "))
inputEducation = input("Education level (high school or university degree allowed only): ")

if inputAge >= 18 and inputEducation == "High school" or "high school" or "university" or "University":
    print("Candidate is suitable for driving license.")

elif inputAge < 18 and inputEducation == "High school" or "high school" or "university" or "University":
    print(f"Candidate is not suitable for driving license. Because age {inputAge} is not suitable.")

elif inputEducation != "High school" or "high school" or "university" or "University" and inputAge >= 18:
    print(f"Candidate is not suitable for driving license. Because education level {inputEducation} is not suitable.")

elif not (inputAge >= 18 and inputEducation == "High school" or "high school" or "university" or "University"):
    print(f"Candidate is not suitable for driving license. Because education level {inputEducation} and age {inputAge} is not suitable.")
