# If conditions run only if the condition stated in the if fonction is 'True'

if(True):
    print("Hello world!")

if(False):
    print("Hello world!")

# When if(False) method checked, we can see that the code is actually unrachable since if statement only works with true conditions.

email = 'ifelsestudy@yahoo.com'
username = 'ifelsestudy1'
password = '123456789a.'

if (input("Email or username: ") in [email,username]):
    if(input("Password: ") == password):
        print("Login successful!")
    else:
        print("Password wrong!")
else:
    print("Email or username is wrong!")


if (input("Email or username: ") not in [email,username]):
    print("Email or username is wrong!")
elif(input("Password: ") != password):
    print("Password is wrong!")
else:
    print("Login successful!")

