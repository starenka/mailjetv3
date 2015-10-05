import unittest
from mailjet import Client
import os

API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['MJ_APIKEY_PRIVATE']

mailjet = Client(auth=(API_KEY, API_SECRET))

class TestSuite(unittest.TestCase):

    def test_get_no_param(self):
        result = mailjet.contact.get().json()
        self.failUnless(('Data' in result and 'Count' in result))

    def test_get_valid_params(self):
        result = mailjet.contact.get(filters={'limit': 2}).json()
        self.failUnless('Count' in result and result['Count'] is 2)

    def test_get_invalid_parameters(self):
        # invalid parameters are ignored
        result = mailjet.contact.get(filters={'invalid': 'false'}).json()
        self.failUnless('Count' in result)

    def test_get_with_data(self):
        # it shouldn't use data
        result = mailjet.contact.get(data={'name': 'guillaume'}).json()
        self.failUnless('Count' in result)

    def test_get_with_action(self):
        result = mailjet.contact_getcontactslists.get(id=2).json()
        self.failUnless('Count' in result)

    def test_get_with_id_filter(self):
        result = mailjet.contact.get(filter={'id': 2}).json()
        self.failUnless('Count' in result)

    def test_post_with_no_param(self):
        result = mailjet.sender.create(data={}).json()
        self.failUnless('StatusCode' in result and result['StatusCode'] is not 400)


if __name__ == '__main__':
    unittest.main()
