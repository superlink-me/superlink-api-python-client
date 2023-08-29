# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.0
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ApiNameService(str, Enum):
    """
    ApiNameService
    """

    """
    allowed enum values
    """
    UD = 'ud'
    ENS = 'ens'
    SUPERLINK = 'superlink'

    @classmethod
    def from_json(cls, json_str: str) -> ApiNameService:
        """Create an instance of ApiNameService from a JSON string"""
        return ApiNameService(json.loads(json_str))


