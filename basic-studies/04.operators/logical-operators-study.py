# logical operators allow us to work on and, or questions. 
# Lets say a candidate has to be over 18 and at least high school graduate.

inputAge = int(input("Age of the candidate: "))
inputEducation = input("Education level (high school or university degree allowed only): ").strip().lower()

if inputAge >= 18 and (inputEducation == "high school" or inputEducation == "university"):
    print("Candidate is suitable for a driving license.")

elif inputAge < 18:
    print(f"Candidate is not suitable for a driving license. Because age {inputAge} is not suitable.")

elif inputEducation not in ["high school", "university"]:
    print(f"Candidate is not suitable for a driving license. Because education level '{inputEducation}' is not suitable.")

else:
    print(f"Candidate is not suitable for a driving license. Because education level '{inputEducation}' and age {inputAge} are not suitable.")
