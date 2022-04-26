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
        
        print('/n')

        

""" 
    to ensure the main file is executed
"""
if __name__ == "__main__":
    main()