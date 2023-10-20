# ApiCryptoPurchaseRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**demo** | **bool** |  | [optional] 
**domain** | **str** |  | [optional] 
**owner_address** | **str** |  | [optional] 
**owner_email** | **str** |  | [optional] 
**years** | **int** |  | [optional] 

## Example

```python
from superlink.models.api_crypto_purchase_request import ApiCryptoPurchaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCryptoPurchaseRequest from a JSON string
api_crypto_purchase_request_instance = ApiCryptoPurchaseRequest.from_json(json)
# print the JSON string representation of the object
print ApiCryptoPurchaseRequest.to_json()

# convert the object into a dict
api_crypto_purchase_request_dict = api_crypto_purchase_request_instance.to_dict()
# create an instance of ApiCryptoPurchaseRequest from a dict
api_crypto_purchase_request_form_dict = api_crypto_purchase_request.from_dict(api_crypto_purchase_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


