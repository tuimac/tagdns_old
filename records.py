import json
import os
import sys

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

    def addNewRecord(self, name, ipv4, ipv6="", cname="", mx="", ns="", ptr="", svr="", txt="", soa=""):
        if name in self.records["Records"]:
            print("You can't register same name.", file=sys.stderr)
            return

        record = dict()
        record["A"] = ipv4
        record["AAAA"] = ipv6
        record["CNAME"] = cname
        record["MX"] = mx
        record["NS"] = ns
        record["PTR"] = ptr
        record["SVR"] = svr
        record["TXT"] = txt
        record["SOA"] = soa

        self.records["Records"][name] = record
        self.writeRecordsFile(self.records)

    def lookupIp(self, name):
        print(name in self.records["Records"])
        if not name in self.records["Records"]:
            print("There is no such a records", file=sys.stderr)
            return
        return self.records["Records"][name]["A"]
