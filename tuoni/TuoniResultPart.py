import json
from tuoni.TuoniExceptions import *


class TuoniResultPart:
    def __init__(self, conf, c2):
        self._load_conf(conf)
        self.c2 = c2

    def _load_conf(self, conf):
        self.type = conf["type"]
        if self.type == "text":
            self.name = conf["name"]
            self.value = conf["value"]
        if self.type == "file":
            self.filename = conf["filename"]
            self.href = conf["href"]
            if "//" in self.href:
                self.uri = self.href[self.href.find("//")+2:]
                self.uri = self.uri[self.uri.find("/"):]
            else:
                self.uri = self.href

    def get_as_text(self):
        if self.type == "text":
            return self.value
        if self.type == "file":
            return self.c2.request_get(self.uri, result_as_json=False)
        return None

    def get_as_file(self, filename):
        if self.type == "file":
            self.c2.request_get_file(self.uri, filename)
        return None

    def get_as_json(self):
        if self.type == "text":
            return json.loads(self.value)
        if self.type == "file":
            return json.loads(self.c2.request_get(self.uri, result_as_json=False))
        return None



