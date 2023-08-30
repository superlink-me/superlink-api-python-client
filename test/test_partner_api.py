# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.3
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import superlink
from superlink.api.partner_api import PartnerApi  # noqa: E501
from superlink.rest import ApiException


class TestPartnerApi(unittest.TestCase):
    """PartnerApi unit test stubs"""

    def setUp(self):
        self.api = superlink.api.partner_api.PartnerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_access_token(self):
        """Test case for create_access_token

        Creates an admin token for a partner  # noqa: E501
        """
        pass

    def test_delete_access_token(self):
        """Test case for delete_access_token

        Deletes an access token  # noqa: E501
        """
        pass

    def test_list_access_tokens(self):
        """Test case for list_access_tokens

        Lists access tokens for a partner  # noqa: E501
        """
        pass

    def test_partner_purchases(self):
        """Test case for partner_purchases

        Returns a list of all purchases  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
