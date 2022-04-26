class Credentials:
    """
    class which will generate instances of credentials added by user
    """

    credentials_list = [] #empty credentials list

    def __init__(self, account_type, account_username, account_password):
        self.account_type = account_type
        self.account_username = account_username
        self.account_password = account_password

   

