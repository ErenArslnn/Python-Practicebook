message = "The usefulness of a cup is in its emptiness."
website = "https://github.com/ErenArslnn"

problem = " I have spaces "
problemFix = problem.strip()
print(problemFix)

messageLower = message.lower()
print(messageLower)

websiteCount = website.count(".")
print(websiteCount)

websiteStart = website.startswith("https:")
print(websiteStart)

websiteEnd = website.endswith("ErenArslnn")
print(websiteEnd)

messageChars = message.isalpha()
print(messageChars)

messageReplace = message.replace(" ","-")
print(messageReplace)

messageReplace2 = message.replace("emptiness","fullness")
print(messageReplace2)

websiteContains = website.index("github.com")
print(websiteContains)

messageList = message.split(" ")
print(messageList)
