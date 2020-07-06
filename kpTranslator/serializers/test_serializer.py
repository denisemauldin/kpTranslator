from kpTranslator.database.models import TestModel
from kpTranslator.config import db, ma

class TestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TestModel
        sqla_session = db.session