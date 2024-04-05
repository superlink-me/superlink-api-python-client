# ApiGetAllDomainsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[ApiDomainBasicInformation]**](ApiDomainBasicInformation.md) |  | [optional] 

## Example

```python
from superlink.models.api_get_all_domains_response import ApiGetAllDomainsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiGetAllDomainsResponse from a JSON string
api_get_all_domains_response_instance = ApiGetAllDomainsResponse.from_json(json)
# print the JSON string representation of the object
print(ApiGetAllDomainsResponse.to_json())

# convert the object into a dict
api_get_all_domains_response_dict = api_get_all_domains_response_instance.to_dict()
# create an instance of ApiGetAllDomainsResponse from a dict
api_get_all_domains_response_form_dict = api_get_all_domains_response.from_dict(api_get_all_domains_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


