# ApiSubDomainItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_timestamp** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_sub_domain_item import ApiSubDomainItem

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSubDomainItem from a JSON string
api_sub_domain_item_instance = ApiSubDomainItem.from_json(json)
# print the JSON string representation of the object
print(ApiSubDomainItem.to_json())

# convert the object into a dict
api_sub_domain_item_dict = api_sub_domain_item_instance.to_dict()
# create an instance of ApiSubDomainItem from a dict
api_sub_domain_item_form_dict = api_sub_domain_item.from_dict(api_sub_domain_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


