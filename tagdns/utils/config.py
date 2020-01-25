import yaml
import os
import re
import socket
from utils.exception import ConfigNotFoundException
from utils.exception import ZoneFormatException

class Config:
    def __init__(self, path):
        if os.path.exists(path) is False: raise ConfigNotFoundException
        confFile = open(path, "r")
        self.config = yaml.load(confFile, Loader=yaml.SafeLoader)
        confFile.close()
        self.__resolveIP(self.config["ipaddress"])
        self.__zoneValidate()
        self.__pathValidate()
    
    def read(self):
        return self.config

    def __resolveIP(self, ip):
        regex= "^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$"
        if re.search(regex, ip) is None: ip = socket.gethostbyname(ip)
        self.config["ipaddress"] = ip
        return

    def __zoneValidate(self):
        for zone in self.config["zones"]:
            if re.match("\D*\.$", zone) is None: raise ZoneFormatException
        return

    def __pathValidate(self):
        recordsPath = self.config["records_path"]
        accessLog = self.config["log"]["access_log"]
        errorLog = self.config["log"]["error_log"]

        if recordsPath == "": self.config["records_path"] = "/etc/tagdns/records.json"
        else: self.config["records_path"] = os.path.expanduser(recordsPath)
        if accessLog == "": self.config["log"]["access_log"] = "/var/log/tagdns/access.log"
        else: self.config["log"]["access_log"] = os.path.expanduser(accessLog)
        if errorLog == "": self.config["log"]["error_log"] = "/var/log/tagdns/error.log"
        else: self.config["log"]["error_log"] = os.path.expanduser(errorLog)
