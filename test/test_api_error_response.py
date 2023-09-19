# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.14
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from superlink.models.api_error_response import ApiErrorResponse  # noqa: E501

class TestApiErrorResponse(unittest.TestCase):
    """ApiErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiErrorResponse:
        """Test ApiErrorResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiErrorResponse`
        """
        model = ApiErrorResponse()  # noqa: E501
        if include_optional:
            return ApiErrorResponse(
                field = 'field',
                info = 'error message'
            )
        else:
            return ApiErrorResponse(
        )
        """

    def testApiErrorResponse(self):
        """Test ApiErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
