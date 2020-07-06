from datetime import datetime
from datetime import datetime
from kpTranslator.config import db, ma

class TestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
