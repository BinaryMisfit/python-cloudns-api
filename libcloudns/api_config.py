#!/usr/bin/env python3
"""Class handling the API configuration
"""


class Config:
    """Object containing the config for the API
    """

    def __init__(self):
        self.version = "0.0.1"
        self.config_file = 'libcloudns_rc'

    def __repr__(self):
        return "<Config version={0} config_file={1}>".format(self.version, self.config_file)

    def __str__(self):
        return self.config_file
