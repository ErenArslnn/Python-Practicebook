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
output = videoGames
print(output)