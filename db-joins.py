import sqlite3
import os

def get_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def db_join(cur, conn):
    cur.execute('SELECT Establishments.cities, `Establishment Count`, `Cuisine Count` FROM Establishments INNER JOIN Cuisines WHERE Establishments.cities = Cuisines.cities')
    cusine_estab_counts = cur.fetchall()
    print(cusine_estab_counts)
    conn.commit()


cur, conn = get_database('final.db')
db_join(cur, conn)