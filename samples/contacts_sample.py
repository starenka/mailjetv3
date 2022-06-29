import json
import os

from mailjet_rest import Client


mailjet30 = Client(auth=(os.environ["MJ_APIKEY_PUBLIC"],
                         os.environ["MJ_APIKEY_PRIVATE"]))

mailjet31 = Client(auth=(os.environ["MJ_APIKEY_PUBLIC"],
                         os.environ["MJ_APIKEY_PRIVATE"]),
                   version="v3.1")


def create_contact():
    """POST https://api.mailjet.com/v3/REST/contact"""
    data = {
        "IsExcludedFromCampaigns": "true",
        "Name": "New Contact",
        "Email": "passenger@mailjet.com",
    }
    return mailjet30.contact.create(data=data)


def create_contact_metadata():
    """POST https://api.mailjet.com/v3/REST/contactmetadata"""
    data = {
        "Datatype": "str",
        "Name": "first_name",
        "NameSpace": "static"
    }
    return mailjet30.contactmetadata.create(data=data)


def edit_contact_data():
    """PUT https://api.mailjet.com/v3/REST/contactdata/$contact_ID"""
    id = "*********"  # Put real ID to make it work.
    data = {
        "Data": [
            {
                "Name": "first_name",
                "Value": "John"
            }
        ]
    }
    return mailjet30.contactdata.update(id=id, data=data)


if __name__ == "__main__":
    result = edit_contact_data()
    print(result.status_code)
    try:
        print(json.dumps(result.json(), indent=4))
    except json.decoder.JSONDecodeError:
        print(result.text)
