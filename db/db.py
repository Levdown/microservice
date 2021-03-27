import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS prices
                        (name TEXT, price REAL)""")

    def insert_values(self, name, price):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO prices (name, price) VALUES (?, ?)', [name, price])
        self.conn.commit()

    def update_price(self, name, price):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE prices SET price=? WHERE name=?", [price, name])
        self.conn.commit()

    def check_name(self, name):
        cursor = self.conn.cursor()
        name = cursor.execute("SELECT * FROM prices WHERE name=?", [name]).fetchall()
        self.conn.commit()          
        if name:
            return True
        else:
            return False           

    def get_info(self, name):
        cursor = self.conn.cursor()
        info = cursor.execute("SELECT * FROM prices WHERE name=?", [name,]).fetchall()[0]
        return info
    



