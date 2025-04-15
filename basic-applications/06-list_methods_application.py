# This is a file for personal python study on list methods. The following problems are to be solved with lists below.

brandNames = ["Mercedes","BMW","Toyota","Audi"]
years = [2013,2012,2010,2024]

# Add year of 2019 for the brand 'Audi'.

years.append(2019)

# Delete last added entry for years.

years.pop()

# print the sentence below for each brands.
    # '<brandName>' brand's manufacturing year is '<2013>'.

for brands in brandNames:
    print(f"{brands} branded car's manufacturing year is {years[0]}.")

# order brandNames in alphabetical order.

brandNames.sort()

# order years desc.

years.sort(reverse=True)
print(years)

# what is the oldest year?

minYear = min(years)
print(minYear)

# count how many audi brands there are in 'brandNames'.

print(brandNames.count("Audi"))

# delete brand 'Mercedes' from 'brandNames'.

brandNames.remove("Mercedes")

# delete all indexes in both lists.

brandNames.clear()
years.clear()

# add brand name and year information you get from input to corresponding lists.

brandNames.append(input("Please provide a car brand: "))
years.append(input("Please provide manufacturing year for your brand: "))

print(brandNames)
print(years)