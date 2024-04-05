# superlink.HnsApi

All URIs are relative to *https://api.superlink.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hns_domain_available**](HnsApi.md#hns_domain_available) | **GET** /v1/hns/tld/{tld}/sld/{sld}/available | checks if a handshake domain is available to mint
[**hns_domain_create**](HnsApi.md#hns_domain_create) | **POST** /v1/hns/tld/{tld}/sld/mint | HNSCreateDomain creates a handshake domain
[**hns_domain_create_sig**](HnsApi.md#hns_domain_create_sig) | **POST** /v1/hns/tld/{tld}/sld/mint-with-sig | creates a handshake domain authenticated by a signed message
[**hns_domain_delete**](HnsApi.md#hns_domain_delete) | **DELETE** /v1/hns/tld/{tld}/sld/{sld} | deletes a handshake domain
[**hns_tld_check_claimed**](HnsApi.md#hns_tld_check_claimed) | **GET** /v1/hns/tld/{tld}/check-if-claimed/{address} | tests if the wallet has already claimed a domain for this TLD.
[**hns_tld_validate**](HnsApi.md#hns_tld_validate) | **GET** /v1/hns/tld/{tld}/validate | HNSTLDValidation tests if the TLD blockchain DNS records are valid.


# **hns_domain_available**
> ApiHNSDomainAvailableResponse hns_domain_available(tld, sld)

checks if a handshake domain is available to mint

checks if a handshake domain is available to mint

### Example


```python
import superlink
from superlink.models.api_hns_domain_available_response import ApiHNSDomainAvailableResponse
from superlink.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.superlink.me
# See configuration.py for a list of all supported configuration parameters.
configuration = superlink.Configuration(
    host = "https://api.superlink.me"
)


# Enter a context with an instance of the API client
with superlink.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = superlink.HnsApi(api_client)
    tld = 'tld_example' # str | com
    sld = 'sld_example' # str | google

    try:
        # checks if a handshake domain is available to mint
        api_response = api_instance.hns_domain_available(tld, sld)
        print("The response of HnsApi->hns_domain_available:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HnsApi->hns_domain_available: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tld** | **str**| com | 
 **sld** | **str**| google | 

### Return type

[**ApiHNSDomainAvailableResponse**](ApiHNSDomainAvailableResponse.md)

### Authorization

No authorization required

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

# **hns_domain_create**
> ApiHNSDomainAvailableResponse hns_domain_create(tld, request)

HNSCreateDomain creates a handshake domain

HNSCreateDomain creates a handshake domain

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_hns_create_domain_request import ApiHNSCreateDomainRequest
from superlink.models.api_hns_domain_available_response import ApiHNSDomainAvailableResponse
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
    api_instance = superlink.HnsApi(api_client)
    tld = 'tld_example' # str | com
    request = superlink.ApiHNSCreateDomainRequest() # ApiHNSCreateDomainRequest | register hns tld request

    try:
        # HNSCreateDomain creates a handshake domain
        api_response = api_instance.hns_domain_create(tld, request)
        print("The response of HnsApi->hns_domain_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HnsApi->hns_domain_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tld** | **str**| com | 
 **request** | [**ApiHNSCreateDomainRequest**](ApiHNSCreateDomainRequest.md)| register hns tld request | 

### Return type

[**ApiHNSDomainAvailableResponse**](ApiHNSDomainAvailableResponse.md)

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hns_domain_create_sig**
> ApiHNSDomainAvailableResponse hns_domain_create_sig(tld, request)

creates a handshake domain authenticated by a signed message

creates a handshake domain authenticated by a signed message

### Example


```python
import superlink
from superlink.models.api_hns_create_domain_with_wallet_request import ApiHNSCreateDomainWithWalletRequest
from superlink.models.api_hns_domain_available_response import ApiHNSDomainAvailableResponse
from superlink.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.superlink.me
# See configuration.py for a list of all supported configuration parameters.
configuration = superlink.Configuration(
    host = "https://api.superlink.me"
)


# Enter a context with an instance of the API client
with superlink.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = superlink.HnsApi(api_client)
    tld = 'tld_example' # str | com
    request = superlink.ApiHNSCreateDomainWithWalletRequest() # ApiHNSCreateDomainWithWalletRequest | register hns domain request

    try:
        # creates a handshake domain authenticated by a signed message
        api_response = api_instance.hns_domain_create_sig(tld, request)
        print("The response of HnsApi->hns_domain_create_sig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HnsApi->hns_domain_create_sig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tld** | **str**| com | 
 **request** | [**ApiHNSCreateDomainWithWalletRequest**](ApiHNSCreateDomainWithWalletRequest.md)| register hns domain request | 

### Return type

[**ApiHNSDomainAvailableResponse**](ApiHNSDomainAvailableResponse.md)

### Authorization

No authorization required

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

# **hns_domain_delete**
> hns_domain_delete(tld, sld)

deletes a handshake domain

deletes a handshake domain

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
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
    api_instance = superlink.HnsApi(api_client)
    tld = 'tld_example' # str | com
    sld = 'sld_example' # str | google

    try:
        # deletes a handshake domain
        api_instance.hns_domain_delete(tld, sld)
    except Exception as e:
        print("Exception when calling HnsApi->hns_domain_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tld** | **str**| com | 
 **sld** | **str**| google | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hns_tld_check_claimed**
> hns_tld_check_claimed(tld, address)

tests if the wallet has already claimed a domain for this TLD.

tests if the wallet has already claimed a domain for this TLD.

### Example


```python
import superlink
from superlink.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.superlink.me
# See configuration.py for a list of all supported configuration parameters.
configuration = superlink.Configuration(
    host = "https://api.superlink.me"
)


# Enter a context with an instance of the API client
with superlink.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = superlink.HnsApi(api_client)
    tld = 'tld_example' # str | com
    address = 'address_example' # str | 0x123456789

    try:
        # tests if the wallet has already claimed a domain for this TLD.
        api_instance.hns_tld_check_claimed(tld, address)
    except Exception as e:
        print("Exception when calling HnsApi->hns_tld_check_claimed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tld** | **str**| com | 
 **address** | **str**| 0x123456789 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hns_tld_validate**
> ApiMarketPurchaseResponse hns_tld_validate(tld)

HNSTLDValidation tests if the TLD blockchain DNS records are valid.

HNSTLDValidation tests if the TLD blockchain DNS records are valid.

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_market_purchase_response import ApiMarketPurchaseResponse
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
    api_instance = superlink.HnsApi(api_client)
    tld = 'tld_example' # str | com

    try:
        # HNSTLDValidation tests if the TLD blockchain DNS records are valid.
        api_response = api_instance.hns_tld_validate(tld)
        print("The response of HnsApi->hns_tld_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HnsApi->hns_tld_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tld** | **str**| com | 

### Return type

[**ApiMarketPurchaseResponse**](ApiMarketPurchaseResponse.md)

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

