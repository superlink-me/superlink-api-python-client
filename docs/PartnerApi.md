# superlink.PartnerApi

All URIs are relative to *https://api.superlink.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_token**](PartnerApi.md#create_access_token) | **POST** /v1/partner/access-token | Creates an admin token for a partner
[**delete_access_token**](PartnerApi.md#delete_access_token) | **DELETE** /v1/partner/access-token | Deletes an access token
[**list_access_tokens**](PartnerApi.md#list_access_tokens) | **GET** /v1/partner/access-token | Lists access tokens for a partner
[**partner_purchases**](PartnerApi.md#partner_purchases) | **GET** /v1/partner/purchases | Returns a list of all purchases


# **create_access_token**
> ApiAccessTokenResponse create_access_token(request)

Creates an admin token for a partner

Creates an admin token for a partner

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_access_token_create_request import ApiAccessTokenCreateRequest
from superlink.models.api_access_token_response import ApiAccessTokenResponse
from superlink.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.superlink.me
# See configuration.py for a list of all supported configuration parameters.
configuration = superlink.Configuration(
    host = "https://api.superlink.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with superlink.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = superlink.PartnerApi(api_client)
    request = superlink.ApiAccessTokenCreateRequest() # ApiAccessTokenCreateRequest | access token create request

    try:
        # Creates an admin token for a partner
        api_response = api_instance.create_access_token(request)
        print("The response of PartnerApi->create_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerApi->create_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApiAccessTokenCreateRequest**](ApiAccessTokenCreateRequest.md)| access token create request | 

### Return type

[**ApiAccessTokenResponse**](ApiAccessTokenResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_token**
> delete_access_token(request)

Deletes an access token

Deletes an access token

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_access_token_delete_request import ApiAccessTokenDeleteRequest
from superlink.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.superlink.me
# See configuration.py for a list of all supported configuration parameters.
configuration = superlink.Configuration(
    host = "https://api.superlink.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with superlink.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = superlink.PartnerApi(api_client)
    request = superlink.ApiAccessTokenDeleteRequest() # ApiAccessTokenDeleteRequest | access token delete request

    try:
        # Deletes an access token
        api_instance.delete_access_token(request)
    except Exception as e:
        print("Exception when calling PartnerApi->delete_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApiAccessTokenDeleteRequest**](ApiAccessTokenDeleteRequest.md)| access token delete request | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_access_tokens**
> ApiAccessTokenResponse list_access_tokens()

Lists access tokens for a partner

Lists access tokens for a partner

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_access_token_response import ApiAccessTokenResponse
from superlink.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.superlink.me
# See configuration.py for a list of all supported configuration parameters.
configuration = superlink.Configuration(
    host = "https://api.superlink.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with superlink.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = superlink.PartnerApi(api_client)

    try:
        # Lists access tokens for a partner
        api_response = api_instance.list_access_tokens()
        print("The response of PartnerApi->list_access_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerApi->list_access_tokens: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiAccessTokenResponse**](ApiAccessTokenResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_purchases**
> ApiPurchaseListResponse partner_purchases()

Returns a list of all purchases

Returns a list of all purchases

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_purchase_list_response import ApiPurchaseListResponse
from superlink.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.superlink.me
# See configuration.py for a list of all supported configuration parameters.
configuration = superlink.Configuration(
    host = "https://api.superlink.me"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with superlink.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = superlink.PartnerApi(api_client)

    try:
        # Returns a list of all purchases
        api_response = api_instance.partner_purchases()
        print("The response of PartnerApi->partner_purchases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerApi->partner_purchases: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiPurchaseListResponse**](ApiPurchaseListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

