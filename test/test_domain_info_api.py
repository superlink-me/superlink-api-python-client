# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.4.1
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from superlink.api.domain_info_api import DomainInfoApi


class TestDomainInfoApi(unittest.TestCase):
    """DomainInfoApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DomainInfoApi()

    def tearDown(self) -> None:
        pass

    def test_get_all_domains(self) -> None:
        """Test case for get_all_domains

        Returns all the domains owned by a given ownerAddress
        """
        pass


if __name__ == '__main__':
    unittest.main()
