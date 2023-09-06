# ApiMarketListing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**name_service** | **str** |  | [optional] 
**price** | **Dict[str, float]** |  | [optional] 

## Example

```python
from superlink.models.api_market_listing import ApiMarketListing

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMarketListing from a JSON string
api_market_listing_instance = ApiMarketListing.from_json(json)
# print the JSON string representation of the object
print ApiMarketListing.to_json()

# convert the object into a dict
api_market_listing_dict = api_market_listing_instance.to_dict()
# create an instance of ApiMarketListing from a dict
api_market_listing_form_dict = api_market_listing.from_dict(api_market_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


