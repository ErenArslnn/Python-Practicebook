#get things auto

print("Welcome to tax calculator")
print("")
price = float(input("Please tell us your order price: "))
tax = float(input("Please tell us your tax %: "))
priceTotal = price + ((price / 100) * tax)
print("Your total price is: " + str(priceTotal))