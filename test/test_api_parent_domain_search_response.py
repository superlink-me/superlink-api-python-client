# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.4.2
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from superlink.models.api_parent_domain_search_response import ApiParentDomainSearchResponse

class TestApiParentDomainSearchResponse(unittest.TestCase):
    """ApiParentDomainSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiParentDomainSearchResponse:
        """Test ApiParentDomainSearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiParentDomainSearchResponse`
        """
        model = ApiParentDomainSearchResponse()
        if include_optional:
            return ApiParentDomainSearchResponse(
                available_parent_domain = [
                    ''
                    ]
            )
        else:
            return ApiParentDomainSearchResponse(
        )
        """

    def testApiParentDomainSearchResponse(self):
        """Test ApiParentDomainSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
