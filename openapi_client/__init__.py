# coding: utf-8

# flake8: noqa

"""
    Superlink

    API for Superlink  # noqa: E501

    The version of the OpenAPI document: v0.0.2-alpha.1
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "v0.0.2-alpha.1"

# import apis into sdk package
from openapi_client.api.access_token_api import AccessTokenApi
from openapi_client.api.health_api import HealthApi
from openapi_client.api.resolution_api import ResolutionApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.api_access_token_create_request import ApiAccessTokenCreateRequest
from openapi_client.models.api_access_token_delete_request import ApiAccessTokenDeleteRequest
from openapi_client.models.api_access_token_response import ApiAccessTokenResponse
from openapi_client.models.api_bad_request_response import ApiBadRequestResponse
from openapi_client.models.api_coin import ApiCoin
from openapi_client.models.api_dns_record import ApiDNSRecord
from openapi_client.models.api_error_response import ApiErrorResponse
from openapi_client.models.api_internal_server_error_response import ApiInternalServerErrorResponse
from openapi_client.models.api_resolve_wallet_address_by_domain_response import ApiResolveWalletAddressByDomainResponse
from openapi_client.models.api_wallet_data import ApiWalletData
from openapi_client.models.data_access_token_type import DataAccessTokenType