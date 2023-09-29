# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.21
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from superlink.models.api_purchase_request import ApiPurchaseRequest  # noqa: E501

class TestApiPurchaseRequest(unittest.TestCase):
    """ApiPurchaseRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiPurchaseRequest:
        """Test ApiPurchaseRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiPurchaseRequest`
        """
        model = ApiPurchaseRequest()  # noqa: E501
        if include_optional:
            return ApiPurchaseRequest(
                checkout_id = '92353d2b-c3f5-4b3b-b214-c34b490b7324',
                demo = False,
                domain = 'firstname.lastname',
                external_user_id = '248b8553-effa-4d99-a906-041a54f7df87',
                owner_address = '0x1234567890abcdef1234567890abcdef12345678',
                stripe_connected_account_id = 'acct_1J1Z2X2Y2Z2X2Y2Z',
                years = 1
            )
        else:
            return ApiPurchaseRequest(
        )
        """

    def testApiPurchaseRequest(self):
        """Test ApiPurchaseRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
