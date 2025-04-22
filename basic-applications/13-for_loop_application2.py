products = [
    {"product": "HP Victus", "price": 1200},
    {"product": "Asus ROG", "price": 1500},
    {"product": "Dell XPS", "price": 1400},
    {"product": "MacBook Pro", "price": 2000},
    {"product": "Lenovo Legion", "price": 1300},
    {"product": "Acer Predator", "price": 1600},
    {"product": "Razer Blade", "price": 1800},
    {"product": "MSI Stealth", "price": 1700},
    {"product": "Alienware m15", "price": 1900},
    {"product": "Gigabyte AORUS", "price": 1750}
]

# 1- Apply the following sentence to each product in the list:
#    "The [product] is available for [price] dollars."
# 2- Calculate the total price of all products in the list.
# 3- Print the products with the price between 1300 and 1600 dollars.
# 4- List the products according to input(product brand) from user.


# Solution 1:
print("Solution 1:")
for items in products:
    print(f"The {items.get("product")} is available for {items.get("price")} dollars.")

# Solution 2:
print("Solution 2:")
totalPrice = 0
for items in products:
    totalPrice += items.get("price")
print(f"{totalPrice} is the total price for all items in the list.")

# Solution 3:
print("Solution 3:")
for items in products:
    if items.get("price") >= 1300 and items.get("price") <= 1600:
        print(f"{items.get("product")}'s price is {items.get("price")} dollars and its between 1300 and 1600 dollars")

# Solution 4:
print("Solution 4:")
key = input("Please enter a brand: ").strip().lower()
for items in products:
    if items["product"].lower().find(key) > -1:
        print(f"The {key} products you are looking for are: {items.get("product")} with the price of {items.get("price")} dollars.")


