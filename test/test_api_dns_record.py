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
from superlink.models.api_dns_record import ApiDNSRecord  # noqa: E501
from superlink.rest import ApiException

class TestApiDNSRecord(unittest.TestCase):
    """ApiDNSRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiDNSRecord
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiDNSRecord`
        """
        model = superlink.models.api_dns_record.ApiDNSRecord()  # noqa: E501
        if include_optional :
            return ApiDNSRecord(
                name = '', 
                ttl = 56, 
                type = '', 
                value = ''
            )
        else :
            return ApiDNSRecord(
        )
        """

    def testApiDNSRecord(self):
        """Test ApiDNSRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
