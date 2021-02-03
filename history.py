import sqlite3
from sqlite3 import Error

history_table = """ CREATE TABLE IF NOT EXISTS history (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        user_id text NOT NULL,
                                        query text
                                    ); """
db_file = "history.db"
class History():
    def __init__(self, user_id,query):
        self.query = query
        self.id = user_id

    def save_history(self):
        conn = self.connection()
        try:
            if conn is not None:
                c = conn.cursor() 
                # c.execute(history_table)
                c.execute("SELECT COUNT(*) FROM history WHERE user_id=? and query = ?", (self.id,self.query))
                data=c.fetchone()[0]
                if data==0:
                    c.execute("INSERT INTO history (user_id,query) VALUES (?, ?);" ,(self.id,self.query))
                    conn.commit() 
                conn.close()
        except Error as e:
            print(e)

    def get_history(self):
        conn = self.connection()
        rows=None
        try:
            if conn is not None:
                c = conn.cursor() 
                # c.execute(history_table)
                c.execute("SELECT query FROM history WHERE user_id=? and query like ?", (self.id,f'%{self.query}%'))
                rowsdata = c.fetchall()
                rows=[]
                for row in rowsdata:
                    if row[0] != "":
                        rows.append(row[0])
                conn.close()
        except Error as e:
            print(e)
        return rows
    
    def connection(self):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            c = conn.cursor() 
            c.execute(history_table)
            return conn
        except Error as e:
            print(e)

        return conn

    