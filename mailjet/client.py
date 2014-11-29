#!/usr/bin/env python
# coding=utf-8

import json
import logging

import requests
from requests.compat import urljoin


class Config(object):
    API_URL = 'https://api.mailjet.com/v3/REST/'
    API_DOC = 'http://dev.mailjet.com/email-api/v3/'
    API_PATHS = {  # our_name:API_URL+part (http://dev.mailjet.com/email-api/v3/%s)
        # api
        'ApiKey': 'apikey',
        'ApiKeyAccess': 'apikeyaccess',
        'ApiKeyTotals': 'apikeytotals',
        'ApiToken': 'apitoken',
        'Metadata': 'metadata',
        # account
        'MetaSender': 'metasender',
        'MyProfile': 'myprofile',
        'Sender': 'sender',
        'User': 'user',
        # domain settings
        'DomainStats': 'domainstatistics',
        'ParseRoute': 'parseroute',
        # campaigns
        'BounceStats': 'bouncestatistics',
        'Campaign': 'campaign',
        'CampaignAggregate': 'campaignaggregate',
        'CampaignGraphStats': 'campaigngraphstatistics',
        'CampaignOverview': 'campaignoverview',
        'CampaignStats': 'campaignstatistics',
        'ClickStats': 'clickstatistics',
        'Preferences': 'preferences',
        'Trigger': 'trigger',
        # contact list
        'Aggregategraphstatistics': 'aggregategraphstatistics',
        'Contact': 'contact',
        'ContactData': 'contactdata',
        'ContactFilter': 'contactfilter',
        'ContactHistoryData': 'contacthistorydata',
        'ContactMetadata': 'contactmetadata',
        'Contactslist': 'contactslist',
        'ContactsListSignup': 'contactslistsignup',
        'ContactStats': 'contactstatistics',
        'CSVImport': 'csvimport',
        'GEOStats': 'geostatistics',
        'GraphStats': 'graphstatistics',
        'ListRecipient': 'listrecipient',
        'ListRecipientstatistics': 'listrecipientstatistics',
        'ListStats': 'liststatistics',
        'ManyContacts': 'manycontacts',
        # messages
        'Message': 'message',
        'MessageHistory': 'messagehistory',
        'MessageInformation': 'messageinformation',
        'MessageSentStats': 'messagesentstatistics',
        'MessageState': 'messagestate',
        'MessageStats': 'messagestatistics',
        # newsletter
        'AXTesting': 'axtesting',
        'Batchjob': 'batchjob',
        'Newsletter': 'newsletter',
        'NewsletterTemplate': 'newslettertemplate',
        'NewsletterTemplateCategory': 'newslettertemplatecategory',
        # events
        'EventCallbackURL': 'eventcallbackurl',
        'OpenInformation': 'openinformation',
        'OpenStats': 'openstatistics',
        'SenderStats': 'senderstatistics',
        'ToplinkClicked': 'toplinkclicked',
        'UseragentStats': 'useragentstatistics',
        # widget
        'Widget': 'widget',
        'WidgetCustomValue': 'widgetcustomvalue',

    }

    ENDPOINTS = API_PATHS.keys()

    def __getitem__(self, key):
        try:
            path = self.API_PATHS[key]
            return urljoin(self.API_URL, path), urljoin(self.API_DOC, path)
        except KeyError:
            raise NotImplementedError('Endpoint "%s" is not implemented. Valid endpoints: %s' %
                                      (key, self.ENDPOINTS))


class Endpoint(object):

    def __init__(self, url, doc, auth):
        self.url, self.doc, self.auth = url, doc, auth

    def __doc__(self):
        return self.doc

    def get(self, res_id=None, **kwargs):
        return api_call(self.auth, 'get', self.url, resource_id=res_id, **kwargs)

    def create(self, data, **kwargs):
        return api_call(self.auth, 'post', self.url, data=data, **kwargs)

    def update(self, res_id, data, **kwargs):
        return api_call(self.auth, 'put', self.url, resource_id=res_id, data=data, **kwargs)

    def delete(self, res_id, **kwargs):
        return api_call(self.auth, 'delete', self.url, resource_id=res_id, **kwargs)


class Client(object):

    def __init__(self, auth=None, config=Config()):
        self.auth, self.config = auth, config
        self.endpoints = self.config.ENDPOINTS

    def __dir__(self):
        return self.endpoints

    def __getattr__(self, name):
        if name in self.endpoints:
            url, doc = self.config[name]
            return type(name, (Endpoint,), {})(url=url, doc=doc, auth=self.auth)
        raise AttributeError


def api_call(auth, method, url, data=None, resource_id=None, extra_headers=None,
             timeout=60, debug=False, **kwargs):
    data, url = build_body_and_url(url, method=method,
                                   data=data, resource_id=resource_id)
    headers = build_headers(extra_headers)
    req_method = getattr(requests, method)

    try:
        response = req_method(url, data=data, headers=headers, auth=auth,
                              timeout=timeout, verify=False, stream=False)

        return parse_response(response, debug=debug)

    except requests.exceptions.Timeout:
        raise TimeoutError
    except requests.RequestException as e:
        raise ApiError(e)
    except ValidationError, e:
        raise
    except Exception as e:
        raise


def build_headers(extra_headers=None):
    headers = {'Content-type': 'application/json'}

    if extra_headers:
        headers.update(extra_headers)

    return headers


def build_body_and_url(url, method, data=None, resource_id=None):
    data = json.dumps(data) if data else None

    if resource_id:
        url += '/%d' % resource_id

    return data, url


def parse_response(response, debug=False):
    data = response.json()

    if debug:
        logging.debug('REQUEST: %s' % response.request.url)
        logging.debug('REQUEST_HEADERS: %s' % response.request.headers)
        logging.debug('REQUEST_CONTENT: %s' % response.request.body)

        logging.debug('RESPONSE: %s' % response.content)
        logging.debug('RESP_HEADERS: %s' % response.headers)
        logging.debug('RESP_CODE: %s' % response.status_code)

    if response.status_code > 300:
        errors = data
        exc_data = dict(message=errors.get('ErrorMessage', None),
                        info=errors.get('ErrorInfo', None),
                        response_parsed=data,
                        response=response,
                        request=response.request,
                        )

    if response.status_code == 401:
        raise AuthorizationError(exc_data)
    elif response.status_code == 403:
        raise ActionDeniedError(exc_data)
    elif response.status_code == 404:
        raise DoesNotExistError(exc_data)
    elif response.status_code == 422:
        raise ValidationError(exc_data)
    elif response.status_code >= 500:
        logging.error('Critical API error', exc_info=True, extra=exc_data)
        raise CriticalApiError(errors)
    elif response.status_code >= 400:
        logging.error('API error', exc_info=True, extra=exc_data)
        raise ApiError(exc_data)

    return data


class ApiError(Exception):
    pass


class AuthorizationError(ApiError):
    pass


class ActionDeniedError(ApiError):
    pass


class CriticalApiError(ApiError):
    pass


class ApiRateLimitError(ApiError):
    pass


class TimeoutError(ApiError):
    pass


class DoesNotExistError(ApiError):
    pass


class ValidationError(ApiError):
    pass
