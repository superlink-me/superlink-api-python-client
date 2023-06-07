# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.5
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import superlink
from superlink.models.api_resolve_wallet_address_by_domain_response import ApiResolveWalletAddressByDomainResponse  # noqa: E501
from superlink.rest import ApiException

class TestApiResolveWalletAddressByDomainResponse(unittest.TestCase):
    """ApiResolveWalletAddressByDomainResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResolveWalletAddressByDomainResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiResolveWalletAddressByDomainResponse`
        """
        model = superlink.models.api_resolve_wallet_address_by_domain_response.ApiResolveWalletAddressByDomainResponse()  # noqa: E501
        if include_optional :
            return ApiResolveWalletAddressByDomainResponse(
                domain = '', 
                records = [
                    superlink.models.api/dns_record.api.DNSRecord(
                        name = '', 
                        ttl = 56, 
                        type = '', 
                        value = '', )
                    ], 
                wallets = {
                    'key' : ''
                    }
            )
        else :
            return ApiResolveWalletAddressByDomainResponse(
        )
        """

    def testApiResolveWalletAddressByDomainResponse(self):
        """Test ApiResolveWalletAddressByDomainResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
