#!/usr/bin/env python3
"""Command line functionality for ClouDNS APi
"""
from .api_config import Config


def build_version():
    """Build the output for the method
    """


def build_debug():
    """Build the out for the debug method
    """
    config = Config()
    result = """Config:
    File: {0}
    Dir: {1}
    Path: {1}/{0}
    User File: {2}
    User Dir: {3}
    User Path: {3}/{2}""".format(
        config.config_file,
        config.config_dir,
        config.user_config_file,
        config.user_config_dir)
    return result


def show_version():
    """Print the version information for ClouDNS API
    """
    print(build_version())


def show_debug():
    """Print debug information for the CloudDNS API
    """
    print(build_debug())
