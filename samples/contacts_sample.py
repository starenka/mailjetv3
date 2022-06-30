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
    _id = "*********"  # Put real ID to make it work.
    data = {
        "Data": [
            {
                "Name": "first_name",
                "Value": "John"
            }
        ]
    }
    return mailjet30.contactdata.update(id=_id, data=data)


def create_a_contact():
    """POST https://api.mailjet.com/v3/REST/contact"""
    data = {
        "IsExcludedFromCampaigns": "true",
        "Name": "New Contact",
        "Email": "passenger@mailjet.com"
    }
    return mailjet30.contact.create(data=data)


def manage_contact_properties():
    """POST https://api.mailjet.com/v3/REST/contactmetadata"""
    _id = "$contact_ID"
    data = {
        "Data": [
            {
                "Name": "first_name",
                "Value": "John"
            }
        ]
    }
    return mailjet30.contactdata.update(id=_id, data=data)


def create_a_contact_list():
    """POST https://api.mailjet.com/v3/REST/contactslist"""
    data = {
        "Name": "my_contactslist"
    }
    return mailjet30.contactslist.create(data=data)


def add_a_contact_to_a_contact_list():
    """POST https://api.mailjet.com/v3/REST/listrecipient"""
    data = {
        "IsUnsubscribed": "true",
        "ContactID": "987654321",
        "ContactAlt": "passenger@mailjet.com",
        "ListID": "123456",
        "ListAlt": "abcdef123"
    }
    return mailjet30.listrecipient.create(data=data)


def manage_the_subscription_status_of_an_existing_contact():
    """POST https://api.mailjet.com/v3/REST/contact/$contact_ID/managecontactslists"""
    _id = "$contact_ID"
    data = {
        "ContactsLists": [
            {
                "Action": "addforce",
                "ListID": "987654321"
            },
            {
                "Action": "addnoforce",
                "ListID": "987654321"
            },
            {
                "Action": "remove",
                "ListID": "987654321"
            },
            {
                "Action": "unsub",
                "ListID": "987654321"
            }
        ]
    }
    return mailjet30.contact_managecontactslists.create(id=_id, data=data)


def manage_multiple_contacts_in_a_list():
    """POST https://api.mailjet.com/v3/REST/contactslist/$list_ID/managemanycontacts"""
    _id = "$list_ID"
    data = {
        "Action": "addnoforce",
        "Contacts": [
            {
                "Email": "passenger@mailjet.com",
                "IsExcludedFromCampaigns": "false",
                "Name": "Passenger 1",
                "Properties": "object"
            }
        ]
    }
    return mailjet30.contactslist_managemanycontacts.create(id=_id, data=data)


def monitor_the_upload_job():
    """GET https://api.mailjet.com/v3/REST/contactslist/$list_ID/managemanycontacts"""
    _id = "$list_ID"
    return mailjet30.contactslist_managemanycontacts.get(id=_id)


def manage_multiple_contacts_across_multiple_lists():
    """POST https://api.mailjet.com/v3/REST/contact/managemanycontacts"""
    data = {
        "Contacts": [
            {
                "Email": "passenger@mailjet.com",
                "IsExcludedFromCampaigns": "false",
                "Name": "Passenger 1",
                "Properties": "object"
            }
        ],
        "ContactsLists": [
            {
                "Action": "addforce",
                "ListID": "987654321"
            },
            {
                "Action": "addnoforce",
                "ListID": "987654321"
            },
            {
                "Action": "remove",
                "ListID": "987654321"
            },
            {
                "Action": "unsub",
                "ListID": "987654321"
            }
        ]
    }
    return mailjet30.contact_managemanycontacts.create(data=data)


def upload_the_csv():
    """POST https://api.mailjet.com/v3/DATA/contactslist/$ID_CONTACTLIST/CSVData/text:plain"""
    f = open("./data.csv")
    return mailjet30.contactslist_csvdata.create(id="$ID_CONTACTLIST", data=f.read())


def import_csv_content_to_a_list():
    """POST https://api.mailjet.com/v3/REST/csvimport"""
    data = {
        "ErrTreshold": "1",
        "ImportOptions": "",
        "Method": "addnoforce",
        "ContactsListID": "123456",
        "DataID": "98765432123456789"
    }
    return mailjet30.csvimport.create(data=data)


def using_csv_with_atetime_contact_data():
    """POST https://api.mailjet.com/v3/REST/csvimport"""
    data = {
        "ContactsListID": "$ID_CONTACTLIST",
        "DataID": "$ID_DATA",
        "Method": "addnoforce",
        "ImportOptions": "{\"DateTimeFormat\": \"yyyy/mm/dd\",\"TimezoneOffset\": 2,\"FieldNames\": [\"email\","
                         "\"birthday\"]} "
    }
    return mailjet30.csvimport.create(data=data)


def monitor_the_import_progress():
    """GET https://api.mailjet.com/v3/REST/csvimport/$importjob_ID"""
    _id = "$importjob_ID"
    return mailjet30.csvimport.get(id=id)


def error_handling():
    """https://api.mailjet.com/v3/DATA/BatchJob/$job_id/CSVError/text:csv"""
    """Not available in Python, please refer to Curl"""


def single_contact_exclusion():
    """PUT https://api.mailjet.com/v3/REST/contact/$ID_OR_EMAIL"""
    _id = "$ID_OR_EMAIL"
    data = {
        "IsExcludedFromCampaigns": "true"
    }
    return mailjet30.contact.update(id=_id, data=data)


def using_contact_managemanycontacts():
    """POST https://api.mailjet.com/v3/REST/contact/managemanycontacts"""
    data = {
        "Contacts": [
            {
                "Email": "jimsmith@example.com",
                "Name": "Jim",
                "IsExcludedFromCampaigns": "true",
                "Properties": {
                    "Property1": "value",
                    "Property2": "value2"
                }
            },
            {
                "Email": "janetdoe@example.com",
                "Name": "Janet",
                "IsExcludedFromCampaigns": "true",
                "Properties": {
                    "Property1": "value",
                    "Property2": "value2"
                }
            }
        ]
    }
    return mailjet30.contact_managemanycontacts.create(data=data)


def using_csvimport():
    """POST https://api.mailjet.com/v3/REST/csvimport"""
    data = {
        "DataID": "$ID_DATA",
        "Method": "excludemarketing"
    }
    return mailjet30.csvimport.create(data=data)


def retrieve_a_contact():
    """GET https://api.mailjet.com/v3/REST/contact/$CONTACT_EMAIL"""
    _id = "$CONTACT_EMAIL"
    return mailjet30.contact.get(id=_id)


def delete_the_contact():
    """DELETE https://api.mailjet.com/v4/contacts/{contact_ID}"""


################################################################
# ### Email template. Template API
################################################################


def create_a_template():
    """POST https://api.mailjet.com/v3/REST/template"""
    data = {
        "Author": "John Doe",
        "Categories": "array",
        "Copyright": "Mailjet",
        "Description": "Used to send out promo codes.",
        "EditMode": "1",
        "IsStarred": "false",
        "IsTextPartGenerationEnabled": "true",
        "Locale": "en_US",
        "Name": "Promo Codes",
        "OwnerType": "user",
        "Presets": "string",
        "Purposes": "array"
    }
    return mailjet30.template.create(data=data)


def create_a_template_detailcontent():
    """POST https://api.mailjet.com/v3/REST/template/$template_ID/detailcontent"""
    _id = "$template_ID"
    data = {
        "Headers": "",
        "Html-part": "<h3>Dear passenger, welcome to Mailjet!</h3><br />May the delivery force be with you!",
        "MJMLContent": "",
        "Text-part": "Dear passenger, welcome to Mailjet! May the delivery force be with you!"
    }
    return mailjet30.template_detailcontent.create(id=_id, data=data)


def ise_templates_with_send_api():
    """POST https://api.mailjet.com/v3.1/send"""
    data = {
        "Messages": [
            {
                "From": {
                    "Email": "pilot@mailjet.com",
                    "Name": "Mailjet Pilot"
                },
                "To": [
                    {
                        "Email": "passenger1@mailjet.com",
                        "Name": "passenger 1"
                    }
                ],
                "TemplateID": 1,
                "TemplateLanguage": True,
                "Subject": "Your email flight plan!"
            }
        ]
    }
    return mailjet31.send.create(data=data)


###############################################################
# ### Send campaigns using /campaigndraft
###############################################################


def create_a_campaign_draft():
    """POST https://api.mailjet.com/v3/REST/campaigndraft"""
    data = {
        "Locale": "en_US",
        "Sender": "MisterMailjet",
        "SenderEmail": "Mister@mailjet.com",
        "Subject": "Greetings from Mailjet",
        "ContactsListID": "$ID_CONTACTSLIST",
        "Title": "Friday newsletter"
    }
    return mailjet30.campaigndraft.create(data=data)


def by_adding_custom_content():
    """POST https://api.mailjet.com/v3/REST/campaigndraft/$draft_ID/detailcontent"""
    _id = "$draft_ID"
    data = {
        "Headers": "object",
        "Html-part": "<h3>Dear passenger, welcome to Mailjet!</h3><br />May the delivery force be with you!",
        "MJMLContent": "",
        "Text-part": "Dear passenger, welcome to Mailjet! May the delivery force be with you!"
    }
    return mailjet30.campaigndraft_detailcontent.create(id=_id, data=data)


def test_your_campaign():
    """POST https://api.mailjet.com/v3/REST/campaigndraft/$draft_ID/test"""
    _id = "$draft_ID"
    data = {
        "Recipients": [
            {
                "Email": "passenger@mailjet.com",
                "Name": "Passenger 1"
            }
        ]
    }
    return mailjet30.campaigndraft_test.create(id=_id, data=data)


def schedule_the_sending():
    """POST https://api.mailjet.com/v3/REST/campaigndraft/$draft_ID/schedule"""
    _id = "$draft_ID"
    data = {
        "Date": "2018-01-01T00:00:00"
    }
    return mailjet30.campaigndraft_schedule.create(id=_id, data=data)


def send_the_campaign_right_away():
    """POST https://api.mailjet.com/v3/REST/campaigndraft/$draft_ID/send"""
    _id = "$draft_ID"
    return mailjet30.campaigndraft_send.create(id=_id)


################################################################################
# ## Send campaigns using the Send API
################################################################################

def api_call_requirements():
    """POST https://api.mailjet.com/v3.1/send"""
    data = {
        "Messages": [
            {
                "From": {
                    "Email": "pilot@mailjet.com",
                    "Name": "Mailjet Pilot"
                },
                "To": [
                    {
                        "Email": "passenger1@mailjet.com",
                        "Name": "passenger 1"
                    }
                ],
                "Subject": "Your email flight plan!",
                "TextPart": "Dear passenger 1, welcome to Mailjet! May the delivery force be with you!",
                "HTMLPart": "<h3>Dear passenger 1, welcome to <a "
                            "href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with "
                            "you!",
                "CustomCampaign": "SendAPI_campaign",
                "DeduplicateCampaign": True
            }
        ]
    }
    return mailjet31.send.create(data=data)


########################################################################################
# ## Segmentation
########################################################################################


def create_your_segment():
    """POST https://api.mailjet.com/v3/REST/contactfilter"""
    data = {
        "Description": "Will send only to contacts under 35 years of age.",
        "Expression": "(age<35)",
        "Name": "Customers under 35"
    }
    return mailjet30.contactfilter.create(data=data)


def create_a_campaign_with_a_segmentation_filter():
    """POST https://api.mailjet.com/v3/REST/newsletter"""
    data = {
        "Title": "Mailjet greets every contact over 40",
        "Locale": "en_US",
        "Sender": "MisterMailjet",
        "SenderEmail": "Mister@mailjet.com",
        "Subject": "Greetings from Mailjet",
        "ContactsListID": "$ID_CONTACTLIST",
        "SegmentationID": "$ID_CONTACT_FILTER"
    }
    return mailjet30.newsletter.create(data=data)


##############################################################
# ## Event tracking via webhooks
###############################################################


################################################################
# ## Statistics
###############################################################


def event_based_vs_message_based_stats_timing():
    """GET https://api.mailjet.com/v3/REST/statcounters"""
    filters = {
        "SourceId": "$Campaign_ID",
        "CounterSource": "Campaign",
        "CounterTiming": "Message",
        "CounterResolution": "Lifetime"
    }
    return mailjet30.statcounters.get(filters=filters)


def view_the_spread_of_events_over_time():
    """GET https://api.mailjet.com/v3/REST/statcounters"""
    filters = {
        "SourceId": "$Campaign_ID",
        "CounterSource": "Campaign",
        "CounterTiming": "Event",
        "CounterResolution": "Day",
        "FromTS": "123",
        "ToTS": "456"
    }
    return mailjet30.statcounters.get(filters=filters)


def statistics_for_specific_recipient():
    """GET https://api.mailjet.com/v3/REST/contactstatistics"""
    return mailjet30.contactstatistics.get()


def stats_for_clicked_links():
    """GET https://api.mailjet.com/v3/REST/statistics/link-click"""
    filters = {
        "CampaignId": "$Campaign_ID"
    }
    return mailjet30.statistics_linkClick.get(filters=filters)  # TODO


def mailbox_provider_statistics():
    """GET https://api.mailjet.com/v3/REST/statistics/recipient-esp"""
    filters = {
        "CampaignId": "$Campaign_ID"
    }
    return mailjet30.statistics_recipientEsp.get(filters=filters)   # TODO


def geographical_statistics():
    """GET https://api.mailjet.com/v3/REST/geostatistics"""
    return mailjet30.geostatistics.get()


############################################################################
# ## Parse API: inbound emails
############################################################################


def basic_setup():
    """POST https://api.mailjet.com/v3/REST/parseroute"""
    data = {
        "Url": "https://www.mydomain.com/mj_parse.php"
    }
    return mailjet30.parseroute.create(data=data)


####################################################################################
# ## Senders and Domains
###################################################################################


def validate_an_entire_domain():
    """GET https: // api.mailjet.com / v3 / REST / dns"""
    _id = "$dns_ID"
    return mailjet30.dns.get(id=_id)


def do_an_immediate_check_via_a_post():
    """POST https://api.mailjet.com/v3/REST/dns/$dns_ID/check"""
    _id = "$dns_ID"
    return mailjet30.dns_check.create(id=_id)


def host_a_text_file():
    """GET https://api.mailjet.com/v3/REST/sender"""
    _id = "$sender_ID"
    return mailjet30.sender.get(id=_id)


def validation_by_doing_a_post():
    """POST https://api.mailjet.com/v3/REST/sender/$sender_ID/validate"""
    _id = "$sender_ID"
    return mailjet30.sender_validate.create(id=_id)


def spf_and_dkim_validation():
    """ET https://api.mailjet.com/v3/REST/dns"""
    _id = "$dns_ID"
    return mailjet30.dns.get(id=_id)


def use_a_sender_on_all_api_keys():
    """POST https://api.mailjet.com/v3/REST/metasender"""
    data = {
        "Description": "Metasender 1 - used for Promo emails",
        "Email": "pilot@mailjet.com"
    }
    return mailjet30.metasender.create(data=data)


###################################################################
# ## Language libraries
###################################################################


if __name__ == "__main__":
    result = edit_contact_data()
    print(result.status_code)
    try:
        print(json.dumps(result.json(), indent=4))
    except json.decoder.JSONDecodeError:
        print(result.text)
