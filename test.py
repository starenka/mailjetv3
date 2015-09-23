"""
Create : This resource can be used to add historical data to contact.
"""
from mailjet import Client
import os
api_key = os.environ['MJ_APIKEY_PUBLIC']
api_secret = os.environ['MJ_APIKEY_PRIVATE']
mailjet = Client(auth=(api_key, api_secret))
data = {
  'ContactID': 1,
  'Data': 10,
  'Name': 'Purchase'
}
result = mailjet.contacthistorydata.create(data=data)
print result.text
