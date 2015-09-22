from mailjet import Client
import os

API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['MJ_APIKEY_PRIVATE']

mailjet = Client(auth=(API_KEY, API_SECRET))

result = mailjet.Contact_getcontactslists.get(id=10, filters={'Limit': 2})
print result
