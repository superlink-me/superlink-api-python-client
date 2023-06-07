# ApiDNSRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ttl** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_dns_record import ApiDNSRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDNSRecord from a JSON string
api_dns_record_instance = ApiDNSRecord.from_json(json)
# print the JSON string representation of the object
print ApiDNSRecord.to_json()

# convert the object into a dict
api_dns_record_dict = api_dns_record_instance.to_dict()
# create an instance of ApiDNSRecord from a dict
api_dns_record_form_dict = api_dns_record.from_dict(api_dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


