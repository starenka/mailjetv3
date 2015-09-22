#Simple Mailjet APIv3 wrapper (WIP)

## Usage:

    In [1]: from mailjet import Client

    In [2]: c = Client(auth=(API_KEY, API_SECRET))

    In [3]: c.
    c.AXTesting                   c.CampaignGraphStats          c.Contactslist                c.MessageInformation          c.OpenStats
    c.Aggregategraphstatistics    c.CampaignOverview            c.DomainStats                 c.MessageSentStats            c.ParseRoute
    c.ApiKey                      c.CampaignStats               c.EventCallbackURL            c.MessageState                c.Preferences
    c.ApiKeyAccess                c.ClickStats                  c.GEOStats                    c.MessageStats                c.Sender
    c.ApiKeyTotals                c.Contact                     c.GraphStats                  c.MetaSender                  c.SenderStats
    c.ApiToken                    c.ContactData                 c.ListRecipient               c.Metadata                    c.ToplinkClicked
    c.Batchjob                    c.ContactFilter               c.ListRecipientstatistics     c.MyProfile                   c.Trigger
    c.BounceStats                 c.ContactHistoryData          c.ListStats                   c.Newsletter                  c.User
    c.CSVImport                   c.ContactMetadata             c.ManyContacts                c.NewsletterTemplate          c.UseragentStats
    c.Campaign                    c.ContactStats                c.Message                     c.NewsletterTemplateCategory  c.Widget
    c.CampaignAggregate           c.ContactsListSignup          c.MessageHistory              c.OpenInformation             c.WidgetCustomValue

    In [4]: c.Campaign.get_many
    Out[4]: {u'Count': 0, u'Data': [], u'Total': 0}

    In [5: c.Campaign.get(1)
    Out[5:
    {u'Count': 1,
     u'Data': [{u'CampaignType': 2,
       u'ClickTracked': 3,
       u'CreatedAt': u'2014-11-27T14:38:11Z',
       u'CustomValue': u'mj.nl=1',
       u'FirstMessageID': 16888499051509351,
       u'FromEmail': u'tomas.berger@imper.cz',
       u'FromID': 2,
       u'FromName': u'Tom',
       u'HasHtmlCount': 3,
       u'HasTxtCount': 3,
       u'ID': 1,
       u'IsDeleted': False,
       u'IsStarred': False,
       u'ListID': 1,
       u'NewsLetterID': 1,
       u'OpenTracked': 3,
       u'SendEndAt': u'2014-11-27T14:38:11Z',
       u'SendStartAt': u'2014-11-27T14:38:11Z',
       u'SpamassScore': 1.464,
       u'Status': 0,
       u'Subject': u'Test',
       u'UnsubscribeTrackedCount': 0}],
     u'Total': 1}


    In [6]: c.Campaign.get(2)

    DoesNotExistError                         Traceback (most recent call last)
    <ipython-input-8-4a064dbddd21> in <module>()

    ...

    DoesNotExistError: {'info': u'', 'request': <PreparedRequest [GET]>, 'message': u'Object not found', 'response_parsed': {u'StatusCode': 404, u'ErrorInfo': u'', u'ErrorMessage
    ': u'Object not found'}, 'response': <Response [404]>}


    In [7]: c.Campaign.
    c.Campaign.create    c.Campaign.delete    c.Campaign.get       c.Campaign.get_many  c.Campaign.new       c.Campaign.update

    In [8]: help(c.Campaign)
    Help on Campaign in module mailjet.client object:

    class Campaign(Endpoint)
     |  Method resolution order:
     |      Campaign
     |      Endpoint
     |      __builtin__.object
     |
     |  Methods inherited from Endpoint:
     |
     |  __init__(self, url, doc, auth)
     |
     |  create(self, data, **kwargs)
     |
     |  delete(self, res_id, **kwargs)
     |
     |  get(self, res_id, **kwargs)
     |
     |  get_many(self, **kwargs)
     |
     |  new = create(self, data, **kwargs)
     |
     |  update(self, res_id, data, **kwargs)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Endpoint:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)


    In [9]: c.Campaign._doc
    Out[9]: 'http://dev.mailjet.com/email-api/v3/campaign'

    In [10]: c.Campaign._url
    Out[10]: 'https://api.mailjet.com/v3/REST/campaign'

    In [11]: data={
            'AllowedAccess': 'campaigns,contacts,reports,stats,preferences,property,contact_filter,account,pricing',
            'TokenType': 'iframe',
            'ValidFor': 500000,
            'IsActive': True}


    In [12]: c.ApiToken.create(data=data)
    Out[12]:
    {u'Count': 1,
     u'Data': [{u'APIKeyID': 111111,
       u'AllowedAccess': u'campaigns,contacts,reports,stats,preferences,property,contact_filter,account,pricing',
       u'CatchedIp': u'127.0.0.1',
       u'CreatedAt': u'2014-11-29T15:30:05Z',
       u'FirstUsedAt': u'',
       u'ID': 1536460,
       u'IsActive': True,
       u'Lang': u'',
       u'LastUsedAt': u'',
       u'SentData': u'',
       u'Timezone': u'',
       u'Token': u'xxxxxxxxxxxxxxxxxxxxxxxF4FE61C3BBC3146F9FA17A760F171250C10502C212EF00DE3A6F66DD68C494885F2F3BD49AB407019BD0D894B8885DE7',
       u'TokenType': u'iframe',
       u'ValidFor': 500000}],
     u'Total': 1}

## TODOs:

- tests
