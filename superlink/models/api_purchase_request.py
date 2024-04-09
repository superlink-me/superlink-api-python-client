# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.5.0
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from superlink.models.api_address_record import ApiAddressRecord
from typing import Optional, Set
from typing_extensions import Self

class ApiPurchaseRequest(BaseModel):
    """
    ApiPurchaseRequest
    """ # noqa: E501
    checkout_id: Optional[StrictStr] = Field(default=None, alias="checkoutId")
    domain: Optional[StrictStr] = None
    external_user_id: Optional[StrictStr] = Field(default=None, alias="externalUserId")
    owner_address: Optional[StrictStr] = Field(default=None, alias="ownerAddress")
    partner_id: Optional[StrictStr] = Field(default=None, alias="partnerId")
    stripe_connected_account_id: Optional[StrictStr] = Field(default=None, alias="stripeConnectedAccountId")
    wallet_addrs: Optional[List[ApiAddressRecord]] = Field(default=None, alias="walletAddrs")
    years: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["checkoutId", "domain", "externalUserId", "ownerAddress", "partnerId", "stripeConnectedAccountId", "walletAddrs", "years"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiPurchaseRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in wallet_addrs (list)
        _items = []
        if self.wallet_addrs:
            for _item in self.wallet_addrs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['walletAddrs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiPurchaseRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "checkoutId": obj.get("checkoutId"),
            "domain": obj.get("domain"),
            "externalUserId": obj.get("externalUserId"),
            "ownerAddress": obj.get("ownerAddress"),
            "partnerId": obj.get("partnerId"),
            "stripeConnectedAccountId": obj.get("stripeConnectedAccountId"),
            "walletAddrs": [ApiAddressRecord.from_dict(_item) for _item in obj["walletAddrs"]] if obj.get("walletAddrs") is not None else None,
            "years": obj.get("years")
        })
        return _obj


