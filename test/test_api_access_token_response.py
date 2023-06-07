# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.2
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import Superlink
from Superlink.models.api_access_token_response import ApiAccessTokenResponse  # noqa: E501
from Superlink.rest import ApiException

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
        model = Superlink.models.api_access_token_response.ApiAccessTokenResponse()  # noqa: E501
        if include_optional :
            return ApiAccessTokenResponse(
                created_at = '', 
                id = '', 
                label = '', 
                type = '', 
                updated_at = '', 
                valid_from = '', 
                valid_till = '', 
                value = ''
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
