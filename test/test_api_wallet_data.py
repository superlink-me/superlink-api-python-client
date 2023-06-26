# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.1.6-alpha.3
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import superlink
from superlink.models.api_wallet_data import ApiWalletData  # noqa: E501
from superlink.rest import ApiException

class TestApiWalletData(unittest.TestCase):
    """ApiWalletData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiWalletData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiWalletData`
        """
        model = superlink.models.api_wallet_data.ApiWalletData()  # noqa: E501
        if include_optional :
            return ApiWalletData(
                address = '<wallet address>', 
                coin = 'BTC', 
                version = 'ERC20'
            )
        else :
            return ApiWalletData(
        )
        """

    def testApiWalletData(self):
        """Test ApiWalletData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
