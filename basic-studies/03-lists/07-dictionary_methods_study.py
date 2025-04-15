# Dictionary Methods

videoGames = {
    "Game Name": "Ghost of Tsushima",
    "Genre": "Open-world Action Adventure",
    "Class": "AAA" 
}

# access items
output = videoGames["Game Name"]
output = videoGames.get("Game Name")
output = videoGames.keys()
output = videoGames.values()
output = videoGames.items()

# update items
videoGames["Genre"] = "Open-world Role-Playing Action Adventure"
videoGames.update({"Game Name":"Skyrim"})
output = videoGames

# delete items
videoGames.pop("Genre")  # Deletes spesified key, value pair.
videoGames.popitem()     # Deletes last added key, value pair.
videoGames.clear()       # Deletes all items in the dictionary.






output = videoGames
print(output)