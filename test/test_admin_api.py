# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.33
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from superlink.api.admin_api import AdminApi


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AdminApi()

    def tearDown(self) -> None:
        pass

    def test_admin_create_access_token(self) -> None:
        """Test case for admin_create_access_token

        Creates an admin token
        """
        pass

    def test_admin_delete_access_token(self) -> None:
        """Test case for admin_delete_access_token

        Deletes an access token
        """
        pass

    def test_admin_list_access_tokens(self) -> None:
        """Test case for admin_list_access_tokens

        Lists access tokens
        """
        pass

    def test_admin_list_partners(self) -> None:
        """Test case for admin_list_partners

        Lists partners
        """
        pass

    def test_admin_partner_create(self) -> None:
        """Test case for admin_partner_create

        Creates a partner
        """
        pass

    def test_remove_reverse_resolution_address(self) -> None:
        """Test case for remove_reverse_resolution_address

        Removes a reverse resolution address from a domain
        """
        pass

    def test_set_reverse_resolution_address(self) -> None:
        """Test case for set_reverse_resolution_address

        Assigns an address to a domain for reverse resolution
        """
        pass


if __name__ == '__main__':
    unittest.main()
