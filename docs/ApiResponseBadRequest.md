# ApiResponseBadRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ApiResponseError]**](ApiResponseError.md) |  | [optional] 

## Example

```python
from SuperlinkAPI.models.api_response_bad_request import ApiResponseBadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseBadRequest from a JSON string
api_response_bad_request_instance = ApiResponseBadRequest.from_json(json)
# print the JSON string representation of the object
print ApiResponseBadRequest.to_json()

# convert the object into a dict
api_response_bad_request_dict = api_response_bad_request_instance.to_dict()
# create an instance of ApiResponseBadRequest from a dict
api_response_bad_request_form_dict = api_response_bad_request.from_dict(api_response_bad_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


