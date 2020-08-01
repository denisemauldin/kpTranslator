import connexion
import six

from kpTranslator.database.models import TranslatorKnowledgeGraphNode
from kpTranslator.database.models import TranslatorKnowledgeGraphEdge
from kpTranslator.serializers.translator_knowledge_graph_serializer import TranslatorKnowledgeGraphNodeSchema
from kpTranslator.serializers.translator_knowledge_graph_serializer import TranslatorKnowledgeGraphEdgeSchema

from kpTranslator.models.message import Message  # noqa: E501
from kpTranslator.models.query import Query
from kpTranslator import util


def query(request_body):  # noqa: E501
    """Query reasoner via one of several inputs

     # noqa: E501

    :param request_body: Query information to be submitted
    :type request_body: Dict[str, ]

    :rtype: Message
    """
    request = Query.from_dict(request_body)
    query_graph = request.message.query_graph

    qnodes = query_graph.nodes
    qedges = query_graph.edges

    curie = None
    for k, v in qnodes.items():
        if v.curie is not None:
            curie = v.curie

    if curie is not None:
        edges = TranslatorKnowledgeGraphEdge.query \
            .filter(
                (TranslatorKnowledgeGraphEdge.subject == curie) |
                (TranslatorKnowledgeGraphEdge.object == curie)).all()
        edges_schema = TranslatorKnowledgeGraphEdgeSchema(many=True)
        return edges_schema.dump(edges)
    else:
        return 'Curie not found!'
