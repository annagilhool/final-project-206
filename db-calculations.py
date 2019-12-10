import json
import os
import sqlite3

def get_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


# uses SQL to gather list of cities and cuisines, then calculates the number of cuisines per city
# returns list of tuples (city, cuisine count)
# adds third column to Cuisines table with cuisine count

def get_cuisine_count(conn, cur):
    cur.execute('SELECT cities, cuisines FROM Cuisines')
    li = cur.fetchall()
    list_of_tups_cus = []

    for item in li:
        city = item[0]

        cuisines = item[1]
        cuisines = cuisines.strip("[]")
        cuisines = list(cuisines.split(","))
        l = []
        for c in cuisines:
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

# uses SQL to gather list of cities and establishments, then calculates the number of establishments per city
# returns list of tuples (city, establishment count)
# adds third column to Establishments table with establishment count

def get_establishment_count(conn, cur):
    cur.execute('SELECT cities, establishments FROM Establishments')
    li = cur.fetchall()
    list_of_tups = []

    for item in li:
        city = item[0]

        estab = item[1]
        estab = estab.strip("[]")
        estab = list(estab.split(","))
        l = []
        for e in estab:
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


# uses SQL to gather list of cities and ratings, then calculates the average rating per city
# returns list of tuples (city, average rating)
# adds fourth column to Restaurants and Ratings table with average rating

def get_avg_rating(conn, cur):
    cur.execute('SELECT cities, ratings FROM `Restaurants and Ratings`')
    li = cur.fetchall() # list of tuples  [(New York, [4.5, 4.5, 4.5])...

    list_of_tups = [] 
    for item in li:
        city = item[0]

        ratings = item[1]
        ratings = ratings.strip("[]")
        ratings = list(ratings.split(","))

        total = 0
        for r in ratings:
            r = r.replace("'", "")
            r = r.strip()
            r_int = float(r)

            total += r_int
        
        avg_rating = total / 3
        avg_rating = round(avg_rating, 1)
        tup = (city, avg_rating)
        list_of_tups.append(tup)

    return list_of_tups


# uses SQL to gather list of cities and prices, then calculates the average pricing per city
# returns list of tuples (city, average pricing)
# adds fourth column to Restaurants and Pricing table with average pricing

def get_avg_price(conn, cur):
    cur.execute('SELECT cities, pricing FROM `Restaurants and Pricing`')
    li = cur.fetchall() # list of tuples  [(New York, [2, 2, 2])...

    list_of_tups = []
    for item in li:
        city = item[0]

        prices = item[1]
        prices = prices.strip("[]")
        prices = list(prices.split(","))

        total = 0
        for p in prices:
            p = p.replace("'", "")
            p = p.strip()
            p_float = float(p)

            total += p_float
        
        avg_price = total / len(prices)
        avg_price = round(avg_price, 1)

        if avg_price <= 1:
            price = "Inexpensive"
        elif avg_price <= 2:
            price = "Moderate"
        else:
            price = "Pricey"

        tup = (city, price)
        list_of_tups.append(tup)

    return list_of_tups


def write_to_db(cur, conn, ratings, prices):

    # ratings = ('New York', 2.0)
    # prices = ('New York', 'Moderate')

    for item in ratings:
        city = item[0]
        rating = item[1]
        cur.execute("UPDATE `Restaurants and Ratings` SET avg_rating = ? WHERE cities = ?", (rating, city))
    conn.commit()

    for item in prices:
        city = item[0]
        price = item[1]
        cur.execute("UPDATE `Restaurants and Pricing` SET avg_price = ? WHERE cities = ?", (price, city))
    conn.commit()


def write_to_txt_file(filename, calc_1, calc_2, calc_3, calc_4):
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path, "a")
    f.write(str(calc_1) + "\n")
    f.write(str(calc_2) + "\n")
    f.write(str(calc_3) + "\n")
    f.write(str(calc_4) + "\n")
    f.close()


def main():

    cur, conn = get_database('final.db')
    calc1 = get_cuisine_count(conn, cur)
    calc2 = get_establishment_count(conn, cur)
    calc3 = get_avg_rating(conn, cur)
    calc4 = get_avg_price(conn, cur)

    cities_and_ratings = get_avg_rating(conn, cur)
    cities_and_prices = get_avg_price(conn, cur)
    write_to_db(cur, conn, cities_and_ratings, cities_and_prices)
    conn.close()
    write_to_txt_file("calculations.txt", calc1, calc2, calc3, calc4)


if __name__ == "__main__":
    main()