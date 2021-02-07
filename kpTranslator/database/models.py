from datetime import datetime
from datetime import datetime
from kpTranslator.config import db, ma


class TestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))


class TranslatorKnowledgeGraphNode(db.Model):
    node_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=True)
    category = db.Column(db.String(80), unique=False, nullable=False)


class TranslatorKnowledgeGraphEdge(db.Model):
    edge_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80), unique=False, nullable=False)
    edge_label = db.Column(db.String(80), unique=False, nullable=False)
    object = db.Column(db.String(80), unique=False, nullable=False)
    relation = db.Column(db.String(80), unique=False, nullable=False)
