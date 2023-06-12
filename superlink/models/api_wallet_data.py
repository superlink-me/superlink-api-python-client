# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.1.4-alpha.1
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr
from superlink.models.api_coin import ApiCoin

class ApiWalletData(BaseModel):
    """
    ApiWalletData
    """
    address: Optional[StrictStr] = None
    coin: Optional[ApiCoin] = None
    network: Optional[StrictStr] = None
    tag: Optional[StrictStr] = None
    __properties = ["address", "coin", "network", "tag"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiWalletData:
        """Create an instance of ApiWalletData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiWalletData:
        """Create an instance of ApiWalletData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiWalletData.parse_obj(obj)

        _obj = ApiWalletData.parse_obj({
            "address": obj.get("address"),
            "coin": obj.get("coin"),
            "network": obj.get("network"),
            "tag": obj.get("tag")
        })
        return _obj

