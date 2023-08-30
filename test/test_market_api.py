# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.2
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import superlink
from superlink.api.market_api import MarketApi  # noqa: E501
from superlink.rest import ApiException


class TestMarketApi(unittest.TestCase):
    """MarketApi unit test stubs"""

    def setUp(self):
        self.api = superlink.api.market_api.MarketApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_market_purchase(self):
        """Test case for market_purchase

        Purchase returns the payment details required by Stripe  # noqa: E501
        """
        pass

    def test_market_search(self):
        """Test case for market_search

        Returns market listings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
