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

from superlink.models.api_market_listing import ApiMarketListing

class TestApiMarketListing(unittest.TestCase):
    """ApiMarketListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiMarketListing:
        """Test ApiMarketListing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiMarketListing`
        """
        model = ApiMarketListing()
        if include_optional:
            return ApiMarketListing(
                currency = 'USD',
                domain = 'firstname.lastname',
                features = [["email", "userId", "web3"]],
                name_service = 'superlink',
                price = {
                    'key' : 1.337
                    }
            )
        else:
            return ApiMarketListing(
        )
        """

    def testApiMarketListing(self):
        """Test ApiMarketListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
