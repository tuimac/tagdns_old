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
        try:
            result = self.records[zone]["A"][hostname]
            result = " A " + result
            return result
        except KeyError:
            self.rcode = 3
            return " A "

    def ptr(self, flag=True):
        target = re.sub("\.\D*\.", "", self.qname)
        for zone in self.records:
            if not target in self.records[zone]["PTR"]: self.rcode = 3
            else:
                self.rcode = 16
                result = self.records[zone]["PTR"][target]
                result = " PTR " + result + '.' + zone
                return result
        return " PTR "

    def aaaa(self):
        hostname = self.qname.split(".")[0]
        zone = '.'.join(self.qname.split(".")[1:])
        if len(self.records[zone]["AAAA"]) == 0:
            self.rcode = 0
            return " AAAA "
        try:
            result = self.records[zone]["AAAA"][hostname]
            result = " AAAA " + result
            return result
        except KeyError:
            self.rcode = 3
            return " AAAA "

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
