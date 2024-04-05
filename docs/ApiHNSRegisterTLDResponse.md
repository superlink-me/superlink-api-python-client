# ApiHNSRegisterTLDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**ApiHNSBlockchainRecords**](ApiHNSBlockchainRecords.md) |  | [optional] 
**tld** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_hns_register_tld_response import ApiHNSRegisterTLDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHNSRegisterTLDResponse from a JSON string
api_hns_register_tld_response_instance = ApiHNSRegisterTLDResponse.from_json(json)
# print the JSON string representation of the object
print(ApiHNSRegisterTLDResponse.to_json())

# convert the object into a dict
api_hns_register_tld_response_dict = api_hns_register_tld_response_instance.to_dict()
# create an instance of ApiHNSRegisterTLDResponse from a dict
api_hns_register_tld_response_form_dict = api_hns_register_tld_response.from_dict(api_hns_register_tld_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


