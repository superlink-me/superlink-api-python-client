# ApiTXTRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_txt_record import ApiTXTRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTXTRecord from a JSON string
api_txt_record_instance = ApiTXTRecord.from_json(json)
# print the JSON string representation of the object
print ApiTXTRecord.to_json()

# convert the object into a dict
api_txt_record_dict = api_txt_record_instance.to_dict()
# create an instance of ApiTXTRecord from a dict
api_txt_record_form_dict = api_txt_record.from_dict(api_txt_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


