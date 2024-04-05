# superlink.DomainInfoApi

All URIs are relative to *https://api.superlink.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_domains**](DomainInfoApi.md#get_all_domains) | **GET** /v1/domain | Returns all the domains owned by a given ownerAddress


# **get_all_domains**
> ApiGetAllDomainsResponse get_all_domains()

Returns all the domains owned by a given ownerAddress

returns all the domains owned by a given ownerAddress

### Example


```python
import superlink
from superlink.models.api_get_all_domains_response import ApiGetAllDomainsResponse
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
    api_instance = superlink.DomainInfoApi(api_client)

    try:
        # Returns all the domains owned by a given ownerAddress
        api_response = api_instance.get_all_domains()
        print("The response of DomainInfoApi->get_all_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainInfoApi->get_all_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiGetAllDomainsResponse**](ApiGetAllDomainsResponse.md)

### Authorization

No authorization required

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

