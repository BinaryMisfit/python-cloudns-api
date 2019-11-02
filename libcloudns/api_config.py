#!/usr/bin/env python3
"""Class handling the API configuration
"""


class Config:
    """Object containing the config for the API
    """

    def __init__(self):
        self.config_file = 'libcloudns_rc'

    def __repr__(self):
        return "<Config config_file={0}".format(self.config_file)

    def __str__(self):
        return self.config_file
