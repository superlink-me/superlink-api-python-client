# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.4.1
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from superlink.models.api_sub_domain_mint_with_sig_request import ApiSubDomainMintWithSigRequest

class TestApiSubDomainMintWithSigRequest(unittest.TestCase):
    """ApiSubDomainMintWithSigRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiSubDomainMintWithSigRequest:
        """Test ApiSubDomainMintWithSigRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiSubDomainMintWithSigRequest`
        """
        model = ApiSubDomainMintWithSigRequest()
        if include_optional:
            return ApiSubDomainMintWithSigRequest(
                message = '0x1234567890abcdef1234567890abcdef12345678',
                name_data = superlink.models.api/sub_domain_name_data.api.SubDomainNameData(
                    addresses = {
                        'key' : ''
                        }, 
                    contenthash = '0xe301017012204edd2984eeaf3ddf50bac238ec95c5713fb40b5e428b508fdbe55d3b9f155ffe', 
                    text = {
                        'key' : ''
                        }, ),
                signed_message = '0x1234567890abcdef1234567890abcdef12345678'
            )
        else:
            return ApiSubDomainMintWithSigRequest(
        )
        """

    def testApiSubDomainMintWithSigRequest(self):
        """Test ApiSubDomainMintWithSigRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
