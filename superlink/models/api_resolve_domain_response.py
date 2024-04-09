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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from superlink.models.api_dns_record import ApiDNSRecord
from superlink.models.api_name_service import ApiNameService
from superlink.models.api_txt_record import ApiTXTRecord
from superlink.models.api_wallet_data import ApiWalletData
from typing import Optional, Set
from typing_extensions import Self

class ApiResolveDomainResponse(BaseModel):
    """
    ApiResolveDomainResponse
    """ # noqa: E501
    content_hash: Optional[StrictStr] = Field(default=None, alias="contentHash")
    dns_records: Optional[List[ApiDNSRecord]] = Field(default=None, alias="dnsRecords")
    domain: Optional[StrictStr] = None
    name_service: Optional[ApiNameService] = Field(default=None, alias="nameService")
    owner_address: Optional[StrictStr] = Field(default=None, alias="ownerAddress")
    txt_records: Optional[List[ApiTXTRecord]] = Field(default=None, alias="txtRecords")
    wallets: Optional[List[ApiWalletData]] = None
    __properties: ClassVar[List[str]] = ["contentHash", "dnsRecords", "domain", "nameService", "ownerAddress", "txtRecords", "wallets"]

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
        """Create an instance of ApiResolveDomainResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dns_records (list)
        _items = []
        if self.dns_records:
            for _item in self.dns_records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dnsRecords'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in txt_records (list)
        _items = []
        if self.txt_records:
            for _item in self.txt_records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['txtRecords'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in wallets (list)
        _items = []
        if self.wallets:
            for _item in self.wallets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['wallets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiResolveDomainResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contentHash": obj.get("contentHash"),
            "dnsRecords": [ApiDNSRecord.from_dict(_item) for _item in obj["dnsRecords"]] if obj.get("dnsRecords") is not None else None,
            "domain": obj.get("domain"),
            "nameService": obj.get("nameService"),
            "ownerAddress": obj.get("ownerAddress"),
            "txtRecords": [ApiTXTRecord.from_dict(_item) for _item in obj["txtRecords"]] if obj.get("txtRecords") is not None else None,
            "wallets": [ApiWalletData.from_dict(_item) for _item in obj["wallets"]] if obj.get("wallets") is not None else None
        })
        return _obj


