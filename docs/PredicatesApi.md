# kpTranslator.PredicatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**predicates_get**](PredicatesApi.md#predicates_get) | **GET** /predicates | Get supported relationships by source and target


# **predicates_get**
> {str: ({str: ([str],)},)} predicates_get()

Get supported relationships by source and target

### Example

```python
from __future__ import print_function
import time
import kpTranslator
from kpTranslator.api import predicates_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kpTranslator.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kpTranslator.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = predicates_api.PredicatesApi(api_client)
    
    # example, this endpoint has no required or optional parameters
    try:
        # Get supported relationships by source and target
        api_response = api_instance.predicates_get()
        pprint(api_response)
    except kpTranslator.ApiException as e:
        print("Exception when calling PredicatesApi->predicates_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**{str: ({str: ([str],)},)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Predicates by source and target |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

