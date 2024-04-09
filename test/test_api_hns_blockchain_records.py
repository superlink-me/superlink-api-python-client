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

from superlink.models.api_hns_blockchain_records import ApiHNSBlockchainRecords

class TestApiHNSBlockchainRecords(unittest.TestCase):
    """ApiHNSBlockchainRecords unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiHNSBlockchainRecords:
        """Test ApiHNSBlockchainRecords
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiHNSBlockchainRecords`
        """
        model = ApiHNSBlockchainRecords()
        if include_optional:
            return ApiHNSBlockchainRecords(
                a = '1.2.3.4',
                ds1 = '64385959c14e13c10600e82ae0e203e5c7c317a4',
                ds2 = '0ead833907382ecfbe7134dc3ded40befe91f4d59a9c8bf3247b6a390b678bbb',
                ds4 = '4ef86f59cc6a0aaa9658a293871b6ca1ba93b2b60853949a9cbc79b10101b3572b3e3537974fda3d8b038bc42ed3f649'
            )
        else:
            return ApiHNSBlockchainRecords(
        )
        """

    def testApiHNSBlockchainRecords(self):
        """Test ApiHNSBlockchainRecords"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()