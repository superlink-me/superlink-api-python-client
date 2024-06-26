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

from superlink.models.api_marketplace_order_response import ApiMarketplaceOrderResponse

class TestApiMarketplaceOrderResponse(unittest.TestCase):
    """ApiMarketplaceOrderResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiMarketplaceOrderResponse:
        """Test ApiMarketplaceOrderResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiMarketplaceOrderResponse`
        """
        model = ApiMarketplaceOrderResponse()
        if include_optional:
            return ApiMarketplaceOrderResponse(
                base_currency = 'USD',
                base_price = 15.0,
                created_at = '2023-06-08T10:30:00Z',
                currency = 'ETH',
                domain = 'noramiller.eth',
                id = '92456d2b-c315-4b2b-b234-c674490b7324',
                name_service = 'ens',
                order_status = 'PENDING',
                order_status_reason = 'Waiting for transaction',
                owner_address = '0x4c0f4c2ad123be4256784e9475fa243b5f6ccab4',
                payment_reference_id = '92456d2b-c315-4b2b-b234-c674490b7324',
                payment_type = 'crypto',
                price = 0.001,
                updated_at = '2024-01-02T11:20:00Z'
            )
        else:
            return ApiMarketplaceOrderResponse(
        )
        """

    def testApiMarketplaceOrderResponse(self):
        """Test ApiMarketplaceOrderResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
