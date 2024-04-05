# ApiSubDomainResolveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**name_data** | [**ApiSubDomainNameData**](ApiSubDomainNameData.md) |  | [optional] 

## Example

```python
from superlink.models.api_sub_domain_resolve_response import ApiSubDomainResolveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSubDomainResolveResponse from a JSON string
api_sub_domain_resolve_response_instance = ApiSubDomainResolveResponse.from_json(json)
# print the JSON string representation of the object
print(ApiSubDomainResolveResponse.to_json())

# convert the object into a dict
api_sub_domain_resolve_response_dict = api_sub_domain_resolve_response_instance.to_dict()
# create an instance of ApiSubDomainResolveResponse from a dict
api_sub_domain_resolve_response_form_dict = api_sub_domain_resolve_response.from_dict(api_sub_domain_resolve_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


