# ApiPartnerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_partner_response import ApiPartnerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPartnerResponse from a JSON string
api_partner_response_instance = ApiPartnerResponse.from_json(json)
# print the JSON string representation of the object
print ApiPartnerResponse.to_json()

# convert the object into a dict
api_partner_response_dict = api_partner_response_instance.to_dict()
# create an instance of ApiPartnerResponse from a dict
api_partner_response_form_dict = api_partner_response.from_dict(api_partner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


