# ApiDomainMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**animation_url** | **str** |  | [optional] 
**attributes** | [**List[ApiDomainMetadataAttribute]**](ApiDomainMetadataAttribute.md) |  | [optional] 
**avatar** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**external_url** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**namehash** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_domain_metadata_response import ApiDomainMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDomainMetadataResponse from a JSON string
api_domain_metadata_response_instance = ApiDomainMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(ApiDomainMetadataResponse.to_json())

# convert the object into a dict
api_domain_metadata_response_dict = api_domain_metadata_response_instance.to_dict()
# create an instance of ApiDomainMetadataResponse from a dict
api_domain_metadata_response_form_dict = api_domain_metadata_response.from_dict(api_domain_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


