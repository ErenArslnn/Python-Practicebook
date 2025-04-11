# Code a calculation app to calculate cost of fuel in given destination according to the price informations below.

benzin = 1.5
diesel = 1.6
lpg = 0.6

distence = int(input("Please enter your travel distence in km: "))
fuel = input("Please enter your fuel type (Benzin, diesel, lpg): ").strip().lower()

if(fuel == "benzin"):
    print(f"Your cost for {distence} km with {fuel} is {distence * fuel}.")
elif(fuel == "diesel"):
    print(f"Your cost for {distence} km with {fuel} is {distence * fuel}.")
elif(fuel == "lpg"):
    print(f"Your cost for {distence} km with {fuel} is {distence * fuel}.")
else:
    print("Please enter a valid fuel type (benzin, diesel, lpg).")

# Take a students 3 exam mark from input and calculate the average mark. Decide the students point from chart below.

# Avg of
# 0-24 => F
# 25-44 => E
# 45-54 => D
# 55-69 => C
# 70-85 => B
# 86-100 => A

mark1 = int(input("Exam mark 1: "))
mark2 = int(input("Exam mark 2: "))
mark3 = int(input("Exam mark 3: "))

total = mark1 + mark2 + mark3
avg = total / 3

if(avg < 25):
    print("Student grade is F")
elif(25 <= avg < 45):
    print("Student grade is E")
elif(45 <= avg < 54):
    print("Student grade is D")
elif(55 <= avg < 70):
    print("Student grade is C")
elif(70 <= avg < 85):
    print("Student grade is B")
elif(85 <= avg <= 100):
    print("Student grade is A")
else:
    print("Invalid average range.")






