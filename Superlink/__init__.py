# coding: utf-8

# flake8: noqa

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.2
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "1.0.0"

# import apis into sdk package
from Superlink.api.access_token_api import AccessTokenApi
from Superlink.api.health_api import HealthApi
from Superlink.api.resolution_api import ResolutionApi

# import ApiClient
from Superlink.api_response import ApiResponse
from Superlink.api_client import ApiClient
from Superlink.configuration import Configuration
from Superlink.exceptions import OpenApiException
from Superlink.exceptions import ApiTypeError
from Superlink.exceptions import ApiValueError
from Superlink.exceptions import ApiKeyError
from Superlink.exceptions import ApiAttributeError
from Superlink.exceptions import ApiException

# import models into sdk package
from Superlink.models.api_access_token_create_request import ApiAccessTokenCreateRequest
from Superlink.models.api_access_token_delete_request import ApiAccessTokenDeleteRequest
from Superlink.models.api_access_token_response import ApiAccessTokenResponse
from Superlink.models.api_bad_request_response import ApiBadRequestResponse
from Superlink.models.api_dns_record import ApiDNSRecord
from Superlink.models.api_error_response import ApiErrorResponse
from Superlink.models.api_internal_server_error_response import ApiInternalServerErrorResponse
from Superlink.models.api_resolve_wallet_address_by_domain_response import ApiResolveWalletAddressByDomainResponse
from Superlink.models.data_access_token_type import DataAccessTokenType
