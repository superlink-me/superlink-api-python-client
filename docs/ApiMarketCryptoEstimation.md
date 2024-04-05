# ApiMarketCryptoEstimation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exhange_rate** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from superlink.models.api_market_crypto_estimation import ApiMarketCryptoEstimation

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMarketCryptoEstimation from a JSON string
api_market_crypto_estimation_instance = ApiMarketCryptoEstimation.from_json(json)
# print the JSON string representation of the object
print(ApiMarketCryptoEstimation.to_json())

# convert the object into a dict
api_market_crypto_estimation_dict = api_market_crypto_estimation_instance.to_dict()
# create an instance of ApiMarketCryptoEstimation from a dict
api_market_crypto_estimation_form_dict = api_market_crypto_estimation.from_dict(api_market_crypto_estimation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


