# ApiSubDomainPerDayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregates** | [**List[ApiSubDomainPerDayCount]**](ApiSubDomainPerDayCount.md) |  | [optional] 
**next_pagination_token** | **str** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from superlink.models.api_sub_domain_per_day_response import ApiSubDomainPerDayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSubDomainPerDayResponse from a JSON string
api_sub_domain_per_day_response_instance = ApiSubDomainPerDayResponse.from_json(json)
# print the JSON string representation of the object
print(ApiSubDomainPerDayResponse.to_json())

# convert the object into a dict
api_sub_domain_per_day_response_dict = api_sub_domain_per_day_response_instance.to_dict()
# create an instance of ApiSubDomainPerDayResponse from a dict
api_sub_domain_per_day_response_form_dict = api_sub_domain_per_day_response.from_dict(api_sub_domain_per_day_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


