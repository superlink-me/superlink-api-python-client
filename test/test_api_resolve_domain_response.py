# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.1.4-alpha.2
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import superlink
from superlink.models.api_resolve_domain_response import ApiResolveDomainResponse  # noqa: E501
from superlink.rest import ApiException

class TestApiResolveDomainResponse(unittest.TestCase):
    """ApiResolveDomainResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResolveDomainResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiResolveDomainResponse`
        """
        model = superlink.models.api_resolve_domain_response.ApiResolveDomainResponse()  # noqa: E501
        if include_optional :
            return ApiResolveDomainResponse(
                content_hash = '', 
                dns_records = [
                    superlink.models.api/dns_record.api.DNSRecord(
                        name = 'firstname.lastname', 
                        ttl = 3600, 
                        type = 'A', 
                        value = '192.168.0.1', )
                    ], 
                domain = '', 
                provider = '', 
                txt_records = [
                    superlink.models.api/txt_record.api.TXTRecord(
                        key = '', 
                        value = '', )
                    ], 
                wallets = [
                    superlink.models.api/wallet_data.api.WalletData(
                        address = '<wallet address>', 
                        coin = 'BTC', 
                        network = 'mainnet', 
                        tag = 'business', )
                    ]
            )
        else :
            return ApiResolveDomainResponse(
        )
        """

    def testApiResolveDomainResponse(self):
        """Test ApiResolveDomainResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
