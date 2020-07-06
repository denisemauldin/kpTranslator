# query_graph.QueryGraph

A graph intended to be the thought path to be followed by a reasoner to answer the question. This graph is a representation of a question.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**{str: (q_node.QNode,)}**](QNode.md) | List of nodes in the QueryGraph | 
**edges** | [**{str: (q_edge.QEdge,)}**](QEdge.md) | List of edges in the QueryGraph | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


