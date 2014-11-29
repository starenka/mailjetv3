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

    In [4]: c.Campaign.get()
    Out[4]: {u'Count': 0, u'Data': [], u'Total': 0}


    In [5]: c.Campaign.get(res_id=1)

    DoesNotExistError                         Traceback (most recent call last)
    <ipython-input-8-4a064dbddd21> in <module>()

    ...

    DoesNotExistError: {'info': u'', 'request': <PreparedRequest [GET]>, 'message': u'Object not found', 'response_parsed': {u'StatusCode': 404, u'ErrorInfo': u'', u'ErrorMessage
    ': u'Object not found'}, 'response': <Response [404]>}

    In [6]: c.Campaign.
    c.Campaign.auth    c.Campaign.create  c.Campaign.delete  c.Campaign.doc     c.Campaign.get     c.Campaign.update  c.Campaign.url

    In [7]: c.Campaign.doc
    Out[7]: 'http://dev.mailjet.com/email-api/v3/campaign'

    In [8]: c.Campaign.url
    Out[8]: 'https://api.mailjet.com/v3/REST/campaign'

    In [9]: data={
            'AllowedAccess': 'campaigns,contacts,reports,stats,preferences,property,contact_filter,account,pricing',
            'TokenType': 'iframe',
            'ValidFor': 500000,
            'IsActive': True}


    In [10]: c.ApiToken.create(data=data)
    Out[10]:
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
