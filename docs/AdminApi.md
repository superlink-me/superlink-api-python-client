# superlink.AdminApi

All URIs are relative to *https://api.superlink.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_create_access_token**](AdminApi.md#admin_create_access_token) | **POST** /v1/admin/access-token | Creates an admin token
[**admin_delete_access_token**](AdminApi.md#admin_delete_access_token) | **DELETE** /v1/admin/access-token | Deletes an access token
[**admin_list_access_tokens**](AdminApi.md#admin_list_access_tokens) | **GET** /v1/admin/access-token | Lists access tokens
[**admin_list_partners**](AdminApi.md#admin_list_partners) | **GET** /v1/admin/partner | Lists partners
[**admin_partner_create**](AdminApi.md#admin_partner_create) | **POST** /v1/admin/partner | Creates a partner
[**hns_tld_register**](AdminApi.md#hns_tld_register) | **POST** /v1/admin/hns/tld/register | HNSTLDRegister registers a Handshake TLD
[**remove_reverse_resolution_address**](AdminApi.md#remove_reverse_resolution_address) | **DELETE** /v1/admin/reverse | Removes a reverse resolution address from a domain
[**set_reverse_resolution_address**](AdminApi.md#set_reverse_resolution_address) | **POST** /v1/admin/reverse | Assigns an address to a domain for reverse resolution


# **admin_create_access_token**
> ApiAccessTokenResponse admin_create_access_token(request)

Creates an admin token

Creates an admin token

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_access_token_response import ApiAccessTokenResponse
from superlink.models.api_admin_access_token_create_request import ApiAdminAccessTokenCreateRequest
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
    api_instance = superlink.AdminApi(api_client)
    request = superlink.ApiAdminAccessTokenCreateRequest() # ApiAdminAccessTokenCreateRequest | access token create request

    try:
        # Creates an admin token
        api_response = api_instance.admin_create_access_token(request)
        print("The response of AdminApi->admin_create_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_create_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApiAdminAccessTokenCreateRequest**](ApiAdminAccessTokenCreateRequest.md)| access token create request | 

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

# **admin_delete_access_token**
> admin_delete_access_token(request)

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
    api_instance = superlink.AdminApi(api_client)
    request = superlink.ApiAccessTokenDeleteRequest() # ApiAccessTokenDeleteRequest | access token delete request

    try:
        # Deletes an access token
        api_instance.admin_delete_access_token(request)
    except Exception as e:
        print("Exception when calling AdminApi->admin_delete_access_token: %s\n" % e)
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

# **admin_list_access_tokens**
> ApiAccessTokenResponse admin_list_access_tokens()

Lists access tokens

Lists access tokens

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
    api_instance = superlink.AdminApi(api_client)

    try:
        # Lists access tokens
        api_response = api_instance.admin_list_access_tokens()
        print("The response of AdminApi->admin_list_access_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_list_access_tokens: %s\n" % e)
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

# **admin_list_partners**
> ApiPartnerResponse admin_list_partners()

Lists partners

Lists partners

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_partner_response import ApiPartnerResponse
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
    api_instance = superlink.AdminApi(api_client)

    try:
        # Lists partners
        api_response = api_instance.admin_list_partners()
        print("The response of AdminApi->admin_list_partners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_list_partners: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiPartnerResponse**](ApiPartnerResponse.md)

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

# **admin_partner_create**
> ApiPartnerResponse admin_partner_create(request)

Creates a partner

Creates a partner

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_admin_partner_create_request import ApiAdminPartnerCreateRequest
from superlink.models.api_partner_response import ApiPartnerResponse
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
    api_instance = superlink.AdminApi(api_client)
    request = superlink.ApiAdminPartnerCreateRequest() # ApiAdminPartnerCreateRequest | partner create request

    try:
        # Creates a partner
        api_response = api_instance.admin_partner_create(request)
        print("The response of AdminApi->admin_partner_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_partner_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApiAdminPartnerCreateRequest**](ApiAdminPartnerCreateRequest.md)| partner create request | 

### Return type

[**ApiPartnerResponse**](ApiPartnerResponse.md)

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

# **hns_tld_register**
> ApiHNSRegisterTLDResponse hns_tld_register(request)

HNSTLDRegister registers a Handshake TLD

HNSTLDRegister registers a Handshake TLD

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_hns_register_tld_request import ApiHNSRegisterTLDRequest
from superlink.models.api_hns_register_tld_response import ApiHNSRegisterTLDResponse
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
    api_instance = superlink.AdminApi(api_client)
    request = superlink.ApiHNSRegisterTLDRequest() # ApiHNSRegisterTLDRequest | register hns tld request

    try:
        # HNSTLDRegister registers a Handshake TLD
        api_response = api_instance.hns_tld_register(request)
        print("The response of AdminApi->hns_tld_register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->hns_tld_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApiHNSRegisterTLDRequest**](ApiHNSRegisterTLDRequest.md)| register hns tld request | 

### Return type

[**ApiHNSRegisterTLDResponse**](ApiHNSRegisterTLDResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_reverse_resolution_address**
> remove_reverse_resolution_address(request)

Removes a reverse resolution address from a domain

Removes a reverse resolution address from a domain

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_reverse_resolution_delete_request import ApiReverseResolutionDeleteRequest
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
    api_instance = superlink.AdminApi(api_client)
    request = superlink.ApiReverseResolutionDeleteRequest() # ApiReverseResolutionDeleteRequest | reverse address delete request

    try:
        # Removes a reverse resolution address from a domain
        api_instance.remove_reverse_resolution_address(request)
    except Exception as e:
        print("Exception when calling AdminApi->remove_reverse_resolution_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApiReverseResolutionDeleteRequest**](ApiReverseResolutionDeleteRequest.md)| reverse address delete request | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_reverse_resolution_address**
> set_reverse_resolution_address(request)

Assigns an address to a domain for reverse resolution

Assigns an address to a domain for reverse resolution

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_set_reverse_address_request import ApiSetReverseAddressRequest
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
    api_instance = superlink.AdminApi(api_client)
    request = superlink.ApiSetReverseAddressRequest() # ApiSetReverseAddressRequest | set reverse address request

    try:
        # Assigns an address to a domain for reverse resolution
        api_instance.set_reverse_resolution_address(request)
    except Exception as e:
        print("Exception when calling AdminApi->set_reverse_resolution_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApiSetReverseAddressRequest**](ApiSetReverseAddressRequest.md)| set reverse address request | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

