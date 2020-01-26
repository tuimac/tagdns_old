from .getRecord import GetRecord
from .utils.exception import ZoneNotFoundException

import json
import os
import sys

class Records:
    def __init__(self, config):
        self.path = os.path.expanduser(config["records_path"])
        self.zone = config["zones"]
        if os.path.exists(self.path) is False or self.readRecordsFile() == "":
            os.mknod(self.path)
            self.writeRecordsFile(dict())
        self.records = self.readRecordsFile()

    def writeRecordsFile(self, records):
        with open(self.path, 'w', encoding='utf8') as f:
            json.dump(records, f,
                default=True,
                ensure_ascii=False,
                indent=4,
                separators=(',', ': ')
            )

    def readRecordsFile(self):
        with open(self.path, 'r') as f:
            return json.load(f)

    def getDatabase(self):
        return self.records

    def renewRecord(self, newRecord):
        self.records = newRecord
        self.writeRecordsFile(self.records)
        return

    def getRecord(self, rrtype, qname):
        getrecord = GetRecord(rrtype, self.records, qname)
        record = getrecord.getRecord()
        rcode = getrecord.getRCode()
        return (record, rcode)
