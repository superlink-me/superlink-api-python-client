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

from superlink.models.api_domain_metadata_attribute import ApiDomainMetadataAttribute  # noqa: E501

class TestApiDomainMetadataAttribute(unittest.TestCase):
    """ApiDomainMetadataAttribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiDomainMetadataAttribute:
        """Test ApiDomainMetadataAttribute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiDomainMetadataAttribute`
        """
        model = ApiDomainMetadataAttribute()  # noqa: E501
        if include_optional:
            return ApiDomainMetadataAttribute(
                trait_type = '',
                value = None
            )
        else:
            return ApiDomainMetadataAttribute(
        )
        """

    def testApiDomainMetadataAttribute(self):
        """Test ApiDomainMetadataAttribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
