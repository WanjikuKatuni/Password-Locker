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


if __name__== '__main__':
    unittest.main()