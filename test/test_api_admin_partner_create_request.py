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

from superlink.models.api_admin_partner_create_request import ApiAdminPartnerCreateRequest

class TestApiAdminPartnerCreateRequest(unittest.TestCase):
    """ApiAdminPartnerCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiAdminPartnerCreateRequest:
        """Test ApiAdminPartnerCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAdminPartnerCreateRequest`
        """
        model = ApiAdminPartnerCreateRequest()
        if include_optional:
            return ApiAdminPartnerCreateRequest(
                name = 'company-xyz'
            )
        else:
            return ApiAdminPartnerCreateRequest(
        )
        """

    def testApiAdminPartnerCreateRequest(self):
        """Test ApiAdminPartnerCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
