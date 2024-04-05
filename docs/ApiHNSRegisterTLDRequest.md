# ApiHNSRegisterTLDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** |  | [optional] 
**tld** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_hns_register_tld_request import ApiHNSRegisterTLDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHNSRegisterTLDRequest from a JSON string
api_hns_register_tld_request_instance = ApiHNSRegisterTLDRequest.from_json(json)
# print the JSON string representation of the object
print(ApiHNSRegisterTLDRequest.to_json())

# convert the object into a dict
api_hns_register_tld_request_dict = api_hns_register_tld_request_instance.to_dict()
# create an instance of ApiHNSRegisterTLDRequest from a dict
api_hns_register_tld_request_form_dict = api_hns_register_tld_request.from_dict(api_hns_register_tld_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


