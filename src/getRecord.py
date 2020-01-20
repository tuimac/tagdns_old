import re

class GetRecord:
    def __init__(self, rrtype, records, qname):
        self.rrtype = rrtype
        self.records = records
        self.qname = qname
        self.rcode = 16

    def a(self, flag=True):
        hostname = self.qname.split(".")[0]
        zone = '.'.join(self.qname.split(".")[1:])
        empty = " A "
        try:
            if len(self.records[zone]["A"]) == 0:
                self.rcode = 0
                return empty
            result = self.records[zone]["A"][hostname]
            result = empty + result
            return result
        except KeyError:
            if not "A" in self.records[zone]:
                self.rcode = 0
                return empty
            self.rcode = 3
            return empty

    def ptr(self, flag=True):
        print(self.qname)
        target = re.sub("\.\D*\.", "", self.qname)
        empty = " PTR "
        try:
            for zone in self.records:
                if not target in self.records[zone]["PTR"]: self.rcode = 3
                else:
                    self.rcode = 16
                    result = self.records[zone]["PTR"][target]
                    result = empty + result + '.' + zone
                    return result
            return empty
        except KeyError:
            if not "PTR" in self.records[zone]:
                self.rcode = 0
                return empty
            self.rcode = 3
            return empty

    def aaaa(self):
        hostname = self.qname.split(".")[0]
        zone = '.'.join(self.qname.split(".")[1:])
        empty = " AAAA "
        try:
            if len(self.records[zone]["AAAA"]) == 0:
                self.rcode = 0
                return empty
            result = self.records[zone]["AAAA"][hostname]
            result = empty + result
            return result
        except KeyError:
            if not "AAAA" in self.records[zone]:
                self.rcode = 0
                return empty
            self.rcode = 3
            return empty

    def getRecord(self):
        switcher = {
            1: "a",
            12: "ptr",
            28: "aaaa"
        }
        method = getattr(self, switcher[self.rrtype])
        return method()

    def getRCode(self):
        return self.rcode
