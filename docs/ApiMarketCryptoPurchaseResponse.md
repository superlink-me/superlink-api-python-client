# ApiMarketCryptoPurchaseResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**amount** | **float** | PaymentDetails     CryptoPaymentDetails &#x60;json:\&quot;paymentDetails\&quot;&#x60; | [optional] 
**expiry_date_epoch** | **int** |  | [optional] 
**order_id** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_market_crypto_purchase_response import ApiMarketCryptoPurchaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMarketCryptoPurchaseResponse from a JSON string
api_market_crypto_purchase_response_instance = ApiMarketCryptoPurchaseResponse.from_json(json)
# print the JSON string representation of the object
print ApiMarketCryptoPurchaseResponse.to_json()

# convert the object into a dict
api_market_crypto_purchase_response_dict = api_market_crypto_purchase_response_instance.to_dict()
# create an instance of ApiMarketCryptoPurchaseResponse from a dict
api_market_crypto_purchase_response_form_dict = api_market_crypto_purchase_response.from_dict(api_market_crypto_purchase_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


