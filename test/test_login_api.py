# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.5.0
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from superlink.api.login_api import LoginApi


class TestLoginApi(unittest.TestCase):
    """LoginApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LoginApi()

    def tearDown(self) -> None:
        pass

    def test_login_with_link(self) -> None:
        """Test case for login_with_link

        Login via a magic link
        """
        pass

    def test_login_with_wallet(self) -> None:
        """Test case for login_with_wallet

        Login with a valid wallet
        """
        pass

    def test_send_login_email(self) -> None:
        """Test case for send_login_email

        Sends the e-mail that contains the magic link to login a specfic user
        """
        pass


if __name__ == '__main__':
    unittest.main()
