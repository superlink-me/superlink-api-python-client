# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.27
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
from superlink.models.api_access_token_create_request import ApiAccessTokenCreateRequest
from superlink.models.api_access_token_delete_request import ApiAccessTokenDeleteRequest
from superlink.models.api_access_token_response import ApiAccessTokenResponse
from superlink.models.api_purchase_list_response import ApiPurchaseListResponse

from superlink.api_client import ApiClient
from superlink.api_response import ApiResponse
from superlink.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PartnerApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def create_access_token(
        self,
        request: Annotated[ApiAccessTokenCreateRequest, Field(description="access token create request")],
        **kwargs,
    ) -> ApiAccessTokenResponse:
        """Creates an admin token for a partner  # noqa: E501

        Creates an admin token for a partner  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_access_token(request, async_req=True)
        >>> result = thread.get()

        :param request: access token create request (required)
        :type request: ApiAccessTokenCreateRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiAccessTokenResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_access_token_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return self.create_access_token_with_http_info.raw_function(
            request,
            **kwargs,
        )

    @validate_call
    def create_access_token_with_http_info(
        self,
        request: Annotated[ApiAccessTokenCreateRequest, Field(description="access token create request")],
        **kwargs,
    ) -> ApiResponse:
        """Creates an admin token for a partner  # noqa: E501

        Creates an admin token for a partner  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_access_token_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param request: access token create request (required)
        :type request: ApiAccessTokenCreateRequest
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
        :rtype: tuple(ApiAccessTokenResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'request'
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
                    " to method create_access_token" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        if _params['request'] is not None:
            _body_params = _params['request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings: List[str] = ['BearerAuth']  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiAccessTokenResponse",
            '400': "ApiBadRequestResponse",
            '500': "ApiInternalServerErrorResponse",
        }

        return self.api_client.call_api(
            '/v1/partner/access-token', 'POST',
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
    def delete_access_token(
        self,
        request: Annotated[ApiAccessTokenDeleteRequest, Field(description="access token delete request")],
        **kwargs,
    ) -> None:
        """Deletes an access token  # noqa: E501

        Deletes an access token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_access_token(request, async_req=True)
        >>> result = thread.get()

        :param request: access token delete request (required)
        :type request: ApiAccessTokenDeleteRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the delete_access_token_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return self.delete_access_token_with_http_info.raw_function(
            request,
            **kwargs,
        )

    @validate_call
    def delete_access_token_with_http_info(
        self,
        request: Annotated[ApiAccessTokenDeleteRequest, Field(description="access token delete request")],
        **kwargs,
    ) -> ApiResponse:
        """Deletes an access token  # noqa: E501

        Deletes an access token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_access_token_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param request: access token delete request (required)
        :type request: ApiAccessTokenDeleteRequest
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'request'
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
                    " to method delete_access_token" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        if _params['request'] is not None:
            _body_params = _params['request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = ['BearerAuth']  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {}

        return self.api_client.call_api(
            '/v1/partner/access-token', 'DELETE',
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
    def list_access_tokens(
        self,
        **kwargs,
    ) -> ApiAccessTokenResponse:
        """Lists access tokens for a partner  # noqa: E501

        Lists access tokens for a partner  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_access_tokens(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiAccessTokenResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_access_tokens_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return self.list_access_tokens_with_http_info.raw_function(
            **kwargs,
        )

    @validate_call
    def list_access_tokens_with_http_info(
        self,
        **kwargs,
    ) -> ApiResponse:
        """Lists access tokens for a partner  # noqa: E501

        Lists access tokens for a partner  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_access_tokens_with_http_info(async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(ApiAccessTokenResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method list_access_tokens" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
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
            '200': "ApiAccessTokenResponse",
            '500': "ApiInternalServerErrorResponse",
        }

        return self.api_client.call_api(
            '/v1/partner/access-token', 'GET',
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
    def partner_purchases(
        self,
        **kwargs,
    ) -> ApiPurchaseListResponse:
        """Returns a list of all purchases  # noqa: E501

        Returns a list of all purchases  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.partner_purchases(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiPurchaseListResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the partner_purchases_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return self.partner_purchases_with_http_info.raw_function(
            **kwargs,
        )

    @validate_call
    def partner_purchases_with_http_info(
        self,
        **kwargs,
    ) -> ApiResponse:
        """Returns a list of all purchases  # noqa: E501

        Returns a list of all purchases  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.partner_purchases_with_http_info(async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(ApiPurchaseListResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method partner_purchases" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
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
            '200': "ApiPurchaseListResponse",
            '500': "ApiInternalServerErrorResponse",
        }

        return self.api_client.call_api(
            '/v1/partner/purchases', 'GET',
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
