class User:
    """ 
    this stores the user password locker login credentials
    """

    user_list = [] #empty user list

    def __init__(self,user_name, password):
        self.user_name = user_name
        self.password =  password