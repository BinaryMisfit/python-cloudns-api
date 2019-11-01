#!/usr/bin/env python3
from unittest import TestCase
from libcloudns import Response


class TestResponse(TestCase):
    def test_has_version(self):
        response = Response()
        self.assertIsInstance(response.version, str)
