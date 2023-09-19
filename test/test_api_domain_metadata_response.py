# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.15
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from superlink.models.api_domain_metadata_response import ApiDomainMetadataResponse  # noqa: E501

class TestApiDomainMetadataResponse(unittest.TestCase):
    """ApiDomainMetadataResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiDomainMetadataResponse:
        """Test ApiDomainMetadataResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiDomainMetadataResponse`
        """
        model = ApiDomainMetadataResponse()  # noqa: E501
        if include_optional:
            return ApiDomainMetadataResponse(
                animation_url = 'https://superlink.me/animation?name=jon.johnson',
                attributes = [
                    superlink.models.api/domain_metadata_attribute.api.DomainMetadataAttribute(
                        trait_type = '', 
                        value = superlink.models.value.value(), )
                    ],
                avatar = 'https://assets.superlink.me/avatar/b94c22d4-02b4-464e-aead-3f6cafceb1db',
                background_color = 'FFFFFF',
                description = 'A blockchain domain. Use it to resolve your cryptocurrency addresses and decentralized websites.',
                external_url = 'https://superlink.me/animation?name=jon.johnson',
                image = 'https://api.superlink.me/card-image/jon.johnson.svg',
                image_url = 'https://api.superlink.me/card-image/jon.johnson.svg',
                name = 'jon.johnson',
                namehash = '0x3538e2ebd840880e82448521324fc0c308fc6cd576a65a532a51c8d60c32b58a',
                token_id = '24073090563576551262032245933984978621011965102670616730489196997318148273546'
            )
        else:
            return ApiDomainMetadataResponse(
        )
        """

    def testApiDomainMetadataResponse(self):
        """Test ApiDomainMetadataResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
