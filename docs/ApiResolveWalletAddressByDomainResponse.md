# ApiResolveWalletAddressByDomainResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**records** | [**List[ApiDNSRecord]**](ApiDNSRecord.md) |  | [optional] 
**wallets** | [**List[ApiWalletData]**](ApiWalletData.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_resolve_wallet_address_by_domain_response import ApiResolveWalletAddressByDomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResolveWalletAddressByDomainResponse from a JSON string
api_resolve_wallet_address_by_domain_response_instance = ApiResolveWalletAddressByDomainResponse.from_json(json)
# print the JSON string representation of the object
print ApiResolveWalletAddressByDomainResponse.to_json()

# convert the object into a dict
api_resolve_wallet_address_by_domain_response_dict = api_resolve_wallet_address_by_domain_response_instance.to_dict()
# create an instance of ApiResolveWalletAddressByDomainResponse from a dict
api_resolve_wallet_address_by_domain_response_form_dict = api_resolve_wallet_address_by_domain_response.from_dict(api_resolve_wallet_address_by_domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


