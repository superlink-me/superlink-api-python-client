# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.1.17
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import superlink
from superlink.api.nft_api import NftApi  # noqa: E501
from superlink.rest import ApiException


class TestNftApi(unittest.TestCase):
    """NftApi unit test stubs"""

    def setUp(self):
        self.api = superlink.api.nft_api.NftApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_token_image_by_domain(self):
        """Test case for get_token_image_by_domain

        Returns a SVG image for a Superlink NFT  # noqa: E501
        """
        pass

    def test_get_token_metadata_by_domain(self):
        """Test case for get_token_metadata_by_domain

        Returns metadata usually associated with NFTs uri  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
