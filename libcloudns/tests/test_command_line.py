#!/usr/bin/env python3
from unittest import TestCase
from libcloudns import command_line


class TestCommandLine(TestCase):
    def test_has_main(self):
        self.assertIsInstance(command_line.build_version(), str)