# ApiMarketCryptoEstimationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimations** | [**List[ApiMarketCryptoEstimation]**](ApiMarketCryptoEstimation.md) |  | [optional] 

## Example

```python
from superlink.models.api_market_crypto_estimation_response import ApiMarketCryptoEstimationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMarketCryptoEstimationResponse from a JSON string
api_market_crypto_estimation_response_instance = ApiMarketCryptoEstimationResponse.from_json(json)
# print the JSON string representation of the object
print ApiMarketCryptoEstimationResponse.to_json()

# convert the object into a dict
api_market_crypto_estimation_response_dict = api_market_crypto_estimation_response_instance.to_dict()
# create an instance of ApiMarketCryptoEstimationResponse from a dict
api_market_crypto_estimation_response_form_dict = api_market_crypto_estimation_response.from_dict(api_market_crypto_estimation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


