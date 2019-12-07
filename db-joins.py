import sqlite3

def get_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def db_join(cur, conn):
    cur.execute('SELECT cities, restaurants, ratings, avg_rating')



cur, conn = get_database('final.db')