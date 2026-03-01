import connexion
import six

from pdfserver.models.extracttext_body import ExtracttextBody  # noqa: E501
from pdfserver.models.inline_response200 import InlineResponse200  # noqa: E501
from pdfserver import util


def extract_text_from_pdf(body, subscription_key):  # noqa: E501
    """Extract text from a PDF file

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param subscription_key: Valid subscription key
    :type subscription_key: str

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = ExtracttextBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
