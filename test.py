import unittest
from mailjet_rest import Client
import os


class TestSuite(unittest.TestCase):

    def setUp(self):
        self.API_KEY = os.environ['MJ_APIKEY_PUBLIC']
        self.API_SECRET = os.environ['MJ_APIKEY_PRIVATE']
        self.client = Client(auth=(self.API_KEY, self.API_SECRET))

    def test_get_no_param(self):
        result = self.client.contact.get().json()
        self.failUnless(('Data' in result and 'Count' in result))

    def test_get_valid_params(self):
        result = self.client.contact.get(filters={'limit': 2}).json()
        self.failUnless('Count' in result)

    def test_get_invalid_parameters(self):
        # invalid parameters are ignored
        result = self.client.contact.get(filters={'invalid': 'false'}).json()
        self.failUnless('Count' in result)

    def test_get_with_data(self):
        # it shouldn't use data
        result = self.client.contact.get(data={'Email': 'gbadi@mailjet.com'})
        self.failUnless(result.status_code == 200)

    def test_get_with_action(self):
        result = self.client.contact_getcontactslists.get(id=5771382).json()
        self.failUnless('Count' in result)

    def test_get_with_id_filter(self):
        result = self.client.contact.get(filter={'id': 5771382}).json()
        self.failUnless('Count' in result)

    def test_post_with_no_param(self):
        result = self.client.sender.create(data={}).json()
        self.failUnless('StatusCode' in result and result['StatusCode'] is not 400)


if __name__ == '__main__':
    unittest.main()
