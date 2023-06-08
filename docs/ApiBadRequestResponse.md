# ApiBadRequestResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ApiErrorResponse]**](ApiErrorResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_bad_request_response import ApiBadRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiBadRequestResponse from a JSON string
api_bad_request_response_instance = ApiBadRequestResponse.from_json(json)
# print the JSON string representation of the object
print ApiBadRequestResponse.to_json()

# convert the object into a dict
api_bad_request_response_dict = api_bad_request_response_instance.to_dict()
# create an instance of ApiBadRequestResponse from a dict
api_bad_request_response_form_dict = api_bad_request_response.from_dict(api_bad_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


