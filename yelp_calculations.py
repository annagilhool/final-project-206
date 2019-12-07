import json
import os
import sqlite3

def get_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


def get_avg_rating(cur, conn):
    cur.execute('SELECT cities, ratings FROM `Restaurants and Ratings`')
    li = cur.fetchall() # list of tuples  [(New York, [4.5, 4.5, 4.5])...

    list_of_tups = []
    for item in li:
        city = item[0]

        ratings = item[1]
        ratings = ratings.strip("[]")
        ratings = list(ratings.split(","))
        l = []

        total = 0
        for r in ratings:
            # print(c)
            r = r.replace("'", "")
            r = r.strip()
            r_int = float(r)

            total += r_int
            l.append(r)
        
        avg_rating = total / 3
        avg_rating = round(avg_rating, 1)
        tup = (city, avg_rating)
        list_of_tups.append(tup)

    print(list_of_tups)



def main():
    cur, conn = get_database('final.db')
    get_avg_rating(cur, conn)


if __name__ == "__main__":
    main()
