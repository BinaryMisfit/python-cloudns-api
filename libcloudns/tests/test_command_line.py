#!/usr/bin/env python3
"""Command line functionality for ClouDNS API
"""
from io import StringIO
from unittest.mock import patch
from unittest import TestCase
from libcloudns import command_line


class TestCommandLine(TestCase):
    """Class containing tests for command_line
    """

    def test_has_build_version(self):
        """Test build_version output type
        """
        self.assertIsInstance(command_line.build_version(), str)

    def test_has_output(self):
        """Test main method output
        """
        expected = command_line.build_version()
        with patch('sys.stdout', new=StringIO()) as output:
            command_line.main()
            self.assertEqual(output.getvalue().strip(), expected)
