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
from SuperlinkAPI.models.api_response_bad_request import ApiResponseBadRequest  # noqa: E501
from SuperlinkAPI.rest import ApiException

class TestApiResponseBadRequest(unittest.TestCase):
    """ApiResponseBadRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseBadRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiResponseBadRequest`
        """
        model = SuperlinkAPI.models.api_response_bad_request.ApiResponseBadRequest()  # noqa: E501
        if include_optional :
            return ApiResponseBadRequest(
                errors = [
                    SuperlinkAPI.models.api/response_error.api.ResponseError(
                        field = '', 
                        info = '', )
                    ]
            )
        else :
            return ApiResponseBadRequest(
        )
        """

    def testApiResponseBadRequest(self):
        """Test ApiResponseBadRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
