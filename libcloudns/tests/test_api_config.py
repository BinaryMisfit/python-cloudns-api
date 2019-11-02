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
        expected = """<Config version={0}
        config_dir={1}
        config_file={2}
        user_config_dir={3}
        user_config_file={4}>""".format(
            config.version,
            config.config_dir,
            config.config_file,
            config.user_config_dir,
            config.user_config_file
        )
        actual = repr(config)
        self.assertEqual(actual, expected)

    def test_has_str(self):
        """Test output for class string description
        """
        config = Config()
        expected = "0.0.1"
        actual = str(config)
        self.assertEqual(actual, expected)

    def test_has_version(self):
        """Test the output of version is correct
        """
        config = Config()
        self.assertIsInstance(config.version, str)
