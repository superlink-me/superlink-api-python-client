# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: dev
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from Superlink.models.data_access_token_type import DataAccessTokenType

class ApiAccessTokenCreateRequest(BaseModel):
    """
    ApiAccessTokenCreateRequest
    """
    label: Optional[StrictStr] = None
    type: Optional[DataAccessTokenType] = None
    valid_from: Optional[StrictStr] = Field(None, alias="validFrom")
    valid_till: Optional[StrictStr] = Field(None, alias="validTill")
    __properties = ["label", "type", "validFrom", "validTill"]

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
    def from_json(cls, json_str: str) -> ApiAccessTokenCreateRequest:
        """Create an instance of ApiAccessTokenCreateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiAccessTokenCreateRequest:
        """Create an instance of ApiAccessTokenCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiAccessTokenCreateRequest.parse_obj(obj)

        _obj = ApiAccessTokenCreateRequest.parse_obj({
            "label": obj.get("label"),
            "type": obj.get("type"),
            "valid_from": obj.get("validFrom"),
            "valid_till": obj.get("validTill")
        })
        return _obj

