from flask_sqlalchemy import SQLAlchemy
import logging

log = logging.getLogger(__name__)
db = SQLAlchemy()


def reset_database():
    from app.database.models import TestModel
    db.drop_all()
    db.create_all()