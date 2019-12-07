import json
import os
import sqlite3

def get_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


def get_cuisine_count(conn, cur):
    cur.execute('SELECT cities, cuisines FROM Cuisines')
    li = cur.fetchall()
    list_of_tups = []
    # print(li)

    for item in li:
        city = item[0]

        cuisines = item[1]
        cuisines = cuisines.strip("[]")
        cuisines = list(cuisines.split(","))
        l = []
        for c in cuisines:
            # print(c)
            c = c.replace("'", "")
            c = c.strip()
            l.append(c)
        cuisine_count = len(l)
        tup = (city, cuisine_count)
        list_of_tups.append(tup)



    # li_cuisines = []
    # for entry in list_of_cuisines:
    #     entry = entry[0]
    #     entry = entry.strip("[]")
    #     entry = list(entry.split(","))
    #     cuisines = []
    #     for c in entry:
    #         # print(c)
    #         c = c.replace("'", "")
    #         c = c.strip()
    #         cuisines.append(c)
    #     li_cuisines.append(cuisines)
    # # print(li_cuisines)
    # cur.execute('SELECT cities FROM Cuisines')
    # list_of_cities = cur.fetchall()
    # # print(list_of_cities)
    # li_cities = []
    # for entry in list_of_cities:
    #     entry = entry[0]
    #     li_cities.append(entry)
    # # print(li_cities)



    for item in list_of_tups:
        count = item[1]
        city = item[0]
        cur.execute("UPDATE Cuisines SET `Cuisine Count` = ? WHERE cities = ?", (count, city))
    conn.commit()

cur, conn = get_database('final.db')
get_cuisine_count(conn, cur)