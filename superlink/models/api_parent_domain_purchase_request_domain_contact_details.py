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
from typing import Optional, Set
from typing_extensions import Self

class ApiParentDomainPurchaseRequestDomainContactDetails(BaseModel):
    """
    ApiParentDomainPurchaseRequestDomainContactDetails
    """ # noqa: E501
    address1: Optional[StrictStr] = None
    address2: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    name_first: Optional[StrictStr] = Field(default=None, alias="nameFirst")
    name_last: Optional[StrictStr] = Field(default=None, alias="nameLast")
    phone_country_code: Optional[StrictStr] = Field(default=None, alias="phoneCountryCode")
    phone_number: Optional[StrictStr] = Field(default=None, alias="phoneNumber")
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    state: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["address1", "address2", "city", "country", "email", "nameFirst", "nameLast", "phoneCountryCode", "phoneNumber", "postalCode", "state"]

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
        """Create an instance of ApiParentDomainPurchaseRequestDomainContactDetails from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiParentDomainPurchaseRequestDomainContactDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address1": obj.get("address1"),
            "address2": obj.get("address2"),
            "city": obj.get("city"),
            "country": obj.get("country"),
            "email": obj.get("email"),
            "nameFirst": obj.get("nameFirst"),
            "nameLast": obj.get("nameLast"),
            "phoneCountryCode": obj.get("phoneCountryCode"),
            "phoneNumber": obj.get("phoneNumber"),
            "postalCode": obj.get("postalCode"),
            "state": obj.get("state")
        })
        return _obj


