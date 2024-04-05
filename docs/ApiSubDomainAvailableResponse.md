# ApiSubDomainAvailableResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**status** | [**ApiSubdomainStatus**](ApiSubdomainStatus.md) |  | [optional] 

## Example

```python
from superlink.models.api_sub_domain_available_response import ApiSubDomainAvailableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSubDomainAvailableResponse from a JSON string
api_sub_domain_available_response_instance = ApiSubDomainAvailableResponse.from_json(json)
# print the JSON string representation of the object
print(ApiSubDomainAvailableResponse.to_json())

# convert the object into a dict
api_sub_domain_available_response_dict = api_sub_domain_available_response_instance.to_dict()
# create an instance of ApiSubDomainAvailableResponse from a dict
api_sub_domain_available_response_form_dict = api_sub_domain_available_response.from_dict(api_sub_domain_available_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


