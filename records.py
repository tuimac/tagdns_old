import json
import os
import sys

from database import AddRecord, DeleteRecord, GetRecord

class Records:
    def __init__(self, path):
        self.path = os.path.expanduser(path)
        self.template = {"NameServer": {}, "Records": {}}
        if os.path.exists(self.path) is False:
            os.mknod(path)
            self.writeRecordsFile(self.template)
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

    def addRecord(self, rrtype, **args):
        addrecord = AddRecord(rrtype, self.records, args)
        record = addrecord.addRecord()
        self.writeRecordsFile(record)
        return

    def deleteRecord(self, rrtype, **args):
        deleterecord = DeleteRecord(rrtype, self.records, args)
        record = deleterecord.deleteRecord()
        self.writeRecordsFile(record)
        return

    def getRecord(self, rrtype, qname):
        getrecord = GetRecord(rrtype, self.records, qname)
        record = getrecord.getRecord()
        result = getrecord.getSearchResult()
        return (record, result)
