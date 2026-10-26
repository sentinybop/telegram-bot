import json
class RWcounters: #read-write counters
    def __init__(self, filename):
        self.data={}
        self.filename = filename
        self.read()
    def read(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data={}
        except json.JSONDecodeError:
            self.data={}
            self.write()
    def write(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
    def add_one(self, user_id):
        userid = str(user_id)
        count = self.data.get(userid, 0)
        count +=1
        self.data[userid] = count
        self.write()
    def count_read(self, user_id):
        userid=str(user_id)
        return self.data.get(userid, 0)