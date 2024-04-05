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

from superlink.models.api_wallet_message_response import ApiWalletMessageResponse

class TestApiWalletMessageResponse(unittest.TestCase):
    """ApiWalletMessageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiWalletMessageResponse:
        """Test ApiWalletMessageResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiWalletMessageResponse`
        """
        model = ApiWalletMessageResponse()
        if include_optional:
            return ApiWalletMessageResponse(
                message = 'Sign this message for authorization to log in to superlink
OwnerAddress: 0xA5D70E12348Fef6A123EBD1231b123c51235E321
CreationTime: 2006-01-02T15:04:05-0700
ExpiryTime: 2006-01-02T15:04:05-0700
UniqueSignature: KCJuYW1lIjoiYWJjLmRlZi5naGkiLCJkYXRlIjoiMjAyMS0xMS0xMSIp'
            )
        else:
            return ApiWalletMessageResponse(
        )
        """

    def testApiWalletMessageResponse(self):
        """Test ApiWalletMessageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
