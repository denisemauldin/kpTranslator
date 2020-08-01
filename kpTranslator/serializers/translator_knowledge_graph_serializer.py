from kpTranslator.database.models import TranslatorKnowledgeGraphNode
from kpTranslator.database.models import TranslatorKnowledgeGraphEdge
from kpTranslator.config import db, ma


class TranslatorKnowledgeGraphNodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TranslatorKnowledgeGraphNode
        sqla_session = db.session


class TranslatorKnowledgeGraphEdgeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TranslatorKnowledgeGraphEdge
        sqla_session = db.session
