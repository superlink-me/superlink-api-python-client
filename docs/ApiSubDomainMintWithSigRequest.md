# ApiSubDomainMintWithSigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**name_data** | [**ApiSubDomainNameData**](ApiSubDomainNameData.md) |  | [optional] 
**signed_message** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_sub_domain_mint_with_sig_request import ApiSubDomainMintWithSigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSubDomainMintWithSigRequest from a JSON string
api_sub_domain_mint_with_sig_request_instance = ApiSubDomainMintWithSigRequest.from_json(json)
# print the JSON string representation of the object
print(ApiSubDomainMintWithSigRequest.to_json())

# convert the object into a dict
api_sub_domain_mint_with_sig_request_dict = api_sub_domain_mint_with_sig_request_instance.to_dict()
# create an instance of ApiSubDomainMintWithSigRequest from a dict
api_sub_domain_mint_with_sig_request_form_dict = api_sub_domain_mint_with_sig_request.from_dict(api_sub_domain_mint_with_sig_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


