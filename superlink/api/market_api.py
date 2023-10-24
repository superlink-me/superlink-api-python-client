# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.26
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
from pydantic import StrictStr

from typing import Optional

from superlink.models.api_crypto_purchase_request import ApiCryptoPurchaseRequest
from superlink.models.api_market_crypto_estimation_response import ApiMarketCryptoEstimationResponse
from superlink.models.api_market_crypto_purchase_response import ApiMarketCryptoPurchaseResponse
from superlink.models.api_market_purchase_response import ApiMarketPurchaseResponse
from superlink.models.api_market_search_response import ApiMarketSearchResponse
from superlink.models.api_marketplace_order_response import ApiMarketplaceOrderResponse
from superlink.models.api_purchase_request import ApiPurchaseRequest

from superlink.api_client import ApiClient
from superlink.api_response import ApiResponse
from superlink.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class MarketApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def market_crypto_estimate(
        self,
        basecurrency: Annotated[Optional[Annotated[str, Field(min_length=2, strict=True, max_length=4)]], Field(description="string valid")] = None,
        **kwargs,
    ) -> ApiMarketCryptoEstimationResponse:
        """CryptoEstimate returns the estimated conversion rates for supported crypto payment options  # noqa: E501

        CryptoEstimate returns the estimated conversion rates for supported crypto payment options  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.market_crypto_estimate(basecurrency, async_req=True)
        >>> result = thread.get()

        :param basecurrency: string valid
        :type basecurrency: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiMarketCryptoEstimationResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the market_crypto_estimate_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return self.market_crypto_estimate_with_http_info.raw_function(
            basecurrency,
            **kwargs,
        )

    @validate_call
    def market_crypto_estimate_with_http_info(
        self,
        basecurrency: Annotated[Optional[Annotated[str, Field(min_length=2, strict=True, max_length=4)]], Field(description="string valid")] = None,
        **kwargs,
    ) -> ApiResponse:
        """CryptoEstimate returns the estimated conversion rates for supported crypto payment options  # noqa: E501

        CryptoEstimate returns the estimated conversion rates for supported crypto payment options  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.market_crypto_estimate_with_http_info(basecurrency, async_req=True)
        >>> result = thread.get()

        :param basecurrency: string valid
        :type basecurrency: str
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
        :rtype: tuple(ApiMarketCryptoEstimationResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'basecurrency'
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
                    " to method market_crypto_estimate" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get('basecurrency') is not None:  # noqa: E501
            _query_params.append(('basecurrency', _params['basecurrency']))

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
            '200': "ApiMarketCryptoEstimationResponse",
            '500': "ApiInternalServerErrorResponse",
        }

        return self.api_client.call_api(
            '/v1/market/crypto/estimate', 'GET',
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
    def market_crypto_purchase(
        self,
        request: Annotated[ApiCryptoPurchaseRequest, Field(description="crypto purchase request")],
        **kwargs,
    ) -> ApiMarketCryptoPurchaseResponse:
        """CryptoPurchase returns the payment details required for crypto payment  # noqa: E501

        CryptoPurchase returns the payment details required for crypto payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.market_crypto_purchase(request, async_req=True)
        >>> result = thread.get()

        :param request: crypto purchase request (required)
        :type request: ApiCryptoPurchaseRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiMarketCryptoPurchaseResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the market_crypto_purchase_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return self.market_crypto_purchase_with_http_info.raw_function(
            request,
            **kwargs,
        )

    @validate_call
    def market_crypto_purchase_with_http_info(
        self,
        request: Annotated[ApiCryptoPurchaseRequest, Field(description="crypto purchase request")],
        **kwargs,
    ) -> ApiResponse:
        """CryptoPurchase returns the payment details required for crypto payment  # noqa: E501

        CryptoPurchase returns the payment details required for crypto payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.market_crypto_purchase_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param request: crypto purchase request (required)
        :type request: ApiCryptoPurchaseRequest
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
        :rtype: tuple(ApiMarketCryptoPurchaseResponse, status_code(int), headers(HTTPHeaderDict))
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
                    " to method market_crypto_purchase" % _key
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
            '200': "ApiMarketCryptoPurchaseResponse",
            '500': "ApiInternalServerErrorResponse",
        }

        return self.api_client.call_api(
            '/v1/market/crypto/purchase', 'POST',
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
    def market_order(
        self,
        order_id: Annotated[StrictStr, Field(description="92456d2b-c315-4b2b-b234-c674490b7324")],
        **kwargs,
    ) -> ApiMarketplaceOrderResponse:
        """Returns order information  # noqa: E501

        Returns order information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.market_order(order_id, async_req=True)
        >>> result = thread.get()

        :param order_id: 92456d2b-c315-4b2b-b234-c674490b7324 (required)
        :type order_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiMarketplaceOrderResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the market_order_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return self.market_order_with_http_info.raw_function(
            order_id,
            **kwargs,
        )

    @validate_call
    def market_order_with_http_info(
        self,
        order_id: Annotated[StrictStr, Field(description="92456d2b-c315-4b2b-b234-c674490b7324")],
        **kwargs,
    ) -> ApiResponse:
        """Returns order information  # noqa: E501

        Returns order information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.market_order_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param order_id: 92456d2b-c315-4b2b-b234-c674490b7324 (required)
        :type order_id: str
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
        :rtype: tuple(ApiMarketplaceOrderResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'order_id'
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
                    " to method market_order" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['order_id'] is not None:
            _path_params['orderID'] = _params['order_id']


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
            '200': "ApiMarketplaceOrderResponse",
            '500': "ApiInternalServerErrorResponse",
        }

        return self.api_client.call_api(
            '/v1/market/order/{orderID}', 'GET',
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
    def market_purchase(
        self,
        request: Annotated[ApiPurchaseRequest, Field(description="purchase request")],
        **kwargs,
    ) -> ApiMarketPurchaseResponse:
        """Purchase returns the payment details required by Stripe  # noqa: E501

        Purchase returns the payment details required by Stripe  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.market_purchase(request, async_req=True)
        >>> result = thread.get()

        :param request: purchase request (required)
        :type request: ApiPurchaseRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiMarketPurchaseResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the market_purchase_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return self.market_purchase_with_http_info.raw_function(
            request,
            **kwargs,
        )

    @validate_call
    def market_purchase_with_http_info(
        self,
        request: Annotated[ApiPurchaseRequest, Field(description="purchase request")],
        **kwargs,
    ) -> ApiResponse:
        """Purchase returns the payment details required by Stripe  # noqa: E501

        Purchase returns the payment details required by Stripe  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.market_purchase_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param request: purchase request (required)
        :type request: ApiPurchaseRequest
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
        :rtype: tuple(ApiMarketPurchaseResponse, status_code(int), headers(HTTPHeaderDict))
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
                    " to method market_purchase" % _key
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
            '200': "ApiMarketPurchaseResponse",
            '500': "ApiInternalServerErrorResponse",
        }

        return self.api_client.call_api(
            '/v1/market/purchase', 'POST',
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
    def market_search(
        self,
        query: Annotated[StrictStr, Field(description="johndoe")],
        **kwargs,
    ) -> ApiMarketSearchResponse:
        """Returns market listings  # noqa: E501

        Returns market listings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.market_search(query, async_req=True)
        >>> result = thread.get()

        :param query: johndoe (required)
        :type query: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiMarketSearchResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the market_search_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return self.market_search_with_http_info.raw_function(
            query,
            **kwargs,
        )

    @validate_call
    def market_search_with_http_info(
        self,
        query: Annotated[StrictStr, Field(description="johndoe")],
        **kwargs,
    ) -> ApiResponse:
        """Returns market listings  # noqa: E501

        Returns market listings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.market_search_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param query: johndoe (required)
        :type query: str
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
        :rtype: tuple(ApiMarketSearchResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'query'
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
                    " to method market_search" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['query'] is not None:
            _path_params['query'] = _params['query']


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
            '200': "ApiMarketSearchResponse",
            '500': "ApiInternalServerErrorResponse",
        }

        return self.api_client.call_api(
            '/v1/market/search/{query}', 'GET',
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
