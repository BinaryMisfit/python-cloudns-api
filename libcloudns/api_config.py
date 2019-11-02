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

    def __repr__(self):
        """Return visual representation of object
        """

        return """<Config
        config_dir={0}
        config_file={1}
        found_config={2}
        found_user={3}
        user_config_dir={4}
        user_config_file={5}>""".format(
            self.config_dir,
            self.config_file,
            self.found_config,
            self.found_user,
            self.user_config_dir,
            self.user_config_file
        )

    def __str__(self):
        """Return string representation of object
        """

        return self.found_user

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
