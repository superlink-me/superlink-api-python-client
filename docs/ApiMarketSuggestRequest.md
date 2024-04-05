# ApiMarketSuggestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addrs** | [**List[ApiAddressRecord]**](ApiAddressRecord.md) |  | [optional] 
**query** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_market_suggest_request import ApiMarketSuggestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMarketSuggestRequest from a JSON string
api_market_suggest_request_instance = ApiMarketSuggestRequest.from_json(json)
# print the JSON string representation of the object
print(ApiMarketSuggestRequest.to_json())

# convert the object into a dict
api_market_suggest_request_dict = api_market_suggest_request_instance.to_dict()
# create an instance of ApiMarketSuggestRequest from a dict
api_market_suggest_request_form_dict = api_market_suggest_request.from_dict(api_market_suggest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


