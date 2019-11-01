#!/usr/bin/env python3
from unittest import TestCase
from libcloudns import command_line


class TestCommandLine(TestCase):
    def test_has_main(self):
        self.assertIsInstance(command_line.build_version(), str)

    def test_has_output(self):
        from io import StringIO
        from unittest.mock import patch

        expected = command_line.build_version()
        with patch('sys.stdout', new=StringIO()) as output:
            command_line.main()
            self.assertEqual(output.getvalue().strip(), expected)
