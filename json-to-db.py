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

    # creating table for cities with top 3 restaurants and ratings
    cur.execute("DROP TABLE IF EXISTS `Restaurants and Ratings`")
    cur.execute("CREATE TABLE `Restaurants and Ratings` (cities TEXT PRIMARY KEY, restaurants varchar(3), ratings varchar(3))")


    # writing json restaurant data to database for ratings 

    for data in rest_data['yelp_data']:

        sql_query = "INSERT INTO `Restaurants and Ratings` (cities, restaurants, ratings) VALUES (?, ?, ?)"
        city = data['city']
        results = data['results'] # dictionary 
        top3 = results['Top 3']
        top3 = str(top3)
        ratings = results['Ratings']
        ratings = str(ratings)

        values = (city, top3, ratings)
        cur.execute(sql_query, values)
    conn.commit()


def write_yelp_pricing_data(rest_data, cur, conn):
    # creating table for cities with top 3 restaurants and prices 
    cur.execute("DROP TABLE IF EXISTS `Restaurants and Pricing`")
    cur.execute("CREATE TABLE `Restaurants and Pricing` (cities TEXT PRIMARY KEY, restaurants varchar(3), pricing varchar(3))")

    # writing json restaurant data to database for prices 

    for data in rest_data['yelp_data']:

        sql_query = "INSERT INTO `Restaurants and Pricing` (cities, restaurants, pricing) VALUES (?, ?, ?)"
        city = data['city']
        results = data['results'] # dictionary 
        top3 = results['Top 3']
        top3 = str(top3)
        prices = results['Prices']
        prices = str(prices)

        values = (city, top3, prices)
        cur.execute(sql_query, values)
    conn.commit()


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

    # creating table for Establishments
    cur.execute("DROP TABLE IF EXISTS Establishments")
    cur.execute("CREATE TABLE Establishments (cities TEXT PRIMARY KEY, establishments TEXT)")


    # writing json zomato estab data 

    for item in estab_data['data']:

        sql_query = "INSERT INTO Establishments (cities, establishments) VALUES (?, ?)"
        city = item['city']
        establishments = item['establishments'] # list
        establishments = str(establishments)
        values = (city, establishments)
        cur.execute(sql_query, values)
    conn.commit()


def get_zomato_cuisine_data(filename):
    # reading data from zomato cuisines

    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path, encoding="utf8")
    zomato_cuis_data = f.read()
    f.close()
    json_cuis_data = json.loads(zomato_cuis_data) # now a dictionary
    return json_cuis_data


def write_zomato_cuisine_data(cuis_data, cur, conn):
    # creating table for Cuisines
    cur.execute("DROP TABLE IF EXISTS Cuisines")
    cur.execute("CREATE TABLE Cuisines (cities TEXT PRIMARY KEY, cuisines TEXT)")

    # writing json zomato cuisine data 

    for item in cuis_data['data']:

        sql_query = "INSERT INTO Cuisines (cities, cuisines) VALUES (?, ?)"
        city = item['city']
        cuisines = item['cuisines'] # list
        cuisines = str(cuisines)
        values = (city, cuisines)
        cur.execute(sql_query, values)
    conn.commit()


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


