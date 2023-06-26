# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.1.6-alpha.2
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import superlink
from superlink.models.api_access_token_response import ApiAccessTokenResponse  # noqa: E501
from superlink.rest import ApiException

class TestApiAccessTokenResponse(unittest.TestCase):
    """ApiAccessTokenResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiAccessTokenResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAccessTokenResponse`
        """
        model = superlink.models.api_access_token_response.ApiAccessTokenResponse()  # noqa: E501
        if include_optional :
            return ApiAccessTokenResponse(
                created_at = '2023-06-08T10:30:00Z', 
                id = '248b8553-effa-4d99-a906-041a54f7df87', 
                label = 'company-xyz', 
                type = 'ADMIN', 
                updated_at = '2023-06-08T15:45:00Z', 
                valid_from = '2023-06-08T00:00:00Z', 
                valid_till = '2023-06-15T23:59:59Z', 
                value = '<JWT>'
            )
        else :
            return ApiAccessTokenResponse(
        )
        """

    def testApiAccessTokenResponse(self):
        """Test ApiAccessTokenResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
