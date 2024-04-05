# ApiSetReverseAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**signed_message** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_set_reverse_address_request import ApiSetReverseAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSetReverseAddressRequest from a JSON string
api_set_reverse_address_request_instance = ApiSetReverseAddressRequest.from_json(json)
# print the JSON string representation of the object
print(ApiSetReverseAddressRequest.to_json())

# convert the object into a dict
api_set_reverse_address_request_dict = api_set_reverse_address_request_instance.to_dict()
# create an instance of ApiSetReverseAddressRequest from a dict
api_set_reverse_address_request_form_dict = api_set_reverse_address_request.from_dict(api_set_reverse_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


