# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.16
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class ApiPurchaseRequest(BaseModel):
    """
    ApiPurchaseRequest
    """
    checkout_id: Optional[StrictStr] = Field(None, alias="checkoutId")
    demo: Optional[StrictBool] = None
    domain: Optional[StrictStr] = None
    external_user_id: Optional[StrictStr] = Field(None, alias="externalUserId")
    owner_address: Optional[StrictStr] = Field(None, alias="ownerAddress")
    stripe_connected_account_id: Optional[StrictStr] = Field(None, alias="stripeConnectedAccountId")
    years: Optional[StrictInt] = None
    __properties = ["checkoutId", "demo", "domain", "externalUserId", "ownerAddress", "stripeConnectedAccountId", "years"]

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
    def from_json(cls, json_str: str) -> ApiPurchaseRequest:
        """Create an instance of ApiPurchaseRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiPurchaseRequest:
        """Create an instance of ApiPurchaseRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiPurchaseRequest.parse_obj(obj)

        _obj = ApiPurchaseRequest.parse_obj({
            "checkout_id": obj.get("checkoutId"),
            "demo": obj.get("demo"),
            "domain": obj.get("domain"),
            "external_user_id": obj.get("externalUserId"),
            "owner_address": obj.get("ownerAddress"),
            "stripe_connected_account_id": obj.get("stripeConnectedAccountId"),
            "years": obj.get("years")
        })
        return _obj


