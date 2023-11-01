# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.32
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from superlink.models.api_access_token_create_request import ApiAccessTokenCreateRequest

class TestApiAccessTokenCreateRequest(unittest.TestCase):
    """ApiAccessTokenCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiAccessTokenCreateRequest:
        """Test ApiAccessTokenCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAccessTokenCreateRequest`
        """
        model = ApiAccessTokenCreateRequest()
        if include_optional:
            return ApiAccessTokenCreateRequest(
                label = 'company-xyz',
                valid_from = '2023-06-08T00:00:00Z',
                valid_till = '2023-06-15T23:59:59Z'
            )
        else:
            return ApiAccessTokenCreateRequest(
        )
        """

    def testApiAccessTokenCreateRequest(self):
        """Test ApiAccessTokenCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
