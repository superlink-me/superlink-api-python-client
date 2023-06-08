# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.0.2-alpha.1
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import openapi_client
from openapi_client.models.api_resolve_wallet_address_by_domain_response import ApiResolveWalletAddressByDomainResponse  # noqa: E501
from openapi_client.rest import ApiException

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
        model = openapi_client.models.api_resolve_wallet_address_by_domain_response.ApiResolveWalletAddressByDomainResponse()  # noqa: E501
        if include_optional :
            return ApiResolveWalletAddressByDomainResponse(
                domain = 'firstname.lastname', 
                records = [
                    openapi_client.models.api/dns_record.api.DNSRecord(
                        name = 'firstname.lastname', 
                        ttl = 3600, 
                        type = 'A', 
                        value = '192.168.0.1', )
                    ], 
                wallets = [
                    openapi_client.models.api/wallet_data.api.WalletData(
                        address = '<wallet address>', 
                        coin = 'BTC', 
                        network = 'mainnet', 
                        tag = 'business', )
                    ]
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
