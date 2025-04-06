# There is already usage of membership operator and identity operator examples in previous studies but to cover them regardless.
# We can check them in both reference types and value types.

x = 1
y = 1

print(x is y)

print(x is not y)

a,b = [2,4,6],[2,4,6]
a == b

print(a)

print(a is b)

print(a is not b)

print(a[0] in b)

print(a[0] not in b)