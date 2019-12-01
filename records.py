import json
import os

class Records():
    def __init__(self, path):
        if os.path.exists(path) is False:
            records = {"NameServer": [], "Records": []}
            self.__writeToFile(records)
        self.path = path

    def __writeToFile(self, records):
        json_data = open(self.path, 'w')
        json.dump(records, 
            ensure_ascii=False,
            indent=4,
            separators=(',',': ')
        )

    def getRecords(self):
        with open(self.path, 'r') as f:
            return json.load(f)
