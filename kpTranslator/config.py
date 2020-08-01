import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from kpTranslator import encoder

basedir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(basedir, 'translator_kg.db')

# Delete database file if it exists currently
if os.path.exists(db_file):
    print("Deleting existing database file...")
    os.remove(db_file)

connex_app = connexion.App(__name__, specification_dir='./openapi/')

# Get the underlying Flask app instance
app = connex_app.app
app.json_encoder = encoder.JSONEncoder

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
