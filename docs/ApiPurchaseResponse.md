# ApiPurchaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**name_service** | **str** |  | [optional] 
**owner_address** | **str** |  | [optional] 
**partner_id** | **str** |  | [optional] 
**price** | **float** |  | [optional] 

## Example

```python
from superlink.models.api_purchase_response import ApiPurchaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPurchaseResponse from a JSON string
api_purchase_response_instance = ApiPurchaseResponse.from_json(json)
# print the JSON string representation of the object
print(ApiPurchaseResponse.to_json())

# convert the object into a dict
api_purchase_response_dict = api_purchase_response_instance.to_dict()
# create an instance of ApiPurchaseResponse from a dict
api_purchase_response_form_dict = api_purchase_response.from_dict(api_purchase_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


