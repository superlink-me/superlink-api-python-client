# superlink.NftApi

All URIs are relative to *https://api.superlink.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token_image_by_domain**](NftApi.md#get_token_image_by_domain) | **GET** /v1/card-image/{domain} | Returns a SVG image for a Superlink NFT
[**get_token_metadata_by_domain**](NftApi.md#get_token_metadata_by_domain) | **GET** /v1/metadata/{domain} | Returns metadata usually associated with NFTs uri


# **get_token_image_by_domain**
> str get_token_image_by_domain(domain)

Returns a SVG image for a Superlink NFT

returns the image for a \"domain\" nft

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
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
    api_instance = superlink.NftApi(api_client)
    domain = 'domain_example' # str | firstname.lastname

    try:
        # Returns a SVG image for a Superlink NFT
        api_response = api_instance.get_token_image_by_domain(domain)
        print("The response of NftApi->get_token_image_by_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->get_token_image_by_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| firstname.lastname | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/svg+xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_metadata_by_domain**
> ApiDomainMetadataResponse get_token_metadata_by_domain(domain)

Returns metadata usually associated with NFTs uri

returns the metadata for a \"domain\" nft

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import superlink
from superlink.models.api_domain_metadata_response import ApiDomainMetadataResponse
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
    api_instance = superlink.NftApi(api_client)
    domain = 'domain_example' # str | firstname.lastname

    try:
        # Returns metadata usually associated with NFTs uri
        api_response = api_instance.get_token_metadata_by_domain(domain)
        print("The response of NftApi->get_token_metadata_by_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NftApi->get_token_metadata_by_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| firstname.lastname | 

### Return type

[**ApiDomainMetadataResponse**](ApiDomainMetadataResponse.md)

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

