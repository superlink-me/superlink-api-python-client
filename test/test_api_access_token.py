# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import SuperlinkAPI
from SuperlinkAPI.models.api_access_token import ApiAccessToken  # noqa: E501
from SuperlinkAPI.rest import ApiException

class TestApiAccessToken(unittest.TestCase):
    """ApiAccessToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiAccessToken
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAccessToken`
        """
        model = SuperlinkAPI.models.api_access_token.ApiAccessToken()  # noqa: E501
        if include_optional :
            return ApiAccessToken(
                created_at = '', 
                id = '', 
                label = '', 
                type = 'ADMIN', 
                updated_at = '', 
                valid_from = '', 
                valid_till = '', 
                value = ''
            )
        else :
            return ApiAccessToken(
        )
        """

    def testApiAccessToken(self):
        """Test ApiAccessToken"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
