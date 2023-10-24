# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.26
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from superlink.models.api_purchase_response import ApiPurchaseResponse  # noqa: E501

class TestApiPurchaseResponse(unittest.TestCase):
    """ApiPurchaseResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiPurchaseResponse:
        """Test ApiPurchaseResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiPurchaseResponse`
        """
        model = ApiPurchaseResponse()  # noqa: E501
        if include_optional:
            return ApiPurchaseResponse(
                currency = 'USD',
                domain = 'firstname.lastname',
                name_service = 'superlink',
                owner_address = '0x1234567890abcdef1234567890abcdef12345678',
                partner_id = '1234567890abcdef1234567890abcdef12345678',
                price = 59.99
            )
        else:
            return ApiPurchaseResponse(
        )
        """

    def testApiPurchaseResponse(self):
        """Test ApiPurchaseResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
