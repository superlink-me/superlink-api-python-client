# ApiHNSDomainAvailableResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**status** | [**ApiSubdomainStatus**](ApiSubdomainStatus.md) |  | [optional] 

## Example

```python
from superlink.models.api_hns_domain_available_response import ApiHNSDomainAvailableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHNSDomainAvailableResponse from a JSON string
api_hns_domain_available_response_instance = ApiHNSDomainAvailableResponse.from_json(json)
# print the JSON string representation of the object
print(ApiHNSDomainAvailableResponse.to_json())

# convert the object into a dict
api_hns_domain_available_response_dict = api_hns_domain_available_response_instance.to_dict()
# create an instance of ApiHNSDomainAvailableResponse from a dict
api_hns_domain_available_response_form_dict = api_hns_domain_available_response.from_dict(api_hns_domain_available_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


