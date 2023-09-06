# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.7
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from superlink.api.resolution_api import ResolutionApi  # noqa: E501


class TestResolutionApi(unittest.TestCase):
    """ResolutionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ResolutionApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_resolve_data_by_address(self) -> None:
        """Test case for resolve_data_by_address

        Resolves wallets and DNS records for an address  # noqa: E501
        """
        pass

    def test_resolve_data_by_domain(self) -> None:
        """Test case for resolve_data_by_domain

        Resolves wallets and DNS records for a domain  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
