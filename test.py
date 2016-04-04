import unittest
import mailjet.client
import os

API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['MJ_APIKEY_PRIVATE']

mj = mailjet.Client(auth=(API_KEY, API_SECRET))

class TestSuite(unittest.TestCase):

    def test_get_no_param(self):
        result = mj.contact.get().json()
        self.failUnless(('Data' in result and 'Count' in result))

    def test_get_valid_params(self):
        result = mj.contact.get(filters={'limit': 2}).json()
        self.failUnless('Count' in result)

    def test_get_invalid_parameters(self):
        # invalid parameters are ignored
        result = mj.contact.get(filters={'invalid': 'false'}).json()
        self.failUnless('Count' in result)

    def test_get_with_data(self):
        # it shouldn't use data
        result = mj.contact.get(data={'Email': 'gbadi@mailjet.com'})
        self.failUnless(result.status_code == 200)

    def test_get_with_action(self):
        result = mj.contact_getcontactslists.get(id=5771382).json()
        self.failUnless('Count' in result)

    def test_get_with_id_filter(self):
        result = mj.contact.get(filter={'id': 5771382}).json()
        self.failUnless('Count' in result)

    def test_post_with_no_param(self):
        result = mj.sender.create(data={}).json()
        self.failUnless('StatusCode' in result and result['StatusCode'] is not 400)


if __name__ == '__main__':
    unittest.main()
