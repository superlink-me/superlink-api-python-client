# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.25
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DataAccessTokenType from a JSON string"""
        return cls(json.loads(json_str))


