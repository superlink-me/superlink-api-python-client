# ApiAccessTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**valid_from** | **str** |  | [optional] 
**valid_till** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_access_token_response import ApiAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAccessTokenResponse from a JSON string
api_access_token_response_instance = ApiAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print ApiAccessTokenResponse.to_json()

# convert the object into a dict
api_access_token_response_dict = api_access_token_response_instance.to_dict()
# create an instance of ApiAccessTokenResponse from a dict
api_access_token_response_form_dict = api_access_token_response.from_dict(api_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


