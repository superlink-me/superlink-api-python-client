# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.33
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApiAccessTokenResponse(BaseModel):
    """
    ApiAccessTokenResponse
    """ # noqa: E501
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    id: Optional[StrictStr] = None
    label: Optional[StrictStr] = None
    partner_id: Optional[StrictStr] = Field(default=None, alias="partnerId")
    type: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = Field(default=None, alias="updatedAt")
    valid_from: Optional[StrictStr] = Field(default=None, alias="validFrom")
    valid_till: Optional[StrictStr] = Field(default=None, alias="validTill")
    value: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["createdAt", "id", "label", "partnerId", "type", "updatedAt", "validFrom", "validTill", "value"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ADMIN', 'CUSTOMER'):
            raise ValueError("must be one of enum values ('ADMIN', 'CUSTOMER')")
        return value

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
        """Create an instance of ApiAccessTokenResponse from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApiAccessTokenResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdAt": obj.get("createdAt"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "partnerId": obj.get("partnerId"),
            "type": obj.get("type"),
            "updatedAt": obj.get("updatedAt"),
            "validFrom": obj.get("validFrom"),
            "validTill": obj.get("validTill"),
            "value": obj.get("value")
        })
        return _obj


