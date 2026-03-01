# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from pdfserver.models.extracttext_body import ExtracttextBody  # noqa: E501
from pdfserver.models.inline_response200 import InlineResponse200  # noqa: E501
from pdfserver.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_extract_text_from_pdf(self):
        """Test case for extract_text_from_pdf

        Extract text from a PDF file
        """
        body = ExtracttextBody()
        headers = [('subscription_key', 'subscription_key_example')]
        response = self.client.open(
            '/extract-text',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
