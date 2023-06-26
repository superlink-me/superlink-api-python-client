# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.1.6-alpha.4
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

class ApiTXTRecord(BaseModel):
    """
    ApiTXTRecord
    """
    key: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
    __properties = ["key", "value"]

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
    def from_json(cls, json_str: str) -> ApiTXTRecord:
        """Create an instance of ApiTXTRecord from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiTXTRecord:
        """Create an instance of ApiTXTRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiTXTRecord.parse_obj(obj)

        _obj = ApiTXTRecord.parse_obj({
            "key": obj.get("key"),
            "value": obj.get("value")
        })
        return _obj
