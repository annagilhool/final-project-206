import sqlite3
import os
import json


def set_up_database(filename):
    # setting up database

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+filename)
    cur = conn.cursor()
    return cur, conn


def get_yelp_restaurant_data(filename):
    # reading data from restaurant json file

    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path, encoding="utf8")
    rest_data = f.read()
    f.close()
    json_rest_data = json.loads(rest_data) # now a dictionary
    return json_rest_data


def write_yelp_rating_data(rest_data, cur, conn):

    try:
        cur.execute("SELECT cities FROM `Restaurants and Ratings` ORDER BY rowid ASC")
        cities = cur.fetchall()

        city = cities[-1]
        last = city[0]
        run = False
        count = 0
        for data in rest_data['yelp_data']:

            if data['city'] == last:
                run = True
                continue

            if (run == True) and (count < 20):

                count += 1
                sql_query = "INSERT INTO `Restaurants and Ratings` (cities, restaurants, ratings, avg_rating) VALUES (?, ?, ?, ?)"
                city = data['city']
                results = data['results'] # dictionary 
                top3 = results['Top 3']
                top3 = str(top3)
                ratings = results['Ratings']
                ratings = str(ratings)

                values = (city, top3, ratings, None)
                cur.execute(sql_query, values)
        
        conn.commit()

        print("Ratings: Added 20 items after " + last)
    

    except: # empty db, put in first 20
        cur.execute("DROP TABLE IF EXISTS `Restaurants and Ratings`")

        cur.execute("CREATE TABLE `Restaurants and Ratings` (rowid INTEGER PRIMARY KEY, cities TEXT, restaurants varchar(3), ratings varchar(3), avg_rating REAL)")

        count = 0
        for data in rest_data['yelp_data']:

            if count < 20:
                count += 1
                sql_query = "INSERT INTO `Restaurants and Ratings` (rowid, cities, restaurants, ratings, avg_rating) VALUES (?, ?, ?, ?, ?)"
                city = data['city']
                results = data['results'] # dictionary 
                top3 = results['Top 3']
                top3 = str(top3)
                ratings = results['Ratings']
                ratings = str(ratings)

                values = (None, city, top3, ratings, None)
                cur.execute(sql_query, values)
        conn.commit()
        print("Ratings: Added first 20 items to db")
   

    


def write_yelp_pricing_data(rest_data, cur, conn):


    try:
        cur.execute("SELECT cities FROM `Restaurants and Pricing` ORDER BY rowid ASC")
        cities = cur.fetchall()

        city = cities[-1]
        last = city[0]
        run = False
        count = 0
        for data in rest_data['yelp_data']:

            if data['city'] == last:
                run = True
                continue

            if (run == True) and (count < 20):

                count += 1
                sql_query = "INSERT INTO `Restaurants and Pricing` (cities, restaurants, pricing, avg_rating) VALUES (?, ?, ?, ?)"
                city = data['city']
                results = data['results'] # dictionary 
                top3 = results['Top 3']
                top3 = str(top3)
                prices = results['Prices']
                prices = str(prices)

                values = (city, top3, prices, None)
                cur.execute(sql_query, values)
        
        conn.commit()

        print("Pricing: Added 20 items after " + last)
    

    except: # empty db, put in first 20
        cur.execute("DROP TABLE IF EXISTS `Restaurants and Pricing`")

        cur.execute("CREATE TABLE `Restaurants and Pricing` (rowid INTEGER PRIMARY KEY, cities TEXT, restaurants varchar(3), pricing varchar(3), avg_rating REAL)")

        count = 0
        for data in rest_data['yelp_data']:

            if count < 20:
                count += 1
                sql_query = "INSERT INTO `Restaurants and Pricing` (rowid, cities, restaurants, pricing, avg_rating) VALUES (?, ?, ?, ?, ?)"
                city = data['city']
                results = data['results'] # dictionary 
                top3 = results['Top 3']
                top3 = str(top3)
                prices = results['Prices']
                prices = str(prices)

                values = (None, city, top3, prices, None)
                cur.execute(sql_query, values)
        conn.commit()
        print("Pricing: Added first 20 items to db")




# ESTABLISHMENTS

def get_zomato_estab_data(filename):
    # reading data from zomato establishments

    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path, encoding="utf8")
    zomato_estab_data = f.read()
    f.close()
    json_estab_data = json.loads(zomato_estab_data) # now a dictionary
    return json_estab_data


def write_zomato_estab_data(estab_data, cur, conn):

    try:

        cur.execute("SELECT cities FROM Establishments ORDER BY rowid ASC")
        cities = cur.fetchall()

        city = cities[-1]
        last = city[0]
        run = False
        count = 0

        for item in estab_data['data']:

            if item['city'] == last:
                run = True
                continue

            if (run == True) and (count < 20):

                count += 1
                sql_query = "INSERT INTO Establishments (cities, establishments, `Establishment Count`) VALUES (?, ?, ?)"
                city = item['city']
                establishments = item['establishments'] # list
                establishments = str(establishments)
                values = (city, establishments, None)
                cur.execute(sql_query, values)
        conn.commit()
        print("Establishments: Added 20 items after " + last)

    except: # empty db, put in first 20
        cur.execute("DROP TABLE IF EXISTS Establishments")

        cur.execute("CREATE TABLE Establishments (rowid INTEGER PRIMARY KEY, cities TEXT, establishments TEXT, `Establishment Count` INTEGER)")

        count = 0
        for item in estab_data['data']:

            if count < 20:
                count += 1
                sql_query = "INSERT INTO Establishments (rowid, cities, establishments, `Establishment Count`) VALUES (?, ?, ?, ?)"
                city = item['city']
                establishments = item['establishments'] # list
                establishments = str(establishments)
                values = (None, city, establishments, None)
                cur.execute(sql_query, values)
        conn.commit()
        print("Establishments: Added first 20 items to db")


def get_zomato_cuisine_data(filename):
    # reading data from zomato cuisines

    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path, encoding="utf8")
    zomato_cuis_data = f.read()
    f.close()
    json_cuis_data = json.loads(zomato_cuis_data) # now a dictionary
    return json_cuis_data


def write_zomato_cuisine_data(cuis_data, cur, conn):

    # writing json zomato cuisine data 

    try:

        cur.execute("SELECT cities FROM Cuisines ORDER BY rowid ASC")
        cities = cur.fetchall()

        city = cities[-1]
        last = city[0]
        run = False
        count = 0

        for item in cuis_data['data']:

            if item['city'] == last:
                run = True
                continue

            if (run == True) and (count < 20):

                count += 1
                sql_query = "INSERT INTO Cuisines (cities, cuisines, `Cuisine Count`) VALUES (?, ?, ?)"
                city = item['city']
                cuisines = item['cuisines'] # list
                cuisines = str(cuisines)
                values = (city, cuisines, None)
                cur.execute(sql_query, values)
        conn.commit()
        print("Cuisines: Added 20 items after " + last)

    except: # empty db, put in first 20
        cur.execute("DROP TABLE IF EXISTS Cuisines")

        cur.execute("CREATE TABLE Cuisines (rowid INTEGER PRIMARY KEY, cities TEXT, cuisines TEXT, `Cuisine Count` INTEGER)")

        count = 0
        for item in cuis_data['data']:

            if count < 20:
                count += 1
                sql_query = "INSERT INTO Cuisines (rowid, cities, cuisines, `Cuisine Count`) VALUES (?, ?, ?, ?)"
                city = item['city']
                cuisines = item['cuisines'] # list
                cuisines = str(cuisines)
                values = (None, city, cuisines, None)
                cur.execute(sql_query, values)
        conn.commit()
        print("Cuisines: Added first 20 items to db")


def main():

    cur, conn = set_up_database('final.db')

    # yelp
    yelp_rest_data = get_yelp_restaurant_data('yelp-restaurant-data.json')
    write_yelp_rating_data(yelp_rest_data, cur, conn)
    write_yelp_pricing_data(yelp_rest_data, cur, conn)

    #zomato
    zomato_estab_data = get_zomato_estab_data('zomato-establishments.json')
    write_zomato_estab_data(zomato_estab_data, cur, conn)
    zomato_cuis_data = get_zomato_cuisine_data('zomato-cuisines.json')
    write_zomato_cuisine_data(zomato_cuis_data, cur, conn)

    conn.close()


if __name__ == "__main__":
    main()


