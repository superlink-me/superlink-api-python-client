# ApiPurchaseRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_email_address** | **str** |  | [optional] 
**customer_name** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**owner_address** | **str** |  | [optional] 
**stripe_connected_account_id** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_purchase_request import ApiPurchaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPurchaseRequest from a JSON string
api_purchase_request_instance = ApiPurchaseRequest.from_json(json)
# print the JSON string representation of the object
print ApiPurchaseRequest.to_json()

# convert the object into a dict
api_purchase_request_dict = api_purchase_request_instance.to_dict()
# create an instance of ApiPurchaseRequest from a dict
api_purchase_request_form_dict = api_purchase_request.from_dict(api_purchase_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


