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

from superlink.api.market_api import MarketApi


class TestMarketApi(unittest.TestCase):
    """MarketApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MarketApi()

    def tearDown(self) -> None:
        pass

    def test_market_crypto_estimate(self) -> None:
        """Test case for market_crypto_estimate

        CryptoEstimate returns the estimated conversion rates for supported crypto payment options
        """
        pass

    def test_market_crypto_purchase(self) -> None:
        """Test case for market_crypto_purchase

        CryptoPurchase returns the payment details required for crypto payment
        """
        pass

    def test_market_order(self) -> None:
        """Test case for market_order

        Returns order information
        """
        pass

    def test_market_purchase(self) -> None:
        """Test case for market_purchase

        Purchase returns the payment details required by Stripe
        """
        pass

    def test_market_search(self) -> None:
        """Test case for market_search

        Returns market listings
        """
        pass

    def test_market_suggestion(self) -> None:
        """Test case for market_suggestion

        Returns market listings for suggestions
        """
        pass


if __name__ == '__main__':
    unittest.main()
