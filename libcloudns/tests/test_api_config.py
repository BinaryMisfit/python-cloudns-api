#!/usr/bin/env python3
"""TestCase for the api_config module
"""
from unittest import TestCase
from libcloudns import Config


class TestConfig(TestCase):
    """TestCase for the TestConfig class
    """

    def test_has_repr(self):
        """Test output for class representation string
        """
        config = Config()
        expected = "<Config version=0.0.1 config_file=libcloudns_rc>"
        actual = repr(config)
        self.assertEqual(actual, expected)

    def test_has_str(self):
        """Test output for class string description
        """
        config = Config()
        expected = "libcloudns_rc"
        actual = str(config)
        self.assertEqual(actual, expected)

    def test_has_version(self):
        """Test the output of version is correct
        """
        config = Config()
        self.assertIsInstance(config.version, str)
