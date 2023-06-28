# coding: utf-8

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.1.13
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from superlink.models.api_dns_record import ApiDNSRecord
from superlink.models.api_name_service import ApiNameService
from superlink.models.api_txt_record import ApiTXTRecord
from superlink.models.api_wallet_data import ApiWalletData

class ApiResolveDomainResponse(BaseModel):
    """
    ApiResolveDomainResponse
    """
    content_hash: Optional[StrictStr] = Field(None, alias="contentHash")
    dns_records: Optional[conlist(ApiDNSRecord)] = Field(None, alias="dnsRecords")
    domain: Optional[StrictStr] = None
    name_service: Optional[ApiNameService] = Field(None, alias="nameService")
    txt_records: Optional[conlist(ApiTXTRecord)] = Field(None, alias="txtRecords")
    wallets: Optional[conlist(ApiWalletData)] = None
    __properties = ["contentHash", "dnsRecords", "domain", "nameService", "txtRecords", "wallets"]

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
    def from_json(cls, json_str: str) -> ApiResolveDomainResponse:
        """Create an instance of ApiResolveDomainResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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
    def from_dict(cls, obj: dict) -> ApiResolveDomainResponse:
        """Create an instance of ApiResolveDomainResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiResolveDomainResponse.parse_obj(obj)

        _obj = ApiResolveDomainResponse.parse_obj({
            "content_hash": obj.get("contentHash"),
            "dns_records": [ApiDNSRecord.from_dict(_item) for _item in obj.get("dnsRecords")] if obj.get("dnsRecords") is not None else None,
            "domain": obj.get("domain"),
            "name_service": obj.get("nameService"),
            "txt_records": [ApiTXTRecord.from_dict(_item) for _item in obj.get("txtRecords")] if obj.get("txtRecords") is not None else None,
            "wallets": [ApiWalletData.from_dict(_item) for _item in obj.get("wallets")] if obj.get("wallets") is not None else None
        })
        return _obj

