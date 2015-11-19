from mailjet import Client
import os

mailjet = Client(auth=(os.environ['MJ_APIKEY_PUBLIC'], os.environ['MJ_APIKEY_PRIVATE']))

# f = open('./test.csv')
# result = mailjet.contactslist_csvdata.create(data=f.read(), id=38)

result = mailjet.contact.post(data={'Email': 'ekgjewg@egwgwe.com'})

print result.text
