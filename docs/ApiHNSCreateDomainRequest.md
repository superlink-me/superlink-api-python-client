# ApiHNSCreateDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **Dict[str, str]** |  | [optional] 
**domain** | **str** |  | [optional] 
**owner_address** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_hns_create_domain_request import ApiHNSCreateDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHNSCreateDomainRequest from a JSON string
api_hns_create_domain_request_instance = ApiHNSCreateDomainRequest.from_json(json)
# print the JSON string representation of the object
print(ApiHNSCreateDomainRequest.to_json())

# convert the object into a dict
api_hns_create_domain_request_dict = api_hns_create_domain_request_instance.to_dict()
# create an instance of ApiHNSCreateDomainRequest from a dict
api_hns_create_domain_request_form_dict = api_hns_create_domain_request.from_dict(api_hns_create_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


