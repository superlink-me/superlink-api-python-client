# superlink.SubdomainApi

All URIs are relative to *https://api.superlink.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parentdomain_purchase**](SubdomainApi.md#parentdomain_purchase) | **POST** /v1/parentdomains/{parentDomain}/buy | Purchases and sets up a parent domain for use with ens subdomains
[**parentdomain_search**](SubdomainApi.md#parentdomain_search) | **GET** /v1/parentdomains/{parentDomain}/search | Returns a list of available parent-domains provided the preferred parent ddomain
[**parentdomain_validation**](SubdomainApi.md#parentdomain_validation) | **GET** /v1/parentdomains/{parentDomain} | Validates if parent domain is correctly configured for use with ens subdomains
[**subdomain_available**](SubdomainApi.md#subdomain_available) | **GET** /v1/parentdomains/{parentDomain}/subdomains/{subDomainName} | Returns subdomain availability
[**subdomain_claimed**](SubdomainApi.md#subdomain_claimed) | **GET** /v1/parentdomains/{parentDomain}/claimed/{ethAddress} | Returns subdomain availability
[**subdomain_invalidate_claim_rate_limit**](SubdomainApi.md#subdomain_invalidate_claim_rate_limit) | **DELETE** /v1/parentdomains/{parentDomain}/invalidate-claim-rate-limit | Invalidates the claim rate limit for the current IP
[**subdomain_list**](SubdomainApi.md#subdomain_list) | **GET** /v1/parentdomains/{parentDomain}/list | Paginates over all subdomains in descending order of the creation date
[**subdomain_mint**](SubdomainApi.md#subdomain_mint) | **POST** /v1/parentdomains/{parentDomain}/subdomains/{subDomainName} | Creates a subdomain for provided parentdomain
[**subdomain_mint_sig**](SubdomainApi.md#subdomain_mint_sig) | **POST** /v1/parentdomains/{parentDomain}/subdomains/{subDomainName}/mint-with-sig | Creates a subdomain for provided parentdomain with signature
[**subdomain_per_day**](SubdomainApi.md#subdomain_per_day) | **GET** /v1/parentdomains/{parentDomain}/per-day | Paginates over per-day aggregated counts for subdomains created given a parentdomain
[**subdomain_resolve**](SubdomainApi.md#subdomain_resolve) | **GET** /v1/parentdomains/{parentDomain}/subdomains/{subDomainName}/resolve | Returns resolution of a provided subdomain
[**subdomain_reverse_resolve**](SubdomainApi.md#subdomain_reverse_resolve) | **GET** /v1/parentdomains/{parentDomain}/addresses/{ethAddress}/reverse-resolve | Returns reverse-resolution of a provided eth address limited to provided parentdomain
[**subdomain_revoke**](SubdomainApi.md#subdomain_revoke) | **DELETE** /v1/parentdomains/{parentDomain}/subdomains/{subDomainName} | Deletes a subdomain for provided parentdomain (Omnipotent)
[**subdomain_total**](SubdomainApi.md#subdomain_total) | **GET** /v1/parentdomains/{parentDomain}/total | Returns the total number of subdomains registered to parentdomain


# **parentdomain_purchase**
> parentdomain_purchase(parent_domain, request)

Purchases and sets up a parent domain for use with ens subdomains

Purchases and sets up a parent domain for use with ens subdomains

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_parent_domain_purchase_request import ApiParentDomainPurchaseRequest
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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me
    request = superlink.ApiParentDomainPurchaseRequest() # ApiParentDomainPurchaseRequest | purchase parent domain

    try:
        # Purchases and sets up a parent domain for use with ens subdomains
        api_instance.parentdomain_purchase(parent_domain, request)
    except Exception as e:
        print("Exception when calling SubdomainApi->parentdomain_purchase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 
 **request** | [**ApiParentDomainPurchaseRequest**](ApiParentDomainPurchaseRequest.md)| purchase parent domain | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parentdomain_search**
> ApiParentDomainSearchResponse parentdomain_search(parent_domain)

Returns a list of available parent-domains provided the preferred parent ddomain

Returns a list of available parent-domains provided the preferred parent ddomain

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_parent_domain_search_response import ApiParentDomainSearchResponse
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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me

    try:
        # Returns a list of available parent-domains provided the preferred parent ddomain
        api_response = api_instance.parentdomain_search(parent_domain)
        print("The response of SubdomainApi->parentdomain_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubdomainApi->parentdomain_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 

### Return type

[**ApiParentDomainSearchResponse**](ApiParentDomainSearchResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parentdomain_validation**
> ApiParentDomainValidationResponse parentdomain_validation(parent_domain)

Validates if parent domain is correctly configured for use with ens subdomains

Validates if parent domain is correctly configured for use with ens subdomains

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_parent_domain_validation_response import ApiParentDomainValidationResponse
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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me

    try:
        # Validates if parent domain is correctly configured for use with ens subdomains
        api_response = api_instance.parentdomain_validation(parent_domain)
        print("The response of SubdomainApi->parentdomain_validation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubdomainApi->parentdomain_validation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 

### Return type

[**ApiParentDomainValidationResponse**](ApiParentDomainValidationResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subdomain_available**
> ApiSubDomainAvailableResponse subdomain_available(parent_domain, sub_domain_name)

Returns subdomain availability

Returns subdomain availability

### Example


```python
import superlink
from superlink.models.api_sub_domain_available_response import ApiSubDomainAvailableResponse
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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me
    sub_domain_name = 'sub_domain_name_example' # str | test

    try:
        # Returns subdomain availability
        api_response = api_instance.subdomain_available(parent_domain, sub_domain_name)
        print("The response of SubdomainApi->subdomain_available:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubdomainApi->subdomain_available: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 
 **sub_domain_name** | **str**| test | 

### Return type

[**ApiSubDomainAvailableResponse**](ApiSubDomainAvailableResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subdomain_claimed**
> ApiSubDomainAvailableResponse subdomain_claimed(parent_domain, eth_address)

Returns subdomain availability

Returns subdomain availability

### Example


```python
import superlink
from superlink.models.api_sub_domain_available_response import ApiSubDomainAvailableResponse
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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me
    eth_address = 'eth_address_example' # str | 0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266

    try:
        # Returns subdomain availability
        api_response = api_instance.subdomain_claimed(parent_domain, eth_address)
        print("The response of SubdomainApi->subdomain_claimed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubdomainApi->subdomain_claimed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 
 **eth_address** | **str**| 0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266 | 

### Return type

[**ApiSubDomainAvailableResponse**](ApiSubDomainAvailableResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subdomain_invalidate_claim_rate_limit**
> subdomain_invalidate_claim_rate_limit(parent_domain)

Invalidates the claim rate limit for the current IP

Invalidates the claim rate limit for the current IP

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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me

    try:
        # Invalidates the claim rate limit for the current IP
        api_instance.subdomain_invalidate_claim_rate_limit(parent_domain)
    except Exception as e:
        print("Exception when calling SubdomainApi->subdomain_invalidate_claim_rate_limit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 

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
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subdomain_list**
> ApiSubDomainListResponse subdomain_list(parent_domain, pagination_token=pagination_token, page_size=page_size)

Paginates over all subdomains in descending order of the creation date

Paginates over all subdomains in descending order of the creation date

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_sub_domain_list_response import ApiSubDomainListResponse
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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me
    pagination_token = 'pagination_token_example' # str | KCJuYW1lIjoiYWJjLmRlZi5naGkiLCJkYXRlIjoiMjAyMS0xMS0xMSIp (optional)
    page_size = 56 # int | 100 (optional)

    try:
        # Paginates over all subdomains in descending order of the creation date
        api_response = api_instance.subdomain_list(parent_domain, pagination_token=pagination_token, page_size=page_size)
        print("The response of SubdomainApi->subdomain_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubdomainApi->subdomain_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 
 **pagination_token** | **str**| KCJuYW1lIjoiYWJjLmRlZi5naGkiLCJkYXRlIjoiMjAyMS0xMS0xMSIp | [optional] 
 **page_size** | **int**| 100 | [optional] 

### Return type

[**ApiSubDomainListResponse**](ApiSubDomainListResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subdomain_mint**
> subdomain_mint(parent_domain, sub_domain_name, request)

Creates a subdomain for provided parentdomain

Creates a subdomain for provided parentdomain

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_sub_domain_mint_request import ApiSubDomainMintRequest
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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me
    sub_domain_name = 'sub_domain_name_example' # str | test
    request = superlink.ApiSubDomainMintRequest() # ApiSubDomainMintRequest | create subdomain

    try:
        # Creates a subdomain for provided parentdomain
        api_instance.subdomain_mint(parent_domain, sub_domain_name, request)
    except Exception as e:
        print("Exception when calling SubdomainApi->subdomain_mint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 
 **sub_domain_name** | **str**| test | 
 **request** | [**ApiSubDomainMintRequest**](ApiSubDomainMintRequest.md)| create subdomain | 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subdomain_mint_sig**
> subdomain_mint_sig(parent_domain, sub_domain_name, request)

Creates a subdomain for provided parentdomain with signature

Creates a subdomain for provided parentdomain with signature

### Example


```python
import superlink
from superlink.models.api_sub_domain_mint_with_sig_request import ApiSubDomainMintWithSigRequest
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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me
    sub_domain_name = 'sub_domain_name_example' # str | test
    request = superlink.ApiSubDomainMintWithSigRequest() # ApiSubDomainMintWithSigRequest | create subdomain

    try:
        # Creates a subdomain for provided parentdomain with signature
        api_instance.subdomain_mint_sig(parent_domain, sub_domain_name, request)
    except Exception as e:
        print("Exception when calling SubdomainApi->subdomain_mint_sig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 
 **sub_domain_name** | **str**| test | 
 **request** | [**ApiSubDomainMintWithSigRequest**](ApiSubDomainMintWithSigRequest.md)| create subdomain | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subdomain_per_day**
> ApiSubDomainPerDayResponse subdomain_per_day(parent_domain, pagination_token=pagination_token, page_size=page_size)

Paginates over per-day aggregated counts for subdomains created given a parentdomain

Paginates over per-day aggregated counts for subdomains created given a parentdomain

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_sub_domain_per_day_response import ApiSubDomainPerDayResponse
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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me
    pagination_token = 'pagination_token_example' # str | KCJuYW1lIjoiYWJjLmRlZi5naGkiLCJkYXRlIjoiMjAyMS0xMS0xMSIp (optional)
    page_size = 56 # int | 100 (optional)

    try:
        # Paginates over per-day aggregated counts for subdomains created given a parentdomain
        api_response = api_instance.subdomain_per_day(parent_domain, pagination_token=pagination_token, page_size=page_size)
        print("The response of SubdomainApi->subdomain_per_day:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubdomainApi->subdomain_per_day: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 
 **pagination_token** | **str**| KCJuYW1lIjoiYWJjLmRlZi5naGkiLCJkYXRlIjoiMjAyMS0xMS0xMSIp | [optional] 
 **page_size** | **int**| 100 | [optional] 

### Return type

[**ApiSubDomainPerDayResponse**](ApiSubDomainPerDayResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subdomain_resolve**
> ApiSubDomainResolveResponse subdomain_resolve(parent_domain, sub_domain_name)

Returns resolution of a provided subdomain

Returns resolution of a provided subdomain

### Example


```python
import superlink
from superlink.models.api_sub_domain_resolve_response import ApiSubDomainResolveResponse
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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me
    sub_domain_name = 'sub_domain_name_example' # str | test

    try:
        # Returns resolution of a provided subdomain
        api_response = api_instance.subdomain_resolve(parent_domain, sub_domain_name)
        print("The response of SubdomainApi->subdomain_resolve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubdomainApi->subdomain_resolve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 
 **sub_domain_name** | **str**| test | 

### Return type

[**ApiSubDomainResolveResponse**](ApiSubDomainResolveResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subdomain_reverse_resolve**
> ApiSubDomainReverseResolveResponse subdomain_reverse_resolve(parent_domain, eth_address)

Returns reverse-resolution of a provided eth address limited to provided parentdomain

Returns reverse-resolution of a provided eth address limited to provided parentdomain

### Example


```python
import superlink
from superlink.models.api_sub_domain_reverse_resolve_response import ApiSubDomainReverseResolveResponse
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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me
    eth_address = 'eth_address_example' # str | 0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266

    try:
        # Returns reverse-resolution of a provided eth address limited to provided parentdomain
        api_response = api_instance.subdomain_reverse_resolve(parent_domain, eth_address)
        print("The response of SubdomainApi->subdomain_reverse_resolve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubdomainApi->subdomain_reverse_resolve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 
 **eth_address** | **str**| 0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266 | 

### Return type

[**ApiSubDomainReverseResolveResponse**](ApiSubDomainReverseResolveResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subdomain_revoke**
> subdomain_revoke(parent_domain, sub_domain_name)

Deletes a subdomain for provided parentdomain (Omnipotent)

Deletes a subdomain for provided parentdomain (Omnipotent)

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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me
    sub_domain_name = 'sub_domain_name_example' # str | test

    try:
        # Deletes a subdomain for provided parentdomain (Omnipotent)
        api_instance.subdomain_revoke(parent_domain, sub_domain_name)
    except Exception as e:
        print("Exception when calling SubdomainApi->subdomain_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 
 **sub_domain_name** | **str**| test | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subdomain_total**
> ApiSubDomainTotalResponse subdomain_total(parent_domain)

Returns the total number of subdomains registered to parentdomain

Returns the total number of subdomains registered to parentdomain

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_sub_domain_total_response import ApiSubDomainTotalResponse
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
    api_instance = superlink.SubdomainApi(api_client)
    parent_domain = 'parent_domain_example' # str | superlink.me

    try:
        # Returns the total number of subdomains registered to parentdomain
        api_response = api_instance.subdomain_total(parent_domain)
        print("The response of SubdomainApi->subdomain_total:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubdomainApi->subdomain_total: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_domain** | **str**| superlink.me | 

### Return type

[**ApiSubDomainTotalResponse**](ApiSubDomainTotalResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

