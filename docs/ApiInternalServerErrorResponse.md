# ApiInternalServerErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_internal_server_error_response import ApiInternalServerErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInternalServerErrorResponse from a JSON string
api_internal_server_error_response_instance = ApiInternalServerErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ApiInternalServerErrorResponse.to_json())

# convert the object into a dict
api_internal_server_error_response_dict = api_internal_server_error_response_instance.to_dict()
# create an instance of ApiInternalServerErrorResponse from a dict
api_internal_server_error_response_form_dict = api_internal_server_error_response.from_dict(api_internal_server_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


