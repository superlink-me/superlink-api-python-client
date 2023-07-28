# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.1.18
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import superlink
from superlink.api.access_token_api import AccessTokenApi  # noqa: E501
from superlink.rest import ApiException


class TestAccessTokenApi(unittest.TestCase):
    """AccessTokenApi unit test stubs"""

    def setUp(self):
        self.api = superlink.api.access_token_api.AccessTokenApi()  # noqa: E501

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
