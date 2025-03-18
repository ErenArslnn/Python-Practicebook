# Customer credentials

nameSurname = "Eren Arslan"
phone = "05386571312"
email = "erenarslan365@gmail.com"
address = "Turkey"

# Items bought

product1 = "Wireless mouse"
product1Price = 550

product2 = "Wireless keyboard"
product2Price = 650

product3 = "Laptop"
product3Price = 55000

tax = 0.20

# Total price (no tax)

totalPrice = product1Price + product2Price + product3Price
print("Total price without tax: " + str(totalPrice))

# Total price (tax included)

generalTotal = (product1Price + (product1Price * tax)) + (product2Price + (product2Price * tax)) + (product3Price + (product3Price * tax))

print("Your order total: " + str(generalTotal))