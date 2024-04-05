# ApiWalletLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**signed_message** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_wallet_login_request import ApiWalletLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWalletLoginRequest from a JSON string
api_wallet_login_request_instance = ApiWalletLoginRequest.from_json(json)
# print the JSON string representation of the object
print(ApiWalletLoginRequest.to_json())

# convert the object into a dict
api_wallet_login_request_dict = api_wallet_login_request_instance.to_dict()
# create an instance of ApiWalletLoginRequest from a dict
api_wallet_login_request_form_dict = api_wallet_login_request.from_dict(api_wallet_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


