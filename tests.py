# -*- coding: utf-8 -*-
import os
import unittest

from chuk import CompanyHouseAPI, Client, Response


class TestClient(unittest.TestCase):
    def test_post(self):
        self.assertRaises(NotImplementedError, Client.post)

    # def test_get(self):
        # self.assertEqual(1, 2)


class TestResponse(unittest.TestCase):
    def test_response(self):
        res = Response(200, {'hello': 'test'})
        self.assertEqual(res.code, 200)
        self.assertEqual(res.data, {'hello': 'test'})


class TestCompanyHouseAPI(unittest.TestCase):
    def unset_var(self, var):
        del os.environ[var]

    def test_no_key_raises_error(self):
        self.assertRaises(ValueError, CompanyHouseAPI)

    def test_key_on_env_var(self):
        os.environ['COMPANY_HOUSE_API_KEY'] = 'test'
        api = CompanyHouseAPI()
        self.assertEqual(api._key, 'test')
        self.unset_var('COMPANY_HOUSE_API_KEY')

    def test_key_on_custom_env_var(self):
        var = 'MY_CUSTOM_CHUK_ENV_VAR'
        os.environ[var] = 'customtest'
        self.assertRaises(ValueError, CompanyHouseAPI)
        api = CompanyHouseAPI(key_environment_var=var)
        self.assertEqual(api._key, 'customtest')
        self.unset_var(var)

    def test_normal_key(self):
        api = CompanyHouseAPI(key='123')
        self.assertEqual(api._key, '123')

    def test_custom_url(self):
        api = CompanyHouseAPI(key='test', url='http://myproxy')
        self.assertEqual(api._key, 'test')
        self.assertEqual(api._url, 'http://myproxy')

    def test_default_client_assigned(self):
        api = CompanyHouseAPI(key='test')
        self.assertIs(api._client, Client)

    def test_custom_client_assigned(self):
        class MockClient:
            pass

        api = CompanyHouseAPI(key='test', client=MockClient())
        self.assertIsInstance(api._client, MockClient)

    def test_custom_serializer_assigned(self):
        class MockSerializer:
            pass

        api = CompanyHouseAPI(key='test', serializer=MockSerializer())
        self.assertIsInstance(api._serializer, MockSerializer)

if __name__ == '__main__':
    unittest.main()
