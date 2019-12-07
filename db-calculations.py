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
    list_of_tups_cus = []
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
        list_of_tups_cus.append(tup)

    for item in list_of_tups_cus:
        count = item[1]
        city = item[0]
        cur.execute("UPDATE Cuisines SET `Cuisine Count` = ? WHERE cities = ?", (count, city))
    conn.commit()

    return list_of_tups_cus

def get_establishment_count(conn, cur):
    cur.execute('SELECT cities, establishments FROM Establishments')
    li = cur.fetchall()
    list_of_tups = []
    # print(li)

    for item in li:
        city = item[0]

        estab = item[1]
        estab = estab.strip("[]")
        estab = list(estab.split(","))
        l = []
        for e in estab:
            # print(e)
            e = e.replace("'", "")
            e = e.strip()
            l.append(e)
        estab_count = len(l)
        tup = (city, estab_count)
        list_of_tups.append(tup)

    for item in list_of_tups:
        count = item[1]
        city = item[0]
        cur.execute("UPDATE Establishments SET `Establishment Count` = ? WHERE cities = ?", (count, city))
    conn.commit()

    return list_of_tups

def write_to_txt_file(filename, calc_1, calc_2):
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path, "a")
    f.write(str(calc_1) + "\n")
    f.write(str(calc_2) + "\n")
    f.close()



cur, conn = get_database('final.db')
calc1 = get_cuisine_count(conn, cur)
calc2 = get_establishment_count(conn, cur)
write_to_txt_file("calculations.txt", calc1, calc2)

