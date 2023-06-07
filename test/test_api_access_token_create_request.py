# coding: utf-8

"""
    Superlink API

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import SuperlinkAPI
from SuperlinkAPI.models.api_access_token_create_request import ApiAccessTokenCreateRequest  # noqa: E501
from SuperlinkAPI.rest import ApiException

class TestApiAccessTokenCreateRequest(unittest.TestCase):
    """ApiAccessTokenCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiAccessTokenCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAccessTokenCreateRequest`
        """
        model = SuperlinkAPI.models.api_access_token_create_request.ApiAccessTokenCreateRequest()  # noqa: E501
        if include_optional :
            return ApiAccessTokenCreateRequest(
                label = '', 
                type = '', 
                valid_from = '', 
                valid_till = ''
            )
        else :
            return ApiAccessTokenCreateRequest(
        )
        """

    def testApiAccessTokenCreateRequest(self):
        """Test ApiAccessTokenCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
