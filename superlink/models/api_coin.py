# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.1.4
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ApiCoin(str, Enum):
    """
    ApiCoin
    """

    """
    allowed enum values
    """
    BTC = 'BTC'
    ETH = 'ETH'
    XRP = 'XRP'

    @classmethod
    def from_json(cls, json_str: str) -> ApiCoin:
        """Create an instance of ApiCoin from a JSON string"""
        return ApiCoin(json.loads(json_str))


