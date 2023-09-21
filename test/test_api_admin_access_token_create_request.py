# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.19
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from superlink.models.api_admin_access_token_create_request import ApiAdminAccessTokenCreateRequest  # noqa: E501

class TestApiAdminAccessTokenCreateRequest(unittest.TestCase):
    """ApiAdminAccessTokenCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiAdminAccessTokenCreateRequest:
        """Test ApiAdminAccessTokenCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAdminAccessTokenCreateRequest`
        """
        model = ApiAdminAccessTokenCreateRequest()  # noqa: E501
        if include_optional:
            return ApiAdminAccessTokenCreateRequest(
                label = 'company-xyz',
                partner_id = '248b8553-effa-4d99-a906-041a54f7df87',
                type = 'ADMIN',
                valid_from = '2023-06-08T00:00:00Z',
                valid_till = '2023-06-15T23:59:59Z'
            )
        else:
            return ApiAdminAccessTokenCreateRequest(
        )
        """

    def testApiAdminAccessTokenCreateRequest(self):
        """Test ApiAdminAccessTokenCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
