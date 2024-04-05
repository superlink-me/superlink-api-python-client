# ApiParentDomainSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_parent_domain** | **List[str]** |  | [optional] 

## Example

```python
from superlink.models.api_parent_domain_search_response import ApiParentDomainSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiParentDomainSearchResponse from a JSON string
api_parent_domain_search_response_instance = ApiParentDomainSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ApiParentDomainSearchResponse.to_json())

# convert the object into a dict
api_parent_domain_search_response_dict = api_parent_domain_search_response_instance.to_dict()
# create an instance of ApiParentDomainSearchResponse from a dict
api_parent_domain_search_response_form_dict = api_parent_domain_search_response.from_dict(api_parent_domain_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


