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

from superlink.models.api_hns_domain_available_response import ApiHNSDomainAvailableResponse

class TestApiHNSDomainAvailableResponse(unittest.TestCase):
    """ApiHNSDomainAvailableResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiHNSDomainAvailableResponse:
        """Test ApiHNSDomainAvailableResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiHNSDomainAvailableResponse`
        """
        model = ApiHNSDomainAvailableResponse()
        if include_optional:
            return ApiHNSDomainAvailableResponse(
                domain = 'test1.test',
                status = 'available'
            )
        else:
            return ApiHNSDomainAvailableResponse(
        )
        """

    def testApiHNSDomainAvailableResponse(self):
        """Test ApiHNSDomainAvailableResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
