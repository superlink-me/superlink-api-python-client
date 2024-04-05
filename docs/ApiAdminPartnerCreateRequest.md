# ApiAdminPartnerCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_admin_partner_create_request import ApiAdminPartnerCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAdminPartnerCreateRequest from a JSON string
api_admin_partner_create_request_instance = ApiAdminPartnerCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiAdminPartnerCreateRequest.to_json())

# convert the object into a dict
api_admin_partner_create_request_dict = api_admin_partner_create_request_instance.to_dict()
# create an instance of ApiAdminPartnerCreateRequest from a dict
api_admin_partner_create_request_form_dict = api_admin_partner_create_request.from_dict(api_admin_partner_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


