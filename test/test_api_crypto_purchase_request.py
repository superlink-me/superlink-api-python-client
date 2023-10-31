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
import datetime

from superlink.models.api_crypto_purchase_request import ApiCryptoPurchaseRequest

class TestApiCryptoPurchaseRequest(unittest.TestCase):
    """ApiCryptoPurchaseRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiCryptoPurchaseRequest:
        """Test ApiCryptoPurchaseRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiCryptoPurchaseRequest`
        """
        model = ApiCryptoPurchaseRequest()
        if include_optional:
            return ApiCryptoPurchaseRequest(
                currency = 'ETH',
                demo = False,
                domain = 'firstname.lastname',
                owner_address = '0x1234567890abcdef1234567890abcdef12345678',
                owner_email = 'nora@gmail.com',
                years = 1
            )
        else:
            return ApiCryptoPurchaseRequest(
        )
        """

    def testApiCryptoPurchaseRequest(self):
        """Test ApiCryptoPurchaseRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
