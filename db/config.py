import mariadb
import sys

config = {
    "user":"root",
    "password":"1234",
    "host":"localhost",
    "port":3307,
    "database":"aitrading_db"
}

class Database:
    def __init__(self):
        try:
            self.db = mariadb.connect(**config)
            self.cursor = self.db.cursor(dictionary=True)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        
    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def excuteOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()
        












