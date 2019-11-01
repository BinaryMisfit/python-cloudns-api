#!/usr/bin/env python3
from unittest import TestCase
from libcloudns import Response


class TestResponse(TestCase):
    def test_has_repr(self):
        response = Response()
        expected = "<Response version=0.0.1>"
        actual = repr(response)
        self.assertEqual(actual, expected)

    def test_has_str(self):
        response = Response()
        expected = "0.0.1"
        actual = str(response)
        self.assertEqual(actual, expected)

    def test_has_version(self):
        response = Response()
        self.assertIsInstance(response.version, str)
