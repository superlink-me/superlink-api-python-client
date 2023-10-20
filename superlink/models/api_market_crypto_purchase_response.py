# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.22
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApiMarketCryptoPurchaseResponse(BaseModel):
    """
    ApiMarketCryptoPurchaseResponse
    """
    address: Optional[StrictStr] = None
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="PaymentDetails     CryptoPaymentDetails `json:\"paymentDetails\"`")
    expiry_date_epoch: Optional[StrictInt] = Field(default=None, alias="expiryDateEpoch")
    order_id: Optional[StrictStr] = Field(default=None, alias="orderID")
    payment_id: Optional[StrictStr] = Field(default=None, alias="paymentId")
    protocol: Optional[StrictStr] = None
    uri: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["address", "amount", "expiryDateEpoch", "orderID", "paymentId", "protocol", "uri"]

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
        """Create an instance of ApiMarketCryptoPurchaseResponse from a JSON string"""
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
        """Create an instance of ApiMarketCryptoPurchaseResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "amount": obj.get("amount"),
            "expiryDateEpoch": obj.get("expiryDateEpoch"),
            "orderID": obj.get("orderID"),
            "paymentId": obj.get("paymentId"),
            "protocol": obj.get("protocol"),
            "uri": obj.get("uri")
        })
        return _obj


