# ApiAccessTokenCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**valid_from** | **str** |  | [optional] 
**valid_till** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_access_token_create_request import ApiAccessTokenCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAccessTokenCreateRequest from a JSON string
api_access_token_create_request_instance = ApiAccessTokenCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiAccessTokenCreateRequest.to_json())

# convert the object into a dict
api_access_token_create_request_dict = api_access_token_create_request_instance.to_dict()
# create an instance of ApiAccessTokenCreateRequest from a dict
api_access_token_create_request_form_dict = api_access_token_create_request.from_dict(api_access_token_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


