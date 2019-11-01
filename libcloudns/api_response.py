#!/usr/bin/env python3
"""Object containing the response from the ClouDNS API
"""


class Response:
    """Object containing the response from the ClouDNS API
    """

    def __init__(self):
        self.version = "0.0.1"

    def __repr__(self):
        return ("<Response version={0}>").format(self.version)

    def __str__(self):
        return self.version
