# String concat:
name = "Eren"
surname = "Arslan"
age = 23

print("My name is: " + name + " | My surname is: " + surname + " | My age is: " + str(age)) 
# String format:

message = "My name is {} {}. I am {} years old.".format(name, surname, age)
print(message)

# f-string:

message2 = f"My name is {name} {surname}. I am {age} years old."
print(message2)