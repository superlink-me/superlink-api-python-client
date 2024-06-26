# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.5.0
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from superlink.models.api_partner_response import ApiPartnerResponse

class TestApiPartnerResponse(unittest.TestCase):
    """ApiPartnerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiPartnerResponse:
        """Test ApiPartnerResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiPartnerResponse`
        """
        model = ApiPartnerResponse()
        if include_optional:
            return ApiPartnerResponse(
                created_at = '2023-06-08T10:30:00Z',
                id = '248b8553-effa-4d99-a906-041a54f7df87',
                name = 'company-xyz',
                updated_at = '2023-06-08T15:45:00Z'
            )
        else:
            return ApiPartnerResponse(
        )
        """

    def testApiPartnerResponse(self):
        """Test ApiPartnerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
