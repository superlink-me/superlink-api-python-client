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

from superlink.models.api_address_record import ApiAddressRecord

class TestApiAddressRecord(unittest.TestCase):
    """ApiAddressRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiAddressRecord:
        """Test ApiAddressRecord
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAddressRecord`
        """
        model = ApiAddressRecord()
        if include_optional:
            return ApiAddressRecord(
                addr = '0x1234567890abcdef1234567890abcdef12345678',
                coin_id = 60
            )
        else:
            return ApiAddressRecord(
        )
        """

    def testApiAddressRecord(self):
        """Test ApiAddressRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
