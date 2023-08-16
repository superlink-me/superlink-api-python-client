# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.2.2
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import superlink
from superlink.models.api_set_reverse_address_request import ApiSetReverseAddressRequest  # noqa: E501
from superlink.rest import ApiException

class TestApiSetReverseAddressRequest(unittest.TestCase):
    """ApiSetReverseAddressRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiSetReverseAddressRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiSetReverseAddressRequest`
        """
        model = superlink.models.api_set_reverse_address_request.ApiSetReverseAddressRequest()  # noqa: E501
        if include_optional :
            return ApiSetReverseAddressRequest(
                address = '0x1234567890abcdef1234567890abcdef12345678', 
                domain = 'firstname.lastname', 
                signed_message = '0x1234567890abcdef1234567890abcdef12345678', 
                user_id = '248b8553-effa-4d99-a906-041a54f7df87'
            )
        else :
            return ApiSetReverseAddressRequest(
        )
        """

    def testApiSetReverseAddressRequest(self):
        """Test ApiSetReverseAddressRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
