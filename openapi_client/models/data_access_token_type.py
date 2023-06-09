# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.1.1
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class DataAccessTokenType(str, Enum):
    """
    DataAccessTokenType
    """

    """
    allowed enum values
    """
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'

    @classmethod
    def from_json(cls, json_str: str) -> DataAccessTokenType:
        """Create an instance of DataAccessTokenType from a JSON string"""
        return DataAccessTokenType(json.loads(json_str))


