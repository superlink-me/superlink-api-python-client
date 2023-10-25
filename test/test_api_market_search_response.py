# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.29
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from superlink.models.api_market_search_response import ApiMarketSearchResponse  # noqa: E501

class TestApiMarketSearchResponse(unittest.TestCase):
    """ApiMarketSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiMarketSearchResponse:
        """Test ApiMarketSearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiMarketSearchResponse`
        """
        model = ApiMarketSearchResponse()  # noqa: E501
        if include_optional:
            return ApiMarketSearchResponse(
                market_listings = [
                    superlink.models.api/market_listing.api.MarketListing(
                        currency = 'USD', 
                        domain = 'firstname.lastname', 
                        features = [["email", "userId", "web3"]], 
                        name_service = 'superlink', 
                        price = {
                            'key' : 1.337
                            }, )
                    ]
            )
        else:
            return ApiMarketSearchResponse(
        )
        """

    def testApiMarketSearchResponse(self):
        """Test ApiMarketSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
