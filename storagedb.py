import sqlite3
class db:
    def __init__(self, filename):
        self.con = sqlite3.connect(filename)
        self.c = self.con.cursor()
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            count INTEGER
        );
        ''')
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS settings(
            user_id INTEGER PRIMARY KEY,
            mode TEXT
        );
        ''')
    def add_one(self, user_id):
        self.c.execute('''
        INSERT INTO users (user_id, count) VALUES (?, 1)
        ON CONFLICT(user_id) DO UPDATE SET count = count + 1;
        ''', (user_id,))
        self.con.commit()
    def count_read(self, user_id):
        self.c.execute('''
        SELECT count FROM users WHERE user_id = ?
        ''', (user_id,))
        row = self.c.fetchone()
        if row is None:
            return 0
        else:
            return row[0]
    def set_mode(self, user_id, mode):
        self.c.execute('''
        INSERT INTO settings (user_id, mode) VALUES (?, ?)
        ON CONFLICT(user_id) DO UPDATE SET mode = excluded.mode
        ''', (user_id, mode))
        self.con.commit()
    def get_mode(self, user_id):
        self.c.execute('''
        SELECT mode FROM settings WHERE user_id = ?
        ''', (user_id,))
        row = self.c.fetchone()
        if row is None:
            return 'none'
        else:
            return row[0]