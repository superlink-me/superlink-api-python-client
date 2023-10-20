# ApiMarketplaceOrderResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_currency** | **str** |  | [optional] 
**base_price** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name_service** | **str** |  | [optional] 
**order_status** | **str** |  | [optional] 
**order_status_reason** | **str** |  | [optional] 
**owner_address** | **str** |  | [optional] 
**payment_reference_id** | **str** |  | [optional] 
**payment_type** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_marketplace_order_response import ApiMarketplaceOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMarketplaceOrderResponse from a JSON string
api_marketplace_order_response_instance = ApiMarketplaceOrderResponse.from_json(json)
# print the JSON string representation of the object
print ApiMarketplaceOrderResponse.to_json()

# convert the object into a dict
api_marketplace_order_response_dict = api_marketplace_order_response_instance.to_dict()
# create an instance of ApiMarketplaceOrderResponse from a dict
api_marketplace_order_response_form_dict = api_marketplace_order_response.from_dict(api_marketplace_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


