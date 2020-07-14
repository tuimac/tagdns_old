import json
import logging
import traceback
from threading import Thread

logger = logging.getLogger('tagdns')

class DNSRecords(dict):
    def __init__(self, path):
        self.path = path
        self.preload()

    def __setitem__(self, key, item):
        dict.__setitem__(self, key, item)
        try:
            dump = Thread(target=self.dump)
            dump.start()
        except:
            logger.error(traceback.format_exc())
            raise

    def __getitem__(self, key):
        return dict.__getitem__(self, key)

    def dump(self):
        try:
            with open(self.path, 'w') as f:
                json.dump(self, f,
                    indent=4,
                    separators=(',', ': ')
                )
        except FileNotFoundError:
            logger.error("DNSRecords.dump(): There is no DNS Record file.")
            raise
        except:
            logger.error(traceback.format_exc())
            raise

    def preload(self):
        try:
            with open(self.path, 'r') as f:
                self.update(json.load(f))
        except FileNotFoundError:
            logger.error("DNSRecords.preload(): There is no DNS Record file.")
            raise
        except:
            logger.error(traceback.format_exc())
            raise
