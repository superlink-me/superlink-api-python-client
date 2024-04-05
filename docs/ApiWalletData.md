# ApiWalletData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**coin** | [**ApiCoin**](ApiCoin.md) |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_wallet_data import ApiWalletData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiWalletData from a JSON string
api_wallet_data_instance = ApiWalletData.from_json(json)
# print the JSON string representation of the object
print(ApiWalletData.to_json())

# convert the object into a dict
api_wallet_data_dict = api_wallet_data_instance.to_dict()
# create an instance of ApiWalletData from a dict
api_wallet_data_form_dict = api_wallet_data.from_dict(api_wallet_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


