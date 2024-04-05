# ApiWalletMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_wallet_message_response import ApiWalletMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWalletMessageResponse from a JSON string
api_wallet_message_response_instance = ApiWalletMessageResponse.from_json(json)
# print the JSON string representation of the object
print(ApiWalletMessageResponse.to_json())

# convert the object into a dict
api_wallet_message_response_dict = api_wallet_message_response_instance.to_dict()
# create an instance of ApiWalletMessageResponse from a dict
api_wallet_message_response_form_dict = api_wallet_message_response.from_dict(api_wallet_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


