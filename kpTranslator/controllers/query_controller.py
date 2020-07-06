import connexion
import six

from kpTranslator.models.message import Message  # noqa: E501
from kpTranslator import util


def query(request_body):  # noqa: E501
    """Query reasoner via one of several inputs

     # noqa: E501

    :param request_body: Query information to be submitted
    :type request_body: Dict[str, ]

    :rtype: Message
    """
    return 'do some magic!'
