# ApiMarketPurchaseResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_id** | **str** |  | [optional] 
**stripe_customer_id** | **str** |  | [optional] 
**stripe_ephemeral_key** | **str** |  | [optional] 
**stripe_payment_intent** | **str** |  | [optional] 
**stripe_publishable_key** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_market_purchase_response import ApiMarketPurchaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMarketPurchaseResponse from a JSON string
api_market_purchase_response_instance = ApiMarketPurchaseResponse.from_json(json)
# print the JSON string representation of the object
print ApiMarketPurchaseResponse.to_json()

# convert the object into a dict
api_market_purchase_response_dict = api_market_purchase_response_instance.to_dict()
# create an instance of ApiMarketPurchaseResponse from a dict
api_market_purchase_response_form_dict = api_market_purchase_response.from_dict(api_market_purchase_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


