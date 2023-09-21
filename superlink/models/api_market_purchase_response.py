# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.19
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

class ApiMarketPurchaseResponse(BaseModel):
    """
    ApiMarketPurchaseResponse
    """
    checkout_id: Optional[StrictStr] = Field(None, alias="checkoutId")
    stripe_customer_id: Optional[StrictStr] = Field(None, alias="stripeCustomerId")
    stripe_ephemeral_key: Optional[StrictStr] = Field(None, alias="stripeEphemeralKey")
    stripe_payment_intent: Optional[StrictStr] = Field(None, alias="stripePaymentIntent")
    stripe_publishable_key: Optional[StrictStr] = Field(None, alias="stripePublishableKey")
    __properties = ["checkoutId", "stripeCustomerId", "stripeEphemeralKey", "stripePaymentIntent", "stripePublishableKey"]

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
    def from_json(cls, json_str: str) -> ApiMarketPurchaseResponse:
        """Create an instance of ApiMarketPurchaseResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiMarketPurchaseResponse:
        """Create an instance of ApiMarketPurchaseResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiMarketPurchaseResponse.parse_obj(obj)

        _obj = ApiMarketPurchaseResponse.parse_obj({
            "checkout_id": obj.get("checkoutId"),
            "stripe_customer_id": obj.get("stripeCustomerId"),
            "stripe_ephemeral_key": obj.get("stripeEphemeralKey"),
            "stripe_payment_intent": obj.get("stripePaymentIntent"),
            "stripe_publishable_key": obj.get("stripePublishableKey")
        })
        return _obj


