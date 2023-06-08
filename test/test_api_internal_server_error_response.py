# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.0.5
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import openapi_client
from openapi_client.models.api_internal_server_error_response import ApiInternalServerErrorResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestApiInternalServerErrorResponse(unittest.TestCase):
    """ApiInternalServerErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiInternalServerErrorResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiInternalServerErrorResponse`
        """
        model = openapi_client.models.api_internal_server_error_response.ApiInternalServerErrorResponse()  # noqa: E501
        if include_optional :
            return ApiInternalServerErrorResponse(
                message = 'Internal server error'
            )
        else :
            return ApiInternalServerErrorResponse(
        )
        """

    def testApiInternalServerErrorResponse(self):
        """Test ApiInternalServerErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
