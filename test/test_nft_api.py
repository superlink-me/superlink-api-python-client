# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.30
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from superlink.api.nft_api import NftApi


class TestNftApi(unittest.TestCase):
    """NftApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NftApi()

    def tearDown(self) -> None:
        pass

    def test_get_token_image_by_domain(self) -> None:
        """Test case for get_token_image_by_domain

        Returns a SVG image for a Superlink NFT
        """
        pass

    def test_get_token_metadata_by_domain(self) -> None:
        """Test case for get_token_metadata_by_domain

        Returns metadata usually associated with NFTs uri
        """
        pass


if __name__ == '__main__':
    unittest.main()
