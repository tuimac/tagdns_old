class AddRecord:
    def __init__(self, rrtype, records, args):
        self.rrtype = rrtype
        self.records = records
        for k,v in args.items():
            if k.lower() == "ipv4":
                self.ipv4 = v
            elif k.lower() == "hostname":
                self.hostname = v
    def a(self, flag=True, reversedIp=""):
        if flag is True:
            self.records["A"][self.hostname] = self.ipv4
            reversedIp = self.__reverseIp(self.ipv4)
            self.ptr(False, reversedIp=reversedIp)
        else:
            self.records["A"][self.hostname] = reversedIp
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
            self.records["PTR"][self.ipv4] = self.hostname
            reversedIp = self.__reversedIp(self.ipv4)           
            self.a(False, reversedIp=reversedIp)
        else:
            self.records["PTR"][reversedIp] = self.hostname
        return self.records

    def hinfo(self):
        return self.records
    def minfo(self):
        return self.records
    def mx(self):
        return self.records
    def txt(self):
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
            16: "txt" 
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
    def __init__(self, rrtype, records, args):
        self.rrtype = rrtype
        self.records = records
        for k,v in args.items():
            if k.lower() == "ipv4":
                self.ipv4 = v
            elif k.lower() == "hostname":
                self.hostname = v
    def a(self, flag=True, hostname=""):
        if flag is True:
            ipv4 = self.records["A"].pop(self.hostname)
            reversedIp = self.__reverseIp(ipv4)
            self.ptr(False, reversedIp=reversedIp)
        else:
            self.records["A"].pop(self.hostname)
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
            hostname = self.records["PTR"].pop(self.ipv4)
            self.a(False, hostname)
        else:
            hostname = self.records["PTR"].pop(reversedIp)
        return self.records
    def hinfo(self):
        return self.records
    def minfo(self):
        return self.records
    def mx(self):
        return self.records
    def txt(self):
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
            16: "txt" 
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
        self.searchResult = True

    def a(self, flag=True):
        target = self.qname.split(".")[0]
        if target not in self.records["A"]:
            self.searchResult = False
            return " A "
        result = self.records["A"][target]
        result = " A " + result
        return result

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

    def ptr(self, flag=True):
        target = 
        if target not in self.records["PTR"]:
            self.searchResult = False
            return " PTR "
        result = self.records["PTR"][target]
        result = " PTR " + result
        return result

    def hinfo(self):
        return self.records
    def minfo(self):
        return self.records
    def mx(self):
        return self.records
    def txt(self):
        return self.records
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
        method = getattr(self, switcher[self.rrtype])
        return method()

    def getSearchResult(self):
        return self.searchResult
