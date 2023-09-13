# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.12
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class ApiPartnerResponse(BaseModel):
    """
    ApiPartnerResponse
    """
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = Field(None, alias="updatedAt")
    __properties = ["createdAt", "id", "name", "updatedAt"]

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
    def from_json(cls, json_str: str) -> ApiPartnerResponse:
        """Create an instance of ApiPartnerResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiPartnerResponse:
        """Create an instance of ApiPartnerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiPartnerResponse.parse_obj(obj)

        _obj = ApiPartnerResponse.parse_obj({
            "created_at": obj.get("createdAt"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


