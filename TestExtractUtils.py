import unittest

from conf import creds
from utils import extract_utils as eu,nse_utils as nu



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.api_key=creds.upstox_creds['api_key']
        self.api_secret=creds.upstox_creds['api_secret']
        self.redirect_uri=creds.upstox_creds['redirect_uri']

    #@unittest.skip("skipping test_login")
    def test_login(self):
        login_code = eu.get_login_code(api_key=self.api_key,api_secret=self.api_secret,redirect_uri=self.redirect_uri);
        print (login_code)
        #login_code='08de5ff37d04676a50efe12d4e813f05349b6ec1'
        self.assertEqual(eu.login_histdata_system(api_key=self.api_key,api_secret=self.api_secret,redirect_uri=self.redirect_uri,code=login_code),True)

    def test_get_option_chain(self):
        self.assertEqual(nu.get_option_chain("SUNPHARMA","30AUG2018"),True)
        pass

if __name__ == '__main__':
    unittest.main()
