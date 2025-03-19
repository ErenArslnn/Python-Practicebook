# lets store these informations in a dictionary list
    # Greece 30 Europe
    # Turkey 90 Asia
    # Bulgaria 359 Europe
    # Romania 40 Europe

countryInfo = {
    'Greece': [30, 'Europe'],
    'Turkey': [90, 'Asia'],
    'Bulgaria': [359, 'Europe'],
    'Romania': [40, 'Europe']
}

print(countryInfo)

# print dynamic sentence using key pairs from the dictionary list

keyboardInput = input("Country: ")


if keyboardInput == 'Turkey':
    print(f"{keyboardInput} located in {countryInfo['Turkey'][1]} and its phone code is {countryInfo['Turkey'][0]}")
elif keyboardInput == 'Greece':
     print(f"{keyboardInput} located in {countryInfo['Greece'][1]} and its phone code is {countryInfo['Greece'][0]}")
elif keyboardInput == 'Bulgaria':
    print(f"{keyboardInput} located in {countryInfo['Bulgaria'][1]} and its phone code is {countryInfo['Bulgaria'][0]}")
elif keyboardInput == 'Romania':
    print(f"{keyboardInput} located in {countryInfo['Romania'][1]} and its phone code is {countryInfo['Romania'][0]}")

# it seems this is the long way to do it. We can also define dictionaries as values. Here is the more efficent way:

countryInfo2 = {
    "Greece": {
        "Phone Code": 30,
        "Continent": "Europe"
    },
    "Turkey": {
        "Phone Code": 90,
        "Continent": "Asia"
    },
    "Bulgaria": {
        "Phone Code": 359,
        "Continent": "Europe"
    },
    "Romania": {
        "Phone Code": 40,
        "Continent": "Europe"
    }
}
countryName = input("Country: ")

country = countryInfo2[countryName]

print(f"{countryName} is located in {country["Continent"]} and its phone code is: {country["Phone Code"]}")
