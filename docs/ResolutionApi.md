# superlink.ResolutionApi

All URIs are relative to *https://api.superlink.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolve_data_by_address**](ResolutionApi.md#resolve_data_by_address) | **GET** /v1/reverse/{address} | Resolves wallets and DNS records for an address
[**resolve_data_by_domain**](ResolutionApi.md#resolve_data_by_domain) | **GET** /v1/resolve/{domain} | Resolves wallets and DNS records for a domain


# **resolve_data_by_address**
> ApiResolveDomainResponse resolve_data_by_address(address, nameservice=nameservice)

Resolves wallets and DNS records for an address

resolve domain data by address

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_resolve_domain_response import ApiResolveDomainResponse
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
    api_instance = superlink.ResolutionApi(api_client)
    address = 'address_example' # str | 0x1234561234556
    nameservice = 'nameservice_example' # str | superlink (optional)

    try:
        # Resolves wallets and DNS records for an address
        api_response = api_instance.resolve_data_by_address(address, nameservice=nameservice)
        print("The response of ResolutionApi->resolve_data_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionApi->resolve_data_by_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| 0x1234561234556 | 
 **nameservice** | **str**| superlink | [optional] 

### Return type

[**ApiResolveDomainResponse**](ApiResolveDomainResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_data_by_domain**
> ApiResolveDomainResponse resolve_data_by_domain(domain, nameservices=nameservices, coins=coins)

Resolves wallets and DNS records for a domain

resolve domain data by domain

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_resolve_domain_response import ApiResolveDomainResponse
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
    api_instance = superlink.ResolutionApi(api_client)
    domain = 'domain_example' # str | firstname.lastname
    nameservices = ['nameservices_example'] # List[str] | superlink,ens,ud (optional)
    coins = ['coins_example'] # List[str] | BTC,ETH,MATIC (optional)

    try:
        # Resolves wallets and DNS records for a domain
        api_response = api_instance.resolve_data_by_domain(domain, nameservices=nameservices, coins=coins)
        print("The response of ResolutionApi->resolve_data_by_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionApi->resolve_data_by_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| firstname.lastname | 
 **nameservices** | [**List[str]**](str.md)| superlink,ens,ud | [optional] 
 **coins** | [**List[str]**](str.md)| BTC,ETH,MATIC | [optional] 

### Return type

[**ApiResolveDomainResponse**](ApiResolveDomainResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

