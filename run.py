from user import User
from credentials import Credentials


def main():

    print("Welcome to PasswordLocker. What should we call you?")

    name=input()

    print(f"Hello {name}. To proceed select the shortcodes below")
    print('/n')

    """ while loop to achieve application requisites """

    while True:
        print("To create new username use 'new':'/n' To login to existing account use 'log': '/n' T0 exit the applicaiton use 'x'")
        short_code = input().lower() #ensure shortcodes are in lowercase
        print('/n')

        if short_code == 'new':
            print('Create new username')
            new_user_name = input()

            print('Create new password')
            new_password=input()

            print('Confirm new password')
            confirm_password=input()

            while confirm_password != new_password:
                print("Alert!!!Password does not match!!!")
                print('/n')
                print("Enter new password again")
                new_password=input()
                print('/n')
                print("Confirm new password.hint:should be same as the password written above")
                confirm_password=input()
                print('/n')
            
            else:
                print(f"Congratulations!!! Account creation successful Welcome {user_name} to your password locker VAULT!!")
                print('/n')
                print("Enter Login details")
                print("Username")
                existing_user_name = input()
                print("Password")
                existing_password=input()
            
            while existing_user_name != new_user_name or existing_password != new_password:
                print("Oopsie!! Memory can be fleeting at times :) Invalid username or password")
                print('/n')
                print("Enter Login details again.This time, get it right")
                print("Username")
                existing_user_name = input()
                print("Password")
                existing_password=input()
            


        

""" 
    to ensure the main file is executed
"""
if __name__ == "__main__":
    main()