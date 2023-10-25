# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.27
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApiMarketPurchaseResponse(BaseModel):
    """
    ApiMarketPurchaseResponse
    """
    checkout_id: Optional[StrictStr] = Field(default=None, alias="checkoutId")
    order_id: Optional[StrictStr] = Field(default=None, alias="orderId")
    stripe_customer_id: Optional[StrictStr] = Field(default=None, alias="stripeCustomerId")
    stripe_ephemeral_key: Optional[StrictStr] = Field(default=None, alias="stripeEphemeralKey")
    stripe_payment_intent: Optional[StrictStr] = Field(default=None, alias="stripePaymentIntent")
    stripe_publishable_key: Optional[StrictStr] = Field(default=None, alias="stripePublishableKey")
    __properties: ClassVar[List[str]] = ["checkoutId", "orderId", "stripeCustomerId", "stripeEphemeralKey", "stripePaymentIntent", "stripePublishableKey"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApiMarketPurchaseResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of ApiMarketPurchaseResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "checkoutId": obj.get("checkoutId"),
            "orderId": obj.get("orderId"),
            "stripeCustomerId": obj.get("stripeCustomerId"),
            "stripeEphemeralKey": obj.get("stripeEphemeralKey"),
            "stripePaymentIntent": obj.get("stripePaymentIntent"),
            "stripePublishableKey": obj.get("stripePublishableKey")
        })
        return _obj


