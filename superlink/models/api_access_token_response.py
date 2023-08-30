# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.2
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class ApiAccessTokenResponse(BaseModel):
    """
    ApiAccessTokenResponse
    """
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    id: Optional[StrictStr] = None
    label: Optional[StrictStr] = None
    partner_id: Optional[StrictStr] = Field(None, alias="partnerId")
    type: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = Field(None, alias="updatedAt")
    valid_from: Optional[StrictStr] = Field(None, alias="validFrom")
    valid_till: Optional[StrictStr] = Field(None, alias="validTill")
    value: Optional[StrictStr] = None
    __properties = ["createdAt", "id", "label", "partnerId", "type", "updatedAt", "validFrom", "validTill", "value"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ADMIN', 'CUSTOMER'):
            raise ValueError("must be one of enum values ('ADMIN', 'CUSTOMER')")
        return value

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
    def from_json(cls, json_str: str) -> ApiAccessTokenResponse:
        """Create an instance of ApiAccessTokenResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiAccessTokenResponse:
        """Create an instance of ApiAccessTokenResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiAccessTokenResponse.parse_obj(obj)

        _obj = ApiAccessTokenResponse.parse_obj({
            "created_at": obj.get("createdAt"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "partner_id": obj.get("partnerId"),
            "type": obj.get("type"),
            "updated_at": obj.get("updatedAt"),
            "valid_from": obj.get("validFrom"),
            "valid_till": obj.get("validTill"),
            "value": obj.get("value")
        })
        return _obj


