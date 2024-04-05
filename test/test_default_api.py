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

from superlink.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_health_check(self) -> None:
        """Test case for health_check

        Checks the health of the API
        """
        pass


if __name__ == '__main__':
    unittest.main()
