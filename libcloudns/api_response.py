#!/usr/bin/env python3
class Response:
    def __init__(self):
        self.version = "0.0.1"

    def __repr__(self):
        return ("<Response version={0}").format(self.version)

    def __str__(self):
        return self.version
