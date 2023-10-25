# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.29
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_call, ValidationError
from typing import Dict, List, Optional, Tuple

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictStr, field_validator

from typing import List, Optional

from superlink.models.api_resolve_domain_response import ApiResolveDomainResponse

from superlink.api_client import ApiClient
from superlink.api_response import ApiResponse
from superlink.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ResolutionApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def resolve_data_by_address(
        self,
        address: Annotated[StrictStr, Field(description="0x1234561234556")],
        nameservice: Annotated[Optional[StrictStr], Field(description="superlink")] = None,
        **kwargs,
    ) -> ApiResolveDomainResponse:
        """Resolves wallets and DNS records for an address  # noqa: E501

        resolve domain data by address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.resolve_data_by_address(address, nameservice, async_req=True)
        >>> result = thread.get()

        :param address: 0x1234561234556 (required)
        :type address: str
        :param nameservice: superlink
        :type nameservice: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiResolveDomainResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the resolve_data_by_address_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return self.resolve_data_by_address_with_http_info.raw_function(
            address,
            nameservice,
            **kwargs,
        )

    @validate_call
    def resolve_data_by_address_with_http_info(
        self,
        address: Annotated[StrictStr, Field(description="0x1234561234556")],
        nameservice: Annotated[Optional[StrictStr], Field(description="superlink")] = None,
        **kwargs,
    ) -> ApiResponse:
        """Resolves wallets and DNS records for an address  # noqa: E501

        resolve domain data by address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.resolve_data_by_address_with_http_info(address, nameservice, async_req=True)
        >>> result = thread.get()

        :param address: 0x1234561234556 (required)
        :type address: str
        :param nameservice: superlink
        :type nameservice: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ApiResolveDomainResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'address',
            'nameservice'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resolve_data_by_address" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['address'] is not None:
            _path_params['address'] = _params['address']


        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get('nameservice') is not None:  # noqa: E501
            _query_params.append(('nameservice', _params['nameservice']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = ['BearerAuth']  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiResolveDomainResponse",
            '404': "ApiErrorResponse",
            '500': "ApiInternalServerErrorResponse",
        }

        return self.api_client.call_api(
            '/v1/reverse/{address}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_call
    def resolve_data_by_domain(
        self,
        domain: Annotated[StrictStr, Field(description="firstname.lastname")],
        nameservices: Annotated[Optional[List[StrictStr]], Field(description="superlink,ens,ud")] = None,
        coins: Annotated[Optional[List[StrictStr]], Field(description="BTC,ETH,MATIC")] = None,
        **kwargs,
    ) -> ApiResolveDomainResponse:
        """Resolves wallets and DNS records for a domain  # noqa: E501

        resolve domain data by domain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.resolve_data_by_domain(domain, nameservices, coins, async_req=True)
        >>> result = thread.get()

        :param domain: firstname.lastname (required)
        :type domain: str
        :param nameservices: superlink,ens,ud
        :type nameservices: List[str]
        :param coins: BTC,ETH,MATIC
        :type coins: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiResolveDomainResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the resolve_data_by_domain_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return self.resolve_data_by_domain_with_http_info.raw_function(
            domain,
            nameservices,
            coins,
            **kwargs,
        )

    @validate_call
    def resolve_data_by_domain_with_http_info(
        self,
        domain: Annotated[StrictStr, Field(description="firstname.lastname")],
        nameservices: Annotated[Optional[List[StrictStr]], Field(description="superlink,ens,ud")] = None,
        coins: Annotated[Optional[List[StrictStr]], Field(description="BTC,ETH,MATIC")] = None,
        **kwargs,
    ) -> ApiResponse:
        """Resolves wallets and DNS records for a domain  # noqa: E501

        resolve domain data by domain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.resolve_data_by_domain_with_http_info(domain, nameservices, coins, async_req=True)
        >>> result = thread.get()

        :param domain: firstname.lastname (required)
        :type domain: str
        :param nameservices: superlink,ens,ud
        :type nameservices: List[str]
        :param coins: BTC,ETH,MATIC
        :type coins: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ApiResolveDomainResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'domain',
            'nameservices',
            'coins'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resolve_data_by_domain" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['domain'] is not None:
            _path_params['domain'] = _params['domain']


        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get('nameservices') is not None:  # noqa: E501
            _query_params.append(('nameservices', _params['nameservices']))
            _collection_formats['nameservices'] = 'csv'

        if _params.get('coins') is not None:  # noqa: E501
            _query_params.append(('coins', _params['coins']))
            _collection_formats['coins'] = 'csv'

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = ['BearerAuth']  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiResolveDomainResponse",
            '400': "ApiErrorResponse",
            '404': "ApiErrorResponse",
            '500': "ApiInternalServerErrorResponse",
        }

        return self.api_client.call_api(
            '/v1/resolve/{domain}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
