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
        self.found_config = False
        self.found_user = False
        self.user_config_dir = ""
        self.user_config_file = ".libcloudns_rc"
        self.find_config()

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

    def current(self):
        """Return the current loaded configuration
        """
