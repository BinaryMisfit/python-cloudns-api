#!/usr/bin/env python3
"""Object containing the response from the ClouDNS API
"""


class Response:
    """Object containing the response from the ClouDNS API
    """

    def __init__(self):
        self.response_code = 0

    def validate(self):
        """Validate the response before parsing
        """

    def parse(self):
        """Parse the response and return state
        """
