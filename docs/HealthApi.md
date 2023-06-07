# SuperlinkAPI.HealthApi

All URIs are relative to *https://api.superlink.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](HealthApi.md#health_check) | **GET** /v1/health | Checks the health of the API


# **health_check**
> health_check()

Checks the health of the API

Checks the health of the API

### Example

```python
import time
import os
import SuperlinkAPI
from SuperlinkAPI.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.superlink.me
# See configuration.py for a list of all supported configuration parameters.
configuration = SuperlinkAPI.Configuration(
    host = "https://api.superlink.me"
)


# Enter a context with an instance of the API client
with SuperlinkAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = SuperlinkAPI.HealthApi(api_client)

    try:
        # Checks the health of the API
        api_instance.health_check()
    except Exception as e:
        print("Exception when calling HealthApi->health_check: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

