# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.29
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from superlink.api.partner_api import PartnerApi  # noqa: E501


class TestPartnerApi(unittest.TestCase):
    """PartnerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PartnerApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_access_token(self) -> None:
        """Test case for create_access_token

        Creates an admin token for a partner  # noqa: E501
        """
        pass

    def test_delete_access_token(self) -> None:
        """Test case for delete_access_token

        Deletes an access token  # noqa: E501
        """
        pass

    def test_list_access_tokens(self) -> None:
        """Test case for list_access_tokens

        Lists access tokens for a partner  # noqa: E501
        """
        pass

    def test_partner_purchases(self) -> None:
        """Test case for partner_purchases

        Returns a list of all purchases  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
