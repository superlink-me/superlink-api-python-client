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

class ApiMarketplaceOrderResponse(BaseModel):
    """
    ApiMarketplaceOrderResponse
    """
    base_currency: Optional[StrictStr] = Field(default=None, alias="baseCurrency")
    base_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="basePrice")
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    currency: Optional[StrictStr] = None
    domain: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    name_service: Optional[StrictStr] = Field(default=None, alias="nameService")
    order_status: Optional[StrictStr] = Field(default=None, alias="orderStatus")
    order_status_reason: Optional[StrictStr] = Field(default=None, alias="orderStatusReason")
    owner_address: Optional[StrictStr] = Field(default=None, alias="ownerAddress")
    payment_reference_id: Optional[StrictStr] = Field(default=None, alias="paymentReferenceId")
    payment_type: Optional[StrictStr] = Field(default=None, alias="paymentType")
    price: Optional[Union[StrictFloat, StrictInt]] = None
    updated_at: Optional[StrictStr] = Field(default=None, alias="updatedAt")
    __properties: ClassVar[List[str]] = ["baseCurrency", "basePrice", "createdAt", "currency", "domain", "id", "nameService", "orderStatus", "orderStatusReason", "ownerAddress", "paymentReferenceId", "paymentType", "price", "updatedAt"]

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
        """Create an instance of ApiMarketplaceOrderResponse from a JSON string"""
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
        """Create an instance of ApiMarketplaceOrderResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "baseCurrency": obj.get("baseCurrency"),
            "basePrice": obj.get("basePrice"),
            "createdAt": obj.get("createdAt"),
            "currency": obj.get("currency"),
            "domain": obj.get("domain"),
            "id": obj.get("id"),
            "nameService": obj.get("nameService"),
            "orderStatus": obj.get("orderStatus"),
            "orderStatusReason": obj.get("orderStatusReason"),
            "ownerAddress": obj.get("ownerAddress"),
            "paymentReferenceId": obj.get("paymentReferenceId"),
            "paymentType": obj.get("paymentType"),
            "price": obj.get("price"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


