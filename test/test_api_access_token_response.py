# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.8
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from superlink.models.api_access_token_response import ApiAccessTokenResponse  # noqa: E501

class TestApiAccessTokenResponse(unittest.TestCase):
    """ApiAccessTokenResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiAccessTokenResponse:
        """Test ApiAccessTokenResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAccessTokenResponse`
        """
        model = ApiAccessTokenResponse()  # noqa: E501
        if include_optional:
            return ApiAccessTokenResponse(
                created_at = '2023-06-08T10:30:00Z',
                id = '248b8553-effa-4d99-a906-041a54f7df87',
                label = 'company-xyz',
                partner_id = '328b8553-effa-4d99-a906-041a54f7df87',
                type = 'ADMIN',
                updated_at = '2023-06-08T15:45:00Z',
                valid_from = '2023-06-08T00:00:00Z',
                valid_till = '2023-06-15T23:59:59Z',
                value = '<JWT>'
            )
        else:
            return ApiAccessTokenResponse(
        )
        """

    def testApiAccessTokenResponse(self):
        """Test ApiAccessTokenResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
