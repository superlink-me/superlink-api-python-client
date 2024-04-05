# superlink.LoginApi

All URIs are relative to *https://api.superlink.me*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_with_link**](LoginApi.md#login_with_link) | **GET** /v1/login/link/{loginToken} | Login via a magic link
[**login_with_wallet**](LoginApi.md#login_with_wallet) | **POST** /v1/login/wallet/{ownerAddress} | Login with a valid wallet
[**send_login_email**](LoginApi.md#send_login_email) | **POST** /v1/login/email/{emailAddress} | Sends the e-mail that contains the magic link to login a specfic user


# **login_with_link**
> ApiAccessTokenResponse login_with_link(login_token, return_url=return_url)

Login via a magic link

Sets the auth cookie for a client provided a valid encrypted json

### Example


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


# Enter a context with an instance of the API client
with superlink.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = superlink.LoginApi(api_client)
    login_token = 'login_token_example' # str | ycA4dEverAzydH0Df2si5QAqoFFeYJxDdszP2WIBEQ6rx%2FT98aJQ7HZSAl7abC1f%2BDYBlL6bQxOrr%2FVHgabyqC4ln1c8L%2BmkDRFC9QsR67kcW%2BZc92KAv9eGKdOyHgIjarjUw3FmQSeQpKsAtGytVRBzhVHLHQ%3D%3D
    return_url = 'return_url_example' # str | /superlinks (optional)

    try:
        # Login via a magic link
        api_response = api_instance.login_with_link(login_token, return_url=return_url)
        print("The response of LoginApi->login_with_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->login_with_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_token** | **str**| ycA4dEverAzydH0Df2si5QAqoFFeYJxDdszP2WIBEQ6rx%2FT98aJQ7HZSAl7abC1f%2BDYBlL6bQxOrr%2FVHgabyqC4ln1c8L%2BmkDRFC9QsR67kcW%2BZc92KAv9eGKdOyHgIjarjUw3FmQSeQpKsAtGytVRBzhVHLHQ%3D%3D | 
 **return_url** | **str**| /superlinks | [optional] 

### Return type

[**ApiAccessTokenResponse**](ApiAccessTokenResponse.md)

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

# **login_with_wallet**
> login_with_wallet(owner_address, request)

Login with a valid wallet

Sets the auth cookie for a client provided a valid wallet + signed message

### Example


```python
import superlink
from superlink.models.api_wallet_login_request import ApiWalletLoginRequest
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
    api_instance = superlink.LoginApi(api_client)
    owner_address = 'owner_address_example' # str | 0xA5D70E12348Fef6A123EBD1231b123c51235E321
    request = superlink.ApiWalletLoginRequest() # ApiWalletLoginRequest | wallet login request

    try:
        # Login with a valid wallet
        api_instance.login_with_wallet(owner_address, request)
    except Exception as e:
        print("Exception when calling LoginApi->login_with_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_address** | **str**| 0xA5D70E12348Fef6A123EBD1231b123c51235E321 | 
 **request** | [**ApiWalletLoginRequest**](ApiWalletLoginRequest.md)| wallet login request | 

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
**204** | No Content |  -  |
**302** | Found |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_login_email**
> send_login_email(email_address, return_url=return_url)

Sends the e-mail that contains the magic link to login a specfic user

Sends the e-mail that contains the magic link to login a specfic user

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
    api_instance = superlink.LoginApi(api_client)
    email_address = 'email_address_example' # str | test@superlink.me
    return_url = 'return_url_example' # str | /superlinks (optional)

    try:
        # Sends the e-mail that contains the magic link to login a specfic user
        api_instance.send_login_email(email_address, return_url=return_url)
    except Exception as e:
        print("Exception when calling LoginApi->send_login_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| test@superlink.me | 
 **return_url** | **str**| /superlinks | [optional] 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

