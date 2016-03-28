#!/usr/bin/env python

import json


class RMenu:
    def __init__(self, config=None):
        self.config = config
        self.position = []

    def load_config_file(self, file):
        self.config = json.load(file)

    def select(self, selection):
        pass

    def _descend(self, selection):
        self.position.append(selection)

    def _ascend(self):
        self.position.pop()
