import yaml
import os
from exception import ConfigNotFoundException

class Config:
    def __init__(self, path):
        if os.path.exists(path) is False: raise ConfigNotFoundException
        confFile = open(path, "r")
        self.conf = yaml.load(confFile)
        confFile.close()
    
    def read(self):
        return self.conf
