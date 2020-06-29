#import necessary modules
import sys, random, string, math
from random import randint
import random

''' Online Banking System with Object Oriented Programming '''
#storing structure for the accounts
accounts_data = {'drizzyR': ['7675234','7234',230]}
for i in accounts_data.keys():
    print(i)

#defining our class object
class Bank:
    digits = "0123456789"
    number = ''
    card = ''
    #initializing our balance in our account
    def __init__(self):
        self.balance = 0

    #deositing method -- takes in amount as argument
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    #wthdrawing method -- takes in an argument amount as well
    def withdraw(self, amount):
        #conditional statement to check that the account has sufficient funds
        if self.balance >= amount:
            self.balance -= amount
        else:
            #otherwise let the user know there's insufficient funds
            return 'Amount entered cannot be withdraw due to insufficient funds!'

    #function to output balance to user
    def showbalance(self):
        return 'Balance: ' + str(self.balance)
  
    # function for generating our 7 digits pin as account number
    def account_number_gen():
        for i in range(10):
            #join the number between the range of 0 to 9 [10*]
            Bank.number += Bank.digits[math.floor(random.random() * 10)]
        return Bank.number

    def card_number(self):
        for i in range(16):
            Bank.card += Bank.digits[math.floor(random.random() * 10)]

        Bank.card = '-'.join([Bank.card[i:i+4] for i in range(0, len(Bank.card), 4)])
        return Bank.card

#storing structure for the accounts


balance = 0
class ActionMenu:
    balance = 0
    def __init__(self):
        pass
    
    def open_account(self):  
        #generating account number from the imported module
        account_number = Bank.account_number_gen()

        print(f'Your account number will be: {account_number}')
        username = input('Create a username or Enter [S]top: \n')
        if username.upper() == 'S':
            sys.exit()
            
        while username in accounts_data.keys():
            username = input('Username is already taken. Choose a different one: ') 

        #user creates 4-digit pin
        user_pin = input('Choose a 4-digit pin for accessing your account: \n')
        action = True
        while action:
            #don't take any length of pin that doesn't equal 4
            if len(user_pin) != 4:
                user_pin = input('Did not meet requirement. Try again! \n')
                continue
            else:
                #success
                print('\nAccount Created Successfully!')
                username = username.lower()
                #matching username and pin for future authentication to see account details
                accounts_data[username] = [account_number, user_pin, ActionMenu.balance]
                user_input = input('Would you like to deposit money now? [Y]es Or [N]o: ')
                if user_input.upper() == 'Y':
                    user_amount = int(input('Amount: -- $50 Above: '))
                    if user_amount >= 50:
                        ActionMenu.balance += user_amount
                        print('\n.............  Account Details  .............')
                        print("\tAccount Username: " + str(username) + '\n\tAccount Number: ' + str(account_number), '\n\tBalance: $' + str(ActionMenu.balance))
                    else:
                        print('Your input is invalid')
                else:
                    sys.exit()
            break
    def deposit(self):
        account_username = input('\nUsername: ')
        if account_username in accounts_data.keys():
            account_pin = input('Pin: ')
            if account_pin == accounts_data[account_username][1]:
                user_amount = int(input('\nHow much do you want to deposit? Amount must be over 50..\n'))
                if user_amount >= 50:
                    ActionMenu.balance += user_amount
                    print('....... Details  ........')
                    print('\tA sum of',str(user_amount), 'was added')
                    print('\tBalance: ', ActionMenu.balance)
                else:
                    print('Your input is invalid')
                    self.deposit()
            else:
                print('Wrong Pin number')
                self.deposit()
        else:
            print(f'No Account under that {account_username}')
            self.deposit()
            
    def withdraw(self):
        account_username = input('\nUsername: ')
        if account_username in accounts_data.keys():
            account_pin = input('Pin: ')
            if account_pin == accounts_data[account_username][1]:
                user_amount = int(input('\nHow much do you want to withdraw? Amount must be over 50..\n'))
                if user_amount <= ActionMenu.balance:
                    ActionMenu.balance -= user_amount
                    print('....... Details  ........')
                    print('\tA total of $' + str(user_amount) + ' was withdrew')
                    print('\tBalance: ', ActionMenu.balance)
                else:
                    print('Insufficient funds!')
                    self.withdraw()
            else:
                print('Wrong Pin number')
                self.withdraw()
        else:
            print(f'No Account under that {account_username}')
            self.withdraw()
                

                           
    def close_account(self):
        checking = True
        account_username = input('\nUsername: ')
        while checking:
            if account_username in accounts_data.keys():
                account_pin = input('Pin: ')
                if account_pin == accounts_data[account_username][1]:
                    accounts_data.pop(account_username)
                    print('Your account was successfully close.')
                    ActionMenu.anything_else()
                else:
                    print('Wrong pin number')
            else:
                print('Account not found!')
        return close_account()

    #SHOW CUSTOMER DETAILS
    def show_account(self):
        checking = True
        account_username = input('\nUsername: ')
        while checking:
            if account_username in accounts_data.keys():
                account_pin = input('Pin: ')
                if account_pin == accounts_data[account_username][1]:
                    print('.............. Showing Account Number ............')
                    print('\t\tAccount number: ' + str(accounts_data[account_username][0]))
                    break
                else:
                    print('Wrong pin number')
                    continue
            else:
                print('User doesn\'t exit')
                continue
    def anything_else(self):
        user_input = input('Would you like to do anything else? [Y]es Or [N]o: ')
        if user_input.upper() == 'Y':
            perform_action()
        elif user_input.upper() == 'N':
            print('Thank you!')
            sys.exit()
        else:
            sys.exit()


action = ActionMenu()
name = input('Name: ')
print(f'Hi there {name}! What would you like to do today? \n')
def perform_action():
    try:
        user_action = input('[O]pen Account c[L]ose Account s[H]ow Customers [S]ervices [D]eposit [E]xit [W]ithdraw: \n')
        while user_action:
            if user_action.upper() == "O":
                action.open_account()
                action.anything_else() 
            
            elif user_action.upper() == "L":
                action.close_account()
                action.anything_else()

            elif user_action.upper() == "H":
                action.show_account()
                action.anything_else()
            elif user_action.upper() == 'E':
                sys.exit()
            elif user_action.upper() == 'D':
                action.deposit()
                action.anything_else()
            elif user_action.upper() == 'W':
                action.withdraw()
                action.anything_else()
    
    except:
        sys.exit()
    print(f'Have a wonderful day, {name}')

perform_action()
        
