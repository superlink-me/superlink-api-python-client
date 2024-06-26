# superlink
API for Superlink

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.5.0
- Package version: v0.5.0
- Generator version: 7.5.0-SNAPSHOT
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
*AdminApi* | [**hns_tld_register**](docs/AdminApi.md#hns_tld_register) | **POST** /v1/admin/hns/tld/register | HNSTLDRegister registers a Handshake TLD
*AdminApi* | [**remove_reverse_resolution_address**](docs/AdminApi.md#remove_reverse_resolution_address) | **DELETE** /v1/admin/reverse | Removes a reverse resolution address from a domain
*AdminApi* | [**set_reverse_resolution_address**](docs/AdminApi.md#set_reverse_resolution_address) | **POST** /v1/admin/reverse | Assigns an address to a domain for reverse resolution
*DefaultApi* | [**health_check**](docs/DefaultApi.md#health_check) | **GET** /v1/health | Checks the health of the API
*DomainInfoApi* | [**get_all_domains**](docs/DomainInfoApi.md#get_all_domains) | **GET** /v1/domain | Returns all the domains owned by a given ownerAddress
*HnsApi* | [**hns_domain_available**](docs/HnsApi.md#hns_domain_available) | **GET** /v1/hns/tld/{tld}/sld/{sld}/available | checks if a handshake domain is available to mint
*HnsApi* | [**hns_domain_create**](docs/HnsApi.md#hns_domain_create) | **POST** /v1/hns/tld/{tld}/sld/mint | HNSCreateDomain creates a handshake domain
*HnsApi* | [**hns_domain_create_sig**](docs/HnsApi.md#hns_domain_create_sig) | **POST** /v1/hns/tld/{tld}/sld/mint-with-sig | creates a handshake domain authenticated by a signed message
*HnsApi* | [**hns_domain_delete**](docs/HnsApi.md#hns_domain_delete) | **DELETE** /v1/hns/tld/{tld}/sld/{sld} | deletes a handshake domain
*HnsApi* | [**hns_tld_check_claimed**](docs/HnsApi.md#hns_tld_check_claimed) | **GET** /v1/hns/tld/{tld}/check-if-claimed/{address} | tests if the wallet has already claimed a domain for this TLD.
*HnsApi* | [**hns_tld_validate**](docs/HnsApi.md#hns_tld_validate) | **GET** /v1/hns/tld/{tld}/validate | HNSTLDValidation tests if the TLD blockchain DNS records are valid.
*LoginApi* | [**login_with_link**](docs/LoginApi.md#login_with_link) | **GET** /v1/login/link/{loginToken} | Login via a magic link
*LoginApi* | [**login_with_wallet**](docs/LoginApi.md#login_with_wallet) | **POST** /v1/login/wallet/{ownerAddress} | Login with a valid wallet
*LoginApi* | [**send_login_email**](docs/LoginApi.md#send_login_email) | **POST** /v1/login/email/{emailAddress} | Sends the e-mail that contains the magic link to login a specfic user
*MarketApi* | [**market_crypto_estimate**](docs/MarketApi.md#market_crypto_estimate) | **GET** /v1/market/crypto/estimate | CryptoEstimate returns the estimated conversion rates for supported crypto payment options
*MarketApi* | [**market_crypto_purchase**](docs/MarketApi.md#market_crypto_purchase) | **POST** /v1/market/crypto/purchase | CryptoPurchase returns the payment details required for crypto payment
*MarketApi* | [**market_order**](docs/MarketApi.md#market_order) | **GET** /v1/market/order/{orderID} | Returns order information
*MarketApi* | [**market_purchase**](docs/MarketApi.md#market_purchase) | **POST** /v1/market/purchase | Purchase returns the payment details required by Stripe
*MarketApi* | [**market_search**](docs/MarketApi.md#market_search) | **POST** /v1/market/search | Returns market listings
*MarketApi* | [**market_suggestion**](docs/MarketApi.md#market_suggestion) | **POST** /v1/market/suggest | Returns market listings for suggestions
*NftApi* | [**get_token_image_by_domain**](docs/NftApi.md#get_token_image_by_domain) | **GET** /v1/card-image/{domain}.svg | Returns a SVG image for a Superlink NFT
*NftApi* | [**get_token_metadata_by_domain**](docs/NftApi.md#get_token_metadata_by_domain) | **GET** /v1/metadata/{domain} | Returns metadata usually associated with NFTs uri
*PartnerApi* | [**create_access_token**](docs/PartnerApi.md#create_access_token) | **POST** /v1/partner/access-token | Creates an admin token for a partner
*PartnerApi* | [**delete_access_token**](docs/PartnerApi.md#delete_access_token) | **DELETE** /v1/partner/access-token | Deletes an access token
*PartnerApi* | [**list_access_tokens**](docs/PartnerApi.md#list_access_tokens) | **GET** /v1/partner/access-token | Lists access tokens for a partner
*PartnerApi* | [**partner_purchases**](docs/PartnerApi.md#partner_purchases) | **GET** /v1/partner/purchases | Returns a list of all purchases
*ProveApi* | [**get_eth_wallet_message**](docs/ProveApi.md#get_eth_wallet_message) | **GET** /v1/prove/wallet/eth/{ownerAddress} | Get message which should be signed by an eth wallet as proof of ownership
*ResolutionApi* | [**resolve_data_by_address**](docs/ResolutionApi.md#resolve_data_by_address) | **GET** /v1/reverse/{address} | Resolves wallets and DNS records for an address
*ResolutionApi* | [**resolve_data_by_domain**](docs/ResolutionApi.md#resolve_data_by_domain) | **GET** /v1/resolve/{domain} | Resolves wallets and DNS records for a domain
*SubdomainApi* | [**parentdomain_purchase**](docs/SubdomainApi.md#parentdomain_purchase) | **POST** /v1/parentdomains/{parentDomain}/buy | Purchases and sets up a parent domain for use with ens subdomains
*SubdomainApi* | [**parentdomain_search**](docs/SubdomainApi.md#parentdomain_search) | **GET** /v1/parentdomains/{parentDomain}/search | Returns a list of available parent-domains provided the preferred parent ddomain
*SubdomainApi* | [**parentdomain_validation**](docs/SubdomainApi.md#parentdomain_validation) | **GET** /v1/parentdomains/{parentDomain} | Validates if parent domain is correctly configured for use with ens subdomains
*SubdomainApi* | [**subdomain_available**](docs/SubdomainApi.md#subdomain_available) | **GET** /v1/parentdomains/{parentDomain}/subdomains/{subDomainName} | Returns subdomain availability
*SubdomainApi* | [**subdomain_claimed**](docs/SubdomainApi.md#subdomain_claimed) | **GET** /v1/parentdomains/{parentDomain}/claimed/{ethAddress} | Returns subdomain availability
*SubdomainApi* | [**subdomain_invalidate_claim_rate_limit**](docs/SubdomainApi.md#subdomain_invalidate_claim_rate_limit) | **DELETE** /v1/parentdomains/{parentDomain}/invalidate-claim-rate-limit | Invalidates the claim rate limit for the current IP
*SubdomainApi* | [**subdomain_list**](docs/SubdomainApi.md#subdomain_list) | **GET** /v1/parentdomains/{parentDomain}/list | Paginates over all subdomains in descending order of the creation date
*SubdomainApi* | [**subdomain_mint**](docs/SubdomainApi.md#subdomain_mint) | **POST** /v1/parentdomains/{parentDomain}/subdomains/{subDomainName} | Creates a subdomain for provided parentdomain
*SubdomainApi* | [**subdomain_mint_sig**](docs/SubdomainApi.md#subdomain_mint_sig) | **POST** /v1/parentdomains/{parentDomain}/subdomains/{subDomainName}/mint-with-sig | Creates a subdomain for provided parentdomain with signature
*SubdomainApi* | [**subdomain_per_day**](docs/SubdomainApi.md#subdomain_per_day) | **GET** /v1/parentdomains/{parentDomain}/per-day | Paginates over per-day aggregated counts for subdomains created given a parentdomain
*SubdomainApi* | [**subdomain_resolve**](docs/SubdomainApi.md#subdomain_resolve) | **GET** /v1/parentdomains/{parentDomain}/subdomains/{subDomainName}/resolve | Returns resolution of a provided subdomain
*SubdomainApi* | [**subdomain_reverse_resolve**](docs/SubdomainApi.md#subdomain_reverse_resolve) | **GET** /v1/parentdomains/{parentDomain}/addresses/{ethAddress}/reverse-resolve | Returns reverse-resolution of a provided eth address limited to provided parentdomain
*SubdomainApi* | [**subdomain_revoke**](docs/SubdomainApi.md#subdomain_revoke) | **DELETE** /v1/parentdomains/{parentDomain}/subdomains/{subDomainName} | Deletes a subdomain for provided parentdomain (Omnipotent)
*SubdomainApi* | [**subdomain_total**](docs/SubdomainApi.md#subdomain_total) | **GET** /v1/parentdomains/{parentDomain}/total | Returns the total number of subdomains registered to parentdomain


## Documentation For Models

 - [ApiAccessTokenCreateRequest](docs/ApiAccessTokenCreateRequest.md)
 - [ApiAccessTokenDeleteRequest](docs/ApiAccessTokenDeleteRequest.md)
 - [ApiAccessTokenResponse](docs/ApiAccessTokenResponse.md)
 - [ApiAddressRecord](docs/ApiAddressRecord.md)
 - [ApiAdminAccessTokenCreateRequest](docs/ApiAdminAccessTokenCreateRequest.md)
 - [ApiAdminPartnerCreateRequest](docs/ApiAdminPartnerCreateRequest.md)
 - [ApiBadRequestResponse](docs/ApiBadRequestResponse.md)
 - [ApiCoin](docs/ApiCoin.md)
 - [ApiCryptoPurchaseRequest](docs/ApiCryptoPurchaseRequest.md)
 - [ApiDNSRecord](docs/ApiDNSRecord.md)
 - [ApiDomainBasicInformation](docs/ApiDomainBasicInformation.md)
 - [ApiDomainMetadataAttribute](docs/ApiDomainMetadataAttribute.md)
 - [ApiDomainMetadataResponse](docs/ApiDomainMetadataResponse.md)
 - [ApiErrorResponse](docs/ApiErrorResponse.md)
 - [ApiGetAllDomainsResponse](docs/ApiGetAllDomainsResponse.md)
 - [ApiHNSBlockchainRecords](docs/ApiHNSBlockchainRecords.md)
 - [ApiHNSCreateDomainRequest](docs/ApiHNSCreateDomainRequest.md)
 - [ApiHNSCreateDomainWithWalletRequest](docs/ApiHNSCreateDomainWithWalletRequest.md)
 - [ApiHNSDomainAvailableResponse](docs/ApiHNSDomainAvailableResponse.md)
 - [ApiHNSRegisterTLDRequest](docs/ApiHNSRegisterTLDRequest.md)
 - [ApiHNSRegisterTLDResponse](docs/ApiHNSRegisterTLDResponse.md)
 - [ApiInternalServerErrorResponse](docs/ApiInternalServerErrorResponse.md)
 - [ApiMarketCryptoEstimation](docs/ApiMarketCryptoEstimation.md)
 - [ApiMarketCryptoEstimationResponse](docs/ApiMarketCryptoEstimationResponse.md)
 - [ApiMarketCryptoPurchaseResponse](docs/ApiMarketCryptoPurchaseResponse.md)
 - [ApiMarketListing](docs/ApiMarketListing.md)
 - [ApiMarketPurchaseResponse](docs/ApiMarketPurchaseResponse.md)
 - [ApiMarketSearchRequest](docs/ApiMarketSearchRequest.md)
 - [ApiMarketSearchResponse](docs/ApiMarketSearchResponse.md)
 - [ApiMarketSuggestRequest](docs/ApiMarketSuggestRequest.md)
 - [ApiMarketplaceOrderResponse](docs/ApiMarketplaceOrderResponse.md)
 - [ApiNameService](docs/ApiNameService.md)
 - [ApiParentDomainPurchaseRequest](docs/ApiParentDomainPurchaseRequest.md)
 - [ApiParentDomainPurchaseRequestDomainContactDetails](docs/ApiParentDomainPurchaseRequestDomainContactDetails.md)
 - [ApiParentDomainSearchResponse](docs/ApiParentDomainSearchResponse.md)
 - [ApiParentDomainValidationResponse](docs/ApiParentDomainValidationResponse.md)
 - [ApiPartnerResponse](docs/ApiPartnerResponse.md)
 - [ApiPurchaseListResponse](docs/ApiPurchaseListResponse.md)
 - [ApiPurchaseRequest](docs/ApiPurchaseRequest.md)
 - [ApiPurchaseResponse](docs/ApiPurchaseResponse.md)
 - [ApiResolveDomainResponse](docs/ApiResolveDomainResponse.md)
 - [ApiReverseResolutionDeleteRequest](docs/ApiReverseResolutionDeleteRequest.md)
 - [ApiSetReverseAddressRequest](docs/ApiSetReverseAddressRequest.md)
 - [ApiSubDomainAvailableResponse](docs/ApiSubDomainAvailableResponse.md)
 - [ApiSubDomainItem](docs/ApiSubDomainItem.md)
 - [ApiSubDomainListResponse](docs/ApiSubDomainListResponse.md)
 - [ApiSubDomainMintRequest](docs/ApiSubDomainMintRequest.md)
 - [ApiSubDomainMintWithSigRequest](docs/ApiSubDomainMintWithSigRequest.md)
 - [ApiSubDomainNameData](docs/ApiSubDomainNameData.md)
 - [ApiSubDomainPerDayCount](docs/ApiSubDomainPerDayCount.md)
 - [ApiSubDomainPerDayResponse](docs/ApiSubDomainPerDayResponse.md)
 - [ApiSubDomainResolveResponse](docs/ApiSubDomainResolveResponse.md)
 - [ApiSubDomainReverseResolveResponse](docs/ApiSubDomainReverseResolveResponse.md)
 - [ApiSubDomainTotalResponse](docs/ApiSubDomainTotalResponse.md)
 - [ApiSubdomainStatus](docs/ApiSubdomainStatus.md)
 - [ApiTXTRecord](docs/ApiTXTRecord.md)
 - [ApiWalletData](docs/ApiWalletData.md)
 - [ApiWalletLoginRequest](docs/ApiWalletLoginRequest.md)
 - [ApiWalletMessageResponse](docs/ApiWalletMessageResponse.md)
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


