# ApiHNSCreateDomainWithWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **Dict[str, str]** |  | [optional] 
**domain** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**owner_address** | **str** |  | [optional] 
**signed_message** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_hns_create_domain_with_wallet_request import ApiHNSCreateDomainWithWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHNSCreateDomainWithWalletRequest from a JSON string
api_hns_create_domain_with_wallet_request_instance = ApiHNSCreateDomainWithWalletRequest.from_json(json)
# print the JSON string representation of the object
print(ApiHNSCreateDomainWithWalletRequest.to_json())

# convert the object into a dict
api_hns_create_domain_with_wallet_request_dict = api_hns_create_domain_with_wallet_request_instance.to_dict()
# create an instance of ApiHNSCreateDomainWithWalletRequest from a dict
api_hns_create_domain_with_wallet_request_form_dict = api_hns_create_domain_with_wallet_request.from_dict(api_hns_create_domain_with_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


