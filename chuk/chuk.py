# -*- coding: utf-8 -*-
import os
import sys
import json
import base64
from collections import namedtuple

if (sys.version_info > (3, 0)):
    # Python 3
    from urllib.request import urlopen, Request
    from urllib.parse import urljoin, urlencode
else:
    # Python 2
    from urlparse import urljoin
    from urllib import urlencode
    from urllib2 import Request, urlopen, HTTPError


Response = namedtuple('Response', ['code', 'data'])


class Client(object):
    """Encapsulated client. Used for
    """
    @staticmethod
    def post(*args, **kwargs):
        """Not implemented as Company House doesn't use anything other than GET.
        """
        raise NotImplementedError

    @staticmethod
    def get(url, payload=None, auth=None):
        """Performs a GET HTTP request.

        :param url: The url.
        :param payload: The parameters in a dictionary.
        :param auth: A tuple containing username and password.
        """
        if payload is None:
            payload = {}

        full_url = '{}?{}'.format(url, urlencode(payload))
        request = Request(full_url)
        if auth is not None:
            base64_auth = base64.b64encode('{}{}'.format(auth[0], auth[1]))
            request.add_header("Authorization", "Basic {}".format(base64_auth))
        try:
            response = urlopen(request)
        except HTTPError as e:
            return e.code, None

        return response.code, response.read()


class CompanyHouseAPI(object):
    """A simple consumer for the Company House API.

    You can find detailed documentation about the API here:
    https://developer.companieshouse.gov.uk/api/docs/index.html
    """
    def __init__(self, key=None,
                 url='https://api.companieshouse.gov.uk', **kwargs):
        """
        :param key: The API key.
        :param url. The API base url.
        Defaults to https://api.companieshouse.gov.uk.
        """
        if key is not None:
            self._key = key
        else:
            api_env_var = kwargs.get(
                'key_environment_var', 'COMPANY_HOUSE_API_KEY')
            self._key = os.getenv(api_env_var)
            if self._key is None:
                raise ValueError(
                    "No API key specified. "
                    "Pass it as first parameter of constructor or "
                    "define it in environment variable COMPANY_HOUSE_API_KEY")

        self._url = url
        self._serializer = kwargs.get('serializer', json)
        self._client = kwargs.get('client', Client)

    def _make_request(self, method, endpoint, parameters=None):
        """
        """
        method = getattr(self._client, method.lower())
        url = urljoin(self._url, endpoint)
        return self._client.get(
            url, parameters, auth=self.get_authentication())

    def _serialize(self, data):
        return self._serializer.loads(data)

    def _wrap(self, endpoint, parameters=None, method='get'):
        """Internal method used to make the request and wrap the response.
        """
        status, data = self._make_request(method, endpoint, parameters)
        return Response(status, self._serialize(data))

    def raw(self, method, endpoint, parameters=None):
        """Perform a raw request passing a custom endpoint and parameters.
        :param method: A string containing a http method. Currently Company
        House only supports GET requests.
        :param endpoint: A string containing an endpoint. E.g: "/company/123"
        :param parameters: An optional dictionary containg parameters.
        """
        return self._wrap(endpoint, parameters)

    def get_authentication(self):
        """
        """
        return (self._key, ':')

    def validate_company_number(self, company_number):
        pass

    def search_companies(self):
        """
        """
        endpoint = '/search/companies'
        return self._wrap(endpoint)

    def search_officers(self):
        """
        """
        endpoint = '/search/officers'
        return self._wrap(endpoint)

    def company_profile(self, company_number):
        """
        """
        endpoint = '/company/{}'.format(company_number)
        return self._wrap(endpoint)

    def company_registered_office_address(self, company_number):
        """
        """
        endpoint = '/company/{}/registered-office-address'.format(
            company_number)
        return self._wrap(endpoint)

    def company_officer_list(self, company_number):
        """
        """
        endpoint = '/company/{}/officers'.format(company_number)
        return self._wrap(endpoint)

    def company_filing_history(self, company_number):
        """
        """
        endpoint = '/company/{}/filing-history'.format(company_number)
        return self._wrap(endpoint)

    def company_filing_history_detail(self, company_number, transaction_id):
        """
        """
        endpoint = '/company/{}/filing-history/{}'.format(
            company_number, transaction_id)
        return self._wrap(endpoint)

    def company_insolvency(self, company_number):
        """
        """
        endpoint = '/company/{}/insolvency'.format(company_number)
        return self._wrap(endpoint)

    def company_charges(self, company_number):
        """
        """
        endpoint = '/company/{}/charges'.format(company_number)
        return self._wrap(endpoint)

    def company_charge_detail(self, company_number, charge_id):
        """
        """
        endpoint = '/company/{}/charges/{}'.format(company_number, charge_id)
        return self._wrap(endpoint)

    def officers_appointments(self, officer_id):
        """
        """
        endpoint = '/officers/{}/appointments'.format(officer_id)
        return self._wrap(endpoint)
