#!/usr/bin/env python3
"""TestCase for the api_response module
"""
from unittest import TestCase
from libcloudns import Response


class TestResponse(TestCase):
    """TestCase for the TestResponse class
    """

    def test_has_repr(self):
        """Test output for class representation string
        """
        response = Response()
        expected = "<Response version=0.0.1>"
        actual = repr(response)
        self.assertEqual(actual, expected)

    def test_has_str(self):
        """Test output for class string description
        """
        response = Response()
        expected = "0.0.1"
        actual = str(response)
        self.assertEqual(actual, expected)

    def test_has_version(self):
        """Test the output of version is correct
        """
        response = Response()
        self.assertIsInstance(response.version, str)
