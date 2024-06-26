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

from superlink.models.api_market_crypto_purchase_response import ApiMarketCryptoPurchaseResponse

class TestApiMarketCryptoPurchaseResponse(unittest.TestCase):
    """ApiMarketCryptoPurchaseResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiMarketCryptoPurchaseResponse:
        """Test ApiMarketCryptoPurchaseResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiMarketCryptoPurchaseResponse`
        """
        model = ApiMarketCryptoPurchaseResponse()
        if include_optional:
            return ApiMarketCryptoPurchaseResponse(
                address = '0xA5D70E12348Fef6A123EBD1231b123c51235E321',
                amount = 0.001,
                expiry_date_epoch = 1697009575596,
                order_id = '92456d2b-c315-4b2b-b234-c674490b7324',
                payment_id = 'fa13ba20-da1d-426f-a0e4-f7629caae626',
                protocol = 'ETH',
                uri = 'ethereum:0x4c0f4c2ad289be425e034e9475fa243b5f6ccab4?value=1.349965E+16'
            )
        else:
            return ApiMarketCryptoPurchaseResponse(
        )
        """

    def testApiMarketCryptoPurchaseResponse(self):
        """Test ApiMarketCryptoPurchaseResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
