# ApiResolveDomainResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_hash** | **str** |  | [optional] 
**dns_records** | [**List[ApiDNSRecord]**](ApiDNSRecord.md) |  | [optional] 
**domain** | **str** |  | [optional] 
**name_service** | [**ApiNameService**](ApiNameService.md) |  | [optional] 
**owner_address** | **str** |  | [optional] 
**txt_records** | [**List[ApiTXTRecord]**](ApiTXTRecord.md) |  | [optional] 
**wallets** | [**List[ApiWalletData]**](ApiWalletData.md) |  | [optional] 

## Example

```python
from superlink.models.api_resolve_domain_response import ApiResolveDomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResolveDomainResponse from a JSON string
api_resolve_domain_response_instance = ApiResolveDomainResponse.from_json(json)
# print the JSON string representation of the object
print(ApiResolveDomainResponse.to_json())

# convert the object into a dict
api_resolve_domain_response_dict = api_resolve_domain_response_instance.to_dict()
# create an instance of ApiResolveDomainResponse from a dict
api_resolve_domain_response_form_dict = api_resolve_domain_response.from_dict(api_resolve_domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


