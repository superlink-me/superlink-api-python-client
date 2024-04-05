# ApiParentDomainPurchaseRequestDomainContactDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name_first** | **str** |  | [optional] 
**name_last** | **str** |  | [optional] 
**phone_country_code** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_parent_domain_purchase_request_domain_contact_details import ApiParentDomainPurchaseRequestDomainContactDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApiParentDomainPurchaseRequestDomainContactDetails from a JSON string
api_parent_domain_purchase_request_domain_contact_details_instance = ApiParentDomainPurchaseRequestDomainContactDetails.from_json(json)
# print the JSON string representation of the object
print(ApiParentDomainPurchaseRequestDomainContactDetails.to_json())

# convert the object into a dict
api_parent_domain_purchase_request_domain_contact_details_dict = api_parent_domain_purchase_request_domain_contact_details_instance.to_dict()
# create an instance of ApiParentDomainPurchaseRequestDomainContactDetails from a dict
api_parent_domain_purchase_request_domain_contact_details_form_dict = api_parent_domain_purchase_request_domain_contact_details.from_dict(api_parent_domain_purchase_request_domain_contact_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


