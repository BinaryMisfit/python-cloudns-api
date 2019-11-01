#!/usr/bin/env python3
"""Command line functionality for ClouDNS APi
"""
from .api_response import Response


def build_version():
    """Build the output for the main method
    """
    response = Response()
    version = "Response version: {0}".format(response.version)
    return version


def main():
    """Print the version information for ClouDNS API
    """
    print(build_version())
