# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.1.18
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import superlink
from superlink.models.api_domain_metadata_attribute import ApiDomainMetadataAttribute  # noqa: E501
from superlink.rest import ApiException

class TestApiDomainMetadataAttribute(unittest.TestCase):
    """ApiDomainMetadataAttribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiDomainMetadataAttribute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiDomainMetadataAttribute`
        """
        model = superlink.models.api_domain_metadata_attribute.ApiDomainMetadataAttribute()  # noqa: E501
        if include_optional :
            return ApiDomainMetadataAttribute(
                trait_type = '', 
                value = None
            )
        else :
            return ApiDomainMetadataAttribute(
        )
        """

    def testApiDomainMetadataAttribute(self):
        """Test ApiDomainMetadataAttribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
