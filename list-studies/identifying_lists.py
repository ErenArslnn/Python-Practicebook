languages = ["English", "German", "French", "Turkish"]
languages[-1] = "Spanish"
print(languages)
languages = languages + ["Turkish", "Russian"]
print(languages)
result = "Russian" in languages
print(result)

del languages[0]

for items in languages:
    print(items)
