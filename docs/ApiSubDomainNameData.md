# ApiSubDomainNameData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **Dict[str, str]** |  | [optional] 
**contenthash** | **str** |  | [optional] 
**text** | **Dict[str, str]** |  | [optional] 

## Example

```python
from superlink.models.api_sub_domain_name_data import ApiSubDomainNameData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSubDomainNameData from a JSON string
api_sub_domain_name_data_instance = ApiSubDomainNameData.from_json(json)
# print the JSON string representation of the object
print(ApiSubDomainNameData.to_json())

# convert the object into a dict
api_sub_domain_name_data_dict = api_sub_domain_name_data_instance.to_dict()
# create an instance of ApiSubDomainNameData from a dict
api_sub_domain_name_data_form_dict = api_sub_domain_name_data.from_dict(api_sub_domain_name_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


