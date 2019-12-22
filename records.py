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

    def addRecord(self, rrtype, **args):
        '''
        # A and PTR
        ipv4: IPv4 IPaddress
        host: hostname within the Zone
        '''
        addrecord = AddRecord(rrtype, self.records, args)
        record = addrecord.getRecord()
        self.writeRecordsFile(record)
        return

    def lookupIp(self, qname):
        hostname = qname.split(".")[0]
        zone = qname.split(".")[1:]
        if not hostname in self.records["A"]: return ""
        return self.records["A"][hostname]

    def lookupName(self, qname):
        print(qname)
        return "test"

class AddRecord:
    def __init__(self, rrtype, records, args):
        self.rrtype = rrtype
        self.records = records
        for k,v in args.items():
            if k.lower() == "ipv4":
                self.ipv4 = v
            elif k.lower() == "hostname"
                self.hostname = v
    def a(self):
        return "hello"
    def ns(self):
        pass
    def md(self):
        pass
    def mf(self):
        pass
    def cname(self):
        pass
    def soa(self):
        pass
    def mb(self):
        pass
    def mg(self):
        pass
    def mr(self):
        pass
    def null(self):
        pass
    def wks(self):
        pass
    def ptr(self):
        pass
    def hinfo(self):
        pass
    def minfo(self):
        pass
    def mx(self):
        pass
    def txt(self):
        pass
    def getRecord(self):
        switcher = {
            1: "a",
            2: "ns",
            3: "md",
            4: "mf",
            5: "cname",
            6: "soa",
            7: "mb",
            8: "mg",
            9: "mr",
            10: "null",
            11: "wks",
            12: "ptr",
            13: "hinfo",
            14: "minfo",
            15: "mx",
            16: "txt" 
        }
        method = getattr(self, switcher[self.rrtype], lambda :'Invalid')
        return method()
