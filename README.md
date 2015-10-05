#Simple Mailjet APIv3 wrapper

[![Build Status](https://travis-ci.org/mailjet/mailjet-apiv3-python.svg?branch=master)](https://travis-ci.org/mailjet/mailjet-apiv3-python)

Compatibility: python2.*

### API documentation

Every code examples can be find on the Mailjet Documentation: http://dev.mailjet.com/guides/?python

## Getting Started

First, make sure you have an API key, and an API secret.
Once you got them, save them in your environment:

```
export MJ_APIKEY_PUBLIC='your api key'
export MJ_APIKEY_PRIVATE='your api secret'
```

``` python
# import the mailjet wrapper
from mailjet import Client
import os

# Get your environment Mailjet keys
API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['MJ_APIKEY_PRIVATE']

mailjet = Client(auth=(API_KEY, API_SECRET))

```

## Make a `GET` request:
``` python
# get every contacts
result = mailjet.contact.get()
```

## `GET` request with filters:
``` python
# get the 2 first contacts
result = mailjet.contact.get(filters={'limit': 2})
```
## `POST` request
``` python
# Register a new sender email address
result = mailjet.sender.post(data={'email': 'test@mailjet.com'})
```

## Combine a resource with an action
``` python
# Get the contact lists of contact #2
result = mailjet.contact_getcontactslists.get(id=2)
```

## Send an Email
``` python

email = {
	'FromName': 'Mr Smith',
	'FromEmail': 'mr@smith.com',
	'Subject': 'Test Email',
	'Text-Part': 'Hey there !',
	'Recipients': [{'Email': 'your email here'}]
}

mailjet.send.post(email)

```

## Create a new Contact
``` python

# wrapping the call inside a function
def new_contact(email):
	return mailjet.contact.new(data={'Email': email})

new_contact('mr@smith.com')
```
