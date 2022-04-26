from user import User
from credentials import Credentials


def store_account_credentials(a_type,a_username,a_password):
    new_credentials=Credentials(a_type,a_username,a_password)
    return new_credentials

def save_credentials(credentials):
    credentials.save_credentials()

def display_credentials():
    return Credentials.display_credentials()

def main():

    print("Welcome to PasswordLocker. What should we call you?")

    name=input()

    print(f"Hello {name}. To proceed select the shortcodes below")
    print('/n')

    """ while loop to achieve application requisites """

    while True:
        print("To create new username use 'new':'/n' To login to guest account use 'log': '/n' To exit the applicaiton use 'x'")
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
                print(f"Congratulations!!! Account creation successful Welcome {new_user_name} to your password locker VAULT!!")
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
                else:
                    print(f"Welcome {existing_user_name} to your password vault account")
                    print('\n')
                   
                    """
                    after login has accepted
                    """

                    while True: 
                        print(f"{existing_user_name} use these shortcodes to navigate the application: 'sto' -store existing account credentials, 'cr' - create new account credentials, 'dis' - display existing credentials, 'd' -delete credentials, 'ex'-logout of credentials account ")
                        print('\n')
                        short_code = input().lower()

                        if short_code =='sto':
                            print("Enter account details for storage in the VAULT")
                            print("-"*10)

                            print("Enter account name")
                            a_type=input()

                            print("Enter account username")
                            a_username=input()

                            print("Enter account password")
                            a_password=input()

                            save_credentials(store_account_credentials(a_type,a_username,a_password))
                            print('\n')
                                                        
                            print(f"Yippie!!! Credentials for {a_type} with {a_username} and password ****** created successfully")

                       
                        elif short_code =='cr':
                            
                            print("Enter account details for new account")
                            print("-"*10)

                        
                                    

                            print("Enter account name")
                            a_type=input()

                            print("Enter account username")
                            a_username=input()

                                



                        elif short_code =='dis':
                            if display_credentials():
                                print("Below are all your saved credentials")
                                print('\n')

                                for credentials in display_credentials():
                                    print(f"{credentials.account_type} {credentials.account_username} {credentials.account_password}")
                                    print('\n')
                            else:
                                print("No credentials available")
                        # elif short_code =='d':
                        # elif short_code == 'ex':

                        

                    



            
        elif short_code == 'log':
            print('Welcome to your guest Vault')
            print("Enter Login details")
            print("Username")
            preset_user_name = input()
            print("Password")
            preset_password = input()

            while preset_user_name != 'guestuser' or preset_password != '12345':
                    print("Oopsie!! For guest login use the username 'guestuser' and password '12345' ")
                    print('/n')
                    print("Enter Login details again.This time, get it right")
                    print("Username")
                    preset_user_name = input()
                    print("Password")
                    preset_password= input()
            else:
                    print(f"Welcome {preset_user_name} to your guest password vault account")
                    print('/n')


                    """
                    after login has accepted
                    """

                    while True: 
                        print(f"{preset_user_name} use these shortcodes to navigate the application: 'sto' -store existing account credentials, 'dis' - display existing credentials, 'd' -delete credentials, 'ex'-logout of credentials account ")
                        print('\n')
                        short_code = input().lower()

                        if short_code =='sto':
                            print("Enter account details for storage in the VAULT")
                            print("-"*10)

                            print("Enter account name")
                            a_type=input()

                            print("Enter account username")
                            a_username=input()

                            print("Enter account password")
                            a_password=input()

                            save_credentials(store_account_credentials(a_type,a_username,a_password))
                            print('\n')
                                                        
                            print(f"Yippie!!! Credentials for {a_type} with {a_username} and password ****** created successfully")

                       
                        elif short_code =='dis':
                            if display_credentials():
                                print("Below are all your saved credentials")
                                print('\n')

                                for credentials in display_credentials():
                                    print(f"{credentials.account_type} {credentials.account_username} {credentials.account_password}")
                                    print('\n')
                            else:
                                print("No credentials available")
                        # elif short_code =='d':
                        # elif short_code == 'ex':

        elif short_code == 'x':
            print(f"Leaving so soon? Goodbye")
            break

        else:
            print("Oopsie!!! You used the wrong shortcode! Enter a valid showrtcode")


  
        
            


        

""" 
    to ensure the main file is executed
"""
if __name__ == "__main__":
    main()