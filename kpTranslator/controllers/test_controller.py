import connexion
import six

from kpTranslator import util
from kpTranslator.database.models import TestModel
from kpTranslator.serializers.test_serializer import TestSchema

def test_get():  # noqa: E501
    """Get supported relationships by source and target

     # noqa: E501


    :rtype: Dict[str, Dict[str, List[str]]]
    """
    tests = TestModel.query.all()
    test_schema = TestSchema(many=True)
    return test_schema.dump(tests)