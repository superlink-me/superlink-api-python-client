# superlink.MarketApi

All URIs are relative to *https://api.superlink.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_crypto_estimate**](MarketApi.md#market_crypto_estimate) | **GET** /v1/market/crypto/estimate | CryptoEstimate returns the estimated conversion rates for supported crypto payment options
[**market_crypto_purchase**](MarketApi.md#market_crypto_purchase) | **POST** /v1/market/crypto/purchase | CryptoPurchase returns the payment details required for crypto payment
[**market_order**](MarketApi.md#market_order) | **GET** /v1/market/order/{orderID} | Returns order information
[**market_purchase**](MarketApi.md#market_purchase) | **POST** /v1/market/purchase | Purchase returns the payment details required by Stripe
[**market_search**](MarketApi.md#market_search) | **GET** /v1/market/search/{query} | Returns market listings


# **market_crypto_estimate**
> ApiMarketCryptoEstimationResponse market_crypto_estimate(basecurrency=basecurrency)

CryptoEstimate returns the estimated conversion rates for supported crypto payment options

CryptoEstimate returns the estimated conversion rates for supported crypto payment options

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import superlink
from superlink.models.api_market_crypto_estimation_response import ApiMarketCryptoEstimationResponse
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
    basecurrency = 'basecurrency_example' # str | string valid (optional)

    try:
        # CryptoEstimate returns the estimated conversion rates for supported crypto payment options
        api_response = api_instance.market_crypto_estimate(basecurrency=basecurrency)
        print("The response of MarketApi->market_crypto_estimate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->market_crypto_estimate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basecurrency** | **str**| string valid | [optional] 

### Return type

[**ApiMarketCryptoEstimationResponse**](ApiMarketCryptoEstimationResponse.md)

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

# **market_crypto_purchase**
> ApiMarketCryptoPurchaseResponse market_crypto_purchase(request)

CryptoPurchase returns the payment details required for crypto payment

CryptoPurchase returns the payment details required for crypto payment

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import superlink
from superlink.models.api_crypto_purchase_request import ApiCryptoPurchaseRequest
from superlink.models.api_market_crypto_purchase_response import ApiMarketCryptoPurchaseResponse
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
    request = superlink.ApiCryptoPurchaseRequest() # ApiCryptoPurchaseRequest | crypto purchase request

    try:
        # CryptoPurchase returns the payment details required for crypto payment
        api_response = api_instance.market_crypto_purchase(request)
        print("The response of MarketApi->market_crypto_purchase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->market_crypto_purchase: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApiCryptoPurchaseRequest**](ApiCryptoPurchaseRequest.md)| crypto purchase request | 

### Return type

[**ApiMarketCryptoPurchaseResponse**](ApiMarketCryptoPurchaseResponse.md)

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

# **market_order**
> ApiMarketplaceOrderResponse market_order(order_id)

Returns order information

Returns order information

### Example

* Api Key Authentication (BearerAuth):
```python
import time
import os
import superlink
from superlink.models.api_marketplace_order_response import ApiMarketplaceOrderResponse
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
    order_id = 'order_id_example' # str | 92456d2b-c315-4b2b-b234-c674490b7324

    try:
        # Returns order information
        api_response = api_instance.market_order(order_id)
        print("The response of MarketApi->market_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->market_order: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| 92456d2b-c315-4b2b-b234-c674490b7324 | 

### Return type

[**ApiMarketplaceOrderResponse**](ApiMarketplaceOrderResponse.md)

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

