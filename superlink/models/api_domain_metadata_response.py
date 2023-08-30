# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.4
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from superlink.models.api_domain_metadata_attribute import ApiDomainMetadataAttribute

class ApiDomainMetadataResponse(BaseModel):
    """
    ApiDomainMetadataResponse
    """
    animation_url: Optional[StrictStr] = None
    attributes: Optional[conlist(ApiDomainMetadataAttribute)] = None
    avatar: Optional[StrictStr] = None
    background_color: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    external_url: Optional[StrictStr] = None
    image: Optional[StrictStr] = None
    image_url: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    namehash: Optional[StrictStr] = None
    token_id: Optional[StrictStr] = Field(None, alias="tokenId")
    __properties = ["animation_url", "attributes", "avatar", "background_color", "description", "external_url", "image", "image_url", "name", "namehash", "tokenId"]

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
    def from_json(cls, json_str: str) -> ApiDomainMetadataResponse:
        """Create an instance of ApiDomainMetadataResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiDomainMetadataResponse:
        """Create an instance of ApiDomainMetadataResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiDomainMetadataResponse.parse_obj(obj)

        _obj = ApiDomainMetadataResponse.parse_obj({
            "animation_url": obj.get("animation_url"),
            "attributes": [ApiDomainMetadataAttribute.from_dict(_item) for _item in obj.get("attributes")] if obj.get("attributes") is not None else None,
            "avatar": obj.get("avatar"),
            "background_color": obj.get("background_color"),
            "description": obj.get("description"),
            "external_url": obj.get("external_url"),
            "image": obj.get("image"),
            "image_url": obj.get("image_url"),
            "name": obj.get("name"),
            "namehash": obj.get("namehash"),
            "token_id": obj.get("tokenId")
        })
        return _obj


