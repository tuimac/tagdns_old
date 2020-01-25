class ZoneFormatException(Exception):
    def __init__(self):
        self.message = "'zones' value format in tagdns.yml is wrong."

class ConfigNotFoundException(Exception):
    def __init__(self):
        self.message = "There is no config file[tagdns.yml]."

class ZoneNotFoundException(Exception):
    def __init__(self):
        self.message = "There is no such a zone in database."

class StopNodesError(Exception):
    def __init__(self):
        self.message = "Stoping nodes is failed."

class TagKeyNotFoundException(Exception):
    def __init__(self):
        self.message = "There is no such a EC2's Tag key."
