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

        total = 0
        for r in ratings:
            # print(c)
            r = r.replace("'", "")
            r = r.strip()
            r_int = float(r)

            total += r_int
        
        avg_rating = total / 3
        avg_rating = round(avg_rating, 1)
        tup = (city, avg_rating)
        list_of_tups.append(tup)

    return list_of_tups


def get_avg_price(cur, conn):
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




def main():
    cur, conn = get_database('final.db')
    cities_and_ratings = get_avg_rating(cur, conn)
    cities_and_prices = get_avg_price(cur, conn)
    write_to_db(cur, conn, cities_and_ratings, cities_and_prices)
    conn.close()


if __name__ == "__main__":
    main()
