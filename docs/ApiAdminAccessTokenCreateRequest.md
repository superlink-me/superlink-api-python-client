# ApiAdminAccessTokenCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**partner_id** | **str** |  | [optional] 
**type** | [**DataAccessTokenType**](DataAccessTokenType.md) |  | [optional] 
**valid_from** | **str** |  | [optional] 
**valid_till** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_admin_access_token_create_request import ApiAdminAccessTokenCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAdminAccessTokenCreateRequest from a JSON string
api_admin_access_token_create_request_instance = ApiAdminAccessTokenCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiAdminAccessTokenCreateRequest.to_json())

# convert the object into a dict
api_admin_access_token_create_request_dict = api_admin_access_token_create_request_instance.to_dict()
# create an instance of ApiAdminAccessTokenCreateRequest from a dict
api_admin_access_token_create_request_form_dict = api_admin_access_token_create_request.from_dict(api_admin_access_token_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


