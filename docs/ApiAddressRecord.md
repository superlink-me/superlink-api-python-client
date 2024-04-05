# ApiAddressRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr** | **str** |  | [optional] 
**coin_id** | **int** |  | [optional] 

## Example

```python
from superlink.models.api_address_record import ApiAddressRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAddressRecord from a JSON string
api_address_record_instance = ApiAddressRecord.from_json(json)
# print the JSON string representation of the object
print(ApiAddressRecord.to_json())

# convert the object into a dict
api_address_record_dict = api_address_record_instance.to_dict()
# create an instance of ApiAddressRecord from a dict
api_address_record_form_dict = api_address_record.from_dict(api_address_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


