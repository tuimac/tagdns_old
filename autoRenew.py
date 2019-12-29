import boto3
from exception import TagKeyNotFoundException

class AutoRenew:
    def __init__(self, records, zone):
        self.records = records
        self.zone = zone
        self.ec2 = boto3.client('ec2')
        self.newRecords = records.getDatabase()

    def __getAllTags(self, key):
        tempRecord = dict()
        def findTag(tagList, key):
            for tag in tagList:
                if tag["Key"] == key: return tag["Value"]
            raise TagKeyNotFoundException
        for instance in self.ec2.describe_instances()['Reservations']:
            status = instance["Instances"][0]["State"]["Name"]
            if status != "terminated":
                ipaddress = instance["Instances"][0]["PrivateIpAddress"]
                hostname = findTag(instance["Instances"][0]["Tags"], key)
                tempRecord[hostname] = ipaddress
        return tempRecord

    def __renewA(self, tempRecord, zone):
        self.newRecords[zone].pop("A")
        self.newRecords[zone]["A"] = dict()
        for hostname, ipaddress in tempRecord.items():
            self.newRecords[zone]["A"][hostname] = ipaddress

    def __renewPTR(self, tempRecord, zone):
        self.newRecords[zone].pop("PTR")
        self.newRecords[zone]["PTR"] = dict()
        def reverseIp(ipaddr):
            result = ""
            element = ipaddr.split(".")
            for i in range(len(element) - 1, 0, -1):
                result += element[i] + "."
            result += element[0]
            return result
        for hostname, ipaddress in tempRecord.items():
            ip = reverseIp(ipaddress)
            self.newRecords[zone]["PTR"][ip] = hostname

    def autoRenewRecords(self):
        for target in self.zone:
            tempRecord = self.__getAllTags(self.zone[target]["key"])
            self.__renewA(tempRecord, target)
            self.__renewPTR(tempRecord, target)
            self.records.renewRecord(self.newRecords)
