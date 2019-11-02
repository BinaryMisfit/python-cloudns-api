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
        expected = """<Config
        config_dir={0}
        config_file={1}
        found_config={2}
        found_user={3}
        user_config_dir={4}
        user_config_file={5}>""".format(
            config.config_dir,
            config.config_file,
            config.found_config,
            config.found_user,
            config.user_config_dir,
            config.user_config_file
        )
        actual = repr(config)
        self.assertEqual(actual, expected)
