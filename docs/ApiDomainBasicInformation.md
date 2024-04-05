# ApiDomainBasicInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_domain_basic_information import ApiDomainBasicInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDomainBasicInformation from a JSON string
api_domain_basic_information_instance = ApiDomainBasicInformation.from_json(json)
# print the JSON string representation of the object
print(ApiDomainBasicInformation.to_json())

# convert the object into a dict
api_domain_basic_information_dict = api_domain_basic_information_instance.to_dict()
# create an instance of ApiDomainBasicInformation from a dict
api_domain_basic_information_form_dict = api_domain_basic_information.from_dict(api_domain_basic_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


