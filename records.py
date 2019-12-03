import json
import os

class Records:

    def __init__(self, path):
        path = os.path.expanduser(path)
        if os.path.exists(path) is False:
            print(path)
            records = {"NameServer": [], "Records": []}
			os.mknod(path, 0o644)
            self.__updateRecordsFile(path, records)
        self.records = self.__getRecords(path)

    def __updateRecordsFile(self, path, records):
        with open(path, 'w', encoding='utf8') as f:
            json.dump(records, f,
                default=True,
                ensure_ascii=False,
                indent=4,
                separators=(',', ': ')
            )

    def __getRecords(self, path):
        with open(path, 'r') as f:
            return json.load(f)
