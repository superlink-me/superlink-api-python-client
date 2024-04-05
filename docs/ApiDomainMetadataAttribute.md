# ApiDomainMetadataAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trait_type** | **str** |  | [optional] 
**value** | **object** | This can be string or int | [optional] 

## Example

```python
from superlink.models.api_domain_metadata_attribute import ApiDomainMetadataAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDomainMetadataAttribute from a JSON string
api_domain_metadata_attribute_instance = ApiDomainMetadataAttribute.from_json(json)
# print the JSON string representation of the object
print(ApiDomainMetadataAttribute.to_json())

# convert the object into a dict
api_domain_metadata_attribute_dict = api_domain_metadata_attribute_instance.to_dict()
# create an instance of ApiDomainMetadataAttribute from a dict
api_domain_metadata_attribute_form_dict = api_domain_metadata_attribute.from_dict(api_domain_metadata_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


