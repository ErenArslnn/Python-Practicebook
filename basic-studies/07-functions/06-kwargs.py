# In this file, we will handle key word arguments, kwargs in short.

# Goal is the same with '*args'. We want to sent custom amount of paramters in our function but this time, we will be working with key value types.

def loginInfo(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value} \n")

loginInfo(username = 'lionellmessi', email = 'messi@goat.com', keylogin = '123messi123')

