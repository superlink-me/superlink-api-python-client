# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.0.2-alpha.1
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import openapi_client
from openapi_client.api.access_token_api import AccessTokenApi  # noqa: E501
from openapi_client.rest import ApiException


class TestAccessTokenApi(unittest.TestCase):
    """AccessTokenApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.access_token_api.AccessTokenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_access_token(self):
        """Test case for create_access_token

        Creates an admin token  # noqa: E501
        """
        pass

    def test_delete_access_token(self):
        """Test case for delete_access_token

        Deletes an access token  # noqa: E501
        """
        pass

    def test_list_access_tokens(self):
        """Test case for list_access_tokens

        Lists access tokens  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()