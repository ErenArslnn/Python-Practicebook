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
if keyboardInput != countryInfo.keys():
    print("Wrong input. Available countries: 'Greece','Turkey','Bulgaria','Romania'")

if keyboardInput == 'Turkey':
    print(f"{keyboardInput} located at {countryInfo['Turkey'][1]} and its phone code is {countryInfo['Turkey'][0]}")
elif keyboardInput == 'Greece':
     print(f"{keyboardInput} located at {countryInfo['Greece'][1]} and its phone code is {countryInfo['Greece'][0]}")
elif keyboardInput == 'Bulgaria':
    print(f"{keyboardInput} located at {countryInfo['Bulgaria'][1]} and its phone code is {countryInfo['Bulgaria'][0]}")
elif keyboardInput == 'Romania':
    print(f"{keyboardInput} located at {countryInfo['Romania'][1]} and its phone code is {countryInfo['Romania'][0]}")

