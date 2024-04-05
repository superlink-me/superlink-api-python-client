# ApiParentDomainValidationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_domain** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from superlink.models.api_parent_domain_validation_response import ApiParentDomainValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiParentDomainValidationResponse from a JSON string
api_parent_domain_validation_response_instance = ApiParentDomainValidationResponse.from_json(json)
# print the JSON string representation of the object
print(ApiParentDomainValidationResponse.to_json())

# convert the object into a dict
api_parent_domain_validation_response_dict = api_parent_domain_validation_response_instance.to_dict()
# create an instance of ApiParentDomainValidationResponse from a dict
api_parent_domain_validation_response_form_dict = api_parent_domain_validation_response.from_dict(api_parent_domain_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


