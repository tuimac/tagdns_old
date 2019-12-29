import re

class AddRecord:
    def __init__(self, rrtype, records, zone, args):
        self.rrtype = rrtype
        self.records = records
        self.zone = zone
        for k,v in args.items():
            if k.lower() == "ipv4":
                self.ipv4 = v
            elif k.lower() == "hostname":
                self.hostname = v
    def a(self, flag=True, reversedIp=""):
        if flag is True:
            self.records[self.zone]["A"][self.hostname] = self.ipv4
            reversedIp = self.__reverseIp(self.ipv4)
            self.ptr(False, reversedIp=reversedIp)
        else:
            self.records[self.zone]["A"][self.hostname] = reversedIp
        return self.records
    def ns(self):
        return self.records
    def md(self):
        return self.records
    def mf(self):
        return self.records
    def cname(self):
        return self.records
    def soa(self):
        return self.records
    def mb(self):
        return self.records
    def mg(self):
        return self.records
    def mr(self):
        return self.records
    def null(self):
        return self.records
    def wks(self):
        return self.records
    def ptr(self, flag=True, reversedIp=""):
        if flag is True:
            self.records[self.zone]["PTR"][self.ipv4] = self.hostname
            reversedIp = self.__reversedIp(self.ipv4)          
            self.a(False, reversedIp=reversedIp)
        else:
            self.records[self.zone]["PTR"][reversedIp] = self.hostname
        return self.records

    def hinfo(self):
        return self.records
    def minfo(self):
        return self.records
    def mx(self):
        return self.records
    def txt(self):
        return self.records
    def aaaa(self):
        return self.records
    def addRecord(self):
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
            16: "txt",
            28: "aaaa"
        }
        method = getattr(self, switcher[self.rrtype])
        return method()
    
    def __reverseIp(self, ipaddr):
        result = ""
        element = ipaddr.split(".")
        for i in range(len(element) - 1, 0, -1):
            result += element[i] + "."
        result += element[0]
        return result

class DeleteRecord:
    def __init__(self, rrtype, records, zone, args):
        self.rrtype = rrtype
        self.records = records
        self.zone = zone
        for k,v in args.items():
            if k.lower() == "ipv4":
                self.ipv4 = v
            elif k.lower() == "hostname":
                self.hostname = v
    def a(self, flag=True, hostname=""):
        if flag is True:
            ipv4 = self.records[self.zone]["A"].pop(self.hostname)
            reversedIp = self.__reverseIp(ipv4)
            self.ptr(False, reversedIp=reversedIp)
        else:
            self.records[self.zone]["A"].pop(self.hostname)
        return self.records
    def ns(self):
        return self.records
    def md(self):
        return self.records
    def mf(self):
        return self.records
    def cname(self):
        return self.records
    def soa(self):
        return self.records
    def mb(self):
        return self.records
    def mg(self):
        return self.records
    def mr(self):
        return self.records
    def null(self):
        return self.records
    def wks(self):
        return self.records
    def ptr(self, flag=True, reversedIp=""):
        if flag is True:
            hostname = self.records[self.zone]["PTR"].pop(self.ipv4)
            self.a(False, hostname)
        else:
            hostname = self.records[self.zone]["PTR"].pop(reversedIp)
        return self.records
    def hinfo(self):
        return self.records
    def minfo(self):
        return self.records
    def mx(self):
        return self.records
    def txt(self):
        return self.records
    def aaaa(self):
        return self.records
    def deleteRecord(self):
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
            16: "txt",
            28: "aaaa"
        }
        method = getattr(self, switcher[self.rrtype])
        return method()

    def __reverseIp(self, ipaddr):
        result = ""
        element = ipaddr.split(".")
        for i in range(len(element) - 1, 0, -1):
            result += element[i] + "."
        result += element[0]
        return result

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

    def ns(self):
        return " NS "
    def md(self):
        return " MD "
    def mf(self):
        return " MF "
    def cname(self):
        return " CNAME "
    def soa(self):
        return " SOA "
    def mb(self):
        return " MB "
    def mg(self):
        return " MG "
    def mr(self):
        return " MR "
    def null(self):
        return " NULL "
    def wks(self):
        return " WKS "

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

    def hinfo(self):
        return " HINFO "
    def minfo(self):
        return " MINFO "
    def mx(self):
        return " MX "
    def txt(self):
        return " TXT "
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
            16: "txt",
            28: "aaaa"
        }
        method = getattr(self, switcher[self.rrtype])
        return method()

    def getRCode(self):
        return self.rcode
