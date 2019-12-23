class AddRecord:
    def __init__(self, rrtype, records, args):
        self.rrtype = rrtype
        self.records = records
        for k,v in args.items():
            if k.lower() == "ipv4":
                self.ipv4 = v
            elif k.lower() == "hostname":
                self.hostname = v
    def a(self, flag=True):
        print(self.records)
        self.records["A"][self.hostname] = self.ipv4
        if flag is True: self.ptr(False)
        return self.records
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
    def ptr(self, flag=True):
        self.records["PTR"][self.ipv4] = self.hostname
        if flag is True: self.a(False)
        return self.records
    def hinfo(self):
        pass
    def minfo(self):
        pass
    def mx(self):
        pass
    def txt(self):
        pass
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

class DeleteRecord:
    def __init__(self, rrtype, records, args):
        self.rrtype = rrtype
        self.records = records
        for k,v in args.items():
            if k.lower() == "ipv4":
                self.ipv4 = v
            elif k.lower() == "hostname":
                self.hostname = v
    def a(self, flag=True):
        self.records["A"].pop(self.hostname)
        if flag is True: self.ptr(False)
        return self.records
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
    def ptr(self, flag=True):
        self.records["PTR"].pop(self.ipv4)
        if flag is True: self.a(False)
        return self.records
    def hinfo(self):
        pass
    def minfo(self):
        pass
    def mx(self):
        pass
    def txt(self):
        pass
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
    def ptr(self, flag=True):
        target = ""
        if target not in self.records["PTR"]:
            self.searchResult = False
            return " PTR "
        result = self.records["PTR"][target]
        result = " PTR " + result
        return result
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
        method = getattr(self, switcher[self.rrtype])
        return method()
    def getSearchResult(self):
        return self.searchResult
