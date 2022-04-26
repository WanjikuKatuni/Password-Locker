import unittest 
""" pythin test framework """

from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """ subclass which inherits unittest.TestCase """

    """
    this test class defines test cases for credentials class

    args:
    unittest.Testcase - Testcase class assists in creating test cases
    """
    def setUp(self):
        """
        used to define methods which will be executed by the test method
        """
        self.new_credentials = Credentials("instagram","ann","123")


    def test_init(self):
        """
        define test method
        """

        self.assertEqual(self.new_credentials.account_type,"instagram")
        self.assertEqual(self.new_credentials.account_username,"ann")
        self.assertEqual(self.new_credentials.account_password,"123")

    def test_save_credentials(self):
        """ check if save credentials saves and gives the result """

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def tearDown(self):
        """ to clear the test cases so as to avoid len errors"""
        Credentials.credentials_list=[]

    def test_display_credentials(self):
        """ check if display credentials saves and gives the result """
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

if __name__== '__main__':
    unittest.main()