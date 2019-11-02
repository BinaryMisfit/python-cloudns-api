#!/usr/bin/env python3
"""Class handling the API configuration
"""
from sys import prefix
from site import getuserbase
from os import environ, path


class Config:
    """Object containing the config for the API
    """

    def __init__(self):
        self.config_dir = ""
        self.config_file = "libcloudns_rc"
        self.user_config_dir = ""
        self.user_config_file = ".libcloudns_rc"
        self.version = "0.0.1"
        self.find_config()

    def __repr__(self):
        """Return visual representation of object
        """

        return """<Config version={0}
        config_dir={1}
        config_file={2}
        user_config_dir={3}
        user_config_file={4}>""".format(
            self.version,
            self.config_dir,
            self.config_file,
            self.user_config_dir,
            self.user_config_file
        )

    def __str__(self):
        """Return string representation of object
        """

        return self.version

    def find_config(self):
        """Find the required config files
        """

        config_file = "{0}/{1}".format(environ["HOME"], self.user_config_file)
        if path.isfile(config_file):
            self.user_config_dir = environ['HOST']

        config_file = "{0}/etc/{1}".format(prefix, self.config_file)
        if path.isfile(config_file):
            self.config_dir = "{0}/etc".format(prefix)
            return

        user_root = getuserbase()
        config_file = "{0}/etc/{1}".format(user_root, self.config_file)
        if path.isfile(config_file):
            self.config_dir = "{0}/etc".format(user_root)
            return
