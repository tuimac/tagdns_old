class ZoneFormatException(Exception):
    def __init__(self):
        self.message = "Zone format in tagdns.ini is wrong."

class ConfigNotFoundException(Exception):
    def __init__(self):
        self.message = "There is no Configure file"

class ZoneNotFoundException(Exception):
    def __init__(self):
        self.message = "There is no such a zone in database."
