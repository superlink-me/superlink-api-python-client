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

from superlink.models.api_sub_domain_per_day_response import ApiSubDomainPerDayResponse

class TestApiSubDomainPerDayResponse(unittest.TestCase):
    """ApiSubDomainPerDayResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiSubDomainPerDayResponse:
        """Test ApiSubDomainPerDayResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiSubDomainPerDayResponse`
        """
        model = ApiSubDomainPerDayResponse()
        if include_optional:
            return ApiSubDomainPerDayResponse(
                aggregates = [
                    superlink.models.api/sub_domain_per_day_count.api.SubDomainPerDayCount(
                        count = 28, 
                        date = '2024-01-01', )
                    ],
                next_pagination_token = 'KCJuYW1lIjoiYWJjLmRlZi5naGkiLCJkYXRlIjoiMjAyMS0xMS0xMSIp',
                total = 128
            )
        else:
            return ApiSubDomainPerDayResponse(
        )
        """

    def testApiSubDomainPerDayResponse(self):
        """Test ApiSubDomainPerDayResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()