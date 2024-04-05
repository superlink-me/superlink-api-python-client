# ApiPurchaseListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchases** | [**List[ApiPurchaseResponse]**](ApiPurchaseResponse.md) |  | [optional] 

## Example

```python
from superlink.models.api_purchase_list_response import ApiPurchaseListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPurchaseListResponse from a JSON string
api_purchase_list_response_instance = ApiPurchaseListResponse.from_json(json)
# print the JSON string representation of the object
print(ApiPurchaseListResponse.to_json())

# convert the object into a dict
api_purchase_list_response_dict = api_purchase_list_response_instance.to_dict()
# create an instance of ApiPurchaseListResponse from a dict
api_purchase_list_response_form_dict = api_purchase_list_response.from_dict(api_purchase_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


