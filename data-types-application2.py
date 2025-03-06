# Application 2: Kilometer to Mile converter
# To convert Mile to Kilometer please type "toKm"
# To convert Kilometer to Mile please type "toMile"

print("Welcome to Kilometer to Mile converter.")
print("To convert Mile to Kilometer please type 'toKM'")
print("For Kilometer to Mile please type 'toMile'")

unit = input("Please select target unit: ")
if unit == "toKM":
    miles = float(input("Please provide Mile you want to convert to KM: "))
    kilometer = miles * 1.609344
    roundedKilometers = round(kilometer, 2)
    print(f"Your mile equals to: {roundedKilometers} kilometers.")
elif unit == "toMile":
    kilometer = float(input("Please provide Kilometer you want to convert to Mile: "))
    miles = kilometer / 1.609344
    roundedMiles = round(miles, 2)
    print(f"Your kilometer equals to: {roundedMiles} miles.")
else:
    print("Your unit is wrong. Please provide 'toKM' for miles to kilometers or 'toMile' for kilometers to Miles")
