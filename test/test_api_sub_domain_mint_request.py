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

from superlink.models.api_sub_domain_mint_request import ApiSubDomainMintRequest

class TestApiSubDomainMintRequest(unittest.TestCase):
    """ApiSubDomainMintRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiSubDomainMintRequest:
        """Test ApiSubDomainMintRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiSubDomainMintRequest`
        """
        model = ApiSubDomainMintRequest()
        if include_optional:
            return ApiSubDomainMintRequest(
                name_data = superlink.models.api/sub_domain_name_data.api.SubDomainNameData(
                    addresses = {
                        'key' : ''
                        }, 
                    contenthash = '0xe301017012204edd2984eeaf3ddf50bac238ec95c5713fb40b5e428b508fdbe55d3b9f155ffe', 
                    text = {
                        'key' : ''
                        }, )
            )
        else:
            return ApiSubDomainMintRequest(
        )
        """

    def testApiSubDomainMintRequest(self):
        """Test ApiSubDomainMintRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()