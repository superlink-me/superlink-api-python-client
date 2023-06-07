# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ApiAccessTokenType(str, Enum):
    """
    ApiAccessTokenType
    """

    """
    allowed enum values
    """
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'

    @classmethod
    def from_json(cls, json_str: str) -> ApiAccessTokenType:
        """Create an instance of ApiAccessTokenType from a JSON string"""
        return ApiAccessTokenType(json.loads(json_str))

