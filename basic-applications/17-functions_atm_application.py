# ATM application:

# This ATM application will be able to:
# 1- Hold user credentials
# 2- Provide menu, withdraw, deposit and check balance functions as services
# 3- Additional account usage will be determined if current account is not able to accomplish any of the service.


def myATMApp(**kwargs):
    def services():
        while True:
            balance = 100
            balance2 = 35000
            print("Welcome, please select a service: \n To check your balance enter '1' \n To deposit currency enter '2' \n To withdraw currency enter '3' \n To exit enter 'q'")

            selection = input("Please enter a service number: ")
            if selection == '1':
                print(f"Your balance is {balance} USD ")
                input("Please press enter to continue...")

            elif selection == '2':
                deposit = int(input(f"Please enter the amonth you want to deposit: "))
                balance += deposit
                print(f"You deposited {deposit} USD. Your new balance is {balance} USD.")
                input("Please press enter to continue...")

            elif selection == '3':
                withdraw = int(input(f"Please enter the amonth you want to withdraw: "))
                if balance < withdraw:
                    print("Your current account do not have enough currency. To switch second accont press 'y' to exit press 'q'")
                    selection = input()
                    if selection == 'y':
                        balance2 -= withdraw
                        print(f"You withdraw {withdraw} USD from second account. Your new balance in second account is {balance2} USD")
                        input("Please press enter to continue...")
                        continue
                    else: 
                        continue
                else:
                    balance -= withdraw
                    print(f"You withdraw {withdraw} USD from your account. Your new balance is {balance} USD")
                    input("Please press enter to continue...")
            elif selection == 'q':
                print("Hope to see you soon!")
                break

    username = 'thisismyid123'
    pin = '1234'
    
    givenUsername = kwargs.get('username')
    givenPin = kwargs.get('pin')

    if givenUsername == username and givenPin == pin:
        print("Login successful!")
        services()
    else:
        print("Your credentials are wrong!")
myATMApp(username = 'thisismyid123',pin = '1234')
        
        
        
