# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.13
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from superlink.models.api_access_token_delete_request import ApiAccessTokenDeleteRequest  # noqa: E501

class TestApiAccessTokenDeleteRequest(unittest.TestCase):
    """ApiAccessTokenDeleteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiAccessTokenDeleteRequest:
        """Test ApiAccessTokenDeleteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAccessTokenDeleteRequest`
        """
        model = ApiAccessTokenDeleteRequest()  # noqa: E501
        if include_optional:
            return ApiAccessTokenDeleteRequest(
                id = '248b8553-effa-4d99-a906-041a54f7df87'
            )
        else:
            return ApiAccessTokenDeleteRequest(
        )
        """

    def testApiAccessTokenDeleteRequest(self):
        """Test ApiAccessTokenDeleteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
