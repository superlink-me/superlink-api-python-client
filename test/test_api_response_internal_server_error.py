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

import Superlink
from Superlink.models.api_response_internal_server_error import ApiResponseInternalServerError  # noqa: E501
from Superlink.rest import ApiException

class TestApiResponseInternalServerError(unittest.TestCase):
    """ApiResponseInternalServerError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseInternalServerError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiResponseInternalServerError`
        """
        model = Superlink.models.api_response_internal_server_error.ApiResponseInternalServerError()  # noqa: E501
        if include_optional :
            return ApiResponseInternalServerError(
                message = ''
            )
        else :
            return ApiResponseInternalServerError(
        )
        """

    def testApiResponseInternalServerError(self):
        """Test ApiResponseInternalServerError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()