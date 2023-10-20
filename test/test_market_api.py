# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.24
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from superlink.api.market_api import MarketApi  # noqa: E501


class TestMarketApi(unittest.TestCase):
    """MarketApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MarketApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_market_crypto_estimate(self) -> None:
        """Test case for market_crypto_estimate

        CryptoEstimate returns the estimated conversion rates for supported crypto payment options  # noqa: E501
        """
        pass

    def test_market_crypto_purchase(self) -> None:
        """Test case for market_crypto_purchase

        CryptoPurchase returns the payment details required for crypto payment  # noqa: E501
        """
        pass

    def test_market_order(self) -> None:
        """Test case for market_order

        Returns order information  # noqa: E501
        """
        pass

    def test_market_purchase(self) -> None:
        """Test case for market_purchase

        Purchase returns the payment details required by Stripe  # noqa: E501
        """
        pass

    def test_market_search(self) -> None:
        """Test case for market_search

        Returns market listings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
