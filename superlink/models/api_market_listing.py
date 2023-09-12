# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.9
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class ApiMarketListing(BaseModel):
    """
    ApiMarketListing
    """
    currency: Optional[StrictStr] = None
    domain: Optional[StrictStr] = None
    name_service: Optional[StrictStr] = Field(None, alias="nameService")
    price: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = None
    __properties = ["currency", "domain", "nameService", "price"]

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
    def from_json(cls, json_str: str) -> ApiMarketListing:
        """Create an instance of ApiMarketListing from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiMarketListing:
        """Create an instance of ApiMarketListing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiMarketListing.parse_obj(obj)

        _obj = ApiMarketListing.parse_obj({
            "currency": obj.get("currency"),
            "domain": obj.get("domain"),
            "name_service": obj.get("nameService"),
            "price": obj.get("price")
        })
        return _obj


