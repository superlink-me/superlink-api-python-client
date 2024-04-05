# superlink.ProveApi

All URIs are relative to *https://api.superlink.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_eth_wallet_message**](ProveApi.md#get_eth_wallet_message) | **GET** /v1/prove/wallet/eth/{ownerAddress} | Get message which should be signed by an eth wallet as proof of ownership


# **get_eth_wallet_message**
> ApiWalletMessageResponse get_eth_wallet_message(owner_address)

Get message which should be signed by an eth wallet as proof of ownership

Gets message which should be signed by an eth wallet as proof of ownership

### Example

* Api Key Authentication (BearerAuth):

```python
import superlink
from superlink.models.api_wallet_message_response import ApiWalletMessageResponse
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
    api_instance = superlink.ProveApi(api_client)
    owner_address = 'owner_address_example' # str | 0xA5D70E12348Fef6A123EBD1231b123c51235E321

    try:
        # Get message which should be signed by an eth wallet as proof of ownership
        api_response = api_instance.get_eth_wallet_message(owner_address)
        print("The response of ProveApi->get_eth_wallet_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProveApi->get_eth_wallet_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_address** | **str**| 0xA5D70E12348Fef6A123EBD1231b123c51235E321 | 

### Return type

[**ApiWalletMessageResponse**](ApiWalletMessageResponse.md)

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

