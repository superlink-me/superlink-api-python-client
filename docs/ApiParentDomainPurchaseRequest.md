# ApiParentDomainPurchaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_contact_details** | [**ApiParentDomainPurchaseRequestDomainContactDetails**](ApiParentDomainPurchaseRequestDomainContactDetails.md) |  | [optional] 

## Example

```python
from superlink.models.api_parent_domain_purchase_request import ApiParentDomainPurchaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiParentDomainPurchaseRequest from a JSON string
api_parent_domain_purchase_request_instance = ApiParentDomainPurchaseRequest.from_json(json)
# print the JSON string representation of the object
print(ApiParentDomainPurchaseRequest.to_json())

# convert the object into a dict
api_parent_domain_purchase_request_dict = api_parent_domain_purchase_request_instance.to_dict()
# create an instance of ApiParentDomainPurchaseRequest from a dict
api_parent_domain_purchase_request_form_dict = api_parent_domain_purchase_request.from_dict(api_parent_domain_purchase_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


