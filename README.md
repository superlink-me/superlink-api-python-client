# superlink
API for Superlink

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.3.14
- Package version: v0.3.14
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
import superlink
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import superlink
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
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
    api_instance = superlink.AdminApi(api_client)
    request = superlink.ApiAdminAccessTokenCreateRequest() # ApiAdminAccessTokenCreateRequest | access token create request

    try:
        # Creates an admin token
        api_response = api_instance.admin_create_access_token(request)
        print("The response of AdminApi->admin_create_access_token:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_create_access_token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.superlink.me*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**admin_create_access_token**](docs/AdminApi.md#admin_create_access_token) | **POST** /v1/admin/access-token | Creates an admin token
*AdminApi* | [**admin_delete_access_token**](docs/AdminApi.md#admin_delete_access_token) | **DELETE** /v1/admin/access-token | Deletes an access token
*AdminApi* | [**admin_list_access_tokens**](docs/AdminApi.md#admin_list_access_tokens) | **GET** /v1/admin/access-token | Lists access tokens
*AdminApi* | [**admin_list_partners**](docs/AdminApi.md#admin_list_partners) | **GET** /v1/admin/partner | Lists partners
*AdminApi* | [**admin_partner_create**](docs/AdminApi.md#admin_partner_create) | **POST** /v1/admin/partner | Creates a partner
*AdminApi* | [**remove_reverse_resolution_address**](docs/AdminApi.md#remove_reverse_resolution_address) | **DELETE** /v1/admin/reverse | Removes a reverse resolution address from a domain
*AdminApi* | [**set_reverse_resolution_address**](docs/AdminApi.md#set_reverse_resolution_address) | **POST** /v1/admin/reverse | Assigns an address to a domain for reverse resolution
*DefaultApi* | [**health_check**](docs/DefaultApi.md#health_check) | **GET** /v1/health | Checks the health of the API
*MarketApi* | [**market_purchase**](docs/MarketApi.md#market_purchase) | **POST** /v1/market/purchase | Purchase returns the payment details required by Stripe
*MarketApi* | [**market_search**](docs/MarketApi.md#market_search) | **GET** /v1/market/search/{query} | Returns market listings
*NftApi* | [**get_token_image_by_domain**](docs/NftApi.md#get_token_image_by_domain) | **GET** /v1/card-image/{domain}.svg | Returns a SVG image for a Superlink NFT
*NftApi* | [**get_token_metadata_by_domain**](docs/NftApi.md#get_token_metadata_by_domain) | **GET** /v1/metadata/{domain} | Returns metadata usually associated with NFTs uri
*PartnerApi* | [**create_access_token**](docs/PartnerApi.md#create_access_token) | **POST** /v1/partner/access-token | Creates an admin token for a partner
*PartnerApi* | [**delete_access_token**](docs/PartnerApi.md#delete_access_token) | **DELETE** /v1/partner/access-token | Deletes an access token
*PartnerApi* | [**list_access_tokens**](docs/PartnerApi.md#list_access_tokens) | **GET** /v1/partner/access-token | Lists access tokens for a partner
*PartnerApi* | [**partner_purchases**](docs/PartnerApi.md#partner_purchases) | **GET** /v1/partner/purchases | Returns a list of all purchases
*ResolutionApi* | [**resolve_data_by_address**](docs/ResolutionApi.md#resolve_data_by_address) | **GET** /v1/reverse/{address} | Resolves wallets and DNS records for an address
*ResolutionApi* | [**resolve_data_by_domain**](docs/ResolutionApi.md#resolve_data_by_domain) | **GET** /v1/resolve/{domain} | Resolves wallets and DNS records for a domain


## Documentation For Models

 - [ApiAccessTokenCreateRequest](docs/ApiAccessTokenCreateRequest.md)
 - [ApiAccessTokenDeleteRequest](docs/ApiAccessTokenDeleteRequest.md)
 - [ApiAccessTokenResponse](docs/ApiAccessTokenResponse.md)
 - [ApiAdminAccessTokenCreateRequest](docs/ApiAdminAccessTokenCreateRequest.md)
 - [ApiAdminPartnerCreateRequest](docs/ApiAdminPartnerCreateRequest.md)
 - [ApiBadRequestResponse](docs/ApiBadRequestResponse.md)
 - [ApiCoin](docs/ApiCoin.md)
 - [ApiDNSRecord](docs/ApiDNSRecord.md)
 - [ApiDomainMetadataAttribute](docs/ApiDomainMetadataAttribute.md)
 - [ApiDomainMetadataResponse](docs/ApiDomainMetadataResponse.md)
 - [ApiErrorResponse](docs/ApiErrorResponse.md)
 - [ApiInternalServerErrorResponse](docs/ApiInternalServerErrorResponse.md)
 - [ApiMarketListing](docs/ApiMarketListing.md)
 - [ApiMarketPurchaseResponse](docs/ApiMarketPurchaseResponse.md)
 - [ApiMarketSearchResponse](docs/ApiMarketSearchResponse.md)
 - [ApiNameService](docs/ApiNameService.md)
 - [ApiPartnerResponse](docs/ApiPartnerResponse.md)
 - [ApiPurchaseListResponse](docs/ApiPurchaseListResponse.md)
 - [ApiPurchaseRequest](docs/ApiPurchaseRequest.md)
 - [ApiPurchaseResponse](docs/ApiPurchaseResponse.md)
 - [ApiResolveDomainResponse](docs/ApiResolveDomainResponse.md)
 - [ApiReverseResolutionDeleteRequest](docs/ApiReverseResolutionDeleteRequest.md)
 - [ApiSetReverseAddressRequest](docs/ApiSetReverseAddressRequest.md)
 - [ApiTXTRecord](docs/ApiTXTRecord.md)
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


