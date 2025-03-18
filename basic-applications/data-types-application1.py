# Application 1: perimeter of circle calculation with radius of circumference

# To calculate perimeter of circle and radius please provide radius of circumference (float supported)
radiusOfCircumference = float(input("Please provide radius of circumference: "))
π = 3.14

radius = π * (radiusOfCircumference ** 2)

perimeter = 2 * π * radiusOfCircumference

print(f"Radius = {radius}")
print(f"Perimeter = {perimeter}")
