# ApiAccessToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**type** | [**ApiAccessTokenType**](ApiAccessTokenType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**valid_from** | **str** |  | [optional] 
**valid_till** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from Superlink.models.api_access_token import ApiAccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAccessToken from a JSON string
api_access_token_instance = ApiAccessToken.from_json(json)
# print the JSON string representation of the object
print ApiAccessToken.to_json()

# convert the object into a dict
api_access_token_dict = api_access_token_instance.to_dict()
# create an instance of ApiAccessToken from a dict
api_access_token_form_dict = api_access_token.from_dict(api_access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


