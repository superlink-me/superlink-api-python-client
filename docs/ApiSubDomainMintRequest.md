# ApiSubDomainMintRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_data** | [**ApiSubDomainNameData**](ApiSubDomainNameData.md) |  | [optional] 

## Example

```python
from superlink.models.api_sub_domain_mint_request import ApiSubDomainMintRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSubDomainMintRequest from a JSON string
api_sub_domain_mint_request_instance = ApiSubDomainMintRequest.from_json(json)
# print the JSON string representation of the object
print(ApiSubDomainMintRequest.to_json())

# convert the object into a dict
api_sub_domain_mint_request_dict = api_sub_domain_mint_request_instance.to_dict()
# create an instance of ApiSubDomainMintRequest from a dict
api_sub_domain_mint_request_form_dict = api_sub_domain_mint_request.from_dict(api_sub_domain_mint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


