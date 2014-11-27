#Simple Mailjet APIv3 wrapper (WIP)


    In [1]: import mailjet

    In [2]: a = mailjet.Api(auth=(API_KEY, API_SECRET))

    In [3]: a.get('apikey')
    Out[3]:
    {u'Count': 1,
     u'Data': [{u'APIKey': u'xxxxxxxxxxxxxxxxxxxxx',
       u'CreatedAt': u'2014-10-21T21:24:15Z',
       u'ID': 194472,
       u'IsActive': True,
       u'IsMaster': True,
       u'Name': u'user',
       u'Runlevel': u'Normal',
       u'SecretKey': u'xxxxxxxxxxxxxxxxx',
       u'Skipspamd': 1,
       u'TrackHost': u'2x15.xx',
       u'UserID': 111111},
     u'Total': 1}
