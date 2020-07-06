# kpTranslator.QueryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query**](QueryApi.md#query) | **POST** /query | Query reasoner via one of several inputs


# **query**
> message.Message query(query_query)

Query reasoner via one of several inputs

### Example

```python
from __future__ import print_function
import time
import kpTranslator
from kpTranslator.api import query_api
from kpTranslator.model import query
from kpTranslator.model import message
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kpTranslator.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kpTranslator.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = query_api.QueryApi(api_client)
    query_query = query.Query() # query.Query | Query information to be submitted
    
    # example passing only required values which don't have defaults set
    try:
        # Query reasoner via one of several inputs
        api_response = api_instance.query(query_query)
        pprint(api_response)
    except kpTranslator.ApiException as e:
        print("Exception when calling QueryApi->query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_query** | [**query.Query**](Query.md)| Query information to be submitted |

### Return type

[**message.Message**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

