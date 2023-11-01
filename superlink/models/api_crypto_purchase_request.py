# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.32
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApiCryptoPurchaseRequest(BaseModel):
    """
    ApiCryptoPurchaseRequest
    """ # noqa: E501
    currency: Optional[StrictStr] = None
    demo: Optional[StrictBool] = None
    domain: Optional[StrictStr] = None
    owner_address: Optional[StrictStr] = Field(default=None, alias="ownerAddress")
    owner_email: Optional[StrictStr] = Field(default=None, alias="ownerEmail")
    owner_name: Optional[StrictStr] = Field(default=None, alias="ownerName")
    years: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["currency", "demo", "domain", "ownerAddress", "ownerEmail", "ownerName", "years"]

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
        """Create an instance of ApiCryptoPurchaseRequest from a JSON string"""
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
        """Create an instance of ApiCryptoPurchaseRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currency": obj.get("currency"),
            "demo": obj.get("demo"),
            "domain": obj.get("domain"),
            "ownerAddress": obj.get("ownerAddress"),
            "ownerEmail": obj.get("ownerEmail"),
            "ownerName": obj.get("ownerName"),
            "years": obj.get("years")
        })
        return _obj


