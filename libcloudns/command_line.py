#!/usr/bin/env python3
from .api_response import Response


def build_version():
    response = Response()
    version = "Response version: {0}".format(response.version)
    return version

def main():
    print(build_version())
