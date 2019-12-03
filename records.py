import json
import os

class Records:

    def __init__(self, path):
        path = os.path.expanduser(path)
        if os.path.exists(path) is False:
            records = {"NameServer": [], "Records": []}
<<<<<<< HEAD
            print(path)
            os.mknod(path, 0o644)
=======
			os.mknod(path, 0o644)
>>>>>>> d0d248f48a1b8e9e1e7687a2194fe6cf6c7923e0
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
