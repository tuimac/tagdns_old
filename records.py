import json
import os

class Records:
    def __init__(self, path):
        self.path = os.path.expanduser(path)
        self.template = {"NameServer": [], "Records": []}
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
        record = dict()
        items = dict()
        items["A"] = ipv4
        items["AAAA"] = ipv6
        items["CNAME"] = cname
        items["MX"] = mx
        items["NS"] = ns
        items["PTR"] = ptr
        items["SVR"] = svr
        items["TXT"] = txt
        items["SOA"] = soa
        record[name] = items

        self.records["Records"].append(record)
        self.writeRecordsFile(self.records)

    def lookupIp(self):
        pass	

