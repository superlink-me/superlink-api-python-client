# ApiMarketSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addrs** | [**List[ApiAddressRecord]**](ApiAddressRecord.md) |  | [optional] 
**query** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_market_search_request import ApiMarketSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMarketSearchRequest from a JSON string
api_market_search_request_instance = ApiMarketSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiMarketSearchRequest.to_json())

# convert the object into a dict
api_market_search_request_dict = api_market_search_request_instance.to_dict()
# create an instance of ApiMarketSearchRequest from a dict
api_market_search_request_form_dict = api_market_search_request.from_dict(api_market_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


