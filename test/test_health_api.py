# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import openapi_client
from openapi_client.api.health_api import HealthApi  # noqa: E501
from openapi_client.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.health_api.HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_check(self):
        """Test case for health_check

        Checks the health of the API  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
