# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.1.7
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import superlink
from superlink.api.default_api import DefaultApi  # noqa: E501
from superlink.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = superlink.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_check(self):
        """Test case for health_check

        Checks the health of the API  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
