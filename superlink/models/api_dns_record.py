# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.11
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr

class ApiDNSRecord(BaseModel):
    """
    ApiDNSRecord
    """
    name: Optional[StrictStr] = None
    ttl: Optional[StrictInt] = None
    type: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
    __properties = ["name", "ttl", "type", "value"]

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
    def from_json(cls, json_str: str) -> ApiDNSRecord:
        """Create an instance of ApiDNSRecord from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiDNSRecord:
        """Create an instance of ApiDNSRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiDNSRecord.parse_obj(obj)

        _obj = ApiDNSRecord.parse_obj({
            "name": obj.get("name"),
            "ttl": obj.get("ttl"),
            "type": obj.get("type"),
            "value": obj.get("value")
        })
        return _obj


