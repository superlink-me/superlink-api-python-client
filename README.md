# superlink
API for Superlink

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.0.1
- Package version: v0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://superlink.me/about#contact-us](https://superlink.me/about#contact-us)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/superlink-me/superlink-api-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/superlink-me/superlink-api-python-client.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.superlink.me
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccessTokenApi(api_client)
    request = openapi_client.ApiAccessTokenCreateRequest() # ApiAccessTokenCreateRequest | access token create request

    try:
        # Creates an admin token
        api_response = api_instance.create_access_token(request)
        print("The response of AccessTokenApi->create_access_token:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessTokenApi->create_access_token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.superlink.me*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessTokenApi* | [**create_access_token**](docs/AccessTokenApi.md#create_access_token) | **POST** /v1/access-token | Creates an admin token
*AccessTokenApi* | [**delete_access_token**](docs/AccessTokenApi.md#delete_access_token) | **DELETE** /v1/access-token | Deletes an access token
*AccessTokenApi* | [**list_access_tokens**](docs/AccessTokenApi.md#list_access_tokens) | **GET** /v1/access-token | Lists access tokens
*HealthApi* | [**health_check**](docs/HealthApi.md#health_check) | **GET** /v1/health | Checks the health of the API
*ResolutionApi* | [**resolve_data_by_domain**](docs/ResolutionApi.md#resolve_data_by_domain) | **GET** /v1/resolve/{domain} | Resolves wallets and DNS records for a domain


## Documentation For Models

 - [ApiAccessTokenCreateRequest](docs/ApiAccessTokenCreateRequest.md)
 - [ApiAccessTokenDeleteRequest](docs/ApiAccessTokenDeleteRequest.md)
 - [ApiAccessTokenResponse](docs/ApiAccessTokenResponse.md)
 - [ApiBadRequestResponse](docs/ApiBadRequestResponse.md)
 - [ApiCoin](docs/ApiCoin.md)
 - [ApiDNSRecord](docs/ApiDNSRecord.md)
 - [ApiErrorResponse](docs/ApiErrorResponse.md)
 - [ApiInternalServerErrorResponse](docs/ApiInternalServerErrorResponse.md)
 - [ApiResolveWalletAddressByDomainResponse](docs/ApiResolveWalletAddressByDomainResponse.md)
 - [ApiWalletData](docs/ApiWalletData.md)
 - [DataAccessTokenType](docs/DataAccessTokenType.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@superlink.me


