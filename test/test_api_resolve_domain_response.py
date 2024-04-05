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

from superlink.models.api_resolve_domain_response import ApiResolveDomainResponse

class TestApiResolveDomainResponse(unittest.TestCase):
    """ApiResolveDomainResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiResolveDomainResponse:
        """Test ApiResolveDomainResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiResolveDomainResponse`
        """
        model = ApiResolveDomainResponse()
        if include_optional:
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
                name_service = 'ud',
                owner_address = '',
                txt_records = [
                    superlink.models.api/txt_record.api.TXTRecord(
                        key = '', 
                        value = '', )
                    ],
                wallets = [
                    superlink.models.api/wallet_data.api.WalletData(
                        address = '<wallet address>', 
                        coin = 'BTC', 
                        version = 'ERC20', )
                    ]
            )
        else:
            return ApiResolveDomainResponse(
        )
        """

    def testApiResolveDomainResponse(self):
        """Test ApiResolveDomainResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
