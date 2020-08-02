import os
import csv
import json
import argparse
from kpTranslator.config import db, db_file
from kpTranslator.database.models import TestModel, TranslatorKnowledgeGraphNode, TranslatorKnowledgeGraphEdge

parser = argparse.ArgumentParser()
parser.add_argument('--db_config', help="Configuration file (.json) for populating database", default=None)
args = parser.parse_args()

# Delete database file if it exists currently
if os.path.exists(db_file):
    print("Deleting existing database file...")
    os.remove(db_file)

# Populate database from TSV files
if args.db_config is not None:
    db_config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', args.db_config)
    print('Database configuration file: {}'.format(db_config_file))

    with open(db_config_file, 'r') as config_file:
        config_data = json.load(config_file)

    print(config_data)

    for src, dat in config_data.items():
        assert('source_dir' in list(dat.keys()))
        assert('nodes_file' in list(dat.keys()))
        assert('edges_file' in list(dat.keys()))

        dat_root = os.path.dirname(db_config_file)
        dat_path = os.path.join(dat_root, dat['source_dir'])
        nodes_file = os.path.join(dat_root, dat['source_dir'], dat['nodes_file'])
        edges_file = os.path.join(dat_root, dat['source_dir'], dat['edges_file'])
        print(dat_path)
        print(nodes_file)
        print(edges_file)

        node_count = 0
        with open(nodes_file, 'r', newline='') as nodes_in:
            nodes_reader = csv.reader(nodes_in, delimiter='\t')
            headers = nodes_reader.__next__()
            print(headers)
            for node_record in nodes_reader:
                node_data = {k: v for k, v in zip(headers, node_record)}
                n = TranslatorKnowledgeGraphNode(
                    id=node_data['id'], name=node_data['name'], category=node_data['category']
                )
                db.session.add(n)

        edge_count = 0
        with open(edges_file, 'r', newline='') as edges_in:
            edges_reader = csv.reader(edges_in, delimiter='\t')
            headers = edges_reader.__next__()
            print(headers)
            for edge_record in edges_reader:
                edge_data = {k: v for k, v in zip(headers, edge_record)}
                e = TranslatorKnowledgeGraphEdge(
                    subject=edge_data['subject'], edge_label=edge_data['edge_label'], object=edge_data['object'],
                    relation=edge_data['relation']
                )
                db.session.add(e)

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
