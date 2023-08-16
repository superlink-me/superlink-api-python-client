# ApiMarketSearchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_listings** | [**List[ApiMarketListing]**](ApiMarketListing.md) |  | [optional] 

## Example

```python
from superlink.models.api_market_search_response import ApiMarketSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMarketSearchResponse from a JSON string
api_market_search_response_instance = ApiMarketSearchResponse.from_json(json)
# print the JSON string representation of the object
print ApiMarketSearchResponse.to_json()

# convert the object into a dict
api_market_search_response_dict = api_market_search_response_instance.to_dict()
# create an instance of ApiMarketSearchResponse from a dict
api_market_search_response_form_dict = api_market_search_response.from_dict(api_market_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


