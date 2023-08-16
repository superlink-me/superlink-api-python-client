# superlink.MarketApi

All URIs are relative to *https://api.superlink.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_purchase**](MarketApi.md#market_purchase) | **POST** /v1/market/purchase | Purchase returns the payment details required by Stripe
[**market_search**](MarketApi.md#market_search) | **GET** /v1/market/search/{query} | Returns market listings


# **market_purchase**
> ApiMarketPurchaseResponse market_purchase(request)

Purchase returns the payment details required by Stripe

Purchase returns the payment details required by Stripe

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import superlink
from superlink.models.api_market_purchase_response import ApiMarketPurchaseResponse
from superlink.models.api_purchase_request import ApiPurchaseRequest
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
    api_instance = superlink.MarketApi(api_client)
    request = superlink.ApiPurchaseRequest() # ApiPurchaseRequest | purchase request

    try:
        # Purchase returns the payment details required by Stripe
        api_response = api_instance.market_purchase(request)
        print("The response of MarketApi->market_purchase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->market_purchase: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApiPurchaseRequest**](ApiPurchaseRequest.md)| purchase request | 

### Return type

[**ApiMarketPurchaseResponse**](ApiMarketPurchaseResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_search**
> ApiMarketSearchResponse market_search(query)

Returns market listings

Returns market listings

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import superlink
from superlink.models.api_market_search_response import ApiMarketSearchResponse
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
    api_instance = superlink.MarketApi(api_client)
    query = 'query_example' # str | johndoe

    try:
        # Returns market listings
        api_response = api_instance.market_search(query)
        print("The response of MarketApi->market_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->market_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| johndoe | 

### Return type

[**ApiMarketSearchResponse**](ApiMarketSearchResponse.md)

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

