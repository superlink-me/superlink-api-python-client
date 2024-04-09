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

from superlink.models.api_parent_domain_validation_response import ApiParentDomainValidationResponse

class TestApiParentDomainValidationResponse(unittest.TestCase):
    """ApiParentDomainValidationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiParentDomainValidationResponse:
        """Test ApiParentDomainValidationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiParentDomainValidationResponse`
        """
        model = ApiParentDomainValidationResponse()
        if include_optional:
            return ApiParentDomainValidationResponse(
                parent_domain = 'test.eth',
                reason = 'Parent incorrectly configured: no ENS text record configured',
                status = True
            )
        else:
            return ApiParentDomainValidationResponse(
        )
        """

    def testApiParentDomainValidationResponse(self):
        """Test ApiParentDomainValidationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
