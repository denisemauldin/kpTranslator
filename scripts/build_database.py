import os
from kpTranslator.config import db
from kpTranslator.database.models import TestModel

# Data to initialize database with
TEST = [
    {'name': 'Doug'},
    {'name': 'Kent'},
    {'name': 'Bunny'}
]

# Delete database file if it exists currently
if os.path.exists('test.db'):
    os.remove('test.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for test in TEST:
    p = TestModel(name=test['name'])
    db.session.add(p)

db.session.commit()