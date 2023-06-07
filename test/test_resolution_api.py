# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import Superlink
from Superlink.api.resolution_api import ResolutionApi  # noqa: E501
from Superlink.rest import ApiException


class TestResolutionApi(unittest.TestCase):
    """ResolutionApi unit test stubs"""

    def setUp(self):
        self.api = Superlink.api.resolution_api.ResolutionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resolve_data_by_domain(self):
        """Test case for resolve_data_by_domain

        Resolves wallets and DNS records for a domain  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()